---
layout: llm_review
title: "xAI: Grok Code Fast 1"
date: "2025-08-26 22:08:47"
model_id: x-ai/grok-code-fast-1
slug: x-ai-grok-code-fast-1
provider: xAI
pricing:
  prompt_per_m: 0.2
  completion_per_m: 1.5
  blend_per_m: 0.525
context_length: 256,000
max_output: 10,000
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Programování
  - Agenti
strengths:
  - area: Agentní schopnosti
    description: Vysoké skóre v τ2-Bench (75.7%) naznačuje silné schopnosti pro agentní aplikace a automatizaci úloh.
  - area: Programování
    description: Solidní skóre v LiveCodeBench (65.7%) ukazuje dobrou úroveň programovacích dovedností.
weaknesses:
  - area: Logické uvažování
    description: Nízké skóre v HLE (7.5%) a terminalbench_hard (16.3%) naznačuje slabé stránky v hard logic a řešení komplexních problémů.
  - area: Obecná inteligence
    description: Průměrné skóre v AI Intelligence Index (48.6%) a MMLU Pro (79.3%) naznačuje, že model není špičkový v obecných znalostech a uvažování.
competitors:
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Podobná cena vstupu i výstupu
    comparison: Konkuruje v poměru cena/výkon, nabízí srovnatelný kontext.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-speciale
    model_id: deepseek/deepseek-v3.2-speciale
    price_comparison: Mírně dražší vstup i výstup
    comparison: Konkuruje v oblasti programování, ale má menší kontext.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Stejná cena vstupu, levnější výstup
    comparison: Konkuruje v rychlosti a ceně, nabízí mnohem větší kontext.
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Mírně dražší vstup, levnější výstup
    comparison: Konkuruje v ceně výstupu, ale má menší kontext a pravděpodobně nižší výkon v kódování.
recommendation:
  target_users:
    - Vývojáři softwaru
    - Data scientisti
    - Agentní inženýři
  use_cases:
    - Automatizace kódování
    - Generování kódu
    - Vývoj agentů
  avoid_for:
    - Složité logické úlohy
    - Aplikace vyžadující hluboké znalosti
    - Úlohy v češtině
verdict: Grok Code Fast 1 je vhodný pro vývojáře, kteří hledají rychlý a cenově dostupný model pro automatizaci kódování a vývoj agentů, ale je třeba počítat s omezenými logickými schopnostmi a jazykovou podporou.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 72.7
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 65.7
    tier: Dobrý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 75.7
    tier: Výborný
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 52.4
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 50.0
    tier: Průměrný
overall_score: 64.8
overall_tier: Dobrý
radar:
  logic_code: 65.7
  agentic: 75.7
  languages: 0
  safety: 0
  speed: Průměrný
expert_verdict:
  killer_feature: Agentní schopnosti a rychlost
  hidden_risk: Slabé logické uvažování a omezené jazykové schopnosti (čeština)
  recommended_use_case: Automatizace jednoduchých kódovacích úloh a vývoj agentů pro specifické účely
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:12"
---

Grok Code Fast 1 je rychlý a ekonomický model pro usuzování, který vyniká v agentním kódování. Díky viditelným stopám usuzování v odpovědi mohou vývojáři řídit Grok Code pro vysoce kvalitní pracovní postupy.

## Unikátní charakteristiky

Grok Code Fast 1 je rychlý a ekonomický model zaměřený na kódování s agentními schopnostmi. Důkazem jsou viditelné reasoning traces v odpovědích, což umožňuje vývojářům řídit Grok Code pro vysoce kvalitní pracovní postupy. Vyniká v τ2-Bench (agenti) s 75.7%.

## Silné stránky

### Agentní schopnosti
Vysoké skóre v τ2-Bench (75.7%) naznačuje silné schopnosti pro agentní aplikace a automatizaci úloh.

### Programování
Solidní skóre v LiveCodeBench (65.7%) ukazuje dobrou úroveň programovacích dovedností.

## Slabé stránky

### Logické uvažování
Nízké skóre v HLE (7.5%) a terminalbench_hard (16.3%) naznačuje slabé stránky v hard logic a řešení komplexních problémů.

### Obecná inteligence
Průměrné skóre v AI Intelligence Index (48.6%) a MMLU Pro (79.3%) naznačuje, že model není špičkový v obecných znalostech a uvažování.
