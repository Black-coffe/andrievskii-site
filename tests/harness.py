"""Обвязка тестов: поднятый сервер, запросы и счёт проверок.

Ни pytest, ни httpx: тесты ходят по настоящему приложению обычным urllib
из стандартной библиотеки. Зависимостей у проекта от этого не прибавляется,
а проверяется то же, что увидит браузер.
"""

from __future__ import annotations

import os
import re
import socket
import sqlite3
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Телеграм в тестах заведомо чужой: настоящий токен из .env сюда не попадает
# и ни одно сообщение никуда не уходит.
FAKE_TELEGRAM = {"TELEGRAM_BOT_TOKEN": "000:test-token", "TELEGRAM_CHAT_ID": "0"}


class Result:
    """Счёт проверок: что прошло, что нет."""

    def __init__(self) -> None:
        self.passed = 0
        self.failed: list[str] = []

    def check(self, name: str, ok: bool, detail: str = "") -> bool:
        line = name + (f" — {detail}" if detail else "")
        if ok:
            self.passed += 1
            print(f"  [ok]    {line}")
        else:
            self.failed.append(line)
            print(f"  [ПЛОХО] {line}")
        return ok

    def section(self, title: str) -> None:
        print(f"\n{title}")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Редиректы не следуем: важно, куда именно они ведут."""

    def redirect_request(self, *args, **kwargs):
        return None


class Server:
    """Живой uvicorn на свободном порту, со своей базой и чужим телеграмом."""

    def __init__(self, db: Path) -> None:
        self.port = _free_port()
        self.base = f"http://127.0.0.1:{self.port}"
        self.db = db
        self.process: subprocess.Popen | None = None

    def __enter__(self) -> "Server":
        env = os.environ | FAKE_TELEGRAM | {"LEADS_DB": str(self.db), "PYTHONIOENCODING": "utf-8"}
        self.process = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "app.main:app", "--port", str(self.port),
             "--log-level", "warning"],
            cwd=str(BASE_DIR),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        self._wait()
        return self

    def __exit__(self, *exc) -> None:
        if self.process:
            self.process.terminate()
            self.process.wait(timeout=10)

    def _wait(self) -> None:
        for _ in range(80):
            if self.process and self.process.poll() is not None:
                raise SystemExit("сервер не запустился, смотри вывод uvicorn")
            try:
                self.get("/")
                return
            except OSError:
                time.sleep(0.25)
        raise SystemExit("сервер не поднялся за 20 секунд")

    def get(self, path: str) -> tuple[int, str | None, str]:
        return self._open(urllib.request.Request(self.base + path))

    def post(self, path: str, data: dict, referer: str | None = None) -> tuple[int, str | None, str]:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        if referer:
            headers["Referer"] = referer
        request = urllib.request.Request(
            self.base + path, data=urllib.parse.urlencode(data).encode(), headers=headers
        )
        return self._open(request)

    def leads(self) -> list[dict]:
        if not self.db.is_file():
            return []
        db = sqlite3.connect(self.db)
        try:
            db.row_factory = sqlite3.Row
            return [dict(row) for row in db.execute("SELECT * FROM leads ORDER BY id")]
        finally:
            db.close()

    @staticmethod
    def _open(request: urllib.request.Request) -> tuple[int, str | None, str]:
        opener = urllib.request.build_opener(NoRedirect)
        try:
            with opener.open(request, timeout=20) as response:
                return response.status, response.headers.get("Location"), response.read().decode()
        except urllib.error.HTTPError as exc:
            return exc.code, exc.headers.get("Location"), exc.read().decode()


def _free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def stamp_of(html: str) -> str:
    """Подписанная метка времени из формы."""
    match = re.search(r'name="at" value="([^"]+)"', html)
    return match.group(1) if match else ""


def page_lang(html: str) -> str:
    match = re.search(r'<html lang="([^"]+)"', html)
    return match.group(1) if match else ""


def alternates(html: str) -> dict[str, str]:
    head = html.split("</head>")[0]
    return dict(re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">', head))


def switcher(html: str) -> dict[str, str]:
    """Переключатель языка: код языка → адрес, «—» если это не ссылка."""
    block = html.split("</header>")[0].split("<nav>")[2]
    out = {}
    for code in ("ru", "uk", "en"):
        link = re.search(r'<a href="([^"]+)"[^>]*>' + code.upper() + r"</a>", block)
        out[code] = link.group(1) if link else "—"
    return out
