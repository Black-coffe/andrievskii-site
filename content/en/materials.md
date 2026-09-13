---
title: "Materials"
slug: "materials"
lang: "en"
description: "Checklists, templates, a repository — everything published alongside the videos"
---

Materials are what I publish in the description of my YouTube videos: checklists, templates and code you can take and use right away.

## Video 1 — "My site sat broken for five years. Rebuilding it into a portal"

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/ckT8cU17QD4" title="My site sat broken for five years. Rebuilding it into a portal" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

The video is in Russian. It takes apart this very site — the version that came before — and rebuilds it into the portal you are reading now. Twenty-two minutes: architecture, three languages, the funnel, deploying to my own server, and the place where the model invented facts about me.

### What to take

Everything lives in the open [**site-audit-kit**](https://github.com/Black-coffe/site-audit-kit) repository.

- [`audit-console.js`](https://github.com/Black-coffe/site-audit-kit/blob/main/audit-console.js) — a browser-console script. It closes 8 of the 12 checklist items in two seconds: duplicate blocks, actions above the fold, forms, language links. It sends nothing anywhere and changes nothing on the page.
- [`audit-checklist.md`](https://github.com/Black-coffe/site-audit-kit/blob/main/audit-checklist.md) — all twelve items, each with what counts as a failure. Four of them are about meaning, and no machine will check those.
- [`audit-prompt.md`](https://github.com/Black-coffe/site-audit-kit/blob/main/audit-prompt.md) — if you would rather not touch the console, hand this to a model along with your URL. The prompt is written so it won't flatter you.
- [`structure-template.md`](https://github.com/Black-coffe/site-audit-kit/blob/main/structure-template.md) — the "after" structure template: four jobs first, then the sections that serve them, then what we deliberately don't build.
- [`hreflang-snippet.html`](https://github.com/Black-coffe/site-audit-kit/blob/main/hreflang-snippet.html) — a working block of language links with `x-default` and the correct `uk` (not `ua`, which isn't a language code at all).

### Homework — one hour

1. **Run your own site through the checklist.** No site? Use your LinkedIn or GitHub profile: it has exactly the same four jobs, and most items apply as-is.
2. **Write the "after" structure on a single page:** four jobs, a section under each, and where each section leads.
3. **The hard one: write the single line for your first screen** — "I do X for Y, who come to me with Z". If the line won't come, the problem isn't the site.

Tell me in the comments how many duplicates you found. I had 125, and the worst block appeared in fifteen copies.

---

Links to the repository and materials collect here as new videos come out.
