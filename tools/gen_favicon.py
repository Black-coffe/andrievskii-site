"""Генератор фавикона: монограмма «А», без внешних ассетов.

Цвета — те же переменные, что тёмная тема сайта (static/css/site.css,
@media (prefers-color-scheme:dark)): фон --color-ground, буква
--color-accent. Ничего не выдумываем заново.

Буква рисуется системным Arial Bold (Pillow не читает .woff2 проекта
напрямую) — для монограммы в 16×16 это не имеет значения, различимость
проверяется здесь же, при генерации.

Запуск:
    .venv\\Scripts\\python.exe tools\\gen_favicon.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"

BG = "#0f1213"      # --color-ground, тёмная тема
FG = "#93a6ff"       # --color-accent, тёмная тема
FONT = "C:/Windows/Fonts/arialbd.ttf"

SUPERSAMPLE = 512  # рисуем крупно, потом уменьшаем — так буква не дробится


def render(size: int, radius_frac: float = 0.22) -> Image.Image:
    """Квадрат size×size: скруглённый фон + буква «А» по центру."""
    scale = SUPERSAMPLE
    img = Image.new("RGBA", (scale, scale), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    radius = int(scale * radius_frac)
    draw.rounded_rectangle([0, 0, scale - 1, scale - 1], radius=radius, fill=BG)

    font = ImageFont.truetype(FONT, int(scale * 0.62))
    text = "A"
    bbox = draw.textbbox((0, 0), text, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pos = ((scale - w) / 2 - bbox[0], (scale - h) / 2 - bbox[1])
    draw.text(pos, text, font=font, fill=FG)

    return img.resize((size, size), Image.LANCZOS)


def render_square(size: int) -> Image.Image:
    """Без скругления — для apple-touch-icon и манифеста: маску даёт ОС."""
    return render(size, radius_frac=0.0)


def main() -> None:
    STATIC.mkdir(exist_ok=True)

    # SVG — тот же рисунок, векторно.
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="{BG}"/>
  <text x="16" y="23" text-anchor="middle" font-family="Arial, sans-serif"
        font-weight="700" font-size="20" fill="{FG}">A</text>
</svg>
'''
    (STATIC / "favicon.svg").write_text(svg, encoding="utf-8")

    # ICO — набор размеров в одном файле, как ждут старые клиенты.
    sizes = (16, 32, 48)
    render(sizes[-1]).save(
        STATIC / "favicon.ico",
        format="ICO",
        sizes=[(s, s) for s in sizes],
    )

    render_square(180).save(STATIC / "apple-touch-icon.png")
    render_square(192).save(STATIC / "icon-192.png")
    render_square(512).save(STATIC / "icon-512.png")

    print("Готово:", STATIC / "favicon.svg", STATIC / "favicon.ico",
          STATIC / "apple-touch-icon.png", STATIC / "icon-192.png",
          STATIC / "icon-512.png")


if __name__ == "__main__":
    main()
