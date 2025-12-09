---
layout: llm_review
title: "Google: Gemini 2.5 Flash Image (Nano Banana)"
date: "2025-10-07 22:53:51"
model_id: google/gemini-2.5-flash-image
slug: google-gemini-2-5-flash-image
provider: Google
pricing:
  prompt_per_m: 0.3
  completion_per_m: 2.5
  blend_per_m: 0.85
context_length: 32,768
max_output: 32,768
input_modalities:
  - image
  - text
output_modalities:
  - image
  - text
focus:
  - Generování obrázků
  - Konverzační AI
strengths:
  - area: Cena
    description: Relativně nízká cena ve srovnání s jinými multimodálními modely.
  - area: Multimodalita
    description: Schopnost zpracovávat a generovat obrázky i text.
weaknesses:
  - area: Benchmarky
    description: Benchmark data nejsou k dispozici, nelze objektivně posoudit výkon.
  - area: Kontext
    description: Relativně malý kontext (32,768 tokenů) ve srovnání s textovými modely.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: 16x dražší vstup, 10x dražší výstup
    comparison: Claude Opus je textový model s větším kontextem, vhodný pro náročnější textové úlohy. Gemini 2.5 Flash Image je zaměřen na obrázky.
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: 6.6x dražší vstup, 4.8x dražší výstup
    comparison: Gemini 3 Pro Image Preview má větší kontext, ale je dražší.
  - provider: OPENAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: 4.1x dražší vstup, 4x dražší výstup
    comparison: GPT-5.1 je textový model s větším kontextem, vhodný pro náročnější textové úlohy. Gemini 2.5 Flash Image je zaměřen na obrázky.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: O něco levnější vstup i výstup
    comparison: Ministral-14b-2512 je textový model s velkým kontextem, vhodný pro textové úlohy. Gemini 2.5 Flash Image je zaměřen na obrázky.
recommendation:
  target_users:
    - Tvůrci obsahu
    - Marketingoví specialisté
    - Vývojáři aplikací
  use_cases:
    - Generování obrázků pro sociální média
    - Vytváření vizuálů pro prezentace
    - Vývoj aplikací s vizuálním obsahem
  avoid_for:
    - Náročné textové úlohy
    - Aplikace vyžadující extrémně dlouhý kontext
    - Kritické aplikace vyžadující vysokou přesnost a spolehlivost
verdict: Gemini 2.5 Flash Image je vhodný pro uživatele, kteří hledají cenově dostupný model pro generování obrázků, ale měli by být opatrní kvůli chybějícím benchmarkům a potenciálním omezením v kvalitě a porozumění češtině.
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
  killer_feature: Nízká cena pro generování obrázků s kontextovým porozuměním.
  hidden_risk: Chybějící benchmark data znemožňují objektivní posouzení kvality generovaných obrázků a porozumění češtině.
  recommended_use_case: Rychlé generování obrázků pro interní použití nebo pro prototypování.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:14"
---

Gemini 2.5 Flash Image, známý také jako "Nano Banana," je nyní obecně dostupný. Jedná se o nejmodernější model pro generování obrázků s kontextuálním porozuměním. Je schopen generovat obrázky, provádět úpravy a vést vícekolové konverzace. Poměry stran lze ovládat pomocí [parametru API image_config](https://openrouter.ai/docs/features/multimodal/image-generation#image-aspect-ratio-configuration)

## Unikátní charakteristiky

Gemini 2.5 Flash Image je model pro generování obrázků s kontextovým porozuměním. Umožňuje editaci obrázků a vícekolové konverzace. Podpora nastavení poměru stran pomocí API.

## Silné stránky

### Cena
Relativně nízká cena ve srovnání s jinými multimodálními modely.

### Multimodalita
Schopnost zpracovávat a generovat obrázky i text.

## Slabé stránky

### Benchmarky
Benchmark data nejsou k dispozici, nelze objektivně posoudit výkon.

### Kontext
Relativně malý kontext (32,768 tokenů) ve srovnání s textovými modely.
