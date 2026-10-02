---
title: "Матеріали"
slug: "materials"
lang: "uk"
description: "Чек-листи, шаблони, репозиторій — усе, що викладається в роликах"
---

Матеріали — те, що викладаю в описі до роликів на YouTube: чек-листи, шаблони і код, які можна забрати і використати одразу.

## Ролик 4 — «Дубляж своїм голосом: три способи перекласти ролик із Claude Code, один безкоштовний»

Ролик 4 поки не опубліковано, тому тут лише посилання. Оригінал, який ми дублюємо, — [ролик 3](https://youtu.be/FA1oVqBTUeM): подивіться його першим, щоб порівняти оригінал і дубль. Мені писали: «говориш українською, а пишеш російською». Слушно. Показую, як дублювати ролик самому: той самий голос, інша мова. Три варіанти поруч, кожен можна почути, і по кожному чесна ціна за ролик на 20 хвилин. Головна думка: моделі не потрібен запит, їй потрібне робоче місце — тека з інструкцією, глосарієм і скриптами.

### Що забрати

Усе лежить у відкритому репозиторії [**dubbing-starter-kit**](https://github.com/Black-coffe/dubbing-starter-kit).

- [`README.md`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/README.md) — встановлення, запуск трьох варіантів і домашка повністю.
- [`dub.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/dub.py) — варіант A: Demucs, faster-whisper, переклад Claude за глосарієм, озвучення клоном голосу в ElevenLabs, підгонка за часом. Близько $0.20 за ролик на 20 хвилин за заміром (ціна озвучення діяла за акцією).
- [`eldub.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/eldub.py) — варіант B: готовий сервіс ElevenLabs Dubbing API, для порівняння. Від $10 до $23 за ролик на 20 хвилин.
- [`variant_local.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/variant_local.py) і [`tts_omnivoice.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/tts_omnivoice.py) — варіант C: усе локально й безкоштовно, переклад в Ollama і голос OmniVoice. Близько $0.01 за електрику, потрібна відеокарта.
- [`glossary.json`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/glossary.json) — словник термінів: що не перекладати і як вимовляти.
- [`ab.html`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/ab.html) — сторінка, де доріжки перемикаються кожні кілька секунд.
- [**ai-video-dubbing**](https://github.com/Black-coffe/ai-video-dubbing) — готова програма дубляжу під свої ключі, англійською, з інструкцією та промптами для Claude Code і Codex.

### Доріжки для порівняння на слух

Той самий фрагмент ролика 3 завдовжки 3:15, продубльований трьома способами. Доріжки вирівняно за гучністю, щоб гучніша не здавалася кращою.

- [Доріжка A](https://raw.githubusercontent.com/Black-coffe/dubbing-starter-kit/main/tracks/A.m4a) — наш конвеєр `dub.py`: клон голосу, переклад за глосарієм.
- [Доріжка B](https://raw.githubusercontent.com/Black-coffe/dubbing-starter-kit/main/tracks/B.m4a) — готовий сервіс, ElevenLabs Dubbing API, одна команда.
- [Доріжка C](https://raw.githubusercontent.com/Black-coffe/dubbing-starter-kit/main/tracks/C.m4a) — усе локально й безкоштовно: Ollama і OmniVoice.

Ваги OmniVoice (варіант C) поширюються за ліцензією CC-BY-NC: лише некомерційне використання. Для озвучення монетизованого каналу C не підходить, потрібна інша модель.

### Домашка — близько години

**Продубль 30 секунд свого ролика іншою мовою своїм голосом і порівняй результат на слух із готовим сервісом.**

1. Візьми фрагмент свого відео на 30 секунд і поклади в теку разом з описом завдання; нехай Claude Code спершу розпитає тебе про сервіси, залізо і бюджет.
2. Прожени фрагмент через конвеєр, прочитай переклад очима поруч з оригіналом і виправ те, чого глосарій не ловить.
3. Увімкни свою доріжку й доріжку готового сервісу, чергуючи кожні 6 секунд з того самого місця, і запиши, яка звучить краще і скільки коштувала.

Якщо ви таке вже робили — напишіть у коментарях, яку мову і який варіант обрали, і де у вас зламалася вимова.

---

## Ролик 3 — «Claude сам збирає мої робочі документи. Показую систему цілком»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/FA1oVqBTUeM" title="Claude сам збирає мої робочі документи. Показую систему цілком" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Збирати один і той самий документ руками — таблицю, звіт, акт — звичка, а не необхідність. Claude Code вміє знаходити скіл за описом і сам запускати потрібний скрипт, без ручного виклику з термінала. Показую на еталонному прикладі: docx-шаблон, що ламається на об'єднаних клітинках і дворівневій шапці, скрипт підстановки даних і вигадана компанія «Меридіан».

### Що забрати

Усе лежить у відкритому репозиторії [**skills-starter-kit**](https://github.com/Black-coffe/skills-starter-kit).

- [`skill-skeleton/SKILL.md`](https://github.com/Black-coffe/skills-starter-kit/blob/main/skill-skeleton/SKILL.md) — еталонний скіл: шапка `name`/`description` і правила заповнення.
- [`skill-skeleton/templates/report-template.docx`](https://github.com/Black-coffe/skills-starter-kit/blob/main/skill-skeleton/templates/report-template.docx) — нейтральний шаблон звіту.
- [`skill-skeleton/scripts/fill_report.py`](https://github.com/Black-coffe/skills-starter-kit/blob/main/skill-skeleton/scripts/fill_report.py) — скрипт підстановки даних у шаблон.
- [`gen/make_templates.py`](https://github.com/Black-coffe/skills-starter-kit/blob/main/gen/make_templates.py) — генератор синтетичних шаблонів, детермінований.
- [`data/shipments.csv`](https://github.com/Black-coffe/skills-starter-kit/blob/main/data/shipments.csv) — дванадцять вигаданих відвантажень компанії «Меридіан» за серпень 2026.
- [`demo-naive/`](https://github.com/Black-coffe/skills-starter-kit/tree/main/demo-naive) — той самий нейтральний шаблон без скіла і без правил: що виходить, якщо просто попросити модель заповнити його.
- [`demo-break/`](https://github.com/Black-coffe/skills-starter-kit/tree/main/demo-break) — шаблон з колонтитулами, об'єднаними клітинками і дворівневою шапкою таблиці, на якому скрипт робить не те.

### Домашка — від пів години

**Візьміть документ, який робите регулярно, покладіть шаблон та інструкцію в папку скіла і отримайте готовий файл з одного рядка запиту.**

1. **Розберіть `skill-skeleton/` як зразок структури** — `SKILL.md` → `templates/` → `scripts/`.
2. **Зберіть свою версію**: свій шаблон, свій скрипт підстановки; дані кладіть поруч зі скілом, а не всередину його папки.
3. **Запитайте звичайною мовою.** Не викликайте скрипт руками — попросіть Claude Code словами («зроби звіт за такий-то період із такого-то файлу») і переконайтеся, що він сам знаходить скіл за `description` і запускає потрібний скрипт.

На вхідних даних еталон дає шапку «Меридіан», період «серпень 2026», дванадцять рядків за порядком CSV і підсумок 164 850 $ — порахований скриптом, у CSV не зберігається. Інший підсумок означає розбіжність у шаблоні або скрипті, не в даних.

---

## Ролик 2 — «MCP з нуля: підключаю Claude до своїх даних за 20 хвилин»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/Gk8QB-5l4ms" title="MCP з нуля: підключаю Claude до своїх даних за 20 хвилин" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Модель уміє міркувати й писати код, але не бачить жодного вашого файлу. MCP — протокол, який це лагодить. Чотирнадцять хвилин: демо-сервер з документації, підключення й перевірка викликом, а далі задача словами — і Claude Code пише сервер на три інструменти над двома сотнями замовлень вигаданої кавʼярні.

### Що забрати

Усе лежить у відкритому репозиторії [**mcp-starter-kit**](https://github.com/Black-coffe/mcp-starter-kit).

- [`gen_orders.py`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/gen_orders.py) — генератор синтетичних замовлень. Детермінований: у вас вийдуть ті самі цифри, що в ролику.
- [`data/orders.json`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/data/orders.json) — двісті вигаданих замовлень кавʼярні «Три зерна». Компанії не існує, дані синтетичні.
- [`server-minimal/server.py`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/server-minimal/server.py) — еталонний сервер на три інструменти, коротший за шістдесят рядків.
- [`prompts/server.md`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/prompts/server.md) — та сама задача словами, яку в ролику віддають Claude Code замість готового коду.
- [`config-example.json`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/config-example.json) — зразок `.mcp.json` для реєстрації сервера.

### Домашка — від двадцяти хвилин до години

**Підніміть мінімальний MCP-сервер з одним інструментом над своєю текою і поставте Claude три питання, на які він без нього не відповідає.**

1. **Один інструмент, а не три.** Річ не в обсязі, а в тому, щоб пройти шлях повністю.
2. **Підключіть його** і переконайтеся, що модель його бачить.
3. **Поставте три питання.** Результат перевіряється одразу: запитали — дістали точну відповідь із цифрами зі своїх файлів, а не загальні слова.

Напишіть у коментарях під роликом одну річ: який інструмент ви зробили і на якому питанні він зламався. Друге цікавіше за перше.

---

## Ролик 1 — «Мій сайт не працював п’ять років. Перезбираю його в портал»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/ckT8cU17QD4" title="Мій сайт не працював п’ять років. Перезбираю його в портал" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Ролик російською. Розбір цього самого сайту — того, що був до, — і збирання порталу, який ви зараз читаєте. Двадцять дві хвилини: архітектура, три мови, воронка, розгортання на власний сервер і місце, де модель вигадала про мене факти.

### Що забрати

Усе лежить у відкритому репозиторії [**site-audit-kit**](https://github.com/Black-coffe/site-audit-kit).

- [`audit-console.js`](https://github.com/Black-coffe/site-audit-kit/blob/main/audit-console.js) — скрипт для консолі браузера. Закриває 8 пунктів чек-листа за дві секунди: рахує дублікати блоків, дії на першому екрані, форми, мовні посилання. Нічого не надсилає назовні й нічого не змінює на сторінці.
- [`audit-checklist.md`](https://github.com/Black-coffe/site-audit-kit/blob/main/audit-checklist.md) — усі дванадцять пунктів із поясненням, що вважається провалом. Чотири з них про сенс: їх не перевірить жодна машина.
- [`audit-prompt.md`](https://github.com/Black-coffe/site-audit-kit/blob/main/audit-prompt.md) — якщо не хочете в консоль, віддайте це моделі разом зі своєю адресою. Промпт написаний так, щоб вона не хвалила.
- [`structure-template.md`](https://github.com/Black-coffe/site-audit-kit/blob/main/structure-template.md) — шаблон структури «після»: спочатку чотири задачі, потім розділи під них, потім те, чого ми свідомо не робимо.
- [`hreflang-snippet.html`](https://github.com/Black-coffe/site-audit-kit/blob/main/hreflang-snippet.html) — робочий блок мовних посилань із `x-default` і правильним `uk` (не `ua` — такого коду мови не існує).

### Домашка — година роботи

1. **Пройдіть за чек-листом свій сайт.** Немає сайта — беріть профіль у LinkedIn або на GitHub: у нього рівно ті самі чотири задачі, і більшість пунктів застосовна один в один.
2. **Зберіть структуру «після» на одну сторінку:** чотири задачі, під кожною розділ, у кожного розділу — куди він веде.
3. **Найважче: напишіть один рядок першого екрана** за схемою «я роблю те-то для тих-то, приходять з такими задачами». Якщо рядок не пишеться — річ не в сайті.

Напишіть у коментарях під роликом, скільки дублів знайшлося у вас. У мене їх було 125, найгірший блок — у п’ятнадцяти копіях.

---

Тут збираються посилання на репозиторій і матеріали з появою нових роликів.
