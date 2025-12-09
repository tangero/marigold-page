---
layout: llm_review
title: "Mistral: Voxtral Small 24B 2507"
date: "2025-10-30 15:39:04"
model_id: mistralai/voxtral-small-24b-2507
slug: mistralai-voxtral-small-24b-2507
provider: Mistral
pricing:
  prompt_per_m: 0.1
  completion_per_m: 0.3
  blend_per_m: 0.15
context_length: 32,000
max_output: N/A
input_modalities:
  - text
  - audio
output_modalities:
  - text
focus:
  - Přepis audia
  - Porozumění audiu
  - Překlad audia
strengths:
  - area: Audio vstup
    description: Vyniká v přepisu řeči, překladu a porozumění audiu.
  - area: Cena
    description: Relativně nízká cena za vstup textu a audia v porovnání s modely s podobnými schopnostmi.
weaknesses:
  - area: Benchmark data
    description: Chybí benchmark data pro objektivní srovnání s konkurencí v textových úlohách.
  - area: Čeština
    description: MMMLU skóre pro češtinu není známo, což ztěžuje posouzení kvality pro lokální nasazení.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: 50x dražší vstup, 83x dražší výstup
    comparison: Claude Opus je pravděpodobně výkonnější v textových úlohách, ale výrazně dražší.
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: 10x dražší vstup, 17x dražší výstup
    comparison: Claude Haiku může být rychlejší, ale Voxtral Small nabízí lepší poměr cena/výkon pro audio úlohy.
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: 20x dražší vstup, 40x dražší výstup
    comparison: Gemini Pro Image Preview má multimodální schopnosti (obraz), ale je dražší.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: 2x dražší vstup, 0.6x levnější výstup
    comparison: Ministral 14B má větší kontext a může být vhodnější pro delší textové úlohy, ale nemá audio vstup.
recommendation:
  target_users:
    - Vývojáři audio aplikací
    - Překladatelé
    - Transkripční služby
  use_cases:
    - Automatický přepis podcastů
    - Překlad audio nahrávek
    - Hlasové ovládání aplikací
  avoid_for:
    - Úlohy vyžadující špičkový výkon v logickém uvažování
    - Aplikace s vysokými nároky na bezpečnost
verdict: Voxtral Small je dobrá volba pro vývojáře, kteří potřebují audio vstup a zpracování za rozumnou cenu, ale měli by si ověřit jeho výkon v češtině a textových úlohách.
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
  killer_feature: Audio vstup a zpracování za rozumnou cenu
  hidden_risk: Nejasný výkon v češtině a textových úlohách bez benchmarků
  recommended_use_case: Automatický přepis a překlad audio obsahu
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:16"
---

Voxtral Small je vylepšení modelu Mistral Small 3, které zahrnuje nejmodernější možnosti audio vstupu při zachování špičkového textového výkonu. Vyniká v přepisu řeči, překladu a porozumění audiu. Vstupní audio je zpoplatněno sazbou 100 USD za milion sekund.

## Unikátní charakteristiky

Voxtral Small 24B 2507 je vylepšená verze Mistral Small 3, která přidává pokročilé možnosti audio vstupu při zachování špičkového výkonu v textu. Specializuje se na přepis řeči, překlad a porozumění audiu. Benchmark data nejsou k dispozici.

## Silné stránky

### Audio vstup
Vyniká v přepisu řeči, překladu a porozumění audiu.

### Cena
Relativně nízká cena za vstup textu a audia v porovnání s modely s podobnými schopnostmi.

## Slabé stránky

### Benchmark data
Chybí benchmark data pro objektivní srovnání s konkurencí v textových úlohách.

### Čeština
MMMLU skóre pro češtinu není známo, což ztěžuje posouzení kvality pro lokální nasazení.
