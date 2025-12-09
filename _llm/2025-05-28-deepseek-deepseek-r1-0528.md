---
layout: llm_review
title: "DeepSeek: R1 0528"
date: "2025-05-28 19:59:30"
model_id: deepseek/deepseek-r1-0528
slug: deepseek-deepseek-r1-0528
provider: DeepSeek
pricing:
  prompt_per_m: 0.4
  completion_per_m: 1.75
  blend_per_m: 0.7375
context_length: 163,840
max_output: 163,840
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Matematika
  - Programování
strengths:
  - area: Matematika
    description: Vynikající výkon v matematických úlohách, s vysokým skóre v MATH-500 (98.3%) a AIME 2025 (89.3%).
  - area: Programování
    description: Silný v kódování, dosahuje 77.0% na LiveCodeBench.
weaknesses:
  - area: Agenti a nástroje
    description: Slabý výkon v úlohách zaměřených na agenty, s nízkým skóre 36.5% na τ2-Bench.
  - area: Rychlost
    description: Nízká rychlost inference, což omezuje jeho použitelnost v aplikacích vyžadujících rychlou odezvu.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: Výrazně dražší (7x vstup, 14x výstup)
    comparison: Claude Opus je pravděpodobně silnější v obecné inteligenci, ale dražší.
  - provider: GOOGLE
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Dražší (5x vstup, 7x výstup)
    comparison: Gemini Pro má větší kontext, ale je dražší.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Levnější (poloviční cena)
    comparison: Ministral 14B je levnější, ale pravděpodobně méně výkonný v matematice.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-speciale
    model_id: deepseek/deepseek-v3.2-speciale
    price_comparison: Levnější (poloviční cena)
    comparison: Deepseek v3.2 Speciale je levnější alternativou od stejného poskytovatele.
recommendation:
  target_users:
    - Výzkumníci v oblasti AI
    - Vývojáři matematických aplikací
  use_cases:
    - Řešení komplexních matematických problémů
    - Generování kódu pro vědecké výpočty
  avoid_for:
    - Aplikace vyžadující rychlou odezvu
    - Úlohy zaměřené na agenty a nástroje
verdict: DeepSeek R1 0528 je vhodný pro výzkumníky a vývojáře, kteří potřebují silný model pro matematické a programovací úlohy a oceňují otevřený přístup.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 87.9
    tier: Výborný
  coding:
    name: Programování
    icon: 💻
    score: 77.0
    tier: Výborný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 36.5
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 58.6
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 0.0
    tier: Slabý
overall_score: 57.8
overall_tier: Průměrný
radar:
  logic_code: 77.0
  agentic: 36.5
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající výkon v matematice a programování s otevřeným přístupem.
  hidden_risk: Slabší výkon v úlohách zaměřených na agenty a nástroje, pomalá inference.
  recommended_use_case: Výzkum v oblasti matematiky a vývoj vědeckých aplikací.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:06"
---

Aktualizace z 28. května k [původnímu DeepSeek R1](/deepseek/deepseek-r1) s výkonem srovnatelným s [OpenAI o1](/openai/o1), ale s otevřeným zdrojovým kódem a plně otevřenými reasoning tokeny. Má velikost 671B parametrů, přičemž 37B je aktivních v jednom průchodu inferencí.

Plně open-source model.

## Unikátní charakteristiky

DeepSeek R1 0528 je open-source model s vysokým kontextem a silným výkonem v matematice a programování. Jeho otevřenost a plně otevřené reasoning tokeny ho odlišují od uzavřených modelů.

## Silné stránky

### Matematika
Vynikající výkon v matematických úlohách, s vysokým skóre v MATH-500 (98.3%) a AIME 2025 (89.3%).

### Programování
Silný v kódování, dosahuje 77.0% na LiveCodeBench.

## Slabé stránky

### Agenti a nástroje
Slabý výkon v úlohách zaměřených na agenty, s nízkým skóre 36.5% na τ2-Bench.

### Rychlost
Nízká rychlost inference, což omezuje jeho použitelnost v aplikacích vyžadujících rychlou odezvu.
