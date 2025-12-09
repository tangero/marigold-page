---
layout: llm_review
title: "Google: Gemini 2.5 Pro"
date: "2025-06-17 16:12:24"
model_id: google/gemini-2.5-pro
slug: google-gemini-2-5-pro
provider: Google
pricing:
  prompt_per_m: 1.25
  completion_per_m: 10.0
  blend_per_m: 3.4375
context_length: 1,048,576
max_output: 65,536
input_modalities:
  - text
  - image
  - file
  - audio
  - video
output_modalities:
  - text
focus:
  - Věda
  - Matematika
  - Programování
strengths:
  - area: Věda a Matematika
    description: Vynikající výkon ve vědeckých a matematických úlohách, což dokazují benchmarky MATH-500 (96.7%) a GPQA Diamond (84.4%).
  - area: Programování
    description: Solidní schopnosti v programování, s výsledkem 80.1% v LiveCodeBench.
  - area: Kontext
    description: Velký kontext (1,048,576 tokenů) umožňuje zpracovávat rozsáhlé dokumenty a komplexní úlohy.
weaknesses:
  - area: Rychlost
    description: Nízká rychlost zpracování, s TPS 154.4 a TTFT 33.438s, což omezuje použití v aplikacích vyžadujících rychlou odezvu.
  - area: Čeština
    description: Nedostatek dat o výkonu v češtině (MMMLU), což ztěžuje posouzení vhodnosti pro české uživatele.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: 4x dražší vstup, 2.5x dražší výstup
    comparison: Claude Opus je dražší, ale může nabídnout lepší výkon v některých oblastech. Nemáme data pro přímé srovnání.
  - provider: OPENAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: Stejná cena
    comparison: GPT-5.1 má menší kontext (400,000 tokenů). Nemáme data pro přímé srovnání výkonu.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 6x levnější vstup, 20x levnější výstup
    comparison: Grok je výrazně levnější a má větší kontext (2,000,000 tokenů), ale pravděpodobně nižší výkon ve vědeckých a matematických úlohách.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: 6x levnější vstup, 50x levnější výstup
    comparison: Mistral je mnohem levnější, ale má menší kontext (262,144 tokenů) a pravděpodobně nižší výkon ve vědeckých a matematických úlohách.
recommendation:
  target_users:
    - Výzkumníci
    - Data Scientists
    - Softwaroví inženýři
  use_cases:
    - Analýza dat
    - Vědecké modelování
    - Generování kódu
  avoid_for:
    - Aplikace s nízkou latencí
    - Úlohy vyžadující plynulou konverzaci
    - Aplikace v češtině
verdict: Gemini 2.5 Pro je vhodný pro uživatele, kteří potřebují vysoký výkon v matematice, vědě a programování a nevadí jim pomalejší odezva. Pro aplikace v češtině je třeba ověřit jeho schopnosti.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 88.6
    tier: Výborný
  coding:
    name: Programování
    icon: 💻
    score: 80.1
    tier: Výborný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 54.1
    tier: Průměrný
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 61.8
    tier: Dobrý
  speed:
    name: Rychlost
    icon: ⚡
    score: 38.6
    tier: Slabý
overall_score: 69.2
overall_tier: Dobrý
radar:
  logic_code: 84.3
  agentic: 54.1
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající matematické schopnosti
  hidden_risk: Pomalá inference může omezit interaktivní použití
  recommended_use_case: Řešení komplexních matematických problémů a vědeckých simulací
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:07"
---

Gemini 2.5 Pro je nejmodernější AI model od Googlu, navržený pro pokročilé usuzování, kódování, matematiku a vědecké úlohy. Využívá "myšlenkové" schopnosti, které mu umožňují odůvodňovat odpovědi se zvýšenou přesností a nuancovanou manipulací s kontextem. Gemini 2.5 Pro dosahuje špičkového výkonu v několika benchmarkách, včetně prvního místa v žebříčku LMArena, což odráží vynikající sladění s preferencemi lidí a schopnosti řešit složité problémy.

## Unikátní charakteristiky

Gemini 2.5 Pro vyniká ve vědeckých a matematických úlohách, což dokazuje vysoké skóre v benchmarkách MATH-500 (96.7%) a GPQA Diamond (84.4%). Model se také dobře umisťuje v programování (LiveCodeBench 80.1%). Jeho velký kontext (1,048,576 tokenů) umožňuje zpracovávat komplexní úlohy.

## Silné stránky

### Věda a Matematika
Vynikající výkon ve vědeckých a matematických úlohách, což dokazují benchmarky MATH-500 (96.7%) a GPQA Diamond (84.4%).

### Programování
Solidní schopnosti v programování, s výsledkem 80.1% v LiveCodeBench.

### Kontext
Velký kontext (1,048,576 tokenů) umožňuje zpracovávat rozsáhlé dokumenty a komplexní úlohy.

## Slabé stránky

### Rychlost
Nízká rychlost zpracování, s TPS 154.4 a TTFT 33.438s, což omezuje použití v aplikacích vyžadujících rychlou odezvu.

### Čeština
Nedostatek dat o výkonu v češtině (MMMLU), což ztěžuje posouzení vhodnosti pro české uživatele.
