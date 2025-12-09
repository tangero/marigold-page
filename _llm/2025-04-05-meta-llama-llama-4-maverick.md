---
layout: llm_review
title: "Meta: Llama 4 Maverick"
date: "2025-04-05 21:37:02"
model_id: meta-llama/llama-4-maverick
slug: meta-llama-llama-4-maverick
provider: Meta
pricing:
  prompt_per_m: 0.136
  completion_per_m: 0.68
  blend_per_m: 0.272
context_length: 1,048,576
max_output: 8,192
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Multimodální interakce
  - Vysoká propustnost
strengths:
  - area: Věda a matematika
    description: Vynikající výsledky ve vědeckých a matematických benchmarkách, jako je GPQA Diamond (67.1%) a MATH-500 (88.9%).
  - area: Kontextové okno
    description: Velké kontextové okno (1,048,576 tokenů) umožňuje zpracovávat rozsáhlé dokumenty a složité konverzace.
weaknesses:
  - area: Programování
    description: Slabší výsledky v programovacích benchmarkách (LiveCodeBench 39.7%).
  - area: Logické uvažování
    description: Velmi nízké skóre v benchmarku HLE (4.8%) naznačuje problémy s hard logic.
competitors:
  - provider: Anthropic
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: Výrazně dražší (cca 35x vstup, 36x výstup)
    comparison: Claude Opus je silnější v obecné inteligenci, ale dražší.
  - provider: Google
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Dražší (cca 14x vstup, 17x výstup)
    comparison: Gemini 3 Pro nabízí multimodální schopnosti, ale za vyšší cenu.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Levnější (cca 1.4x vstup, 2.7x levnější výstup)
    comparison: Grok nabízí větší kontextové okno a nižší cenu, ale pravděpodobně nižší výkon v náročnějších úlohách.
  - provider: MistralAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Podobná cena vstupu, výrazně levnější výstup
    comparison: Ministral 14B je levnější na výstup, ale nemá multimodální schopnosti.
recommendation:
  target_users:
    - Výzkumníci
    - Data scientists
  use_cases:
    - Analýza vědeckých dat
    - Zpracování rozsáhlých dokumentů
  avoid_for:
    - Vývoj aplikací vyžadujících robustní logické uvažování
    - Úkoly s vysokými nároky na programování
verdict: Llama 4 Maverick je vhodný pro výzkumníky a data scientisty, kteří potřebují zpracovávat velké objemy dat a využívat multimodální vstupy, ale měli by zvážit jeho slabší stránky v logice a programování.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 60.2
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 39.7
    tier: Slabý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 17.8
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 52.4
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 61.4
    tier: Dobrý
overall_score: 44.6
overall_tier: Průměrný
radar:
  logic_code: 50.0
  agentic: 17.8
  languages: 0
  safety: 0
  speed: Dobrý
expert_verdict:
  killer_feature: Velké kontextové okno a multimodální schopnosti
  hidden_risk: Slabší logické uvažování a programovací schopnosti mohou omezit použitelnost v některých aplikacích.
  recommended_use_case: Analýza vědeckých článků a extrakce informací z obrázků.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:01"
---

Llama 4 Maverick 17B Instruct (128E) je velkokapacitní multimodální jazykový model od společnosti Meta, postavený na architektuře mixture-of-experts (MoE) se 128 experty a 17 miliardami aktivních parametrů na jeden průchod dopřednou sítí (celkem 400B). Podporuje multijazyčný textový a obrazový vstup a produkuje multijazyčný textový a kódový výstup ve 12 podporovaných jazycích. Maverick, optimalizovaný pro úlohy vidění a jazyka, je doladěn pomocí instrukcí pro chování podobné asistentovi, obrazové usuzování a všeobecnou multimodální interakci.

Maverick využívá ranou fúzi pro nativní multimodalitu a kontextové okno o velikosti 1 milionu tokenů. Byl trénován na kurátorské směsi veřejných, licencovaných a Meta-platform dat, pokrývající ~22 bilionů tokenů, s datovým cut-off v srpnu 2024. Maverick, vydaný 5. dubna 2025 pod licencí Llama 4 Community License, je vhodný pro výzkumné a komerční aplikace vyžadující pokročilé multimodální porozumění a vysokou propustnost modelu.

## Unikátní charakteristiky

Llama 4 Maverick je multimodální model s velkým kontextovým oknem (1 milion tokenů) a architekturou MoE. Vyniká ve vědeckých úlohách (GPQA Diamond 67.1%, MATH-500 88.9%), ale má slabší výsledky v logice a programování.

## Silné stránky

### Věda a matematika
Vynikající výsledky ve vědeckých a matematických benchmarkách, jako je GPQA Diamond (67.1%) a MATH-500 (88.9%).

### Kontextové okno
Velké kontextové okno (1,048,576 tokenů) umožňuje zpracovávat rozsáhlé dokumenty a složité konverzace.

## Slabé stránky

### Programování
Slabší výsledky v programovacích benchmarkách (LiveCodeBench 39.7%).

### Logické uvažování
Velmi nízké skóre v benchmarku HLE (4.8%) naznačuje problémy s hard logic.
