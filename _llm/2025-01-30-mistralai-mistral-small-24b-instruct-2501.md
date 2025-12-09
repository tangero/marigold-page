---
layout: llm_review
title: "Mistral: Mistral Small 3"
date: "2025-01-30 17:43:29"
model_id: mistralai/mistral-small-24b-instruct-2501
slug: mistralai-mistral-small-24b-instruct-2501
provider: Mistral
pricing:
  prompt_per_m: 0.03
  completion_per_m: 0.11
  blend_per_m: 0.05
context_length: 32,768
max_output: 32,768
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Nízká latence
  - Obecné AI úlohy
strengths:
  - area: Rychlost
    description: Vysoká rychlost zpracování s TPS 116.2 a nízkou latencí 0.294s, což je vhodné pro aplikace vyžadující rychlou odezvu.
  - area: Obecná inteligence
    description: Solidní výkon v MMLU s 52.9%, což naznačuje dobrou schopnost porozumění a řešení úloh v různých oblastech.
weaknesses:
  - area: Věda a matematika
    description: Slabé skóre ve vědeckých a matematických úlohách (GPQA Diamond 38.1%, AIME 2025 6.3%) omezuje jeho použitelnost pro specializované vědecké výpočty.
  - area: Programování
    description: Nízké skóre v programovacích benchmarcích (LiveCodeBench 14.1%, scicode 15.6%) naznačuje omezenou schopnost generovat a rozumět kódu.
competitors:
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Podobná cena vstupu, výrazně levnější výstup
    comparison: Gemini 2.5 Flash je levnější na výstup, ale může mít horší výkon v některých oblastech.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Výrazně levnější vstup i výstup
    comparison: Grok-4.1-fast je mnohem levnější, ale může mít nižší kvalitu výstupu a menší kontextové okno.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: Podobná cena vstupu, levnější výstup
    comparison: Deepseek v3.2-exp nabízí podobný výkon za nižší cenu výstupu, ale má menší kontextové okno.
recommendation:
  target_users:
    - Vývojáři aplikací s nízkou latencí
    - Podniky hledající efektivní řešení pro obecné AI úlohy
  use_cases:
    - Chatboti
    - Rychlá sumarizace textu
  avoid_for:
    - Náročné vědecké výpočty
    - Generování komplexního kódu
verdict: Mistral Small 3 je vhodný pro aplikace, kde je klíčová rychlost a nízká latence, ale je třeba počítat s omezenými schopnostmi v oblasti vědy, matematiky a programování.
categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 29.0
    tier: Slabý
  coding:
    name: Programování
    icon: 💻
    score: 14.1
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 34.7
    tier: Slabý
  speed:
    name: Rychlost
    icon: ⚡
    score: 64.3
    tier: Dobrý
overall_score: 31.4
overall_tier: Slabý
radar:
  logic_code: 21.6
  agentic: 0
  languages: 0
  safety: 0
  speed: Dobrý
expert_verdict:
  killer_feature: Nízká latence
  hidden_risk: Slabší výkon v úlohách vyžadujících hluboké logické uvažování a programování.
  recommended_use_case: Rychlé generování textu a odpovědí v chatbotovi.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 10:53"
---

Mistral Small 3 je jazykový model s 24 miliardami parametrů optimalizovaný pro nízkou latenci při běžných úlohách umělé inteligence. Je vydán pod licencí Apache 2.0 a nabízí předtrénované i instrukčně doladěné verze navržené pro efektivní lokální nasazení.

Model dosahuje 81% přesnosti v benchmarku MMLU a výkonem konkuruje větším modelům, jako jsou Llama 3.3 70B a Qwen 32B, přičemž na ekvivalentním hardwaru pracuje třikrát rychleji.

## Unikátní charakteristiky

Mistral Small 3 je optimalizován pro nízkou latenci a dosahuje konkurenceschopných výsledků s většími modely, jako je Llama 3 70B, při trojnásobné rychlosti na stejném hardwaru. Dosahuje 81% přesnosti na benchmarku MMLU.

## Silné stránky

### Rychlost
Vysoká rychlost zpracování s TPS 116.2 a nízkou latencí 0.294s, což je vhodné pro aplikace vyžadující rychlou odezvu.

### Obecná inteligence
Solidní výkon v MMLU s 52.9%, což naznačuje dobrou schopnost porozumění a řešení úloh v různých oblastech.

## Slabé stránky

### Věda a matematika
Slabé skóre ve vědeckých a matematických úlohách (GPQA Diamond 38.1%, AIME 2025 6.3%) omezuje jeho použitelnost pro specializované vědecké výpočty.

### Programování
Nízké skóre v programovacích benchmarcích (LiveCodeBench 14.1%, scicode 15.6%) naznačuje omezenou schopnost generovat a rozumět kódu.
