---
layout: llm_review
title: "OpenAI: GPT-5 Image Mini"
date: "2025-10-16 16:23:03"
model_id: openai/gpt-5-image-mini
slug: openai-gpt-5-image-mini
provider: Openai
pricing:
  prompt_per_m: 2.5
  completion_per_m: 2.0
  blend_per_m: 2.375
context_length: 400,000
max_output: 128,000
input_modalities:
  - file
  - image
  - text
output_modalities:
  - image
  - text
focus:
  - Generování obrázků
  - Multimodální zpracování
strengths:
  - area: Multimodální schopnosti
    description: Nativně multimodální model, který kombinuje textové a obrazové vstupy a výstupy.
  - area: Cena
    description: Relativně nízká cena ve srovnání s jinými multimodálními modely, blend cena $2.38/1M tokenů.
weaknesses:
  - area: Nedostatek benchmarků
    description: Chybí benchmark data pro objektivní srovnání výkonu s konkurencí.
  - area: Neznámá kvalita češtiny
    description: Není známa kvalita zpracování češtiny, což je kritické pro lokální nasazení (chybí MMMLU skóre).
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: 2x dražší vstup, 12.5x dražší výstup
    comparison: Claude Opus 4.5 je silnější jazykový model, ale dražší. Konkuruje v kvalitě výstupu.
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: Podobná cena vstupu, 6x dražší výstup
    comparison: Gemini 3 Pro Image Preview konkuruje v multimodálních schopnostech, ale má menší kontext.
  - provider: OPENAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: Poloviční cena vstupu, 5x dražší výstup
    comparison: GPT-5.1 je silný jazykový model, ale není nativně multimodální.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: 8x levnější vstup, 1.25x dražší výstup
    comparison: Gemini 2.5 Flash Image je levnější, ale má menší kontext a může mít nižší kvalitu výstupu.
recommendation:
  target_users:
    - Marketingové týmy
    - Tvůrci obsahu
    - Vývojáři aplikací s vizuálními prvky
  use_cases:
    - Generování obrázků pro sociální média
    - Vytváření vizuálních konceptů
    - Automatické generování grafiky
  avoid_for:
    - Aplikace vyžadující extrémní přesnost a detail
    - Kritické aplikace s vysokými nároky na bezpečnost
verdict: GPT-5 Image Mini je vhodný pro uživatele, kteří hledají efektivní a cenově dostupný způsob generování obrázků s textovým porozuměním, ale měli by být opatrní kvůli nedostatku benchmark dat a neznámé kvalitě češtiny.
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
  killer_feature: Efektivní generování obrázků s textovým porozuměním za rozumnou cenu.
  hidden_risk: Neznámá kvalita češtiny a nedostatek benchmark dat pro objektivní srovnání.
  recommended_use_case: Rychlé generování vizuálního obsahu pro marketingové kampaně a sociální média.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:16"
---

GPT-5 Image Mini kombinuje pokročilé jazykové schopnosti OpenAI, poháněné [GPT-5 Mini](https://openrouter.ai/openai/gpt-5-mini), s GPT Image 1 Mini pro efektivní generování obrázků. Tento nativně multimodální model se vyznačuje vynikajícím dodržováním instrukcí, vykreslováním textu a detailní úpravou obrázků se sníženou latencí a náklady. Vyniká ve vysoce kvalitní vizuální tvorbě při zachování silného porozumění textu, což ho činí ideálním pro aplikace, které vyžadují efektivní generování obrázků a zpracování textu ve velkém měřítku.

## Unikátní charakteristiky

GPT-5 Image Mini kombinuje pokročilé jazykové schopnosti s generováním obrázků. Model je navržen pro efektivní generování obrázků s důrazem na detail a textové porozumění. Benchmark data nejsou k dispozici.

## Silné stránky

### Multimodální schopnosti
Nativně multimodální model, který kombinuje textové a obrazové vstupy a výstupy.

### Cena
Relativně nízká cena ve srovnání s jinými multimodálními modely, blend cena $2.38/1M tokenů.

## Slabé stránky

### Nedostatek benchmarků
Chybí benchmark data pro objektivní srovnání výkonu s konkurencí.

### Neznámá kvalita češtiny
Není známa kvalita zpracování češtiny, což je kritické pro lokální nasazení (chybí MMMLU skóre).
