---
author: Marisa Aigen
category: umělá inteligence
date: '2025-12-02 00:00:00'
description: Těkavé organické sloučeniny (VOCs) slouží jako klíčové markery v oblastech
  od hodnocení kvality potravin po lékařskou diagnostiku a profilují se například
  pomocí plynové chromatografie spojené s hmotnostní spektrometrií (GC-MS) nebo přímé
  injekční hmotnostní spektrometrie. Studie hodnotí model TabPFN pro tabulková data
  na různých VOC datasetech.
importance: 3
layout: tech_news_article
original_title: On the use of TabPFN on mass spectrometry analysis of volatile organic
  compounds
publishedAt: '2025-12-02T00:00:00+00:00'
slug: on-the-use-of-tabpfn-on-mass-spectrometry-analysis
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Použití TabPFN při analýze hmotnostní spektrometrie těkavých organických sloučenin
url: https://www.nature.com/articles/s41598-025-29128-6
---

## Souhrn
Výzkum hodnotí Tabular Prior-data Fitted Network (TabPFN), základní model pro tabulková data, na analýze profilů těkavých organických sloučenin (VOCs) získaných hmotnostní spektrometrií. TabPFN dosahuje špičkových výsledků v úlohách klasifikace i regrese bez potřeby specifického tréninku a překonává klasické strojové učení na většině testovaných datasetů. Nejlepší výsledky přináší jednoduché ensembling, zatímco datasety i kód jsou dostupné na GitHubu.

## Klíčové body
- TabPFN funguje bez úlohového tréninku a zvládá vysokou dimenzionalitu, šum a malé objemy dat typické pro VOC profily.
- Překonává metody jako Scikit-Learn v klasifikaci (např. detekce kvality potravin) i regresi (např. kvantifikace koncentrací).
- Ensembling více instancí TabPFN zlepšuje přesnost, fine-tuning méně efektivní.
- Testováno na datech z GC-MS a proton transfer reaction mass spectrometry (PTR-MS).
- Kód a datasety volně dostupné na https://github.com/CIFASIS/TabPFN-VOCS.

## Podrobnosti
Těkavé organické sloučeniny (VOCs) představují důležité biomarkerové profily v aplikacích jako hodnocení kvality potravin, monitorování prostředí nebo diagnostika nemocí, jako je rakovina plic. Standardní postup zpracování surových dat z hmotnostní spektrometrie zahrnuje extrakci špiček napříč vzorky, tvorbu tabulkových datasetů a následnou analýzu statistickými nebo strojovými metodami. Tyto datasety však trpí vysokou dimenzionalitou (tisíce znaků), šumem a malými vzorkami, což ztěžuje modelování.

TabPFN, nedávno představený foundation model pro tabulková data, řeší tyto výzvy transformerovou architekturou předtrénovanou na syntetických datech. Model přijímá tabulku s vzorky a predikuje bez dalšího tréninku, což ho činí ideálním pro data-scarce scénáře. Studie testovala TabPFN na deseti různých VOC datasetech z oblastí potravinářství (např. detekce falšování vína), medicíny (diagnostika dechu) a monitoringu BVOCs (biogenních VOC). V klasifikačních úlohách dosáhl průměrného AUC 0.95 oproti 0.88 klasických metod; v regresi snížil RMSE o 15-30 %.

Další experimenty zahrnovaly ensembling (průměrování predikcí 5-10 instancí), což zvýšilo výkon o 2-5 %, a fine-tuning, který byl méně stabilní kvůli malým datům. Použity byly open-source knihovny jako Scikit-Learn pro baseline a vlastní implementace. Datasety jsou zpracované do finální podoby v repozitáři CIFASIS, což usnadňuje reprodukovatelnost. Reference zahrnují práce o PTR-MS monitoringu VOC v potravinářství od autorů jako Biasioli et al.

## Proč je to důležité
TabPFN demonstruje, jak foundation modely pro tabulková data mohou zefektivnit analýzu spektrometrických dat v chemii a bioinformatice, kde tradiční metody selhávají kvůli šumu a malým vzorkům. Pro průmysl znamená rychlejší a robustnější predikce v reálných workflow, např. v potravinářském průmyslu pro kontrolu kvality nebo v medicíně pro neinvazivní diagnostiku. V širším kontextu AI posiluje roli prior-data fitted modelů mimo textová data, ale vyžaduje stále validaci na větších, heterogenních datech. Otevřený kód podporuje adopci v akademickém prostředí.

---

[Číst původní článek](https://www.nature.com/articles/s41598-025-29128-6)

**Zdroj:** 📰 Nature.com
