"""Приложение FastAPI: серверный рендер разделов из content/ и works/.

Маршруты не пишутся по одному — они регистрируются циклом по парам
«язык × раздел», а обработчик у всех один: render_page.
"""

from __future__ import annotations

import hashlib
import hmac
import logging
import secrets
import time
from pathlib import Path
from typing import Callable

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.background import BackgroundTask

from app import config, content, leads
from app.content import ContentNotFound, SchemaError

# Токен бота и chat_id лежат в .env, который в репозиторий не входит.
config.load()

BASE_DIR = Path(__file__).resolve().parent.parent

log = logging.getLogger("andrievskii")

# Свои сообщения идут в тот же поток, что и сообщения uvicorn. Без этого
# на уровне INFO не видно строки «заявка записана», а она — то место,
# где заявка находится, если телеграм молчит.
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Русский — без префикса, остальные языки — первым сегментом пути.
# Ни поддоменов, ни параметров в адресе: язык — это папка.
LANG_PREFIX = {"ru": "", "uk": "/uk", "en": "/en"}

# Язык по умолчанию. Перевода нет — ведём сюда, и он же стоит в x-default
# для посетителя, чей язык не совпал ни с одним объявленным.
BASE_LANG = content.BASE_LANG

# rel="alternate" адресов без домена не понимает, поэтому адреса там
# абсолютные. Домен берётся из окружения, а если его там нет — из самого
# запроса: на localhost ссылки тогда тоже рабочие.
SITE_ORIGIN = config.get("SITE_ORIGIN").rstrip("/")

# Разделы из BRIEF.md. Порядок — порядок пунктов в навигации.
PAGES = ("index", "how", "works", "materials", "contact", "archive")

# Страница «спасибо». В меню её нет — на неё приходят только с формы.
# Адрес у неё отдельный намеренно: на переход ставится цель в аналитике,
# а всплывающее сообщение на той же странице целью быть не может.
THANKS = "thanks"

# Всё, у чего есть адрес и файл в content/. Меню строится только по PAGES.
ROUTED = PAGES + (THANKS,)

# Скрытое поле-ловушка: заполнено — значит, это бот.
HONEYPOT = "website"

# Скрытое поле с временем показа формы. Подпись обязательна: без неё бот
# просто поставит нужное число и пройдёт проверку.
STAMP = "at"

# Секрет для подписи метки. Не задан — случайный на время работы процесса:
# подделать метку всё равно нельзя, но форма, открытая до перезапуска,
# попросит отправить ещё раз.
FORM_SECRET = config.get("FORM_SECRET").encode() or secrets.token_bytes(32)

# Быстрее трёх секунд три поля заполняет только робот.
MIN_AGE = 3

# Сутки на открытой вкладке — метка устарела, просим отправить заново.
MAX_AGE = 24 * 60 * 60

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def page_url(lang: str, page: str) -> str:
    """Адрес раздела. index живёт в корне языка, остальные — сегментом ниже."""
    prefix = LANG_PREFIX[lang]
    return f"{prefix}/" if page == "index" else f"{prefix}/{page}"


def work_url(lang: str, slug: str) -> str:
    return f"{LANG_PREFIX[lang]}/works/{slug}"


def page_versions(page: str) -> dict[str, str]:
    """Языковые версии раздела: язык → адрес.

    Список берётся с диска: есть файл — есть версия. Переводим не всё,
    и набор переведённых разделов задаётся содержимым content/,
    а не списком в коде.
    """
    return {
        code: page_url(code, page)
        for code in LANG_PREFIX
        if content.has_page(code, page)
    }


def work_versions(slug: str) -> dict[str, str]:
    """Языковые версии одной работы. Правило то же, что у разделов."""
    return {
        code: work_url(code, slug)
        for code in LANG_PREFIX
        if content.has_work(code, slug)
    }


def absolute(request: Request, path: str) -> str:
    origin = SITE_ORIGIN or str(request.base_url).rstrip("/")
    return origin + path


def build_alternates(request: Request, versions: dict[str, str]) -> dict:
    """Блок rel="alternate" для <head>: все версии страницы и версия
    по умолчанию.

    Версия одна — блока нет вовсе: выбирать не из чего, а страница,
    объявляющая альтернативой саму себя, ничего не сообщает. Версия
    по умолчанию — русская: её получает тот, чей язык не совпал ни с одним
    объявленным.
    """
    if len(versions) < 2:
        return {"links": [], "default": None}
    default = versions.get(BASE_LANG)
    return {
        "links": [
            {"lang": code, "url": absolute(request, path)}
            for code, path in versions.items()
        ],
        "default": absolute(request, default) if default else None,
    }


def build_nav(lang: str, current: str) -> list[dict]:
    """Пункты меню.

    Подписи берутся из title разделов — в шаблоне текста нет, правится всё
    в content/{lang}/*.md. Раздела на этом языке нет («Архив» живёт только
    по-русски) — пункт не исчезает, а ведёт на русскую версию и помечается
    её языком: иначе раздел с украинской и английской страниц недостижим.
    """
    items = []
    for page in PAGES:
        source = lang if content.has_page(lang, page) else BASE_LANG
        try:
            title = content.load_page(source, page).title
        except ContentNotFound:
            continue
        items.append(
            {
                "page": page,
                "title": title,
                "url": page_url(source, page),
                "lang": source,
                "foreign": source != lang,
                "current": page == current,
            }
        )
    return items


def build_lang_links(lang: str, versions: dict[str, str]) -> list[dict]:
    """Переключатель языка в шапке: та же страница на другом языке.

    Обычные ссылки, без JavaScript, и ведут они на текущий раздел, а не
    на главную. Версии на этом языке нет — пункт остаётся, но ссылкой
    не становится: вести некуда, а придуманная пустая страница хуже,
    чем её отсутствие.
    """
    return [
        {
            "lang": code,
            "code": code.upper(),
            "url": versions.get(code),
            "current": code == lang,
        }
        for code in LANG_PREFIX
    ]


def issue_stamp() -> str:
    """Подписанная метка времени показа формы."""
    now = str(int(time.time()))
    return f"{now}.{_sign(now)}"


def check_stamp(raw: str) -> bool:
    """Метка наша, не подделана и форме больше трёх секунд?

    Подделанная подпись и слишком быстрая отправка отличаются только
    в логах — человеку в обоих случаях показывается одно и то же:
    форма с его текстом и просьбой отправить ещё раз.
    """
    stamp, _, signature = raw.partition(".")
    if not stamp.isdigit() or not signature:
        return False
    if not hmac.compare_digest(_sign(stamp), signature):
        return False
    return MIN_AGE <= int(time.time()) - int(stamp) <= MAX_AGE


def _sign(stamp: str) -> str:
    return hmac.new(FORM_SECRET, stamp.encode(), hashlib.sha256).hexdigest()


def build_action(lang: str, doc: content.Page) -> dict | None:
    """Основное действие экрана — или ничего, если раздел его не объявил."""
    if not doc.action or doc.action_to not in PAGES:
        return None
    return {"label": doc.action, "url": page_url(lang, doc.action_to)}


def render_page(
    request: Request, lang: str, page: str, form_state: dict | None = None
) -> Response:
    """Единственный обработчик раздела — общий для всех языков и адресов.

    Раздела на этом языке нет — вместо пустой страницы уходим на русскую,
    в тот же раздел. Нет и её — 404.
    """
    if not content.has_page(lang, page):
        if lang != BASE_LANG and content.has_page(BASE_LANG, page):
            return RedirectResponse(page_url(BASE_LANG, page), status_code=302)
        raise ContentNotFound(f"{lang}/{page}")

    doc = content.load_page(lang, page)
    versions = page_versions(page)

    context = {
        "lang": lang,
        "head": {"title": doc.title, "description": doc.description},
        "page": doc,
        "action": build_action(lang, doc),
        "nav": build_nav(lang, page),
        "lang_links": build_lang_links(lang, versions),
        "alternates": build_alternates(request, versions),
    }

    if doc.form:
        # Форма сама себе основное действие: кнопка отправки — единственная.
        leads.check_fields(tuple(field.name for field in doc.form.fields))
        context["action"] = None
        context["post_url"] = page_url(lang, page)
        context["honeypot"] = HONEYPOT
        context["stamp_name"] = STAMP
        context["stamp"] = issue_stamp()
        context["message"] = None
        context["values"] = {}
        context.update(form_state or {})
        return templates.TemplateResponse(
            request, "form.html", context, status_code=context.pop("status", 200)
        )

    if page == "works":
        # Действие раздела «Работы» показывается на странице работы,
        # а не над списком: основное действие списка — открыть работу.
        context["action"] = None
        # Карточка работы без перевода ведёт сразу на русский адрес
        # и помечается его языком — без промежуточного редиректа.
        context["works"] = [
            {
                "work": work,
                "url": work_url(work.lang, work.slug),
                "foreign": work.lang != lang,
            }
            for work in content.list_works(lang)
        ]
        return templates.TemplateResponse(request, "works.html", context)

    return templates.TemplateResponse(request, "page.html", context)


def render_work(request: Request, lang: str, slug: str) -> Response:
    """Одна работа: пять частей и выход на контакт.

    Действие и подпись возврата берутся из раздела «Работы» — текста
    в шаблоне нет, и действие у экрана остаётся одно.

    Перевода работы на этот язык нет — уходим на русский адрес работы,
    а не собираем страницу с чужим текстом под чужим адресом.
    """
    if not content.has_work(lang, slug):
        if lang != BASE_LANG and content.has_work(BASE_LANG, slug):
            return RedirectResponse(work_url(BASE_LANG, slug), status_code=302)
        raise ContentNotFound(f"works/{lang}/{slug}")

    work = content.load_work(slug, lang)
    versions = work_versions(slug)

    # Раздел «Работы» может быть переведён, а сама работа — нет, и наоборот.
    index_lang = lang if content.has_page(lang, "works") else BASE_LANG
    works_index = content.load_page(index_lang, "works")

    return templates.TemplateResponse(
        request,
        "work.html",
        {
            "lang": lang,
            "head": {"title": work.title, "description": work.summary},
            "work": work,
            "action": build_action(index_lang, works_index),
            "nav": build_nav(lang, "works"),
            "lang_links": build_lang_links(lang, versions),
            "alternates": build_alternates(request, versions),
            "back": {
                "title": works_index.title,
                "url": page_url(index_lang, "works"),
                "lang": index_lang,
                "foreign": index_lang != lang,
            },
        },
    )


async def submit_form(request: Request, lang: str, page: str) -> Response:
    """Приём заявки.

    Сначала строка в SQLite, потом — 303 на страницу «спасибо», и только
    после ответа, фоном, сообщение в телеграм. Порядок именно такой:
    заявка не может пропасть из-за того, что бот не ответил.
    """
    if not content.has_page(lang, page):
        raise ContentNotFound(f"{lang}/{page}")

    doc = content.load_page(lang, page)
    if not doc.form:
        raise ContentNotFound(f"{lang}/{page}: формы нет")
    leads.check_fields(tuple(field.name for field in doc.form.fields))

    posted = await request.form()
    thanks = page_url(lang, THANKS)

    # Ловушка: поле скрыто, человек его не видит и не заполняет.
    # Боту показываем ту же страницу «спасибо» — пусть считает, что вышло.
    if str(posted.get(HONEYPOT) or "").strip():
        log.warning("%s: заполнено поле-ловушка, заявка не сохранена", request.url.path)
        return RedirectResponse(thanks, status_code=303)

    values = {
        field.name: str(posted.get(field.name) or "").strip() for field in doc.form.fields
    }

    # Пустые поля — сначала: человеку важнее увидеть, чего именно не хватает.
    if not all(values.values()):
        return render_page(
            request, lang, page, {"message": doc.form.error, "values": values, "status": 422}
        )

    # Метка времени. Не сходится — форма вернётся с уже написанным текстом:
    # ни одно слово человека здесь не теряется.
    if not check_stamp(str(posted.get(STAMP) or "")):
        log.warning("%s: метка времени не прошла проверку", request.url.path)
        return render_page(
            request, lang, page, {"message": doc.form.retry, "values": values, "status": 422}
        )

    lead = leads.save(
        values,
        lang=lang,
        referrer=str(request.headers.get("referer") or "")[:500],
    )
    labels = {field.name: field.label for field in doc.form.fields}

    # Телеграм уходит фоном, уже после ответа: человек не ждёт чужой сервис,
    # а падение бота остаётся в логе и на заявку не влияет.
    return RedirectResponse(
        thanks, status_code=303, background=BackgroundTask(leads.notify, lead, labels)
    )


def _page_endpoint(lang: str, page: str) -> Callable:
    async def endpoint(request: Request) -> Response:
        return render_page(request, lang, page)

    return endpoint


def _submit_endpoint(lang: str, page: str) -> Callable:
    async def endpoint(request: Request) -> Response:
        return await submit_form(request, lang, page)

    return endpoint


def _work_endpoint(lang: str) -> Callable:
    async def endpoint(request: Request, slug: str) -> Response:
        return render_work(request, lang, slug)

    return endpoint


def _redirect_endpoint(target: str) -> Callable:
    async def endpoint(request: Request) -> Response:
        return RedirectResponse(target)

    return endpoint


def register_routes() -> None:
    for lang, prefix in LANG_PREFIX.items():
        for page in ROUTED:
            app.add_api_route(
                page_url(lang, page),
                _page_endpoint(lang, page),
                methods=["GET"],
                response_class=HTMLResponse,
                include_in_schema=False,
                name=f"{lang}-{page}",
            )

        # Приём формы — тем же адресом, что и страница: POST на /contact.
        app.add_api_route(
            page_url(lang, "contact"),
            _submit_endpoint(lang, "contact"),
            methods=["POST"],
            include_in_schema=False,
            name=f"{lang}-contact-submit",
        )

        app.add_api_route(
            f"{prefix}/works/{{slug}}",
            _work_endpoint(lang),
            methods=["GET"],
            response_class=HTMLResponse,
            include_in_schema=False,
            name=f"{lang}-work",
        )

        # /uk и /en без косой черты — на корень своего языка.
        if prefix:
            app.add_api_route(
                prefix,
                _redirect_endpoint(f"{prefix}/"),
                methods=["GET"],
                include_in_schema=False,
                name=f"{lang}-root",
            )


register_routes()

# Видно сразу при старте, а не в тот момент, когда заявка не пришла.
log.info("заявки: %s", leads.db_path())
log.info(
    "телеграм: %s",
    "настроен" if leads.configured() else "НЕ настроен — заявки будут только в базе",
)


@app.exception_handler(ContentNotFound)
async def content_not_found(request: Request, exc: ContentNotFound) -> Response:
    """Текста нет — 404, а не пустая страница.

    Оформленной страницы 404 пока нет: в BRIEF.md такого раздела нет,
    а текст для неё жил бы в шаблоне.
    """
    return PlainTextResponse("Not Found", status_code=404)


@app.exception_handler(leads.FormMismatch)
async def form_mismatch(request: Request, exc: leads.FormMismatch) -> Response:
    """Форма в контенте разошлась с таблицей заявок.

    Не 404 и не тихая форма, которую некуда сохранить: 500 с текстом,
    где сказано, какие поля объявлены и какие колонки есть в базе.
    """
    log.error("%s", exc)
    return PlainTextResponse(str(exc), status_code=500)


@app.exception_handler(SchemaError)
async def schema_error(request: Request, exc: SchemaError) -> Response:
    """Файл контента нарушает схему — страница не собирается.

    Не 404 и не молчаливый пропуск части: 500 с текстом, где сказано,
    какой файл и чего в нём не хватает. То же самое уходит в лог uvicorn.
    """
    log.error("%s", exc)
    return PlainTextResponse(str(exc), status_code=500)
