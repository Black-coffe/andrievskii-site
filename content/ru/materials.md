---
title: "Материалы"
slug: "materials"
lang: "ru"
description: "Чек-листы, шаблоны, репозиторий — всё, что выкладывается в роликах"
---

Материалы — то, что выкладываю в описании к роликам на YouTube: чек-листы, шаблоны и код, которые можно забрать и использовать сразу.

## Ролик 6 — «Своя программа под свою боль: собираю с Claude то, чего нет в сервисах»

Ролик 6 пока не опубликован, поэтому здесь только ссылки. Ролик про метод: как довести до работы программу под свою рабочую боль вместе с Claude Code. В качестве примера результата — Recall, архив звонков с расшифровкой на своей видеокарте и поиском по смыслу. Минусы тоже показаны: Claude подписывает не того спикера, на слабой видеокарте расшифровка хуже, а на цитату без проверки полагаться нельзя.

### Что забрать

Образец результата лежит в открытом репозитории [**Black-coffe/recall**](https://github.com/Black-coffe/recall): ставь по README и разбирай как пример, а не как готовый продукт.

### Чек-лист из шести этапов

1. **Назвать свою боль.** Одна рабочая ситуация, которую не закрывает готовый сервис.
2. **Собрать с Claude по шагу.** Не всё сразу: маленький кусок, проверка, следующий.
3. **Пустить в работу.** Прогнать на настоящих данных, а не на заготовке.
4. **Поймать, где врёт.** Найти места, где результат выглядит верно, но не совпадает с источником.
5. **Сравнить с готовым и посчитать.** Что дал свой вариант и сколько он стоит в деньгах и времени.
6. **Поставить себе.** Программа живёт у тебя и работает без показа.

### Домашка

Теперь домашка. Выпиши одну свою рабочую боль, которую не закрывает готовый сервис. Поставь Recall с Claude Code как образец и попроси Claude добавить в него одну вещь под эту боль — свой источник, свой отчёт или свою подсказку. Проверь результат на трёх своих документах. Ссылка на код и чек-лист — в описании и на сайте.

---

## Ролик 5 — «LinkGuard: код написал Claude, а продажи нет»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/n9umDWm9k8A" title="LinkGuard: код написал Claude, а продажи нет" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Осенью я записал себе цифру: за полгода сервис заработал $510. Весь код написал Claude Code, 759 коммитов из 759, и это было легко. Сервис живой, деньги потерялись в другом месте. Прохожу весь путь по своим настоящим промптам через шесть шагов: идея, задачи, код, прод, деньги, продажи. Главная ошибка не в коде, а в том, что я заранее не записал стоп-цифру: сколько времени и денег, после которых бросаешь.

### Что забрать

Всё лежит в открытом репозитории [**idea-to-backlog-kit**](https://github.com/Black-coffe/idea-to-backlog-kit).

- [`README.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/README.md) — задание и порядок работы целиком.
- [`checklist.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/checklist.md) — шесть шагов ролика и домашка.
- [`spec-template.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/spec-template.md) — ТЗ на одну страницу: три человека, которые заплатят, их ответы и стоп-цифра.
- [`decomposition-prompt.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/decomposition-prompt.md) — промпт для Claude Code: из ТЗ в дерево задач, которые можно отдавать по одной.
- [`CLAUDE.md.example`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/CLAUDE.md.example) — пример `CLAUDE.md` как короткого индекса проекта.
- [`review-checklist.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/review-checklist.md) — как принимать работу Claude после каждой задачи.

### Домашка — вечер на ТЗ и дерево задач, плюс разговоры с тремя людьми

**Я сделал наоборот, а ты сделай по порядку.**

1. Назови трёх людей, которые заплатят за твою идею.
2. Спроси их.
3. Доведи идею до дерева задач.
4. Запиши стоп-цифру: сколько времени и денег, после которых бросаешь.

Напиши в комментариях к ролику, какую стоп-цифру ты себе поставил и что ответили твои трое.

---

## Ролик 4 — «Дубляж своим голосом: три способа перевести ролик с Claude Code, один бесплатный»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/IT9yzqFiF9c" title="Дубляж своим голосом: три способа перевести ролик с Claude Code, один бесплатный" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Оригинал, который мы дублируем, — [ролик 3](https://youtu.be/FA1oVqBTUeM): посмотрите его первым, чтобы сравнить оригинал и дубль. Мне писали: «говоришь на украинском, а пишешь по-русски». Справедливо. Показываю, как дублировать ролик самому: тот же голос, другой язык. Три варианта рядом, каждый можно услышать, и по каждому честная цена за ролик на 20 минут. Главная мысль: модели не нужен запрос, ей нужно рабочее место — папка с инструкцией, глоссарием и скриптами.

### Что забрать

Всё лежит в открытом репозитории [**dubbing-starter-kit**](https://github.com/Black-coffe/dubbing-starter-kit).

- [`README.md`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/README.md) — установка, запуск трёх вариантов и домашка целиком.
- [`dub.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/dub.py) — вариант A: Demucs, faster-whisper, перевод Claude по глоссарию, озвучка ElevenLabs клоном голоса, подгонка по времени. Около $0.20 за ролик на 20 минут по замеру (цена озвучки действовала по акции).
- [`eldub.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/eldub.py) — вариант B: готовый сервис ElevenLabs Dubbing API, для сравнения. От $10 до $23 за ролик на 20 минут.
- [`variant_local.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/variant_local.py) и [`tts_omnivoice.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/tts_omnivoice.py) — вариант C: всё локально и бесплатно, перевод в Ollama и голос OmniVoice. Около $0.01 за электричество, нужна видеокарта.
- [`glossary.json`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/glossary.json) — словарь терминов: что не переводить и как произносить.
- [`ab.html`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/ab.html) — страница, где дорожки переключаются каждые несколько секунд.
- [**ai-video-dubbing**](https://github.com/Black-coffe/ai-video-dubbing) — готовая программа дубляжа под свои ключи, на английском, с инструкцией и промптами для Claude Code и Codex.

### Дорожки для сравнения на слух

Один и тот же фрагмент ролика 3 длиной 3:15, дублированный тремя способами. Дорожки выровнены по громкости, чтобы громкая не казалась лучше.

- [Дорожка A](https://raw.githubusercontent.com/Black-coffe/dubbing-starter-kit/main/tracks/A.m4a) — наш конвейер `dub.py`: клон голоса, перевод по глоссарию.
- [Дорожка B](https://raw.githubusercontent.com/Black-coffe/dubbing-starter-kit/main/tracks/B.m4a) — готовый сервис, ElevenLabs Dubbing API, одна команда.
- [Дорожка C](https://raw.githubusercontent.com/Black-coffe/dubbing-starter-kit/main/tracks/C.m4a) — всё локально и бесплатно: Ollama и OmniVoice.

Веса OmniVoice (вариант C) распространяются под лицензией CC-BY-NC: только некоммерческое использование. Для озвучки монетизируемого канала C не подходит, нужна другая модель.

### Домашка — около часа

**Продублируй 30 секунд своего ролика на другой язык своим голосом и сравни результат на слух с готовым сервисом.**

1. Возьми фрагмент своего видео на 30 секунд и положи в папку вместе с описанием задачи; пусть Claude Code сначала расспросит тебя про сервисы, железо и бюджет.
2. Прогони фрагмент через конвейер, прочитай перевод глазами рядом с оригиналом и исправь то, что глоссарий не ловит.
3. Включи свою дорожку и дорожку готового сервиса, чередуя каждые 6 секунд с того же места, и запиши, какая звучит лучше и сколько стоила.

Если вы такое уже делали — напишите в комментариях, какой язык и какой вариант выбрали, и где у вас сломалось произношение.

---

## Ролик 3 — «Claude сам собирает мои рабочие документы. Показываю систему целиком»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/FA1oVqBTUeM" title="Claude сам собирает мои рабочие документы. Показываю систему целиком" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Собирать один и тот же документ руками — таблицу, отчёт, акт — привычка, а не необходимость. Claude Code умеет находить скилл по описанию и запускать нужный скрипт сам, без ручного вызова из терминала. Показываю на эталонном примере: докс-шаблон, который ломается на объединённых ячейках и двухуровневой шапке, скрипт подстановки данных и вымышленная компания «Меридиан».

### Что забрать

Всё лежит в открытом репозитории [**skills-starter-kit**](https://github.com/Black-coffe/skills-starter-kit).

- [`skill-skeleton/SKILL.md`](https://github.com/Black-coffe/skills-starter-kit/blob/main/skill-skeleton/SKILL.md) — эталонный скилл: шапка `name`/`description` и правила заполнения.
- [`skill-skeleton/templates/report-template.docx`](https://github.com/Black-coffe/skills-starter-kit/blob/main/skill-skeleton/templates/report-template.docx) — нейтральный шаблон отчёта.
- [`skill-skeleton/scripts/fill_report.py`](https://github.com/Black-coffe/skills-starter-kit/blob/main/skill-skeleton/scripts/fill_report.py) — скрипт подстановки данных в шаблон.
- [`gen/make_templates.py`](https://github.com/Black-coffe/skills-starter-kit/blob/main/gen/make_templates.py) — генератор синтетических шаблонов, детерминирован.
- [`data/shipments.csv`](https://github.com/Black-coffe/skills-starter-kit/blob/main/data/shipments.csv) — двенадцать вымышленных отгрузок компании «Меридиан» за август 2026.
- [`demo-naive/`](https://github.com/Black-coffe/skills-starter-kit/tree/main/demo-naive) — тот же нейтральный шаблон без скилла и без правил: что выходит, если просто попросить модель заполнить его.
- [`demo-break/`](https://github.com/Black-coffe/skills-starter-kit/tree/main/demo-break) — шаблон с колонтитулами, объединёнными ячейками и двухуровневой шапкой таблицы, на котором скрипт делает не то.

### Домашка — от получаса

**Возьмите документ, который делаете регулярно, положите шаблон и инструкцию в папку скилла и получите готовый файл из одной строки запроса.**

1. **Разберите `skill-skeleton/` как образец структуры** — `SKILL.md` → `templates/` → `scripts/`.
2. **Соберите свою версию**: свой шаблон, свой скрипт подстановки; данные кладите рядом со скиллом, а не внутрь его папки.
3. **Спросите обычным языком.** Не вызывайте скрипт руками — попросите Claude Code словами («собери отчёт за такой-то период из такого-то файла») и убедитесь, что он сам находит скилл по `description` и запускает нужный скрипт.

На входных данных эталон даёт шапку «Меридиан», период «август 2026», двенадцать строк в порядке CSV и итог 164 850 $ — посчитан скриптом, в CSV не хранится. Другой итог — расхождение в шаблоне или в скрипте, не в данных.

---

## Ролик 2 — «MCP с нуля: подключаю Claude к своим данным за 20 минут»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/Gk8QB-5l4ms" title="MCP с нуля: подключаю Claude к своим данным за 20 минут" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Модель умеет рассуждать и писать код, но не видит ни одного вашего файла. MCP — протокол, который это чинит. Четырнадцать минут: демо-сервер из документации, подключение и проверка вызовом, а потом задача словами — и Claude Code пишет сервер на три инструмента над двумя сотнями заказов вымышленной кофейной лавки.

### Что забрать

Всё лежит в открытом репозитории [**mcp-starter-kit**](https://github.com/Black-coffe/mcp-starter-kit).

- [`gen_orders.py`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/gen_orders.py) — генератор синтетических заказов. Детерминирован: у вас получатся ровно те же цифры, что в ролике, и ответы на пять вопросов сойдутся.
- [`data/orders.json`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/data/orders.json) — двести вымышленных заказов кофейной лавки «Три зерна». Компании не существует, данные синтетические.
- [`server-minimal/server.py`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/server-minimal/server.py) — эталонный сервер на три инструмента, короче шестидесяти строк. Берите, если не хотите писать свой.
- [`prompts/server.md`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/prompts/server.md) — та самая задача словами, которую в ролике отдают Claude Code вместо готового кода.
- [`config-example.json`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/config-example.json) — образец `.mcp.json` для регистрации сервера.

### Домашка — от двадцати минут до часа

**Поднимите минимальный MCP-сервер с одним инструментом над своей папкой и задайте Claude три вопроса, на которые он без него не отвечает.**

1. **Один инструмент, а не три.** Задача не в объёме, а в том, чтобы пройти путь целиком.
2. **Подключите его** и убедитесь, что модель его видит.
3. **Задайте три вопроса.** Результат проверяется сразу: спросили — получили точный ответ с цифрами из своих файлов, а не общие слова.

Напишите в комментариях под роликом одну вещь: какой инструмент вы сделали и на каком вопросе он сломался. Второе интереснее первого.

### Пять вопросов из ролика

Ответы вычислены генератором — запустите его у себя и получите те же.

| # | Вопрос | Ответ |
|---|---|---|
| 1 | Сколько заказов отменено? | 59 |
| 2 | Самый крупный заказ — номер и сумма? | `ORD-0083`, 185 000 |
| 3 | Что заказывала «Кофейня Полдень»? | одиннадцать заказов |
| 4 | Что в заказе `ORD-0042`? | весы кофейные, 6 шт., shipped, 7800 |
| 5 | Общая сумма за август? | 333 280 |

Пятый вопрос — самый интересный. Инструмент отдаёт строки, а складывает их модель. На двухстах заказах это работает, на двухстах тысячах строк — нет: упирается в предел размера ответа инструмента. Тогда считать должен сам инструмент, либо задача уходит в обычный скрипт.

---

## Ролик 1 — «Мой сайт не работал пять лет. Пересобираю его в портал»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/ckT8cU17QD4" title="Мой сайт не работал пять лет. Пересобираю его в портал — показываю всё" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Разбор этого самого сайта — того, что был до, — и сборка портала, который вы сейчас читаете. Двадцать две минуты: архитектура, три языка, воронка, деплой на свой сервер и место, где модель придумала про меня факты.

### Что забрать

Всё лежит в открытом репозитории [**site-audit-kit**](https://github.com/Black-coffe/site-audit-kit).

- [`audit-console.js`](https://github.com/Black-coffe/site-audit-kit/blob/main/audit-console.js) — скрипт для консоли браузера. Закрывает 8 пунктов чек-листа за две секунды: считает дубликаты блоков, действия на первом экране, формы, языковые ссылки. Ничего не отправляет наружу и ничего не меняет на странице.
- [`audit-checklist.md`](https://github.com/Black-coffe/site-audit-kit/blob/main/audit-checklist.md) — все двенадцать пунктов с объяснением, что считается провалом. Четыре из них про смысл: их не проверит никакая машина.
- [`audit-prompt.md`](https://github.com/Black-coffe/site-audit-kit/blob/main/audit-prompt.md) — если не хотите в консоль, отдайте это модели вместе со своим адресом. Промпт написан так, чтобы она не хвалила.
- [`structure-template.md`](https://github.com/Black-coffe/site-audit-kit/blob/main/structure-template.md) — шаблон структуры «после»: сначала четыре задачи, потом разделы под них, потом то, чего мы сознательно не делаем.
- [`hreflang-snippet.html`](https://github.com/Black-coffe/site-audit-kit/blob/main/hreflang-snippet.html) — рабочий блок языковых ссылок с `x-default` и правильным `uk` (не `ua` — такого кода языка не существует).

### Домашка — час работы

1. **Пройдите по чек-листу свой сайт.** Нет сайта — берите профиль в LinkedIn или на GitHub: у него ровно те же четыре задачи, и большая часть пунктов применима один в один.
2. **Соберите структуру «после» на одну страницу:** четыре задачи, под каждой раздел, у каждого раздела — куда он ведёт.
3. **Самое тяжёлое: напишите одну строку первого экрана** по схеме «я делаю то-то для тех-то, приходят с такими задачами». Если строка не пишется — дело не в сайте.

Напишите в комментариях под роликом, сколько дублей нашлось у вас. У меня их было 125, худший блок — в пятнадцати копиях.

---

Здесь собираются ссылки на репозиторий и материалы по мере выхода новых роликов.
