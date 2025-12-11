---
layout: llm_review
title: "OpenAI: GPT-5.2 Chat"
date: "2025-12-10 19:03:03"
model_id: openai/gpt-5.2-chat
slug: openai-gpt-5-2-chat
provider: Openai
pricing:
  prompt_per_m: 1.75
  completion_per_m: 14.0
context_length: 128,000
max_output: 16,384
input_modalities:
  - file
  - image
  - text
output_modalities:
  - text
focus:
  - Nízká latence
  - Adaptivní uvažování
  - Interaktivní chat
competitors:
  - provider: Anthropic
    model: Claude Sonnet 4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: Vstup o 71 % dražší, výstup o 7 % dražší
    comparison: Sonnet 4.5 nabízí téměř 8x větší kontext (1M vs 128k), což jej činí lepším pro RAG a analýzu dokumentů, zatímco GPT-5.2 Chat cílí na rychlejší konverzační výměny.
  - provider: Google
    model: Gemini 3 Pro Preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Vstup o 14 % dražší, výstup o 14 % levnější
    comparison: Gemini 3 Pro nabízí masivní kontext (1M+) za srovnatelnou cenu, což představuje silnou konkurenci pro GPT-5.2 Chat v úlohách vyžadujících paměť.
  - provider: OpenAI
    model: GPT-5.2
    model_id: openai/gpt-5.2
    price_comparison: Identická cena
    comparison: Standardní verze GPT-5.2 nabízí více než trojnásobný kontext (400k) za stejnou cenu; verze Chat je preferována pouze pokud je prioritou latence a konverzační tón.
recommendation:
  target_users:
    - Vývojáři chatbotů
    - Zákaznická podpora
    - Týmy vyžadující real-time asistenci
  use_cases:
    - Interaktivní kódování s nízkou latencí
    - Složité konverzační scénáře
    - Rychlé řešení logických úloh
  avoid_for:
    - Analýza rozsáhlých repozitářů (nad 128k tokenů)
    - Dávkové zpracování dat (kvůli ceně)
verdict: GPT-5.2 Chat je optimální volbou pro aplikace vyžadující rovnováhu mezi inteligencí a rychlostí odezvy, kde není kritická velikost kontextového okna.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2025-12-11 20:31"
---

GPT-5.2 Chat (AKA Instant) je rychlý, nenáročný člen rodiny 5.2, optimalizovaný pro chat s nízkou latencí při zachování silné obecné inteligence. Využívá adaptivní usuzování k selektivnímu "přemýšlení" nad složitějšími dotazy, čímž zlepšuje přesnost v matematice, kódování a úlohách s více kroky, aniž by zpomaloval typické konverzace. Model je ve výchozím nastavení srdečnější a konverzačnější, s lepším dodržováním instrukcí a stabilnějším krátkodobým usuzováním. GPT-5.2 Chat je navržen pro interaktivní pracovní zátěže s vysokou propustností, kde na odezvě a konzistenci záleží více než na hlubokém uvažování.

## Unikátní charakteristiky

GPT-5.2 Chat (Instant) představuje hybridní přístup, který kombinuje rychlou inferenci s dynamicky aktivovaným hlubším uvažováním pro složité úlohy. Model je specificky laděn pro konverzační plynulost a okamžitou odezvu, přičemž obětuje délku kontextového okna ve prospěch rychlosti a stability.

## Silné stránky

### Adaptivní uvažování
Selektivní aktivace 'myšlení' u náročných dotazů (matematika, kódování) zvyšuje přesnost bez plošného zpomalení typického pro plné reasoning modely.

### Instrukční stabilita
Vylepšené dodržování složitých instrukcí a formátování v porovnání s předchozími 'turbo' nebo 'instant' variantami.

## Slabé stránky

### Kontextové okno
Kapacita 128,000 tokenů je výrazně pod průměrem přímé konkurence (Sonnet 4.5 i Gemini 3 Pro nabízejí 1M+), což limituje analýzu velkých dokumentů.

### Poměr cena/výkon
Cena výstupu $14.00/1M je relativně vysoká pro model prezentovaný jako 'lightweight', zejména v porovnání s modely Google Gemini.
