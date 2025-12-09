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
  - area: Věda
    description: Silný výkon ve vědeckých úlohách, s GPQA Diamond skóre 74.8%.
  - area: Programování
    description: Solidní schopnosti v kódování, s LiveCodeBench skóre 71.7%.
weaknesses:
  - area: Rychlost
    description: Nízká rychlost, s TPS 140.1 a TTFT 18.052s, což je pomalé.
  - area: Agenti
    description: Slabé schopnosti v úlohách agentů, s τ2-Bench skóre pouze 28.7%.
  - area: Čeština
    description: Data o výkonu v češtině nejsou k dispozici, což omezuje použitelnost v lokálních aplikacích.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Podobná cena vstupu, vyšší cena výstupu
    comparison: Podobná cena, ale potenciálně lepší rychlost a širší použitelnost, pokud nepotřebujete excelentní matematiku.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Levnější vstup i výstup
    comparison: Výrazně levnější, ale pravděpodobně nižší kvalita v matematice a vědě. Vhodné pro méně náročné úlohy.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: Výrazně levnější vstup i výstup
    comparison: Mnohem levnější, ale pravděpodobně nižší výkon v matematice a vědě. Dobrá volba pro experimentování a prototypování.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Levnější vstup i výstup
    comparison: Levnější, ale kontext je menší. Může být srovnatelný v kódování, ale pravděpodobně horší v matematice.
recommendation:
  target_users:
    - Výzkumníci
    - Studenti
    - Vývojáři STEM aplikací
  use_cases:
    - Řešení matematických problémů
    - Vědecké výpočty
    - Generování kódu pro vědecké aplikace
  avoid_for:
    - Úlohy vyžadující rychlou odezvu
    - Aplikace agentů
    - Úlohy vyžadující silnou podporu češtiny
verdict: OpenAI o3-mini je dobrá volba pro uživatele, kteří potřebují silný model pro matematiku a vědu a nevadí jim pomalejší rychlost. Je vhodný pro výzkum a vývoj, kde je přesnost klíčová.
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
overall_score: 55.7
overall_tier: Průměrný
radar:
  logic_code: 76.0
  agentic: 28.7
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Excelentní matematika
  hidden_risk: Pomalá inference může být limitující pro interaktivní aplikace
  recommended_use_case: Řešení komplexních matematických úloh, kde je přesnost důležitější než rychlost
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 11:02"
---

OpenAI o3-mini je nákladově efektivní jazykový model optimalizovaný pro úlohy STEM uvažování, obzvláště vynikající ve vědě, matematice a kódování.

Tento model podporuje parametr `reasoning_effort`, který lze nastavit na "high", "medium" nebo "low" pro řízení doby přemýšlení modelu. Výchozí hodnota je "medium". OpenRouter také nabízí model slug `openai/o3-mini-high` pro nastavení parametru na "high" jako výchozí.

Model nabízí tři nastavitelné úrovně úsilí uvažování a podporuje klíčové vývojářské funkce, včetně volání funkcí, strukturovaných výstupů a streamování, i když nezahrnuje možnosti zpracování obrazu.

Model vykazuje významné zlepšení oproti svému předchůdci, přičemž odborní testeři preferovali jeho odpovědi v 56 % případů a zaznamenali 39% snížení závažných chyb u složitých otázek. S nastavením středního úsilí uvažování (medium reasoning effort), o3-mini dosahuje výkonu většího modelu o1 v náročných hodnoceních uvažování, jako jsou AIME a GPQA, při zachování nižší latence a nákladů.

## Unikátní charakteristiky

OpenAI o3-mini je nákladově efektivní jazykový model optimalizovaný pro úlohy STEM, vyniká ve vědě, matematice a kódování. Podporuje tři nastavitelné úrovně úsilí a klíčové vývojářské funkce, jako je volání funkcí a strukturované výstupy.

## Silné stránky

### Matematika
Vynikající výsledky v matematických úlohách, dosahuje 97.3% v MATH-500 a 77.0% v AIME 2025.

### Věda
Silný výkon ve vědeckých úlohách, s GPQA Diamond skóre 74.8%.

### Programování
Solidní schopnosti v kódování, s LiveCodeBench skóre 71.7%.

## Slabé stránky

### Rychlost
Nízká rychlost, s TPS 140.1 a TTFT 18.052s, což je pomalé.

### Agenti
Slabé schopnosti v úlohách agentů, s τ2-Bench skóre pouze 28.7%.

### Čeština
Data o výkonu v češtině nejsou k dispozici, což omezuje použitelnost v lokálních aplikacích.
