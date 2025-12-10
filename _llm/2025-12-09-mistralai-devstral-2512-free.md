---
layout: llm_review
title: "Mistral: Devstral 2 2512 (free)"
date: "2025-12-09 14:03:39"
model_id: "mistralai/devstral-2512:free"
slug: mistralai-devstral-2512-free
provider: Mistralai
pricing:
  prompt_per_m: 0.0
  completion_per_m: 0.0
context_length: 262,144
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Agentní programování
  - Orchestrace změn ve více souborech
  - Modernizace legacy systémů
competitors:
  - provider: OpenAI
    model: GPT-5.1 Codex Max
    model_id: openai/gpt-5.1-codex-max
    price_comparison: Devstral je zdarma, zatímco GPT-5.1 stojí $1.25/$10.00 za 1M tokenů
    comparison: GPT-5.1 Codex Max nabízí větší kontext (400k) a pravděpodobně vyšší obecnou inteligenci, ale Devstral 2 nabízí srovnatelnou specializaci na kód s nulovými provozními náklady.
  - provider: X-AI
    model: Grok Code Fast 1
    model_id: x-ai/grok-code-fast-1
    price_comparison: Devstral je zdarma, Grok stojí $0.20/$1.50
    comparison: Grok má identický kontext (256k) a je zaměřen na rychlost. Devstral (123B dense) bude pravděpodobně pomalejší, ale důkladnější v komplexním uvažování nad architekturou.
  - provider: DeepSeek
    model: DeepSeek v3.2 Speciale
    model_id: deepseek/deepseek-v3.2-speciale
    price_comparison: Devstral je zdarma, DeepSeek stojí $0.27/$0.41
    comparison: Devstral nabízí výrazně větší kontextové okno (256k vs 164k) a je specificky laděn na agentní chování, zatímco DeepSeek je spíše obecný model.
recommendation:
  target_users:
    - Softwaroví inženýři
    - DevOps týmy
    - Enterprise architekti
  use_cases:
    - Automatizovaný refactoring legacy kódu
    - Hromadné opravy chyb napříč repozitářem
    - Generování unit testů s kontextem celého projektu
  avoid_for:
    - Úlohy vyžadující vizuální vstupy (obrázky)
    - Aplikace vyžadující extrémně nízkou latenci (real-time chat)
verdict: Ideální volba pro vývojáře a firmy hledající výkonný open-source model pro náročné kódovací úlohy bez provozních nákladů na tokeny, pokud není vyžadována analýza obrazu.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2025-12-10 07:24"
---

Devstral 2 je nejmodernější open-source model od Mistral AI specializující se na agentické kódování. Jedná se o hustý transformátorový model se 123 miliardami parametrů, který podporuje kontextové okno o velikosti 256 tisíc tokenů.

Devstral 2 podporuje prozkoumávání kódových základen a orchestraci změn napříč více soubory při zachování kontextu na úrovni architektury. Sleduje závislosti frameworků, detekuje selhání a opakuje pokusy s opravami – řeší výzvy, jako je oprava chyb a modernizace starších systémů. Model lze doladit tak, aby upřednostňoval specifické jazyky nebo optimalizoval pro rozsáhlé podnikové kódové základy. Je k dispozici pod modifikovanou licencí MIT.

## Unikátní charakteristiky

Devstral 2 je masivní 123B dense model optimalizovaný specificky pro softwarové inženýrství a agentní pracovní toky. Vyniká schopností udržovat kontext architektury napříč mnoha soubory a autonomně opravovat chyby pomocí iterativního přístupu.

## Silné stránky

### Nákladová efektivita
S cenou $0.00 za vstup i výstup poskytuje bezkonkurenční poměr cena/výkon pro náročné dávkové zpracování kódu.

### Agentní schopnosti
Nativní podpora pro detekci selhání a automatické opakování (retries) umožňuje řešit komplexní refactoring, který by u běžných modelů vyžadoval externí smyčky.

### Specializace na kód
Model je vyladěn pro práci se závislostmi frameworků a modernizaci starších kódových bází, což přesahuje schopnosti obecných chatovacích modelů.

## Slabé stránky

### Multimodalita
Podporuje pouze text-to-text, chybí schopnost analyzovat diagramy architektury nebo UI screenshoty (na rozdíl od Gemini nebo Claude).

### Velikost kontextu
Okno 256k tokenů je sice robustní, ale zaostává za modely jako Gemini 3 Pro (1M+) nebo GPT-5.1 (400k) pro analýzu extrémně rozsáhlých monolitů.
