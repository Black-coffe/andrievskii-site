/**
 * Рендерит static/og-image.png (1200×630) из tools/og-image.html.
 *
 * Тот же подход, что в соседнем репозитории для кадров-врезок
 * (D:\YouTube_AI\frames\render.mjs): реальный Chrome, реальные шрифты
 * проекта — картинка выглядит так же, как сам сайт, а не приближённо.
 *
 * Запуск:
 *   node tools/gen_og_image.mjs
 */
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import puppeteer from "puppeteer-core";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PAGE = "file:///" + path.join(HERE, "og-image.html").replace(/\\/g, "/");
const OUT = path.join(HERE, "..", "static", "og-image.png");

const CHROME_CANDIDATES = [
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
  path.join(process.env.LOCALAPPDATA || "", "Google\\Chrome\\Application\\chrome.exe"),
  "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe",
];

async function findChrome() {
  for (const p of CHROME_CANDIDATES) {
    try { await fs.access(p); return p; } catch {}
  }
  throw new Error("Не нашёл Chrome. Пропишите путь в CHROME_CANDIDATES.");
}

const main = async () => {
  const exe = await findChrome();
  const browser = await puppeteer.launch({
    executablePath: exe,
    headless: "new",
    defaultViewport: { width: 1200, height: 630, deviceScaleFactor: 1 },
    args: ["--hide-scrollbars", "--force-device-scale-factor=1", "--allow-file-access-from-files"],
  });
  const page = await browser.newPage();
  await page.goto(PAGE, { waitUntil: "networkidle0" });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: OUT });
  await browser.close();
  console.log("Готово:", OUT);
};

main().catch(e => { console.error("ОШИБКА:", e.message); process.exit(1); });
