---
layout: llm_review
title: "OpenAI: o3 Mini High"
date: "2025-02-12 16:03:31"
model_id: openai/o3-mini-high
slug: openai-o3-mini-high
provider: Openai
pricing:
  prompt_per_m: 1.1
  completion_per_m: 4.4
  blend_per_m: 1.925
context_length: 200,000
max_output: 100,000
input_modalities:
  - text
  - file
output_modalities:
  - text
focus:
  - Věda
  - Matematika
  - Programování
strengths:
  - area: Věda a Matematika
    description: Vynikající výsledky v matematických úlohách, dosahuje 98.5% v MATH-500 a 86.0% v AIME 2025.
  - area: Programování
    description: Dobrý výkon v kódovacích úlohách s LiveCodeBench skóre 73.4%.
weaknesses:
  - area: Rychlost
    description: Nízká rychlost zpracování, TPS 142.4 a TTFT 59.851s, což je pomalé v porovnání s konkurencí.
  - area: Agenti a Nástroje
    description: Slabý výkon v úlohách agentů, τ2-Bench skóre pouze 31.3%.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Podobná cena vstupu, vyšší cena výstupu
    comparison: Claude Haiku je rychlejší, ale o3-mini-high má lepší výsledky ve vědeckých a matematických úlohách.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Levnější vstup i výstup
    comparison: Gemini 2.5 Flash je levnější, ale o3-mini-high má větší kontextové okno a lepší výsledky ve specializovaných úlohách.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: Mnohem levnější vstup i výstup
    comparison: Mistral 8B je výrazně levnější, ale o3-mini-high dosahuje lepších výsledků ve vědeckých a matematických benchmarkách.
recommendation:
  target_users:
    - Výzkumníci
    - Vývojáři STEM aplikací
    - Studenti
  use_cases:
    - Řešení matematických problémů
    - Generování kódu pro vědecké simulace
    - Analýza dat
  avoid_for:
    - Úkoly vyžadující rychlou odezvu
    - Aplikace s rozsáhlou interakcí s agenty
    - Úlohy vyžadující multimodalitu
verdict: OpenAI o3-mini-high je vhodný pro uživatele, kteří potřebují spolehlivý model pro vědecké a matematické úlohy a jsou ochotni akceptovat pomalejší rychlost zpracování.
categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 85.0
    tier: Výborný
  coding:
    name: Programování
    icon: 💻
    score: 73.4
    tier: Dobrý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 31.3
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 54.7
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 35.6
    tier: Slabý
overall_score: 58.3
overall_tier: Průměrný
radar:
  logic_code: 73.4
  agentic: 31.3
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající výsledky v matematických úlohách (MATH-500, AIME 2025).
  hidden_risk: Pomalá inference může být limitující pro interaktivní aplikace.
  recommended_use_case: Řešení složitých matematických a vědeckých problémů, kde je přesnost důležitější než rychlost.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 10:54"
---

OpenAI o3-mini-high je stejný model jako [o3-mini](/openai/o3-mini) s nastaveným parametrem reasoning_effort na hodnotu high.

o3-mini je nákladově efektivní jazykový model optimalizovaný pro úlohy STEM usuzování, přičemž vyniká zejména ve vědě, matematice a kódování. Model nabízí tři nastavitelné úrovně úsilí usuzování a podporuje klíčové vývojářské funkce, včetně volání funkcí, strukturovaných výstupů a streamování, nicméně nezahrnuje schopnosti zpracování obrazu.

Model vykazuje významné zlepšení oproti svému předchůdci, přičemž odborní testeři preferovali jeho odpovědi v 56 % případů a zaznamenali 39% snížení závažných chyb u složitých otázek. S nastavením středního úsilí usuzování (medium reasoning effort) dosahuje o3-mini výkonu většího modelu o1 v náročných hodnoceních usuzování, jako jsou AIME a GPQA, při zachování nižší latence a nákladů.

## Unikátní charakteristiky

OpenAI o3-mini-high je optimalizovaný pro STEM úlohy a nabízí tři úrovně úsilí při odvozování. Dosahuje lepších výsledků než jeho předchůdce a snižuje množství chyb u složitých otázek. Podporuje function calling a strukturované výstupy.

## Silné stránky

### Věda a Matematika
Vynikající výsledky v matematických úlohách, dosahuje 98.5% v MATH-500 a 86.0% v AIME 2025.

### Programování
Dobrý výkon v kódovacích úlohách s LiveCodeBench skóre 73.4%.

## Slabé stránky

### Rychlost
Nízká rychlost zpracování, TPS 142.4 a TTFT 59.851s, což je pomalé v porovnání s konkurencí.

### Agenti a Nástroje
Slabý výkon v úlohách agentů, τ2-Bench skóre pouze 31.3%.
