---
layout: llm_review
title: "OpenAI: o3 Pro"
date: "2025-06-11 01:32:32"
model_id: openai/o3-pro
slug: openai-o3-pro
provider: Openai
pricing:
  prompt_per_m: 20.0
  completion_per_m: 80.0
  blend_per_m: 35.0
context_length: 200,000
max_output: 100,000
input_modalities:
  - text
  - file
  - image
output_modalities:
  - text
focus:
  - Rozumování
  - Věda
strengths:
  - area: Věda a matematika
    description: Vynikající výkon v GPQA Diamond benchmarku (84.5%), což značí silné schopnosti v řešení vědeckých problémů.
  - area: Kontext
    description: Velký kontext 200 000 tokenů umožňuje zpracování rozsáhlých dokumentů a složitých úloh.
weaknesses:
  - area: Rychlost
    description: Velmi pomalá rychlost zpracování, TPS pouze 29.5 a TTFT 103.672s, což omezuje použitelnost v interaktivních aplikacích.
  - area: Čeština
    description: Chybí data o výkonu v češtině, což ztěžuje posouzení vhodnosti pro české uživatele.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: Levnější vstup (4x), levnější výstup (3x)
    comparison: Claude Opus je levnější a pravděpodobně rychlejší, ale nemusí dosahovat tak vysoké přesnosti ve vědeckých úlohách (data nejsou k dispozici).
  - provider: GOOGLE
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Levnější vstup (10x), levnější výstup (6.6x)
    comparison: Gemini 3 Pro je výrazně levnější a má větší kontext, ale chybí data pro srovnání kvality ve vědeckých úlohách.
  - provider: OPENAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: Levnější vstup (16x), levnější výstup (8x)
    comparison: GPT-5.1 je výrazně levnější, ale má menší kontext a chybí data pro srovnání kvality ve vědeckých úlohách.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Výrazně levnější vstup (100x), výrazně levnější výstup (160x)
    comparison: Grok je extrémně levný a má obrovský kontext, ale chybí data pro srovnání kvality ve vědeckých úlohách.
recommendation:
  target_users:
    - Vědci
    - Výzkumníci
  use_cases:
    - Analýza vědeckých dat
    - Řešení komplexních vědeckých problémů
  avoid_for:
    - Interaktivní aplikace vyžadující rychlou odezvu
    - Úlohy vyžadující znalost češtiny
verdict: OpenAI o3-pro je vhodný pro vědce a výzkumníky, kteří potřebují vysokou přesnost v řešení komplexních vědeckých problémů a nevadí jim pomalá rychlost zpracování.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 84.5
    tier: Výborný
  speed:
    name: Rychlost
    icon: ⚡
    score: 7.4
    tier: Slabý
overall_score: 58.8
overall_tier: Průměrný
radar:
  logic_code: 0
  agentic: 0
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající výkon ve vědeckých úlohách (GPQA Diamond)
  hidden_risk: Extrémně pomalá inference, což omezuje použitelnost v reálném čase
  recommended_use_case: Hloubková analýza vědeckých dat a řešení komplexních problémů, kde není rychlost kritická
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:07"
---

Modely řady o jsou trénovány pomocí posilovaného učení, aby přemýšlely před odpovědí a prováděly komplexní usuzování. Model o3-pro využívá více výpočetního výkonu k intenzivnějšímu přemýšlení a poskytování trvale lepších odpovědí.

Upozorňujeme, že pro tento model je vyžadováno BYOK (Bring Your Own Key). Nastavte si jej zde: https://openrouter.ai/settings/integrations

## Unikátní charakteristiky

Model o3-pro je trénován s posilovacím učením pro komplexní rozumování. Dosahuje vysokého skóre v GPQA Diamond (84.5%), což naznačuje silné schopnosti ve vědeckých úlohách, ale má pomalou rychlost (TPS 29.5, TTFT 103.672s).

## Silné stránky

### Věda a matematika
Vynikající výkon v GPQA Diamond benchmarku (84.5%), což značí silné schopnosti v řešení vědeckých problémů.

### Kontext
Velký kontext 200 000 tokenů umožňuje zpracování rozsáhlých dokumentů a složitých úloh.

## Slabé stránky

### Rychlost
Velmi pomalá rychlost zpracování, TPS pouze 29.5 a TTFT 103.672s, což omezuje použitelnost v interaktivních aplikacích.

### Čeština
Chybí data o výkonu v češtině, což ztěžuje posouzení vhodnosti pro české uživatele.
