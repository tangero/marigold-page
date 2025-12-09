---
layout: llm_review
title: "Meta: Llama 4 Scout"
date: "2025-04-05 21:31:59"
model_id: meta-llama/llama-4-scout
slug: meta-llama-llama-4-scout
provider: Meta
pricing:
  prompt_per_m: 0.08
  completion_per_m: 0.3
  blend_per_m: 0.135
context_length: 327,680
max_output: 16,384
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Multimodální asistent
  - Vizuální uvažování
strengths:
  - area: Kontext
    description: Velký kontext 327 680 tokenů umožňuje zpracování rozsáhlých dokumentů a komplexních úloh.
  - area: Multimodalita
    description: Podporuje nativní multimodální vstup (text a obraz), což rozšiřuje možnosti využití.
weaknesses:
  - area: Programování
    description: S nízkým skóre 29.9 na LiveCodeBench je model slabý v programovacích úlohách.
  - area: Čeština
    description: Data pro češtinu nejsou k dispozici, což omezuje jeho použitelnost v českém prostředí.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-sonnet-4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: 21x dražší vstup, 50x dražší výstup
    comparison: Claude Sonnet 4.5 má větší kontext (1M tokenů) a pravděpodobně lepší schopnosti, ale je výrazně dražší.
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: 14x dražší vstup, 40x dražší výstup
    comparison: Gemini 3 Pro Image Preview nabízí multimodální schopnosti, ale s menším kontextem a vyšší cenou.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 1.4x dražší vstup, 1.6x dražší výstup
    comparison: Grok-4.1-fast má větší kontext (2M tokenů) a je rychlejší, ale nemusí mít tak dobré multimodální schopnosti.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: 1.4x dražší vstup, 0.6x levnější výstup
    comparison: Ministral-14b-2512 je levnější na výstup, ale má menší kontext a chybí mu multimodalita.
recommendation:
  target_users:
    - Výzkumníci v oblasti AI
    - Firmy hledající efektivní multimodální řešení
  use_cases:
    - Zpracování obrazových dat s textovým popisem
    - Asistent pro vizuální uvažování
  avoid_for:
    - Úkoly vyžadující pokročilé programování
    - Aplikace vyžadující nativní podporu češtiny
verdict: Llama 4 Scout je vhodný pro uživatele, kteří potřebují efektivní multimodální model s velkým kontextem, ale nemají vysoké nároky na programování nebo češtinu.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 51.7
    tier: Průměrný
  coding:
    name: Programování
    icon: 💻
    score: 29.9
    tier: Slabý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 15.5
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 48.6
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 55.0
    tier: Průměrný
overall_score: 38.5
overall_tier: Slabý
radar:
  logic_code: 40.8
  agentic: 15.5
  languages: 0
  safety: 0
  speed: Průměrný
expert_verdict:
  killer_feature: Nativní multimodalita s velkým kontextem
  hidden_risk: Slabé výsledky v programování a neznámá výkonnost v češtině
  recommended_use_case: Analýza obrazových dat s textovým kontextem, například pro automatické generování popisků.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:01"
---

Llama 4 Scout 17B Instruct (16E) je jazykový model typu mixture-of-experts (MoE) vyvinutý společností Meta, který aktivuje 17 miliard parametrů z celkového počtu 109 miliard. Podporuje nativní multimodální vstup (text a obrázek) a multijazyčný výstup (text a kód) ve 12 podporovaných jazycích. Scout, navržený pro interakci ve stylu asistenta a vizuální usuzování, používá 16 expertů na jeden forward pass a disponuje kontextovou délkou 10 milionů tokenů, s trénovacím korpusem o velikosti ~40 bilionů tokenů.

Llama 4 Scout, vytvořený pro vysokou efektivitu a lokální nebo komerční nasazení, zahrnuje early fusion pro bezproblémovou integraci modalit. Je instruction-tuned pro použití v multijazyčném chatu, vytváření titulků a úlohách porozumění obrázkům. Byl vydán pod licencí Llama 4 Community License, naposledy trénován na datech do srpna 2024 a veřejně spuštěn 5. dubna 2025.

## Unikátní charakteristiky

Llama 4 Scout je navržen pro vysokou efektivitu a lokální nasazení, integruje multimodální vstupy pomocí early fusion a je optimalizován pro interakci ve stylu asistenta. Využívá 16 expertů na průchod a má kontextovou délku 327 680 tokenů.

## Silné stránky

### Kontext
Velký kontext 327 680 tokenů umožňuje zpracování rozsáhlých dokumentů a komplexních úloh.

### Multimodalita
Podporuje nativní multimodální vstup (text a obraz), což rozšiřuje možnosti využití.

## Slabé stránky

### Programování
S nízkým skóre 29.9 na LiveCodeBench je model slabý v programovacích úlohách.

### Čeština
Data pro češtinu nejsou k dispozici, což omezuje jeho použitelnost v českém prostředí.
