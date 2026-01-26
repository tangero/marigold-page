---
layout: llm_review
title: "Z.AI: GLM 4.7 Flash"
date: "2026-01-19 15:45:13"
model_id: z-ai/glm-4.7-flash
slug: z-ai-glm-4-7-flash
provider: Z-Ai
pricing:
  prompt_per_m: 0.07
  completion_per_m: 0.4
context_length: 200,000
max_output: 131,072
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Agentní kódování
  - Efektivita nákladů
  - Dlouhodobé plánování úloh
competitors:
  - provider: MistralAI
    model: devstral-2512
    model_id: mistralai/devstral-2512
    price_comparison: Levnější vstup ($0.05 vs $0.07) i výstup ($0.22 vs $0.40)
    comparison: Devstral je přímý konkurent zaměřený na vývojáře s ještě nižší cenou a větším kontextem (262k), GLM však může nabízet lepší schopnosti v obecném plánování mimo čistý kód.
  - provider: DeepSeek
    model: deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: 3x dražší vstup ($0.21), ale levnější výstup ($0.32)
    comparison: DeepSeek je silný v logice, ale GLM 4.7 Flash je výrazně ekonomičtější pro úlohy náročné na čtení kontextu (input-heavy).
  - provider: X-AI
    model: grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Cca 3x dražší vstup ($0.20), podobný výstup ($0.50)
    comparison: Grok nabízí desetinásobný kontext (2M), ale pro úlohy do 200k tokenů nabízí GLM lepší návratnost investic.
recommendation:
  target_users:
    - Vývojáři autonomních agentů
    - SaaS platformy zpracovávající velké objemy textu
    - Startupy s omezeným rozpočtem na inferenci
  use_cases:
    - Generování rozsáhlé dokumentace a kódu
    - Analýza logů a dlouhých dokumentů (RAG)
    - Orchestrace nástrojů v rámci agentních systémů
  avoid_for:
    - Úlohy vyžadující analýzu obrázků nebo zvuku
    - Kreativní psaní vyžadující vysokou stylistickou úroveň
    - Extrémně komplexní logické úlohy vyžadující model třídy Frontier (GPT-5/Opus)
verdict: Vynikající volba pro vysokoobjemové, automatizované procesy a kódovací agenty, kde je prioritou nízká cena a velký kontext, nikoliv absolutní špičková inteligence největších modelů.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2026-01-20 07:27"
---

Jako SOTA model třídy 30B nabízí GLM-4.7-Flash novou možnost, která vyvažuje výkon a efektivitu. Je dále optimalizován pro agentní případy použití v kódování, posiluje schopnosti kódování, plánování úloh s dlouhým horizontem a spolupráci s nástroji, a dosáhl špičkového výkonu mezi open-source modely stejné velikosti na několika současných veřejných žebříčcích benchmarků.

## Unikátní charakteristiky

GLM 4.7 Flash je model střední velikosti (30B), který agresivně optimalizuje poměr ceny a výkonu pro agentní pracovní toky a generování kódu. Vyniká vysokým limitem pro výstupní tokeny (131k) a specifickým laděním pro používání externích nástrojů (tool use).

## Silné stránky

### Cenová efektivita
S cenou $0.07 za 1M vstupních tokenů patří k nejlevnějším modelům na trhu, což umožňuje masivní RAG operace s minimálními náklady.

### Výstupní kapacita
Maximální výstup 131,072 tokenů je výrazně vyšší než u většiny konkurentů (standardně 4k-8k), což je klíčové pro generování celých softwarových modulů.

### Agentní specializace
Model je explicitně trénován pro 'long-horizon task planning', což zvyšuje spolehlivost při autonomním řešení složitých, vícekrokových úloh.

## Slabé stránky

### Omezená modalita
Model podporuje pouze text-to-text, což jej znevýhodňuje oproti multimodálním konkurentům (např. Gemini Flash) při analýze vizuálních dat.

### Hloubka znalostí
Jako 30B model nemůže konkurovat v encyklopedické šíři znalostí a nuancích modelům třídy 'Pro' nebo 'Opus' s parametry nad 100B.
