"""Приложение FastAPI: серверный рендер разделов из content/ и works/.

Маршруты не пишутся по одному — они регистрируются циклом по парам
«язык × раздел», а обработчик у всех один: render_page.
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import content
from app.content import ContentNotFound, SchemaError

BASE_DIR = Path(__file__).resolve().parent.parent

log = logging.getLogger("andrievskii")

# Русский — без префикса, остальные языки — первым сегментом пути.
LANG_PREFIX = {"ru": "", "uk": "/uk", "en": "/en"}

# Разделы из BRIEF.md. Порядок — порядок пунктов в навигации.
PAGES = ("index", "how", "works", "materials", "contact", "archive")

# Заявки с формы. Файл, а не почта: без внешних сервисов ничего не теряется.
SUBMISSIONS = BASE_DIR / "data" / "contact.jsonl"

# Скрытое поле-ловушка: заполнено — значит, это бот.
HONEYPOT = "website"

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


def page_url(lang: str, page: str) -> str:
    """Адрес раздела. index живёт в корне языка, остальные — сегментом ниже."""
    prefix = LANG_PREFIX[lang]
    return f"{prefix}/" if page == "index" else f"{prefix}/{page}"


def work_url(lang: str, slug: str) -> str:
    return f"{LANG_PREFIX[lang]}/works/{slug}"


def build_nav(lang: str, current: str) -> list[dict]:
    """Пункты меню.

    Подписи берутся из title разделов текущего языка — в шаблоне текста нет,
    правится всё в content/{lang}/*.md. Раздела без файла в меню не будет.
    """
    items = []
    for page in PAGES:
        try:
            title = content.load_page(lang, page).title
        except ContentNotFound:
            continue
        items.append(
            {"page": page, "title": title, "url": page_url(lang, page), "current": page == current}
        )
    return items


def build_lang_links(lang: str, path: str) -> list[dict]:
    """Переключатель языков: тот же раздел на других языках."""
    return [
        {
            "lang": code,
            "code": code.upper(),
            "url": f"{prefix}{path}" if path else f"{prefix}/",
            "current": code == lang,
        }
        for code, prefix in LANG_PREFIX.items()
    ]


def build_action(lang: str, doc: content.Page) -> dict | None:
    """Основное действие экрана — или ничего, если раздел его не объявил."""
    if not doc.action or doc.action_to not in PAGES:
        return None
    return {"label": doc.action, "url": page_url(lang, doc.action_to)}


def render_page(
    request: Request, lang: str, page: str, form_state: dict | None = None
) -> Response:
    """Единственный обработчик раздела — общий для всех языков и адресов."""
    doc = content.load_page(lang, page)
    path = "" if page == "index" else f"/{page}"

    context = {
        "lang": lang,
        "head": {"title": doc.title, "description": doc.description},
        "page": doc,
        "action": build_action(lang, doc),
        "nav": build_nav(lang, page),
        "lang_links": build_lang_links(lang, path),
    }

    if doc.form:
        # Форма сама себе основное действие: кнопка отправки — единственная.
        context["action"] = None
        context["post_url"] = page_url(lang, page)
        context["sent"] = request.query_params.get("sent") == "1"
        context["error"] = False
        context["values"] = {}
        context.update(form_state or {})
        return templates.TemplateResponse(
            request, "form.html", context, status_code=context.pop("status", 200)
        )

    if page == "works":
        # Действие раздела «Работы» показывается на странице работы,
        # а не над списком: основное действие списка — открыть работу.
        context["action"] = None
        context["works"] = [
            {"work": work, "url": work_url(lang, work.slug)}
            for work in content.list_works(lang)
        ]
        return templates.TemplateResponse(request, "works.html", context)

    return templates.TemplateResponse(request, "page.html", context)


def render_work(request: Request, lang: str, slug: str) -> Response:
    """Одна работа: пять частей и выход на контакт.

    Действие и подпись возврата берутся из раздела «Работы» — текста
    в шаблоне нет, и действие у экрана остаётся одно.
    """
    work = content.load_work(slug, lang)
    works_index = content.load_page(lang, "works")

    return templates.TemplateResponse(
        request,
        "work.html",
        {
            "lang": lang,
            "head": {"title": work.title, "description": work.summary},
            "work": work,
            "action": build_action(lang, works_index),
            "nav": build_nav(lang, "works"),
            "lang_links": build_lang_links(lang, f"/works/{slug}"),
            "back": {"title": works_index.title, "url": page_url(lang, "works")},
        },
    )


async def submit_form(request: Request, lang: str, page: str) -> Response:
    """Приём заявки.

    Заявка дописывается в data/contact.jsonl: ни почты, ни внешних сервисов,
    ничего не теряется, если письмо не ушло. IP и заголовки не пишем —
    в файле только то, что человек сам ввёл.
    """
    doc = content.load_page(lang, page)
    if not doc.form:
        raise ContentNotFound(f"{lang}/{page}: формы нет")

    posted = await request.form()
    target = page_url(lang, page)

    # Ловушка для ботов: поле скрыто, человек его не заполнит.
    if str(posted.get(HONEYPOT) or "").strip():
        return RedirectResponse(f"{target}?sent=1", status_code=303)

    values = {
        field.name: str(posted.get(field.name) or "").strip() for field in doc.form.fields
    }
    if not all(values.values()):
        return render_page(
            request,
            lang,
            page,
            {"error": True, "values": values, "status": 422},
        )

    record = {
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "lang": lang,
        "fields": values,
    }
    SUBMISSIONS.parent.mkdir(parents=True, exist_ok=True)
    with SUBMISSIONS.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")

    log.info("заявка записана: %s", SUBMISSIONS)
    return RedirectResponse(f"{target}?sent=1", status_code=303)


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
        for page in PAGES:
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


@app.exception_handler(ContentNotFound)
async def content_not_found(request: Request, exc: ContentNotFound) -> Response:
    """Текста нет — 404, а не пустая страница.

    Оформленной страницы 404 пока нет: в BRIEF.md такого раздела нет,
    а текст для неё жил бы в шаблоне.
    """
    return PlainTextResponse("Not Found", status_code=404)


@app.exception_handler(SchemaError)
async def schema_error(request: Request, exc: SchemaError) -> Response:
    """Файл контента нарушает схему — страница не собирается.

    Не 404 и не молчаливый пропуск части: 500 с текстом, где сказано,
    какой файл и чего в нём не хватает. То же самое уходит в лог uvicorn.
    """
    log.error("%s", exc)
    return PlainTextResponse(str(exc), status_code=500)
