---
layout: llm_review
title: "Google: Gemma 3 27B"
date: "2025-03-12 06:12:39"
model_id: google/gemma-3-27b-it
slug: google-gemma-3-27b-it
provider: Google
pricing:
  prompt_per_m: 0.05
  completion_per_m: 0.22
  blend_per_m: 0.0925
context_length: 96,000
max_output: 96,000
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Multimodální aplikace
  - Chatboti
strengths:
  - area: Multimodalita
    description: Podpora obrazového vstupu rozšiřuje možnosti použití modelu.
  - area: Dlouhý kontext
    description: Kontextové okno 96,000 tokenů umožňuje zpracovávat delší dokumenty a konverzace.
weaknesses:
  - area: Cena výstupu
    description: Cena za výstup je relativně vysoká v porovnání s jinými modely.
  - area: Chybějící benchmarky
    description: Nedostupnost benchmark dat znemožňuje objektivní srovnání s konkurencí v různých úlohách.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: Dražší vstup i výstup
    comparison: Claude Opus 4.5 je dražší, ale nabízí větší kontext a potenciálně lepší výkon (data nejsou k dispozici pro Gemma 3).
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: Dražší vstup i výstup
    comparison: Gemini 3 Pro Image Preview je dražší, ale může nabízet lepší multimodální schopnosti (data nejsou k dispozici pro Gemma 3).
  - provider: OPENAI
    model: openai/gpt-5.1-chat
    model_id: openai/gpt-5.1-chat
    price_comparison: Dražší vstup i výstup
    comparison: GPT-5.1-chat je dražší, ale má kratší kontextové okno. Výkonnostní srovnání není možné bez benchmarků.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Levnější vstup i výstup
    comparison: Mistral 14B je levnější, ale nenabízí multimodální schopnosti. Má delší kontextové okno.
recommendation:
  target_users:
    - Vývojáři multimodálních aplikací
    - Firmy hledající open-source řešení
  use_cases:
    - Chatboti s podporou obrázků
    - Zpracování dokumentů s obrázky
  avoid_for:
    - Aplikace vyžadující maximální výkon a přesnost
    - Aplikace citlivé na cenu výstupu
verdict: Gemma 3 27B je zajímavá volba pro vývojáře, kteří chtějí experimentovat s multimodálními aplikacemi a preferují open-source řešení. Nicméně, kvůli chybějícím benchmarkům je obtížné objektivně posoudit její výkon v porovnání s konkurencí.
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
  killer_feature: Multimodalita a open-source licence
  hidden_risk: Výkonnostní nedostatky v češtině (bez MMMLU dat nelze potvrdit)
  recommended_use_case: Prototypování multimodálních aplikací a experimentování s novými funkcemi
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 12:59"
---

Gemma 3 zavádí multimodalitu, podporuje vstup v podobě obrazu a jazyka a textové výstupy. Zvládá kontextová okna až do velikosti 128 tisíc tokenů, rozumí více než 140 jazykům a nabízí vylepšené matematické, logické a chatovací schopnosti, včetně strukturovaných výstupů a volání funkcí. Gemma 3 27B je nejnovější open source model od Googlu, nástupce [Gemma 2](google/gemma-2-27b-it).

## Unikátní charakteristiky

Gemma 3 27B je multimodální model s podporou obrazového vstupu a textového výstupu. Zvládá kontextové okno až 128k tokenů a rozumí více než 140 jazykům. Benchmark data nejsou k dispozici, takže nelze objektivně posoudit jeho výkon v porovnání s konkurencí.

## Silné stránky

### Multimodalita
Podpora obrazového vstupu rozšiřuje možnosti použití modelu.

### Dlouhý kontext
Kontextové okno 96,000 tokenů umožňuje zpracovávat delší dokumenty a konverzace.

## Slabé stránky

### Cena výstupu
Cena za výstup je relativně vysoká v porovnání s jinými modely.

### Chybějící benchmarky
Nedostupnost benchmark dat znemožňuje objektivní srovnání s konkurencí v různých úlohách.
