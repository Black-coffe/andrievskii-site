---
title: "Материалы"
slug: "materials"
lang: "ru"
description: "Чек-листы, шаблоны, репозиторий — всё, что выкладывается в роликах"
---

Материалы — то, что выкладываю в описании к роликам на YouTube: чек-листы, шаблоны и код, которые можно забрать и использовать сразу.

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
