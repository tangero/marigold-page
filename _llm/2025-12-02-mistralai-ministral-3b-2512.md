---
layout: llm_review
title: "Mistral: Ministral 3 3B 2512"
date: "2025-12-02 14:19:20"
model_id: mistralai/ministral-3b-2512
slug: mistralai-ministral-3b-2512
provider: Mistral
pricing:
  prompt_per_m: 0.1
  completion_per_m: 0.1
  blend_per_m: 0.1
context_length: 131,072
max_output: N/A
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Rychlá inference
  - Multimodalita
strengths:
  - area: Rychlost
    description: Model dosahuje výborné rychlosti inference (309.9 tokenů/s) a nízké latence (0.263s), což ho předurčuje pro aplikace s požadavkem na rychlou odezvu.
  - area: Cena
    description: Model nabízí velmi nízkou cenu za vstup i výstup ($0.10/1M tokenů), což z něj činí atraktivní volbu pro rozsáhlé nasazení.
weaknesses:
  - area: Obecná inteligence
    description: Model dosahuje slabých výsledků v benchmarkách zaměřených na obecnou inteligenci (celkové skóre 36.3/100), což omezuje jeho použitelnost pro komplexní úlohy.
  - area: Programování
    description: Výsledky v programovacích benchmarkách (LiveCodeBench 24.7/100) jsou slabé, což naznačuje omezené schopnosti v generování a porozumění kódu.
competitors:
  - provider: X-AI
    model: grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 2x levnější vstup, 5x levnější výstup
    comparison: Grok-4.1-fast nabízí mnohem větší kontextové okno (2,000,000 tokenů) a lepší poměr cena/výkon, ale postrádá multimodalitu.
  - provider: MISTRALAI
    model: ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: 1.5x dražší vstup i výstup
    comparison: Ministral-8b-2512 je větší model s potenciálně lepšími schopnostmi, ale za vyšší cenu. Nemá multimodalitu.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: 3x dražší vstup, 25x dražší výstup
    comparison: Gemini 2.5 Flash Image je dražší, ale nabízí multimodalitu a potenciálně lepší výkon v některých oblastech. Má menší kontext.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: 2.1x dražší vstup, 3.2x dražší výstup
    comparison: Deepseek v3.2-exp je dražší, ale může nabídnout lepší výkon v programování a dalších oblastech. Nemá multimodalitu.
recommendation:
  target_users:
    - Vývojáři prototypů
    - Aplikace s nízkými nároky na inteligenci
  use_cases:
    - Rychlá extrakce klíčových slov z obrázků
    - Jednoduché chatboty
  avoid_for:
    - Generování kódu
    - Složité logické úlohy
verdict: Ministral 3 3B je vhodný pro aplikace, kde je prioritou rychlost a nízká cena, a kde nejsou kladeny vysoké nároky na inteligenci modelu. Multimodalita je plus, ale celkové schopnosti jsou omezené.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 35.8
    tier: Slabý
  coding:
    name: Programování
    icon: 💻
    score: 24.7
    tier: Slabý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 24.9
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 34.7
    tier: Slabý
  speed:
    name: Rychlost
    icon: ⚡
    score: 86.8
    tier: Výborný
overall_score: 36.3
overall_tier: Slabý
radar:
  logic_code: 16.6
  agentic: 24.9
  languages: 0
  safety: 0
  speed: Výborný
expert_verdict:
  killer_feature: Rychlost a nízká cena
  hidden_risk: Slabé výsledky v benchmarkách naznačují omezenou použitelnost pro komplexní úlohy. Data pro češtinu nejsou k dispozici.
  recommended_use_case: Rychlá analýza obrázků pro extrakci klíčových informací v aplikacích s omezeným rozpočtem.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:20"
---

Ministral 3 3B, nejmenší model z rodiny Ministral 3, je výkonný a efektivní malý jazykový model s vizuálními schopnostmi.

## Unikátní charakteristiky

Ministral 3 3B je malý, ale efektivní jazykový model s vizuálními schopnostmi. Vyniká rychlostí inference (309.9 tokenů/s) a nízkou latencí (0.263s), což ho činí vhodným pro aplikace vyžadující rychlou odezvu. Jeho celkové skóre je však slabé, což naznačuje omezené schopnosti v náročnějších úlohách.

## Silné stránky

### Rychlost
Model dosahuje výborné rychlosti inference (309.9 tokenů/s) a nízké latence (0.263s), což ho předurčuje pro aplikace s požadavkem na rychlou odezvu.

### Cena
Model nabízí velmi nízkou cenu za vstup i výstup ($0.10/1M tokenů), což z něj činí atraktivní volbu pro rozsáhlé nasazení.

## Slabé stránky

### Obecná inteligence
Model dosahuje slabých výsledků v benchmarkách zaměřených na obecnou inteligenci (celkové skóre 36.3/100), což omezuje jeho použitelnost pro komplexní úlohy.

### Programování
Výsledky v programovacích benchmarkách (LiveCodeBench 24.7/100) jsou slabé, což naznačuje omezené schopnosti v generování a porozumění kódu.
