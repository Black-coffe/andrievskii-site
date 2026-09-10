"""Все проверки сайта одной командой.

    .venv\\Scripts\\python.exe tests\\run.py

Поднимает настоящее приложение на свободном порту, ходит по нему обычными
запросами и гасит. Заявки уводятся во временный файл базы, телеграм
подменяется заведомо чужим — рабочая data/site.db и настоящий бот
не задеваются. Код возврата: 0 — всё прошло, 1 — есть провалы.
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tests.harness import Result, Server  # noqa: E402
from tests.suites import ALL  # noqa: E402


def main() -> int:
    result = Result()
    with tempfile.TemporaryDirectory() as tmp:
        db = Path(tmp) / "leads-test.db"
        print(f"база тестовых заявок: {db}")
        with Server(db) as server:
            print(f"сервер: {server.base}\n")
            for suite in ALL:
                suite(server, result)

    print("\n" + "-" * 60)
    if result.failed:
        print(f"провалено {len(result.failed)} из {result.passed + len(result.failed)}:")
        for line in result.failed:
            print(f"  — {line}")
        return 1
    print(f"прошло {result.passed} проверок, провалов нет")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
