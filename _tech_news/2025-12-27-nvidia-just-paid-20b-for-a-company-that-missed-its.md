---
author: Marisa Aigen
category: ai bublina
companies:
- Nvidia
date: '2025-12-27 16:47:13'
description: Panické nákupy, jednoduše řečeno. Pokud něco naznačuje, že bublina AI
  právě praskne, je to toto.
importance: 5
layout: tech_news_article
original_title: Nvidia Just Paid $20B for a Company That Missed Its Revenue Target
  by 75%
publishedAt: '2025-12-27T16:47:13+00:00'
slug: nvidia-just-paid-20b-for-a-company-that-missed-its
source:
  emoji: 📰
  id: null
  name: Drjoshcsimmons.com
title: Nvidia zaplatila 20 miliard dolarů za firmu, která nedosáhla svého cíle v tržbách
  o 75 %
url: https://blog.drjoshcsimmons.com/p/nvidia-just-paid-20-billion-for-a
urlToImage: https://substackcdn.com/image/fetch/$s_!7ppM!,w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a099433-4de1-45a1-9804-cfcede6b28da_5064x2704.png
urlToImageBackup: https://substackcdn.com/image/fetch/$s_!7ppM!,w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a099433-4de1-45a1-9804-cfcede6b28da_5064x2704.png
---

## Souhrn
Nvidia oznámila akvizici společnosti Groq za 20 miliard dolarů, přestože tato firma nedosáhla svého cíle v tržbách o 75 procent. Groq se specializuje na hardware pro rychlé zpracování velkých jazykových modelů (LLM), kde nabízí čipy LPU založené na ASIC, které slibují vyšší rychlost než standardní GPU. Tento krok vyvolává otázky o přehřátém trhu AI.

## Klíčové body
- Nvidia koupila Groq za 20 miliard dolarů navzdory selhání v plnění tržeb o 75 %.
- Groq vyvinula LPU (Language Processing Unit), čip optimalizovaný pro rychlou inferenci LLM.
- LPU využívá SRAM pro rychlejší přístup k datům oproti HBM v GPU od Nvidie.
- Akvizice signalizuje paniku v AI sektoru kvůli soutěži v hardwaru pro AI.
- Groq není xAI Grok – jde o samostatnou firmu zaměřenou na akceleraci AI modelů.

## Podrobnosti
Společnost Groq, založená v roce 2016, se zaměřuje na vývoj hardwaru a softwaru pro urychlení inference velkých jazykových modelů, což je fáze, kdy model generuje odpovědi na požadavky uživatelů. Na rozdíl od tréninkových úloh, kde dominují GPU od Nvidie, je inference klíčová pro reálné nasazení v chatbotech, jako jsou ChatGPT nebo Gemini, kde se počítají s latencemi v řádu sekund. Groq vyřešila tento problém svým LPU, což je aplikace specifický integrovaný obvod (ASIC) navržený výhradně pro zpracování jazykových úloh. Tento čip používá SRAM (statickou paměť s náhodným přístupem), která umožňuje rychlejší čtení dat než HBM (vysokopásmová paměť) v Nvidia GPU. Například při srovnání: GPU musí často přistupovat k externí paměti, což způsobuje zpoždění, zatímco LPU integruje paměť přímo na čipu, což zkracuje latenci na desítky milisekund.

Příklad z praxe: Pokud model jako Claude nebo Llama na GPU odpoví za 2–5 sekund, LPU to zvládne 10–100krát rychleji, což je ideální pro konverzační aplikace nebo real-time systémy, jako jsou hlasoví asistenti. Groq již spolupracuje s poskytovateli LLM a nabízí cloudovou službu pro inference, kde uživatelé nahrají svůj model a spustí ho na LPU. Přesto firma hlásila výrazné podvýkony – cíl tržeb nebyl naplněn o 75 %, což naznačuje problémy se škálovatelností nebo adopcí. Nvidia, která kontroluje 80–90 % trhu s AI hardwarovými akcelerátory, tak platí obrovskou prémií za technologii, která by mohla ohrozit její monopol. Tento nákup následuje za sérií akvizic v AI, ale cena 20 miliard je extrémní, zejména když Groq dosud nedokázala komercializovat svůj potenciál plně. Článek zdůrazňuje rizika: Groq není Elon Muskův Grok z xAI, který je spíše marketingovým nástrojem pro politicky nekorektní odpovědi, ale seriózní hardware hráč.

## Proč je to důležité
Tato akvizice podtrhuje napětí v AI ekosystému, kde Nvidia čelí konkurenci od custom čipů jako LPU, TPU od Google nebo nadcházejících čipů od Amazonu a Microsoftu. Pro průmysl znamená integraci LPU do Nvidia ekosystému potenciální zrychlení inference, což by snížilo náklady na provoz LLM o desítky procent – klíčové pro škálování služeb jako Copilot nebo Perplexity. Pro uživatele to přinese rychlejší odpovědi v aplikacích bez kompromisů na kvalitě. Nicméně vysoká cena a podvýkony Groq signalizují bublinu: investoři pumpují miliardy do nereálných očekávání, což může vést k korekci trhu podobné dot-com krizi. Jako expert vidím riziko, že LPU nebude univerzální jako GPU a zůstane niche řešením. Dlouhodobě to posílí Nvidia dominanci, ale krátkodobě zvyšuje tlak na valuace v AI sektoru.

---

[Číst původní článek](https://blog.drjoshcsimmons.com/p/nvidia-just-paid-20-billion-for-a)

**Zdroj:** 📰 Drjoshcsimmons.com
