---
layout: llm_review
title: "OpenAI: o3 Mini"
date: "2025-01-31 20:28:41"
model_id: openai/o3-mini
slug: openai-o3-mini
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
  - area: Matematika
    description: Vynikající výsledky v matematických úlohách, dosahuje 97.3% v MATH-500 a 77.0% v AIME 2025.
  - area: Programování
    description: Solidní výkon v kódování s LiveCodeBench skóre 71.7%.
  - area: Věda
    description: Vysoké skóre v GPQA Diamond (74.8%) naznačuje silné vědecké znalosti.
weaknesses:
  - area: Rychlost
    description: Nízká rychlost zpracování, TPS 140.1 a TTFT 18.052s, což je pomalé.
  - area: Agenti a nástroje
    description: Slabý výkon v úlohách agentů, τ2-Bench skóre pouze 28.7%.
  - area: Čeština
    description: Data pro češtinu nejsou k dispozici, nelze posoudit kvalitu v českém jazyce.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Podobná cena vstupu, vyšší cena výstupu
    comparison: Claude Haiku je rychlejší, ale o3-mini má lepší výsledky v matematice a programování.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Levnější vstup i výstup
    comparison: Gemini Flash je levnější, ale o3-mini má větší kontextové okno a lepší výsledky ve vědeckých úlohách.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: Výrazně levnější vstup i výstup
    comparison: Ministral-8b je mnohem levnější, ale o3-mini má lepší výsledky v matematice a programování.
recommendation:
  target_users:
    - Studenti
    - Výzkumníci
    - Vývojáři
  use_cases:
    - Řešení matematických úloh
    - Vědecké výpočty
    - Generování kódu
  avoid_for:
    - Úlohy vyžadující rychlou odezvu
    - Složité úlohy agentů
    - Aplikace vyžadující silnou podporu češtiny
verdict: OpenAI o3-mini je dobrá volba pro uživatele, kteří hledají cenově efektivní model pro vědecké a matematické úlohy, ale měli by zvážit jeho pomalou rychlost a omezenou podporu pro agenty.
categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 80.2
    tier: Výborný
  coding:
    name: Programování
    icon: 💻
    score: 71.7
    tier: Dobrý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 28.7
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 52.7
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 35.0
    tier: Slabý
overall_score: 55.7
overall_tier: Průměrný
radar:
  logic_code: 76.0
  agentic: 28.7
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající v matematice a vědě za rozumnou cenu.
  hidden_risk: Pomalá inference může být problém pro interaktivní aplikace.
  recommended_use_case: Řešení matematických a vědeckých problémů, kde není kritická rychlost odezvy.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 10:53"
---

OpenAI o3-mini je nákladově efektivní jazykový model optimalizovaný pro úlohy STEM uvažování, přičemž vyniká zejména ve vědě, matematice a kódování.

Tento model podporuje parametr `reasoning_effort`, který lze nastavit na "high", "medium" nebo "low" pro řízení doby přemýšlení modelu. Výchozí hodnota je "medium". OpenRouter také nabízí model slug `openai/o3-mini-high` pro nastavení parametru na výchozí hodnotu "high".

Model nabízí tři nastavitelné úrovně úsilí uvažování a podporuje klíčové vývojářské funkce, včetně volání funkcí, strukturovaných výstupů a streamování, i když nezahrnuje možnosti zpracování obrazu.

Model vykazuje významné zlepšení oproti svému předchůdci, přičemž odborní testeři preferovali jeho odpovědi v 56 % případů a zaznamenali 39% snížení závažných chyb u složitých otázek. S nastavením středního úsilí uvažování (medium reasoning effort) dosahuje o3-mini výkonu většího modelu o1 v náročných hodnoceních uvažování, jako jsou AIME a GPQA, při zachování nižší latence a nákladů.

## Unikátní charakteristiky

OpenAI o3-mini je nákladově efektivní jazykový model optimalizovaný pro úlohy STEM, vyniká ve vědě, matematice a kódování. Podporuje tři nastavitelné úrovně usuzování a klíčové vývojářské funkce, včetně volání funkcí a strukturovaných výstupů.

## Silné stránky

### Matematika
Vynikající výsledky v matematických úlohách, dosahuje 97.3% v MATH-500 a 77.0% v AIME 2025.

### Programování
Solidní výkon v kódování s LiveCodeBench skóre 71.7%.

### Věda
Vysoké skóre v GPQA Diamond (74.8%) naznačuje silné vědecké znalosti.

## Slabé stránky

### Rychlost
Nízká rychlost zpracování, TPS 140.1 a TTFT 18.052s, což je pomalé.

### Agenti a nástroje
Slabý výkon v úlohách agentů, τ2-Bench skóre pouze 28.7%.

### Čeština
Data pro češtinu nejsou k dispozici, nelze posoudit kvalitu v českém jazyce.
