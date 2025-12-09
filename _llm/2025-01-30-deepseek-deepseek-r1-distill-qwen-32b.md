---
layout: llm_review
title: "DeepSeek: R1 Distill Qwen 32B"
date: "2025-01-30 00:53:50"
model_id: deepseek/deepseek-r1-distill-qwen-32b
slug: deepseek-deepseek-r1-distill-qwen-32b
provider: DeepSeek
pricing:
  prompt_per_m: 0.24
  completion_per_m: 0.24
  blend_per_m: 0.24
context_length: 64,000
max_output: 32,000
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Věda
  - Matematika
strengths:
  - area: Matematika
    description: Vysoké skóre v matematických benchmarcích MATH-500 (94.1%) a AIME 2025 (68.7%) naznačuje silnou schopnost řešit komplexní matematické problémy.
  - area: Věda
    description: Dobrý výsledek v GPQA Diamond (61.5%) ukazuje na schopnost porozumět a řešit vědecké otázky.
weaknesses:
  - area: Programování
    description: Nízké skóre v LiveCodeBench (27.0%) naznačuje slabší schopnosti v oblasti programování.
  - area: Rychlost
    description: Nízké TPS (53.1) a relativně vysoká latence (0.582s) znamenají, že model není ideální pro aplikace vyžadující rychlou odezvu.
competitors:
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Podobná cena vstupu i výstupu
    comparison: Ministral-14b má větší kontext (262,144 tokenů) a může být lepší v úlohách vyžadujících dlouhodobou paměť.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: Levnější vstup i výstup
    comparison: Ministral-8b je levnější, ale pravděpodobně méně výkonný v náročných úlohách.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-speciale
    model_id: deepseek/deepseek-v3.2-speciale
    price_comparison: Mírně dražší vstup i výstup
    comparison: Deepseek-v3.2-speciale má menší kontext, ale může mít lepší výkon v některých specifických úlohách (data nejsou k dispozici).
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Levnější vstup i výstup
    comparison: Grok-4.1-fast nabízí obrovský kontext (2,000,000 tokenů) a nižší cenu, ale jeho výkon v matematice a vědě není znám.
recommendation:
  target_users:
    - Výzkumníci
    - Studenti
    - Data Scientists
  use_cases:
    - Řešení matematických problémů
    - Analýza vědeckých dat
    - Vzdělávací aplikace
  avoid_for:
    - Generování kódu
    - Aplikace vyžadující rychlou odezvu
    - Úlohy v češtině (chybí data)
verdict: DeepSeek R1 Distill Qwen 32B je vhodný pro uživatele, kteří potřebují model s vysokým výkonem v matematice a vědě, ale nemají vysoké nároky na rychlost a programování. Je nutné ověřit jeho schopnosti v češtině.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 70.9
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 27.0
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 48.2
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 34.2
    tier: Slabý
overall_score: 46.6
overall_tier: Průměrný
radar:
  logic_code: 27.0
  agentic: 0
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající v matematice
  hidden_risk: Slabší v programování a logickém uvažování, chybí data pro češtinu
  recommended_use_case: Řešení komplexních matematických úloh a analýza vědeckých dat
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 11:01"
---

DeepSeek R1 Distill Qwen 32B je destilovaný velký jazykový model založený na [Qwen 2.5 32B](https://huggingface.co/Qwen/Qwen2.5-32B), využívající výstupy z [DeepSeek R1](/deepseek/deepseek-r1). Překonává o1-mini od OpenAI v různých benchmarkách a dosahuje nových nejlepších výsledků pro husté modely.

Další výsledky benchmarků zahrnují:

- AIME 2024 pass@1: 72.6
- MATH-500 pass@1: 94.3
- CodeForces Rating: 1691

Model využívá doladění z výstupů DeepSeek R1, což umožňuje konkurenceschopný výkon srovnatelný s většími špičkovými modely.

## Unikátní charakteristiky

DeepSeek R1 Distill Qwen 32B je destilovaný model, který dosahuje vysokých skóre v matematických benchmarcích (MATH-500: 94.1%, AIME 2025: 68.7%). Vyniká v náročných matematických úlohách, ale má slabší výsledky v logickém uvažování a programování.

## Silné stránky

### Matematika
Vysoké skóre v matematických benchmarcích MATH-500 (94.1%) a AIME 2025 (68.7%) naznačuje silnou schopnost řešit komplexní matematické problémy.

### Věda
Dobrý výsledek v GPQA Diamond (61.5%) ukazuje na schopnost porozumět a řešit vědecké otázky.

## Slabé stránky

### Programování
Nízké skóre v LiveCodeBench (27.0%) naznačuje slabší schopnosti v oblasti programování.

### Rychlost
Nízké TPS (53.1) a relativně vysoká latence (0.582s) znamenají, že model není ideální pro aplikace vyžadující rychlou odezvu.
