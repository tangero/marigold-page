---
layout: llm_review
title: "Mistral: Ministral 3 8B 2512"
date: "2025-12-02 14:20:54"
model_id: mistralai/ministral-8b-2512
slug: mistralai-ministral-8b-2512
provider: Mistral
pricing:
  prompt_per_m: 0.15
  completion_per_m: 0.15
  blend_per_m: 0.15
context_length: 262,144
max_output: N/A
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Obecná inteligence
  - Multimodalita
strengths:
  - area: Věda a matematika
    description: Dosahuje průměrných výsledků v testech zaměřených na vědu a matematiku, například GPQA Diamond (47.1%) a AIME (31.7%).
  - area: Rychlost
    description: Vyniká rychlostí zpracování, s TPS 197.6 a TTFT 0.291s, což z něj činí vhodnou volbu pro aplikace vyžadující rychlou odezvu.
weaknesses:
  - area: Programování
    description: Dosahuje slabých výsledků v programovacích benchmarcích, jako je LiveCodeBench (30.3%).
  - area: Logické uvažování
    description: Slabé výsledky v testech tvrdé logiky (HLE 4.3%, terminalbench_hard 4.3%) naznačují omezené schopnosti v komplexním logickém uvažování.
competitors:
  - provider: MISTRALAI
    model: mistralai/ministral-3b-2512
    model_id: mistralai/ministral-3b-2512
    price_comparison: Levnější
    comparison: Levnější varianta, ale s menšími schopnostmi a polovičním kontextem.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Dražší
    comparison: Dražší, ale pravděpodobně s lepšími schopnostmi v náročnějších úlohách.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Podobná cena
    comparison: Srovnatelná cena, ale menší kontextové okno. Nabízí multimodální vstupy.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Mírně dražší
    comparison: Větší kontextové okno, ale data o výkonu nejsou k dispozici.
recommendation:
  target_users:
    - Výzkumníci
    - Vývojáři prototypů
  use_cases:
    - Rychlé prototypování
    - Zpracování obrazového vstupu
    - Vědecké výpočty
  avoid_for:
    - Složité programovací úlohy
    - Aplikace vyžadující silné logické uvažování
verdict: Ministral 3 8B je vhodný pro uživatele, kteří hledají rychlý a multimodální model pro prototypování a experimentování, ale měli by zvážit jeho omezení v programování a logickém uvažování.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 47.1
    tier: Průměrný
  coding:
    name: Programování
    icon: 💻
    score: 30.3
    tier: Slabý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 26.6
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 41.7
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 84.9
    tier: Výborný
overall_score: 41.8
overall_tier: Průměrný
radar:
  logic_code: 38.7
  agentic: 26.6
  languages: 0
  safety: 0
  speed: Výborný
expert_verdict:
  killer_feature: Multimodální vstup a velký kontext za rozumnou cenu.
  hidden_risk: Slabší výkon v programování a logickém uvažování může omezit použitelnost v některých aplikacích.
  recommended_use_case: Rychlé prototypování aplikací, které kombinují textový a obrazový vstup.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:20"
---

Vyvážený model v rodině Ministral 3, Ministral 3 8B je výkonný, efektivní malý jazykový model s vizuálními schopnostmi.

## Unikátní charakteristiky

Ministral 3 8B je vyvážený model s multimodálními schopnostmi a velkým kontextovým oknem. Jeho silné stránky leží v oblasti vědy a matematiky, kde dosahuje průměrných výsledků. Rychlost zpracování je výborná.

## Silné stránky

### Věda a matematika
Dosahuje průměrných výsledků v testech zaměřených na vědu a matematiku, například GPQA Diamond (47.1%) a AIME (31.7%).

### Rychlost
Vyniká rychlostí zpracování, s TPS 197.6 a TTFT 0.291s, což z něj činí vhodnou volbu pro aplikace vyžadující rychlou odezvu.

## Slabé stránky

### Programování
Dosahuje slabých výsledků v programovacích benchmarcích, jako je LiveCodeBench (30.3%).

### Logické uvažování
Slabé výsledky v testech tvrdé logiky (HLE 4.3%, terminalbench_hard 4.3%) naznačují omezené schopnosti v komplexním logickém uvažování.
