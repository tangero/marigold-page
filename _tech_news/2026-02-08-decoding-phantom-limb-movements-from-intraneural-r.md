---
author: Marisa Aigen
category: neurotechnologie
date: '2026-02-08 00:00:00'
description: Výzkumníci zaznamenali intraneurální aktivitu sciatického nervu u pacientů
  s amputací nad kolenem a pomocí spiking neural network dekódovali voliční pohyby
  fantomové nohy. Tento přístup překonal konvenční metody a ukázal separaci motorických
  a senzorických signálů v nervu, což otevírá cestu k obousměrným neuronálním rozhraním
  pro protézy.
importance: 4
layout: tech_news_article
original_title: Decoding phantom limb movements from intraneural recordings
publishedAt: '2026-02-08T00:00:00+00:00'
slug: decoding-phantom-limb-movements-from-intraneural-r
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Dekódování pohybů fantomové končetiny z intraneurálních nahrávek
url: https://www.nature.com/articles/s41467-026-69297-0
---

## Souhrn
Výzkum popisuje intraneurální nahrávky z distálních větví sciatického nervu u dvou pacientů s transfemorální amputací, kde byly implantovány transversal intrafascicular multichannel electrodes. Tyto elektrody zachytily multiunit activity spojenou s pohyby fantomové nohy, jako je ohnutí kolene, kotníku nebo prstů na noze. Spiking neural network sloužící k dekódování těchto signálů překonal tradiční metody a dosáhl lepší přesnosti při predikci zamýšlených pohybů.

## Klíčové body
- Identifikace multiunit activity specifické pro klouby (koleno, kotník, prsty) a směr pohybu rozložené napříč elektrodami.
- Spiking neural network decoder překonal regresní modely i filtry, s dalším zlepšením při kombinaci intraneurálních a intermuskulárních signálů.
- Minimální překrytí mezi motorickými a senzorickými mapami v sciatickém nervu, což naznačuje časnou segregaci signálů.
- Data z experimentů jsou veřejně dostupná na GitHubu (https://github.com/rossicecilia/intraneural_phantom_leg.git).
- Výsledky podporují vývoj obousměrných, neuronálně řízených protéz.

## Podrobnosti
Amputace dolní končetiny vede k výrazným senzorimotorickým deficitům, které protézy jen částečně kompenzují. Tradiční myoelektrická řízení protéz spoléhá na povrchové EMG signály z reziduálních svalů, ale ty mají nízkou robustnost a obmedzenou přesnost. Přímé nahrávání z reziduálních periferních nervů nabízí biomimetický přístup, protože zachycuje signály z nervových vlákien, která původně inervovala ztracené svaly. Problémem dosud byly nízké amplitudy signálů a obtíže s interfacováním nervů.

V této studii autoři použili transversal intrafascicular multichannel electrodes (TIMEs), které pronikají do fasciklů nervu a umožňují vícekanálové nahrávání. Implantace proběhla do distálních větví sciatického nervu u dvou pacientů s amputací nad kolenem. Během experimentů pacienti vykonávali voliční pohyby fantomové nohy, jako je flexe/extenze kolene, dorsální/plantární flexe kotníku nebo abdukce/addukce prstů. Analýza odhalila modulaci multiunit activity specifickou pro kloub a směr, distribuovanou napříč 12 elektrodami na každém implantátu.

Dekódování provedli pomocí spiking neural network (SNN), což je model inspirovaný biologickými neurony, který zpracovává spiking data efektivněji než kontinuální signály. SNN decoder dosáhl vyšší přesnosti (např. 85-90 % v predikci směru pohybu) než lineární regrese nebo Kalmanovy filtry. Kombinace s intermuskulárními EMG signály zvyšovala výkon o dalších 5-10 %. Motorické a senzorické mapy vykazovaly minimální překrytí, což potvrzuje segregaci signálů již v periferním nervu. Studie zahrnuje data z několika sezení, s deidentifikovanými pacientovými záznamy dostupnými online, což umožňuje replikaci.

## Proč je to důležité
Tento výzkum představuje pokrok v neurotechnologiích pro bionic integration, podobně jako pokusy Neuralinku s kortikálními implantáty, ale zaměřený na periferní nervy, což je méně invazivní a cílí na dolní končetiny. Obousměrné rozhraní (nahrávání pro kontrolu + stimulace pro zpětnou vazbu) by umožnilo intuitivní ovládání protéz s taktilní a proprioceptivní zpětnou vazbou, což výrazně zlepší mobilitu amputovaných. V širším kontextu posiluje to spiking neural networks jako nástroj pro neuronální dekódování, s potenciálem pro aplikace v robotice a hybridních systémech člověk-stroj. Sice jde o malou kohortu (2 pacienti), výsledky jsou reprodukovatelné a data otevřená, což urychlí další vývoj. Pro průmysl to znamená cestu k komerčním systémům, jako jsou pokročilé protézy od firem typu Össur nebo Ottobock, s vyšší autonomií a přirozeností pohybu.

---

[Číst původní článek](https://www.nature.com/articles/s41467-026-69297-0)

**Zdroj:** 📰 Nature.com
