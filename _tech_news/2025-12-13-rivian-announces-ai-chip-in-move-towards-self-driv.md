---
author: Marisa Aigen
category: elektromobilita
companies:
- Rivian
date: '2025-12-13 01:00:00'
description: Výrobce elektromobilů Rivian navrhl svůj čip interně uprostřed Silicon
  Valley. Čip pohání nový Autonomy Compute Module 3 pro nadcházející SUV R2.
importance: 4
layout: tech_news_article
original_title: Rivian announces AI chip in move towards self-driving future
publishedAt: '2025-12-13T01:00:00+00:00'
slug: rivian-announces-ai-chip-in-move-towards-self-driv
source:
  emoji: 📰
  id: null
  name: Popular Science
title: Rivian oznámil AI čip v kroku k autonomnímu řízení
url: http://www.popsci.com/technology/rivian-ai-chip/
urlToImage: https://www.popsci.com/wp-content/uploads/2025/12/Rivian_Universal_Hands_Free.jpg?quality=85&w=1200
urlToImageBackup: https://www.popsci.com/wp-content/uploads/2025/12/Rivian_Universal_Hands_Free.jpg?quality=85&w=1200
---

## Souhrn
Rivian, americký výrobce elektromobilů zaměřený na prémiové SUV a pickupy, oznámil vlastní navržený AI čip. Tento procesor napájí nový Autonomy Compute Module 3, který se objeví v příští generaci vozů R2 SUV a slouží k zpracování dat pro autonomní řízení. Oznámení proběhlo na první Autonomy and AI Day společnosti v Silicon Valley.

## Klíčové body
- Čip dosahuje výkonu 1600 sparse INT8 TOPS (trilion operací za sekundu v 8bitové celé aritmetice s řídkými daty) a zpracovává 5 miliard pixelů za sekundu.
- Je čtyřnásobně výkonnější než současný systém Rivianu založený na čipech Nvidia.
- Navržený a zapouzdřený interně Rivianem, výroba čipu probíhá u externích dodavatelů.
- Zaměřený na neurální engine a nový middleware stack pro autonomní software.
- Použití v modelech R2 SUV, které Rivian plánuje spustit v roce 2026.

## Podrobnosti
Rivian, založený v roce 2009 a známý modely jako R1T pickup a R1S SUV, se dlouhodobě soustředí na elektromobilitu s důrazem na autonomní funkce. Na Autonomy and AI Day, který uspořádal zakladatel a CEO RJ Scaringe, představil společnost hardware, který mění jejich přístup k výpočetní platformě pro autonomii. Klíčovým prvkem je Autonomy Compute Module 3 (ACM3), palubní počítač poháněný vlastním AI čipem.

Technické specifikace ukazují na vysoký výkon určený pro inferenci neuronových sítí v reálném čase. Sparse INT8 TOPS je metrika pro efektivní zpracování AI modelů, kde řídká data (sparse) umožňují rychlejší výpočty bez ztráty přesnosti v konvolučních neuronových sítích používaných pro detekci objektů, predikci dráhy nebo senzorové fúzi v autonomním řízení. Zpracování 5 miliard pixelů za sekundu znamená kapacitu pro více kamerových vstupů – typicky 8-12 kamer v moderních EV – s vysokým rozlišením, což je nezbytné pro bird's-eye view mapování nebo 3D rekonstrukci prostředí.

Rivian zdůrazňuje neural engine, což je specializovaná část čipu pro akceleraci AI úloh, a nový middleware stack. Middleware slouží jako vrstva mezi senzory, AI modely a akčním softwarem vozu, zajišťuje bezpečnou komunikaci a optimalizaci datového toku. Na rozdíl od plnohodnotné výroby čipů (jako TSMC s miliardovými továrnami), Rivian navrhuje architekturu a balení interně, ale fabrikaci outsourcovává. To snižuje náklady a zrychluje iterace oproti závislosti na dodavatelích jako Nvidia.

Současný systém Rivianu na Nvidia čipech (pravděpodobně Orin nebo podobný) dosahuje asi 400 TOPS; nový ACM3 tuto kapacitu čtyřnásobí, což umožní složitější modely, jako víceúrovňovou predikci chování nebo lepší generalizaci v nepříznivých podmínkách. Rivian testuje autonomní software na současných modelech R1 a plánuje rozšíření na R2, které cílí na masovější trh s cenou kolem 45 000 USD.

## Proč je to důležité
Vývoj vlastního AI čipu Rivianem signalizuje trend vertikální integrace v automobilovém průmyslu, podobně jako u Tesly s jejich Hardware 4 (HW4) nebo Dojo superpočítači. Snížení závislosti na Nvidia, který ovládá 80-90 % trhu AI hardware, umožňuje Rivianu optimalizovat čip pro specifické workloady autonomního řízení – například lepší efektivitu v edge computingu na palubě vozu, kde latence musí být pod 10 ms. To může vést k rychlejšímu nasazení vyšších úrovní autonomie (SAE Level 3+), kde vůz zvládá složité scénáře bez řidiče.

Pro průmysl to znamená větší konkurenci: Rivian, s výrobní kapacitou rostoucí na 150 000 vozů ročně, může konkurovat Tesle (FSD) nebo Waymu v robotaxi segmentech. Kriticky však, 1600 TOPS není rekordní – Tesla HW4 dosahuje podobných hodnot a mobilní SoC jako Qualcomm Snapdragon X Elite překonávají 40 TOPS v INT8. Rivian musí prokázat spolehlivost v reálném nasazení, kde bezpečnostní certifikace (ISO 26262 ASIL-D) a robustnost proti adversarialním útokům jsou klíčové. Dlouhodobě to posiluje ekosystém elektromobility, kde AI hardware urychluje přechod k plně autonomním flotilám, ale závisí na softwarovém pokroku a regulacích.

---

[Číst původní článek](http://www.popsci.com/technology/rivian-ai-chip/)

**Zdroj:** 📰 Popular Science
