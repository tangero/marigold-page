---
author: Marisa Aigen
category: ai
date: '2025-11-10 23:06:42'
description: Nová studie startupu Goodfire.ai ukazuje, že velké jazykové modely mají
  zřetelně oddělené neuronové komponenty pro doslovné memorování tréninkových dat
  a pro logické uvažování, což otevírá cestu k přesnějšímu řízení chování AI.
importance: 3
layout: tech_news_article
original_title: Researchers isolate memorization from reasoning in AI neural networks
  - Ars Technica
publishedAt: '2025-11-10T23:06:42+00:00'
slug: researchers-isolate-memorization-from-reasoning-in
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: Výzkum naznačuje oddělené dráhy pro memorování a uvažování v AI modelech
url: https://arstechnica.com/ai/2025/11/study-finds-ai-models-store-memories-and-logic-in-different-neural-regions/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/07/surprised_robot_2-1152x648.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/07/surprised_robot_2-1152x648.jpg
---

## Souhrn
Výzkumníci z Goodfire.ai předložili experimentální důkazy, že velké jazykové modely (LLM) mají výrazně oddělené neuronové dráhy pro memorování tréninkových dat a pro obecné uvažování. Ukazují, že selektivním zásahem do těchto drah lze dramaticky omezit schopnost modelu citovat tréninková data, aniž by se podstatně zhoršil jeho výkon v úlohách vyžadujících logické myšlení a zobecnění.

## Klíčové body
- Oddělené „memorizační“ a „logické“ komponenty byly identifikovány v interní struktuře LLM.
- Odstranění memorizačních cest snížilo schopnost přesného citování tréninkových dat o cca 97 %, při zachování téměř nezměněného výkonu v úlohách uvažování.
- Analýza byla demonstrována na modelu OLMo-7B (Allen Institute for AI) pomocí metriky označené jako „curvature“ k seřazení vah.
- Komponenty spojené s memorováním se koncentrovaly ve spodní části žebříčku vah, komponenty pro zobecnění a řešení úloh naopak v horní části.
- Zjištění naznačují, že i základní aritmetika je v těchto modelech částečně obsluhována „memorizačními“ drahami, nikoli čistě abstraktním „logickým“ modulem.

## Podrobnosti
Studie Goodfire.ai, menšího výzkumného startupu zaměřeného na interpretovatelnost a bezpečnost AI modelů, se soustředí na mechanistickou analýzu vnitřní struktury velkých jazykových modelů. Na příkladu OLMo-7B, otevřeného modelu vyvinutého Allen Institute for AI, autoři hodnotili jednotlivé váhové komponenty v konkrétních vrstvách modelu podle metriky nazývané „curvature“. Tato metrika měří, jak citlivě daná komponenta reaguje na změny v datech a jak se podílí na nelineárním chování modelu.

Při porovnání aktivačních vzorců na datech, která byla součástí tréninku, a na nových, netréninkových textech se ukázalo, že spodních 50 % komponent v dané vrstvě vykazuje významně vyšší aktivaci na memorovaných pasážích. Naopak horní část žebříčku, přibližně 10 % komponent s nejvyšší „curvature“, se více aktivuje na obecný text a úlohy vyžadující zobecnění. Prakticky to umožnilo „chirurgický“ zásah: odstraněním komponent identifikovaných jako memorizační autoři dramaticky omezili schopnost modelu doslovně reprodukovat tréninková data, ale výkon v úlohách uvažování, porozumění textu a řešení nových úloh zůstal téměř zachován.

Zajímavým a potenciálně kontroverzním zjištěním je, že i aritmetické schopnosti modelu, jako jsou jednoduché výpočty, jsou částečně realizovány přes stejné dráhy, které nesou memorizační chování. To naznačuje, že pro některé typy úloh, které vnímáme jako „logické“, model ve skutečnosti využívá komplexní statistické a paměťové vzorce namísto odděleného, obecného mechanismu uvažování. Studie je ve formátu preprintu a výsledky zatím nejsou nezávisle široce replikovány, ale zapadají do rostoucího trendu mechanistické interpretovatelnosti, který se snaží převést chování AI z černé skříňky na analyzovatelnou infrastrukturu.

## Proč je to důležité
Pokud se tyto výsledky potvrdí, mohou mít přímý dopad na několik oblastí. Pro poskytovatele LLM by možnost cíleně omezit memorování znamenala lepší kontrolu nad únikem citlivých nebo autorsky chráněných tréninkových dat, což je zásadní pro právní a reputační rizika. Pro regulátory a firmy nasazující AI systémy by šlo o konkrétní technický nástroj, jak sladit výkonnost modelů s požadavky na ochranu dat.

Z hlediska výzkumu bezpečnosti a alignmentu AI je existence oddělitelných drah pro různé typy chování klíčová. Umožňuje navrhovat zásahy, které nepoškozují celkovou užitečnost systému, ale cílí na konkrétní rizikové projevy (memorování, toxický obsah, specifické prompt injection vzory). Zároveň je nutná opatrnost: odstranění memorizačních komponent může oslabit některé užitečné schopnosti, jako je přesná citace, znalost vzácných faktů nebo spolehlivější aritmetika. Tento výzkum proto není receptem na jednoduché „opravy“ AI, ale spíše počátkem systematičtějšího, jemně odstupňovaného řízení chování modelů na úrovni jejich interní architektury.

---

[Číst původní článek](https://arstechnica.com/ai/2025/11/study-finds-ai-models-store-memories-and-logic-in-different-neural-regions/)

**Zdroj:** 🔬 Ars Technica
