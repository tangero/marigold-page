---
author: Marisa Aigen
category: kvantové počítače
companies:
- Classiq
- Comcast
- AMD
date: '2026-02-17 12:00:10'
description: Startup Classiq Technologies oznámil partnerství s telekomunikačním gigantem
  Comcast a výrobcem čipů AMD, které demonstruje, jak kvantové algoritmy výrazně zlepšují
  odolnost sítí. Test řeší optimalizaci nezávislých cest pro přesměrování provozu
  při současném výpadku primárního i záložního uzlu.
importance: 5
layout: tech_news_article
original_title: Quantum algorithms enhance network resilience in Classiq, Comcast,
  AMD trial
publishedAt: '2026-02-17T12:00:10+00:00'
slug: quantum-algorithms-enhance-network-resilience-in-c
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: Kvantové algoritmy zvyšují odolnost sítí v experimentu Classiq, Comcast a AMD
url: https://siliconangle.com/2026/02/17/quantum-algorithms-enhance-network-resilience-classiq-comcast-amd-trial/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2026/02/Screenshot-from-2026-02-16-09-01-30.png
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2026/02/Screenshot-from-2026-02-16-09-01-30.png
---

## Souhrn
Startup Classiq Technologies, specializující se na software pro kvantové počítače, provedl experiment s Comcast a AMD. Kvantové algoritmy umožnily rychle identifikovat optimální nezávislé cesty v síti při výpadcích uzlů, což zlepšuje odolnost telekomunikačních sítí a minimalizuje výpadky internetu. Tento trial ukazuje praktické využití kvantových výpočtů v optimalizačních úkolech s exponenciálně rostoucím kombinatorickým prostorem.

## Klíčové body
- Partnerství Classiq (kvantový software), Comcast (telekomunikační sítě) a AMD (hardware pro výpočty) testuje kvantové algoritmy na reálném problému síťové odolnosti.
- Řeší scénář, kdy primární uzel i hlavní záloha selžou, vyžaduje rychlé nalezení nízkolatentních, resilientních cest.
- Tradiční procesory selhávají kvůli časové složitosti; kvantové algoritmy zvládají exponenciální růst možností efektivněji.
- Experiment popisován jako průlomový trial pro real-time síťovou správu.
- Aktualizováno 17. února 2026.

## Podrobnosti
Classiq Technologies je izraelský startup zaměřený na platformu pro návrh a optimalizaci kvantových algoritmů, která umožňuje inženýrům snadno vytvářet kvantové obvody bez hlubokých znalostí kvantové fyziky. V tomto experimentu spolupracoval s Comcast, jedním z největších poskytovatelů internetu v USA s sítěmi pokrývajícími miliony zákazníků, a AMD, výrobcem výkonových procesorů a grafických karet, který nedávno rozšiřuje svou nabídku o nástroje pro kvantové simulace.

Problém, který řeší, je typický pro moderní sítě: při plánované údržbě primárního uzlu (např. datového centra) a neočekávaném selhání záložního musí operátoři okamžitě přesměrovat provoz na alternativní cestu. Tato cesta musí být nezávislá na selhaných spojích, rychlá (nízká latence), resilientní vůči dalším výpadkům a optimalizovaná pro minimální zpoždění. V sítích s desítkami nebo stovkami uzlů počet možných cest roste exponenciálně – například v grafu se 20 uzly může počet Hamiltonianových cest blížit miliardám kombinací. Tradiční klasické počítače, i na bázi GPU od AMD, musí tyto varianty enumerovat a porovnávat, což trvá minuty až hodiny, což je v real-time správě nepřijatelné.

Kvantové algoritmy, jako varianty Groverova algoritmu nebo QAOA (Quantum Approximate Optimization Algorithm), využívají superpozici a provázanost kvantových bitů (qubitů) k prohledávání obrovského prostoru paralelně. V tomto trialu Classiq navrhl algoritmus, který identifikuje optimální cesty rychleji než klasické metody, simulovaně nebo na malém kvantovém hardware. Comcast tak může testovat scénáře s reálnými daty ze svých sítí, kde výpadky uzlů způsobují ztráty v řádech milionů dolarů za hodinu. AMD poskytuje výpočetní podporu, pravděpodobně prostřednictvím svých simulátorů kvantových systémů, které emulují chování qubitů na klasickém hardware. Tento přístup není ještě plným quantum advantage (kde kvantový hardware překonává klasický v praktickém čase), ale ukazuje škálovatelnost pro budoucí NISQ (Noisy Intermediate-Scale Quantum) éru.

## Proč je to důležité
Tento experiment demonstruje první praktickou aplikaci kvantových algoritmů v telekomunikačních sítích, kde optimalizace cest spadá do NP-těžkých problémů, jako je traveling salesman problem nebo max-flow min-cut. Pro průmysl znamená potenciál nulových výpadků v 5G/6G sítích, kde latence pod 1 ms je klíčová pro autonomní vozidla nebo IoT. V širším kontextu posiluje kvantové počítače jako nástroj pro kombinatorickou optimalizaci v logistice, financiích či energetice. Partnerství s Comcast a AMD signalizuje komercializaci – Classiqova platforma slouží k generování kvantového kódu pro hardware od IBM, IonQ či Rigetti. Pokud se quantum advantage potvrdí na větších systémech (50+ qubitů), změní to real-time síťovou architekturu, sníží náklady na redundanci a zvýší spolehlivost internetu pro miliardy uživatelů. Zatím jde o proof-of-concept, ale s daty z 2026 naznačuje urychlený pokrok v praktických nasazeních.

---

[Číst původní článek](https://siliconangle.com/2026/02/17/quantum-algorithms-enhance-network-resilience-classiq-comcast-amd-trial/)

**Zdroj:** 📰 SiliconANGLE News
