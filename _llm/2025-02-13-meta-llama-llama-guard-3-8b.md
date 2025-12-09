---
layout: llm_review
title: Llama Guard 3 8B
date: "2025-02-13 00:01:58"
model_id: meta-llama/llama-guard-3-8b
slug: meta-llama-llama-guard-3-8b
provider: Meta
pricing:
  prompt_per_m: 0.02
  completion_per_m: 0.06
  blend_per_m: 0.03
context_length: 131,072
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Bezpečnost obsahu
  - Moderování obsahu
strengths:
  - area: Bezpečnost obsahu
    description: Specializovaný model pro detekci nebezpečného obsahu ve vstupech a výstupech LLM.
  - area: Vícejazyčnost
    description: Podporuje moderování obsahu v 8 jazycích.
weaknesses:
  - area: Obecná inteligence
    description: Není určen pro obecné úkoly, ale specificky pro bezpečnost obsahu.
  - area: Benchmark data
    description: Chybí benchmark data pro objektivní srovnání s konkurencí.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: 33x dražší vstup, 83x dražší výstup
    comparison: Claude Haiku je univerzálnější, ale dražší. Llama Guard 3 je specializovaný na bezpečnost.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: 10x dražší vstup, 41x dražší výstup
    comparison: Gemini Flash je univerzálnější, ale dražší. Llama Guard 3 je specializovaný na bezpečnost.
  - provider: MISTRALAI
    model: mistralai/ministral-3b-2512
    model_id: mistralai/ministral-3b-2512
    price_comparison: 3x dražší vstup, 3x dražší výstup
    comparison: Ministral 3B je menší a rychlejší, ale Llama Guard 3 je specializovaný na bezpečnost.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: 7x dražší vstup, 10x dražší výstup
    comparison: Deepseek V3.2 Exp je univerzálnější, ale dražší. Llama Guard 3 je specializovaný na bezpečnost.
recommendation:
  target_users:
    - Vývojáři LLM aplikací
    - Platformy pro generování obsahu
  use_cases:
    - Moderování uživatelských vstupů
    - Filtrování nevhodných výstupů LLM
    - Zajištění bezpečnosti aplikací s LLM
  avoid_for:
    - Obecné úkoly zpracování textu
    - Úkoly vyžadující kreativitu a originalitu
verdict: Llama Guard 3 je ideální pro vývojáře a platformy, které potřebují specializovaný a cenově dostupný nástroj pro moderování obsahu a zajištění bezpečnosti LLM aplikací.
benchmark_categories: null
overall_score: null
overall_tier: null
radar:
  logic_code: 0
  agentic: 0
  languages: 0
  safety: 5
  speed: Nehodnoceno
expert_verdict:
  killer_feature: Specializace na bezpečnost obsahu
  hidden_risk: Závislost na kvalitě trénovacích dat pro bezpečnost; potenciální falešně pozitivní/negativní výsledky.
  recommended_use_case: Automatické filtrování nevhodných komentářů na sociálních sítích.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 11:03"
---

Llama Guard 3 je předtrénovaný model Llama-3.1-8B, doladěný pro klasifikaci bezpečnosti obsahu. Podobně jako předchozí verze, může být použit ke klasifikaci obsahu jak ve vstupech LLM (klasifikace promptů), tak v odpovědích LLM (klasifikace odpovědí). Funguje jako LLM – generuje text ve svém výstupu, který indikuje, zda je daný prompt nebo odpověď bezpečný nebo nebezpečný, a pokud je nebezpečný, také vypíše kategorie obsahu, které byly porušeny.

Llama Guard 3 byl sladěn tak, aby chránil proti standardizované taxonomii rizik MLCommons a byl navržen tak, aby podporoval schopnosti Llama 3.1. Konkrétně poskytuje moderování obsahu v 8 jazycích a byl optimalizován pro podporu bezpečnosti a zabezpečení pro vyhledávání a volání nástrojů interpretu kódu.

## Unikátní charakteristiky

Llama Guard 3 je model pro klasifikaci bezpečnosti obsahu, který generuje textové výstupy indikující, zda je daný vstup nebo výstup bezpečný. Byl optimalizován pro podporu bezpečnosti a zabezpečení pro vyhledávání a volání nástrojů pro interpretaci kódu. Benchmark data nejsou k dispozici.

## Silné stránky

### Bezpečnost obsahu
Specializovaný model pro detekci nebezpečného obsahu ve vstupech a výstupech LLM.

### Vícejazyčnost
Podporuje moderování obsahu v 8 jazycích.

## Slabé stránky

### Obecná inteligence
Není určen pro obecné úkoly, ale specificky pro bezpečnost obsahu.

### Benchmark data
Chybí benchmark data pro objektivní srovnání s konkurencí.
