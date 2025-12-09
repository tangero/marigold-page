---
layout: llm_review
title: "Mistral: Devstral Medium"
date: "2025-07-10 17:28:41"
model_id: mistralai/devstral-medium
slug: mistralai-devstral-medium
provider: Mistral
pricing:
  prompt_per_m: 0.4
  completion_per_m: 2.0
  blend_per_m: 0.8
context_length: 131,072
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Generování kódu
  - Agentní uvažování
strengths:
  - area: Generování kódu
    description: Dosahuje 61.6% na SWE-Bench Verified, což je lepší než Gemini 2.5 Pro a GPT-4.1.
  - area: Cena
    description: Nabízí srovnatelný výkon jako dražší modely (Gemini, GPT-4) za výrazně nižší cenu.
weaknesses:
  - area: Obecná inteligence
    description: Celkové skóre 36.4/100 naznačuje slabší výkon v oblastech mimo kódování a agentní uvažování.
  - area: Čeština
    description: MMMLU skóre pro češtinu není k dispozici, což ztěžuje posouzení použitelnosti v českém jazyce.
competitors:
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: Levnější vstup, dražší výstup
    comparison: Gemini 2.5 Flash Image je levnější na vstupu, ale Devstral Medium má lepší kontext a pravděpodobně lepší výkon v kódování.
  - provider: OPENAI
    model: openai/gpt-5.1-codex-max
    model_id: openai/gpt-5.1-codex-max
    price_comparison: Dražší vstup i výstup
    comparison: GPT-5.1 Codex Max je dražší, ale může nabízet lepší obecnou inteligenci a širší škálu schopností (data nejsou k dispozici).
  - provider: X-AI
    model: x-ai/grok-code-fast-1
    model_id: x-ai/grok-code-fast-1
    price_comparison: Levnější vstup, levnější výstup
    comparison: Grok-code-fast-1 je výrazně levnější, ale může mít horší výkon v náročnějších kódovacích úlohách (data nejsou k dispozici).
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Levnější vstup, levnější výstup
    comparison: Deepseek v3.2 je levnější, ale Devstral Medium má větší kontext a pravděpodobně lepší výkon v agentním uvažování.
recommendation:
  target_users:
    - Vývojáři softwaru
    - AI inženýři
  use_cases:
    - Generování kódu
    - Automatizace úloh pomocí agentů
  avoid_for:
    - Úlohy vyžadující vysokou úroveň matematických schopností
    - Aplikace vyžadující silnou podporu češtiny
verdict: Devstral Medium je vhodný pro vývojáře, kteří hledají cenově efektivní řešení pro generování kódu a automatizaci úloh pomocí agentů, ale měli by zvážit jeho omezení v obecné inteligenci a jazykové podpoře.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 36.5
    tier: Slabý
  coding:
    name: Programování
    icon: 💻
    score: 33.7
    tier: Slabý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 19.9
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 45.7
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 55.8
    tier: Průměrný
overall_score: 36.4
overall_tier: Slabý
radar:
  logic_code: 33.7
  agentic: 19.9
  languages: 0
  safety: 0
  speed: Průměrný
expert_verdict:
  killer_feature: Vynikající poměr cena/výkon v generování kódu.
  hidden_risk: Slabší výkon v oblastech mimo kódování a agentní uvažování, neznámá kvalita češtiny.
  recommended_use_case: Automatizace generování kódu a vývoj agentů pro specifické úlohy.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:08"
---

Devstral Medium je vysoce výkonný model pro generování kódu a agentní usuzování, vyvinutý společně společnostmi Mistral AI a All Hands AI. Je koncipován jako vylepšení oproti Devstral Small a dosahuje 61,6 % na SWE-Bench Verified, čímž v úlohách souvisejících s kódem předčí Gemini 2.5 Pro a GPT-4.1, a to za zlomek nákladů. Je navržen pro generalizaci napříč styly promptů a používání nástrojů v kódových agentech a frameworkách.

Devstral Medium je dostupný pouze přes API (není open-weight) a podporuje nasazení v podnikovém prostředí na soukromé infrastruktuře, s volitelnými možnostmi fine-tuningu.

## Unikátní charakteristiky

Devstral Medium vyniká v generování kódu a agentním uvažování, s výkonem srovnatelným s Gemini 2.5 Pro a GPT-4.1 v kódovacích úlohách, ale za zlomek ceny. Je navržen pro generalizaci napříč různými styly promptů a pro použití nástrojů v kódovacích agentech a frameworkách.

## Silné stránky

### Generování kódu
Dosahuje 61.6% na SWE-Bench Verified, což je lepší než Gemini 2.5 Pro a GPT-4.1.

### Cena
Nabízí srovnatelný výkon jako dražší modely (Gemini, GPT-4) za výrazně nižší cenu.

## Slabé stránky

### Obecná inteligence
Celkové skóre 36.4/100 naznačuje slabší výkon v oblastech mimo kódování a agentní uvažování.

### Čeština
MMMLU skóre pro češtinu není k dispozici, což ztěžuje posouzení použitelnosti v českém jazyce.
