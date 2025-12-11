---
layout: llm_review
title: "Mistral: Devstral 2 2512"
date: "2025-12-09 14:03:39"
model_id: mistralai/devstral-2512
slug: mistralai-devstral-2512
provider: Mistral
pricing:
  prompt_per_m: 0.15
  completion_per_m: 0.6
  blend_per_m: 0.2625
context_length: 262,144
max_output: 65,536
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Agentic coding
  - Generování kódu
strengths:
  - area: Kontextové okno
    description: Podporuje kontextové okno 262,144 tokenů, což umožňuje práci s rozsáhlými kódovými bázemi.
  - area: Specializace na kód
    description: Navržen pro agentic coding, bug fixing a modernizaci legacy systémů.
weaknesses:
  - area: Benchmark data
    description: Chybějící benchmark data znemožňují objektivní srovnání s konkurencí.
  - area: Cena
    description: Cena je vyšší než u některých konkurenčních modelů, ale je nutné zvážit specializaci a kontextové okno.
competitors:
  - provider: X-AI
    model: grok-code-fast-1
    model_id: x-ai/grok-code-fast-1
    price_comparison: Vstup 1.3x levnější, výstup 2.5x levnější
    comparison: Grok-code-fast-1 je levnější, ale Devstral 2 má potenciálně lepší schopnosti v agentic codingu (data nejsou k dispozici).
  - provider: DEEPSEEK
    model: deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Vstup podobný, výstup levnější
    comparison: Deepseek-v3.2 je cenově srovnatelný, ale má menší kontextové okno (163,840 tokenů).
  - provider: MISTRALAI
    model: ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Vstup 25% dražší, výstup 66% levnější
    comparison: Ministral-14b-2512 je levnější, ale Devstral 2 je specializovaný na agentic coding.
  - provider: OPENAI
    model: gpt-5.1-codex-max
    model_id: openai/gpt-5.1-codex-max
    price_comparison: Vstup 8.3x dražší, výstup 16.6x dražší
    comparison: GPT-5.1-codex-max je dražší, ale může mít lepší benchmark skóre (data pro Devstral 2 nejsou k dispozici).
recommendation:
  target_users:
    - Vývojáři
    - Firmy modernizující legacy systémy
  use_cases:
    - Agentic coding
    - Automatické opravy chyb
    - Analýza a úpravy rozsáhlých kódových bází
  avoid_for:
    - Generování textu v češtině
    - Aplikace vyžadující nízkou latenci
verdict: Devstral 2 je zajímavý model pro specifické use case zaměřené na agentic coding, ale je nutné zvážit vyšší cenu a chybějící benchmark data.
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
  killer_feature: Velké kontextové okno pro práci s rozsáhlými kódovými bázemi.
  hidden_risk: Chybějící benchmark data znemožňují objektivní posouzení výkonu a kvality generovaného kódu.
  recommended_use_case: Automatická refaktorizace a modernizace rozsáhlých legacy systémů.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-11 09:25"
---

Devstral 2 je nejmodernější open-source model od Mistral AI specializující se na agentní kódování. Jedná se o hustý transformátorový model se 123 miliardami parametrů, který podporuje kontextové okno o velikosti 256K.

Devstral 2 podporuje prozkoumávání kódových základen a orchestraci změn napříč více soubory při zachování kontextu na úrovni architektury. Sleduje závislosti frameworků, detekuje selhání a opakuje pokusy s opravami – řeší výzvy jako opravy chyb a modernizace starších systémů. Model lze doladit pro upřednostnění specifických jazyků nebo optimalizovat pro rozsáhlé podnikové kódové základy. Je k dispozici pod modifikovanou licencí MIT.

## Unikátní charakteristiky

Devstral 2 je open-source model specializovaný na agentic coding s velkým kontextovým oknem 256K tokenů. Benchmark data nejsou k dispozici, takže nelze objektivně posoudit jeho výkon v porovnání s konkurencí.

## Silné stránky

### Kontextové okno
Podporuje kontextové okno 262,144 tokenů, což umožňuje práci s rozsáhlými kódovými bázemi.

### Specializace na kód
Navržen pro agentic coding, bug fixing a modernizaci legacy systémů.

## Slabé stránky

### Benchmark data
Chybějící benchmark data znemožňují objektivní srovnání s konkurencí.

### Cena
Cena je vyšší než u některých konkurenčních modelů, ale je nutné zvážit specializaci a kontextové okno.
