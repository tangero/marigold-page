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
  - STEM reasoning
  - Matematika
  - Programování
strengths:
  - area: Matematika
    description: Vynikající výsledky v matematických úlohách, dosahuje 98.5% v MATH-500 a 86.0% v AIME 2025.
  - area: Programování
    description: Dobrý výkon v kódovacích úlohách, s LiveCodeBench skóre 73.4%.
weaknesses:
  - area: Rychlost
    description: Nízká rychlost zpracování, s TPS 142.4 a TTFT 59.851s, což omezuje použití v reálném čase.
  - area: Agentické schopnosti
    description: Slabé agentické schopnosti, s τ2-Bench skóre pouze 31.3%.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Levnější vstup i výstup
    comparison: Claude Haiku je rychlejší a levnější, ale pravděpodobně méně přesný v matematice.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Výrazně levnější vstup i výstup
    comparison: Gemini 2.5 Flash je mnohem levnější, ale s menším kontextem a pravděpodobně nižší kvalitou.
  - provider: OPENAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: Podobná cena vstupu, dražší výstup
    comparison: GPT-5.1 má větší kontext a může být lepší v obecných úlohách, ale je dražší na výstup.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: Výrazně levnější vstup i výstup
    comparison: Ministral-8b-2512 je mnohem levnější, ale může mít horší výsledky ve specifických STEM úlohách.
recommendation:
  target_users:
    - Výzkumníci
    - Studenti
    - Vývojáři STEM aplikací
  use_cases:
    - Řešení matematických problémů
    - Generování kódu
    - Vědecké výpočty
  avoid_for:
    - Úlohy vyžadující rychlou odezvu
    - Agentické aplikace
    - Zpracování češtiny (chybí data)
verdict: OpenAI o3-mini-high je vhodný pro uživatele, kteří potřebují vysokou přesnost v matematických a kódovacích úlohách a nevadí jim pomalejší odezva. Je ideální pro výzkum a vývoj v oblasti STEM.
benchmark_categories:
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
  logic_code: 79.2
  agentic: 31.3
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající v matematických úlohách.
  hidden_risk: Pomalá inference může omezit interaktivní použití.
  recommended_use_case: Automatické řešení matematických úloh a generování kódu pro vědecké simulace.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 11:02"
---

OpenAI o3-mini-high je stejný model jako [o3-mini](/openai/o3-mini) s nastaveným parametrem reasoning_effort na hodnotu high.

o3-mini je nákladově efektivní jazykový model optimalizovaný pro úlohy STEM usuzování, obzvláště vyniká ve vědě, matematice a kódování. Model nabízí tři nastavitelné úrovně úsilí usuzování a podporuje klíčové vývojářské funkce, včetně volání funkcí, strukturovaných výstupů a streamování, avšak nezahrnuje schopnosti zpracování obrazu.

Model vykazuje významná zlepšení oproti svému předchůdci, přičemž odborní testeři preferovali jeho odpovědi v 56 % případů a zaznamenali 39% snížení závažných chyb u složitých otázek. S nastavením středního úsilí usuzování dosahuje o3-mini výkonu většího modelu o1 v náročných hodnoceních usuzování, jako jsou AIME a GPQA, přičemž si zachovává nižší latenci a náklady.

## Unikátní charakteristiky

OpenAI o3-mini-high je optimalizovaný pro STEM úlohy, exceluje ve vědě, matematice a kódování. Nabízí tři úrovně úsilí při odvozování a podporuje volání funkcí a strukturované výstupy. Dosahuje lepších výsledků než jeho předchůdce s menším počtem chyb.

## Silné stránky

### Matematika
Vynikající výsledky v matematických úlohách, dosahuje 98.5% v MATH-500 a 86.0% v AIME 2025.

### Programování
Dobrý výkon v kódovacích úlohách, s LiveCodeBench skóre 73.4%.

## Slabé stránky

### Rychlost
Nízká rychlost zpracování, s TPS 142.4 a TTFT 59.851s, což omezuje použití v reálném čase.

### Agentické schopnosti
Slabé agentické schopnosti, s τ2-Bench skóre pouze 31.3%.
