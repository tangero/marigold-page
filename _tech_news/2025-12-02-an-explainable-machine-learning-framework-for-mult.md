---
author: Marisa Aigen
category: strojové učení
date: '2025-12-02 00:00:00'
description: Vědecký článek v Scientific Reports představuje rámec, který integruje
  vysvětlitelné strojové učení s vícecílovou optimalizací pro snížení emisí CO2 při
  renovacích stávajících budov. Zaměřuje se na materiálové, provozní a sezónní emise
  a validuje ho na případové studii průmyslové budovy.
importance: 3
layout: tech_news_article
original_title: An explainable machine learning framework for multi-objective carbon
  reduction targeting material operational seasonal emissions in building retrofits
publishedAt: '2025-12-02T00:00:00+00:00'
slug: an-explainable-machine-learning-framework-for-mult
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Vysvětlitelný rámec strojového učení pro vícecílovou optimalizaci snížení uhlíkových
  emisí materiálů, provozu a sezónní bilance při rekonstrukcích budov
url: https://www.nature.com/articles/s41598-025-29418-z
---

## Souhrn
Výzkum publikovaný v Scientific Reports navrhuje systematický rámec, který spojuje vysvětlitelné strojové učení s vícecílovou optimalizací pro minimalizaci uhlíkových emisí při rekonstrukcích budov. Rámec se soustředí na tři klíčové metriky: materiálovou intenzitu emisí (MCEI), provozní intenzitu emisí (OCEI) a sezónní bilanci emisí (SCEB). V případové studii dosáhl nejlepší kompromisní řešení snížení MCEI o 71,06 %, OCEI o 37,20 % a zlepšení SCEB o 24,75 % oproti referenčnímu stavu.

## Klíčové body
- Nejlepší prediktivní model: CatBoost, který překonal pět dalších algoritmů (např. XGBoost, Random Forest) díky vysoké přesnosti na datech simulací emisí.
- Vysvětlitelnost zajišťuje SHAP, které identifikovalo klíčové proměnné: FLH (full load hours), WWR1 a WWR2 (window-to-wall ratio), NOF (number of floors).
- Optimalizace pomocí NSGA-II algoritmu, který generoval čtyři sady Pareto-optimálních řešení.
- Doporučené strategie: opětovné použití materiálů, nízkouhlíkové materiály, optimalizace příček, zlepšení tepelné izolace obalu budovy a designu atria.
- Data: Vysokouhlíkové simulace emisí, dostupná pro další analýzy.

## Podrobnosti
Článek reaguje na globální tlak k uhlíkové neutralitě v stavebnictví, kde rekonstrukce stávajících budov představuje efektivní cestu k omezení emisí, protože nové stavby tvoří menší podíl emisí než provoz stávajících objektů. Rámec je postaven na třech jádrových metrikách: MCEI měří emise spojené s výrobou a transportem materiálů během rekonstrukce, OCEI hodnotí emise z provozu budovy (vytápění, chlazení, osvětlení) a SCEB porovnává sezónní výkyvy emisí mezi léty, což umožňuje zohlednit dynamiku počasí a užívání.

Pro predikci emisí byly použity data z vysokouhledných simulací, trénovány šest algoritmy strojového učení: CatBoost, LightGBM, XGBoost, Random Forest, Gradient Boosting a AdaBoost. CatBoost dosáhl nejvyšší přesnosti díky své schopnosti zpracovávat kategorické data a odolnosti vůči přeučení, což je klíčové pro heterogenní data z budovních simulací. SHAP (SHapley Additive exPlanations) pak poskytl globální i lokální vysvětlitelnost, ukazujíc, jak proměnné jako FLH (počet plných provozních hodin za rok), WWR1 (poměr oken k stěnám na prvním patře) a WWR2 (na vyšších patrech) nebo NOF (počet pater) ovlivňují emise. Například vyšší WWR zvyšuje tepelné ztráty, což zvyšuje OCEI.

V validaci na třípodlažní průmyslové budově byl NSGA-II (Non-dominated Sorting Genetic Algorithm II) použit pro multi-objective optimalizaci těchto tří metrik. Algoritmus generuje Pareto-frontu, kde neexistuje jedno optimální řešení, ale sady kompromisů. Získány čtyři varianty: od extrémního snížení materiálových emisí po vyvážené řešení. Nejvyváženější dosáhlo zmíněných redukcí, což demonstruje praktickou použitelnost. Doporučení zahrnují recyklaci materiálů (snižuje MCEI), volbu cementu s nižšími emisemi, minimalizaci příček pro lepší průtok vzduchu, zesílení izolace střechy a fasády (ovlivňuje OCEI) a optimalizaci atria pro lepší denní svitlo a ventilaci (zlepšuje SCEB).

Rámec je škálovatelný, protože závisí na simulacích dostupných v softwaru jako EnergyPlus nebo DesignBuilder, a lze ho aplikovat na různé typy budov.

## Proč je to důležité
Tento přístup přispívá k udržitelnému stavebnictví tím, že poskytuje datově podložené rozhodnutí pro architekty a investory, kteří často čelí konfliktům mezi náklady, estetikou a emisemi. V kontextu EU směrnic o energetické náročnosti budov (EPBD) a cílů net-zero do 2050 umožňuje replikovatelný nástroj pro tisíce rekonstrukcí. Pro AI oblast zdůrazňuje hodnotu vysvětlitelných modelů v inženýrských aplikacích, kde black-box modely (jako některé hluboké sítě) selhávají kvůli potřebě auditu. Omezením je závislost na kvalitních simulačních datech, což vyžaduje kalibraci na reálných měřeních. Celkově posiluje integraci ML do zelených technologií bez přehánění očekávání okamžitých průlomů.

---

[Číst původní článek](https://www.nature.com/articles/s41598-025-29418-z)

**Zdroj:** 📰 Nature.com
