---
layout: llm_review
title: "DeepSeek: R1 Distill Qwen 14B"
date: "2025-01-30 00:39:00"
model_id: deepseek/deepseek-r1-distill-qwen-14b
slug: deepseek-deepseek-r1-distill-qwen-14b
provider: DeepSeek
pricing:
  prompt_per_m: 0.12
  completion_per_m: 0.12
  blend_per_m: 0.12
context_length: 32,768
max_output: 16,384
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Matematika
  - Věda
strengths:
  - area: Matematika
    description: Vynikající výsledky v matematických benchmarkách, jako MATH-500 (94.9%) a AIME 2025 (66.7%), naznačují silné schopnosti v řešení matematických problémů.
  - area: Věda
    description: Dobrý výkon v GPQA Diamond (48.4%) ukazuje na schopnost porozumět a řešit složité vědecké otázky.
weaknesses:
  - area: Rychlost
    description: "Nízká rychlost (TPS: 63.8, TTFT: 0.990s) může omezit použitelnost v aplikacích vyžadujících rychlou odezvu."
  - area: Programování
    description: Slabý výkon v LiveCodeBench (37.6%) a scicode (23.9%) naznačuje omezené schopnosti v oblasti programování.
competitors:
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Podobná cena za vstup i výstup
    comparison: Konkuruje v kontextovém okně a ceně, ale benchmarky pro matematiku a vědu nejsou k dispozici.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: Mírně dražší vstup, dražší výstup
    comparison: Konkuruje v kontextovém okně, ale benchmarky pro matematiku a vědu nejsou k dispozici.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Dražší vstup, výrazně dražší výstup
    comparison: Konkuruje v kontextovém okně, ale benchmarky pro matematiku a vědu nejsou k dispozici.
recommendation:
  target_users:
    - Studenti
    - Výzkumníci
    - Inženýři
  use_cases:
    - Řešení matematických úloh
    - Vědecké výpočty
    - Analýza dat
  avoid_for:
    - Aplikace vyžadující rychlou odezvu
    - Programování
    - Úkoly v češtině (data nejsou k dispozici)
verdict: DeepSeek R1 Distill Qwen 14B je vhodný pro uživatele, kteří potřebují model s vysokou přesností v matematických a vědeckých úlohách a nevadí jim pomalejší odezva. Není vhodný pro programování a aplikace vyžadující rychlou interakci.
categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 65.0
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 37.6
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 47.9
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 16.4
    tier: Slabý
overall_score: 45.3
overall_tier: Průměrný
radar:
  logic_code: 37.6
  agentic: 0
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající v matematice, zejména v náročných úlohách.
  hidden_risk: Pomalá inference může být limitující pro interaktivní aplikace.
  recommended_use_case: Řešení komplexních matematických problémů a vědeckých výpočtů, kde není kladen důraz na rychlost.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 10:52"
---

DeepSeek R1 Distill Qwen 14B je destilovaný velký jazykový model založený na [Qwen 2.5 14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B), využívající výstupy z [DeepSeek R1](/deepseek/deepseek-r1). Překonává o1-mini od OpenAI v různých benchmarkách a dosahuje nových nejlepších výsledků (state-of-the-art) pro husté modely.

Další výsledky benchmarků zahrnují:

- AIME 2024 pass@1: 69.7
- MATH-500 pass@1: 93.9
- CodeForces Rating: 1481

Model využívá jemné doladění (fine-tuning) z výstupů DeepSeek R1, což umožňuje konkurenceschopný výkon srovnatelný s většími špičkovými modely (frontier models).

## Unikátní charakteristiky

DeepSeek R1 Distill Qwen 14B je destilovaný model, který dosahuje vysokých výsledků v matematických úlohách (MATH-500: 94.9%, AIME 2025: 66.7%) a vědeckých testech (GPQA Diamond: 48.4%). Využívá fine-tuning z výstupů DeepSeek R1.

## Silné stránky

### Matematika
Vynikající výsledky v matematických benchmarkách, jako MATH-500 (94.9%) a AIME 2025 (66.7%), naznačují silné schopnosti v řešení matematických problémů.

### Věda
Dobrý výkon v GPQA Diamond (48.4%) ukazuje na schopnost porozumět a řešit složité vědecké otázky.

## Slabé stránky

### Rychlost
Nízká rychlost (TPS: 63.8, TTFT: 0.990s) může omezit použitelnost v aplikacích vyžadujících rychlou odezvu.

### Programování
Slabý výkon v LiveCodeBench (37.6%) a scicode (23.9%) naznačuje omezené schopnosti v oblasti programování.
