---
author: Marisa Aigen
category: ai
companies:
- Amazon
- Nvidia
date: '2025-12-02 16:01:46'
description: AWS vydal třetí generaci svého čipu pro trénink AI modelů Trainium3 s
  výrazně vyšším výkonem a energetickou účinností. Na konferenci re:Invent 2025 společnost
  také oznámila plány na Trainium4, který bude integrovat s čipy Nvidia.
importance: 3
layout: tech_news_article
original_title: Amazon releases an impressive new AI chip and teases a Nvidia-friendly
  roadmap   | TechCrunch
publishedAt: '2025-12-02T16:01:46+00:00'
slug: amazon-releases-an-impressive-new-ai-chip-and-teas
source:
  emoji: 🚀
  id: techcrunch
  name: TechCrunch
title: Amazon představil nový AI čip Trainium3 a naznačil roadmapu kompatibilní s
  Nvidia
url: https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/
urlToImage: https://techcrunch.com/wp-content/uploads/2020/01/GettyImages-1136663877.jpg?resize=1200,800
urlToImageBackup: https://techcrunch.com/wp-content/uploads/2020/01/GettyImages-1136663877.jpg?resize=1200,800
---

### Souhrn
Amazon Web Services (AWS) představil na konferenci re:Invent 2025 čip Trainium3, třetí generaci svého hardwaru pro trénink a inference AI modelů. Tento čip na 3nanometrovém výrobním procesu přináší čtyřnásobné zrychlení oproti druhé generaci Trainium2 a čtyřnásobně vyšší kapacitu paměti. Společnost zároveň naznačila vývoj Trainium4, který umožní bezproblémovou spolupráci s čipy Nvidia.

### Klíčové body
- Trainium3 UltraServer obsahuje 144 čipů na jeden server a lze je propojit do clusterů s až 1 milionem čipů, což je desetinásobek předchozí generace.
- Čtyřnásobný nárůst výkonu a paměti platí jak pro trénink velkých jazykových modelů (LLM), tak pro inference, tedy nasazení modelů v produkci.
- 40procentní zlepšení energetické účinnosti oproti Trainium2, což snižuje spotřebu energie v datech centrech.
- Zákazníci jako Anthropic, japonská firma Karakuri specializující se na LLM, SplashMusic (AI pro hudbu) a Decart již čip testovali a snížili náklady na inference.
- Trainium4 bude "Nvidia-friendly", což umožní hybridní konfigurace hardwaru.

### Podrobnosti
AWS vyvíjí vlastní AI čipy od roku 2018, kdy uvedl první Trainium, určený primárně pro trénink hlubokých neuronových sítí. Trainium3 staví na zkušenostech z předchozích generací a integruje pokročilou síťovou technologii neuroných sítí, kterou AWS vyvinul interně. Každý UltraServer, systém postavený kolem Trainium3, zvládne 144 čipů, což umožňuje škálování na obrovské clustery. Například propojením tisíců serverů lze dosáhnout kapacity 1 milionu čipů, ideální pro trénink modelů s biliony parametrů, jako jsou současné LLM typu GPT nebo Claude.

Výkonový skok je podle AWS čtyřnásobný v porovnání s Trainium2, což znamená rychlejší iterace při vývoji AI modelů a nižší latenci při inference – tedy odpovědích AI aplikací v reálném čase. Paměťová kapacita vzrostla podobně, což umožňuje zpracování větších datových sad bez nutnosti častého přenášení dat mezi čipy. Klíčovou výhodou je 40procentní snížení spotřeby energie, což je v době, kdy data centra pohlcují gigawatty elektřiny, zásadní faktor. AWS to prezentuje jako úsporu pro zákazníky, kteří platí podle spotřeby.

Zákazníci jako Anthropic, vývojář modelů Claude a investor Amazonu, potvrdili snížení nákladů na inference. Karakuri vyvíjí japonské LLM pro podnikové aplikace, SplashMusic generuje hudbu pomocí AI a Decart se zaměřuje na optimalizaci AI workflow. Tyto případy ukazují praktické využití v cloudu. Na rozdíl od Nvidia GPU, které dominují trhu díky univerzálnosti, jsou Trainium čipy optimalizovány specificky pro AI trénink, což vede k vyšší efektivitě v této doméně. Oznámení Trainium4 s kompatibilitou k Nvidia naznačuje, že AWS nehodlá ignorovat ekosystém Nvidia CUDA, ale spíše ho doplní hybridními řešeními.

### Proč je to důležité
V éře explozivního růstu AI hardware je Trainium3 dalším krokem v konkurenci custom čipů (TPU od Google, Inferentia od AWS) proti Nvidia monopolům. Energetická úspora řeší klíčový bottleneck data center – spotřebu energie, která brzdí expanzi. Pro uživatele cloudy znamená nižší ceny tréninku a inference, což demokratizuje přístup k velkým AI modelům. Kompatibilita s Nvidia v Trainium4 umožní firmám mixovat hardware podle potřeb, což zvyšuje flexibilitu. Nicméně specifikace pocházejí z AWS, nezávislé benchmarky chybí, a dlouhodobý dopad závisí na adopci zákazníků. V širším kontextu posiluje to závod o suverénní AI infrastrukturu mezi cloudy, kde AWS drží silnou pozici.

---

[Číst původní článek](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/)

**Zdroj:** 🚀 TechCrunch
