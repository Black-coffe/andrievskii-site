---
title: "Materials"
slug: "materials"
lang: "en"
description: "Checklists, templates, a repository — everything published alongside the videos"
---

Materials are what I publish in the description of my YouTube videos: checklists, templates and code you can take and use right away.

## Video 8 — "Claude Code on a team: what goes in CLAUDE.md and what goes in a gate"

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/mjXfoPfIxIA" title="Claude Code on a team: what goes in CLAUDE.md and what goes in a gate" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

There are three of us, three machines, each with their own Claude Code, and together we build a live product. The video walks through four cases where we got out of sync, and every time it went the same way: there was no rule, something broke, we wrote the rule down. The main idea: some agreements hold as words in a shared file, and others have to go into a gate, because words don't hold. The cases are recreated on a training project with three working copies and a study group with a tracker bot.

### What to take

The kit is in the public repository [**Black-coffe/team-agreements-kit**](https://github.com/Black-coffe/team-agreements-kit): a team `CLAUDE.md`, conventions, a review checklist for PRs written by an agent, and deny settings for the agent (`.env`, generated files, pushing to `main`, deploys). How to fill it in and check it step by step is in the kit's README. Tested on Windows, not on Mac. All links in one post are in the [Telegram channel](https://t.me/andrievskii_ai).

### Four cases and what holds the rule

| Case | Rule | Held by |
|---|---|---|
| A generated task board conflicted on almost every PR, 5 times in one session | Generated files don't live in git and aren't edited by hand | a gate |
| Three direct pushes to `main` in a day, the staging server didn't update | Into `main` only through a PR | a gate |
| A regeneration would have wiped 244 hand-written lines | The generator only appends | the generator's code |
| One bug fixed two different ways | Zones with owners, you don't edit someone else's zone yourself | a gate (CODEOWNERS) |

### Homework

Write an agreements file for your team (or for your future self): stack, style, what must not be generated without review, who owns which parts. Lay out the kit's templates, start Claude Code, and it will ask questions one at a time and fill in the templates. Then check that the gate holds: ask the agent to read a decoy key from `.env`, it must not see it. Tell us in the comments under the video what your team agreed on.

### Sources

Our team's working chat (805 messages, 15.06–21.10.2026) and 13 calls. Quotes are paraphrased, colleagues by role, no names. Every number from the video with its source is in the kit's [`facts.md`](https://github.com/Black-coffe/team-agreements-kit/blob/main/facts.md). The training project, its group and the bot are made up; data on screen is labelled "example".

---

## Video 7 — "Company knowledge base: 77 documents, 14 contradictions and 40 questions before and after"

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/bi_R5IPNbLo" title="Company knowledge base: 77 documents, 14 contradictions and 40 questions before and after" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

The video is about an order of steps, not a tool: how to build a company knowledge base together with Claude Code. It is shown on a made-up company, Veltra Power: what to export, what not to give the model, how to find contradictions between documents and how to check the result on 40 questions. No MCP, just an export into a folder: 38 correct answers out of 40 instead of 30, and zero made-up answers. The downsides are shown too: the skill makes mistakes, so every quote is checked by hand, and two of the 40 questions the base never got right.

### What to take

The kit sits in the open repository [**Black-coffe/company-knowledge-kit**](https://github.com/Black-coffe/company-knowledge-kit): a skill that finds contradictions, document precedence rules, an inventory template, a made-up company of 77 documents, a mini set of 13 files and 40 control questions with an answer key. How to run it step by step is in the kit's README. All links in one post are in the [Telegram channel](https://t.me/andrievskii_ai).

### Checklist of six steps

1. **Export.** The document folder is on disk, spreadsheets and PDFs have a text version next to them.
2. **Check the export.** Secrets, personal data and files open to the wrong people are found.
3. **Inventory.** One row per document with its owner, date and status.
4. **Precedence rules.** Signed beats working; the rules sit in the base's `CLAUDE.md`.
5. **Summaries and topics.** Every document has a short summary, the wiki is built by topic.
6. **Measurement.** Control questions with a key, a run before and after, a "helped / did not" column.

### Homework

Export one folder of your own documents. Run the contradiction-finding skill from the kit. Check the list: every row must have two files and a quote. No documents of your own? Take the made-up company from the kit and run the 40 questions; the bar is 9 of 12 traps. Write in the comments under the video how many contradictions you found.

### Sources

Read on 15.10.2026. ✅ — two independent sources, ⚠️ — one source, a vendor about itself or a preprint. Publication date in brackets.

1. ✅ **S1. Customer support, 2023.** +14 % issues resolved per hour, +34 % for novices, about 5,000 agents. Brynjolfsson, Li, Raymond, "Generative AI at Work": [NBER w31161](https://www.nber.org/papers/w31161) (Apr 2023), [arXiv 2304.11771](https://arxiv.org/abs/2304.11771) (06.11.2024, +15 % there, a different version), [NBER Digest](https://www.nber.org/digest/measuring-productivity-impact-generative-ai) (01.06.2023).
2. ⚠️ **S2. Social network, a graph from tickets.** A controlled experiment: median resolution time −28.6 %. Xu et al., SIGIR 2024: [arXiv 2404.17723](https://arxiv.org/abs/2404.17723) (26.04.2024).
3. ✅ **S3. Seven failure points of RAG.** Contradictions in the context as a cause of errors. Barnett et al., CAIN 2024: [arXiv 2401.05856](https://arxiv.org/abs/2401.05856) (11.01.2024).
4. ✅ **S4. A practitioner on Habr, 2025.** One question can have three answers; first the list of questions, then the sources; a test set after every change. Article in Russian: [Habr](https://habr.com/ru/articles/905076/) (28.04.2025).
5. ✅ **S5. Hosting provider, 2026.** Three versions of one document from different years; access is checked by code with the user's token; a full nightly rebuild. Runity, in Russian: [Habr, part 1](https://habr.com/ru/companies/runity/articles/1014712/) (25.03.2026), [part 2](https://habr.com/ru/companies/runity/articles/1086162/) (24.09.2026).
6. ✅ **S6. Telecom, 2025.** Contradictions "solved" with a "do not mix versions" prompt; outdated content is marked by hash. MTS Web Services, in Russian: [Habr](https://habr.com/ru/companies/ru_mts/articles/970476/) (16.12.2025).
7. ✅ **S7. Industrial software, 2026.** Documentation ranks above tickets; personal data is masked before indexing. Zyfra, in Russian: [Habr](https://habr.com/ru/companies/zyfra/articles/1007356/) (06.03.2026).
8. ✅ **S8. Tech marketplace, Genie.** A summary, FAQ and keywords per document; tables from PDFs converted to text; a golden question set from experts. Uber: [Genie](https://www.uber.com/blog/genie-ubers-gen-ai-on-call-copilot/) (10.10.2024), [Enhanced Agentic-RAG](https://www.uber.com/blog/enhanced-agentic-rag/) (29.05.2025).
9. ⚠️ **S9. Delivery service.** A two-level check of the answer against the knowledge-base article; an insufficient base is the root cause of bad answers. A retelling of a DoorDash post, the original of 13.08.2024 is unavailable: [ZenML LLMOps Database](https://www.zenml.io/llmops-database/rag-based-dasher-support-automation-with-llm-guardrails-and-quality-monitoring) (2024).
10. ✅ **S10. Legal systems, 17–33 %.** Wrong citations or unsupported answers in 17–33 % of cases for specialised systems. Magesh et al.: [arXiv 2405.20362](https://arxiv.org/abs/2405.20362) (30.05.2024), [Stanford HAI](https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries) (23.05.2024).
11. ✅ **S11. "They answer rather than abstain".** When data is missing or conflicting, models answer more often than they abstain. Joren et al., "Sufficient Context": [arXiv 2411.06037](https://arxiv.org/abs/2411.06037) (09.11.2024), [Google Research](https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/) (14.05.2025), [Zhang, Wu, CMC 89(1)](https://www.techscience.com/cmc/online/detail/27766) (13.08.2026).
12. ✅ **S12. Permissions and the export.** A copy of permissions in the index goes stale; an export has no permissions; sensitive data leaks through the assistant. [Azure AI Search, document-level access](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview) (updated 17.09.2026), [AWS, secure multi-tenant RAG](https://aws.amazon.com/blogs/architecture/secure-multi-tenant-rag-with-amazon-bedrock-and-verified-permissions/) (22.06.2026), [OWASP LLM08:2025](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/), [OWASP LLM02:2025](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/) (2025).
13. ⚠️ **S13. Where MCP is needed.** Live access is needed when the source is live, permissions follow the account and the data must not be copied; MCP acts with the user's permissions. MCP specification 2025-11-25: [Authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization), [Security Best Practices](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices). Vendors' own documentation: [Notion MCP](https://www.notion.com/help/notion-mcp) (2026), [Asana MCP](https://developers.asana.com/docs/integrating-with-asanas-mcp-server) (08.10.2026), [Atlassian MCP, README](https://github.com/atlassian/atlassian-mcp-server) (no date), [Copilot connectors](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/overview) (12.10.2026), [Google Workspace MCP, still preview](https://developers.google.com/workspace/guides/configure-mcp-servers) (13.10.2026).
14. ⚠️ **S14. The KCS v6 support standard.** Knowledge quality is everyone's duty, old content is marked as replaced, the set is alive. Consortium for Service Innovation, no date: [Practices Guide, 030](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030/040/010), [050](https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/050).
15. ⚠️ **S15. "The model maintains the wiki", 2026.** An idea from April 2026, at a scale of up to hundreds of pages. [Gist llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (04.04.2026), [VentureBeat](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an) (03.04.2026).
16. ✅ **S16. Analyst forecast, 2024.** At least 30 % of GenAI pilots will be abandoned after proof of concept. Gartner, release of 29.07.2024: [Intelligent CIO](https://www.intelligentcio.com/eu/2024/08/05/gartner-predicts-30-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025/) (05.08.2024), [THE Journal](https://thejournal.com/Articles/2024/08/06/Gartner-30-of-Gen-AI-Projects-Will-Be-Abandoned.aspx) (06.08.2024).
17. ✅ **S17. Benchmarks with contradictions.** Planted duplicates and contradictions; conflicts are a hard barrier even for reasoning models. [EnterpriseRAG-Bench, arXiv 2605.05253](https://arxiv.org/abs/2605.05253) (05.05.2026), [EnterpriseRAG, arXiv 2608.11584](https://arxiv.org/abs/2608.11584) (12.08.2026).
18. ✅ **S18. Fintech, customer support.** A chat assistant handled about two thirds of requests; a year later the company brought people back because of quality. [The Decoder](https://the-decoder.com/klarna-says-openais-ai-agent-does-the-work-of-700-support-agents/) (27.02.2024), [CX Dive](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-ai-chatbot/747586/) (09.05.2025).
19. ⚠️ **S19. Preprint, 2026.** Under long delegation, models corrupt about a quarter of the content. Laban, Schnabel, Neville: [arXiv 2604.15597](https://arxiv.org/abs/2604.15597) (17.04.2026).
20. ✅ **S20. A judge model favours the answer that comes first.** Shi et al., "Judging the Judges": [arXiv 2406.07791](https://arxiv.org/abs/2406.07791) (12.06.2024).

The company, documents and questions in the demo are made up. Measurement: claude-sonnet-5-5, 15.10.2026, 40 questions, median of three runs.

---

## Video 6 — "Your own program for your own pain: building with Claude what services don't have"

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/naej9ZaDv_w" title="Your own program for your own pain: building with Claude what services don't have" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

The video is about a method: how to bring a program for your own work pain to a working state together with Claude Code. Recall is the example of the result: an archive of calls with transcription on your own graphics card and search by meaning. The downsides are shown too: Claude labels the wrong speaker, transcription is worse on a weak graphics card, and a quote cannot be trusted without checking.

### What to take

The example of the result sits in the open repository [**Black-coffe/recall**](https://github.com/Black-coffe/recall): install it by the README and study it as an example, not as a finished product.

### Checklist of six stages

1. **Name your pain.** One work situation that a ready-made service does not cover.
2. **Build with Claude step by step.** Not everything at once: a small piece, a check, the next one.
3. **Put it to work.** Run it on real data, not on a stub.
4. **Catch where it lies.** Find places where the result looks right but does not match the source.
5. **Compare with the ready-made one and count.** What your own version gave and what it costs in money and time.
6. **Install it for yourself.** The program lives with you and works without a demo.

### Homework

Now the homework. Write down one work pain of your own that a ready-made service does not cover. Install Recall with Claude Code as a sample and ask Claude to add one thing to it for that pain: your own source, your own report or your own hint. Check the result on three of your own documents. The link to the code and the checklist are in the description and on the site.

---

## Video 5 — "LinkGuard: Claude wrote the code, but there are no sales"

<div style="position:relative;padding-top:56.25%;margin:1.4em 0;background:var(--color-sunk);border:1px solid var(--color-line-soft);border-radius:2px">
<iframe src="https://www.youtube-nocookie.com/embed/n9umDWm9k8A" title="LinkGuard: Claude wrote the code, but there are no sales" style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

Last autumn I wrote down a number: in six months the service earned $510. Claude Code wrote all of the code, 759 commits out of 759, and that part was easy. The service is alive; the money got lost somewhere else. I walk the whole path through my real prompts in six steps: idea, tasks, code, production, money, sales. The main mistake was not in the code: I never wrote down a stop number in advance, how much time and money before you quit.

### What to take

Everything sits in the open [**idea-to-backlog-kit**](https://github.com/Black-coffe/idea-to-backlog-kit) repository (files are in Russian).

- [`README.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/README.md) — the assignment and the full order of work.
- [`checklist.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/checklist.md) — the six steps of the video and the homework.
- [`spec-template.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/spec-template.md) — a one-page spec: three people who will pay, their answers, and the stop number.
- [`decomposition-prompt.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/decomposition-prompt.md) — a Claude Code prompt that turns the spec into a task tree you can hand over one task at a time.
- [`CLAUDE.md.example`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/CLAUDE.md.example) — an example `CLAUDE.md` as a short project index.
- [`review-checklist.md`](https://github.com/Black-coffe/idea-to-backlog-kit/blob/main/review-checklist.md) — how to accept Claude's work after every task.

### Homework — an evening for the spec and the task tree, plus talking to three people

**I did it backwards; you do it in order.**

1. Name three people who will pay for your idea.
2. Ask them.
3. Turn the idea into a task tree.
4. Write down your stop number: how much time and money before you quit.

Tell me in the video comments what stop number you set and what your three people said.

---

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
