---
author: Marisa Aigen
category: kvantové počítačství
companies:
- NVIDIA
- žádné
date: '2025-11-17 22:32:14'
description: Kvantové počítačství vstupuje do nové éry, kdy bude jeho pokrok určován
  těsnou integrací akcelerovaných výpočtů s kvantovými procesory. NVIDIA představila
  otevřenou architekturu NVQLink, která propojuje GPU superčipy s řadiči kvantových
  systémů.
importance: 4
layout: tech_news_article
original_title: NVIDIA NVQLink Architecture Integrates Accelerated Computing with
  Quantum Processors
publishedAt: '2025-11-17T22:32:14+00:00'
slug: nvidia-nvqlink-architecture-integrates-accelerated
source:
  emoji: 📰
  id: null
  name: Nvidia.com
title: Architektura NVIDIA NVQLink propojuje akcelerované výpočty s kvantovými procesory
url: https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/
urlToImage: https://developer-blogs.nvidia.com/wp-content/uploads/2025/11/nvqlink-1.jpg
urlToImageBackup: https://developer-blogs.nvidia.com/wp-content/uploads/2025/11/nvqlink-1.jpg
---

## Souhrn
NVIDIA představila architekturu NVQLink, která integruje akcelerované výpočty na bázi GPU s kvantovými procesory (QPU). Cílem je řešit náročné úlohy jako dekódování kvantové korekce chyb (QEC) a kontinuální kalibraci v reálném čase, které jsou nezbytné pro praktické nasazení kvantových počítačů.

## Klíčové body
- NVQLink je otevřená platforma pro těsné propojení superpočítačového hostitele s řadičem kvantového systému (QSC).
- Architektura podporuje různé typy kvantových technologií: supravodivé, iontové, fotonické i spinové qubity.
- Definuje nový strojový model „Logický QPU“, který zahrnuje fyzické qubity, řídicí elektroniku i výpočetní zdroje pro online úlohy.
- Propojuje svět kvantové koherentní kontroly se stávajícími superpočítačovými systémy NVIDIA.

## Podrobnosti
NVQLink řeší klíčový problém současného kvantového vývoje: řídicí a měřicí systémy kvantových procesorů vyžadují extrémně náročné výpočty v reálném čase. Ty zahrnují dekódování kvantové korekce chyb (QEC), která je nezbytná pro odolnost proti chybám v budoucích chybově odolných kvantových počítačích, a neustálou kalibraci qubitů. Tyto úlohy nelze efektivně zvládnout tradičními procesory – vyžadují akcelerované výpočty na úrovni dnešních GPU superčipů, jako jsou NVIDIA H100 nebo Grace Hopper.

Architektura NVQLink definuje tzv. Logický QPU – komplexní systém, který zahrnuje nejen fyzické qubity a jejich řídicí elektroniku, ale i výpočetní uzel schopný zpracovávat online úlohy. Ten je propojen s kvantovým řadičem nízkolatentním, škálovatelným interkonexním rozhraním. Díky tomu může být superpočítačový uzel považován za nativní součást kvantového prostředí. Platforma je navržena jako otevřená a neutrální vůči konkrétní kvantové technologii, což umožňuje vývojářům QPU a řadičů inovovat bez omezení.

## Proč je to důležité
Integrace akcelerovaných výpočtů do kvantového stacku je zásadní pro dosažení praktického kvantového výhodného (quantum advantage). Bez efektivního zpracování QEC a kalibrace nebude možné škálovat kvantové systémy na počet qubitů nutný pro reálné aplikace. NVQLink tak představuje infrastrukturní most mezi dnešním HPC (high-performance computing) a budoucím kvantovým výpočtem. Pro průmysl to znamená možnost využít stávající ekosystém NVIDIA – včetně softwaru, nástrojů a programovacích jazyků jako C++ nebo Python – pro vývoj kvantových řešení. Tento krok posiluje postavení NVIDIA nejen v AI a HPC, ale i v rychle rostoucím kvantovém sektoru.

---

[Číst původní článek](https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/)

**Zdroj:** 📰 Nvidia.com
