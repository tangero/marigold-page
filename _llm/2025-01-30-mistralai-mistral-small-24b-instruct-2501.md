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
  - Rychlá inference
  - Obecné AI úlohy
strengths:
  - area: Rychlost
    description: Vysoká rychlost inference s TPS 116.2 a nízkou latencí 0.294s umožňuje rychlé zpracování požadavků.
  - area: Kontext
    description: Kontext 32,768 tokenů je dostatečný pro většinu RAG úloh a umožňuje zpracování delších dokumentů.
weaknesses:
  - area: Věda a matematika
    description: Relativně nízké skóre v GPQA Diamond (38.1%) a AIME 2025 (6.3%) naznačuje slabší schopnosti v náročných vědeckých a matematických úlohách.
  - area: Programování
    description: Nízké skóre v LiveCodeBench (14.1%) a scicode (15.6%) naznačuje omezené schopnosti v generování a porozumění kódu.
competitors:
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: 6x levnější vstup, 44x levnější výstup
    comparison: Gemini 2.5 Flash je výrazně levnější, ale může mít nižší kvalitu výstupu pro komplexní úlohy.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 4x levnější vstup, 220x levnější výstup
    comparison: Grok-4.1-fast je mnohem levnější a má obrovský kontext, ale může mít nižší kvalitu výstupu pro komplexní úlohy.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: 1.4x levnější vstup, 3.4x levnější výstup
    comparison: Deepseek v3.2-exp nabízí podobný kontext a může být levnější, ale je třeba porovnat kvalitu výstupu.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: 3x levnější vstup, 0.7x levnější výstup
    comparison: Ministral-8b-2512 je levnější, má větší kontext, ale může mít nižší výkon v některých úlohách.
recommendation:
  target_users:
    - Vývojáři aplikací s důrazem na rychlost
    - Firmy hledající efektivní model pro obecné AI úlohy
  use_cases:
    - Chatboti
    - Rychlá sumarizace textu
    - Generování obsahu s nízkou latencí
  avoid_for:
    - Náročné vědecké výpočty
    - Generování komplexního kódu
    - Úlohy vyžadující hluboké logické uvažování
verdict: Mistral Small 3 je vhodný pro aplikace, kde je prioritou rychlost a efektivita. Je ideální pro obecné AI úlohy, ale méně vhodný pro specializované úkoly vyžadující hluboké znalosti.
benchmark_categories:
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
  killer_feature: Vynikající poměr rychlosti a ceny
  hidden_risk: Slabší výkon v úlohách vyžadujících hluboké znalosti a logické uvažování
  recommended_use_case: Rychlé generování textu a chatbot aplikace, kde je klíčová nízká latence.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 11:02"
---

Mistral Small 3 je jazykový model s 24 miliardami parametrů optimalizovaný pro nízkou latenci při běžných úlohách umělé inteligence. Je vydán pod licencí Apache 2.0 a nabízí jak předtrénovanou, tak i instrukčně doladěnou verzi, navržené pro efektivní lokální nasazení.

Model dosahuje 81% přesnosti v benchmarku MMLU a výkonem konkuruje větším modelům, jako jsou Llama 3.3 70B a Qwen 32B, přičemž na ekvivalentním hardwaru pracuje třikrát rychleji. [Přečtěte si blogový příspěvek o modelu zde.](https://mistral.ai/news/mistral-small-3/)

## Unikátní charakteristiky

Mistral Small 3 je optimalizován pro nízkou latenci a rychlou inferenci. Dosahuje konkurenceschopných výsledků v MMLU benchmarku a nabízí velký kontext 32,768 tokenů. Jeho rychlost je 3x vyšší než u větších modelů na stejném hardwaru.

## Silné stránky

### Rychlost
Vysoká rychlost inference s TPS 116.2 a nízkou latencí 0.294s umožňuje rychlé zpracování požadavků.

### Kontext
Kontext 32,768 tokenů je dostatečný pro většinu RAG úloh a umožňuje zpracování delších dokumentů.

## Slabé stránky

### Věda a matematika
Relativně nízké skóre v GPQA Diamond (38.1%) a AIME 2025 (6.3%) naznačuje slabší schopnosti v náročných vědeckých a matematických úlohách.

### Programování
Nízké skóre v LiveCodeBench (14.1%) a scicode (15.6%) naznačuje omezené schopnosti v generování a porozumění kódu.
