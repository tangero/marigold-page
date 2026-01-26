---
author: Marisa Aigen
category: startupy
companies:
- Inferact Inc
- Andreessen Horowitz
- Lightspeed
date: '2026-01-23 01:13:45'
description: Skupina výzkumníků v umělé inteligenci spustila startup Inferact Inc.,
  který bude komercializovat open-source projekt vLLM pro optimalizaci inference velkých
  jazykových modelů. Financování seed kola činí 150 milionů dolarů s oceňováním společnosti
  800 milionů dolarů.
importance: 4
layout: tech_news_article
original_title: Inferact launches with $150M in funding to commercialize vLLM
publishedAt: '2026-01-23T01:13:45+00:00'
slug: inferact-launches-with-150m-in-funding-to-commerci
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: Inferact spouští s 150 miliony dolarů financování na komercializaci vLLM
url: https://siliconangle.com/2026/01/22/inferact-launches-150m-funding-commercialize-vllm/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2026/01/AI.png
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2026/01/AI.png
---

## Souhrn
Skupina výzkumníků z University of California at Berkeley spustila startup Inferact Inc., který plánuje komercializovat open-source projekt vLLM. Tento nástroj slouží k urychlení inference u velkých jazykových modelů (LLM) prostřednictvím optimalizací paměti a výkonu. Společnost získala 150 milionů dolarů v seed kole vedeném investory Andreessen Horowitz a Lightspeed, s oceňováním 800 milionů dolarů.

## Klíčové body
- Založení Inferact Inc. týmem včetně Iona Stoicu, spoluzakladatele Databricks a ředitele Sky Computing Lab na UC Berkeley.
- vLLM je open-source knihovna vyvinutá v roce 2023, nyní s přes 2000 přispěvateli, která optimalizuje inference LLM snížením spotřeby paměti a zrychlením generování odpovědí.
- Klíčová funkce PagedAttention umožňuje ukládat KV cache v nepřipojených částech RAM, což minimalizuje plýtvání pamětí.
- Další optimalizace zahrnují kvantizaci vah modelů pro zmenšení paměťové stopy.
- Investoři: Andreessen Horowitz, Lightspeed, Databricks Ventures, UC Berkeley Chancellor’s Fund.

## Podrobnosti
Inferact Inc. vznikl za účelem převodu open-source projektu vLLM do komerčního produktu. vLLM je knihovna určená pro softwarové týmy, které potřebují zpracovávat inference úlohy u velkých jazykových modelů rychleji a efektivněji. Když LLM obdrží výzvu (prompt), provádí výpočty po částech: nejprve malou porci, uloží výsledky do KV cache (klíč-hodnota cache, která uchovává intermediární stavy pro autoregresivní generování), poté pokračuje další porcí a aktualizuje cache, dokud nevygeneruje kompletní odpověď. Tento proces vyžaduje značné množství paměti, protože KV cache roste s délkou kontextu.

Hlavní inovace vLLM spočívá v PagedAttention, které ukládá data KV cache do nepřipojených sekcí serverové RAM, podobně jako paging v operačních systémech. To eliminuje fragmentaci paměti, kdy jsou bloky paměti rozházené a nevyužité mezery způsobují plýtvání. Výsledkem je výrazné snížení paměťové spotřeby, což umožňuje spouštět větší modely na méně hardwaru, například na méně GPU. Navíc vLLM aplikuje kvantizaci, metodu komprese vah modelu, která zmenšuje jejich velikost bez výrazné ztráty přesnosti – například převodem vah z 16bitového na 8bitový nebo nižší formát.

Kromě úspor paměti vLLM zvyšuje i rychlost inference. Standardní LLM generují odpovědi token po tokenu, což je sekvenční proces; vLLM ho optimalizuje pro vyšší propustnost (throughput), což je klíčové pro nasazení v produkci, jako chatbotech nebo API službách. Projekt byl původně vyvinut v Sky Computing Lab na UC Berkeley pod vedením Iona Stoicu, který je profesorem informatiky, spoluzakladatelem Databricks (společnost zaměřená na big data a AI platformy) a má zkušenosti s distribuovanými systémy. Od roku 2023 se k vývoji přidalo přes 2000 vývojářů, což ukazuje na širokou komunitní podporu.

Seed kolo ve výši 150 milionů dolarů vedli Andreessen Horowitz (a16z, známý venture fond zaměřený na tech a AI) a Lightspeed Venture Partners, s účastí Databricks Ventures, fondu UC Berkeley Chancellor’s Fund a dalších. Oceňování na 800 milionů dolarů signalizuje vysoké očekávání od investorů v oblasti AI infrastruktury. Inferact plánuje rozšířit vLLM do plnohodnotné komerční platformy, pravděpodobně s podporou, škálovatelností a integracemi pro enterprise zákazníky.

## Proč je to důležité
Tato komercializace vLLM nastavuje trend v AI ekosystému, kde open-source projekty jako Llama nebo Mistral přecházejí do placených služeb, což zvyšuje dostupnost efektivní inference, ale zároveň riskuje fragmentaci komunity. Pro průmysl znamená nižší náklady na hardware – inference tvoří většinu provozních výdajů u LLM služeb – a umožňuje škálovat aplikace jako RAG systémy nebo real-time chaty. V kontextu rostoucí poptávky po GPU (např. od Nvidia) pomáhá vLLM snižovat závislost na hardwaru, což je kritické pro menší firmy. Nicméně jako expert upozorňuji, že komercializace může omezit volný vývoj, pokud Inferact zavede uzavřené funkce, a konkurence od TensorRT-LLM nebo Hugging Face TGI zůstává silná. Celkově posiluje to pozici Berkeley jako centra AI výzkumu a urychluje adopci efektivních inference nástrojů.

---

[Číst původní článek](https://siliconangle.com/2026/01/22/inferact-launches-150m-funding-commercialize-vllm/)

**Zdroj:** 📰 SiliconANGLE News
