---
layout: llm_review
title: "xAI: Grok 3 Mini Beta"
date: "2025-04-10 01:09:55"
model_id: x-ai/grok-3-mini-beta
slug: x-ai-grok-3-mini-beta
provider: xAI
pricing:
  prompt_per_m: 0.3
  completion_per_m: 0.5
  blend_per_m: 0.35
context_length: 131,072
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus: []
strengths: []
weaknesses: []
competitors: []
recommendation:

verdict: 
benchmark_categories: null
overall_score: null
overall_tier: null
radar: null
expert_verdict: null
analyzer_model: null
analyzed_at: null
---

Grok 3 Mini je odlehčený, menší myšlenkový model. Na rozdíl od tradičních modelů, které generují odpovědi okamžitě, Grok 3 Mini před odpovědí přemýšlí. Je ideální pro úlohy náročné na usuzování, které nevyžadují rozsáhlé znalosti domény, a vyniká ve specifických matematických a kvantitativních případech použití, jako je řešení náročných hádanek nebo matematických problémů.

Transparentní "myšlenkové" stopy jsou přístupné. Ve výchozím nastavení používá nízké usuzování, které lze zvýšit nastavením `reasoning: { effort: "high" }`

Poznámka: Pro tento model existují dva endpointy xAI. Ve výchozím nastavení vás při použití tohoto modelu vždy směrujeme na základní endpoint. Pokud chcete rychlý endpoint, můžete přidat `provider: { sort: throughput}`, pro řazení podle propustnosti.
