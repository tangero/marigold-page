---
layout: llm_review
title: "OpenAI: gpt-oss-20b"
date: "2025-08-05 19:17:09"
model_id: openai/gpt-oss-20b
slug: openai-gpt-oss-20b
provider: Openai
pricing:
  prompt_per_m: 0.03
  completion_per_m: 0.14
  blend_per_m: 0.0575
context_length: 131,072
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Programování
  - Věda a matematika
strengths:
  - area: Programování
    description: Vysoké skóre v LiveCodeBench (77.7%) naznačuje silné schopnosti v oblasti kódování.
  - area: Matematika
    description: Vynikající výkon v aime_25 (89.3%) a artificial_analysis_math_index (89.3%) ukazuje na silné matematické dovednosti.
weaknesses:
  - area: Logické uvažování
    description: Nízké skóre v HLE (9.8%) a terminalbench_hard (9.9%) naznačuje slabiny v hard logickém uvažování.
  - area: Obecná inteligence
    description: Průměrné skóre v AI Intelligence Index (52.1%) a MMLU Pro (74.8%) naznačuje, že model není špičkový v obecných znalostech.
competitors:
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: 3x levnější vstup i výstup
    comparison: Levnější alternativa s velkým kontextem, ale pravděpodobně nižší inteligencí.
  - provider: MISTRALAI
    model: mistralai/ministral-8b-2512
    model_id: mistralai/ministral-8b-2512
    price_comparison: 4x levnější vstup i výstup
    comparison: Ještě levnější, ale s menšími parametry a potenciálně nižší kvalitou.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Mírně levnější vstup i výstup
    comparison: Konkurenční model s podobnými parametry, ale menším kontextem.
  - provider: X-AI
    model: x-ai/grok-code-fast-1
    model_id: x-ai/grok-code-fast-1
    price_comparison: 3x levnější vstup, 7x levnější výstup
    comparison: Velmi levný model, zaměřený na kódování, ale s menším kontextem.
recommendation:
  target_users:
    - Vývojáři
    - Vědci
    - Studenti
  use_cases:
    - Generování kódu
    - Matematické výpočty
    - Prototypování agentů
  avoid_for:
    - Složité logické úlohy
    - Aplikace vyžadující hluboké znalosti v češtině
verdict: gpt-oss-20b je dobrá volba pro vývojáře a vědce, kteří potřebují model s dobrými matematickými a programovacími schopnostmi, ale měli by se vyhnout úlohám vyžadujícím složité logické uvažování.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 68.8
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 77.7
    tier: Výborný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 60.2
    tier: Dobrý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 50.4
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 74.3
    tier: Dobrý
overall_score: 66.8
overall_tier: Dobrý
radar:
  logic_code: 77.7
  agentic: 60.2
  languages: 0
  safety: 0
  speed: Dobrý
expert_verdict:
  killer_feature: Vynikající matematické schopnosti
  hidden_risk: Slabé logické uvažování a potenciální problémy s češtinou (data nejsou k dispozici)
  recommended_use_case: Vývoj aplikací vyžadujících matematické výpočty a generování kódu.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:09"
---

gpt-oss-20b je model s otevřenými váhami a 21 miliardami parametrů, vydaný společností OpenAI pod licencí Apache 2.0. Používá architekturu Mixture-of-Experts (MoE) s 3,6 miliardami aktivních parametrů na jeden průchod dopřednou sítí, optimalizovanou pro inferenci s nižší latencí a nasazení na spotřebitelském hardwaru nebo hardwaru s jednou GPU. Model je trénován ve formátu odezvy Harmony společnosti OpenAI a podporuje konfiguraci úrovně usuzování, dolaďování a agentní schopnosti včetně volání funkcí, používání nástrojů a strukturovaných výstupů.

## Unikátní charakteristiky

gpt-oss-20b je open-source model s architekturou Mixture-of-Experts, optimalizovaný pro nízkou latenci a nasazení na spotřebitelském hardwaru. Vyniká v matematických úlohách a programování, což dokazují vysoké skóre v aime_25 a LiveCodeBench.

## Silné stránky

### Programování
Vysoké skóre v LiveCodeBench (77.7%) naznačuje silné schopnosti v oblasti kódování.

### Matematika
Vynikající výkon v aime_25 (89.3%) a artificial_analysis_math_index (89.3%) ukazuje na silné matematické dovednosti.

## Slabé stránky

### Logické uvažování
Nízké skóre v HLE (9.8%) a terminalbench_hard (9.9%) naznačuje slabiny v hard logickém uvažování.

### Obecná inteligence
Průměrné skóre v AI Intelligence Index (52.1%) a MMLU Pro (74.8%) naznačuje, že model není špičkový v obecných znalostech.
