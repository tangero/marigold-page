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
    description: Vysoké skóre v matematických benchmarkách, jako MATH-500 (93.5%) a AIME 2025 (67.0%), naznačuje silné schopnosti v řešení matematických problémů.
  - area: Kódování
    description: Solidní výkon v kódovacích benchmarkách, jako LiveCodeBench (26.6%) a scicode (31.2%), ukazuje na schopnost generovat a rozumět kódu.
weaknesses:
  - area: Rychlost
    description: Nízká rychlost inference (98.3 TPS) a vysoká latence (0.957s) mohou omezit použitelnost v aplikacích vyžadujících rychlou odezvu.
  - area: Čeština
    description: Chybí data o výkonu v češtině (MMMLU), což ztěžuje posouzení vhodnosti pro české uživatele.
competitors:
  - provider: GOOGLE
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Podobná cena vstupu, 2x dražší výstup
    comparison: Větší kontext (1,048,576 tokenů) a pravděpodobně lepší podpora multimodality, ale horší v matematice.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Výrazně levnější vstup i výstup
    comparison: Levnější, ale pravděpodobně nižší výkon v matematice a kódování.
  - provider: X-AI
    model: x-ai/grok-4-fast
    model_id: x-ai/grok-4-fast
    price_comparison: Mnohem levnější vstup i výstup
    comparison: Výrazně levnější, obrovský kontext, ale neznámý výkon v matematice a kódování.
recommendation:
  target_users:
    - Výzkumníci v oblasti AI
    - Vývojáři matematických aplikací
  use_cases:
    - Řešení komplexních matematických problémů
    - Generování kódu pro specifické úlohy
  avoid_for:
    - Aplikace vyžadující nízkou latenci
    - Aplikace s primárním zaměřením na češtinu
verdict: DeepSeek R1 Distill Llama 70B je vhodný pro uživatele, kteří potřebují vysoký výkon v matematice a kódování a nevadí jim pomalejší inference. Je ideální pro offline analýzy a výzkum.
categories:
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
  killer_feature: Vynikající výkon v matematických úlohách (MATH-500, AIME 2025).
  hidden_risk: Pomalá inference může omezit použitelnost v reálném čase.
  recommended_use_case: Offline řešení složitých matematických problémů, kde není kladen důraz na rychlost.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 10:52"
---

DeepSeek R1 Distill Llama 70B je destilovaný velký jazykový model založený na [Llama-3.3-70B-Instruct](/meta-llama/llama-3.3-70b-instruct), využívající výstupy z [DeepSeek R1](/deepseek/deepseek-r1). Model kombinuje pokročilé techniky destilace k dosažení vysokého výkonu v několika benchmarkách, včetně:

- AIME 2024 pass@1: 70.0
- MATH-500 pass@1: 94.5
- CodeForces Rating: 1633

Model využívá doladění z výstupů DeepSeek R1, což umožňuje konkurenceschopný výkon srovnatelný s většími špičkovými modely.

## Unikátní charakteristiky

DeepSeek R1 Distill Llama 70B je destilovaný model, který exceluje v matematice a kódování. Dosahuje vysokých skóre v MATH-500 (93.5%) a AIME 2025 (67.0%), což naznačuje silné schopnosti v řešení komplexních problémů. Nicméně, rychlost inference je pomalá (98.3 TPS).

## Silné stránky

### Matematika
Vysoké skóre v matematických benchmarkách, jako MATH-500 (93.5%) a AIME 2025 (67.0%), naznačuje silné schopnosti v řešení matematických problémů.

### Kódování
Solidní výkon v kódovacích benchmarkách, jako LiveCodeBench (26.6%) a scicode (31.2%), ukazuje na schopnost generovat a rozumět kódu.

## Slabé stránky

### Rychlost
Nízká rychlost inference (98.3 TPS) a vysoká latence (0.957s) mohou omezit použitelnost v aplikacích vyžadujících rychlou odezvu.

### Čeština
Chybí data o výkonu v češtině (MMMLU), což ztěžuje posouzení vhodnosti pro české uživatele.
