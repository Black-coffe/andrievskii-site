---
slug: "erp-crm"
title: "ERP/CRM digitization"
client_type: "large business"
period: ""  # TODO: the period of this work is confirmed by Andrei
stack:
  - "Recall"
  - "MCP"
  - "Claude"
  - "GPT"
# TODO: the rest of the ERP/CRM stack is confirmed by Andrei
summary: "ERP, CRM and staff call records digitized — brought together and reachable by AI providers through MCP"
---

## Task

Digitize the processes of a large business so that AI can reach them: bring ERP, CRM and staff call records into one system.

## What came before

The data sat apart: in the ERP, in the CRM and in the call records. Each system on its own, with no shared access for AI.

## How it's built

Everything is built on the Recall system. ERP, CRM and staff call records are brought together and reachable by AI providers — Claude, GPT — through MCP. A separate loop brings Notion, Asana, Obsidian and Google docs into a single knowledge base.

## What worked

Staff query the knowledge base in real time instead of calls and meetings — that closes about 70% of internal questions.

## What didn't work

Digitizing 1C completely didn't work out. The vendor's licence gets in the way, and so does the way the program is built inside: it gives no usable way to connect to it for an AI integration.

So 1C is connected the long way round: an export to XML, parsing that export, and only on top of that — all the rest of the logic.
