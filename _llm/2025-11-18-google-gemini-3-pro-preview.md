---
layout: llm_review
title: "Google: Gemini 3 Pro Preview"
date: "2025-11-18 15:04:28"
model_id: google/gemini-3-pro-preview
slug: google-gemini-3-pro-preview
provider: Google
pricing:
  prompt_per_m: 2.0
  completion_per_m: 12.0
  blend_per_m: 4.5
context_length: 1,048,576
max_output: 65,536
input_modalities:
  - text
  - image
  - file
  - audio
  - video
output_modalities:
  - text
focus: []
strengths: []
weaknesses: []
competitors: []
recommendation:

verdict: 
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 92.8
    tier: Excelentní
  coding:
    name: Programování
    icon: 💻
    score: 91.7
    tier: Excelentní
  agentic:
    name: Agenti & Nástroje
    icon: 🤖
    score: 87.1
    tier: Výborný
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 70.1
    tier: Dobrý
  speed:
    name: Rychlost
    icon: ⚡
    score: 29.7
    tier: Slabý
overall_score: 82.1
overall_tier: Výborný
radar: null
expert_verdict: null
analyzer_model: null
analyzed_at: null
---

Gemini 3 Pro je vlajkový model společnosti Google pro multimodální uvažování s vysokou přesností, který kombinuje silný výkon v oblasti textu, obrazu, videa, zvuku a kódu s kontextovým oknem o velikosti 1 milionu tokenů. Při použití vícekolového volání nástrojů je nutné zachovat detaily uvažování, viz naše dokumentace zde: https://openrouter.ai/docs/use-cases/reasoning-tokens#preserving-reasoning-blocks. Dosahuje nejlepších výsledků v benchmarkových testech v oblasti obecného uvažování, řešení STEM problémů, faktických otázek a multimodálního porozumění, včetně předních skóre v LMArena, GPQA Diamond, MathArena Apex, MMMU-Pro a Video-MMMU. Interakce kladou důraz na hloubku a interpretovatelnost: model je navržen tak, aby odvozoval záměr s minimálním promptingem a produkoval přímé odpovědi zaměřené na vhled.

Gemini 3 Pro, vytvořený pro pokročilý vývoj a agentní pracovní postupy, poskytuje robustní volání nástrojů, stabilitu plánování v dlouhém horizontu a silnou zero-shot generaci pro komplexní UI, vizualizace a kódovací úlohy. Vyniká v agentním kódování (SWE-Bench Verified, Terminal-Bench 2.0), multimodální analýze a strukturovaných úlohách dlouhého formátu, jako je syntéza výzkumu, plánování a interaktivní výukové zkušenosti. Mezi vhodné aplikace patří autonomní agenti, kódovací asistenti, multimodální analytika, vědecké uvažování a zpracování informací s vysokým kontextem.
