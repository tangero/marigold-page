---
author: Marisa Aigen
category: strojové učení
date: '2025-12-02 00:00:00'
description: Vědecký článek v Scientific Reports představuje rámec kombinující vysvětlitelné
  strojové učení s vícecílovou optimalizací pro snížení emisí uhlíku při renovacích
  budov. Zaměřuje se na materiálové, provozní a sezónní emise a validuje ho na případové
  studii průmyslové budovy.
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
title: Vysvětlitelný rámec strojového učení pro vícecílovou redukci uhlíkových emisí
  zaměřenou na provozní sezónní emise materiálů při renovacích budov
url: https://www.nature.com/articles/s41598-025-29418-z
---

## Souhrn
Výzkum navrhuje rámec, který integruje vysvětlitelné strojové učení s vícecílovou optimalizací pro optimalizaci emisí uhlíku při renovacích stávajících budov. Používá data z vysokorychlostní simulace emisí a algoritmy jako CatBoost pro predikci, SHAP pro vysvětlení a NSGA-II pro optimalizaci. V případové studii na třípatrové průmyslové budově dosáhl nejlepší varianty snížení materiálových emisí o 71 %, provozních o 37 % a zlepšení sezónní bilance o 25 % oproti základnímu scénáři.

## Klíčové body
- Rámec se zaměřuje na tři metriky: MCEI (intenzita materiálových emisí uhlíku), OCEI (intenzita provozních emisí uhlíku) a SCEB (sezónní bilance emisí uhlíku).
- Nejlepší prediktivní model CatBoost překonal pět dalších algoritmů (např. XGBoost, Random Forest).
- SHAP analýza identifikovala klíčové proměnné: FLH (výška podlaží), WWR1 (poměr okenní plochy na fasádě), NOF (počet oken) a WWR2 (poměr pro střechu).
- Optimalizace NSGA-II poskytla čtyři sady řešení s doporučenými strategiemi jako opětovné použití materiálů a zlepšení tepelné izolace.
- Studie je publikován v Scientific Reports a data jsou dostupná.

## Podrobnosti
Článek reaguje na globální snahu o uhlíkovou neutralitu v stavebnictví, kde renovace stávajících budov představují klíčový nástroj proti klimatickým změnám. Rámec začíná simulací emisí s vysokým rozlišením, která zahrnuje materiálové emise (MCEI, měřené v kg CO2 ekv./m²), provozní emise během provozu (OCEI, podobně v kg CO2 ekv./m²) a sezónní bilanci (SCEB), která porovnává chladicí a topné emise v různých obdobích. Tyto metriky umožňují komplexní hodnocení renovací.

Pro predikci emisí bylo testováno šest algoritmů strojového učení: CatBoost, LightGBM, XGBoost, Random Forest, Gradient Boosting a AdaBoost. CatBoost dosáhl nejvyšší přesnosti díky své schopnosti zpracovávat kategorické data bez předzpracování a minimalizovat přeučení. Model byl trénován na datech z simulací, které zahrnovaly desítky designových proměnných jako tloušťka stěn, orientace budovy nebo typ materiálů.

Vysvětlitelnost zajišťuje knihovna SHAP (SHapley Additive exPlanations), která přiřazuje příspěvky jednotlivým proměnným k predikci. Nejvlivnější byly FLH (vyšší podlaží snižují emise díky menší ploše fasády), WWR1 a WWR2 (optimalizace okenní plochy ovlivňuje tepelné ztráty) a NOF (počet oken). Tato identifikace umožňuje architektům soustředit se na ovlivnitelné faktory.

Vícecílová optimalizace proběhla pomocí genetického algoritmu NSGA-II (Non-dominated Sorting Genetic Algorithm II), který generuje Pareto-frontu řešení vyvažujících tři cíle. V případové studii třípatrové průmyslové budovy v Číně (pravděpodobně, protože data jsou z lokálních simulací) poskytl čtyři varianty. Nejvyváženější snížila MCEI o 71,06 %, OCEI o 37,20 % a zlepšila SCEB o 24,75 %. Doporučené strategie zahrnují opětovné použití stávajících materiálů, nasazení nízkouhlíkových alternativ (např. recyklovaný beton), optimalizaci příček, zlepšení tepelné výkonnosti obalu budovy (izolace, dvojskla) a design atria pro lepší denní svitlo a ventilaci. Rámec je škálovatelný a replikovatelný, s daty dostupnými pro další výzkum.

## Proč je to důležité
Tento přístup přináší praktickou hodnotu pro stavební průmysl, kde renovace tvoří většinu budoucích investic do udržitelnosti. Vysvětlitelné modely jako CatBoost s SHAP překonávají černé skříňky tradičního ML, což usnadňuje schvalování u regulátorů a architektů. V kontextu AI aplikací v energetice posiluje důvěru v predikce a podporuje cíle uhlíkové neutrality do 2050. Pro průmysl znamená rychlejší a levnější optimalizace projektů, zatímco omezuje rizika suboptimálních rozhodnutí. Nicméně, aplikace závisí na kvalitě simulačních dat a lokálních podmínkách, což vyžaduje validaci mimo případovou studii.

---

[Číst původní článek](https://www.nature.com/articles/s41598-025-29418-z)

**Zdroj:** 📰 Nature.com
