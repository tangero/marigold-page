---
layout: llm_review
title: "Google: Gemma 3 12B"
date: "2025-03-13 22:50:25"
model_id: google/gemma-3-12b-it
slug: google-gemma-3-12b-it
provider: Google
pricing:
  prompt_per_m: 0.03
  completion_per_m: 0.1
  blend_per_m: 0.0475
context_length: 131,072
max_output: 131,072
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Multimodální vstupy
  - Dlouhý kontext
strengths:
  - area: Multimodalita
    description: Podpora obrazových vstupů rozšiřuje možnosti použití modelu.
  - area: Dlouhý kontext
    description: Kontextové okno 128k tokenů umožňuje zpracovávat delší dokumenty a konverzace.
weaknesses:
  - area: Benchmark data
    description: Chybějící benchmark data znemožňují objektivní srovnání s konkurencí.
  - area: Cena
    description: Cena je vyšší než u některých konkurenčních modelů s podobnými parametry.
competitors:
  - provider: Google
    model: gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: Podobná cena vstupu, dražší výstup
    comparison: Konkuruje v multimodálnosti, ale má kratší kontext.
  - provider: MistralAI
    model: ministral-3b-2512
    model_id: mistralai/ministral-3b-2512
    price_comparison: Mnohem levnější
    comparison: Levnější alternativa, ale bez multimodality a s menším počtem parametrů.
  - provider: DeepSeek
    model: deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: Levnější vstup, levnější výstup
    comparison: Levnější alternativa, ale bez multimodality a s kratším kontextem.
  - provider: X-AI
    model: grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Mnohem levnější
    comparison: Výrazně levnější, ale bez multimodality a s potenciálně nižší kvalitou výstupu.
recommendation:
  target_users:
    - Vývojáři multimodálních aplikací
    - Firmy zpracovávající velké objemy textu
  use_cases:
    - Analýza obrázků s textovým popisem
    - Chatbot s podporou obrázků
  avoid_for:
    - Aplikace vyžadující extrémně nízkou latenci
    - Úkoly s vysokými nároky na přesnost a spolehlivost, dokud nejsou k dispozici benchmarky
verdict: Gemma 3 12B je zajímavá volba pro vývojáře, kteří chtějí experimentovat s multimodálními vstupy a dlouhým kontextem, ale je třeba počítat s vyšší cenou a chybějícími benchmarky.
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
  killer_feature: Multimodální vstupy s dlouhým kontextem
  hidden_risk: Nejasná kvalita výstupu v češtině (chybí MMMLU data)
  recommended_use_case: Prototypování multimodálních aplikací a experimentování s dlouhým kontextem.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:00"
---

Gemma 3 přináší multimodalitu, podporuje vstup v podobě obrazu a jazyka a textové výstupy. Zvládá kontextová okna až do velikosti 128 tisíc tokenů, rozumí více než 140 jazykům a nabízí vylepšené matematické, logické a chatovací schopnosti, včetně strukturovaných výstupů a volání funkcí. Gemma 3 12B je druhý největší model z rodiny modelů Gemma 3 po [Gemma 3 27B](google/gemma-3-27b-it).

## Unikátní charakteristiky

Gemma 3 12B je multimodální model s podporou obrazových vstupů a textových výstupů. Nabízí kontextové okno až 128k tokenů a rozumí více než 140 jazykům. Data z benchmarků nejsou k dispozici.

## Silné stránky

### Multimodalita
Podpora obrazových vstupů rozšiřuje možnosti použití modelu.

### Dlouhý kontext
Kontextové okno 128k tokenů umožňuje zpracovávat delší dokumenty a konverzace.

## Slabé stránky

### Benchmark data
Chybějící benchmark data znemožňují objektivní srovnání s konkurencí.

### Cena
Cena je vyšší než u některých konkurenčních modelů s podobnými parametry.
