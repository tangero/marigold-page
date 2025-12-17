---
layout: llm_review
title: "Xiaomi: MiMo-V2-Flash (free)"
date: "2025-12-14 17:55:08"
model_id: "xiaomi/mimo-v2-flash:free"
slug: xiaomi-mimo-v2-flash-free
provider: Xiaomi
pricing:
  prompt_per_m: 0.0
  completion_per_m: 0.0
context_length: 262,144
max_output: 262,144
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Programování (Coding)
  - Pokročilé uvažování (Reasoning)
  - Agentní systémy
competitors:
  - provider: MistralAI
    model: "devstral-2512:free"
    model_id: "mistralai/devstral-2512:free"
    price_comparison: Identická cena (zdarma) i kontext (262k tokenů).
    comparison: Přímý konkurent v 'free' segmentu pro vývojáře. MiMo-V2-Flash deklaruje vyšší výkon v SWE-bench, zatímco Devstral může být efektivnější pro menší nasazení.
  - provider: Anthropic
    model: claude-sonnet-4.5
    model_id: anthropic/claude-sonnet-4.5
    price_comparison: MiMo je zdarma, Sonnet stojí $3.00/$15.00 za 1M tokenů.
    comparison: Sonnet 4.5 je referenční model kvality, kterému se MiMo snaží vyrovnat. Sonnet má 4x větší kontext (1M) a multimodalitu, ale pro čistý text/kód je MiMo ekonomicky výhodnější alternativou.
  - provider: DeepSeek
    model: deepseek-v3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: MiMo je zdarma, DeepSeek je velmi levný ($0.24/$0.38).
    comparison: Oba modely využívají MoE architekturu. MiMo nabízí větší kontext (262k vs 164k) a je zaměřen specificky na 'agentní' scénáře a kódování.
recommendation:
  target_users:
    - Softwaroví inženýři
    - Výzkumníci AI
    - Startupy s omezeným rozpočtem
  use_cases:
    - Automatizované opravy chyb (SWE-bench scénáře)
    - Generování složitého kódu
    - Analýza rozsáhlé textové dokumentace
  avoid_for:
    - Úlohy vyžadující analýzu obrázků nebo grafů
    - Lokální nasazení na běžném spotřebitelském hardwaru (kvůli 309B parametrům)
verdict: Vynikající volba pro náročné úlohy kódování a uvažování, kde je prioritou nulová cena a vysoká kvalita výstupu, a není vyžadována multimodalita.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2025-12-17 07:23"
---

MiMo-V2-Flash je open-source základový jazykový model vyvinutý společností Xiaomi. Jedná se o model typu Mixture-of-Experts s celkovým počtem 309 miliard parametrů a 15 miliardami aktivních parametrů, využívající hybridní architekturu pozornosti. MiMo-V2-Flash podporuje přepínač hybridního myšlení a kontextové okno o velikosti 256K a vyniká v úlohách vyžadujících usuzování, kódování a v agentních scénářích. Na SWE-bench Verified a SWE-bench Multilingual se MiMo-V2-Flash řadí na 1. místo mezi open-source modely globálně a dosahuje výkonu srovnatelného s Claude Sonnet 4.5, přičemž jeho náklady jsou pouze zhruba 3,5 %.

## Unikátní charakteristiky

MiMo-V2-Flash je masivní MoE model s 309 miliardami parametrů, který díky aktivaci pouze 15 miliard parametrů na token dosahuje vysoké efektivity inference. Využívá hybridní architekturu pozornosti a funkci 'hybrid-thinking toggle', což mu umožňuje dosahovat výsledků srovnatelných s Claude Sonnet 4.5 v úlohách softwarového inženýrství.

## Silné stránky

### Výkon v kódování
Hodnocen jako #1 open-source model na SWE-bench Verified a Multilingual, srovnatelný s proprietární špičkou.

### Ekonomická efektivita
Model je nabízen zdarma ($0.00), což představuje bezkonkurenční poměr cena/výkon oproti modelům jako Claude Sonnet 4.5.

### Kontextové okno
Kapacita 262,144 tokenů je dostatečná pro zpracování rozsáhlých repozitářů kódu nebo dlouhých dokumentů.

## Slabé stránky

### Hardwarové nároky na paměť
Ačkoliv je inference efektivní (15B aktivních), celková velikost 309B parametrů vyžaduje enormní VRAM pro načtení modelu při vlastním hostování.

### Omezené modality
Model je pouze text-to-text, chybí mu schopnost zpracování obrazu, kterou disponují konkurenti jako Gemini nebo Claude.
