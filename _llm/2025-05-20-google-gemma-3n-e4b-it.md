---
layout: llm_review
title: "Google: Gemma 3n 4B"
date: "2025-05-20 23:33:44"
model_id: google/gemma-3n-e4b-it
slug: google-gemma-3n-e4b-it
provider: Google
pricing:
  prompt_per_m: 0.02
  completion_per_m: 0.04
  blend_per_m: 0.025
context_length: 32,768
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Efektivita na mobilních zařízeních
  - Multimodální vstupy
strengths:
  - area: Cena
    description: Relativně nízká cena ve srovnání s jinými modely, blend cena $0.03/1M tokenů.
  - area: Kontextové okno
    description: Podporuje kontextové okno 32,768 tokenů, což je dostatečné pro mnoho úloh RAG.
weaknesses:
  - area: Benchmark data
    description: Chybí benchmark data, takže nelze objektivně posoudit výkon v různých úlohách.
  - area: Jazyková podpora
    description: Není známo, jak dobře model funguje v češtině (MMMLU skóre chybí).
competitors:
  - provider: MISTRALAI
    model: mistralai/ministral-3b-2512
    model_id: mistralai/ministral-3b-2512
    price_comparison: 3x levnější vstup i výstup
    comparison: Podobná velikost modelu, ale potenciálně lepší výkon (data nejsou k dispozici).
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: 7x levnější vstup, 8x levnější výstup
    comparison: Větší kontext, potenciálně lepší výkon (data nejsou k dispozici).
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: 15x dražší vstup, 62x dražší výstup
    comparison: Stejný kontext, ale potenciálně lepší výkon (data nejsou k dispozici).
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 10x levnější vstup, 12.5x levnější výstup
    comparison: Mnohem větší kontext, ale potenciálně horší výkon (data nejsou k dispozici).
recommendation:
  target_users:
    - Vývojáři mobilních aplikací
    - Uživatelé s omezenými hardwarovými zdroji
  use_cases:
    - Offline AI aplikace
    - Textová generace na mobilních zařízeních
  avoid_for:
    - Úlohy vyžadující maximální přesnost
    - Aplikace s vysokými nároky na češtinu
verdict: Gemma 3n E4B-it je vhodná pro vývojáře, kteří hledají efektivní model pro mobilní zařízení. Kvůli nedostatku benchmark dat je ale obtížné objektivně posoudit její výkon.
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
  killer_feature: Optimalizace pro mobilní zařízení
  hidden_risk: Nedostatek benchmark dat pro objektivní srovnání
  recommended_use_case: Generování textu na mobilních zařízeních s omezenými zdroji
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:05"
---

Gemma 3n E4B – je optimalizována pro efektivní spouštění na mobilních zařízeních a zařízeních s omezenými zdroji, jako jsou telefony, notebooky a tablety. Podporuje multimodální vstupy – včetně textu, vizuálních dat a zvuku – a umožňuje různorodé úlohy, jako je generování textu, rozpoznávání řeči, překlad a analýza obrazu. Díky využití inovací, jako je Per-Layer Embedding (PLE) caching a architektura MatFormer, Gemma 3n dynamicky spravuje využití paměti a výpočetní zátěž selektivní aktivací parametrů modelu, což výrazně snižuje požadavky na běhové zdroje.

Tento model podporuje širokou jazykovou škálu (trénován ve více než 140 jazycích) a nabízí flexibilní kontextové okno s 32 tisíci tokeny. Gemma 3n může selektivně načítat parametry, optimalizovat paměť a výpočetní efektivitu na základě úlohy nebo schopností zařízení, díky čemuž je vhodná pro aplikace zaměřené na soukromí, s offline funkcemi a pro AI řešení přímo na zařízení. [Více informací v blogovém příspěvku](https://developers.googleblog.com/en/introducing-gemma-3n/)

## Unikátní charakteristiky

Gemma 3n E4B-it je optimalizována pro efektivní běh na mobilních zařízeních a zařízeních s omezenými zdroji. Využívá Per-Layer Embedding (PLE) caching a architekturu MatFormer pro dynamickou správu paměti a výpočetní zátěže. Benchmark data nejsou k dispozici, takže nelze objektivně posoudit výkon.

## Silné stránky

### Cena
Relativně nízká cena ve srovnání s jinými modely, blend cena $0.03/1M tokenů.

### Kontextové okno
Podporuje kontextové okno 32,768 tokenů, což je dostatečné pro mnoho úloh RAG.

## Slabé stránky

### Benchmark data
Chybí benchmark data, takže nelze objektivně posoudit výkon v různých úlohách.

### Jazyková podpora
Není známo, jak dobře model funguje v češtině (MMMLU skóre chybí).
