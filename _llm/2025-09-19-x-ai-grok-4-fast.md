---
layout: llm_review
title: "xAI: Grok 4 Fast"
date: "2025-09-19 02:01:30"
model_id: x-ai/grok-4-fast
slug: x-ai-grok-4-fast
provider: xAI
pricing:
  prompt_per_m: 0.2
  completion_per_m: 0.5
  blend_per_m: 0.275
context_length: 2,000,000
max_output: 30,000
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Rychlost
  - Cenová efektivita
strengths:
  - area: Rychlost
    description: Vysoká propustnost (182.2 tokenů/s) a nízká latence (0.560s) umožňují rychlé generování odpovědí.
  - area: Cena
    description: Nízká cena (0.28 USD/1M tokenů) z něj činí cenově dostupnou volbu pro rozsáhlé nasazení.
  - area: Kontext
    description: Velký kontext (2 miliony tokenů) umožňuje zpracování rozsáhlých dokumentů a složitých konverzací.
weaknesses:
  - area: Logické uvažování
    description: Nízké skóre v HLE (5.0%) naznačuje slabé logické uvažování.
  - area: Programování
    description: Skóre v LiveCodeBench (40.1%) je průměrné, což omezuje jeho využití pro pokročilé programovací úlohy.
  - area: Čeština
    description: MMMLU skóre pro češtinu není k dispozici, což ztěžuje posouzení jeho výkonu v českém jazyce.
competitors:
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: Podobná cena
    comparison: Konkuruje cenou a kontextem, ale Grok 4 Fast má lepší rychlost.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: Podobná cena
    comparison: Konkuruje cenou, ale Grok 4 Fast má výrazně větší kontext.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Mírně dražší výstup
    comparison: Konkuruje cenou, ale Grok 4 Fast má větší kontext a lepší rychlost.
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Dražší
    comparison: Claude Haiku je dražší, ale může mít lepší kvalitu výstupu v některých oblastech (data nejsou k dispozici).
recommendation:
  target_users:
    - Vývojáři prototypující aplikace
    - Firmy s velkým objemem dat
    - Aplikace citlivé na latenci
  use_cases:
    - Chatboti
    - Analýza sentimentu
    - Extrakce informací z dokumentů
  avoid_for:
    - Úlohy vyžadující pokročilé logické uvažování
    - Programování
    - Aplikace vyžadující vysokou přesnost v českém jazyce
verdict: Grok 4 Fast je vhodný pro uživatele, kteří hledají rychlý a cenově dostupný model pro zpracování velkého množství textu, ale nemají vysoké nároky na logické uvažování nebo češtinu.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 60.6
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 40.1
    tier: Průměrný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 63.7
    tier: Dobrý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 47.5
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 67.5
    tier: Dobrý
overall_score: 54.6
overall_tier: Průměrný
radar:
  logic_code: 22.55
  agentic: 63.7
  languages: 0
  safety: 0
  speed: Dobrý
expert_verdict:
  killer_feature: Cenová efektivita a rychlost s velkým kontextem
  hidden_risk: Slabší logické uvažování a neznámý výkon v češtině
  recommended_use_case: Rychlá analýza velkých textových dat s nízkými náklady
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:12"
---

Grok 4 Fast je nejnovější multimodální model od xAI s nejmodernější (SOTA) nákladovou efektivitou a kontextovým oknem o velikosti 2 miliony tokenů. Je dostupný ve dvou variantách: bez uvažování a s uvažováním. Více informací o modelu naleznete v [novinkách](http://x.ai/news/grok-4-fast) od xAI.

Uvažování lze povolit/zakázat pomocí parametru `reasoning` `enabled` v API. [Více informací naleznete v naší dokumentaci](https://openrouter.ai/docs/use-cases/reasoning-tokens#controlling-reasoning-tokens)

## Unikátní charakteristiky

Grok 4 Fast se vyznačuje vysokou rychlostí (182.2 tokenů/s) a nízkou latencí (0.560s), což ho činí vhodným pro aplikace citlivé na čas. Nabízí velký kontext 2 miliony tokenů a multimodální vstupy (text, image → text).

## Silné stránky

### Rychlost
Vysoká propustnost (182.2 tokenů/s) a nízká latence (0.560s) umožňují rychlé generování odpovědí.

### Cena
Nízká cena (0.28 USD/1M tokenů) z něj činí cenově dostupnou volbu pro rozsáhlé nasazení.

### Kontext
Velký kontext (2 miliony tokenů) umožňuje zpracování rozsáhlých dokumentů a složitých konverzací.

## Slabé stránky

### Logické uvažování
Nízké skóre v HLE (5.0%) naznačuje slabé logické uvažování.

### Programování
Skóre v LiveCodeBench (40.1%) je průměrné, což omezuje jeho využití pro pokročilé programovací úlohy.

### Čeština
MMMLU skóre pro češtinu není k dispozici, což ztěžuje posouzení jeho výkonu v českém jazyce.
