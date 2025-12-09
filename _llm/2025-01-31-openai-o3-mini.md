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
  - area: Vědecké úlohy
    description: Dobré výsledky ve vědeckých úlohách, GPQA Diamond skóre 74.8%.
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
    price_comparison: Podobná cena vstupu, dražší výstup
    comparison: Claude Haiku je rychlejší, ale o3-mini má lepší výsledky v matematice a programování.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Mnohem levnější vstup i výstup
    comparison: Gemini 2.5 Flash je výrazně levnější, ale pravděpodobně méně výkonný v náročných úlohách STEM.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: Mnohem levnější vstup i výstup
    comparison: Mistral 8B je výrazně levnější, ale o3-mini má lepší výsledky v matematice a programování.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Levnější vstup i výstup
    comparison: Deepseek v3.2 je levnější, ale o3-mini má lepší výsledky v matematice.
recommendation:
  target_users:
    - Studenti
    - Výzkumníci
    - Vývojáři
  use_cases:
    - Řešení matematických úloh
    - Generování kódu
    - Vědecké výpočty
  avoid_for:
    - Úlohy vyžadující rychlou odezvu
    - Úlohy agentů
    - Aplikace v češtině (bez testování)
verdict: OpenAI o3-mini je dobrá volba pro uživatele, kteří potřebují řešit matematické a vědecké úlohy a nevadí jim pomalejší odezva. Je vhodný pro studenty, výzkumníky a vývojáře v oblasti STEM.
benchmark_categories:
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
overall_score: 57.0
overall_tier: Průměrný
radar:
  logic_code: 76.0
  agentic: 28.7
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající v matematických úlohách
  hidden_risk: Pomalá inference může být problém pro interaktivní aplikace
  recommended_use_case: Řešení komplexních matematických problémů a generování kódu pro vědecké výpočty.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 12:57"
---

OpenAI o3-mini je nákladově efektivní jazykový model optimalizovaný pro úlohy STEM uvažování, obzvláště vynikající ve vědě, matematice a programování.

Tento model podporuje parametr `reasoning_effort`, který lze nastavit na "high", "medium" nebo "low" pro řízení doby přemýšlení modelu. Výchozí hodnota je "medium". OpenRouter také nabízí model slug `openai/o3-mini-high` pro nastavení parametru na "high" jako výchozí.

Model nabízí tři nastavitelné úrovně úsilí uvažování a podporuje klíčové vývojářské schopnosti včetně volání funkcí, strukturovaných výstupů a streamování, i když nezahrnuje schopnosti zpracování obrazu.

Model vykazuje významné zlepšení oproti svému předchůdci, přičemž odborní testeři preferovali jeho odpovědi v 56 % případů a zaznamenali 39% snížení závažných chyb u složitých otázek. S nastavením středního úsilí uvažování (medium reasoning effort), o3-mini dosahuje výkonu většího modelu o1 v náročných hodnoceních uvažování, jako jsou AIME a GPQA, při zachování nižší latence a nákladů.

## Unikátní charakteristiky

OpenAI o3-mini je nákladově efektivní jazykový model optimalizovaný pro STEM úlohy, vyniká ve vědě, matematice a kódování. Podporuje tři nastavitelné úrovně usuzování a klíčové vývojářské funkce, jako je volání funkcí a strukturované výstupy.

## Silné stránky

### Matematika
Vynikající výsledky v matematických úlohách, dosahuje 97.3% v MATH-500 a 77.0% v AIME 2025.

### Programování
Solidní výkon v kódování s LiveCodeBench skóre 71.7%.

### Vědecké úlohy
Dobré výsledky ve vědeckých úlohách, GPQA Diamond skóre 74.8%.

## Slabé stránky

### Rychlost
Nízká rychlost zpracování, TPS 140.1 a TTFT 18.052s, což je pomalé.

### Agenti a nástroje
Slabý výkon v úlohách agentů, τ2-Bench skóre pouze 28.7%.

### Čeština
Data pro češtinu nejsou k dispozici, nelze posoudit kvalitu v českém jazyce.
