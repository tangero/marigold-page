---
author: Marisa Aigen
category: ai hardware
companies:
- Amazon
- Nvidia
date: '2025-12-02 16:00:15'
description: Na konferenci Re:Invent Amazon oznámil, že Trainium4 akcelerátory použijí
  NVLink od Nvidia pro 6násobný výkon. Zároveň debutuje Trainium3 s možností milionových
  clusterů pro trénink AI modelů.
importance: 3
layout: tech_news_article
original_title: Amazon primed to fuse Nvidia's NVLink into 4th-gen Trainium accelerators
publishedAt: '2025-12-02T16:00:15+00:00'
slug: amazon-primed-to-fuse-nvidias-nvlink-into-4th-gen-
source:
  emoji: 📰
  id: null
  name: Theregister.com
title: Amazon integruje Nvidia NVLink do akcelerátorů Trainium čtvrté generace
url: https://www.theregister.com/2025/12/02/amazon_nvidia_trainium/
urlToImage: https://regmedia.co.uk/2025/07/03/trainium2_chip.jpg
urlToImageBackup: https://regmedia.co.uk/2025/07/03/trainium2_chip.jpg
---

## Souhrn
Amazon Web Services (AWS) na konferenci Re:Invent v Las Vegas představil akcelerátory Trainium3, které umožní clustery s miliony čipů pro trénink AI. Další generace Trainium4 integruje NVLink od Nvidia, což má přinést 6násobný výkon oproti předchozím verzím díky lepší propojitosti čipů.

## Klíčové body
- Trainium4 použije NVLink Fusion pro komunikaci mezi akcelerátory Trainium, procesory Graviton a síťovou technologií EFA.
- Očekávané zlepšení: 3násobný výkon v FP8, 6násobný v FP4 a 4násobná šířka pásma paměti.
- Trainium3 slibuje clustery s až milionem čipů pro trénink velkých AI modelů.
- NVLink 5. generace nabízí 1,8 TB/s šířky pásma na GPU, příští rok až 3,6 TB/s.
- Integrace probíhá v rackech Nvidia MGX.

## Podrobnosti
AWS na své konferenci Re:Invent 2. prosince 2025 oznámil pokroky ve vlastním hardware pro AI. Trainium je řada akcelerátorů určených primárně pro trénink velkých jazykových modelů a jiných AI systémů, které AWS vyvíjí, aby snížil závislost na externích dodavatelích jako Nvidia. Trainium3, který právě debutuje, je navržen pro škálování do clusterů s až milionem čipů, což umožní trénink extrémně velkých modelů na úrovni miliard parametrů efektivněji než u současných systémů.

Klíčovou novinkou je Trainium4, který poprvé přijme NVLink Fusion – vysokorychlostní propojovací technologii od Nvidia. NVLink umožňuje propojit více GPU nebo akcelerátorů napříč systémy tak, aby fungovaly jako jeden celek, s minimálními ztrátami při komunikaci. Dříve byla tato technologie omezena na Nvidia hardware, ale v květnu 2025 Nvidia otevřela NVLink Fusion třetím stranám na Computexu. AWS tak může integrovat své Trainium4, procesory Graviton (ARM-based CPU pro cloud) a síťovou technologii Elastic Fabric Adapter (EFA, vysokorychlostní síť pro HPC) přímo do racků Nvidia MGX. Aktuální pátá generace NVLink dosahuje 1,8 TB/s šířky pásma na GPU (900 GB/s oběma směry), přičemž Nvidia plánuje zdvojnásobení na 3,6 TB/s v roce 2026.

AWS neupřesnil, zda zlepšení výkonu (3x FLOPS v FP8 pro trénink, 6x v FP4 pro inference, 4x šířka pásma paměti) platí pro jednotlivé čipy nebo pro rackové systémy UltraServer. Při předpokladu racků, jako u Trainium3, by UltraServer Trainium4 mohl dosáhnout přes 2 exaFLOPS v FP4 a 2,8 PB/s šířky pásma paměti. To je výhoda pro inference úlohy omezené šířkou pásma. Jmenování je matoucí – Trainium slouží AWS interně i externě pro zákazníky přes služby jako SageMaker.

## Proč je to důležité
Tato integrace posiluje konkurenci v AI hardware, kde Nvidia dominuje s 80-90 % trhu GPU. AWS, který investoval miliardy do vlastních čipů (Trainium pro trénink, Inferentia pro inference), nyní spolupracuje s Nvidia místo konfrontace, což urychlí škálování clusterů pro zákazníky. Pro průmysl znamená lepší cenovou efektivitu tréninku velkých modelů, protože NVLink snižuje latenci komunikace v clusterech. Uživatelé AWS získají přístup k výkonnějším instancím bez nutnosti migrace na Nvidia-only ekosystém. V širším kontextu to ukazuje konsolidaci: i velcí hráči jako Amazon potřebují otevřené standardy pro hyperskálování AI, což může snížit ceny cloudových AI služeb o 20-40 % dlouhodobě.

---

[Číst původní článek](https://www.theregister.com/2025/12/02/amazon_nvidia_trainium/)

**Zdroj:** 📰 Theregister.com
