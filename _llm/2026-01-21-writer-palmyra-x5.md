---
layout: llm_review
title: "Writer: Palmyra X5"
date: "2026-01-21 14:57:03"
model_id: writer/palmyra-x5
slug: writer-palmyra-x5
provider: Writer
pricing:
  prompt_per_m: 0.6
  completion_per_m: 6.0
context_length: 1,040,000
max_output: 8,192
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Enterprise AI Agenti
  - Zpracování dlouhého kontextu
  - RAG systémy
competitors:
  - provider: GOOGLE
    model: Gemini 3 Flash Preview
    model_id: google/gemini-3-flash-preview
    price_comparison: Vstup o 17 % levnější, výstup o 50 % levnější
    comparison: Gemini nabízí stejný kontext (1M) za nižší cenu a přidává multimodalitu, Palmyra kontruje specializací na enterprise agenty.
  - provider: ANTHROPIC
    model: Claude Haiku 4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: Vstup dražší ($1.00 vs $0.60), výstup levnější ($5.00 vs $6.00)
    comparison: Haiku má výrazně menší kontext (200k vs 1M), ale konkuruje silnou schopností logického usuzování v enterprise segmentu.
  - provider: X-AI
    model: Grok 4.1 Fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Výrazně levnější (3x levnější vstup, 12x levnější výstup)
    comparison: Grok nabízí dvojnásobný kontext (2M) a nižší cenu, což z něj činí silného konkurenta pro hrubé zpracování dat, ačkoliv Palmyra cílí více na korporátní integrace.
recommendation:
  target_users:
    - Vývojáři podnikových AI agentů
    - Firmy zpracovávající velké textové datasety
    - Týmy vyžadující privátní/enterprise řešení
  use_cases:
    - RAG nad rozsáhlou firemní dokumentací
    - Analýza dlouhých finančních či právních zpráv
    - Orchestrace komplexních agentních workflow
  avoid_for:
    - Úlohy vyžadující analýzu obrázků či audia
    - Generování velkého objemu textu s nízkým rozpočtem (kvůli ceně výstupu)
verdict: Palmyra X5 je robustní volba pro podniky vyžadující spolehlivé zpracování dlouhého kontextu v textové doméně, ačkoliv cenově vychází hůře než agresivní konkurence od Google a xAI.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2026-01-22 07:26"
---

Palmyra X5 je nejpokročilejší model od Writeru, účelově vytvořený pro budování a škálování AI agentů v rámci celého podniku. Poskytuje špičkovou rychlost a efektivitu v kontextových oknech až do 1 milionu tokenů, poháněný novou architekturou transformátoru a hybridními mechanismy pozornosti. To umožňuje rychlejší inferenci a rozšířenou paměť pro zpracování velkých objemů podnikových dat, což je klíčové pro škálování AI agentů.

## Unikátní charakteristiky

Palmyra X5 se vyznačuje specializovanou architekturou s hybridní pozorností, která je optimalizována pro efektivní zpracování kontextového okna o velikosti přes 1 milion tokenů. Model je navržen primárně pro podnikové prostředí s důrazem na rychlou inferenci a škálování autonomních agentů.

## Silné stránky

### Kapacita kontextu
Kontextové okno 1 040 000 tokenů umožňuje zpracování celých knihoven dokumentů nebo rozsáhlých kódových bází v jednom promptu, což je srovnatelné s vlajkovými modely Google a Anthropic.

### Architektonická efektivita
Díky hybridním mechanismům pozornosti dosahuje model vyšší rychlosti inference a lepší správy paměti při práci s velkými objemy dat než standardní transformery.

## Slabé stránky

### Cena výstupu
Cena $6.00 za 1M výstupních tokenů je relativně vysoká; například Google Gemini 3 Flash stojí polovinu ($3.00) a x-ai Grok je řádově levnější.

### Omezení modalit
Model je omezen pouze na zpracování textu (text-to-text), zatímco přímí konkurenti v této třídě (Gemini, GPT) často nabízejí multimodální schopnosti.
