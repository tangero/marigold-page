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
    description: Vysoká rychlost zpracování s 116.2 tokeny za sekundu a nízkou latencí 0.294s.
  - area: Cena
    description: Relativně nízká cena ve srovnání s jinými modely s podobnými schopnostmi.
weaknesses:
  - area: Věda a matematika
    description: Slabé výsledky v oblasti vědy a matematiky (29.0/100).
  - area: Programování
    description: Slabé výsledky v programování (14.1/100).
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: 20x levnější vstup, 45x levnější výstup
    comparison: Claude Haiku je levnější, ale pravděpodobně méně inteligentní. Vhodné pro nenáročné úlohy.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: 6x levnější vstup, 44x levnější výstup
    comparison: Gemini 2.5 Flash je výrazně levnější, ale může mít nižší kvalitu výstupu.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 2.5x levnější vstup, 22x levnější výstup
    comparison: Grok-4.1-fast nabízí delší kontext a je levnější, ale nemusí dosahovat stejné úrovně inteligence.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: 3x levnější vstup, 7x levnější výstup
    comparison: Ministral-8b-2512 je levnější a má delší kontext, ale může mít nižší výkon v některých úlohách.
recommendation:
  target_users:
    - Vývojáři aplikací s nízkou latencí
    - Firmy hledající efektivní řešení pro obecné AI úlohy
  use_cases:
    - Chatboti
    - Generování textu
    - Rychlá analýza dat
  avoid_for:
    - Úlohy vyžadující hluboké vědecké znalosti
    - Složité programovací úlohy
verdict: Mistral Small 3 je vhodný pro aplikace, kde je klíčová rychlost a efektivita, ale je třeba zvážit jeho slabší výkon v náročnějších úlohách, jako je věda a programování.
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
overall_score: 28.9
overall_tier: Slabý
radar:
  logic_code: 21.6
  agentic: 0
  languages: 0
  safety: 0
  speed: Dobrý
expert_verdict:
  killer_feature: Vysoká rychlost inference
  hidden_risk: Slabší výkon v oblastech vědy, matematiky a programování
  recommended_use_case: Rychlé generování textu pro chatboty a automatizaci zákaznické podpory
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 12:57"
---

Mistral Small 3 je jazykový model s 24 miliardami parametrů optimalizovaný pro nízkou latenci při běžných úlohách umělé inteligence. Je vydán pod licencí Apache 2.0 a nabízí předtrénované i instrukčně doladěné verze navržené pro efektivní lokální nasazení.

Model dosahuje 81% přesnosti v benchmarku MMLU a výkonnostně konkuruje větším modelům, jako jsou Llama 3.3 70B a Qwen 32B, přičemž na ekvivalentním hardwaru pracuje třikrát rychleji. [Přečtěte si blogový příspěvek o modelu zde.](https://mistral.ai/news/mistral-small-3/)

## Unikátní charakteristiky

Mistral Small 3 je optimalizován pro nízkou latenci a dosahuje konkurenceschopných výsledků s většími modely, jako je Llama 3 70B, ale s trojnásobnou rychlostí na stejném hardwaru. Dosahuje 81% přesnosti na benchmarku MMLU.

## Silné stránky

### Rychlost
Vysoká rychlost zpracování s 116.2 tokeny za sekundu a nízkou latencí 0.294s.

### Cena
Relativně nízká cena ve srovnání s jinými modely s podobnými schopnostmi.

## Slabé stránky

### Věda a matematika
Slabé výsledky v oblasti vědy a matematiky (29.0/100).

### Programování
Slabé výsledky v programování (14.1/100).
