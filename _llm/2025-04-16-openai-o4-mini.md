---
layout: llm_review
title: "OpenAI: o4 Mini"
date: "2025-04-16 18:29:02"
model_id: openai/o4-mini
slug: openai-o4-mini
provider: Openai
pricing:
  prompt_per_m: 1.1
  completion_per_m: 4.4
  blend_per_m: 1.925
context_length: 200,000
max_output: 100,000
input_modalities:
  - image
  - text
  - file
output_modalities:
  - text
focus:
  - Věda a matematika
  - Programování
strengths:
  - area: Věda a matematika
    description: Model dosahuje vynikajících výsledků v matematických úlohách, s benchmarky jako MATH-500 (98.9%) a AIME 2025 (94.0%).
  - area: Programování
    description: Vysoké skóre v LiveCodeBench (85.9%) naznačuje silné schopnosti v oblasti kódování a řešení programovacích úloh.
weaknesses:
  - area: Rychlost
    description: Model má slabou rychlost inference, s TPS 107.9 a TTFT 65.881s, což ho činí pomalejším než konkurenční modely.
  - area: Čeština
    description: Chybí data pro hodnocení výkonu v češtině (MMMLU), což omezuje jeho použitelnost pro české uživatele.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Podobná cena vstupu, vyšší cena výstupu
    comparison: Claude Haiku je rychlejší, ale o4-mini má lepší matematické schopnosti.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Mnohem levnější vstup i výstup
    comparison: Gemini 2.5 Flash je výrazně levnější, ale o4-mini má lepší výsledky v náročnějších úlohách.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: Mnohem levnější vstup i výstup
    comparison: Mistral 8B je levnější, ale o4-mini má lepší výsledky v matematice a kódování.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Levnější vstup i výstup
    comparison: Deepseek V3.2 je levnější, ale o4-mini má větší kontextové okno a lepší výsledky v některých benchmarkách.
recommendation:
  target_users:
    - Výzkumníci
    - Vývojáři aplikací
  use_cases:
    - Řešení matematických problémů
    - Generování kódu
  avoid_for:
    - Aplikace vyžadující nízkou latenci
    - Použití v češtině
verdict: OpenAI o4-mini je vhodný pro uživatele, kteří potřebují silný model pro matematické a programovací úlohy a nevadí jim pomalejší rychlost a absence podpory češtiny.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 88.7
    tier: Výborný
  coding:
    name: Programování
    icon: 💻
    score: 85.9
    tier: Výborný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 55.6
    tier: Průměrný
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 58.6
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 27.0
    tier: Slabý
overall_score: 69.5
overall_tier: Dobrý
radar:
  logic_code: 87.3
  agentic: 55.6
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající matematické schopnosti
  hidden_risk: Pomalá inference a nedostatečná podpora češtiny
  recommended_use_case: Řešení komplexních matematických úloh a generování kódu v angličtině
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:03"
---

OpenAI o4-mini je kompaktní model pro usuzování v o-sérii, optimalizovaný pro rychlý a nákladově efektivní výkon při zachování silných multimodálních a agentních schopností. Podporuje používání nástrojů a vykazuje konkurenceschopný výkon v usuzování a kódování v benchmarkách jako AIME (99,5 % s Pythonem) a SWE-bench, překonává svého předchůdce o3-mini a v některých oblastech se dokonce blíží o3.

Navzdory své menší velikosti vykazuje o4-mini vysokou přesnost v úlohách STEM, vizuálním řešení problémů (např. MathVista, MMMU) a úpravách kódu. Je obzvláště vhodný pro scénáře s vysokou propustností, kde je latence nebo cena kritická. Díky své efektivní architektuře a vylepšenému tréninku pomocí posilování se o4-mini dokáže řetězit nástroje, generovat strukturované výstupy a řešit vícestupňové úlohy s minimálním zpožděním – často i za méně než minutu.

## Unikátní charakteristiky

OpenAI o4-mini je optimalizovaný pro rychlost a efektivitu nákladů, přičemž si zachovává silné multimodální a agentní schopnosti. Vyniká ve STEM úlohách a kódování, jak dokazují benchmarky AIME a LiveCodeBench.

## Silné stránky

### Věda a matematika
Model dosahuje vynikajících výsledků v matematických úlohách, s benchmarky jako MATH-500 (98.9%) a AIME 2025 (94.0%).

### Programování
Vysoké skóre v LiveCodeBench (85.9%) naznačuje silné schopnosti v oblasti kódování a řešení programovacích úloh.

## Slabé stránky

### Rychlost
Model má slabou rychlost inference, s TPS 107.9 a TTFT 65.881s, což ho činí pomalejším než konkurenční modely.

### Čeština
Chybí data pro hodnocení výkonu v češtině (MMMLU), což omezuje jeho použitelnost pro české uživatele.
