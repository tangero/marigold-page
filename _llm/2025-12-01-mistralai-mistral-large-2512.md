---
layout: llm_review
title: "Mistral: Mistral Large 3 2512"
date: "2025-12-01 22:27:52"
model_id: mistralai/mistral-large-2512
slug: mistralai-mistral-large-2512
provider: Mistral
pricing:
  prompt_per_m: 0.5
  completion_per_m: 1.5
  blend_per_m: 0.75
context_length: 262,144
max_output: N/A
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Obecná inteligence
  - Matematika
strengths:
  - area: Matematika
    description: Relativně silný výkon v matematických úlohách, dosahuje 71.4% na MATH-500.
  - area: Kontext
    description: Velký kontext 262,144 tokenů umožňuje zpracování rozsáhlých dokumentů a komplexních úloh.
weaknesses:
  - area: Logika
    description: "Velmi slabý výkon v hard logic úlohách (HLE: 3.2%)."
  - area: Rychlost
    description: Označena jako 'Slabý', což naznačuje pomalou inferenci.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: 10x dražší vstup, 16.6x dražší výstup
    comparison: Claude Opus by měl být výrazně lepší v komplexních úlohách, ale za vyšší cenu.
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: 4x dražší vstup, 8x dražší výstup
    comparison: Gemini 3 Pro nabízí multimodální schopnosti (image → text), které Mistral Large nemá, ale je dražší.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 3.75x levnější vstup, 3x levnější výstup
    comparison: Grok-4.1-fast je výrazně levnější a má větší kontext, ale jeho výkonnostní charakteristiky nejsou známy.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: 3.75x levnější vstup i výstup
    comparison: Ministral-14b-2512 je levnější alternativou od stejného poskytovatele, vhodná pro méně náročné úlohy.
recommendation:
  target_users:
    - Výzkumníci
    - Data scientisti
  use_cases:
    - Matematické modelování
    - Analýza rozsáhlých textových dat
  avoid_for:
    - Úlohy vyžadující rychlou odezvu
    - Aplikace s vysokými nároky na logické uvažování
verdict: Mistral Large 3 2512 je vhodný pro uživatele, kteří potřebují zpracovávat velké objemy dat a provádět matematické operace, ale měli by se vyhnout úlohám, které vyžadují silné logické uvažování. Pro nasazení v českém prostředí je nutné otestovat jeho jazykové schopnosti.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 36.9
    tier: Slabý
  coding:
    name: Programování
    icon: 💻
    score: 26.7
    tier: Slabý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 33.0
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 43.9
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 0.0
    tier: Slabý
overall_score: 31.2
overall_tier: Slabý
radar:
  logic_code: 31.8
  agentic: 33.0
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Velký kontext
  hidden_risk: Slabý výkon v logických úlohách a neznámá kvalita v češtině
  recommended_use_case: Analýza finančních dat s matematickými výpočty
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:19"
---

Mistral Large 3 2512 je dosud nejvýkonnější model od Mistralu, který využívá řídkou architekturu mixture-of-experts se 41 miliardami aktivních parametrů (celkem 675 miliard) a je uvolněn pod licencí Apache 2.0.

## Unikátní charakteristiky

Mistral Large 3 2512 využívá sparse MoE architekturu, což mu umožňuje dosahovat dobrých výsledků v matematických úlohách (MATH-500: 71.4%). Jeho velký kontext 262,144 tokenů je vhodný pro komplexní úlohy. Nicméně, jeho výkon v hard logic (HLE: 3.2%) je velmi slabý.

## Silné stránky

### Matematika
Relativně silný výkon v matematických úlohách, dosahuje 71.4% na MATH-500.

### Kontext
Velký kontext 262,144 tokenů umožňuje zpracování rozsáhlých dokumentů a komplexních úloh.

## Slabé stránky

### Logika
Velmi slabý výkon v hard logic úlohách (HLE: 3.2%).

### Rychlost
Označena jako 'Slabý', což naznačuje pomalou inferenci.
