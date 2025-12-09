---
layout: llm_review
title: "Mistral: Mistral Medium 3"
date: "2025-05-07 16:15:41"
model_id: mistralai/mistral-medium-3
slug: mistralai-mistral-medium-3
provider: Mistral
pricing:
  prompt_per_m: 0.4
  completion_per_m: 2.0
  blend_per_m: 0.8
context_length: 131,072
max_output: N/A
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Kódování
  - STEM reasoning
strengths:
  - area: Věda a matematika
    description: Vysoké skóre v matematických úlohách, zejména MATH-500 (90.7%) a GPQA Diamond (57.8%), naznačuje silné schopnosti v STEM oblastech.
  - area: Cena a výkon
    description: Nabízí konkurenceschopný výkon za nižší cenu ve srovnání s většími modely, což z něj činí atraktivní volbu pro nasazení ve velkém měřítku.
weaknesses:
  - area: Logické uvažování
    description: Slabé výsledky v HLE (4.3%) a terminalbench_hard (3.5%) naznačují omezené schopnosti v oblasti hard logic.
  - area: Čeština
    description: MMMLU skóre pro češtinu není k dispozici, takže nelze posoudit kvalitu modelu v tomto jazyce.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-sonnet-4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: 3.75x dražší vstup, 7.5x dražší výstup
    comparison: Claude Sonnet 4.5 má větší kontext (1,000,000 tokenů) a může být lepší v komplexnějších úlohách, ale je výrazně dražší.
  - provider: GOOGLE
    model: google/gemini-3-pro-image-preview
    model_id: google/gemini-3-pro-image-preview
    price_comparison: 5x dražší výstup
    comparison: Gemini 3 Pro Image Preview nabízí multimodální schopnosti, ale s menším kontextem (65,536 tokenů) a vyšší cenou za výstup.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 2x levnější vstup, 4x levnější výstup
    comparison: Grok-4.1-fast je levnější a má větší kontext (2,000,000 tokenů), ale jeho výkon v benchmarkách není znám.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: 2x levnější vstup i výstup
    comparison: Ministral-14b-2512 je levnější, ale jeho výkon v benchmarkách není k dispozici.
recommendation:
  target_users:
    - Výzkumníci
    - Podniky s omezeným rozpočtem
    - Vývojáři aplikací
  use_cases:
    - Matematické modelování
    - Analýza dat
    - Generování kódu
  avoid_for:
    - Úlohy vyžadující silné logické uvažování
    - Aplikace s vysokými nároky na češtinu
verdict: Mistral Medium 3 je vhodný pro uživatele, kteří hledají cenově dostupný model s dobrým výkonem v oblasti vědy a matematiky, ale měli by zvážit jeho omezení v logickém uvažování.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 58.9
    tier: Průměrný
  coding:
    name: Programování
    icon: 💻
    score: 40.0
    tier: Průměrný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 24.3
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 49.1
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 50.3
    tier: Průměrný
overall_score: 43.5
overall_tier: Průměrný
radar:
  logic_code: 49.5
  agentic: 24.3
  languages: 0
  safety: 0
  speed: Průměrný
expert_verdict:
  killer_feature: Vynikající poměr cena/výkon pro vědecké a matematické úlohy.
  hidden_risk: Slabé logické uvažování může omezit použitelnost v komplexních úlohách.
  recommended_use_case: Generování a validace matematických modelů.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:04"
---

Mistral Medium 3 je vysoce výkonný jazykový model podnikové třídy navržený tak, aby poskytoval možnosti na špičkové úrovni při výrazně snížených provozních nákladech. Vyvažuje nejmodernější usuzování a multimodální výkon s 8× nižšími náklady ve srovnání s tradičními velkými modely, díky čemuž je vhodný pro škálovatelná nasazení v profesionálních a průmyslových případech použití.

Model vyniká v oblastech, jako je kódování, STEM usuzování a podniková adaptace. Podporuje hybridní, on-prem a in-VPC nasazení a je optimalizován pro integraci do vlastních pracovních postupů. Mistral Medium 3 nabízí konkurenceschopnou přesnost ve srovnání s většími modely, jako jsou Claude Sonnet 3.5/3.7, Llama 4 Maverick a Command R+, přičemž si zachovává širokou kompatibilitu napříč cloudovými prostředími.

## Unikátní charakteristiky

Mistral Medium 3 se zaměřuje na vyvážení výkonu a ceny, nabízí multimodální schopnosti (text, image → text) a velký kontext 131 072 tokenů. Vyniká ve vědeckých a matematických úlohách, což dokazuje vysoké skóre v MATH-500 (90.7%) a GPQA Diamond (57.8%).

## Silné stránky

### Věda a matematika
Vysoké skóre v matematických úlohách, zejména MATH-500 (90.7%) a GPQA Diamond (57.8%), naznačuje silné schopnosti v STEM oblastech.

### Cena a výkon
Nabízí konkurenceschopný výkon za nižší cenu ve srovnání s většími modely, což z něj činí atraktivní volbu pro nasazení ve velkém měřítku.

## Slabé stránky

### Logické uvažování
Slabé výsledky v HLE (4.3%) a terminalbench_hard (3.5%) naznačují omezené schopnosti v oblasti hard logic.

### Čeština
MMMLU skóre pro češtinu není k dispozici, takže nelze posoudit kvalitu modelu v tomto jazyce.
