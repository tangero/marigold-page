---
layout: llm_review
title: "DeepSeek: R1 Distill Llama 70B"
date: "2025-01-23 21:12:49"
model_id: deepseek/deepseek-r1-distill-llama-70b
slug: deepseek-deepseek-r1-distill-llama-70b
provider: DeepSeek
pricing:
  prompt_per_m: 0.03
  completion_per_m: 0.13
  blend_per_m: 0.055
context_length: 131,072
max_output: 131,072
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Matematika
  - Kódování
strengths:
  - area: Matematika
    description: Vysoké skóre v matematických benchmarcích, jako MATH-500 (93.5%) a AIME 2025 (67.0%), naznačuje silné schopnosti v řešení matematických problémů.
  - area: Kontext
    description: Velký kontext 131,072 tokenů umožňuje zpracovávat rozsáhlé dokumenty a složité konverzace.
weaknesses:
  - area: Rychlost
    description: Nízké TPS (98.3) a relativně vysoká latence (0.957s) znamenají pomalejší odezvu ve srovnání s jinými modely.
  - area: Programování
    description: Relativně nízké skóre v LiveCodeBench (26.6%) naznačuje slabší schopnosti v programování ve srovnání s modely zaměřenými na kódování.
competitors:
  - provider: GOOGLE
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Podobná cena vstupu, dražší výstup
    comparison: Gemini Pro má větší kontext (1,048,576 tokenů) a potenciálně lepší obecnou inteligenci, ale je dražší na výstup.
  - provider: ANTHROPIC
    model: anthropic/claude-sonnet-4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: Dražší vstup i výstup
    comparison: Claude Sonnet má větší kontext (1,000,000 tokenů), ale je výrazně dražší.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Levnější vstup i výstup
    comparison: Ministral 14B je levnější, ale pravděpodobně má nižší výkon v matematice a kódování.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Dražší vstup i výstup
    comparison: DeepSeek v3.2 má menší kontext, ale může mít lepší výkon v jiných oblastech (data nejsou k dispozici).
recommendation:
  target_users:
    - Výzkumníci v oblasti matematiky
    - Studenti a učitelé matematiky
  use_cases:
    - Řešení složitých matematických úloh
    - Generování matematických důkazů
  avoid_for:
    - Aplikace vyžadující rychlou odezvu
    - Úkoly vyžadující pokročilé programovací schopnosti
verdict: DeepSeek R1 Distill Llama 70B je vhodný pro uživatele, kteří potřebují model s vysokým výkonem v matematice a jsou ochotni akceptovat pomalejší rychlost a průměrné programovací schopnosti. Je ideální pro výzkum a vzdělávání v matematice.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 61.6
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 26.6
    tier: Slabý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 21.9
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 52.0
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 26.7
    tier: Slabý
overall_score: 39.0
overall_tier: Slabý
radar:
  logic_code: 44.1
  agentic: 21.9
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající výkon v matematických úlohách
  hidden_risk: Slabší výkon v programování a pomalá inference
  recommended_use_case: Řešení komplexních matematických problémů a validace matematických modelů.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 11:01"
---

DeepSeek R1 Distill Llama 70B je destilovaný velký jazykový model založený na [Llama-3.3-70B-Instruct](/meta-llama/llama-3.3-70b-instruct), využívající výstupy z [DeepSeek R1](/deepseek/deepseek-r1). Model kombinuje pokročilé destilační techniky k dosažení vysokého výkonu v několika benchmarkách, včetně:

- AIME 2024 pass@1: 70.0
- MATH-500 pass@1: 94.5
- CodeForces Rating: 1633

Model využívá doladění z výstupů DeepSeek R1, což umožňuje konkurenceschopný výkon srovnatelný s většími hraničními modely.

## Unikátní charakteristiky

DeepSeek R1 Distill Llama 70B je destilovaný model, který dosahuje vysokých skóre v matematických úlohách (MATH-500: 93.5%, AIME 2025: 67.0%). Jeho kódovací schopnosti jsou průměrné (LiveCodeBench: 26.6%).

## Silné stránky

### Matematika
Vysoké skóre v matematických benchmarcích, jako MATH-500 (93.5%) a AIME 2025 (67.0%), naznačuje silné schopnosti v řešení matematických problémů.

### Kontext
Velký kontext 131,072 tokenů umožňuje zpracovávat rozsáhlé dokumenty a složité konverzace.

## Slabé stránky

### Rychlost
Nízké TPS (98.3) a relativně vysoká latence (0.957s) znamenají pomalejší odezvu ve srovnání s jinými modely.

### Programování
Relativně nízké skóre v LiveCodeBench (26.6%) naznačuje slabší schopnosti v programování ve srovnání s modely zaměřenými na kódování.
