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
  - Věda
  - Matematika
strengths:
  - area: Matematika
    description: Vysoké skóre v matematických benchmarkách MATH-500 (94.9%) a AIME 2025 (66.7%) naznačuje silné schopnosti v řešení matematických problémů.
  - area: Znalosti
    description: Dobrý výsledek v MMLU Pro (74.0%) ukazuje na solidní úroveň znalostí.
weaknesses:
  - area: Rychlost
    description: "Nízká rychlost zpracování (TPS: 63.8, TTFT: 0.990s) omezuje použitelnost v aplikacích vyžadujících rychlou odezvu."
  - area: Programování
    description: Slabé skóre v LiveCodeBench (37.6%) naznačuje omezené schopnosti v oblasti programování.
competitors:
  - provider: MISTRALAI
    model: ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Podobná cena
    comparison: Podobný kontext, ale potenciálně lepší rychlost (data nejsou k dispozici). Nutno otestovat v reálném provozu.
  - provider: MISTRALAI
    model: ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: Levnější
    comparison: Menší model, ale potenciálně rychlejší a levnější. Záleží na konkrétních požadavcích na přesnost.
  - provider: GOOGLE
    model: gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Mírně dražší vstup, výrazně dražší výstup
    comparison: Podobný kontext, ale potenciálně lepší v multimodálních úlohách (pokud jsou potřeba).
  - provider: DEEPSEEK
    model: deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: Dražší vstup, dražší výstup
    comparison: Větší kontext, ale vyšší cena. Záleží na potřebě delšího kontextu.
recommendation:
  target_users:
    - Výzkumníci v oblasti matematiky
    - Studenti a učitelé matematiky
    - Analytici dat
  use_cases:
    - Řešení matematických úloh
    - Analýza dat vyžadující matematické operace
    - Vzdělávací aplikace
  avoid_for:
    - Aplikace vyžadující rychlou odezvu
    - Úlohy s komplexním programováním
    - Aplikace vyžadující silnou podporu češtiny (data nejsou k dispozici)
verdict: DeepSeek R1 Distill Qwen 14B je vhodný pro uživatele, kteří potřebují model s vysokou přesností v matematických úlohách a nevadí jim pomalejší rychlost zpracování.
benchmark_categories:
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
  killer_feature: Vynikající v matematických úlohách
  hidden_risk: Pomalá inference může omezit použitelnost v reálném čase
  recommended_use_case: Řešení složitých matematických problémů a validace matematických modelů
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 11:01"
---

DeepSeek R1 Distill Qwen 14B je destilovaný velký jazykový model založený na [Qwen 2.5 14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B), využívající výstupy z [DeepSeek R1](/deepseek/deepseek-r1). Překonává o1-mini od OpenAI v různých benchmarkách a dosahuje nových nejlepších výsledků (state-of-the-art) pro husté modely.

Další výsledky benchmarků zahrnují:

- AIME 2024 pass@1: 69.7
- MATH-500 pass@1: 93.9
- CodeForces Rating: 1481

Model využívá jemné doladění (fine-tuning) z výstupů DeepSeek R1, což umožňuje konkurenceschopný výkon srovnatelný s většími špičkovými modely (frontier models).

## Unikátní charakteristiky

DeepSeek R1 Distill Qwen 14B je destilovaný model, který dosahuje vysokých skóre v matematických úlohách (MATH-500: 94.9%, AIME 2025: 66.7%). Vyniká v porovnání s jinými modely stejné velikosti, ale jeho rychlost je poměrně nízká.

## Silné stránky

### Matematika
Vysoké skóre v matematických benchmarkách MATH-500 (94.9%) a AIME 2025 (66.7%) naznačuje silné schopnosti v řešení matematických problémů.

### Znalosti
Dobrý výsledek v MMLU Pro (74.0%) ukazuje na solidní úroveň znalostí.

## Slabé stránky

### Rychlost
Nízká rychlost zpracování (TPS: 63.8, TTFT: 0.990s) omezuje použitelnost v aplikacích vyžadujících rychlou odezvu.

### Programování
Slabé skóre v LiveCodeBench (37.6%) naznačuje omezené schopnosti v oblasti programování.
