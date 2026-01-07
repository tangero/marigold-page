---
author: Marisa Aigen
category: ai bezpečnost
date: '2026-01-06 11:27:09'
description: Výzkumníci z univerzit v Číně a Singapuru vyvinuli techniku, která činí
  ukradená data ze znalostních grafů neužitečnými pro systémy GraphRAG. Firmy by měly
  zvážit pozici hlavního specialisty na dezinformace pro ochranu svých znalostních
  grafů.
importance: 4
layout: tech_news_article
original_title: Researchers poison stolen data to make AI systems return wrong results
publishedAt: '2026-01-06T11:27:09+00:00'
slug: researchers-poison-stolen-data-to-make-ai-systems-
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Výzkumníci otráví ukradená data, aby AI systémy vracely chybné výsledky
url: https://www.theregister.com/2026/01/06/ai_data_pollution_defense/
urlToImage: https://regmedia.co.uk/2025/10/09/shutterstock_720129613.jpg
urlToImageBackup: https://regmedia.co.uk/2025/10/09/shutterstock_720129613.jpg
---

## Souhrn
Výzkumníci přidružení k univerzitám v Číně a Singapuru vyvinuli metodu otrávení dat v znalostních grafech (knowledge graphs, KG), díky čemuž se stávají ukradená data zbytečnými, pokud jsou začleněna do AI systémů založených na GraphRAG bez souhlasu. Tato technika chrání drahé proprietární znalosti před zneužitím v konkurenčních produktech. Paper s názvem „Making Theft Useless: Adulteration-Based Protection of Proprietary Knowledge Graphs in GraphRAG Systems“ popisuje adulteraci dat jako efektivní obranu.

## Klíčové body
- Výzkumníci navrhují otrávení znalostních grafů, aby GraphRAG systémy vracely nesprávné odpovědi na dotazy.
- Náklady na tvorbu KG dosahují 5,71 USD za jednu faktickou výpověď, například v databázi Cyc s 21 miliony tvrzení.
- Firmy jako Pfizer a Siemens používají KG pro objev léků a výrobní procesy.
- GraphRAG, vývoj od Microsoftu, vylepšuje retrieval-augmented generation (RAG) pomocí sémantických shluků dat.
- Technologie je podporována Amazonem, Googlem a Microsoftem v jejich cloudových službách.

## Podrobnosti
Velké jazykové modely (LLM) jako Gemini od Google nebo modely od Microsoftu spoléhají na tréninková data, ale pro aktuální informace se používá retrieval-augmented generation (RAG). Tato metoda umožňuje LLM přistupovat k externím datovým sadám během generování odpovědí, což zlepšuje přesnost, ale nezaručuje správnost – například Google AI Overviews v prohledávači poskytuje aktuální webová data, která nemusí být vždy přesná. GraphRAG představuje pokročilejší variantu od Microsoftu, která strukturovaná data organizuje do znalostních grafů (KG). KG jsou sémanticky propojené shluky informací, kde uzly představují entity a hrany vztahy mezi nimi, což usnadňuje LLM pochopení kontextu a generování přesnějších predikcí.

Výzkumníci Weijie Wang, Peizhuo Lv a kolegové poukazují na vysoké náklady tvorby KG. Například databáze Cyc obsahuje 21 milionů faktických tvrzení a její rozšíření stojí průměrně 5,71 USD za výpověď. Firmy jako farmaceutický gigant Pfizer využívají KG pro urychlení objevování léků tím, že mapují chemické interakce a biologické dráhy. Podobně Siemens, specializující se na průmyslovou automatizaci, integruje KG do výrobních procesů pro optimalizaci a predikci poruch. Tyto KG jsou klíčovým majetkem, protože umožňují budování specializovaných AI systémů.

Navrhovaná obrana spočívá v adulteraci – záměrném znečištění dat toxickými prvky. Pokud zloděj ukradne KG a načte ji do GraphRAG systému, otrávené části způsobí, že LLM bude na související dotazy odpovídat chybně nebo nesouladně. Metoda je navržena tak, aby byla nepostřehnutelná pro běžné použití originálního KG, ale devastující pro neoprávněné kopie. Autoři testovali přístup na reálných datech a prokázali výrazné snížení přesnosti v ukradených grafech.

## Proč je to důležité
V éře, kdy se data stávají nejhodnotnějším aktivem pro AI, roste riziko krádeže proprietárních KG, podobně jako u mediálních tvůrců bojujících proti scrapingu pro trénink LLM. Tato technika poskytuje firemám praktickou obranu proti konkurentům, kteří by mohli ukradená data použít k rychlému nasazení levnějších AI nástrojů. Podpora GraphRAG velkými cloudy (Amazon, Google, Microsoft) znamená, že metoda má široký dosah – ovlivní celý ekosystém RAG systémů. Pro průmysl to znamená posun od pasivní ochrany (šifrování, přístupová práva) k aktivní sabotáži dat, což může změnit strategie vývoje AI. Kriticky lze dodat, že adulterace vyžaduje pečlivý design, aby nepoškodila vlastní systémy, a otevírá debatu o etice záměrných chyb v datech.

---

[Číst původní článek](https://www.theregister.com/2026/01/06/ai_data_pollution_defense/)

**Zdroj:** 📰 Theregister.com
