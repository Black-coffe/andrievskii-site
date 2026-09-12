"""Сами проверки: контент, языки, форма, заявка.

Каждая функция получает поднятый сервер и счётчик. Проверяется то, что
обещано в README и CLAUDE.md, — и ровно теми словами: схема работы,
языковой слой, три поля формы, защита от роботов, судьба заявки.
"""

from __future__ import annotations

import logging
import os
import re
import time
from pathlib import Path

from app import content, leads
from tests.harness import Server, alternates, menu, page_lang, stamp_of, switcher

LANGS = ("ru", "uk", "en")
BASE_LANG = content.BASE_LANG
PAGES = ("index", "how", "works", "materials", "contact", "archive")
PREFIX = {"ru": "", "uk": "/uk", "en": "/en"}

# Разделы, которых на языке нет: сюда ведёт редирект на русскую версию.
UNTRANSLATED = {("uk", "archive"), ("en", "archive")}


def url_of(lang: str, page: str) -> str:
    return f"{PREFIX[lang]}/" if page == "index" else f"{PREFIX[lang]}/{page}"


def check_content(server: Server, result) -> None:
    """Контент читается и проходит схему — без единого запроса."""
    result.section("Контент и схема")

    for lang in LANGS:
        works = content.list_works(lang)
        result.check(f"{lang}: работы читаются", len(works) == 3, f"{len(works)} шт.")
        for work in works:
            headings = [part.heading for part in work.parts]
            result.check(
                f"{lang}/{work.slug}: пять частей по схеме",
                len(headings) == 5,
                ", ".join(headings),
            )
            result.check(
                f"{lang}/{work.slug}: «что не получилось» написано",
                bool(work.parts[-1].html.strip()),
            )

    for lang in LANGS:
        doc = content.load_page(lang, "contact")
        names = tuple(field.name for field in doc.form.fields)
        result.check(f"{lang}: в форме ровно три поля", names == leads.FIELDS, str(names))
        result.check(
            f"{lang}: тексты формы на месте",
            all([doc.form.submit, doc.form.error, doc.form.retry]),
        )
        result.check(f"{lang}: почта и канал рядом с формой", len(doc.links) == 2)

    result.check(
        "у «Архива» языковых версий нет",
        not content.has_page("uk", "archive") and not content.has_page("en", "archive"),
    )


def check_schema_breaks(server: Server, result) -> None:
    """Сломанный файл роняет страницу с объяснением, а не молча."""
    result.section("Схема ломается заметно")

    probe = Path("content/works/ru/probe-test.md")
    try:
        probe.write_text(
            "---\nslug: \"probe-test\"\ntitle: \"Проба\"\nclient_type: \"\"\n"
            "period: \"\"\nstack: []\nsummary: \"Проба\"\n---\n\n"
            "## Задача\n\nтекст\n\n## Что было до\n\nтекст\n\n## Как устроено\n\nтекст\n\n"
            "## Что получилось\n\nтекст\n\n## Что не получилось\n\n<!-- TODO -->\n",
            encoding="utf-8",
        )
        status, _, body = server.get("/works/probe-test")
        result.check("пустая обязательная часть — 500", status == 500, f"код {status}")
        result.check("в ответе назван файл и причина", "probe-test.md" in body and "пустая" in body)
    finally:
        probe.unlink(missing_ok=True)

    status, _, _ = server.get("/works/net-takoy")
    result.check("несуществующая работа — 404", status == 404, f"код {status}")
    status, _, _ = server.get("/uk/net-takogo-razdela")
    result.check("несуществующий раздел — 404", status == 404, f"код {status}")


def check_menu(server: Server, result) -> None:
    """Меню и заголовок главной.

    Служебное имя раздела («Первый экран») однажды просочилось в заголовок
    и в меню. Здесь проверяется, что заголовок главной говорит о деле,
    подпись в меню — короткая и своя, а в чужом меню нет русских слов.
    """
    result.section("Меню и заголовок главной")

    # Служебные слова, которых в подписях и заголовках быть не должно.
    SERVICE = ("экран", "екран", "screen")
    HOME = {"ru": "Главная", "uk": "Головна", "en": "Home"}
    ARCHIVE = {"ru": "Архив", "uk": "Архів", "en": "Archive"}

    for lang in LANGS:
        status, _, page = server.get(url_of(lang, "index"))
        result.check(f"{lang}: главная отдаётся", status == 200, f"код {status}")

        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", page, re.S).group(1).strip()
        title = re.search(r"<title>(.*?)</title>", page, re.S).group(1).strip()
        items = menu(page)
        labels = [item["label"] for item in items]

        result.check(f"{lang}: тег title повторяет h1", title == h1, f"{title!r} vs {h1!r}")
        result.check(
            f"{lang}: в h1 нет служебного имени раздела",
            not any(word in h1.lower() for word in SERVICE),
            h1,
        )
        result.check(
            f"{lang}: в меню нет служебного имени раздела",
            not any(word in " ".join(labels).lower() for word in SERVICE),
            ", ".join(labels),
        )
        result.check(
            f"{lang}: пункт главной называется «{HOME[lang]}»",
            labels[:1] == [HOME[lang]],
            ", ".join(labels[:1]),
        )
        result.check(
            f"{lang}: подпись в меню короче заголовка страницы",
            len(labels[0]) < len(h1),
            f"{labels[0]!r} vs {h1!r}",
        )
        result.check(f"{lang}: в меню все шесть разделов", len(items) == len(PAGES), str(len(items)))

        # «Архив» живёт только по-русски: подпись переводится, адрес — нет.
        archive = next(item for item in items if item["url"] == "/archive")
        result.check(
            f"{lang}: «Архив» подписан на языке читателя",
            archive["label"] == ARCHIVE[lang],
            archive["label"],
        )
        if lang == BASE_LANG:
            result.check("ru: у своего «Архива» языковых пометок нет",
                         not archive["hreflang"] and not archive["lang"])
        else:
            result.check(
                f"{lang}: «Архив» ведёт на русскую страницу и помечен hreflang",
                archive["hreflang"] == BASE_LANG,
                archive["hreflang"] or "пометки нет",
            )
            result.check(
                f"{lang}: у переведённой подписи нет чужого lang",
                not archive["lang"],
                archive["lang"],
            )

    # Поле nav разбирается строго: молча принять кривой блок нельзя.
    probe = Path(f"content/{BASE_LANG}/probe-nav.md")
    broken = (
        ('nav: 17\n', "nav числом"),
        ('nav:\n  uk: "Проба"\n', "nav без языка самого файла"),
        ('nav: "   "\n', "пустая подпись"),
    )
    try:
        for block, what in broken:
            probe.write_text(
                '---\ntitle: "Проба"\nslug: "probe-nav"\n'
                f'lang: "{BASE_LANG}"\ndescription: "Проба"\n{block}---\n\nтекст\n',
                encoding="utf-8",
            )
            try:
                content.load_page(BASE_LANG, "probe-nav")
                ok, why = False, "принято молча"
            except content.SchemaError as error:
                ok, why = "probe-nav.md" in str(error), str(error)
            result.check(f"{what} — SchemaError с именем файла", ok, why)
    finally:
        probe.unlink(missing_ok=True)


def check_languages(server: Server, result) -> None:
    """Языковой слой: alternate, переключатель, редиректы."""
    result.section("Языковые версии")

    for lang in LANGS:
        for page in PAGES:
            path = url_of(lang, page)
            status, location, html = server.get(path)

            if (lang, page) in UNTRANSLATED:
                result.check(
                    f"{path} → русская версия",
                    status == 302 and location == url_of("ru", page),
                    f"{status} → {location}",
                )
                continue

            if not result.check(f"{path} отдаётся", status == 200, f"код {status}"):
                continue
            result.check(f"{path}: язык страницы {lang}", page_lang(html) == lang)

            alts = alternates(html)
            versions = [code for code in LANGS if content.has_page(code, page)]
            if len(versions) < 2:
                result.check(f"{path}: одна версия — блока alternate нет", not alts)
                continue
            result.check(
                f"{path}: alternate на все версии и на себя",
                set(alts) == set(versions) | {"x-default"},
                ", ".join(sorted(alts)),
            )
            result.check(
                f"{path}: x-default — русская версия",
                alts["x-default"] == alts["ru"],
            )
            result.check(
                f"{path}: адреса абсолютные",
                all(url.startswith("http") for url in alts.values()),
            )

            links = switcher(html)
            for code in LANGS:
                expected = url_of(code, page) if content.has_page(code, page) else "—"
                if code == lang:
                    expected = "—"  # текущий язык — надпись, а не ссылка
                result.check(
                    f"{path}: переключатель {code.upper()} → {expected}",
                    links[code] == expected,
                    links[code],
                )

    result.section("Языковые версии работ")
    for lang in LANGS:
        for slug in ("erp-crm", "fibi", "linguard"):
            path = f"{PREFIX[lang]}/works/{slug}"
            status, _, html = server.get(path)
            result.check(f"{path} отдаётся", status == 200, f"код {status}")
            result.check(f"{path}: язык {lang}", page_lang(html) == lang)

    result.section("Взаимность ссылок")
    broken = []
    for lang in LANGS:
        for page in PAGES:
            if (lang, page) in UNTRANSLATED:
                continue
            _, _, html = server.get(url_of(lang, page))
            for code, url in alternates(html).items():
                if code == "x-default":
                    continue
                _, _, other = server.get(url.replace(server.base, ""))
                if lang not in alternates(other):
                    broken.append(f"{url_of(lang, page)} → {url}")
    result.check("каждая версия названа с обеих сторон", not broken, "; ".join(broken))

    result.section("Корни языков")
    for lang in ("uk", "en"):
        status, location, _ = server.get(PREFIX[lang])
        result.check(
            f"{PREFIX[lang]} без косой черты → {PREFIX[lang]}/",
            status in (307, 308) and location == f"{PREFIX[lang]}/",
            f"{status} → {location}",
        )


def check_form(server: Server, result) -> None:
    """Форма: три поля, отправка без JavaScript, страница «спасибо»."""
    result.section("Форма")

    status, _, html = server.get("/contact")
    fields = re.findall(r'<(?:input|textarea) id="field-(\w+)"', html)
    result.check("форма отдаётся", status == 200, f"код {status}")
    result.check("полей ровно три", fields == list(leads.FIELDS), str(fields))
    # Аналитика (Statable) грузится на каждой странице через defer-скрипты —
    # это не то же самое, что форма, зависящая от JavaScript для отправки.
    # Проверяем узкий факт: обычная форма без обработчиков на submit/кнопке.
    result.check("форма без обработчика отправки", "onsubmit=" not in html)
    result.check("кнопка без обработчика клика", "onclick=" not in html)
    result.check("ловушка на месте", 'name="website"' in html)
    result.check("метка времени подписана", "." in stamp_of(html))
    result.check("mailto рядом с формой", 'href="mailto:' in html)
    result.check("ссылка на канал", 't.me/' in html)

    before = len(server.leads())

    status, _, back = server.post(
        "/contact", {"task": "", "deadline": "", "contact": "", "at": stamp_of(html)}
    )
    result.check("пустые поля — 422", status == 422, f"код {status}")
    result.check("показано сообщение из контента", "Заполните все три поля" in back)
    result.check("заявка не записана", len(server.leads()) == before)

    status, _, back = server.post(
        "/contact",
        {"task": "быстро", "deadline": "вчера", "contact": "@fast", "at": stamp_of(html)},
    )
    result.check("отправка раньше трёх секунд — 422", status == 422, f"код {status}")
    result.check(
        "текст человека вернулся в форму",
        all(word in back for word in ("быстро", "вчера", "@fast")),
    )
    result.check("заявка не записана", len(server.leads()) == before)

    status, _, _ = server.post(
        "/contact", {"task": "a", "deadline": "b", "contact": "c", "at": "1700000000.deadbeef"}
    )
    result.check("подделанная подпись — 422", status == 422, f"код {status}")
    result.check("заявка не записана", len(server.leads()) == before)

    status, location, _ = server.post(
        "/contact",
        {"task": "a", "deadline": "b", "contact": "c", "at": stamp_of(html), "website": "spam"},
    )
    result.check(
        "ловушка: бот получает «спасибо»",
        status == 303 and location == "/thanks",
        f"{status} → {location}",
    )
    result.check("заявка не записана", len(server.leads()) == before)

    # Честная отправка: страница открыта, человек писал дольше трёх секунд.
    _, _, page = server.get("/uk/contact")
    time.sleep(3.2)
    status, location, _ = server.post(
        "/uk/contact",
        {
            "task": "Оцифрувати процес",
            "deadline": "місяць",
            "contact": "@andrii",
            "at": stamp_of(page),
        },
        referer="https://t.me/andrievskii_ai",
    )
    result.check(
        "честная отправка — 303 на «спасибо»",
        status == 303 and location == "/uk/thanks",
        f"{status} → {location}",
    )

    rows = server.leads()
    if result.check("заявка записана", len(rows) == before + 1):
        row = rows[-1]
        result.check(
            "колонки таблицы на месте",
            set(row) == {"id", "task", "deadline", "contact", "created_at", "lang", "referrer"},
            ", ".join(row),
        )
        result.check("текст заявки сохранён", row["task"] == "Оцифрувати процес")
        result.check("язык страницы записан", row["lang"] == "uk")
        result.check("источник перехода записан", row["referrer"] == "https://t.me/andrievskii_ai")

    result.section("Страница «спасибо»")
    for lang in LANGS:
        path = url_of(lang, "thanks")
        status, _, page = server.get(path)
        result.check(f"{path} отдаётся", status == 200, f"код {status}")
        result.check(f"{path}: язык {lang}", page_lang(page) == lang)
        title = re.search(r"<h1[^>]*>([^<]+)", page)
        result.check(f"{path}: в меню её нет", title and f">{title.group(1)}</a>" not in page)


def check_telegram(server: Server, result) -> None:
    """Заявка переживает недоступный и отказавший телеграм."""
    result.section("Телеграм падает — заявка цела")

    logging.disable(logging.ERROR)  # ожидаемые ошибки не засоряют вывод теста
    os.environ["LEADS_DB"] = str(server.db)

    # Настоящий .env тесту не положен: иначе «бот не настроен» превращается
    # в живое сообщение в чужой телеграм. Уводим конфиг на несуществующий файл.
    from app import config

    was = (config.ENV_FILE, config._seen, config._ours)
    config.ENV_FILE = Path(server.db).parent / "no-such.env"
    config._seen, config._ours = 0.0, set()
    values = {"task": "проверка отказа", "deadline": "нет", "contact": "@check"}
    labels = {"task": "Задача", "deadline": "Срок", "contact": "Как связаться"}
    before = len(server.leads())
    api = leads.TELEGRAM_API

    try:
        os.environ.update({"TELEGRAM_BOT_TOKEN": "000:test-token", "TELEGRAM_CHAT_ID": "0"})

        leads.TELEGRAM_API = "http://127.0.0.1:1/bot{token}/sendMessage"
        lead = leads.save(values, lang="ru", referrer="")
        result.check("сеть не ответила — notify вернул False", leads.notify(lead, labels) is False)
        result.check("заявка при этом записана", len(server.leads()) == before + 1)

        leads.TELEGRAM_API = api
        lead = leads.save(values, lang="ru", referrer="")
        result.check("телеграм отказал — notify вернул False", leads.notify(lead, labels) is False)
        result.check("заявка при этом записана", len(server.leads()) == before + 2)

        for key in ("TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID"):
            os.environ.pop(key, None)
        lead = leads.save(values, lang="ru", referrer="")
        result.check("бот не настроен — notify вернул False", leads.notify(lead, labels) is False)
        result.check("заявка при этом записана", len(server.leads()) == before + 3)

        text = leads.message(lead, labels)
        result.check("в сообщении есть номер заявки", f"№{lead.id}" in text)
        result.check("подписи полей — из контента", "Как связаться: @check" in text)
        result.check("сообщение влезает в лимит", len(text) <= leads.TELEGRAM_LIMIT)
    finally:
        leads.TELEGRAM_API = api
        config.ENV_FILE, config._seen, config._ours = was
        logging.disable(logging.NOTSET)


def check_config(server: Server, result) -> None:
    """Правка .env подхватывается без перезапуска процесса.

    Ровно та поломка, из-за которой заявка однажды ушла в базу молча:
    сервер подняли до того, как в .env появились ключи телеграма,
    а `uvicorn --reload` следит за `.py` и правку файла не заметил.
    """
    result.section("Переменные окружения")

    from app import config

    was_file, was_seen, was_ours = config.ENV_FILE, config._seen, config._ours
    probes = ("PROBE_TOKEN", "PROBE_CHAT", "PROBE_OUTER")
    keep = {name: os.environ.get(name) for name in probes}
    try:
        env = Path(server.db).parent / "probe.env"
        config.ENV_FILE, config._seen, config._ours = env, 0.0, set()
        for name in probes:
            os.environ.pop(name, None)

        # Процесс уже работает, файла ещё нет.
        result.check("переменной нет — пусто, без падения", config.get("PROBE_TOKEN") == "")

        env.write_text(
            'PROBE_TOKEN="111:secret"\n# комментарий\nPROBE_CHAT = 42\n', encoding="utf-8"
        )
        result.check("файл появился — значение читается", config.get("PROBE_TOKEN") == "111:secret")
        result.check("кавычки и пробелы сняты", config.get("PROBE_CHAT") == "42")
        result.check("комментарий переменной не стал", "# комментарий" not in os.environ)

        # Значение поправили — процесс тот же, перезапуска не было.
        time.sleep(0.02)
        env.write_text("PROBE_TOKEN=222:fixed\nPROBE_CHAT=42\n", encoding="utf-8")
        result.check(
            "правка файла видна без перезапуска",
            config.get("PROBE_TOKEN") == "222:fixed",
            config.get("PROBE_TOKEN"),
        )

        # Настоящее окружение сильнее файла.
        os.environ["PROBE_OUTER"] = "из окружения"
        env.write_text("PROBE_OUTER=из файла\n", encoding="utf-8")
        config.load(force=True)
        result.check(
            "заданное снаружи файл не перебивает", os.environ["PROBE_OUTER"] == "из окружения"
        )
    finally:
        config.ENV_FILE, config._seen, config._ours = was_file, was_seen, was_ours
        for name, value in keep.items():
            os.environ.pop(name, None)
            if value is not None:
                os.environ[name] = value

    result.check(
        "состояние телеграма спрашивается у кода, а не по факту молчания",
        isinstance(leads.configured(), bool),
    )


def check_files_clean(server: Server, result) -> None:
    """В файлах проекта нет управляющих символов.

    Появляются они не от руки, а от генерации: сорвалось экранирование —
    и в тексте вместо обратного слеша оказался звонок или возврат каретки.
    Глазами такое не видно, страница или README при этом врут.
    """
    result.section("Файлы без мусорных символов")

    allowed = {9, 10, 13}  # табуляция и перевод строки
    watched = ("*.py", "*.md", "*.html", "*.css", "*.js")
    dirty = []
    for pattern in watched:
        for path in Path(".").rglob(pattern):
            parts = set(path.parts)
            if parts & {".venv", ".git", "__pycache__", ".claude", "node_modules"}:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            bad = {ord(ch) for ch in text if ord(ch) < 32 and ord(ch) not in allowed}
            if bad:
                dirty.append(f"{path}: {sorted(bad)}")
            if chr(13) in text.replace(chr(13) + chr(10), ""):
                dirty.append(f"{path}: возврат каретки внутри строки")

    result.check("управляющих символов в файлах нет", not dirty, "; ".join(dirty[:5]))


# Событий ровно четыре, список закрыт. Появится пятое имя в events.js или
# пропадёт одно из этих — тест упадёт здесь, а не выяснится через месяц по
# пустому отчёту.
ANALYTICS_EVENTS = ("yt_referral", "work_read", "form_sent", "tg_click")


def check_analytics(server: Server, result) -> None:
    """Аналитика подключена и считает ровно четыре события.

    Само событие отправляет браузер — этого отсюда не увидеть. Зато повод
    для отправки готовит сервер: атрибут со slug работы, последний блок
    страницы, адрес «спасибо», ссылка на канал. Пропал повод — событие не
    придёт, и в отчёте это выглядит как «никто не читает», а не как поломка.
    """
    result.section("Аналитика")

    source = Path("static/js/events.js").read_text(encoding="utf-8")
    names = sorted(set(re.findall(r'track\("(\w+)"', source)))
    result.check(
        "событий ровно четыре",
        names == sorted(ANALYTICS_EVENTS),
        ", ".join(names) or "ни одного",
    )

    status, _, _ = server.get("/static/js/events.js")
    result.check("events.js отдаётся", status == 200, f"код {status}")

    _, _, html = server.get("/")
    scripts = re.findall(r"<script([^>]*)></script>", html)
    result.check("скриптов на странице ровно два", len(scripts) == 2, f"{len(scripts)} шт.")
    result.check(
        "счётчик Statable подключён с defer",
        any("defer" in tag and "statable.com" in tag for tag in scripts),
    )
    result.check(
        "events.js подключён с defer",
        any("defer" in tag and "/static/js/events.js" in tag for tag in scripts),
    )

    # work_read: slug берётся из атрибута, блок «что не получилось» — последний.
    _, _, work = server.get("/works/fibi")
    result.check('slug работы в data-work-slug', 'data-work-slug="fibi"' in work)
    sections = re.findall(r'<section id="(\w+)"', work)
    result.check(
        "последний блок работы — failed",
        sections[-1:] == ["failed"],
        ", ".join(sections) or "ни одного",
    )

    # form_sent: страница «спасибо» есть на всех трёх языках, адрес кончается
    # на thanks — по нему скрипт её и узнаёт.
    for lang in LANGS:
        path = f"{PREFIX[lang]}/thanks"
        status, _, thanks = server.get(path)
        if result.check(f"{path} отдаётся", status == 200, f"код {status}"):
            result.check(f"{path}: язык страницы {lang}", page_lang(thanks) == lang)

    # tg_click: ссылка на канал — та самая, по префиксу которой её ищет скрипт.
    _, _, contact = server.get("/contact")
    result.check("ссылка на канал на месте", 'href="https://t.me/' in contact)


def check_form_mismatch(server: Server, result) -> None:
    """Поле формы переименовали — заявку некуда класть, и это видно сразу."""
    result.section("Форма расходится с таблицей")

    path = Path("content/ru/contact.md")
    original = path.read_text(encoding="utf-8")
    try:
        path.write_text(original.replace('name: "deadline"', 'name: "srok"', 1), encoding="utf-8")
        status, _, body = server.get("/contact")
        result.check("чужое имя поля — 500", status == 500, f"код {status}")
        result.check("в ответе названы поле и колонки", "srok" in body and "leads" in body)
    finally:
        path.write_text(original, encoding="utf-8")

    status, _, _ = server.get("/contact")
    result.check("после возврата файла форма снова работает", status == 200, f"код {status}")


ALL = (
    check_content,
    check_schema_breaks,
    check_menu,
    check_languages,
    check_form,
    check_telegram,
    check_config,
    check_files_clean,
    check_analytics,
    check_form_mismatch,
)
