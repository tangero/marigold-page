---
layout: llm_review
title: "OpenAI: GPT Audio"
date: "2026-01-19 23:42:49"
model_id: openai/gpt-audio
slug: openai-gpt-audio
provider: Openai
pricing:
  prompt_per_m: 2.5
  completion_per_m: 10.0
context_length: 128,000
max_output: 16,384
input_modalities:
  - text
  - audio
output_modalities:
  - text
  - audio
focus:
  - Nativní zpracování řeči
  - Hlasová interakce v reálném čase
  - Multimodální generování
competitors:
  - provider: OpenAI
    model: GPT Audio Mini
    model_id: openai/gpt-audio-mini
    price_comparison: Textový vstup je cca 4x levnější ($0.60 vs $2.50)
    comparison: Ekonomičtější varianta pro aplikace, kde není vyžadována maximální nuance v hlasovém projevu nebo komplexní uvažování.
  - provider: Google
    model: Gemini 3 Pro Preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Mírně levnější vstup ($2.00), dražší výstup ($12.00)
    comparison: Hlavní konkurent v multimodalitě. Gemini nabízí 8x větší kontextové okno (1M), což je výhodnější pro analýzu dlouhých záznamů.
  - provider: Anthropic
    model: Claude Sonnet 4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: Dražší textové zpracování ($3.00/$15.00)
    comparison: Claude dominuje v textovém uvažování a má větší kontext (1M), ale postrádá nativní audio výstup, což vyžaduje externí TTS řešení.
recommendation:
  target_users:
    - Vývojáři hlasových asistentů
    - Platformy pro výuku jazyků
    - Zákaznická podpora s důrazem na empatii
  use_cases:
    - Konverzační agenti s nízkou latencí
    - Překlad řeči v reálném čase se zachováním intonace
  avoid_for:
    - Analýzu rozsáhlých textových archivů (kvůli kontextu)
    - Dávkové zpracování audia s nízkým rozpočtem
verdict: Ideální volba pro aplikace vyžadující vysoce kvalitní, přirozenou hlasovou interakci, kde vyšší cena za audio tokeny vyvažuje absenci složitého STT/TTS pipeline.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2026-01-20 07:28"
---

Model gpt-audio je prvním obecně dostupným audio modelem od OpenAI. Nový snapshot obsahuje vylepšený dekodér pro přirozeněji znějící hlasy a zachovává lepší konzistenci hlasu. Cena audia je 32 USD za milion vstupních tokenů a 64 USD za milion výstupních tokenů.

## Unikátní charakteristiky

Model gpt-audio představuje první obecně dostupný model OpenAI specializovaný na přímý vstup a výstup audia bez nutnosti externích převodníků (STT/TTS). Vyznačuje se vylepšeným dekodérem pro zachování konzistence hlasu a oddělenou cenovou politikou pro textové a audio tokeny.

## Silné stránky

### Nativní audio modality
Schopnost zpracovávat audio přímo (audio-in/audio-out) umožňuje zachovat neverbální informace (tón, intonace) a snižuje latenci oproti kaskádovým systémům.

### Kvalita syntézy
Nový snapshot modelu obsahuje vylepšený dekodér, který zajišťuje přirozenější projev a vyšší konzistenci hlasu během delších interakcí.

## Slabé stránky

### Cena audio zpracování
Cena za audio tokeny ($32/$64 za 1M) je řádově vyšší než za textové zpracování, což prodražuje aplikace s vysokým objemem hlasových dat.

### Kontextové okno
Kapacita 128,000 tokenů je v prosinci 2025 podprůměrná ve srovnání s konkurencí (Google, X-AI), která běžně nabízí 1M až 2M tokenů.
