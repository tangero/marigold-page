---
layout: llm_review
title: "Google: Gemini 2.5 Flash"
date: "2025-06-17 17:01:28"
model_id: google/gemini-2.5-flash
slug: google-gemini-2-5-flash
provider: Google
pricing:
  prompt_per_m: 0.3
  completion_per_m: 2.5
  blend_per_m: 0.85
context_length: 1,048,576
max_output: 65,535
input_modalities:
  - file
  - image
  - text
  - audio
  - video
output_modalities:
  - text
focus:
  - Rozumování
  - Matematika
strengths:
  - area: Matematika
    description: Vynikající v matematických úlohách, dosahuje 93.2% v MATH-500 a 60.3% v AIME 2025.
  - area: Rychlost
    description: Vysoká rychlost zpracování s TPS 235.4 a nízkou latencí TTFT 0.359s.
weaknesses:
  - area: Logické myšlení
    description: Slabé výsledky v HLE (5.1%) a ifbench (39.0%) naznačují omezení v úlohách vyžadujících složité logické operace.
  - area: Čeština
    description: MMMLU skóre pro češtinu není k dispozici, což ztěžuje posouzení použitelnosti pro české uživatele.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-sonnet-4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: 10x dražší vstup, 6x dražší výstup
    comparison: Claude Sonnet 4.5 má větší kontext (1M tokenů), ale je výrazně dražší. Může být lepší pro úlohy vyžadující rozsáhlý kontext a vyšší kvalitu výstupu.
  - provider: X-AI
    model: x-ai/grok-4-fast
    model_id: x-ai/grok-4-fast
    price_comparison: Levnější vstup i výstup
    comparison: Grok-4-fast je výrazně levnější a má větší kontext (2M tokenů), ale benchmarky naznačují nižší kvalitu v matematice a logice.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Podobná cena vstupu, levnější výstup
    comparison: Deepseek v3.2 nabízí podobnou cenu vstupu a levnější výstup, ale má menší kontext (163,840 tokenů). Může být vhodný pro úlohy s menším kontextem a důrazem na cenu.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Levnější vstup i výstup
    comparison: Ministral-14b-2512 je levnější, ale benchmarky naznačují nižší kvalitu v matematice a logice. Kontext je menší (262,144 tokenů).
recommendation:
  target_users:
    - Výzkumníci
    - Data scientisti
    - Vývojáři
  use_cases:
    - Matematické modelování
    - Vědecké simulace
    - Rychlé prototypování
  avoid_for:
    - Složité logické úlohy
    - Aplikace vyžadující silnou češtinu
verdict: Gemini 2.5 Flash je vhodný pro uživatele, kteří potřebují rychlý a efektivní model pro matematické a vědecké úlohy, ale měli by se vyhnout úlohám vyžadujícím složité logické myšlení nebo silnou podporu češtiny.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 66.0
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 49.5
    tier: Průměrný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 14.9
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 52.5
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 82.0
    tier: Výborný
overall_score: 47.9
overall_tier: Průměrný
radar:
  logic_code: 42.3
  agentic: 14.9
  languages: 0
  safety: 0
  speed: Výborný
expert_verdict:
  killer_feature: Vynikající matematické schopnosti
  hidden_risk: Slabé logické myšlení a neznámá kvalita češtiny
  recommended_use_case: Rychlé řešení matematických úloh a vědeckých výpočtů
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:07"
---

Gemini 2.5 Flash je špičkový pracovní model od Googlu, speciálně navržený pro pokročilé usuzování, kódování, matematiku a vědecké úlohy. Zahrnuje vestavěné "myšlenkové" schopnosti, které mu umožňují poskytovat odpovědi s vyšší přesností a nuancovanějším zpracováním kontextu.

Navíc je Gemini 2.5 Flash konfigurovatelný prostřednictvím parametru "max tokens for reasoning" (maximální počet tokenů pro usuzování), jak je popsáno v dokumentaci (https://openrouter.ai/docs/use-cases/reasoning-tokens#max-tokens-for-reasoning).

## Unikátní charakteristiky

Gemini 2.5 Flash je navržen pro pokročilé úlohy vyžadující rozumování, kódování, matematiku a vědecké výpočty. Model vyniká v matematických úlohách, což dokazuje vysoké skóre 93.2% v MATH-500. Díky konfigurovatelnému parametru 'max tokens for reasoning' umožňuje jemné doladění pro specifické use case.

## Silné stránky

### Matematika
Vynikající v matematických úlohách, dosahuje 93.2% v MATH-500 a 60.3% v AIME 2025.

### Rychlost
Vysoká rychlost zpracování s TPS 235.4 a nízkou latencí TTFT 0.359s.

## Slabé stránky

### Logické myšlení
Slabé výsledky v HLE (5.1%) a ifbench (39.0%) naznačují omezení v úlohách vyžadujících složité logické operace.

### Čeština
MMMLU skóre pro češtinu není k dispozici, což ztěžuje posouzení použitelnosti pro české uživatele.
