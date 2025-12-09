---
layout: llm_review
title: "OpenAI: GPT-5.1-Codex-Max"
date: "2025-12-04 21:08:54"
model_id: openai/gpt-5.1-codex-max
slug: openai-gpt-5-1-codex-max
provider: Openai
pricing:
  prompt_per_m: 1.25
  completion_per_m: 10.0
  blend_per_m: 3.4375
context_length: 400,000
max_output: 128,000
input_modalities:
  - text
  - image
output_modalities:
  - text
focus:
  - Programování
  - Agentické úlohy
strengths:
  - area: Kontext
    description: Podpora kontextu až 400 000 tokenů umožňuje zpracovávat komplexní projekty.
  - area: Agentické úlohy
    description: Optimalizováno pro agentické workflow v softwarovém inženýrství, matematice a výzkumu.
weaknesses:
  - area: Cena
    description: Vyšší cena v porovnání s některými konkurenčními modely.
  - area: Benchmark data
    description: Chybějící benchmark data znemožňují objektivní srovnání výkonu s konkurencí.
competitors:
  - provider: ANTHROPIC
    model: anthropic/claude-opus-4.5
    model_id: anthropic/claude-opus-4.5
    price_comparison: Dražší vstup i výstup
    comparison: Konkuruje v kvalitě, ale je dražší. Kontext je poloviční.
  - provider: GOOGLE
    model: google/gemini-3-pro-preview
    model_id: google/gemini-3-pro-preview
    price_comparison: Dražší výstup
    comparison: Konkuruje v kontextu, ale má dražší výstup a chybí benchmark data.
  - provider: X-AI
    model: x-ai/grok-code-fast-1
    model_id: x-ai/grok-code-fast-1
    price_comparison: Levnější vstup, dražší výstup
    comparison: Konkuruje v programování, ale má menší kontext a chybí benchmark data.
  - provider: MISTRALAI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Mnohem levnější vstup i výstup
    comparison: Konkuruje cenou, ale má menší kontext a chybí benchmark data.
recommendation:
  target_users:
    - Vývojáři softwaru
    - Výzkumníci
  use_cases:
    - Komplexní softwarové projekty
    - Agentické úlohy vyžadující dlouhý kontext
  avoid_for:
    - Úlohy s nízkým rozpočtem
    - Úlohy vyžadující rychlou odezvu
verdict: GPT-5.1-Codex-Max je vhodný pro vývojáře a výzkumníky, kteří potřebují zpracovávat velmi rozsáhlé projekty a nevadí jim vyšší cena. Chybějící benchmark data ale ztěžují objektivní posouzení jeho výkonu.
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
  killer_feature: Velký kontext (400 000 tokenů)
  hidden_risk: Chybějící benchmark data znemožňují objektivní posouzení výkonu v reálných úlohách.
  recommended_use_case: Vývoj komplexních softwarových systémů s rozsáhlou kódovou základnou.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:20"
---

GPT-5.1-Codex-Max je nejnovější agentní model pro kódování od OpenAI, navržený pro dlouhodobé softwarové vývojové úlohy s vysokým kontextem. Je založen na aktualizované verzi odvozovacího stacku 5.1 a trénován na agentních pracovních postupech zahrnujících softwarové inženýrství, matematiku a výzkum.
GPT-5.1-Codex-Max poskytuje rychlejší výkon, vylepšené odvozování a vyšší tokenovou efektivitu v průběhu celého životního cyklu vývoje.

## Unikátní charakteristiky

GPT-5.1-Codex-Max je navržen pro dlouhotrvající vývoj softwaru s vysokým kontextem. Využívá aktualizovanou verzi 5.1 reasoning stack a je trénován na agentických workflow v softwarovém inženýrství, matematice a výzkumu. Benchmark data nejsou k dispozici.

## Silné stránky

### Kontext
Podpora kontextu až 400 000 tokenů umožňuje zpracovávat komplexní projekty.

### Agentické úlohy
Optimalizováno pro agentické workflow v softwarovém inženýrství, matematice a výzkumu.

## Slabé stránky

### Cena
Vyšší cena v porovnání s některými konkurenčními modely.

### Benchmark data
Chybějící benchmark data znemožňují objektivní srovnání výkonu s konkurencí.
