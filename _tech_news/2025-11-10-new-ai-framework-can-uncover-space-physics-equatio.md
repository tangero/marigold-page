---
author: Marisa Aigen
category: ai
date: '2025-11-10 12:00:01'
description: Výzkumníci z Tsinghua University a Peking University představili framework
  PhyE2E, který kombinuje generativní modely, symbolickou regresi a fyzikální omezení
  k automatickému odvozování fyzikálních rovnic přímo z dat vesmírných měření.
importance: 3
layout: tech_news_article
original_title: New AI framework can uncover space physics equations in raw data -
  Phys.org
publishedAt: '2025-11-10T12:00:01+00:00'
slug: new-ai-framework-can-uncover-space-physics-equatio
source:
  emoji: 📰
  id: null
  name: Phys.Org
title: Nový AI framework automaticky odhaluje fyzikální rovnice z kosmických dat
url: https://phys.org/news/2025-11-ai-framework-uncover-space-physics.html
urlToImage: https://scx2.b-cdn.net/gfx/news/hires/2025/new-ai-framework-can-u.jpg
urlToImageBackup: https://scx2.b-cdn.net/gfx/news/hires/2025/new-ai-framework-can-u.jpg
---

## Souhrn
Nový AI framework PhyE2E umožňuje automaticky odvozovat fyzikální rovnice z neuspořádaných měření kosmických jevů bez nutnosti ručního modelování. Systém kombinuje generovaná syntetická data, symbolickou regresi a fyzikální omezení a míří na oblast, kde běžné neuronové sítě fungují jako „černé skříňky“ bez srozumitelné matematiky.

## Klíčové body
- PhyE2E převádí syrová měření (např. z družic) na symbolické rovnice, které jsou lidsky čitelné a fyzikálně konzistentní.
- Framework využívá velký jazykový model (LLM) pro generování syntetických tréninkových dat, čímž rozšiřuje pokrytí možných fyzikálních vztahů.
- Používá techniku dekompozice problému na menší subproblémy (D&C) a end-to-end model pro návrh kandidátních rovnic.
- Nasazuje modul Monte Carlo Tree Search (MCTS) s bezkontextovou gramatikou k dolaďování rovnic na základě přesnosti (RMSE) a fyzikálních omezení.
- Cílí na oblast prostorové fyziky, ale koncept lze přenést i do plazmové fyziky, astrofyziky a dalších datově bohatých oborů.

## Podrobnosti
Framework PhyE2E vyvinutý týmem z Tsinghua University, Peking University a spolupracujících čínských institucí řeší dlouhodobý problém fyziky a inženýrství: jak přejít od velkých objemů experimentálních dat k explicitním rovnicím, které lze ověřit, sdílet a použít v simulačních modelech. Na rozdíl od klasických neuronových sítí, které pouze aproximují vztahy mezi vstupem a výstupem, se PhyE2E snaží rekonstruovat symbolické matematické výrazy.

Architektura stojí na několika krocích. Nejprve je tréninková množina rozšířena syntetickými daty generovanými pomocí LLM, který navrhuje možné fyzikální vztahy a z nich odvozené datové body. Tím se řeší problém omezeného množství reálných měření v některých oblastech kosmické fyziky a zároveň se systém učí rozmanější prostor rovnic. Následně je úloha symbolické regrese rozdělena technikou "divide and conquer" (D&C) na jednodušší dílčí vztahy mezi proměnnými. End-to-end model, typicky založený na MLP (multilayer perceptron), pak z pozorovaných dat a fyzikálních priorů (například zákonů zachování, známých konstant, struktur rovnic) generuje kandidátní formuli.

Poslední krok využívá Monte Carlo Tree Search (MCTS) a bezkontextovou gramatiku, v níž jsou definovány „atomické“ výrazy a operace. MCTS prohledává prostor možných rovnic, porovnává je s daty pomocí metrik, jako je RMSE, a průběžně respektuje fyzikální omezení, aby se minimalizovaly nesmyslné výsledky. Výsledkem jsou rovnice, které nejen dobře sedí na data, ale zároveň odpovídají známým fyzikálním principům nebo navrhují jejich rozšíření.

Pro vědeckou komunitu jde o praktický nástroj: lze jej nasadit na data z družic studujících magnetosféru, sluneční vítr, plazmové interakce či kosmické záření a systematicky hledat nové vztahy bez ručně vedeného „lovu“ v datech. Pro průmysl (aerospace, energetika, materiálové inženýrství) to otevírá cestu k rychlejšímu návrhu fyzikálních modelů, které jsou transparentní a přímo použitelné v simulačním softwaru.

## Proč je to důležité
PhyE2E představuje posun od černoskrínkových AI modelů k nástrojům, které generují srozumitelnou a ověřitelnou matematiku. To je klíčové ve vědě, kde nestačí predikce, ale je nutná interpretace a fyzikální konzistence. Zapojení LLM do generování tréninkových dat zároveň ukazuje trend: spojování generativních modelů, symbolické regrese a fyzikálních priorů pro automatizovaný vědecký objev. Pokud se framework osvědčí mimo kosmickou fyziku, může zrychlit vývoj modelů v plazmové energetice, fúzních reaktorech, klimatických simulacích i materiálovém výzkumu. Zároveň je nutné kriticky sledovat rizika: syntetická data i návrhy rovnic mohou vnášet systematické chyby, proto bude klíčová nezávislá validace a otevřené porovnání s klasickými metodami a experimenty.

---

[Číst původní článek](https://phys.org/news/2025-11-ai-framework-uncover-space-physics.html)

**Zdroj:** 📰 Phys.Org
