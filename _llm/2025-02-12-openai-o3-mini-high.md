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
  - Věda
  - Kódování
strengths:
  - area: Matematika
    description: Vynikající výsledky v matematických úlohách, dosahuje 98.5% v MATH-500 a 86.0% v AIME 2025.
  - area: Věda
    description: Silný výkon ve vědeckých úlohách, s GPQA Diamond skóre 77.3%.
weaknesses:
  - area: Rychlost
    description: Nízká rychlost zpracování, TPS 142.4 a TTFT 59.851s, což omezuje použití v aplikacích vyžadujících rychlou odezvu.
  - area: Agentické schopnosti
    description: Slabé výsledky v agentických úlohách, τ2-Bench skóre pouze 31.3%.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Poloviční cena vstupu, podobný výstup
    comparison: Claude Haiku je levnější, ale pravděpodobně méně výkonný v matematice a vědě. Nemáme data pro přímé srovnání.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: 4x levnější vstup, poloviční cena výstupu
    comparison: Gemini Flash je výrazně levnější, ale má menší kontext a pravděpodobně nižší výkon v náročných úlohách.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: 9x levnější vstup i výstup
    comparison: Ministral-14b je mnohem levnější, ale nemusí dosahovat stejné přesnosti ve specializovaných STEM úlohách. Nemáme data pro přímé srovnání.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: 7x levnější vstup, 11x levnější výstup
    comparison: Deepseek-v3.2 je výrazně levnější, ale má menší kontext a pravděpodobně nižší výkon v náročných úlohách.
recommendation:
  target_users:
    - Výzkumníci
    - Studenti
    - Vývojáři STEM aplikací
  use_cases:
    - Řešení matematických problémů
    - Vědecké modelování
    - Generování kódu pro vědecké výpočty
  avoid_for:
    - Aplikace vyžadující rychlou odezvu
    - Agentické úlohy
    - Zpracování v češtině (chybí data)
verdict: OpenAI o3-mini-high je vhodný pro uživatele, kteří potřebují vysokou přesnost v matematických a vědeckých úlohách a jsou ochotni akceptovat pomalejší rychlost zpracování. Není vhodný pro aplikace vyžadující rychlou odezvu nebo agentické schopnosti.
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
overall_score: 59.6
overall_tier: Průměrný
radar:
  logic_code: 79.2
  agentic: 31.3
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající matematické schopnosti
  hidden_risk: Pomalá inference může být limitující pro interaktivní aplikace
  recommended_use_case: Řešení složitých matematických úloh a vědeckých výpočtů, kde je přesnost důležitější než rychlost.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 12:58"
---

OpenAI o3-mini-high je stejný model jako [o3-mini](/openai/o3-mini) s nastaveným parametrem reasoning_effort na hodnotu high (vysoká).

o3-mini je nákladově efektivní jazykový model optimalizovaný pro úlohy STEM usuzování, obzvláště vyniká ve vědě, matematice a kódování. Model nabízí tři nastavitelné úrovně úsilí usuzování (reasoning effort) a podporuje klíčové vývojářské funkce, včetně volání funkcí (function calling), strukturovaných výstupů a streamování, nicméně nezahrnuje schopnosti zpracování obrazu (vision processing capabilities).

Model vykazuje významné zlepšení oproti svému předchůdci, přičemž odborní testeři preferovali jeho odpovědi v 56 % případů a zaznamenali 39% snížení závažných chyb u složitých otázek. S nastavením středního úsilí usuzování (medium reasoning effort), o3-mini dosahuje výkonu většího modelu o1 v náročných hodnoceních usuzování, jako jsou AIME a GPQA, při zachování nižší latence a nákladů.

## Unikátní charakteristiky

OpenAI o3-mini-high je optimalizovaný pro STEM úlohy, exceluje ve vědě, matematice a kódování. Nabízí nastavitelné úrovně úsilí při odvozování a podporuje function calling a strukturované výstupy. Dosahuje lepších výsledků než jeho předchůdce s menším počtem chyb.

## Silné stránky

### Matematika
Vynikající výsledky v matematických úlohách, dosahuje 98.5% v MATH-500 a 86.0% v AIME 2025.

### Věda
Silný výkon ve vědeckých úlohách, s GPQA Diamond skóre 77.3%.

## Slabé stránky

### Rychlost
Nízká rychlost zpracování, TPS 142.4 a TTFT 59.851s, což omezuje použití v aplikacích vyžadujících rychlou odezvu.

### Agentické schopnosti
Slabé výsledky v agentických úlohách, τ2-Bench skóre pouze 31.3%.
