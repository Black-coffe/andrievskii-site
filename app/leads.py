"""Заявка с формы: строка в SQLite и сообщение в телеграм.

Порядок жёсткий и односторонний: сначала база, потом телеграм. База лежит
рядом, файлом; телеграм — чужой сервис за сетью, он может не ответить.
Поэтому запись в базу — часть ответа человеку, а отправка сообщения —
то, что происходит после и умеет не получиться: любая ошибка уходит в лог,
наверх не поднимается и заявку не отменяет.
"""

from __future__ import annotations

import json
import logging
import os
import sqlite3
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DB = BASE_DIR / "data" / "site.db"

# Колонки таблицы заданы жёстко, поэтому и поля формы заданы жёстко:
# переименовали поле в контенте — заявку некуда класть. Это ошибка схемы,
# и ловится она при показе формы, а не в момент отправки.
FIELDS = ("task", "deadline", "contact")

SCHEMA = """
CREATE TABLE IF NOT EXISTS leads (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    task       TEXT NOT NULL,
    deadline   TEXT NOT NULL,
    contact    TEXT NOT NULL,
    created_at TEXT NOT NULL,
    lang       TEXT NOT NULL,
    referrer   TEXT NOT NULL DEFAULT ''
)
"""

INSERT = """
INSERT INTO leads (task, deadline, contact, created_at, lang, referrer)
VALUES (?, ?, ?, ?, ?, ?)
"""

# Метод бота: адрес вида https://api.telegram.org/bot<токен>/sendMessage,
# тело — JSON, обязательны chat_id и text.
TELEGRAM_API = "https://api.telegram.org/bot{token}/sendMessage"

# sendMessage принимает 1–4096 символов, длинное сообщение он отклонит целиком.
TELEGRAM_LIMIT = 4096

# Сколько ждём телеграм. Ответ человеку уже ушёл, поэтому ждать долго
# незачем — но и рвать соединение на первой секунде не за чем.
TIMEOUT = 10

log = logging.getLogger("andrievskii")


def db_path() -> Path:
    """Файл базы. LEADS_DB уводит заявки в сторону — этим живут тесты.

    Путь берётся в момент обращения, а не при импорте: .env читается
    при старте приложения, то есть уже после того, как модуль загружен.
    """
    return Path(os.environ.get("LEADS_DB") or DEFAULT_DB)


class FormMismatch(Exception):
    """Поля формы в контенте не совпали с колонками таблицы."""


@dataclass(frozen=True)
class Lead:
    """Сохранённая заявка: то, что уже лежит в базе."""

    id: int
    values: dict[str, str]
    created_at: str
    lang: str
    referrer: str


def check_fields(names: tuple[str, ...]) -> None:
    """Сверяет поля формы с колонками таблицы.

    Форма описана в контенте, таблица — здесь. Разошлись — заявку сохранять
    некуда, и узнать об этом надо на показе страницы, а не в тот момент,
    когда человек нажал «Отправить».
    """
    if tuple(names) != FIELDS:
        raise FormMismatch(
            "поля формы («"
            + "», «".join(names)
            + "») не совпадают с колонками таблицы leads («"
            + "», «".join(FIELDS)
            + "»). Имя поля во фронтматтере — это имя колонки"
        )


def save(values: dict[str, str], lang: str, referrer: str) -> Lead:
    """Пишет заявку в data/site.db и возвращает её вместе с номером.

    Файл и таблица создаются при первой заявке: пустой базы в репозитории
    не лежит, и настраивать перед первым запуском нечего.
    """
    created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    path = db_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    db = sqlite3.connect(path)
    try:
        db.execute(SCHEMA)
        cursor = db.execute(
            INSERT,
            (
                values["task"],
                values["deadline"],
                values["contact"],
                created_at,
                lang,
                referrer,
            ),
        )
        db.commit()
        lead_id = int(cursor.lastrowid)
    finally:
        db.close()

    log.info("заявка №%s записана в %s", lead_id, path)
    return Lead(
        id=lead_id,
        values=dict(values),
        created_at=created_at,
        lang=lang,
        referrer=referrer,
    )


def notify(lead: Lead, labels: dict[str, str]) -> bool:
    """Отправляет заявку в телеграм. Возвращает, ушло ли.

    Ни одна ошибка отсюда не выходит наружу: заявка уже в базе, человеку
    уже ответили. Всё, что может пойти не так, пишется в лог — и «бот
    не настроен», и «сеть не ответила», и «телеграм отказал».
    """
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
    if not token or not chat_id:
        log.warning(
            "заявка №%s: телеграм не настроен (нет TELEGRAM_BOT_TOKEN или "
            "TELEGRAM_CHAT_ID). Заявка в базе, сообщение не отправлено",
            lead.id,
        )
        return False

    payload = json.dumps(
        {"chat_id": chat_id, "text": message(lead, labels), "disable_web_page_preview": True}
    ).encode("utf-8")
    request = urllib.request.Request(
        TELEGRAM_API.format(token=token),
        data=payload,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            answer = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        # Телеграм объясняет отказ в теле ответа — его и кладём в лог.
        detail = exc.read().decode("utf-8", "replace")[:300]
        log.error(
            "заявка №%s: телеграм отказал (%s). Заявка в базе, сообщение не ушло: %s",
            lead.id,
            exc.code,
            detail,
        )
        return False
    except (urllib.error.URLError, OSError, ValueError) as exc:
        log.error(
            "заявка №%s: телеграм недоступен (%s). Заявка в базе, сообщение не ушло",
            lead.id,
            exc,
        )
        return False

    if not answer.get("ok"):
        log.error(
            "заявка №%s: телеграм ответил отказом: %s %s. Заявка в базе",
            lead.id,
            answer.get("error_code"),
            answer.get("description"),
        )
        return False

    log.info("заявка №%s отправлена в телеграм", lead.id)
    return True


def message(lead: Lead, labels: dict[str, str]) -> str:
    """Текст сообщения.

    Подписи полей берутся из контента — те же, что человек видел в форме,
    и на том языке, на котором он писал. Разметки нет намеренно: текст
    заявки идёт как есть, и ни одна скобка в нём не ломает сообщение.
    """
    lines = [f"Заявка №{lead.id} · {lead.lang}"]
    lines += [f"{labels.get(name, name)}: {lead.values[name]}" for name in FIELDS]
    lines.append(f"Время (UTC): {lead.created_at}")
    lines.append(f"Источник: {lead.referrer or '—'}")
    return "\n".join(lines)[:TELEGRAM_LIMIT]
