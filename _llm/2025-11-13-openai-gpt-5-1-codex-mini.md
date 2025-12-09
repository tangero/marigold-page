---
layout: llm_review
title: "OpenAI: GPT-5.1-Codex-Mini"
date: "2025-11-13 19:17:00"
model_id: openai/gpt-5.1-codex-mini
slug: openai-gpt-5-1-codex-mini
provider: Openai
pricing:
  prompt_per_m: 0.25
  completion_per_m: 2.0
  blend_per_m: 0.6875
context_length: 400,000
max_output: 100,000
input_modalities:
  - image
  - text
output_modalities:
  - text
focus:
  - Programování
  - Generování kódu
strengths:
  - area: Cena
    description: Relativně nízká cena ve srovnání s jinými modely OpenAI, což z něj činí dostupnější volbu pro některé úlohy.
  - area: Kontext
    description: Velký kontext 400 000 tokenů umožňuje zpracování rozsáhlejších úloh a dokumentů.
weaknesses:
  - area: Benchmarky
    description: Chybějící benchmark data znemožňují objektivní srovnání s konkurencí v konkrétních úlohách.
  - area: Jazyková podpora
    description: Nedostatek informací o výkonu v češtině (MMMLU) ztěžuje posouzení vhodnosti pro české uživatele.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Vstup 4x dražší, výstup 2.5x dražší
    comparison: Claude Haiku je rychlejší a levnější, ale má menší kontext. Vhodný pro rychlé a jednoduché úlohy.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Vstup mírně dražší, výstup podobný
    comparison: Gemini 2.5 Flash má menší kontext, ale může být vhodný pro úlohy s obrázky.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Vstup levnější, výstup výrazně levnější
    comparison: Grok má mnohem větší kontext a nižší cenu, ale neznáme jeho výkon v programování.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Vstup i výstup levnější
    comparison: Ministral 14B je levnější, ale má menší kontext. Potřebuje otestovat v programovacích úlohách.
recommendation:
  target_users:
    - Vývojáři
    - Firmy s omezeným rozpočtem
  use_cases:
    - Generování kódu
    - Automatizace jednoduchých programovacích úloh
  avoid_for:
    - Složité programovací úlohy
    - Aplikace vyžadující vysokou přesnost a spolehlivost
verdict: GPT-5.1-Codex-Mini je vhodný pro vývojáře a firmy s omezeným rozpočtem, kteří potřebují generovat jednoduchý kód a automatizovat programovací úlohy. Je však nutné ověřit jeho výkon v konkrétních úlohách a jazycích.
benchmark_categories: null
overall_score: null
overall_tier: null
radar:
  logic_code: 0
  agentic: 0
  languages: 0
  safety: 0
  speed: Nehodnoceno
expert_verdict:
  killer_feature: Relativně nízká cena a velký kontext
  hidden_risk: Chybějící benchmarky a neznámý výkon v češtině
  recommended_use_case: Generování jednoduchých skriptů a automatizace opakujících se programovacích úloh
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:17"
---

GPT-5.1-Codex-Mini je menší a rychlejší verze GPT-5.1-Codex.

## Unikátní charakteristiky

GPT-5.1-Codex-Mini je menší a rychlejší verze GPT-5.1-Codex. Benchmark data pro detailní charakteristiku nejsou k dispozici.

## Silné stránky

### Cena
Relativně nízká cena ve srovnání s jinými modely OpenAI, což z něj činí dostupnější volbu pro některé úlohy.

### Kontext
Velký kontext 400 000 tokenů umožňuje zpracování rozsáhlejších úloh a dokumentů.

## Slabé stránky

### Benchmarky
Chybějící benchmark data znemožňují objektivní srovnání s konkurencí v konkrétních úlohách.

### Jazyková podpora
Nedostatek informací o výkonu v češtině (MMMLU) ztěžuje posouzení vhodnosti pro české uživatele.
