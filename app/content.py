"""Чтение markdown из content/, разбор YAML-фронтматтера и схемы работы.

Модуль ничего не знает про HTTP: файла нет — поднимается ContentNotFound,
файл нарушает схему работы — WorkSchemaError. В ответы их превращает
app/main.py.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import markdown
import yaml

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
WORKS_DIR = CONTENT_DIR / "works"

# Базовый язык сайта. Перевода нет — отдаётся он, и страница честно
# помечается его lang. Работы разложены по языкам так же, как разделы:
# content/works/{lang}/{slug}.md.
BASE_LANG = "ru"

# Расширения python-markdown. smarty не включаем: он переделывает кавычки
# на английский манер, а в текстах — «ёлочки».
MARKDOWN_EXTENSIONS = ["extra", "sane_lists"]

# Имя файла приходит из URL, поэтому до похода в файловую систему проверяем,
# что в нём нет ни точек, ни слешей.
SAFE_NAME = re.compile(r"^[a-z0-9-]+$")

# Имя поля формы уходит в HTML и в файл заявок.
FIELD_NAME = re.compile(r"^[a-z][a-z0-9_]*$")
FIELD_TYPES = {"text", "textarea", "email"}

FRONTMATTER = re.compile(r"\A---\s*?\n(.*?)\n---\s*?\n?(.*)\Z", re.DOTALL)

# Заголовок части работы — строка второго уровня.
SECTION_HEADING = re.compile(r"^##\s+(.+?)\s*$", re.MULTILINE)

# Схема работы: пять частей, всегда в этом порядке. Ключ — для шаблона,
# дальше заголовок на каждом языке — то, что должно стоять в файле. Подпись
# на странице берётся из самого файла, а не отсюда: в шаблоне текста нет.
# Файл на своём языке пишется своими заголовками: русские в украинском файле
# схему не пройдут.
WORK_SECTIONS = (
    ("task", {"ru": "Задача", "uk": "Завдання", "en": "Task"}),
    ("before", {"ru": "Что было до", "uk": "Що було до", "en": "What came before"}),
    ("how", {"ru": "Как устроено", "uk": "Як влаштовано", "en": "How it's built"}),
    ("result", {"ru": "Что получилось", "uk": "Що вийшло", "en": "What worked"}),
    ("failed", {"ru": "Что не получилось", "uk": "Що не вийшло", "en": "What didn't work"}),
)

# Ключи, которые обязаны быть во фронтматтере работы. Значение может быть
# пустым — факта ещё нет, — но ключ должен стоять.
WORK_FIELDS = ("slug", "title", "client_type", "period", "stack", "summary")

# Эти поля пустыми быть не могут: без них нечего показать в карточке.
WORK_REQUIRED_VALUES = ("title", "summary")

# Часть, которой мало присутствовать — она должна быть написана.
# Остальные четыре могут пока стоять с TODO, эта — нет.
REQUIRED_BODY = {"failed"}

COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


class ContentNotFound(Exception):
    """Запрошенного файла с текстом нет."""


class SchemaError(Exception):
    """Файл контента не соответствует схеме — страницу собирать нельзя."""


class WorkSchemaError(SchemaError):
    """Файл работы не соответствует схеме."""


@dataclass(frozen=True)
class FormField:
    """Одно поле формы. Подпись — из контента, не из шаблона."""

    name: str
    label: str
    type: str


@dataclass(frozen=True)
class Form:
    """Форма раздела: поля и все её тексты.

    Подтверждения здесь нет: после отправки человек уходит на отдельную
    страницу «спасибо», и её текст живёт в её собственном файле.
    """

    fields: tuple[FormField, ...]
    submit: str
    error: str
    retry: str


@dataclass(frozen=True)
class Link:
    """Тихая ссылка рядом с формой: почта, канал. Подпись — она же адрес."""

    label: str
    href: str


@dataclass(frozen=True)
class Page:
    """Раздел сайта: метаданные из фронтматтера плюс HTML тела.

    action и action_to — основное действие экрана. Поле одно, а не список:
    двух равнозначных призывов на странице не появится по устройству.
    """

    lang: str
    slug: str
    title: str
    description: str
    updated: str | None
    action: str
    action_to: str
    form: Form | None
    links: tuple[Link, ...]
    html: str
    path: Path


@dataclass(frozen=True)
class WorkPart:
    """Одна из пяти частей работы."""

    key: str
    heading: str
    html: str


@dataclass(frozen=True)
class Work:
    """Работа: фронтматтер плюс пять частей в фиксированном порядке."""

    lang: str
    slug: str
    title: str
    client_type: str
    period: str
    stack: tuple[str, ...]
    summary: str
    parts: tuple[WorkPart, ...]
    path: Path


def load_page(lang: str, name: str) -> Page:
    """Раздел сайта: content/{lang}/{name}.md."""
    path = CONTENT_DIR / _safe(lang) / f"{_safe(name)}.md"
    meta, body = _read(path)

    updated = meta.get("updated")
    return Page(
        lang=str(meta.get("lang") or lang),
        slug=str(meta.get("slug") or name),
        title=str(meta.get("title") or ""),
        description=str(meta.get("description") or ""),
        updated=str(updated) if updated else None,
        action=str(meta.get("action") or "").strip(),
        action_to=str(meta.get("action_to") or "").strip(),
        form=_read_form(path, meta.get("form")),
        links=_read_links(path, meta.get("links")),
        html=_to_html(body),
        path=path,
    )


def load_work(slug: str, lang: str) -> Work:
    """Одна работа: content/works/{lang}/{slug}.md.

    Перевода на этот язык нет — отдаётся русский файл. Нарушение схемы —
    WorkSchemaError, а не страница без части.
    """
    slug = _safe(slug)
    path = WORKS_DIR / _safe(lang) / f"{slug}.md"
    if not path.is_file():
        lang = BASE_LANG
        path = WORKS_DIR / lang / f"{slug}.md"
    meta, body = _read(path)

    _check_fields(path, meta)

    declared = str(meta.get("slug") or slug).strip()
    if declared != slug:
        raise WorkSchemaError(
            _where(path)
            + ": slug во фронтматтере («"
            + declared
            + "») не совпадает с именем файла («"
            + slug
            + "»)"
        )

    return Work(
        lang=lang,
        slug=slug,
        title=str(meta["title"]).strip(),
        client_type=str(meta.get("client_type") or "").strip(),
        period=str(meta.get("period") or "").strip(),
        stack=tuple(str(item).strip() for item in (meta.get("stack") or [])),
        summary=str(meta["summary"]).strip(),
        parts=_split_sections(path, body, lang),
        path=path,
    )


def list_works(lang: str) -> list[Work]:
    """Все работы для списка, по алфавиту имён файлов.

    Набор работ задаёт русский каталог: перевода может не быть, а работа
    в списке быть должна. Одна работа со сломанной схемой роняет весь
    список — это и есть «страница не собирается».
    """
    slugs = {path.stem for path in (WORKS_DIR / BASE_LANG).glob("*.md")}
    slugs |= {path.stem for path in (WORKS_DIR / _safe(lang)).glob("*.md")}
    return [load_work(slug, lang) for slug in sorted(slugs)]


def has_page(lang: str, name: str) -> bool:
    """Есть ли раздел на этом языке.

    Перевода нет — нет и файла: набор языковых версий раздела задаётся
    содержимым content/, а не списком в коде.
    """
    return (CONTENT_DIR / _safe(lang) / f"{_safe(name)}.md").is_file()


def has_work(lang: str, slug: str) -> bool:
    """Есть ли работа на этом языке. То же правило, что и у разделов."""
    return (WORKS_DIR / _safe(lang) / f"{_safe(slug)}.md").is_file()


def _read_form(path: Path, raw: object) -> Form | None:
    """Разбирает блок form из фронтматтера. Нет блока — нет и формы.

    Половина формы хуже её отсутствия, поэтому неполное описание — ошибка,
    а не форма без подписи кнопки.
    """
    if raw is None:
        return None
    if not isinstance(raw, dict):
        raise SchemaError(_where(path) + ": form должен быть блоком с полями")

    missing = [key for key in ("fields", "submit", "error", "retry") if not raw.get(key)]
    if missing:
        raise SchemaError(_where(path) + ": в form нет: " + ", ".join(missing))

    if not isinstance(raw["fields"], list):
        raise SchemaError(_where(path) + ": form.fields должен быть списком")

    fields = []
    for index, item in enumerate(raw["fields"], start=1):
        if not isinstance(item, dict) or not item.get("name") or not item.get("label"):
            raise SchemaError(
                _where(path) + f": у поля формы №{index} нет name или label"
            )
        name = str(item["name"]).strip()
        if not FIELD_NAME.match(name):
            raise SchemaError(
                _where(path) + f": имя поля «{name}» — только латиница, цифры и подчёркивание"
            )
        kind = str(item.get("type") or "text").strip()
        if kind not in FIELD_TYPES:
            raise SchemaError(
                _where(path)
                + f": тип поля «{kind}» неизвестен. Допустимы: "
                + ", ".join(sorted(FIELD_TYPES))
            )
        fields.append(FormField(name=name, label=str(item["label"]).strip(), type=kind))

    return Form(
        fields=tuple(fields),
        submit=str(raw["submit"]).strip(),
        error=str(raw["error"]).strip(),
        retry=str(raw["retry"]).strip(),
    )


def _read_links(path: Path, raw: object) -> tuple[Link, ...]:
    """Разбирает блок links. Нет блока — нет и ссылок.

    Подпись ссылки — это сам адрес (почта, адрес канала), поэтому
    переводить в ней нечего и во всех языках блок одинаковый.
    """
    if raw is None:
        return ()
    if not isinstance(raw, list):
        raise SchemaError(_where(path) + ": links должен быть списком")

    links = []
    for index, item in enumerate(raw, start=1):
        if not isinstance(item, dict) or not item.get("label") or not item.get("href"):
            raise SchemaError(
                _where(path) + f": у ссылки №{index} нет label или href"
            )
        href = str(item["href"]).strip()
        if not href.startswith(("mailto:", "https://", "http://", "/")):
            raise SchemaError(
                _where(path)
                + f": адрес ссылки «{href}» непонятен. Допустимы mailto:, https://, http:// и адрес внутри сайта"
            )
        links.append(Link(label=str(item["label"]).strip(), href=href))
    return tuple(links)


def _safe(name: str) -> str:
    if not SAFE_NAME.match(name):
        raise ContentNotFound(name)
    return name


def _read(path: Path) -> tuple[dict, str]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ContentNotFound(str(path)) from exc
    return _split_frontmatter(raw)


def _to_html(body: str) -> str:
    return markdown.markdown(body, extensions=MARKDOWN_EXTENSIONS)


def _where(path: Path) -> str:
    """Путь для текста ошибки — от корня проекта, а не абсолютный."""
    try:
        return str(path.relative_to(BASE_DIR)).replace("\\", "/")
    except ValueError:
        return str(path)


def _split_frontmatter(raw: str) -> tuple[dict, str]:
    match = FRONTMATTER.match(raw.lstrip("﻿"))
    if not match:
        return {}, raw

    meta = yaml.safe_load(match.group(1)) or {}
    if not isinstance(meta, dict):
        meta = {}
    return meta, match.group(2)


def _check_fields(path: Path, meta: dict) -> None:
    missing = [field for field in WORK_FIELDS if field not in meta]
    if missing:
        raise WorkSchemaError(
            _where(path)
            + ": во фронтматтере нет полей: "
            + ", ".join(missing)
            + ". Обязательны все: "
            + ", ".join(WORK_FIELDS)
        )

    empty = [
        field for field in WORK_REQUIRED_VALUES if not str(meta.get(field) or "").strip()
    ]
    if empty:
        raise WorkSchemaError(
            _where(path) + ": пустыми быть не могут, а заполнены пусто: " + ", ".join(empty)
        )

    stack = meta.get("stack")
    if stack is not None and not isinstance(stack, list):
        raise WorkSchemaError(
            _where(path) + ": stack должен быть списком, а не " + type(stack).__name__
        )


def _headings(lang: str) -> list[str]:
    """Заголовки пяти частей на языке файла."""
    return [
        names.get(lang, names[BASE_LANG]) for _, names in WORK_SECTIONS
    ]


def _split_sections(path: Path, body: str, lang: str) -> tuple[WorkPart, ...]:
    """Режет тело на пять частей и проверяет, что все они на месте.

    Часть отсутствует, названа иначе или стоит не в том порядке — ошибка.
    Молча пропустить часть нельзя: «Что не получилось» — обязательная.
    """
    expected = _headings(lang)
    matches = list(SECTION_HEADING.finditer(body))
    found = [match.group(1).strip() for match in matches]
    normalized = [_normalize(heading) for heading in found]
    allowed = {_normalize(heading) for heading in expected}

    if not matches:
        raise WorkSchemaError(
            _where(path)
            + ": в файле нет ни одной части. Схема работы — пять частей в порядке: "
            + ", ".join(expected)
        )

    if body[: matches[0].start()].strip():
        raise WorkSchemaError(
            _where(path)
            + ": есть текст до первой части («"
            + found[0]
            + "») — он никуда не попадёт. Весь текст работы живёт внутри пяти частей"
        )

    for heading in expected:
        if _normalize(heading) not in normalized:
            raise WorkSchemaError(
                _where(path)
                + ": нет обязательной части «"
                + heading
                + "». В файле есть: "
                + (", ".join(found) or "—")
                + ". Схема работы — пять частей в порядке: "
                + ", ".join(expected)
            )

    extra = [heading for heading, key in zip(found, normalized) if key not in allowed]
    if extra:
        raise WorkSchemaError(
            _where(path)
            + ": лишние части: "
            + ", ".join(extra)
            + ". Допустимы только пять: "
            + ", ".join(expected)
        )

    if normalized != [_normalize(heading) for heading in expected]:
        raise WorkSchemaError(
            _where(path)
            + ": части идут в порядке "
            + ", ".join(found)
            + ", а должны — "
            + ", ".join(expected)
        )

    bounds = [match.start() for match in matches] + [len(body)]
    parts = []
    for index, (key, _) in enumerate(WORK_SECTIONS):
        text = body[matches[index].end() : bounds[index + 1]]
        if key in REQUIRED_BODY and not COMMENT.sub("", text).strip():
            raise WorkSchemaError(
                _where(path)
                + ": часть «"
                + found[index]
                + "» пустая — заголовок есть, текста нет. "
                + "Это обязательная часть: без неё работа не разбор, а витрина. "
                + "TODO-комментарий за текст не считается"
            )
        parts.append(WorkPart(key=key, heading=found[index], html=_to_html(text)))
    return tuple(parts)


def _normalize(heading: str) -> str:
    """Заголовки сравниваем без учёта регистра и хвостовой пунктуации."""
    return heading.strip().rstrip(".:").casefold()
