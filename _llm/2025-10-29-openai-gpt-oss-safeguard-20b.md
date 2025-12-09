---
layout: llm_review
title: "OpenAI: gpt-oss-safeguard-20b"
date: "2025-10-29 16:47:16"
model_id: openai/gpt-oss-safeguard-20b
slug: openai-gpt-oss-safeguard-20b
provider: Openai
pricing:
  prompt_per_m: 0.075
  completion_per_m: 0.3
  blend_per_m: 0.1312
context_length: 131,072
max_output: 65,536
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Bezpečnost
  - Filtrování obsahu
strengths:
  - area: Cena
    description: Relativně nízká cena v porovnání s modely jako Claude Opus nebo GPT-5.1, což může být atraktivní pro rozsáhlé bezpečnostní aplikace.
  - area: Kontext
    description: Kontext 131,072 tokenů umožňuje zpracování delších textů pro bezpečnostní analýzu.
weaknesses:
  - area: Benchmarky
    description: Absence benchmark dat znemožňuje objektivní srovnání s konkurencí v oblasti bezpečnosti a výkonu.
  - area: Jazyková podpora
    description: Není známa kvalita v češtině (MMMLU), což je kritické pro nasazení v lokálním prostředí.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: Výrazně dražší (vstup 71x, výstup 83x)
    comparison: Claude Opus pravděpodobně nabízí vyšší kvalitu, ale za podstatně vyšší cenu. Vhodné pro aplikace, kde je kvalita prioritou.
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: Dražší (vstup 28x, výstup 40x)
    comparison: Gemini Pro nabízí multimodální vstupy, ale je dražší. Vhodné pokud potřebujete zpracovávat i obrázky.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Mnohem levnější (vstup 2.8x, výstup 1.6x)
    comparison: Grok je levnější a má větší kontext, ale nemusí dosahovat stejné kvality v bezpečnostních úlohách.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Levnější (vstup 2.8x, výstup 0.6x)
    comparison: Ministral 14B je levnější, ale jeho výkon v bezpečnostních úlohách je neznámý.
recommendation:
  target_users:
    - Vývojáři bezpečnostních aplikací
    - Firmy filtrující obsah
  use_cases:
    - Filtrování nevhodného obsahu
    - Detekce toxického textu
  avoid_for:
    - Generování kreativního obsahu
    - Úlohy vyžadující vysokou přesnost v logickém uvažování
verdict: gpt-oss-safeguard-20b je zajímavá volba pro uživatele, kteří hledají cenově dostupný model pro bezpečnostní úlohy. Absence benchmark dat ale vyžaduje opatrnost a vlastní testování.
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
  killer_feature: Nízká cena pro bezpečnostní úlohy
  hidden_risk: Nedostatek benchmark dat pro objektivní srovnání
  recommended_use_case: Automatické filtrování komentářů na sociálních sítích
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:16"
---

gpt-oss-safeguard-20b je model pro odůvodňování bezpečnosti od OpenAI, postavený na modelu gpt-oss-20b. Tento model s otevřenými váhami, 21 miliardami parametrů a architekturou Mixture-of-Experts (MoE) nabízí nižší latenci pro bezpečnostní úlohy, jako je klasifikace obsahu, filtrování LLM a označování pro důvěru a bezpečnost.

Více informací o tomto modelu naleznete v [uživatelské příručce](https://cookbook.openai.com/articles/gpt-oss-safeguard-guide) OpenAI gpt-oss-safeguard.

## Unikátní charakteristiky

gpt-oss-safeguard-20b je model zaměřený na bezpečnostní úlohy, postavený na architektuře Mixture-of-Experts. Absence benchmark dat znemožňuje přesnější charakteristiku jeho výkonu v porovnání s konkurencí.

## Silné stránky

### Cena
Relativně nízká cena v porovnání s modely jako Claude Opus nebo GPT-5.1, což může být atraktivní pro rozsáhlé bezpečnostní aplikace.

### Kontext
Kontext 131,072 tokenů umožňuje zpracování delších textů pro bezpečnostní analýzu.

## Slabé stránky

### Benchmarky
Absence benchmark dat znemožňuje objektivní srovnání s konkurencí v oblasti bezpečnosti a výkonu.

### Jazyková podpora
Není známa kvalita v češtině (MMMLU), což je kritické pro nasazení v lokálním prostředí.
