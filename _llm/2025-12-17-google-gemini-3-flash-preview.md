---
layout: llm_review
title: "Google: Gemini 3 Flash Preview"
date: "2025-12-17 16:57:58"
model_id: google/gemini-3-flash-preview
slug: google-gemini-3-flash-preview
provider: Google
pricing:
  prompt_per_m: 0.5
  completion_per_m: 3.0
context_length: 1,048,576
max_output: 65,535
input_modalities:
  - text
  - image
  - file
  - audio
  - video
output_modalities:
  - text
focus:
  - Agentní workflow
  - Multimodální uvažování (Reasoning)
  - Nízká latence
competitors:
  - provider: Anthropic
    model: Claude Haiku 4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Gemini je 2x levnější na vstupu a 1.6x levnější na výstupu
    comparison: Gemini nabízí 5x větší kontext (1M vs 200k) a pokročilejší 'thinking' schopnosti; Haiku 4.5 může být rychlejší pro jednoduché textové úlohy.
  - provider: x-AI
    model: Grok 4.1 Fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Gemini je 2.5x dražší na vstupu a 6x dražší na výstupu
    comparison: Grok vítězí hrubou cenou a velikostí kontextu (2M), Gemini kontruje lepší integrací agentních nástrojů a nativním zpracováním videa/audia.
  - provider: OpenAI
    model: GPT-5.2 Chat
    model_id: openai/gpt-5.2-chat
    price_comparison: Gemini je 3.5x levnější na vstupu a 4.6x levnější na výstupu
    comparison: Gemini 3 Flash poskytuje srovnatelnou či lepší kvalitu uvažování za zlomek ceny GPT-5.2 Chat a nabízí téměř 8x větší kontext.
recommendation:
  target_users:
    - Vývojáři autonomních agentů
    - Platformy pro analýzu dat a videa
    - SaaS aplikace vyžadující komplexní logiku s nízkou latencí
  use_cases:
    - Dlouhodobé agentní smyčky (agent loops)
    - Analýza dlouhých videí a audio záznamů
    - Interaktivní asistence při kódování (díky nízké latenci)
  avoid_for:
    - Extrémně levné klasifikační úlohy (zde je lepší Grok nebo Mistral)
    - Úlohy vyžadující absolutně nejvyšší možnou přesnost bez ohledu na cenu (zde volit Opus 4.5 nebo GPT-5.2 Pro)
verdict: Gemini 3 Flash Preview je aktuálně nejvýhodnější volbou pro komplexní agentní systémy, kde je kritická rovnováha mezi schopností uvažování, velikostí kontextu a provozními náklady.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2025-12-17 18:28"
---

Gemini 3 Flash Preview je vysokorychlostní, vysoce hodnotný myšlenkový model navržený pro agentní pracovní postupy, vícekolové konverzace a asistenci při kódování. Poskytuje úroveň uvažování a výkonu při používání nástrojů blížící se verzi Pro s podstatně nižší latencí než větší varianty Gemini, díky čemuž je vhodný pro interaktivní vývoj, dlouhotrvající agentní smyčky a úlohy kolaborativního kódování. Ve srovnání s Gemini 2.5 Flash poskytuje široké zlepšení kvality v oblasti uvažování, multimodálního porozumění a spolehlivosti.

Model podporuje kontextové okno o velikosti 1M tokenů a multimodální vstupy včetně textu, obrázků, zvuku, videa a PDF, s textovým výstupem. Zahrnuje konfigurovatelné uvažování prostřednictvím úrovní myšlení (minimální, nízká, střední, vysoká), strukturovaný výstup, používání nástrojů a automatické ukládání kontextu do mezipaměti. Gemini 3 Flash Preview je optimalizován pro uživatele, kteří chtějí silné uvažování a agentní chování bez nákladů nebo latence plnohodnotných frontier modelů.

## Unikátní charakteristiky

Gemini 3 Flash Preview unikátně kombinuje nízkou latenci a cenu kategorie 'Flash' s pokročilými schopnostmi uvažování (Thinking levels), které byly dříve doménou pouze největších modelů. Model se vyznačuje masivním kontextovým oknem 1M tokenů a nativní podporou zpracování videa, audia a dokumentů v reálném čase.

## Silné stránky

### Poměr cena/výkon
S cenou $0.50 za 1M vstupních tokenů nabízí schopnosti uvažování (reasoning) výrazně levněji než srovnatelné modely od OpenAI či Anthropic.

### Konfigurovatelné uvažování
Unikátní možnost nastavit hloubku přemýšlení (minimal až high) umožňuje vývojářům dynamicky vyvažovat latenci a kvalitu výstupu podle typu úlohy.

### Multimodální kontext
Kombinace 1M kontextového okna s nativním zpracováním videa a audia umožňuje efektivní analýzu dlouhých multimediálních záznamů bez nutnosti externí transkripce.

## Slabé stránky

### Cena výstupu
Poměr ceny výstupu k vstupu (6:1) je vysoký; generování dlouhých textů je relativně dražší ($3.00/1M) ve srovnání s velmi levným vstupem.

### Konkurence v kontextu
Ačkoliv je 1M tokenů nadstandard, konkurenční modely x-AI (Grok) nabízejí v podobné cenové hladině dvojnásobný kontext (2M).
