---
author: Marisa Aigen
category: umělá inteligence
date: '2025-12-01 00:00:00'
description: Vědci představili model Cryo-EM Image Evaluation Foundation (Cryo-IEF),
  předtrénovaný na 65 milionech částicových obrazů z kryogenní elektronové mikroskopie
  v nekontrolovaném učení. Tento model automatizuje složité workflowy zpracování dat
  a zvyšuje přístupnost a robustnost technologie cryo-EM.
importance: 3
layout: tech_news_article
original_title: Artificial intelligence foundation model automates cryo-EM structure
  determination
publishedAt: '2025-12-01T00:00:00+00:00'
slug: artificial-intelligence-foundation-model-automates
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Základní model umělé inteligence automatizuje určení struktur v cryo-EM
url: https://www.nature.com/articles/s41592-025-02917-7
urlToImage: https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41592-025-02917-7/MediaObjects/41592_2025_2917_Fig1_HTML.png
urlToImageBackup: https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41592-025-02917-7/MediaObjects/41592_2025_2917_Fig1_HTML.png
---

## Souhrn
Výzkumníci vyvinuli model Cryo-IEF, základní model umělé inteligence předtrénovaný na 65 milionech částicových obrazů z dat cryo-EM bez označení. Tento model zvládá různé úkoly zpracování dat v kryogenní elektronové mikroskopii a automatizuje složitý proces určení struktur molekul. Díky tomu se technologie stává dostupnější pro širší okruh uživatelů.

## Klíčové body
- Předtrénování na 65 milionech particle images v unsupervised módu pomocí self-supervised learning.
- Automatizace celého workflowu cryo-EM, včetně hodnocení obrazů a rekonstrukce struktur.
- Inspirace z vision transformers a metod jako CryoDRGN-AI pro zpracování heterogenních dat.
- Zlepšení robustnosti oproti tradičním metodám, které vyžadují manuální zásahy.
- Publikováno v Nature Methods s odkazy na klíčové reference v oboru.

## Podrobnosti
Kryogenní elektronová mikroskopie (cryo-EM) je klíčovou technikou v strukturální biologii, která umožňuje vizualizovat proteiny a komplexy v nativním stavu při kryogenních teplotách. Tradiční workflow zahrnuje sběr tisíců obrazů, detekci částic, klasifikaci a rekonstrukci 3D struktur, což je časově náročné a náchylné k chybám. Model Cryo-IEF řeší tyto problémy tím, že byl předtrénován na obrovském datasetu 65 milionů particle images z veřejných repozitářů jako EMPIAR. Používá unsupervised pretraining inspirované self-supervised vision transformers, jak je popsáno v práci Chen et al. (2021), kde modely učí porovnáváním augmentovaných verzí stejných obrazů.

Cryo-IEF není omezen na jednu úlohu: exceluje v hodnocení kvality obrazů, detekci částic, klasifikaci heterogenity a ab initio rekonstrukci. Například v porovnání s CryoDRGN-AI (Levy et al., 2025), který se zaměřuje na neurální rekonstrukci heterogenních dat z cryo-EM a cryo-ET, Cryo-IEF rozšiřuje možnosti o širší automatizaci. Reference Nogales (2016) zdůrazňuje vývoj cryo-EM do mainstream metody, kde byly dosaženy rozlišovací schopnosti pod 2 Å, ale workflow zůstává složitý. Cryo-IEF tento workflow zjednodušuje na jednotný model, který lze fine-tunovat pro specifické dataset.

Model je dostupný pro přístup přes instituce nebo předplatné Nature Portfolio, s možností koupě článku za 39,95 USD. Data pocházejí z EMPIAR, což zajišťuje reprodukovatelnost. Oproti předchozím přístupům, které vyžadovaly expertní znalosti, Cryo-IEF snižuje závislost na manuálním nastavování parametrů a zvyšuje konzistenci výsledků napříč různými typy vzorků.

## Proč je to důležité
Tento vývoj posiluje integraci umělé inteligence do biophysikálního výzkumu, kde cryo-EM hraje roli v objevování léků a pochopení biologických mechanismů. Automatizace workflowu umožní menším laboratořím rychleji analyzovat data, což urychlí výzkum proteinů spojených s nemocemi. V širším kontextu AI demonstruje, jak foundation models přenáší úspěchy z počítačového vidění do specializovaných domén, ale zůstává omezen na cryo-EM data – není to univerzální řešení pro jiné mikroskopie. Kriticky, unsupervised přístup minimalizuje potřebu anotací, což je klíčové pro oblasti s nedostatkem označených dat, avšak kvalita závisí na diverzitě tréninkového korpusu.

---

[Číst původní článek](https://www.nature.com/articles/s41592-025-02917-7)

**Zdroj:** 📰 Nature.com
