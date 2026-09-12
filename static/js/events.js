/*
 * Аналитика Statable: ровно четыре события, ничего сверх них.
 * Скрипт аналитики не загрузился — track() молча ничего не делает,
 * страница работает как обычно.
 */
(function () {
  "use strict";

  function track(name, props) {
    try {
      if (window.statable && typeof window.statable.t === "function") {
        window.statable.t(name, props);
      }
    } catch (e) {
      // Аналитика не должна ронять страницу.
    }
  }

  // Хранилище визита недоступно (приватное окно, запрет сайту) — читаем
  // как "не знаем, отправляли ли уже", пишем молча в никуда: лишняя
  // отправка события лучше мёртвой аналитики на оставшихся трёх.
  function readVisitFlag(key) {
    try {
      return sessionStorage.getItem(key);
    } catch (e) {
      return null;
    }
  }

  function writeVisitFlag(key) {
    try {
      sessionStorage.setItem(key, "1");
    } catch (e) {
      // Хранилище недоступно — событие всё равно уйдёт, просто не запомнится.
    }
  }

  // 1. yt_referral — пришли с YouTube. Раз за визит, метка ролика —
  // из utm_content или ?from=; пришли с YouTube без метки — 'none'.
  function initYtReferral() {
    var VISIT_KEY = "statable_yt_referral_sent";
    if (readVisitFlag(VISIT_KEY)) return;

    var params = new URLSearchParams(window.location.search);
    var label = params.get("utm_content") || params.get("from");

    var fromYoutube = false;
    if (document.referrer) {
      try {
        var host = new URL(document.referrer).hostname;
        fromYoutube =
          host === "youtube.com" ||
          host.endsWith(".youtube.com") ||
          host === "youtu.be" ||
          host.endsWith(".youtu.be");
      } catch (e) {
        fromYoutube = false;
      }
    }

    if (!fromYoutube && !label) return;

    writeVisitFlag(VISIT_KEY);
    track("yt_referral", { video: label || "none" });
  }

  // 2. work_read — последний блок работы («что не получилось») продержался
  // в поле зрения две секунды. Одна отправка на страницу.
  function initWorkRead() {
    var target = document.getElementById("failed");
    if (!target || !("IntersectionObserver" in window)) return;

    var article = target.closest("[data-work-slug]");
    var slug = article ? article.getAttribute("data-work-slug") : "";
    var timer = null;
    var sent = false;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (sent) return;
          if (entry.isIntersecting) {
            if (timer) return;
            timer = window.setTimeout(function () {
              sent = true;
              track("work_read", { work: slug });
              observer.disconnect();
            }, 2000);
          } else if (timer) {
            window.clearTimeout(timer);
            timer = null;
          }
        });
      },
      // Порог 0 — «блок попал в поле зрения», как и записано в задаче.
      // Половина блока не годится: блок выше двух экранов до половины
      // не покажется никогда, и событие пропадёт молча. От пролёта мимо
      // на быстрой прокрутке защищают две секунды выдержки, а не порог.
      { threshold: 0 }
    );

    observer.observe(target);
  }

  // 3. form_sent — страница «спасибо» открылась после отправки формы,
  // не клик по кнопке.
  function initFormSent() {
    var segments = window.location.pathname.split("/").filter(Boolean);
    if (segments[segments.length - 1] !== "thanks") return;
    var lang = document.documentElement.lang || "ru";
    track("form_sent", { lang: lang });
  }

  // 4. tg_click — клик по ссылке в телеграм-канал, адресно на эти ссылки,
  // не глобальный перехват кликов.
  function initTgClick() {
    var links = document.querySelectorAll('a[href^="https://t.me/"]');
    links.forEach(function (link) {
      link.addEventListener("click", function () {
        var place = "contact";
        if (link.closest("header")) {
          place = "header";
        } else if (link.closest("footer")) {
          place = "footer";
        }
        track("tg_click", { place: place });
      });
    });
  }

  // Каждый init — сам по себе: падение одного (неожиданная ошибка среды)
  // не должно останавливать остальные три, и в консоль ничего не идёт.
  function safely(init) {
    try {
      init();
    } catch (e) {
      // см. комментарий выше — тихо пропускаем.
    }
  }

  safely(initYtReferral);
  safely(initWorkRead);
  safely(initFormSent);
  safely(initTgClick);
})();
