---
title: "Матеріали"
slug: "materials"
lang: "uk"
description: "Чек-листи, шаблони, репозиторій — усе, що викладається в роликах"
---

Матеріали — те, що викладаю в описі до роликів на YouTube: чек-листи, шаблони і код, які можна забрати і використати одразу.

## Ролик 7 — «База знань компанії: 77 документів, 14 суперечностей і 40 запитань до та після»

Ролик 7 поки не опублікований, тому тут лише посилання. Ролик про порядок, а не про інструмент: як зібрати базу знань компанії разом із Claude Code. Показано на вигаданій компанії Veltra Power: що вивантажувати, що моделі не віддавати, як знайти суперечності між документами і як перевірити результат на 40 запитаннях. Без MCP, вивантаженням у папку: 38 правильних відповідей із 40 замість 30 і нуль вигадок. Мінуси теж показано: скіл помиляється, тому кожну цитату перевіряють руками, а два запитання з 40 база так і не взяла.

### Що забрати

Комплект лежить у відкритому репозиторії [**Black-coffe/company-knowledge-kit**](https://github.com/Black-coffe/company-knowledge-kit): скіл пошуку суперечностей, правила старшинства документів, шаблон реєстру, вигадана компанія з 77 документів, міні-набір із 13 файлів і 40 контрольних запитань із ключем. Як запустити покроково — у README комплекту. Усі посилання одним постом — у [Telegram-каналі](https://t.me/andrievskii_ai).

### Чек-лист із шести кроків

1. **Вивантажити.** Папка документів лежить на диску, таблиці й PDF поруч у тексті.
2. **Перевірити вивантаження.** Знайдено секрети, персональні дані й файли, відкриті не тим, кому треба.
3. **Реєстр.** На кожен документ рядок із власником, датою і статусом.
4. **Правила старшинства.** Підписане старше за робоче; правила покладено в `CLAUDE.md` бази.
5. **Саммарі й теми.** У кожного документа коротке саммарі, вікі зібрана за темами.
6. **Замір.** Контрольні запитання з ключем, прогін до і після, стовпець «допомогло / ні».

### Домашка

Вивантаж одну свою папку документів. Запусти скіл пошуку суперечностей із комплекту. Перевір список: у кожного рядка два файли і цитата. Немає своїх документів — візьми вигадану компанію з комплекту і прожени 40 запитань; поріг — 9 із 12 пасток. Напиши в коментарях під роликом, скільки суперечностей знайшов у себе.

### Джерела

Прочитано 15.10.2026. ✅ — два незалежні джерела, ⚠️ — одне джерело, вендор про себе або препринт. У дужках — дата публікації.

1. ✅ **Д1. Підтримка клієнтів, 2023.** +14 % вирішених звернень за годину, новачкам +34 %, близько 5 тис. операторів. Brynjolfsson, Li, Raymond, «Generative AI at Work»: [NBER w31161](https://www.nber.org/papers/w31161) (квіт. 2023), [arXiv 2304.11771](https://arxiv.org/abs/2304.11771) (06.11.2024, там +15 %, інша версія), [NBER Digest](https://www.nber.org/digest/measuring-productivity-impact-generative-ai) (01.06.2023).
2. ⚠️ **Д2. Соцмережа, граф із тікетів.** Контрольований експеримент: медіана часу вирішення −28,6 %. Xu et al., SIGIR 2024: [arXiv 2404.17723](https://arxiv.org/abs/2404.17723) (26.04.2024).
3. ✅ **Д3. Сім точок відмови RAG.** Суперечності в контексті як причина помилки. Barnett et al., CAIN 2024: [arXiv 2401.05856](https://arxiv.org/abs/2401.05856) (11.01.2024).
4. ✅ **Д4. Практик на Хабрі, 2025.** На одне запитання може бути три відповіді; спершу список запитань, потім джерела; тестовий набір після кожної зміни. «Как сделать RAG для своей компании»: [Хабр](https://habr.com/ru/articles/905076/) (28.04.2025).
5. ✅ **Д5. Хостинг-провайдер, 2026.** Три версії одного документа різних років; права перевіряє код за токеном користувача; нічне перескладання повністю. Рунити: [Хабр, частина 1](https://habr.com/ru/companies/runity/articles/1014712/) (25.03.2026), [частина 2](https://habr.com/ru/companies/runity/articles/1086162/) (24.09.2026).
6. ✅ **Д6. Телеком, 2025.** Суперечності «вирішено» промптом «не змішувати версії»; застаріле позначається за хешем. МТС Web Services, «RAG своими руками»: [Хабр](https://habr.com/ru/companies/ru_mts/articles/970476/) (16.12.2025).
7. ✅ **Д7. Промисловий софт, 2026.** Документація вища за тікети; персональні дані маскуються до індексу. Цифра, «Корпоративная память как инфраструктура»: [Хабр](https://habr.com/ru/companies/zyfra/articles/1007356/) (06.03.2026).
8. ✅ **Д8. Tech-маркетплейс, Genie.** Саммарі, FAQ і ключові слова на документ; таблиці з PDF переклали в текст; золотий набір запитань від експертів. Uber: [Genie](https://www.uber.com/blog/genie-ubers-gen-ai-on-call-copilot/) (10.10.2024), [Enhanced Agentic-RAG](https://www.uber.com/blog/enhanced-agentic-rag/) (29.05.2025).
9. ⚠️ **Д9. Сервіс доставки.** Дворівнева перевірка відповіді за статтею бази; недостатність бази — коренева причина поганих відповідей. Переказ посту DoorDash, оригінал 13.08.2024 недоступний: [ZenML LLMOps Database](https://www.zenml.io/llmops-database/rag-based-dasher-support-automation-with-llm-guardrails-and-quality-monitoring) (2024).
10. ✅ **Д10. Юридичні системи, 17–33 %.** Посилання повз або відповідь не підтверджена в 17–33 % у спеціалізованих систем. Magesh et al.: [arXiv 2405.20362](https://arxiv.org/abs/2405.20362) (30.05.2024), [Stanford HAI](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries) (23.05.2024).
11. ✅ **Д11. «Відповідають, а не утримуються».** Коли даних бракує або вони суперечать одні одним, моделі частіше відповідають, ніж утримуються. Joren et al., «Sufficient Context»: [arXiv 2411.06037](https://arxiv.org/abs/2411.06037) (09.11.2024), [Google Research](https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/) (14.05.2025), [Zhang, Wu, CMC 89(1)](https://www.techscience.com/cmc/online/detail/27766) (13.08.2026).
12. ✅ **Д12. Права і вивантаження.** Копія прав в індексі старіє; у вивантаження прав немає; витік чутливого через асистента. [Azure AI Search, document-level access](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) (оновлено 17.09.2026), [AWS, secure multi-tenant RAG](https://aws.amazon.com/blogs/architecture/secure-multi-tenant-rag-with-amazon-bedrock-and-verified-permissions/) (22.06.2026), [OWASP LLM08:2025](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/), [OWASP LLM02:2025](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/) (2025).
13. ⚠️ **Д13. Де потрібен MCP.** Живий доступ потрібен, коли джерело живе, права йдуть за обліковим записом і дані не можна копіювати; MCP діє з правами користувача. Специфікація MCP 2025-11-25: [Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization), [Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Документація вендорів про себе: [Notion MCP](https://www.notion.com/help/notion-mcp) (2026), [Asana MCP](https://developers.asana.com/docs/integrating-with-asanas-mcp-server) (08.10.2026), [Atlassian MCP, README](https://github.com/atlassian/atlassian-mcp-server) (без дати), [Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/overview) (12.10.2026), [Google Workspace MCP, поки preview](https://developers.google.com/workspace/guides/configure-mcp-servers) (13.10.2026).
14. ⚠️ **Д14. Стандарт підтримки KCS v6.** Якість бази — спільний обов'язок, старе позначають заміненим, набір живий. Consortium for Service Innovation, без дати: [Practices Guide, 030](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/040/010), [050](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/050).
15. ⚠️ **Д15. «Модель веде вікі», 2026.** Ідея квітня 2026, масштаб до сотень сторінок. [Gist llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (04.04.2026), [VentureBeat](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an) (03.04.2026).
16. ✅ **Д16. Прогноз аналітиків, 2024.** Щонайменше 30 % пілотів GenAI покинуть після перевірки ідеї. Gartner, реліз 29.07.2024: [Intelligent CIO](https://www.intelligentcio.com/eu/2024/08/05/gartner-predicts-30-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025/) (05.08.2024), [THE Journal](https://thejournal.com/Articles/2024/08/06/Gartner-30-of-Gen-AI-Projects-Will-Be-Abandoned.aspx) (06.08.2024).
17. ✅ **Д17. Бенчмарки із суперечностями.** Підкладені дублі й суперечності; конфлікти — жорсткий бар'єр навіть для моделей із міркуванням. [EnterpriseRAG-Bench, arXiv 2605.05253](https://arxiv.org/abs/2605.05253) (05.05.2026), [EnterpriseRAG, arXiv 2608.11584](https://arxiv.org/abs/2608.11584) (12.08.2026).
18. ✅ **Д18. Фінтех, підтримка.** Чат-асистент закрив близько двох третин звернень, через рік компанія повернула людей через якість. [The Decoder](https://the-decoder.com/klarna-says-openais-ai-agent-does-the-work-of-700-support-agents/) (27.02.2024), [CX Dive](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-ai-chatbot/747586/) (09.05.2025).
19. ⚠️ **Д19. Препринт, 2026.** При довгому делегуванні моделі псують близько чверті вмісту. Laban, Schnabel, Neville: [arXiv 2604.15597](https://arxiv.org/abs/2604.15597) (17.04.2026).
20. ✅ **Д20. Суддя-модель любить відповідь, яка стоїть першою.** Shi et al., «Judging the Judges»: [arXiv 2406.07791](https://arxiv.org/abs/2406.07791) (12.06.2024).

Компанія, документи і запитання в демо вигадані. Замір: claude-sonnet-5-5, 15.10.2026, 40 запитань, медіана трьох прогонів.

---

## Ролик 6 — «Власна програма під свій біль: збираю з Claude те, чого немає в сервісах»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/naej9ZaDv_w" title="Своя програма під свій біль: збираю з Claude те, чого нема в сервісах" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Ролик про метод: як довести до роботи програму під свій робочий біль разом із Claude Code. Прикладом результату є Recall, архів дзвінків із розшифровкою на своїй відеокарті та пошуком за змістом. Мінуси теж показано: Claude підписує не того спікера, на слабкій відеокарті розшифровка гірша, а на цитату без перевірки покладатися не можна.

### Що забрати

Зразок результату лежить у відкритому репозиторії [**Black-coffe/recall**](https://github.com/Black-coffe/recall): став за README і розбирай як приклад, а не як готовий продукт.

### Чек-лист із шести етапів

1. **Назвати свій біль.** Одна робоча ситуація, яку не закриває готовий сервіс.
2. **Зібрати з Claude по кроку.** Не все одразу: маленький шматок, перевірка, наступний.
3. **Пустити в роботу.** Прогнати на справжніх даних, а не на заготовці.
4. **Зловити, де бреше.** Знайти місця, де результат здається правильним, але не збігається з джерелом.
5. **Порівняти з готовим і порахувати.** Що дав свій варіант і скільки він коштує в грошах і часі.
6. **Поставити собі.** Програма живе в тебе й працює без показу.

### Домашка

Тепер домашка. Випиши один свій робочий біль, який не закриває готовий сервіс. Постав Recall із Claude Code як зразок і попроси Claude додати до нього одну річ під цей біль — своє джерело, свій звіт або свою підказку. Перевір результат на трьох своїх документах. Посилання на код і чек-лист — в описі та на сайті.

---

## Ролик 5 — «LinkGuard: код написав Claude, а продажів немає»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/n9umDWm9k8A" title="LinkGuard: код написав Claude, а продажів немає" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Восени я записав собі цифру: за пів року сервіс заробив $510. Весь код написав Claude Code, 759 комітів із 759, і це було легко. Сервіс живий, гроші загубилися в іншому місці. Проходжу весь шлях своїми справжніми промптами через шість кроків: ідея, задачі, код, прод, гроші, продажі. Головна помилка не в коді, а в тому, що я заздалегідь не записав стоп-цифру: скільки часу й грошей, після яких кидаєш.

### Що забрати

Усе лежить у відкритому репозиторії [**idea-to-backlog-kit**](https://github.com/Black-coffe/idea-to-backlog-kit) (файли російською).

- [`README.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/README.md) — завдання і порядок роботи повністю.
- [`checklist.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/checklist.md) — шість кроків ролика і домашка.
- [`spec-template.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/spec-template.md) — ТЗ на одну сторінку: троє людей, які заплатять, їхні відповіді і стоп-цифра.
- [`decomposition-prompt.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/decomposition-prompt.md) — промпт для Claude Code: з ТЗ у дерево задач, які можна віддавати по одній.
- [`CLAUDE.md.example`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/CLAUDE.md.example) — приклад `CLAUDE.md` як короткого індексу проєкту.
- [`review-checklist.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/review-checklist.md) — як приймати роботу Claude після кожної задачі.

### Домашка — вечір на ТЗ і дерево задач, плюс розмови з трьома людьми

**Я зробив навпаки, а ти зроби по порядку.**

1. Назви трьох людей, які заплатять за твою ідею.
2. Запитай їх.
3. Доведи ідею до дерева задач.
4. Запиши стоп-цифру: скільки часу й грошей, після яких кидаєш.

Напиши в коментарях до ролика, яку стоп-цифру ти собі поставив і що відповіли твої троє.

---

## Ролик 4 — «Дубляж своїм голосом: три способи перекласти ролик із Claude Code, один безкоштовний»

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/IT9yzqFiF9c" title="Дубляж своїм голосом: три способи перекласти ролик із Claude Code, один безкоштовний" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Оригінал, який ми дублюємо, — [ролик 3](https://youtu.be/FA1oVqBTUeM): подивіться його першим, щоб порівняти оригінал і дубль. Мені писали: «говориш українською, а пишеш російською». Слушно. Показую, як дублювати ролик самому: той самий голос, інша мова. Три варіанти поруч, кожен можна почути, і по кожному чесна ціна за ролик на 20 хвилин. Головна думка: моделі не потрібен запит, їй потрібне робоче місце — тека з інструкцією, глосарієм і скриптами.

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
