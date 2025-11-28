---
author: Marisa Aigen
category: počítačové vidění
date: '2025-11-26 00:00:00'
description: Výzkumníci vytvořili první specializovanou datovou sadu RGB snímků plevelů
  spojených s virem INSV v Kalifornii a použili ji k trénování modelů hlubokého učení
  pro přesnou identifikaci těchto rostlin.
importance: 3
layout: tech_news_article
original_title: Deep learning classification of INSV-associated weeds in Monterey
  county using a curated RGB image dataset
publishedAt: '2025-11-26T00:00:00+00:00'
slug: deep-learning-classification-of-insv-associated-we
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Klasifikace plevelů spojených s INSV v okrese Monterey pomocí hlubokého učení
  a RGB obrazové sady
url: https://www.nature.com/articles/s41598-025-29552-8
---

## Souhrn
Výzkumníci z Monterey County v Kalifornii vytvořili první specializovanou datovou sadu RGB snímků dvou druhů plevelu – Sonchus oleraceus a Malva parviflora – které šíří virus Impatiens Necrotic Spot Virus (INSV) a způsobily ztráty přesahující 150 milionů dolarů. Pomocí této sady trénovali a porovnávali tři architektury konvolučních neuronových sítí (CNN) pro klasifikaci plevelů v podmínkách napodobujících reálné pole.

## Klíčové body
- Vytvořena první regionální RGB datová sada plevelů spojených s INSV v Monterey County.
- Porovnány tři CNN modely: ResNet-50, ResNet-101 a DenseNet-121.
- ResNet-101 dosáhl nejvyšší přesnosti (91 %) a Cohenova kappa (0,87).
- DenseNet-121 vykázal nejlepší F1-skóre a AUC nad 0,99.
- Použití augmentace dat výrazně zlepšilo zobecnění modelů.

## Podrobnosti
Studie řeší nedostatek specializovaných obrazových dat pro detekci plevelů v oblastech s vysokou hodnotou plodin, jako je Monterey County – jedna z nejproduktivnějších zemědělských oblastí USA. Existující globální datové sady, jako PlantCLEF nebo DeepWeeds, nezahrnují místní druhy plevelů typické pro kalifornské plantáže. Výzkumníci proto nasbírali vlastní snímky v rámci skleníkových podmínek, které simulovaly variabilitu reálného pole (např. osvětlení, úhel pohledu, fáze růstu). K trénování použili standardní RGB snímky, které jsou snadno dostupné i pro běžné zemědělské drony nebo mobilní zařízení. Data byla rozšířena (augmentace) technikami jako rotace, změna jasu či ořez, což vedlo ke zvýšení robustnosti modelů. Trénink probíhal na deseti nezávislých stratifikovaných rozděleních dat, aby byla minimalizována náhodná odchylka výsledků.

## Proč je to důležité
Tento výzkum ukazuje, že i bez použití hyperspektrálních nebo termálních snímků lze dosáhnout vysoké přesnosti identifikace plevelů pomocí běžných RGB kamer a moderních CNN. To otevírá cestu k levnějším a škálovatelným řešením pro přesné zemědělství, zejména v oblastech s vysokou ekonomickou zátěží ztrát způsobených virovými onemocněními. Výsledky také zdůrazňují důležitost lokálně kurátovaných datových sad pro efektivní nasazení AI v zemědělství – globální modely často selhávají v místních podmínkách kvůli nedostatku reprezentativních dat.

---

[Číst původní článek](https://www.nature.com/articles/s41598-025-29552-8)

**Zdroj:** 📰 Nature.com
