---
layout: llm_review
title: "Mistral: Mistral Small 3.2 24B"
date: "2025-06-20 20:10:16"
model_id: mistralai/mistral-small-3.2-24b-instruct
slug: mistralai-mistral-small-3-2-24b-instruct
provider: Mistral
pricing:
  prompt_per_m: 0.06
  completion_per_m: 0.18
  blend_per_m: 0.09
context_length: 131,072
max_output: 131,072
input_modalities:
  - image
  - text
output_modalities:
  - text
focus:
  - Instrukce
  - Nástroje
strengths:
  - area: Multimodalita
    description: Podporuje obrazové a textové vstupy, což rozšiřuje možnosti použití.
  - area: Dlouhý kontext
    description: Kontext 131,072 tokenů umožňuje zpracovávat rozsáhlé dokumenty a komplexní konverzace.
weaknesses:
  - area: Cena
    description: Cena je vyšší než u některých konkurenčních modelů s podobnými parametry.
  - area: Benchmarky
    description: Benchmark data nejsou k dispozici, což ztěžuje objektivní srovnání s konkurencí.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-sonnet-4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: 33x dražší vstup, 83x dražší výstup
    comparison: Claude Sonnet 4.5 má větší kontext a pravděpodobně lepší výkon, ale je výrazně dražší.
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: 22x dražší vstup, 66x dražší výstup
    comparison: Gemini 3 Pro Image Preview nabízí multimodalitu, ale má menší kontext a je dražší.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 2x levnější vstup, 2.7x levnější výstup
    comparison: Grok-4.1-fast má obrovský kontext a je levnější, ale nemusí dosahovat stejné kvality výstupu.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: 2.2x dražší vstup, 1.1x dražší výstup
    comparison: Ministral-14b-2512 má větší kontext a může mít lepší výkon, ale je dražší.
recommendation:
  target_users:
    - Vývojáři aplikací s multimodálním vstupem
    - Firmy potřebující zpracovávat velké objemy textu
  use_cases:
    - Chatboti s podporou obrázků
    - Analýza dokumentů s obrázky a textem
  avoid_for:
    - Aplikace s extrémně nízkým rozpočtem
    - Úkoly vyžadující maximální rychlost inference
verdict: Mistral Small 3.2 je vhodný pro uživatele, kteří potřebují multimodalitu a dlouhý kontext, ale jsou ochotni zaplatit vyšší cenu a akceptovat nedostatek benchmark dat.
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
  killer_feature: Multimodalita a dlouhý kontext
  hidden_risk: Nedostatek benchmark dat pro objektivní srovnání
  recommended_use_case: Chatbot pro zákaznickou podporu, který dokáže zpracovávat obrázky a text.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:08"
---

Mistral-Small-3.2-24B-Instruct-2506 je aktualizovaný 24B parametrový model od Mistralu, optimalizovaný pro sledování instrukcí, redukci opakování a vylepšené volání funkcí. Oproti verzi 3.1, verze 3.2 významně zlepšuje přesnost na WildBench a Arena Hard, redukuje nekonečné generování a přináší zlepšení v používání nástrojů a úlohách se strukturovaným výstupem.

Podporuje obrazové a textové vstupy se strukturovanými výstupy, volání funkcí/nástrojů a silný výkon v kódování (HumanEval+, MBPP), STEM (MMLU, MATH, GPQA) a vizuálních benchmarkách (ChartQA, DocVQA).

## Unikátní charakteristiky

Mistral Small 3.2 je 24B model optimalizovaný pro sledování instrukcí, redukci opakování a vylepšené volání funkcí. Verze 3.2 přináší významné zlepšení přesnosti na WildBench a Arena Hard, snižuje nekonečné generování a zlepšuje využití nástrojů a strukturované výstupy. Podporuje obrazové a textové vstupy se strukturovanými výstupy a silný výkon v kódování, STEM a vizuálních benchmarkách.

## Silné stránky

### Multimodalita
Podporuje obrazové a textové vstupy, což rozšiřuje možnosti použití.

### Dlouhý kontext
Kontext 131,072 tokenů umožňuje zpracovávat rozsáhlé dokumenty a komplexní konverzace.

## Slabé stránky

### Cena
Cena je vyšší než u některých konkurenčních modelů s podobnými parametry.

### Benchmarky
Benchmark data nejsou k dispozici, což ztěžuje objektivní srovnání s konkurencí.
