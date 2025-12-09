---
layout: llm_review
title: "Anthropic: Claude Sonnet 4"
date: "2025-05-22 18:12:51"
model_id: anthropic/claude-sonnet-4
slug: anthropic-claude-sonnet-4
provider: Anthropic
pricing:
  prompt_per_m: 3.0
  completion_per_m: 15.0
  blend_per_m: 6.0
context_length: 1,000,000
max_output: 64,000
input_modalities:
  - image
  - text
  - file
output_modalities:
  - text
focus:
  - Programování
  - Rozumování
strengths:
  - area: Programování
    description: Dosahuje špičkového výkonu na SWE-bench (72.7%), což naznačuje silné schopnosti v oblasti kódování.
  - area: Kontextové okno
    description: Disponuje kontextovým oknem 1,000,000 tokenů, což umožňuje zpracování rozsáhlých dokumentů a komplexních úloh.
weaknesses:
  - area: Cena
    description: Vyšší cena ve srovnání s některými konkurenčními modely, což může být limitující pro rozsáhlé nasazení.
  - area: Benchmark data
    description: Chybějící benchmark data v jiných kategoriích než programování znemožňují komplexní hodnocení.
competitors:
  - provider: Anthropic
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: Dražší vstup i výstup
    comparison: Opus by měl být výkonnější, ale dražší. Záleží na prioritách.
  - provider: Google
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Levnější vstup, podobný výstup
    comparison: Gemini Pro nabízí srovnatelný kontext za nižší cenu, ale chybí benchmark data pro přímé srovnání výkonu.
  - provider: OpenAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: Výrazně levnější vstup, levnější výstup
    comparison: GPT-5.1 je levnější, ale má menší kontext. Výkonnostní srovnání vyžaduje benchmarky.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Mnohem levnější vstup i výstup
    comparison: Grok je výrazně levnější, ale má potenciálně nižší kvalitu výstupu. Vhodný pro nenáročné úlohy.
recommendation:
  target_users:
    - Vývojáři softwaru
    - Firmy s potřebou zpracování velkého množství textu
  use_cases:
    - Generování kódu
    - Analýza rozsáhlých dokumentů
    - Automatizace komplexních pracovních postupů
  avoid_for:
    - Úlohy s nízkým rozpočtem
    - Úlohy vyžadující maximální rychlost odezvy
verdict: Claude Sonnet 4 je vhodný pro vývojáře a firmy, které potřebují spolehlivý model pro kódování a rozumování s velkým kontextovým oknem, ale jsou ochotni zaplatit vyšší cenu.
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
  killer_feature: Velké kontextové okno (1M tokenů)
  hidden_risk: Vyšší cena může omezit nasazení v nákladově citlivých projektech
  recommended_use_case: Vývoj softwaru, kde je potřeba pracovat s rozsáhlými kódovými bázemi
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:05"
---

Claude Sonnet 4 významně rozšiřuje schopnosti svého předchůdce, Sonnet 3.7, a vyniká v kódování i úlohách vyžadujících usuzování s vylepšenou přesností a ovladatelností. S dosažením nejmodernějšího výkonu na SWE-bench (72,7 %) vyvažuje Sonnet 4 schopnosti a výpočetní efektivitu, díky čemuž je vhodný pro širokou škálu aplikací od běžných úloh kódování až po komplexní projekty vývoje softwaru. Mezi klíčová vylepšení patří zdokonalená autonomní navigace v kódové základně, snížená chybovost v pracovních postupech řízených agenty a zvýšená spolehlivost při dodržování složitých instrukcí. Sonnet 4 je optimalizován pro praktické každodenní použití a poskytuje pokročilé schopnosti usuzování při zachování efektivity a odezvy v různých interních i externích scénářích.

## Unikátní charakteristiky

Claude Sonnet 4 vylepšuje svého předchůdce Sonnet 3.7, vyniká v kódování a rozumování. Dosahuje špičkového výkonu na SWE-bench (72.7%).

## Silné stránky

### Programování
Dosahuje špičkového výkonu na SWE-bench (72.7%), což naznačuje silné schopnosti v oblasti kódování.

### Kontextové okno
Disponuje kontextovým oknem 1,000,000 tokenů, což umožňuje zpracování rozsáhlých dokumentů a komplexních úloh.

## Slabé stránky

### Cena
Vyšší cena ve srovnání s některými konkurenčními modely, což může být limitující pro rozsáhlé nasazení.

### Benchmark data
Chybějící benchmark data v jiných kategoriích než programování znemožňují komplexní hodnocení.
