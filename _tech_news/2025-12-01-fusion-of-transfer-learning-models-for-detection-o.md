---
author: Marisa Aigen
category: umělá inteligence
date: '2025-12-01 00:00:00'
description: Výzkum představuje model FDLM-DADOA, který kombinuje hluboké učení pro
  automatickou detekci Alzheimerovy nemoci z magnetických rezonančních obrazů (MRI).
  Používá fúzi modelů EfficientNet B7, MobileNet a ResNet-50 pro extrakci znaků, následovanou
  klasifikací pomocí BiLSTM a optimalizací hyperparametrů.
importance: 3
layout: tech_news_article
original_title: Fusion of transfer learning models for detection of alzheimer’s disease
  using bidirectional long short-term memory with equilibrium optimization algorithm
publishedAt: '2025-12-01T00:00:00+00:00'
slug: fusion-of-transfer-learning-models-for-detection-o
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Fúze modelů přenášeného učení pro detekci Alzheimerovy nemoci s využitím obousměrné
  dlouhodobé krátkodobé paměti a algoritmu rovnovážné optimalizace
url: https://www.nature.com/articles/s41598-025-30456-w
---

## Souhrn
Nový model FDLM-DADOA spojuje tři konvoluční neuronové sítě pro extrakci znaků z MRI snímků mozku a obousměrnou dlouhodobou krátkodobou paměť (BiLSTM) pro klasifikaci Alzheimerovy nemoci. Předzpracování zahrnuje Wienerův filtr pro odstranění šumu a algoritmus rovnovážné optimalizace pro ladění hyperparametrů. Cílem je zlepšit automatickou diagnostiku před vznikem trvalého poškození mozku.

## Klíčové body
- **Předzpracování obrazů**: Wienerův filtr odstraňuje šum z MRI dat, což zlepšuje kvalitu vstupních dat pro následné analýzy.
- **Extrakce znaků**: Fúze modelů EfficientNet B7 (efektivní architektura pro vysokou přesnost), MobileNet (lehkovágní pro mobilní aplikace) a ResNet-50 (s reziduálními bloky pro hluboké sítě).
- **Klasifikace**: BiLSTM zpracovává sekvenční závislosti v datech pro identifikaci a kategorizaci Alzheimerovy nemoci.
- **Optimalizace**: Algoritmus Equilibrium Optimization (EOA) automaticky vybírá hyperparametry pro maximální výkon modelu.
- **Aplikace**: Zaměřeno na neuroimaging data, kde tradiční metody selhávají kvůli subjektivitě.

## Podrobnosti
Alzheimerova nemoc (AD) je neurodegenerativní onemocnění, jehož časná detekce je klíčová, protože léky jsou nejúčinnější v raných stádiích před nevratným poškozením mozku. Magnetická rezonance (MRI) slouží jako neinvazivní metoda k detekci atrofie mozku, ale její akvizice je časově náročná kvůli nutnosti fyzického prohlídkového postupu. Tradiční diagnostika závisí na manuální analýze, což vede k chybám a zpožděním.

Navrhovaný model FDLM-DADOA řeší tyto limity fúzí hlubokého učení. Nejprve Wienerův filtr, adaptivní filtr v oblasti frekvencí, minimalizuje šum v obrazech bez ztráty detailů okrajů. Poté následuje extrakce znaků z tří předtrénovaných modelů přenášeného učení: EfficientNet B7, který dosahuje vysoké přesnosti díky compound scalingu (vyvážení hloubky, šířky a rozlišení); MobileNet, optimalizovaný pro nízkou výpočetní složitost pomocí depthwise separabilních konvolucí, vhodný pro edge computing; a ResNet-50 s 50 vrstvami a reziduálními spojnicemi, které řeší problém mizejícího gradientu v hlubokých sítích.

Tyto modely generují bohatou sadu znaků, kterou zpracovává BiLSTM – rozšíření LSTM, které učí v obou směrech (vpřed a vzad), což zachycuje dlouhodobé závislosti v sekvencích MRI dat. BiLSTM slouží k binární nebo vícekategoriální klasifikaci (např. zdravý mozek vs. mírná/moderátní/severo pokročilá AD). Hyperparametry jako velikost batchů, rychlost učení nebo počet neuronů v BiLSTM optimalizuje algoritmus Equilibrium Optimization (EOA), metaheuristický algoritmus inspirovaný chemickou rovnováhou, který simuluje hledání rovnovážného stavu pro globální optima.

Model byl testován na standardních datasetu jako ADNI (Alzheimer's Disease Neuroimaging Initiative), kde překonává tradiční machine learning (např. SVM) i samostatné deep learning modely díky fúzi a optimalizaci. Nicméně, jako akademický výzkum postrádá detaily o přesném výkonu (accuracy, F1-score) v poskytnutém abstraktu a vyžaduje nezávislou validaci na reálných klinických datech.

## Proč je to důležité
V širším kontextu AI v medicíně představuje tento přístup další krok k automatizaci neuroimagingu, kde fúze modelů zvyšuje robustnost oproti jednomu modelu a BiLSTM lépe modeluje časové změny v atrofii. Pro průmysl znamená potenciál integrace do PACS systémů (Picture Archiving and Communication Systems) v nemocnicích, urychlení diagnostiky a snížení zátěže radiologů. V porovnání s komerčními řešeními jako Aidoc nebo Viz.ai je to open-source alternativa, ale s rizikem přehřátí – mnoho podobných modelů selže v klinické praxi kvůli variabilitě dat. Pro pacienty by to mohlo znamenat dřívější intervenci, avšak regulace (FDA/CE) a etické aspekty (bias v trénovacích datech) zůstávají výzvou. Celkově posiluje trend AI v neurologii, kde přesnost detekce AD dosahuje 90+ % v kontrolovaných testech, ale reálný dopad závisí na nasazení.

---

[Číst původní článek](https://www.nature.com/articles/s41598-025-30456-w)

**Zdroj:** 📰 Nature.com
