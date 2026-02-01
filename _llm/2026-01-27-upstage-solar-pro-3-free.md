---
layout: llm_review
title: "Upstage: Solar Pro 3 (free)"
date: "2026-01-27 03:33:20"
model_id: "upstage/solar-pro-3:free"
slug: upstage-solar-pro-3-free
provider: Upstage
pricing:
  prompt_per_m: 0.0
  completion_per_m: 0.0
context_length: 128,000
max_output: N/A
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Optimalizace pro korejštinu
  - Efektivita inference
  - Vícejazyčná podpora (EN/JP/KR)
competitors:
  - provider: MistralAI
    model: Mistral Devstral 2512 (free)
    model_id: "mistralai/devstral-2512:free"
    price_comparison: Identická cena (zdarma)
    comparison: Mistral nabízí dvojnásobné kontextové okno (262k) a je pravděpodobně silnější v kódování a evropských jazycích, zatímco Solar vede v asijských jazycích.
  - provider: DeepSeek
    model: DeepSeek v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: DeepSeek je placený ($0.25/1M), Solar je zdarma
    comparison: Oba modely využívají efektivní MoE architekturu. DeepSeek je silnější generalista pro logiku a kód, Solar je výhodnější pro specifické jazykové aplikace a nulové náklady.
  - provider: X-AI
    model: Grok 4.1 Fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Grok je velmi levný ($0.20/1M), ale není zdarma
    comparison: Grok dominuje v práci s dlouhým kontextem (2M tokenů vs 128k u Solar) a rychlosti zpracování velkých objemů dat.
recommendation:
  target_users:
    - Vývojáři aplikací pro korejský/japonský trh
    - Startupy s omezeným rozpočtem
    - Výzkumníci testující MoE architektury
  use_cases:
    - Překlad a lokalizace (KR/JP/EN)
    - RAG aplikace s menším objemem dokumentů
    - Chatboti vyžadující nízkou latenci
  avoid_for:
    - Analýza extrémně dlouhých dokumentů (>100 stran)
    - Multimodální vstupy (obrázky, audio)
    - Komplexní matematické uvažování na úrovni SOTA modelů
verdict: Ideální volba pro projekty vyžadující vysokou jazykovou kompetenci v asijských jazycích nebo nulové provozní náklady, avšak technicky zaostává v délce kontextu za špičkou roku 2025.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2026-01-27 07:26"
---

Solar Pro 3 je výkonný jazykový model typu Mixture-of-Experts (MoE) od společnosti Upstage. S celkovým počtem 102 miliard parametrů a 12 miliardami aktivních parametrů na jeden průchod vpřed (forward pass) poskytuje výjimečný výkon při zachování výpočetní efektivity. Optimalizován pro korejštinu s podporou angličtiny a japonštiny.

## Unikátní charakteristiky

Solar Pro 3 využívá architekturu Mixture-of-Experts k dosažení vysokého výkonu srovnatelného s velkými modely, přičemž aktivuje pouze 12B parametrů pro rychlou inferenci. Technicky se odlišuje specifickým doladěním pro asijské jazyky (zejména korejštinu) při zachování silných schopností v angličtině.

## Silné stránky

### Poměr výkon/náklady
Jako bezplatný model (free tier) nabízí bezkonkurenční hodnotu, zejména s ohledem na architekturu MoE s 102B parametry.

### Jazyková specializace
Cílená optimalizace pro korejštinu a japonštinu poskytuje lepší výsledky v těchto regionech než obecné západní modely.

### Efektivita inference
Díky pouze 12B aktivním parametrům na forward pass je model výrazně rychlejší a výpočetně méně náročný než husté (dense) modely podobné velikosti.

## Slabé stránky

### Kontextové okno
Kapacita 128,000 tokenů je v kontextu konkurence z prosince 2025 (běžně 200k až 2M tokenů) podprůměrná.

### Omezené modality
Model je omezen pouze na text-to-text, zatímco konkurenti v podobné třídě (např. Gemini Flash) nabízejí nativní multimodalitu.
