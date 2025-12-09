---
layout: llm_review
title: "Google: Gemma 3 4B"
date: "2025-03-13 23:38:30"
model_id: google/gemma-3-4b-it
slug: google-gemma-3-4b-it
provider: Google
pricing:
  prompt_per_m: 0.017
  completion_per_m: 0.0682
  blend_per_m: 0.0298
context_length: 96,000
max_output: N/A
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Multimodalita
  - Chat
strengths:
  - area: Multimodalita
    description: Podporuje zpracování obrazových vstupů a generování textových výstupů, což rozšiřuje možnosti použití.
  - area: Dlouhý kontext
    description: Kontextové okno 96 000 tokenů umožňuje zpracování delších textů a složitějších konverzací.
weaknesses:
  - area: Chybějící benchmarky
    description: Nedostatek benchmark dat znemožňuje objektivní srovnání s konkurencí v různých úlohách.
  - area: Neznámá kvalita češtiny
    description: Bez MMMLU skóre nelze posoudit kvalitu generování textu v češtině.
competitors:
  - provider: Google
    model: gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: Gemma 3 je výrazně levnější.
    comparison: Gemini Pro Image má lepší multimodalitu, ale je dražší. Gemma 3 je levnější alternativa.
  - provider: Google
    model: gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Gemma 3 je levnější.
    comparison: Gemini Flash Image je rychlejší, ale Gemma 3 má větší kontext a lepší schopnosti chatu.
  - provider: Anthropic
    model: claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Claude Haiku je dražší.
    comparison: Claude Haiku je rychlejší, ale Gemma 3 má větší kontext a potenciálně lepší schopnosti chatu.
  - provider: MistralAI
    model: ministral-3b-2512
    model_id: mistralai/ministral-3b-2512
    price_comparison: Podobná cena.
    comparison: Ministral 3B je menší model, Gemma 3 má lepší multimodalitu a větší kontext.
recommendation:
  target_users:
    - Vývojáři prototypující multimodalní aplikace
    - Uživatelé hledající levný model pro chat
  use_cases:
    - Prototypování aplikací s obrazovým vstupem
    - Chatboti s dlouhým kontextem
  avoid_for:
    - Produkční nasazení vyžadující vysokou spolehlivost
    - Aplikace vyžadující perfektní češtinu
verdict: Gemma 3 4B je vhodná pro vývojáře, kteří chtějí experimentovat s multimodalitou za nízkou cenu. Je však třeba počítat s tím, že kvalita češtiny a celkový výkon nejsou objektivně změřeny.
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
  killer_feature: Multimodalita za nízkou cenu
  hidden_risk: Neznámá kvalita češtiny a chybějící benchmarky
  recommended_use_case: Prototypování multimodalních chatovacích aplikací
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:00"
---

Gemma 3 zavádí multimodalitu, podporuje vstup obrazu a jazyka a textové výstupy. Zvládá kontextová okna až do 128 tisíc tokenů, rozumí více než 140 jazykům a nabízí vylepšené matematické, logické a chatovací schopnosti, včetně strukturovaných výstupů a volání funkcí.

## Unikátní charakteristiky

Gemma 3 4B je multimodalní model, který podporuje zpracování obrazových vstupů a generování textových výstupů. Má rozšířené kontextové okno až na 128 tisíc tokenů a rozumí více než 140 jazykům. Nabízí vylepšené matematické, logické a chatovací schopnosti, včetně strukturovaných výstupů a volání funkcí. Benchmark data nejsou k dispozici.

## Silné stránky

### Multimodalita
Podporuje zpracování obrazových vstupů a generování textových výstupů, což rozšiřuje možnosti použití.

### Dlouhý kontext
Kontextové okno 96 000 tokenů umožňuje zpracování delších textů a složitějších konverzací.

## Slabé stránky

### Chybějící benchmarky
Nedostatek benchmark dat znemožňuje objektivní srovnání s konkurencí v různých úlohách.

### Neznámá kvalita češtiny
Bez MMMLU skóre nelze posoudit kvalitu generování textu v češtině.
