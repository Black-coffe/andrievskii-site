"""Переменные окружения и файл .env.

Значения живут в окружении и читаются через os.environ — .env только способ
их туда положить. Читается он не один раз при старте, а по требованию:
процесс мог подняться раньше, чем файл появился или был поправлен,
и правка .env не должна требовать перезапуска сервера. `uvicorn --reload`
следит за `.py` и такую правку не замечает — из-за этого заявка однажды
молча ушла в базу без сообщения в телеграм.

Настоящее окружение сильнее файла: то, что задано снаружи, .env не перебьёт.
А то, что мы сами положили из файла, обновляется, когда файл меняется.
"""

from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

# Ключи, которые мы сами взяли из файла: только их и разрешено обновлять.
_ours: set[str] = set()

# Время правки файла на момент последнего чтения.
_seen = 0.0


def load(force: bool = False) -> bool:
    """Кладёт значения из .env в окружение. Возвращает, читался ли файл.

    Файл не изменился с прошлого раза — ничего не делаем: вызывать можно
    сколько угодно часто.
    """
    global _seen

    if not ENV_FILE.is_file():
        return False

    mtime = ENV_FILE.stat().st_mtime
    if not force and mtime == _seen:
        return False

    for key, value in _parse(ENV_FILE.read_text(encoding="utf-8")).items():
        if key not in os.environ or key in _ours:
            os.environ[key] = value
            _ours.add(key)

    _seen = mtime
    return True


def get(name: str, default: str = "") -> str:
    """Значение переменной.

    Перед чтением сверяемся с .env: файл мог появиться или измениться уже
    после того, как процесс запустился. Это и есть то место, из-за которого
    заявка однажды ушла в базу без сообщения в телеграм.
    """
    load()  # дёшево: файл не менялся — ничего не делаем
    return os.environ.get(name, "").strip() or default


def _parse(raw: str) -> dict[str, str]:
    """Разбирает .env: KEY=значение, решётка — комментарий.

    Кавычки вокруг значения снимаются, пробелы по краям тоже: строка
    `TELEGRAM_CHAT_ID = "123" ` и строка `TELEGRAM_CHAT_ID=123` — одно и то же.
    """
    values = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip().removeprefix("export ").strip()
        if not key:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key] = value
    return values
