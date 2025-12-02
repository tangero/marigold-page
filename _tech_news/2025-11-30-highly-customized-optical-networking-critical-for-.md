---
author: Marisa Aigen
category: optické sítě
companies:
- Google
date: '2025-11-30 19:39:18'
description: Systém Google využívá optické obvodové přepínání (OCS) k vytvoření přímých
  optických cest s nízkou latencí mezi čipy TPU, což minimalizuje ztráty při konverzi
  signálů. Tím se vyhýbá opakovaným opticko-elektricko-optickým transformacím a umožňuje
  efektivní sdílení dat mezi tisíci čipů v jednom podu.
importance: 4
layout: tech_news_article
original_title: Highly Customized Optical Networking Critical for Google’s Tensor
  Processing Units (TPUs)
publishedAt: '2025-11-30T19:39:18+00:00'
slug: highly-customized-optical-networking-critical-for-
source:
  emoji: 📰
  id: next-big-future
  name: Next Big Future
title: Vysoce přizpůsobené optické sítě klíčové pro Tensor Processing Units (TPU)
  společnosti Google
url: https://www.nextbigfuture.com/2025/11/highly-customized-optical-networking-critical-for-googles-tensor-processing-units-tpus.html
urlToImage: https://nextbigfuture.s3.amazonaws.com/uploads/2025/11/Screenshot-2025-11-30-at-11.32.54-AM.jpg
urlToImageBackup: https://nextbigfuture.s3.amazonaws.com/uploads/2025/11/Screenshot-2025-11-30-at-11.32.54-AM.jpg
---

## Souhrn
Google představil sedmou generaci svých Tensor Processing Units (TPU) nazvanou Ironwood, která integruje pokročilé optické obvodové přepínání (OCS) pro komunikaci mezi čipy. Tento přístup snižuje latenci a spotřebu energie tím, že signály zůstávají v optické doméně po většinu doby. Ironwood přináší desetinásobný nárůst špičkového výkonu oproti TPU v5p a více než čtyřnásobný zlepšení výkonu na čip oproti TPU v6e.

## Klíčové body
- Optické obvodové přepínání (OCS) vytváří přímé optické cesty mezi čipy TPU bez opakovaných konverzí signálů.
- Ironwood TPU je optimalizováno pro trénink velkých modelů, posilování učení (RL), inference a serving AI modelů.
- Inter-Chip Interconnect (ICI) podporuje až 1,2 Tb/s bidirekční propustnost na čip v topologii 3D torus.
- Optické přepínače na bázi MEMS s 144×144 porty snižují spotřebu o 40 % a náklady o 30 % oproti elektrickým řešením.
- Nové instance na bázi Arm Axion (N4A, C4A) nabízejí lepší poměr ceny a výkonu než x86 alternativy.

## Podrobnosti
Systém Google pro TPU podsahuje tisíce čipů prozpracovávajících náročné AI úlohy, jako je trénink velkých jazykových modelů nebo inference v reálném čase. Klíčovým prvkem je Inter-Chip Interconnect (ICI), vysokorychlostní síť uvnitř a mezi TPU. Používá topologii 3D torus ve formě 4×4×4 kostek po 64 TPU, což zajišťuje nízký průměrný počet meziúsek pro spojování uzlů. V nedávných generacích dosahuje bidirekční propustnosti až 1,2 Tb/s na čip. Pro krátké vzdálenosti uvnitř kostek slouží přímé měděné kabely (DAC), zatímco mezi kostkami a na úrovni podu se přechází na optické přijímače – přibližně 1,5 optického přijímače na TPU.

Optické obvodové přepínače (OCS) jsou zde customizovaným řešením na bázi mikroelektromechanických systémů (MEMS). Obsahují 2D pole zrcadel, čočky a kamery pro řízení svazků světla. Tyto přepínače dynamicky rekonfigurují topologii, například do zkrouceného 3D torus, bez nutnosti elektrických přepínačů. Výsledkem je nižší režie, spotřeba energie o 40 % menší a náklady o 30 % nižší. Jeden OCS zvládá 144×144 portů a podporuje odolné směrování okolo poruch. Signály tak zůstávají optické po většinu komunikace mezi čipy, což eliminuje ztráty spojené s opakovanými konverzemi optika-elektronika-optika (OEO).

Ironwood, sedmá generace TPU, je navržena pro nejtěžší úlohy: od tréninku velkých modelů přes posilování učení až po vysokovýkonnou inferenci a serving modelů. Nabízí 10násobný špičkový výkon oproti TPU v5p a více než 4násobný výkon na čip oproti TPU v6e (Trillium) pro trénink i inferenci. Kromě toho Google zavádí instance na bázi Arm Axion: N4A jako nejvýkonnější virtuální stroj řady N z hlediska ceny/výkonu (až 2násobně lepší než současné x86 VM) a C4A jako první bare-metal instanci na Arm.

## Proč je to důležité
Tento vývoj řeší klíčové výzvy škálování AI: vysokou latenci a spotřebu energie v komunikaci mezi čipy při podpoře tisíců uzlů v jednom podu. V éře modelů s biliony parametrů je efektivní interkonekt esenciální pro udržitelný růst výpočetního výkonu. Optické sítě umožňují Google udržet náskok v AI infrastruktuře, což ovlivňuje cenu a dostupnost služeb jako Gemini nebo Cloud AI. Pro průmysl to znamená tlak na konkurenční řešení od Nvidia nebo AMD, kde elektrické sítě dosahují limitů. Dlouhodobě posiluje to pozici Google v tréninku a nasazení velkých modelů, přičemž Arm-based instance rozšiřují ekosystém o levnější alternativy k x86.

---

[Číst původní článek](https://www.nextbigfuture.com/2025/11/highly-customized-optical-networking-critical-for-googles-tensor-processing-units-tpus.html)

**Zdroj:** 📰 Next Big Future
