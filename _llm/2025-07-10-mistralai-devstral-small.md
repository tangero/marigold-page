---
layout: llm_review
title: "Mistral: Devstral Small 1.1"
date: "2025-07-10 17:19:11"
model_id: mistralai/devstral-small
slug: mistralai-devstral-small
provider: Mistral
pricing:
  prompt_per_m: 0.07
  completion_per_m: 0.28
  blend_per_m: 0.1225
context_length: 128,000
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Programování
  - Agenti
strengths:
  - area: Programování
    description: Vyniká v úlohách spojených s programováním, což dokazuje skóre 53.6% na SWE-Bench Verified.
  - area: Dlouhý kontext
    description: Disponuje kontextovým oknem 128k tokenů, což umožňuje zpracovávat rozsáhlé dokumenty a kódové báze.
weaknesses:
  - area: Obecná inteligence
    description: Celkové skóre 35.7/100 naznačuje slabší výkon v obecných úlohách a znalostech.
  - area: Čeština
    description: Nedostupnost dat pro češtinu (MMMLU) znemožňuje posoudit jeho schopnosti v tomto jazyce.
competitors:
  - provider: X-AI
    model: x-ai/grok-code-fast-1
    model_id: x-ai/grok-code-fast-1
    price_comparison: 1.6x levnější vstup, 5x levnější výstup
    comparison: Grok-code-fast-1 má větší kontext (256k) a je levnější, ale Devstral Small 1.1 může mít lepší výkon v specifických úlohách agentního kódování.
  - provider: MISTRALAI
    model: mistralai/ministral-3b-2512
    model_id: mistralai/ministral-3b-2512
    price_comparison: 1.2x levnější vstup, 2.8x levnější výstup
    comparison: Ministral-3b-2512 je výrazně levnější, ale Devstral Small 1.1 má pravděpodobně lepší výkon a delší kontext.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: 1.75x levnější vstup, 0.875x levnější výstup
    comparison: Deepseek-v3.2-exp je cenově srovnatelný, ale Devstral Small 1.1 má delší kontext a může být lépe optimalizován pro agentní kódování.
  - provider: OPENAI
    model: openai/gpt-5.1-chat
    model_id: openai/gpt-5.1-chat
    price_comparison: 10.4x dražší vstup, 35.7x dražší výstup
    comparison: GPT-5.1-chat je výrazně dražší, ale může nabízet lepší obecnou inteligenci a širší škálu schopností. Kontext je stejný.
recommendation:
  target_users:
    - Vývojáři softwaru
    - Výzkumníci v oblasti umělé inteligence
  use_cases:
    - Autonomní vývoj softwaru
    - Automatizace kódovacích úloh
  avoid_for:
    - Obecné úkoly vyžadující rozsáhlé znalosti
    - Aplikace vyžadující silnou podporu češtiny
verdict: Devstral Small 1.1 je vhodný pro vývojáře a výzkumníky, kteří se zaměřují na agentní kódovací workflow a potřebují model optimalizovaný pro automatizaci úloh spojených s programováním. Je třeba zvážit jeho slabší výkon v obecných znalostech a nedostupnost dat pro češtinu.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 29.4
    tier: Slabý
  coding:
    name: Programování
    icon: 💻
    score: 25.4
    tier: Slabý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 28.4
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 40.3
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 74.6
    tier: Dobrý
overall_score: 35.7
overall_tier: Slabý
radar:
  logic_code: 27.4
  agentic: 28.4
  languages: 0
  safety: 0
  speed: Dobrý
expert_verdict:
  killer_feature: Optimalizace pro agentní kódovací workflow
  hidden_risk: Slabší výkon v obecných znalostech a úlohách mimo programování
  recommended_use_case: Vývoj autonomních agentů pro úpravu a správu kódu
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:08"
---

Devstral Small 1.1 je 24B parametrový jazykový model s otevřenými váhami pro agenty softwarového inženýrství, vyvinutý společností Mistral AI ve spolupráci s All Hands AI. Je doladěn z Mistral Small 3.1 a uvolněn pod licencí Apache 2.0. Disponuje kontextovým oknem o velikosti 128k tokenů a podporuje jak funkci volání ve stylu Mistral, tak výstupní formáty XML.

Devstral Small 1.1, navržený pro agentní pracovní postupy kódování, je optimalizován pro úkoly, jako je průzkum codebase, úpravy více souborů a integrace do autonomních vývojových agentů, jako jsou OpenHands a Cline. Dosahuje 53,6 % na SWE-Bench Verified, čímž překonává všechny ostatní otevřené modely v tomto benchmarku, a přitom zůstává dostatečně nenáročný, aby běžel na jedné GPU 4090 nebo zařízení Apple Silicon. Model používá Tekken tokenizer se 131k slovníkem a je nasaditelný prostřednictvím vLLM, Transformers, Ollama, LM Studio a dalších běhových prostředí kompatibilních s OpenAI.

## Unikátní charakteristiky

Devstral Small 1.1 je optimalizován pro agentní kódovací workflow, dosahuje 53.6% na SWE-Bench Verified. Má kontextové okno 128k tokenů a podporuje Mistral-style function calling a XML výstupní formáty.

## Silné stránky

### Programování
Vyniká v úlohách spojených s programováním, což dokazuje skóre 53.6% na SWE-Bench Verified.

### Dlouhý kontext
Disponuje kontextovým oknem 128k tokenů, což umožňuje zpracovávat rozsáhlé dokumenty a kódové báze.

## Slabé stránky

### Obecná inteligence
Celkové skóre 35.7/100 naznačuje slabší výkon v obecných úlohách a znalostech.

### Čeština
Nedostupnost dat pro češtinu (MMMLU) znemožňuje posoudit jeho schopnosti v tomto jazyce.
