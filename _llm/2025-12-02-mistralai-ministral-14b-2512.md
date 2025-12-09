---
layout: llm_review
title: "Mistral: Ministral 3 14B 2512"
date: "2025-12-02 14:22:15"
model_id: mistralai/ministral-14b-2512
slug: mistralai-ministral-14b-2512
provider: Mistral
pricing:
  prompt_per_m: 0.2
  completion_per_m: 0.2
  blend_per_m: 0.2
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
    description: Dosahuje skóre 57.2% v GPQA Diamond, což naznačuje dobrou schopnost řešit vědecké problémy.
  - area: Obecná inteligence
    description: S MMLU Pro skóre 69.3% vykazuje solidní znalosti v různých oblastech.
weaknesses:
  - area: Programování
    description: S nízkým skóre 35.1% v LiveCodeBench se nehodí pro náročné programovací úkoly.
  - area: Logické uvažování
    description: Velmi nízké skóre 4.6% v HLE naznačuje slabé schopnosti v oblasti hard logic.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-sonnet-4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: 15x dražší výstup
    comparison: Claude Sonnet 4.5 má 4x větší kontext a pravděpodobně lepší schopnosti v oblasti agentů, ale je výrazně dražší.
  - provider: X-AI
    model: x-ai/grok-4-fast
    model_id: x-ai/grok-4-fast
    price_comparison: Stejná cena vstupu, 2.5x dražší výstup
    comparison: Grok-4-fast má mnohem větší kontext (2M tokenů) a může být vhodnější pro úlohy vyžadující dlouhodobou paměť.
  - provider: MISTRALAI
    model: mistralai/mistral-large-2512
    model_id: mistralai/mistral-large-2512
    price_comparison: 2.5x dražší vstup, 7.5x dražší výstup
    comparison: Mistral Large by měl mít lepší celkový výkon, ale je výrazně dražší.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: Mírně dražší vstup, 1.6x dražší výstup
    comparison: Deepseek-v3.2-exp se zaměřuje na kódování, takže je lepší volbou pro programátorské úlohy.
recommendation:
  target_users:
    - Výzkumníci
    - Firmy s velkým objemem dat
  use_cases:
    - Analýza dokumentů
    - Zpracování obrazových dat
  avoid_for:
    - Náročné programování
    - Aplikace vyžadující silné logické uvažování
verdict: Ministral 3 14B je vhodný pro uživatele, kteří potřebují zpracovávat velké objemy dat a využívat multimodální schopnosti, ale nepotřebují pokročilé programovací nebo logické dovednosti.
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 57.2
    tier: Průměrný
  coding:
    name: Programování
    icon: 💻
    score: 35.1
    tier: Slabý
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 27.2
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 45.0
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 72.5
    tier: Dobrý
overall_score: 44.6
overall_tier: Průměrný
radar:
  logic_code: 4.6
  agentic: 27.2
  languages: 0
  safety: 0
  speed: Dobrý
expert_verdict:
  killer_feature: Velký kontext 262,144 tokenů
  hidden_risk: Slabší výkon v programování a logickém uvažování omezuje použitelnost v některých oblastech.
  recommended_use_case: Analýza velkých objemů textových a obrazových dat, kde je důležitý kontext.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:20"
---

Největší model v rodině Ministral 3, Ministral 3 14B, nabízí špičkové schopnosti a výkon srovnatelný s jeho větším protějškem Mistral Small 3.2 24B. Jedná se o výkonný a efektivní jazykový model s funkcemi vidění.

## Unikátní charakteristiky

Ministral 3 14B nabízí multimodální schopnosti a výkon srovnatelný s Mistral Small 3.2 24B. Vyniká velkým kontextovým oknem 262,144 tokenů a dobrou rychlostí inference.

## Silné stránky

### Věda a matematika
Dosahuje skóre 57.2% v GPQA Diamond, což naznačuje dobrou schopnost řešit vědecké problémy.

### Obecná inteligence
S MMLU Pro skóre 69.3% vykazuje solidní znalosti v různých oblastech.

## Slabé stránky

### Programování
S nízkým skóre 35.1% v LiveCodeBench se nehodí pro náročné programovací úkoly.

### Logické uvažování
Velmi nízké skóre 4.6% v HLE naznačuje slabé schopnosti v oblasti hard logic.
