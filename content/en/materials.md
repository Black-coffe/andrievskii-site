---
title: "Materials"
slug: "materials"
lang: "en"
description: "Checklists, templates, a repository — everything published alongside the videos"
---

Materials are what I publish in the description of my YouTube videos: checklists, templates and code you can take and use right away.

## Video 4 — "Dubbing in your own voice: three ways to translate a video with Claude Code, one of them free"

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/IT9yzqFiF9c" title="Dubbing in your own voice: three ways to translate a video with Claude Code, one of them free" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

The video we dub is [video 3](https://youtu.be/FA1oVqBTUeM): watch it first so you can compare the original with the dub. Viewers wrote to me: "you speak Ukrainian but write in Russian." Fair. I show how to dub a video yourself: the same voice, another language. Three options side by side, each one you can hear, and an honest price for each on a 20-minute video. The main idea: a model does not need a prompt, it needs a workplace: a folder with instructions, a glossary and scripts.

### What to take

Everything sits in the open [**dubbing-starter-kit**](https://github.com/Black-coffe/dubbing-starter-kit) repository.

- [`README.md`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/README.md) — setup, how to run all three options, and the full homework.
- [`dub.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/dub.py) — option A: Demucs, faster-whisper, Claude translating by the glossary, ElevenLabs voicing with a clone of your voice, timing fit. About $0.20 per 20-minute video as measured (the voicing price was on promotion).
- [`eldub.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/eldub.py) — option B: the ready-made ElevenLabs Dubbing API service, for comparison. From $10 to $23 per 20-minute video.
- [`variant_local.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/variant_local.py) and [`tts_omnivoice.py`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/tts_omnivoice.py) — option C: all local and free, translation in Ollama and the OmniVoice voice. About $0.01 in electricity, a graphics card is required.
- [`glossary.json`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/glossary.json) — the term glossary: what to leave untranslated and how to pronounce it.
- [`ab.html`](https://github.com/Black-coffe/dubbing-starter-kit/blob/main/ab.html) — a page that switches between the tracks every few seconds.
- [**ai-video-dubbing**](https://github.com/Black-coffe/ai-video-dubbing) — a ready-made dubbing program for your own keys, in English, with instructions and prompts for Claude Code and Codex.

### Tracks to compare by ear

The same 3:15 fragment of video 3, dubbed three ways. The tracks are level-matched so the loud one does not seem better.

- [Track A](https://raw.githubusercontent.com/Black-coffe/dubbing-starter-kit/main/tracks/A.m4a) — our `dub.py` pipeline: voice clone, glossary-based translation.
- [Track B](https://raw.githubusercontent.com/Black-coffe/dubbing-starter-kit/main/tracks/B.m4a) — the ready-made service, ElevenLabs Dubbing API, one command.
- [Track C](https://raw.githubusercontent.com/Black-coffe/dubbing-starter-kit/main/tracks/C.m4a) — all local and free: Ollama and OmniVoice.

The OmniVoice weights (option C) are released under CC-BY-NC: non-commercial use only. C does not suit a monetized channel; you need a different model there.

### Homework — about an hour

**Dub 30 seconds of your own video into another language in your own voice and compare the result by ear with a ready-made service.**

1. Take a 30-second fragment of your video and put it in a folder together with a task description; let Claude Code first ask you about services, hardware and budget.
2. Run the fragment through the pipeline, read the translation next to the original and fix what the glossary does not catch.
3. Play your track and the ready-made service's track, switching every 6 seconds from the same spot, and write down which sounds better and what it cost.

If you have done this before, write in the comments which language and which option you chose, and where the pronunciation broke.

---

## Video 3 — "Claude assembles my work documents by itself. Showing the whole system"

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/FA1oVqBTUeM" title="Claude assembles my work documents by itself. Showing the whole system" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Assembling the same document by hand — a table, a report, a statement — is a habit, not a necessity. Claude Code can find a skill by its description and run the right script on its own, with no manual terminal call. Shown on a reference example: a docx template that breaks on merged cells and a two-level header, a fill-in script, and a fictional company, Meridian.

### What to take

Everything sits in the open [**skills-starter-kit**](https://github.com/Black-coffe/skills-starter-kit) repository.

- [`skill-skeleton/SKILL.md`](https://github.com/Black-coffe/skills-starter-kit/blob/main/skill-skeleton/SKILL.md) — the reference skill: a `name`/`description` header and the filling rules.
- [`skill-skeleton/templates/report-template.docx`](https://github.com/Black-coffe/skills-starter-kit/blob/main/skill-skeleton/templates/report-template.docx) — the neutral report template.
- [`skill-skeleton/scripts/fill_report.py`](https://github.com/Black-coffe/skills-starter-kit/blob/main/skill-skeleton/scripts/fill_report.py) — the script that fills the template with data.
- [`gen/make_templates.py`](https://github.com/Black-coffe/skills-starter-kit/blob/main/gen/make_templates.py) — the synthetic template generator, deterministic.
- [`data/shipments.csv`](https://github.com/Black-coffe/skills-starter-kit/blob/main/data/shipments.csv) — twelve fictional shipments from Meridian for August 2026.
- [`demo-naive/`](https://github.com/Black-coffe/skills-starter-kit/tree/main/demo-naive) — the same neutral template with no skill and no rules: what you get if you just ask a model to fill it in.
- [`demo-break/`](https://github.com/Black-coffe/skills-starter-kit/tree/main/demo-break) — a template with headers/footers, merged cells and a two-level table header, on which the script gets it wrong.

### Homework — half an hour and up

**Take a document you make regularly, put its template and instructions into a skill folder, and get a finished file from a single plain-language request.**

1. **Study `skill-skeleton/` as a structure sample** — `SKILL.md` → `templates/` → `scripts/`.
2. **Build your own version**: your own template, your own fill-in script; keep the data next to the skill, not inside its own folder.
3. **Ask in plain words.** Don't call the script by hand — ask Claude Code in a sentence ("put together the report for such-and-such period from this file") and confirm it finds the skill by its `description` and runs the right script on its own.

On the sample data the reference skill produces a header naming Meridian, the period "August 2026", twelve rows in CSV order, and a total of $164,850 — computed by the script, never stored in the CSV. A different total means the mismatch is in the template or the script, not the data.

---

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
