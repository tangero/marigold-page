---
layout: llm_review
title: "Mistral: Mistral Small Creative"
date: "2025-12-16 19:10:53"
model_id: mistralai/mistral-small-creative
slug: mistralai-mistral-small-creative
provider: Mistralai
pricing:
  prompt_per_m: 0.1
  completion_per_m: 0.3
context_length: 32,768
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Kreativní psaní
  - Roleplay a dialogy
  - Generování narativu
competitors:
  - provider: Mistral AI
    model: mistralai/ministral-14b-2512
    model_id: mistralai/ministral-14b-2512
    price_comparison: Target model je o 50 % levnější na vstupu, ale o 50 % dražší na výstupu
    comparison: Ministral nabízí výrazně větší kontext (262k vs 32k) a je pravděpodobně univerzálnější, zatímco Small Creative je úzce specializovaný.
  - provider: X-AI
    model: x-ai/grok-4.1-fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Grok je 2x dražší na vstupu ($0.20) a téměř 2x na výstupu ($0.50)
    comparison: Grok nabízí masivní kontext (2M tokenů) a vyšší rychlost, Mistral Small Creative konkuruje pouze v úlohách s krátkým kontextem citlivých na cenu.
  - provider: DeepSeek
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: DeepSeek je přibližně 2x dražší na vstupu ($0.21) a srovnatelný na výstupu
    comparison: DeepSeek nabízí lepší poměr cena/výkon pro obecné úlohy díky většímu kontextu (163k), Mistral vítězí pouze v absolutně nejnižších nákladech na vstup.
recommendation:
  target_users:
    - Vývojáři her (NPC dialogy)
    - Tvůrci kreativních aplikací
    - Marketingové agentury (copywriting)
  use_cases:
    - Generování interaktivních příběhů
    - Roleplay chatboti
    - Brainstorming a variace textů
  avoid_for:
    - Analýza dlouhých dokumentů (RAG nad 32k tokenů)
    - Kritické logické operace a matematika
    - Přesná faktografická rešerše
verdict: Ideální volba pro aplikace vyžadující levné a kreativní generování textu v krátkém kontextu, kde je prioritou nízká cena a stylistika před hlubokou logikou.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2025-12-17 07:24"
---

Mistral Small Creative je experimentální malý model navržený pro kreativní psaní, generování narativu, hraní rolí a dialog řízený postavami, sledování instrukcí pro všeobecné použití a konverzační agenty.

## Unikátní charakteristiky

Mistral Small Creative je experimentální model specificky vyladěný (fine-tuned) pro stylistickou variabilitu a plynulost textu spíše než pro striktní logiku, s extrémně agresivní cenovou politikou v segmentu malých modelů.

## Silné stránky

### Cenová efektivita
S cenou $0.10 za 1M vstupních tokenů se jedná o jeden z nejlevnějších modelů na trhu, ideální pro vysokoobjemové aplikace.

### Stylistická adaptabilita
Model je navržen pro snížení repetitivnosti a 'robotického' frázování, což je výhodné pro generování fikce a chatbota s osobností.

## Slabé stránky

### Kontextové okno
Kapacita 32,768 tokenů je na poměry prosince 2025 velmi nízká (konkurence běžně nabízí 200k+), což znemožňuje zpracování dlouhých dokumentů.

### Komplexní uvažování
Jako model kategorie 'Small' zaměřený na kreativitu pravděpodobně zaostává v logických úlohách a kódování oproti modelům třídy Pro/Opus.
