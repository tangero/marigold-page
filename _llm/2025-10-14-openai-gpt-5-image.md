---
layout: llm_review
title: "OpenAI: GPT-5 Image"
date: "2025-10-14 15:19:46"
model_id: openai/gpt-5-image
slug: openai-gpt-5-image
provider: Openai
pricing:
  prompt_per_m: 10.0
  completion_per_m: 10.0
  blend_per_m: 10.0
context_length: 400,000
max_output: 128,000
input_modalities:
  - image
  - text
  - file
output_modalities:
  - image
  - text
focus:
  - Generování obrázků
  - Multimodální aplikace
strengths:
  - area: Multimodálnost
    description: Model kombinuje textové a obrazové vstupy a výstupy, což umožňuje komplexní aplikace.
  - area: Editace obrázků
    description: Podle popisu modelu nabízí detailní možnosti editace obrázků, což je výhodné pro kreativní projekty.
weaknesses:
  - area: Cena
    description: Cena $10.00 za 1M tokenů vstupu i výstupu je relativně vysoká v porovnání s konkurencí.
  - area: Nedostatek benchmarků
    description: Chybějící benchmark data znemožňují objektivní srovnání s konkurencí a posouzení reálného výkonu.
competitors:
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: 5x levnější vstup, 1.2x dražší výstup
    comparison: Gemini 3 Pro Image Preview je levnější na vstupu, ale dražší na výstupu. Konkuruje v multimodálních úlohách.
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: 2x levnější vstup, 2.5x dražší výstup
    comparison: Claude Opus 4.5 je silný jazykový model, který může konkurovat v úlohách, kde je kladen důraz na textové usuzování a generování.
  - provider: GOOGLE
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: 5x levnější vstup, 1.2x dražší výstup
    comparison: Gemini 3 Pro Preview nabízí velký kontext a může konkurovat v úlohách vyžadujících zpracování dlouhých textů.
  - provider: OPENAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: 8x levnější vstup, stejný výstup
    comparison: GPT-5.1 je levnější alternativou pro textové úlohy, pokud není potřeba multimodálnost.
recommendation:
  target_users:
    - Kreativní profesionálové
    - Marketingové týmy
    - Vývojáři multimodálních aplikací
  use_cases:
    - Generování obrázků pro marketingové kampaně
    - Prototypování designu
    - Automatické generování vizuálního obsahu
  avoid_for:
    - Úlohy s vysokými nároky na přesnost a spolehlivost (kvůli chybějícím benchmarkům)
    - Aplikace s omezeným rozpočtem
verdict: GPT-5 Image je zajímavý model pro uživatele, kteří potřebují kombinovat text a obrázky, ale je nutné zvážit vysokou cenu a nedostatek objektivních dat o výkonu. Doporučuje se pro kreativní projekty a marketingové aplikace.
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
  killer_feature: Kombinace pokročilého jazykového modelu a generování obrázků
  hidden_risk: Vysoká cena a nedostatek benchmarků ztěžují posouzení reálné hodnoty a výkonu
  recommended_use_case: Generování vizuálního obsahu pro marketing a reklamu
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:15"
---

[GPT-5](https://openrouter.ai/openai/gpt-5) Image kombinuje nejpokročilejší jazykový model OpenAI s nejmodernějšími schopnostmi generování obrazu. Nabízí zásadní vylepšení v oblasti usuzování, kvality kódu a uživatelské zkušenosti a zároveň integruje vynikající schopnosti sledování instrukcí, vykreslování textu a detailní úpravy obrazu GPT Image 1.

## Unikátní charakteristiky

GPT-5 Image kombinuje pokročilý jazykový model s generováním obrázků. Podle popisu nabízí vylepšení v usuzování, kvalitě kódu a uživatelské zkušenosti, a také vylepšené instrukce, text rendering a detailní úpravy obrázků. Benchmark data nejsou k dispozici, takže nelze objektivně posoudit výkon.

## Silné stránky

### Multimodálnost
Model kombinuje textové a obrazové vstupy a výstupy, což umožňuje komplexní aplikace.

### Editace obrázků
Podle popisu modelu nabízí detailní možnosti editace obrázků, což je výhodné pro kreativní projekty.

## Slabé stránky

### Cena
Cena $10.00 za 1M tokenů vstupu i výstupu je relativně vysoká v porovnání s konkurencí.

### Nedostatek benchmarků
Chybějící benchmark data znemožňují objektivní srovnání s konkurencí a posouzení reálného výkonu.
