---
layout: llm_review
title: "Meta: Llama Guard 4 12B"
date: "2025-04-30 03:06:33"
model_id: meta-llama/llama-guard-4-12b
slug: meta-llama-llama-guard-4-12b
provider: Meta
pricing:
  prompt_per_m: 0.18
  completion_per_m: 0.18
  blend_per_m: 0.18
context_length: 163,840
max_output: N/A
input_modalities:
  - image
  - text
output_modalities:
  - text
focus:
  - Bezpečnost obsahu
  - Multimodální moderace
strengths:
  - area: Bezpečnost obsahu
    description: Specializuje se na detekci nebezpečného obsahu v textu a obrázcích, což je klíčové pro bezpečné nasazení LLM.
  - area: Multimodálnost
    description: Podporuje kombinaci textových a obrazových vstupů, což rozšiřuje možnosti moderování obsahu.
weaknesses:
  - area: Nedostatek benchmarků
    description: Chybí veřejně dostupné benchmarky, takže nelze objektivně porovnat jeho výkon s konkurencí.
  - area: Obecné LLM schopnosti
    description: Není určen pro generování obsahu, ale pro jeho moderování, takže jeho obecné LLM schopnosti jsou omezené.
competitors:
  - provider: GOOGLE
    model: google/gemini-2.5-flash-image
    model_id: google/gemini-2.5-flash-image
    price_comparison: 1.6x dražší vstup, 13.8x dražší výstup
    comparison: Gemini 2.5 Flash Image je multimodální model, ale jeho primární zaměření je širší než jen bezpečnost obsahu.
  - provider: ANTHROPIC
    model: anthropic/claude-haiku-4.5
    model_id: anthropic/claude-haiku-4.5
    price_comparison: 5.5x dražší vstup, 27.7x dražší výstup
    comparison: Claude Haiku 4.5 je rychlejší a levnější pro obecné účely, ale nemá specializaci na bezpečnost obsahu.
  - provider: MISTRALAI
    model: mistralai/ministral-3b-2512
    model_id: mistralai/ministral-3b-2512
    price_comparison: 1.8x levnější vstup, 1.8x levnější výstup
    comparison: Ministral 3B je levnější, ale není specializovaný na bezpečnost obsahu a nemá multimodální schopnosti.
  - provider: DEEPSEEK
    model: deepseek/deepseek-v3.2-exp
    model_id: deepseek/deepseek-v3.2-exp
    price_comparison: 1.16x dražší vstup, 1.77x dražší výstup
    comparison: Deepseek V3.2 EXP je model pro obecné účely, nemá specializaci na bezpečnost obsahu a nemá multimodální schopnosti.
recommendation:
  target_users:
    - Vývojáři LLM aplikací
    - Platformy pro sdílení obsahu
  use_cases:
    - Moderování uživatelského obsahu
    - Filtrování nebezpečných vstupů a výstupů LLM
  avoid_for:
    - Generování kreativního obsahu
    - Úkoly vyžadující hluboké porozumění jazyku
verdict: Llama Guard 4 je užitečný nástroj pro vývojáře, kteří potřebují moderovat obsah generovaný LLM, zejména v multimodálních aplikacích. Chybějící benchmarky ale ztěžují objektivní srovnání s konkurencí.
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
  killer_feature: Specializace na bezpečnost obsahu a multimodální moderace.
  hidden_risk: Závislost na kvalitě trénovacích dat pro detekci nebezpečného obsahu.
  recommended_use_case: Automatické filtrování nebezpečných obrázků a textů na sociálních sítích.
analyzer_model: google/gemini-2.0-flash-001
analyzed_at: "2025-12-09 13:04"
---

Llama Guard 4 je multimodální předtrénovaný model odvozený od Llama 4 Scout, jemně doladěný pro klasifikaci obsahu z hlediska bezpečnosti. Podobně jako předchozí verze, může být použit ke klasifikaci obsahu jak ve vstupech LLM (klasifikace promptu), tak v odpovědích LLM (klasifikace odpovědi). Funguje jako LLM – generuje text ve svém výstupu, který indikuje, zda je daný prompt nebo odpověď bezpečný nebo nebezpečný, a pokud je nebezpečný, také vypisuje kategorie obsahu, které byly porušeny.

Llama Guard 4 byl vyladěn tak, aby chránil proti standardizované taxonomii rizik MLCommons a byl navržen tak, aby podporoval multimodální schopnosti Llama 4. Konkrétně kombinuje funkce z předchozích modelů Llama Guard, poskytuje moderování obsahu pro angličtinu a více podporovaných jazyků, spolu s vylepšenými schopnostmi pro zpracování smíšených textově-obrazových promptů, včetně více obrázků. Kromě toho je Llama Guard 4 integrován do Llama Moderations API, čímž rozšiřuje robustní klasifikaci bezpečnosti na text a obrázky.

## Unikátní charakteristiky

Llama Guard 4 je model pro klasifikaci bezpečnosti obsahu, který podporuje multimodální vstupy (text a obrázky). Je navržen pro moderování obsahu v LLM vstupech a výstupech. Benchmark data nejsou k dispozici, takže nelze přesně určit jeho výkon.

## Silné stránky

### Bezpečnost obsahu
Specializuje se na detekci nebezpečného obsahu v textu a obrázcích, což je klíčové pro bezpečné nasazení LLM.

### Multimodálnost
Podporuje kombinaci textových a obrazových vstupů, což rozšiřuje možnosti moderování obsahu.

## Slabé stránky

### Nedostatek benchmarků
Chybí veřejně dostupné benchmarky, takže nelze objektivně porovnat jeho výkon s konkurencí.

### Obecné LLM schopnosti
Není určen pro generování obsahu, ale pro jeho moderování, takže jeho obecné LLM schopnosti jsou omezené.
