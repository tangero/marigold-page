---
layout: llm_review
title: "Anthropic: Claude Opus 4.5"
date: "2025-11-24 19:56:20"
model_id: anthropic/claude-opus-4.5
slug: anthropic-claude-opus-4-5
provider: Anthropic
pricing:
  prompt_per_m: 5.0
  completion_per_m: 25.0
  blend_per_m: 10.0
context_length: 200,000
max_output: 32,000
input_modalities:
  - file
  - image
  - text
output_modalities:
  - text
focus:
  - Rozumování
  - Agenti
strengths:
  - area: Agentní schopnosti
    description: Vynikající výkon v benchmarku τ2-Bench (86.3) naznačuje silné schopnosti pro autonomní agenty a nástroje.
  - area: Vědecké rozumování
    description: Vysoké skóre v GPQA Diamond (81.0) ukazuje na schopnost řešit komplexní vědecké problémy.
weaknesses:
  - area: Rychlost
    description: Nízké TPS (77.2) a vysoká latence (2.156s) znamenají pomalejší odezvu ve srovnání s konkurencí.
  - area: Čeština
    description: Chybějící data pro MMMLU znemožňují posoudit kvalitu češtiny.
competitors:
  - provider: Anthropic
    model: anthropic/claude-sonnet-4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: 3x levnější vstup, 1.6x levnější výstup
    comparison: Sonnet 4.5 nabízí větší kontext (1M tokenů) za nižší cenu, ale pravděpodobně nižší výkon v náročných úlohách.
  - provider: Google
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: 2.5x levnější vstup, 2x levnější výstup
    comparison: Gemini 3 Pro Preview nabízí obrovský kontext (1M tokenů) za nižší cenu, ale nemusí dosahovat stejné úrovně rozumování.
  - provider: OpenAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: 4x levnější vstup, 2.5x levnější výstup
    comparison: GPT-5.1 nabízí velký kontext (400k tokenů) za nižší cenu, ale je nutné porovnat výkon v specifických úlohách.
  - provider: X-AI
    model: x-ai/grok-4-fast
    model_id: x-ai/grok-4-fast
    price_comparison: 25x levnější vstup, 50x levnější výstup
    comparison: Grok-4-fast je výrazně levnější, nabízí obrovský kontext (2M tokenů), ale pravděpodobně nižší kvalitu rozumování a agentních schopností.
recommendation:
  target_users:
    - Výzkumníci
    - Vývojáři agentů
    - Softwaroví inženýři
  use_cases:
    - Autonomní výzkum
    - Ladění kódu
    - Multi-step plánování
  avoid_for:
    - Úlohy citlivé na latenci
    - Aplikace s omezeným rozpočtem
    - Úlohy vyžadující perfektní češtinu
verdict: Claude Opus 4.5 je vhodný pro uživatele, kteří potřebují špičkový model pro náročné úlohy vyžadující rozumování a agentní schopnosti, a jsou ochotni akceptovat vyšší cenu a pomalejší odezvu.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 81.0
    tier: Výborný
  coding:
    name: Programování
    icon: 💻
    score: 73.8
    tier: Dobrý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 86.3
    tier: Výborný
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 60.4
    tier: Dobrý
  speed:
    name: Rychlost
    icon: ⚡
    score: 19.3
    tier: Slabý
overall_score: 72.1
overall_tier: Dobrý
radar:
  logic_code: 77.4
  agentic: 86.3
  languages: 0
  safety: 0
  speed: Slabý
expert_verdict:
  killer_feature: Vynikající agentní schopnosti a rozumování
  hidden_risk: Vysoká cena a pomalá inference mohou omezit praktické nasazení
  recommended_use_case: Vývoj komplexních agentů pro automatizaci vědeckého výzkumu
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:18"
---

Claude Opus 4.5 je špičkový model pro usuzování od společnosti Anthropic, optimalizovaný pro komplexní softwarové inženýrství, agentní pracovní postupy a dlouhodobé používání počítače. Nabízí silné multimodální schopnosti, konkurenceschopný výkon v reálných programovacích a usuzovacích benchmarkách a vylepšenou odolnost vůči prompt injection. Model je navržen tak, aby efektivně fungoval při různých úrovních úsilí, což vývojářům umožňuje volit mezi rychlostí, hloubkou a využitím tokenů v závislosti na požadavcích úkolu. Dodává se s novým parametrem pro řízení efektivity tokenů, který je přístupný pomocí parametru Verbosity OpenRouter s hodnotami low, medium nebo high.

Opus 4.5 podporuje pokročilé používání nástrojů, rozšířenou správu kontextu a koordinované multi-agentní konfigurace, díky čemuž je vhodný pro autonomní výzkum, ladění, vícestupňové plánování a manipulaci s tabulkami/prohlížeči. Poskytuje podstatné zlepšení ve strukturovaném usuzování, spolehlivosti provádění a sladění ve srovnání s předchozími generacemi Opus, přičemž snižuje režii tokenů a zlepšuje výkon u dlouhotrvajících úkolů.

## Unikátní charakteristiky

Claude Opus 4.5 vyniká v komplexních úlohách vyžadujících sofistikované rozumování a agentní workflow. Dosahuje vysokých skóre v τ2-Bench (86.3) a GPQA Diamond (81.0), což naznačuje silné schopnosti v oblasti agentů a vědeckého uvažování.

## Silné stránky

### Agentní schopnosti
Vynikající výkon v benchmarku τ2-Bench (86.3) naznačuje silné schopnosti pro autonomní agenty a nástroje.

### Vědecké rozumování
Vysoké skóre v GPQA Diamond (81.0) ukazuje na schopnost řešit komplexní vědecké problémy.

## Slabé stránky

### Rychlost
Nízké TPS (77.2) a vysoká latence (2.156s) znamenají pomalejší odezvu ve srovnání s konkurencí.

### Čeština
Chybějící data pro MMMLU znemožňují posoudit kvalitu češtiny.
