---
layout: llm_review
title: "OpenAI: GPT-5 Codex"
date: "2025-09-23 18:03:23"
model_id: openai/gpt-5-codex
slug: openai-gpt-5-codex
provider: Openai
pricing:
  prompt_per_m: 1.25
  completion_per_m: 10.0
  blend_per_m: 3.4375
context_length: 400,000
max_output: 128,000
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Programování
  - Řešení matematických problémů
strengths:
  - area: Programování
    description: Vysoké skóre v LiveCodeBench (84.0) naznačuje silné schopnosti v generování a porozumění kódu.
  - area: Matematika
    description: Výborné výsledky v aime_25 (98.7) a artificial_analysis_math_index (98.7) ukazují na silné matematické dovednosti.
weaknesses:
  - area: Rychlost
    description: Relativně nízké TPS (210.8) a vysoká latence (21.908s) znamenají pomalejší odezvu v porovnání s konkurencí.
  - area: Čeština
    description: Nedostupnost dat pro MMMLU v češtině znemožňuje posoudit kvalitu modelu v českém jazyce.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: 4x dražší vstup, 2.5x dražší výstup
    comparison: Claude Opus je silný konkurent v obecné inteligenci, ale dražší.
  - provider: GOOGLE
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: 1.6x dražší vstup, 1.2x dražší výstup
    comparison: Gemini Pro nabízí velký kontext, ale je dražší.
  - provider: X-AI
    model: x-ai/grok-code-fast-1
    model_id: x-ai/grok-code-fast-1
    price_comparison: 6.25x levnější vstup, 1.5x levnější výstup
    comparison: Grok-code-fast-1 je levnější alternativa pro kódování, ale může mít nižší kvalitu výstupu.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: 6.25x levnější vstup, 50x levnější výstup
    comparison: Mistral 14B je výrazně levnější, ale nemusí dosahovat stejné úrovně inteligence.
recommendation:
  target_users:
    - Softwaroví inženýři
    - Výzkumníci v oblasti AI
  use_cases:
    - Generování kódu
    - Automatické opravy chyb
    - Řešení matematických problémů
  avoid_for:
    - Aplikace vyžadující nízkou latenci
    - Úlohy v českém jazyce (bez testování)
verdict: GPT-5 Codex je vhodný pro softwarové inženýry a výzkumníky, kteří potřebují výkonný model pro generování kódu a řešení matematických problémů, ale měli by zvážit jeho latenci a neznámou kvalitu v češtině.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 83.7
    tier: Výborný
  coding:
    name: Programování
    icon: 💻
    score: 84.0
    tier: Výborný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 86.8
    tier: Výborný
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 63.7
    tier: Dobrý
  speed:
    name: Rychlost
    icon: ⚡
    score: 50.0
    tier: Průměrný
overall_score: 79.2
overall_tier: Výborný
radar:
  logic_code: 84.0
  agentic: 86.8
  languages: 0
  safety: 0
  speed: Průměrný
expert_verdict:
  killer_feature: Vynikající schopnosti v matematice a programování.
  hidden_risk: Vyšší latence a neznámá kvalita v češtině.
  recommended_use_case: Automatické generování a refaktorování kódu v anglickém jazyce.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:13"
---

GPT-5-Codex je specializovaná verze GPT-5 optimalizovaná pro softwarové inženýrství a pracovní postupy kódování. Je navržena jak pro interaktivní vývojové relace, tak pro dlouhé, nezávislé provádění komplexních inženýrských úloh. Model podporuje vytváření projektů od začátku, vývoj funkcí, ladění, rozsáhlý refaktoring a revizi kódu. Ve srovnání s GPT-5 je Codex lépe řiditelný, úzce se drží pokynů vývojáře a produkuje čistší a kvalitnější výstupy kódu. Úsilí vynaložené na usuzování lze upravit pomocí parametru `reasoning.effort`. Přečtěte si [dokumentaci zde](https://openrouter.ai/docs/use-cases/reasoning-tokens#reasoning-effort-level)

Codex se integruje do vývojářských prostředí, včetně CLI, rozšíření IDE, GitHubu a cloudových úloh. Dynamicky přizpůsobuje úsilí vynaložené na usuzování – poskytuje rychlé reakce pro malé úkoly a zároveň udržuje prodloužené vícehodinové běhy pro velké projekty. Model je trénován k provádění strukturovaných revizí kódu, zachycování kritických chyb usuzováním nad závislostmi a validací chování proti testům. Podporuje také multimodální vstupy, jako jsou obrázky nebo snímky obrazovky pro vývoj uživatelského rozhraní, a integruje používání nástrojů pro vyhledávání, instalaci závislostí a nastavení prostředí. Codex je určen speciálně pro agentní kódovací aplikace.

## Unikátní charakteristiky

GPT-5 Codex je specializovaná verze GPT-5 optimalizovaná pro softwarové inženýrství a kódovací workflow. Vyniká v matematických úlohách (aime_25: 98.7%) a programování (LiveCodeBench: 84.0%).

## Silné stránky

### Programování
Vysoké skóre v LiveCodeBench (84.0) naznačuje silné schopnosti v generování a porozumění kódu.

### Matematika
Výborné výsledky v aime_25 (98.7) a artificial_analysis_math_index (98.7) ukazují na silné matematické dovednosti.

## Slabé stránky

### Rychlost
Relativně nízké TPS (210.8) a vysoká latence (21.908s) znamenají pomalejší odezvu v porovnání s konkurencí.

### Čeština
Nedostupnost dat pro MMMLU v češtině znemožňuje posoudit kvalitu modelu v českém jazyce.
