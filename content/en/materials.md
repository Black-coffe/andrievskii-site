---
title: "Materials"
slug: "materials"
lang: "en"
description: "Checklists, templates, a repository — everything published alongside the videos"
---

Materials are what I publish in the description of my YouTube videos: checklists, templates and code you can take and use right away.

## Video 2 — "MCP from scratch: connecting Claude to my own data in 20 minutes"

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/Gk8QB-5l4ms" title="MCP from scratch: connecting Claude to my own data in 20 minutes" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

A model can reason and write code, yet it cannot see a single file of yours. MCP is the protocol that fixes this. Fourteen minutes: the demo server from the docs, wiring it up and proving it with a real call, then a task written in plain words — and Claude Code writes a three-tool server over two hundred orders of a fictional coffee shop.

### What to take

Everything sits in the open [**mcp-starter-kit**](https://github.com/Black-coffe/mcp-starter-kit) repository.

- [`gen_orders.py`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/gen_orders.py) — the synthetic order generator. Deterministic, so your numbers match the ones in the video.
- [`data/orders.json`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/data/orders.json) — two hundred fictional orders. The company does not exist; the data is synthetic.
- [`server-minimal/server.py`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/server-minimal/server.py) — the reference three-tool server, under sixty lines.
- [`prompts/server.md`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/prompts/server.md) — the plain-words task handed to Claude Code in the video instead of ready code.
- [`config-example.json`](https://github.com/Black-coffe/mcp-starter-kit/blob/main/config-example.json) — a sample `.mcp.json`.

### Homework — twenty minutes to an hour

**Stand up a minimal MCP server with one tool over your own folder, then ask Claude three questions it cannot answer without it.**

1. **One tool, not three.** The point is walking the whole path, not the volume.
2. **Connect it** and confirm the model can see it.
3. **Ask three questions.** You will know instantly: a precise answer with numbers from your files beats general words.

In the comments, tell me one thing: which tool you built and which question broke it. The second is more interesting than the first.

---

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
