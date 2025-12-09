---
layout: llm_review
title: "Anthropic: Claude Opus 4"
date: "2025-05-22 18:27:25"
model_id: anthropic/claude-opus-4
slug: anthropic-claude-opus-4
provider: Anthropic
pricing:
  prompt_per_m: 15.0
  completion_per_m: 75.0
  blend_per_m: 30.0
context_length: 200,000
max_output: 32,000
input_modalities:
  - image
  - text
  - file
output_modalities:
  - text
focus:
  - Programování
  - Agent workflows
strengths:
  - area: Programování
    description: Vynikající výsledky v benchmarku SWE-bench (72.5%) a Terminal-bench (43.2%) naznačují silné schopnosti v oblasti programování.
  - area: Agentní workflow
    description: Podporuje rozsáhlé agentní workflow, zvládá tisíce kroků úkolů nepřetržitě po dobu několika hodin bez zhoršení výkonu.
weaknesses:
  - area: Cena
    description: Vysoká cena za vstupní a výstupní tokeny ve srovnání s konkurencí.
  - area: Jazykové schopnosti
    description: Data o výkonu v češtině (MMMLU) nejsou k dispozici, což ztěžuje posouzení kvality pro české uživatele.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: 3x levnější vstup, 3x levnější výstup
    comparison: Novější model od stejného poskytovatele, který nabízí nižší cenu.
  - provider: GOOGLE
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: 7.5x levnější vstup, 6.25x levnější výstup
    comparison: Konkurenční model s větším kontextovým oknem a nižší cenou.
  - provider: OPENAI
    model: openai/gpt-5.1
    model_id: openai/gpt-5.1
    price_comparison: 12x levnější vstup, 7.5x levnější výstup
    comparison: Konkurenční model s nižší cenou a velkým kontextovým oknem.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: 75x levnější vstup, 150x levnější výstup
    comparison: Výrazně levnější model s obrovským kontextovým oknem, ale pravděpodobně nižší kvalitou.
recommendation:
  target_users:
    - Vývojáři softwaru
    - Firmy vyvíjející agentní systémy
  use_cases:
    - Generování kódu
    - Automatizace komplexních úkolů
  avoid_for:
    - Aplikace citlivé na cenu
    - Použití v češtině bez ověření kvality
verdict: Claude Opus 4 je vhodný pro uživatele, kteří hledají nejlepší možný výkon v programování a agentních workflow a jsou ochotni zaplatit vyšší cenu. Pro aplikace citlivé na cenu existují levnější alternativy.
benchmark_categories: null
overall_score: null
overall_tier: null
radar:
  logic_code: 0
  agentic: 0
  languages: 0
  safety: 0
  speed: Nehodnoceno
expert_verdict:
  killer_feature: Špičkový výkon v programování a agentních workflow.
  hidden_risk: Vysoká cena může být limitující pro rozsáhlé nasazení.
  recommended_use_case: Vývoj komplexních softwarových řešení a automatizace náročných úkolů, kde je kvalita kódu kritická.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:05"
---

Claude Opus 4 je v době svého vydání hodnocen jako nejlepší kódovací model na světě, přinášející trvalý výkon při komplexních, dlouhotrvajících úlohách a pracovních postupech agentů. Stanovuje nové benchmarky v softwarovém inženýrství, dosahuje špičkových výsledků na SWE-bench (72,5 %) a Terminal-bench (43,2 %). Opus 4 podporuje rozšířené, agentní pracovní postupy, zvládá tisíce kroků úloh nepřetržitě po dobu hodin bez degradace.

## Unikátní charakteristiky

Claude Opus 4 je prezentován jako špičkový model pro kódování, dosahující vysokých výsledků na SWE-bench (72.5%) a Terminal-bench (43.2%). Je navržen pro komplexní a dlouhotrvající úkoly a agentní workflow.

## Silné stránky

### Programování
Vynikající výsledky v benchmarku SWE-bench (72.5%) a Terminal-bench (43.2%) naznačují silné schopnosti v oblasti programování.

### Agentní workflow
Podporuje rozsáhlé agentní workflow, zvládá tisíce kroků úkolů nepřetržitě po dobu několika hodin bez zhoršení výkonu.

## Slabé stránky

### Cena
Vysoká cena za vstupní a výstupní tokeny ve srovnání s konkurencí.

### Jazykové schopnosti
Data o výkonu v češtině (MMMLU) nejsou k dispozici, což ztěžuje posouzení kvality pro české uživatele.
