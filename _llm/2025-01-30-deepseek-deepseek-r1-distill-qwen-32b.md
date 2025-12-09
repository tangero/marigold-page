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
  - Matematika
  - Věda
strengths:
  - area: Matematika
    description: Vynikající výsledky v matematických benchmarkách, jako MATH-500 (94.1%) a AIME 2025 (68.7%), naznačují silné schopnosti v řešení matematických problémů.
  - area: Věda
    description: Solidní výkon v GPQA Diamond (61.5%) ukazuje na dobrou schopnost porozumět a řešit vědecké otázky.
weaknesses:
  - area: Programování
    description: Slabý výkon v LiveCodeBench (27.0%) naznačuje omezené schopnosti v oblasti programování.
  - area: Rychlost
    description: Nízké TPS (53.1) a relativně vysoká latence (0.582s) znamenají, že model není vhodný pro aplikace vyžadující rychlou odezvu.
competitors:
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Podobná cena
    comparison: Mistral 14B má větší kontext a může být lepší v některých úlohách, ale DeepSeek může mít lepší matematické schopnosti.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Levnější vstup i výstup
    comparison: Grok má mnohem větší kontext (2M tokenů) a je levnější, ale DeepSeek může mít lepší výsledky v matematice a vědě.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: Podobná cena
    comparison: Deepseek v3.2-exp má větší kontext a může být lepší volbou pro delší texty, ale tento model je destilovaný a může mít lepší poměr výkon/cena.
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
    - Programování
    - Aplikace s nízkou latencí
    - Zpracování dlouhých textů
verdict: DeepSeek R1 Distill Qwen 32B je vhodný pro uživatele, kteří potřebují model s dobrými matematickými schopnostmi a jsou ochotni akceptovat pomalejší rychlost a potenciální omezení v oblasti programování a češtiny.
categories:
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
  killer_feature: Vynikající matematické schopnosti
  hidden_risk: Slabá podpora češtiny (data nejsou k dispozici) a pomalá inference
  recommended_use_case: Řešení složitých matematických problémů a vědeckých výpočtů
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 10:53"
---

DeepSeek R1 Distill Qwen 32B je destilovaný velký jazykový model založený na [Qwen 2.5 32B](https://huggingface.co/Qwen/Qwen2.5-32B), využívající výstupy z [DeepSeek R1](/deepseek/deepseek-r1). Překonává o1-mini od OpenAI v různých benchmarkách a dosahuje nových nejlepších výsledků pro husté modely.

Další výsledky benchmarků zahrnují:

- AIME 2024 pass@1: 72.6
- MATH-500 pass@1: 94.3
- CodeForces Rating: 1691

Model využívá doladění z výstupů DeepSeek R1, což umožňuje konkurenceschopný výkon srovnatelný s většími špičkovými modely.

## Unikátní charakteristiky

Model DeepSeek R1 Distill Qwen 32B dosahuje špičkových výsledků v matematických úlohách, zejména v MATH-500 (94.1%) a AIME 2025 (68.7%). Je to destilovaný model, který se snaží dosáhnout srovnatelné výkonnosti s většími modely.

## Silné stránky

### Matematika
Vynikající výsledky v matematických benchmarkách, jako MATH-500 (94.1%) a AIME 2025 (68.7%), naznačují silné schopnosti v řešení matematických problémů.

### Věda
Solidní výkon v GPQA Diamond (61.5%) ukazuje na dobrou schopnost porozumět a řešit vědecké otázky.

## Slabé stránky

### Programování
Slabý výkon v LiveCodeBench (27.0%) naznačuje omezené schopnosti v oblasti programování.

### Rychlost
Nízké TPS (53.1) a relativně vysoká latence (0.582s) znamenají, že model není vhodný pro aplikace vyžadující rychlou odezvu.
