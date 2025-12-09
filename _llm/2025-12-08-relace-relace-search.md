---
layout: llm_review
title: "Relace: Relace Search"
date: "2025-12-08 18:06:00"
model_id: relace/relace-search
slug: relace-relace-search
provider: Relace
pricing:
  prompt_per_m: 1.0
  completion_per_m: 3.0
context_length: 256,000
max_output: 128,000
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Codebase Search
  - Agentic Reasoning
  - Retrieval
competitors:
  - provider: Anthropic
    model: Claude Haiku 4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Stejná cena vstupu ($1.00), Relace je o 40 % levnější na výstupu
    comparison: Haiku je univerzálnější a často se používá pro RAG re-ranking. Relace nabízí specializovanější sadu nástrojů pro hluboký průzkum kódu, ale postrádá obecnost Haiku.
  - provider: X-AI
    model: Grok Code Fast 1
    model_id: x-ai/grok-code-fast-1
    price_comparison: Relace je 5x dražší na vstupu a 2x dražší na výstupu
    comparison: Grok Code Fast má stejný kontext (256k) a je výrazně levnější. Relace musí obhájit svou cenu vyšší úspěšností při autonomním vyhledávání souborů pomocí nástrojů.
  - provider: OpenAI
    model: GPT-5.1 Codex Max
    model_id: openai/gpt-5.1-codex-max
    price_comparison: Relace je o 20 % levnější na vstupu a 3,3x levnější na výstupu
    comparison: Codex Max je 'oracle' model určený k psaní kódu. Relace je navržena jako jeho levnější doplněk pro přípravnou fázi (vyhledávání), čímž šetří drahé tokeny modelu Codex.
recommendation:
  target_users:
    - Vývojáři AI vývojářských nástrojů (IDE extensions)
    - Architekti RAG systémů pro softwarové inženýrství
  use_cases:
    - Sémantické vyhledávání v rozsáhlých legacy kódových bázích
    - Autonomní dohledávání závislostí před refaktoringem
    - Filtrování kontextu pro drahé modely (GPT-5.1, Opus 4.5)
  avoid_for:
    - Jednoduché otázky a odpovědi (Q&A)
    - Generování nového kódu
    - Aplikace bez orchestrátoru/agentní smyčky
verdict: Relace Search je vysoce specializovaný nástroj pro inženýrské týmy, které narazily na limity tradičního RAGu v kódových bázích a potřebují přesnější, agentický způsob retrievalu před samotným generováním kódu.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2025-12-09 07:32"
---

Model relace-search používá paralelně 4-12 nástrojů `view_file` a `grep` k prozkoumání codebase a vrácení relevantních souborů na základě požadavku uživatele.

Na rozdíl od RAG, relace-search provádí agentní vícestupňové usuzování, aby dosáhl vysoce přesných výsledků 4x rychleji než jakýkoli špičkový model. Je navržen tak, aby sloužil jako subagent, který předává svá zjištění "oracle" kódovacímu agentovi, který řídí/provádí zbytek kódovacího úkolu.

Pro použití relace-search je potřeba vytvořit vhodný agent harness a parsovat odpověď pro relevantní informace, které se předají oraclu. Více informací naleznete v [dokumentaci Relace](https://docs.relace.ai/docs/fast-agentic-search/agent).

## Unikátní charakteristiky

Relace Search je specializovaný model navržený jako náhrada za tradiční RAG (Retrieval-Augmented Generation) v kódových bázích, využívající paralelní volání nástrojů jako `grep` a `view_file`. Funguje výhradně jako vyhledávací podagent (sub-agent), který aktivně prozkoumává soubory a předává relevantní kontext nadřazenému 'oracle' modelu pro finální generování kódu.

## Silné stránky

### Přesnost vyhledávání
Díky agentickému přístupu a vícekrokovému uvažování dosahuje vyšší přesnosti při nalézání relevantních souborů než vektorové vyhledávání, zejména ve složitých repozitářích.

### Rychlost a paralelizace
Model využívá 4-12 nástrojů paralelně, což mu umožňuje prozkoumat kódovou bázi až 4x rychleji než běžné frontier modely používané pro stejný účel.

### Kontextové okno
Kapacita 256 000 tokenů je optimalizována pro načtení rozsáhlých struktur souborů a metadat během vyhledávací fáze.

## Slabé stránky

### Implementační složitost
Model není 'plug-and-play'; vyžaduje vybudování specifického agentního postroje (harness) a parseru pro zpracování výstupů před předáním dalšímu modelu.

### Úzká specializace
Model není určen pro generování finálního kódu nebo obecnou konverzaci, slouží pouze k nalezení a extrakci informací.
