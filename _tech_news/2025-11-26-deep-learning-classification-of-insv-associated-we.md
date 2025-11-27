---
author: Marisa Aigen
category: počítačové vidění
date: '2025-11-26 00:00:00'
description: Vědci vyvinuli první specializovanou datovou sadu RGB snímků plevelů
  spojených s virem INSV v kalifornském okrese Monterey a použili ji k trénování modelů
  hlubokého učení pro přesnou identifikaci těchto rostlin.
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
title: Klasifikace plevelů spojených s virem INSV v okrese Monterey pomocí deep learningu
  a RGB obrazové sady
url: https://www.nature.com/articles/s41598-025-29552-8
---

## Souhrn
Výzkumníci z Monterey County v Kalifornii vytvořili první specializovanou datovou sadu RGB snímků plevelů Sonchus oleraceus a Malva parviflora, které šíří virus Impatiens Necrotic Spot Virus (INSV) a způsobily ztráty přes 150 milionů dolarů. Pomocí této sady trénovali tři konvoluční neuronové sítě (CNN) pro klasifikaci plevelů v podmínkách připomínajících reálné pole.

## Klíčové body
- Vytvořena první regionální RGB datová sada plevelů spojených s INSV v Monterey County.
- Porovnány tři architektury CNN: ResNet-50, ResNet-101 a DenseNet-121.
- ResNet-101 dosáhl nejvyšší přesnosti (91 %) a Cohenova kappa (0,87).
- DenseNet-121 vykázal nejlepší F1-skóre a AUC nad 0,99.
- Augmentace dat výrazně zlepšila zobecnění modelů.

## Podrobnosti
Výzkum řeší kritický problém chybějících regionálně specifických dat pro detekci plevelů v systémech přesného zemědělství. Existující globální sady jako PlantCLEF nebo DeepWeeds nezahrnují plevely typické pro kalifornské pěstební systémy s vysokou hodnotou plodin. Autoři proto vytvořili vlastní datovou sadu ve skleníku, kde simulovali variabilitu polních podmínek – odlišné osvětlení, úhly pohledu a fáze růstu rostlin. Pro trénink použili standardní RGB snímky (nikoli hyperspektrální nebo termální), což zvyšuje praktickou využitelnost řešení v běžných zemědělských dronech nebo mobilních aplikacích. Modely byly trénovány na deseti stratifikovaných rozděleních dat, aby se minimalizovalo riziko náhodného zkreslení výsledků. Augmentace dat (otočení, změna jasu, oříznutí) vedla k výraznému zlepšení robustnosti modelů. Výsledky ukazují, že i bez specializovaných senzorů lze dosáhnout vysoké přesnosti identifikace plevelů, což je klíčové pro včasnou detekci a prevenci šíření INSV.

## Proč je to důležité
Tento výzkum přispívá k rozvoji přesného zemědělství, kde AI hraje rostoucí roli při snižování ztrát a minimalizaci používání herbicidů. Přesná identifikace plevelů umožňuje cílené zásahy, což šetří náklady i životní prostředí. I když se nejedná o průlom v architektuře neuronových sítí, ukazuje to praktickou aplikovatelnost stávajících modelů v konkrétním agronomickém kontextu. Pro zemědělský sektor, zejména v regionech s vysokou hodnotou plodin, může být takový nástroj klíčový pro udržitelnost a konkurenceschopnost.

---

[Číst původní článek](https://www.nature.com/articles/s41598-025-29552-8)

**Zdroj:** 📰 Nature.com
