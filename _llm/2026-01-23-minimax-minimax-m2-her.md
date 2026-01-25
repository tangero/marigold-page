---
layout: llm_review
title: "MiniMax: MiniMax M2-her"
date: "2026-01-23 15:07:19"
model_id: minimax/minimax-m2-her
slug: minimax-minimax-m2-her
provider: Minimax
pricing:
  prompt_per_m: 0.3
  completion_per_m: 1.2
context_length: 32,768
max_output: 2,048
input_modalities:
  - text
output_modalities:
  - text
focus:
  - Roleplay a charakterová interakce
  - Emocionální inteligence a konzistence tónu
competitors:
  - provider: MistralAI
    model: Mistral Small Creative
    model_id: mistralai/mistral-small-creative
    price_comparison: Vstup 3x levnější ($0.10), výstup 4x levnější ($0.30)
    comparison: Mistral nabízí stejné kontextové okno (32k) za zlomek ceny a je rovněž laděn na kreativitu, ačkoliv postrádá specifické API funkce pro definici stylu zpráv jako MiniMax.
  - provider: DeepSeek
    model: DeepSeek V3.2
    model_id: deepseek/deepseek-v3.2
    price_comparison: Vstup srovnatelný ($0.25), výstup 3x levnější ($0.38)
    comparison: DeepSeek nabízí 5x větší kontext (163k) a lepší všeobecné schopnosti (reasoning) za nižší cenu, ale nemusí dosahovat stejné kvality v 'lidskosti' dialogu.
  - provider: X-AI
    model: Grok 4.1 Fast
    model_id: x-ai/grok-4.1-fast
    price_comparison: Vstup levnější ($0.20), výstup 2.4x levnější ($0.50)
    comparison: Grok dominuje masivním kontextem (2M), což je klíčové pro dlouhé RP seance, kde MiniMaxu (32k) dojde paměť, přestože MiniMax může mít lepší stylistickou nuanci.
recommendation:
  target_users:
    - Vývojáři chatbotů s osobností (Character AI)
    - Tvůrci interaktivních příběhů
    - Herní studia (NPC dialogy)
  use_cases:
    - Roleplay chatboti vyžadující specifický tón
    - Simulace konverzací s definovanými charaktery
    - Emocionální podpora a společníci
  avoid_for:
    - RAG aplikace vyžadující velký kontext
    - Generování dlouhých textů (nad 2k tokenů)
    - Komplexní logické úlohy a kódování
verdict: MiniMax M2-her je silná volba pro úzce zaměřené aplikace vyžadující vysokou emoční inteligenci a striktní dodržování charakteru, ale pro obecné použití je technicky limitován malým kontextem a vyšší cenou výstupu oproti konkurenci.
analyzer_model: google/gemini-3-pro-preview
analyzed_at: "2026-01-25 07:23"
---

MiniMax M2-her je velký jazykový model, který klade důraz na dialog a je vytvořen pro pohlcující hraní rolí, chat řízený postavami a expresivní vícekolové konverzace. Je navržen tak, aby si udržel konzistentní tón a osobnost, podporuje bohaté role zpráv (user_system, group, sample_message_user, sample_message_ai) a dokáže se učit z ukázkových dialogů, aby lépe odpovídal stylu a tempu vašeho scénáře, což z něj činí silnou volbu pro vyprávění příběhů, společníky a konverzační zážitky, kde nejvíce záleží na přirozeném toku a živé interakci.

## Unikátní charakteristiky

MiniMax M2-her je specializovaný model navržený primárně pro imerzivní roleplay a udržení konzistentní osobnosti v dlouhých konverzacích. Technicky se odlišuje podporou specifických struktur zpráv (sample_message), které umožňují few-shot učení stylu a tempa dialogu přímo v kontextu, což je funkce často chybějící u obecných modelů.

## Silné stránky

### Specializace na Roleplay
Díky podpoře 'sample_message_user' a 'sample_message_ai' dokáže model efektivněji napodobit specifický styl mluvy a formátování než konkurence spoléhající pouze na systémové prompty.

### Konzistence persony
Model je optimalizován tak, aby minimalizoval 'vypadávání z role' (breaking character) během vícekrokových konverzací, což je častý problém u modelů zaměřených na logiku.

## Slabé stránky

### Omezené kontextové okno
S kapacitou 32,768 tokenů výrazně zaostává za standardem roku 2025 (běžně 128k–2M), což limituje jeho paměť pro dlouhodobé příběhy.

### Limit výstupu
Maximální výstup 2,048 tokenů je nedostatečný pro generování delších kapitol nebo rozsáhlých textových bloků v jedné odpovědi.

### Cena výstupu
Cena $1.20 za 1M výstupních tokenů je výrazně vyšší než u srovnatelných 'small' modelů (např. Mistral nebo DeepSeek), které nabízejí výstup pod $0.40.
