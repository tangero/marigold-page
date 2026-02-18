---
author: Marisa Aigen
category: kvantové výpočty
companies:
- Comcast
- Classiq
- AMD
date: '2026-02-17 16:14:47'
description: Classiq, Comcast a AMD dokončily společnou zkoušku, která využívá kvantové
  algoritmy k zlepšení odolnosti směrování sítě. Cílem je zajistit plynulé přesměrování
  provozu i při současném výpadku více uzlů během údržby.
importance: 5
layout: tech_news_article
original_title: (PR) Comcast, Classiq and AMD Demonstrate Quantum Algorithm for More
  Resilient and Reliable Internet
publishedAt: '2026-02-17T16:14:47+00:00'
slug: pr-comcast-classiq-and-amd-demonstrate-quantum-alg
source:
  emoji: 📰
  id: null
  name: Techpowerup.com
title: Comcast, Classiq a AMD demonstrovaly kvantový algoritmus pro odolnější a spolehlivější
  internet
url: https://www.techpowerup.com/346472/comcast-classiq-and-amd-demonstrate-quantum-algorithm-for-more-resilient-and-reliable-internet
urlToImage: https://www.techpowerup.com/img/lIkpsw4iUGd51P1p.jpg
urlToImageBackup: https://www.techpowerup.com/img/lIkpsw4iUGd51P1p.jpg
---

## Souhrn
Společnosti Comcast, Classiq a AMD úspěšně dokončily zkoušku kvantového algoritmu, který řeší problém nalezení nezávislých záložních cest v síti během údržby. Algoritmus kombinuje kvantové výpočty s výkonnými klasickými počítači a umožňuje real-time optimalizaci směrování, což zvyšuje spolehlivost internetového provozu pro miliony uživatelů.

## Klíčové body
- Zkouška se zaměřila na identifikaci unikátních záložních cest pro síťové uzly, aby výpadek jednoho uzlu během údržby druhého nespôsobil přerušení provozu.
- Použití kvantových technik vedle klasických výpočtů pro řešení NP-těžkých problémů optimalizace sítě.
- Classiq poskytl software pro kvantové algoritmy, AMD hardware a Comcast reálná síťová data.
- Výsledky ukazují praktičnost a škálovatelnost pro velké sítě.
- Zkouška proběhla v únoru 2026 a potvrzuje přechod od teorie k praxi v kvantových aplikacích.

## Podrobnosti
Classiq je izraelská firma specializující se na software pro kvantové výpočty, který umožňuje vývoj algoritmů bez nutnosti hlubokých znalostí kvantové fyziky. Jejich platforma automaticky generuje kvantové obvody pro složité úlohy, jako je optimalizace grafů. V této zkoušce spolupracovala s Comcastem, jedním z největších amerických poskytovatelů internetu s sítí pokrývající desítky milionů domácností, a AMD, výrobcem čipů včetně kvantově kompatibilních procesorů.

Problém, který řešily, je klasický v telekomunikačních sítích: při plánované údržbě jednoho uzlu (např. směrovače nebo switch) musí operátoři najít záložní cesty pro provoz, které jsou rychlé, s nízkou latencí a odolné vůči současnému selhání jiného uzlu. S rostoucí velikostí sítě (miliony spojů) se tento úkol stává exponenciálně náročným pro klasické počítače, protože vyžaduje prohledávání obrovského počtu možností – typický příklad NP-kompletního problému disjunktních cest v grafové teorii.

Zkouška aplikovala kvantové algoritmy, jako varianty quantum approximate optimization algorithm (QAOA) nebo Groverova algoritmu pro rychlejší hledání, na reálných datech z Comcastovy sítě. Tyto algoritmy běžely na hybridní platformě: kvantové části na simulátorech nebo skutečném hardwaru AMD, klasická optimalizace na vysokovýkonných serverech. Výsledek? Algoritmus identifikoval optimální záložní cesty v reálném čase i pro velké topologie sítě, kde klasické metody selhaly kvůli časové složitosti.

Elad Nafshi, šéf síťové divize Comcastu, zdůraznil, že zkouška začala minulý rok a potvrdila praktickou použitelnost. Nešlo o pouhou simulaci, ale o testy v reálných scénářích změn managementu sítě, kde se měřila latence, odolnost vůči selháním a škálovatelnost.

## Proč je to důležité
Tato demonstrace představuje jeden z prvních případů quantum advantage v průmyslové aplikaci mimo laboratoř. Telekomunikační sítě čelí rostoucímu provozu (5G, IoT, cloud), kde výpadky stojí miliardy – např. outage Facebooku v roce 2021 způsobil ztráty 100 milionů dolarů za hodinu. Kvantové algoritmy umožňují řešit optimalizaci, kterou klasické systémy zvládnou jen aproximacemi, což vede k lepší odolnosti a nižší latenci pro koncové uživatele.

V širším kontextu urychluje to adopci kvantových technologií: Classiqův software usnadňuje vývojářům tvorbu algoritmů, AMD posiluje svou pozici v quantum hardwaru a Comcast může integrovat tyto nástroje do svého network managementu. Nicméně jako expert upozorňuji, že jde o trial – plné nasazení vyžaduje stabilní kvantové hardware bez chyb (error rates pod 10^-3) a hybridní systémy. Přesto to signalizuje přechod kvantových výpočtů do produkce, podobně jako u finančních optimalizací u JPMorgan. Pro průmysl to znamená potenciál snížení výpadků o desítky procent a nové standardy v síťové bezpečnosti.

---

[Číst původní článek](https://www.techpowerup.com/346472/comcast-classiq-and-amd-demonstrate-quantum-algorithm-for-more-resilient-and-reliable-internet)

**Zdroj:** 📰 Techpowerup.com
