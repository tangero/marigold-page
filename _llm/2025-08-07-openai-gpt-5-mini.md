---
layout: llm_review
title: "OpenAI: GPT-5 Mini"
date: "2025-08-07 19:23:27"
model_id: openai/gpt-5-mini
slug: openai-gpt-5-mini
provider: Openai
pricing:
  prompt_per_m: 0.25
  completion_per_m: 2.0
  blend_per_m: 0.6875
context_length: 400,000
max_output: 128,000
input_modalities:
  - text
  - image
  - file
output_modalities:
  - text
focus:
  - Věda
  - Programování
strengths:
  - area: Věda a matematika
    description: Model dosahuje vynikajících výsledků v matematických úlohách (AIME 90.7%, GPQA Diamond 82.8%), což ho předurčuje pro vědecké aplikace.
  - area: Programování
    description: S vysokým skóre v LiveCodeBench (83.8%) je model vhodný pro generování a analýzu kódu.
weaknesses:
  - area: Rychlost
    description: Model má velmi pomalou rychlost odezvy (TTFT 97.894s, TPS 76.7), což omezuje jeho použitelnost v interaktivních aplikacích.
  - area: Obecná inteligence
    description: Skóre v AI Intelligence Index (64.3%) a HLE (19.7%) naznačuje omezení v komplexním logickém uvažování.
competitors:
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Podstatně levnější (vstup i výstup)
    comparison: Grok-4.1-fast nabízí větší kontext a je výrazně rychlejší, ale může mít nižší přesnost ve vědeckých úlohách.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Levnější (vstup i výstup)
    comparison: Ministral-14b-2512 je levnější a má velký kontext, ale nemusí dosahovat tak dobrých výsledků ve specializovaných úlohách jako GPT-5 Mini.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Levnější (vstup i výstup)
    comparison: Deepseek-v3.2 je levnější a optimalizovaný pro kódování, ale má menší kontextové okno.
  - provider: OPENAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: Dražší (5x dražší vstup, 5x dražší výstup)
    comparison: GPT-5.1 nabízí srovnatelný kontext, ale za vyšší cenu. Může mít lepší obecnou inteligenci, ale data nejsou k dispozici.
recommendation:
  target_users:
    - Výzkumníci
    - Vývojáři
  use_cases:
    - Matematické modelování
    - Generování kódu
    - Analýza dat
  avoid_for:
    - Interaktivní aplikace
    - Úlohy vyžadující rychlou odezvu
    - Aplikace s vysokými nároky na logické uvažování
verdict: GPT-5 Mini je dobrá volba pro uživatele, kteří potřebují model s vynikajícími matematickými schopnostmi a programovacími dovednostmi, ale nevadí jim pomalejší rychlost odezvy.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 82.8
    tier: Výborný
  coding:
    name: Programování
    icon: 💻
    score: 83.8
    tier: Výborný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 68.4
    tier: Dobrý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 59.7
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 19.2
    tier: Slabý
overall_score: 71.2
overall_tier: Dobrý
radar:
  logic_code: 83.8
  agentic: 68.4
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající matematické schopnosti
  hidden_risk: Pomalá inference může být limitující pro některé aplikace
  recommended_use_case: Vědecké výpočty a modelování, kde není kritická rychlost odezvy
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:10"
---

GPT-5 Mini je kompaktní verze GPT-5, navržená pro zvládání méně náročných úloh vyžadujících usuzování. Poskytuje stejné výhody v oblasti dodržování instrukcí a bezpečnostního ladění jako GPT-5, ale se sníženou latencí a náklady. GPT-5 Mini je nástupcem modelu o4-mini od OpenAI.

## Unikátní charakteristiky

GPT-5 Mini je kompaktní verze GPT-5, navržená pro méně náročné úlohy. Vyniká v matematice a programování, ale má pomalou rychlost odezvy. Nabízí vyvážený poměr mezi kvalitou a cenou.

## Silné stránky

### Věda a matematika
Model dosahuje vynikajících výsledků v matematických úlohách (AIME 90.7%, GPQA Diamond 82.8%), což ho předurčuje pro vědecké aplikace.

### Programování
S vysokým skóre v LiveCodeBench (83.8%) je model vhodný pro generování a analýzu kódu.

## Slabé stránky

### Rychlost
Model má velmi pomalou rychlost odezvy (TTFT 97.894s, TPS 76.7), což omezuje jeho použitelnost v interaktivních aplikacích.

### Obecná inteligence
Skóre v AI Intelligence Index (64.3%) a HLE (19.7%) naznačuje omezení v komplexním logickém uvažování.
