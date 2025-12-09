---
layout: llm_review
title: "OpenAI: GPT-5 Nano"
date: "2025-08-07 19:23:22"
model_id: openai/gpt-5-nano
slug: openai-gpt-5-nano
provider: Openai
pricing:
  prompt_per_m: 0.05
  completion_per_m: 0.4
  blend_per_m: 0.1375
context_length: 400,000
max_output: 128,000
input_modalities:
  - text
  - image
  - file
output_modalities:
  - text
focus:
  - Rychlé interakce
  - Nízká latence
  - Developer tools
strengths:
  - area: Programování
    description: Vysoké skóre v LiveCodeBench (78.9) naznačuje dobré schopnosti v generování a porozumění kódu.
  - area: Věda a matematika
    description: Solidní výkon v AIME_25 (83.7) a GPQA Diamond (67.6) naznačuje dobré znalosti a schopnosti v těchto oblastech.
weaknesses:
  - area: Rychlost
    description: "I přes zaměření na rychlost má model slabé skóre v rychlosti (TPS: 111.2, TTFT: 161.623s), což ho řadí mezi pomalejší modely."
  - area: Logické usuzování
    description: Velmi nízké skóre v HLE (8.2) naznačuje slabé schopnosti v komplexním logickém usuzování.
competitors:
  - provider: MISTRALAI
    model: ministral-3b-2512
    model_id: mistralai/ministral-3b-2512
    price_comparison: Podstatně levnější (vstup i výstup)
    comparison: Levnější alternativa, ale pravděpodobně s nižší kvalitou výstupu v komplexních úlohách.
  - provider: X-AI
    model: grok-4-fast
    model_id: x-ai/grok-4-fast
    price_comparison: Mnohem levnější (vstup i výstup)
    comparison: Levnější, s větším kontextem, ale může mít horší výkon v programování.
  - provider: DEEPSEEK
    model: deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: Levnější (vstup i výstup)
    comparison: Levnější alternativa, ale s menším kontextem.
  - provider: OPENAI
    model: gpt-5.1-chat
    model_id: openai/gpt-5.1-chat
    price_comparison: Dražší (1.25/10 vs 0.05/0.40)
    comparison: Dražší, ale pravděpodobně s lepšími schopnostmi v konverzačních úlohách a větším kontextem.
recommendation:
  target_users:
    - Vývojáři
    - Firmy s omezeným rozpočtem
    - Aplikace s nízkou latencí
  use_cases:
    - Rychlé prototypování
    - Jednoduché úlohy generování kódu
    - Real-time interakce
  avoid_for:
    - Složité logické úlohy
    - Aplikace vyžadující hluboké usuzování
    - Úlohy vyžadující rozsáhlé znalosti
verdict: GPT-5-Nano je vhodný pro vývojáře a firmy s omezeným rozpočtem, kteří potřebují rychlý a levný model pro jednoduché úlohy generování kódu a real-time interakce, ale je nutné počítat s jeho omezenými schopnostmi v komplexních úlohách a pomalejší rychlostí.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 67.6
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 78.9
    tier: Výborný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 36.5
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 51.8
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 27.8
    tier: Slabý
overall_score: 55.3
overall_tier: Průměrný
radar:
  logic_code: 73.2
  agentic: 36.5
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Nízká cena a malá velikost
  hidden_risk: Slabá rychlost inference (vysoká latence) může omezit použitelnost v některých real-time aplikacích.
  recommended_use_case: Generování jednoduchých úryvků kódu v prostředí vývojářských nástrojů.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:10"
---

GPT-5-Nano je nejmenší a nejrychlejší varianta v systému GPT-5, optimalizovaná pro vývojářské nástroje, rychlé interakce a prostředí s ultra-nízkou latencí. I když je ve srovnání s většími protějšky omezena v hloubce usuzování, zachovává si klíčové funkce pro dodržování instrukcí a bezpečnost. Je nástupcem GPT-4.1-nano a nabízí odlehčenou variantu pro nákladově citlivé nebo real-time aplikace.

## Unikátní charakteristiky

GPT-5-Nano je nejmenší a nejrychlejší varianta GPT-5, optimalizovaná pro rychlé interakce. I přes omezené schopnosti usuzování si zachovává klíčové vlastnosti pro dodržování instrukcí a bezpečnost. Nízké skóre v HLE (hard logic) naznačuje slabší schopnosti v komplexním logickém usuzování.

## Silné stránky

### Programování
Vysoké skóre v LiveCodeBench (78.9) naznačuje dobré schopnosti v generování a porozumění kódu.

### Věda a matematika
Solidní výkon v AIME_25 (83.7) a GPQA Diamond (67.6) naznačuje dobré znalosti a schopnosti v těchto oblastech.

## Slabé stránky

### Rychlost
I přes zaměření na rychlost má model slabé skóre v rychlosti (TPS: 111.2, TTFT: 161.623s), což ho řadí mezi pomalejší modely.

### Logické usuzování
Velmi nízké skóre v HLE (8.2) naznačuje slabé schopnosti v komplexním logickém usuzování.
