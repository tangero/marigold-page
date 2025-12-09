---
layout: llm_review
title: "OpenAI: gpt-oss-120b"
date: "2025-08-05 19:17:11"
model_id: openai/gpt-oss-120b
slug: openai-gpt-oss-120b
provider: Openai
pricing:
  prompt_per_m: 0.039
  completion_per_m: 0.19
  blend_per_m: 0.0767
context_length: 131,072
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Rozumování
  - Agenti
  - Obecné účely
strengths:
  - area: Věda a matematika
    description: Vynikající výsledky v testech zaměřených na vědu a matematiku, jako GPQA Diamond (78.2%) a AIME (93.4%), ukazují na silné schopnosti v těchto oblastech.
  - area: Programování
    description: Vysoké skóre v LiveCodeBench (87.8%) naznačuje dobrou schopnost generovat a rozumět kódu.
weaknesses:
  - area: Obecná inteligence
    description: Relativně nízké skóre v HLE (18.5%) a průměrné skóre v AI Intelligence Index (60.5%) naznačují slabiny v oblastech vyžadujících komplexní logické uvažování a obecnou inteligenci.
  - area: Jazykové schopnosti (čeština)
    description: Chybí data pro hodnocení jazykových schopností, zejména v češtině (MMMLU), což omezuje jeho použitelnost v lokálních aplikacích.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: Výrazně dražší (62.5x dražší blend cena)
    comparison: Claude Opus je dražší, ale může nabízet lepší kvalitu v některých oblastech. Konkurenční kontextové okno.
  - provider: GOOGLE
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Dražší (15x dražší blend cena)
    comparison: Gemini Pro má menší kontextové okno, ale může mít lepší výkon v některých specifických úlohách.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Výrazně levnější (4x levnější blend cena)
    comparison: Mistral 14B je levnější, ale pravděpodobně nabízí nižší výkon v náročnějších úlohách, menší kontextové okno.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Levnější (cca 3x levnější blend cena)
    comparison: Deepseek V3.2 je levnější, ale má menší kontextové okno a pravděpodobně nižší výkon v náročnějších úlohách.
recommendation:
  target_users:
    - Výzkumníci v oblasti AI
    - Vývojáři agentů
    - Firmy s vysokými nároky na výpočetní výkon
  use_cases:
    - Vědecké modelování
    - Generování kódu
    - Náročné úlohy vyžadující hluboké rozumování
  avoid_for:
    - Aplikace s nízkým rozpočtem
    - Úlohy vyžadující silnou podporu češtiny
    - Aplikace vyžadující extrémně rychlou odezvu
verdict: gpt-oss-120b je vhodný pro uživatele, kteří potřebují vysoký výkon v oblasti vědy, matematiky a programování a jsou ochotni investovat do výpočetního výkonu. Pro aplikace vyžadující silnou podporu češtiny je nutné zvážit alternativy.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 78.2
    tier: Výborný
  coding:
    name: Programování
    icon: 💻
    score: 87.8
    tier: Výborný
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 65.8
    tier: Dobrý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 57.4
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 74.0
    tier: Dobrý
overall_score: 73.8
overall_tier: Dobrý
radar:
  logic_code: 87.8
  agentic: 65.8
  languages: 0
  safety: 0
  speed: Dobrý
expert_verdict:
  killer_feature: Vynikající výkon ve vědeckých a matematických úlohách díky vysokému skóre v GPQA Diamond a AIME.
  hidden_risk: Chybějící data pro češtinu omezují použitelnost v lokálních aplikacích.
  recommended_use_case: Vědecké modelování a simulace, kde je vyžadován vysoký výpočetní výkon a přesnost.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:10"
---

gpt-oss-120b je jazykový model typu Mixture-of-Experts (MoE) s otevřenými váhami a 117 miliardami parametrů od OpenAI, navržený pro produkční případy použití s vysokou úrovní usuzování, agentních schopností a všeobecného určení. Aktivuje 5,1 miliardy parametrů na jeden průchod dopřednou sítí a je optimalizován pro běh na jedné GPU H100 s nativní kvantizací MXFP4. Model podporuje konfigurovatelnou hloubku usuzování, plný přístup k řetězci myšlenek a nativní používání nástrojů, včetně volání funkcí, procházení webu a generování strukturovaného výstupu.

## Unikátní charakteristiky

gpt-oss-120b je navržen pro náročné úlohy vyžadující hluboké rozumování a schopnosti agentů. Využívá architekturu MoE, aktivuje pouze 5.1B parametrů na průchod a je optimalizován pro běh na jedné H100 GPU s MXFP4 kvantizací, což z něj činí efektivní volbu pro náročné aplikace.

## Silné stránky

### Věda a matematika
Vynikající výsledky v testech zaměřených na vědu a matematiku, jako GPQA Diamond (78.2%) a AIME (93.4%), ukazují na silné schopnosti v těchto oblastech.

### Programování
Vysoké skóre v LiveCodeBench (87.8%) naznačuje dobrou schopnost generovat a rozumět kódu.

## Slabé stránky

### Obecná inteligence
Relativně nízké skóre v HLE (18.5%) a průměrné skóre v AI Intelligence Index (60.5%) naznačují slabiny v oblastech vyžadujících komplexní logické uvažování a obecnou inteligenci.

### Jazykové schopnosti (čeština)
Chybí data pro hodnocení jazykových schopností, zejména v češtině (MMMLU), což omezuje jeho použitelnost v lokálních aplikacích.
