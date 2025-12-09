---
layout: llm_review
title: "DeepSeek: R1 Distill Qwen 14B"
date: "2025-01-30 00:39:00"
model_id: deepseek/deepseek-r1-distill-qwen-14b
slug: deepseek-deepseek-r1-distill-qwen-14b
provider: DeepSeek
pricing:
  prompt_per_m: 0.12
  completion_per_m: 0.12
  blend_per_m: 0.12
context_length: 32,768
max_output: 16,384
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
benchmark_categories:
  science:
    name: Věda & Matematika
    icon: 🧮
    score: 65.0
    tier: Dobrý
  coding:
    name: Programování
    icon: 💻
    score: 37.6
    tier: Slabý
  intelligence:
    name: Obecná inteligence
    icon: 🧠
    score: 47.9
    tier: Průměrný
  speed:
    name: Rychlost
    icon: ⚡
    score: 16.4
    tier: Slabý
overall_score: 47.6
overall_tier: Průměrný
radar: null
expert_verdict: null
analyzer_model: null
analyzed_at: null
---

DeepSeek R1 Distill Qwen 14B je destilovaný velký jazykový model založený na [Qwen 2.5 14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B), využívající výstupy z [DeepSeek R1](/deepseek/deepseek-r1). Překonává o1-mini od OpenAI v různých benchmarkách a dosahuje nových nejlepších výsledků (state-of-the-art) pro husté modely.

Další výsledky benchmarků zahrnují:

- AIME 2024 pass@1: 69.7
- MATH-500 pass@1: 93.9
- CodeForces Rating: 1481

Model využívá jemné doladění (fine-tuning) z výstupů DeepSeek R1, což umožňuje konkurenceschopný výkon srovnatelný s většími špičkovými modely (frontier models).
