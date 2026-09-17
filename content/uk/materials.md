---
title: "Матеріали"
slug: "materials"
lang: "uk"
description: "Чек-листи, шаблони, репозиторій — усе, що викладається в роликах"
---

Матеріали — те, що викладаю в описі до роликів на YouTube: чек-листи, шаблони і код, які можна забрати і використати одразу.

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
