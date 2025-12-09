---
layout: llm_review
title: "Mistral: Mistral Small 3.1 24B"
date: "2025-03-17 20:15:37"
model_id: mistralai/mistral-small-3.1-24b-instruct
slug: mistralai-mistral-small-3-1-24b-instruct
provider: Mistral
pricing:
  prompt_per_m: 0.03
  completion_per_m: 0.11
  blend_per_m: 0.05
context_length: 131,072
max_output: 131,072
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Multimodální aplikace
  - Dlouhé kontexty
strengths:
  - area: Multimodalita
    description: Podpora textových i obrazových vstupů rozšiřuje možnosti použití.
  - area: Dlouhý kontext
    description: Kontextové okno 131 072 tokenů umožňuje zpracování dlouhých dokumentů a komplexních konverzací.
weaknesses:
  - area: Nedostatek benchmarků
    description: Chybějící benchmark data znemožňují objektivní srovnání s konkurencí.
  - area: Cena
    description: Cena za výstup je vyšší než u některých konkurenčních modelů.
competitors:
  - provider: ANTHROPIC
    model: claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: Výrazně dražší
    comparison: Claude Opus je výkonnější, ale výrazně dražší. Pokud je cena kritická, Mistral Small může být lepší volba.
  - provider: GOOGLE
    model: gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: Podobná cena za vstup, dražší výstup
    comparison: Gemini Pro Image Preview nabízí multimodální schopnosti, ale má menší kontextové okno.
  - provider: X-AI
    model: grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Levnější
    comparison: Grok je levnější a má větší kontextové okno, ale nemusí dosahovat stejné kvality výstupu.
  - provider: MISTRALAI
    model: ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Levnější
    comparison: Ministral 14b je levnější, ale nemusí mít multimodální schopnosti.
recommendation:
  target_users:
    - Vývojáři multimodálních aplikací
    - Firmy zpracovávající dlouhé dokumenty
  use_cases:
    - Chatboti s podporou obrázků
    - Analýza rozsáhlých datových sad
  avoid_for:
    - Aplikace vyžadující maximální výkon
    - Aplikace citlivé na cenu
verdict: Mistral Small 3.1 24B Instruct je vhodný pro vývojáře, kteří hledají multimodální model s velkým kontextovým oknem, ale nemají k dispozici benchmark data pro srovnání s konkurencí.
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
  killer_feature: Multimodalita a velký kontext
  hidden_risk: Nedostatek benchmark dat pro objektivní srovnání
  recommended_use_case: Prototypování multimodálních aplikací s dlouhým kontextem
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:00"
---

Mistral Small 3.1 24B Instruct je vylepšená varianta modelu Mistral Small 3 (2501), která disponuje 24 miliardami parametrů a pokročilými multimodálními schopnostmi. Poskytuje špičkový výkon v úlohách založených na textovém usuzování a vizuálních úlohách, včetně analýzy obrazu, programování, matematického usuzování a vícejazyčné podpory v desítkách jazyků. Je vybaven rozsáhlým kontextovým oknem o velikosti 128k tokenů a optimalizován pro efektivní lokální inferenci, podporuje případy použití jako konverzační agenti, volání funkcí, porozumění dlouhým dokumentům a nasazení citlivá na soukromí. Aktualizovaná verze je [Mistral Small 3.2](mistralai/mistral-small-3.2-24b-instruct)

## Unikátní charakteristiky

Mistral Small 3.1 24B Instruct je multimodální model s velkým kontextovým oknem. Absence benchmark dat znemožňuje přesné hodnocení jeho výkonu v různých oblastech.

## Silné stránky

### Multimodalita
Podpora textových i obrazových vstupů rozšiřuje možnosti použití.

### Dlouhý kontext
Kontextové okno 131 072 tokenů umožňuje zpracování dlouhých dokumentů a komplexních konverzací.

## Slabé stránky

### Nedostatek benchmarků
Chybějící benchmark data znemožňují objektivní srovnání s konkurencí.

### Cena
Cena za výstup je vyšší než u některých konkurenčních modelů.
