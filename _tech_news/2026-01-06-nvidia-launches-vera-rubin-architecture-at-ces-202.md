---
author: Marisa Aigen
category: hardware
companies:
- NVIDIA
date: '2026-01-06 06:18:03'
description: Na CES 2026 NVIDIA odhalila platformu Rubin s rack-scale systémem Vera
  Rubin NVL72, což je třetí generace její rackové architektury kombinující šest spoludizajnovaných
  čipů do jednoho systému. Platforma bude dostupná od partnerů ve druhé polovině roku
  2026, čipy jsou již vyrobeny a testovány s reálnými úlohami.
importance: 4
layout: tech_news_article
original_title: 'NVIDIA Launches Vera Rubin Architecture at CES 2026: The VR NVL72
  Rack'
publishedAt: '2026-01-06T06:18:03+00:00'
slug: nvidia-launches-vera-rubin-architecture-at-ces-202
source:
  emoji: 📰
  id: null
  name: Storagereview.com
title: 'NVIDIA představila architekturu Vera Rubin na CES 2026: rack VR NVL72'
url: https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack
urlToImage: https://www.storagereview.com/wp-content/uploads/2026/01/StorageReview-NVIDIA-CES-Keynote-2026-14.jpg
urlToImageBackup: https://www.storagereview.com/wp-content/uploads/2026/01/StorageReview-NVIDIA-CES-Keynote-2026-14.jpg
---

## Souhrn
Na veletrhu CES 2026 NVIDIA představila platformu Rubin, jejímž stěžejním prvkem je rack-scale systém Vera Rubin NVL72. Tento systém spojuje šest čipů navržených společně tak, aby fungovaly jako jednotný celek, a představuje třetí generaci rackových architektur NVIDIA. Všechny čipy prošly výrobou a nyní procházejí validací s reálnými výpočetními úlohami v AI.

## Klíčové body
- Systém Vera Rubin NVL72 obsahuje 72 Rubin GPU a 36 Vera CPU s 88 ARM jádry Olympus na každý CPU.
- FP4 inference výkon dosahuje 3,6 ExaFLOPS, což je 2,5násobek oproti Blackwell Ultra NVL72 (1,44 ExaFLOPS).
- Vera CPU nabízí NVLink-C2C připojení s 1,8 TB/s šířkou pásma k GPU, dvojnásobek oproti předchozí generaci.
- GPU používají HBM4 paměť s přibližně 22 TB/s šířkou pásma a NVLink 6 s 3,6 TB/s na GPU.
- Platforma je určena pro AI továrny, zaměřené na datové pohyby a agentické zpracování.

## Podrobnosti
Vera Rubin NVL72 staví na konceptu tzv. extrémního spoludizajnu, při kterém NVIDIA vyvíjí šest různých čipů současně, aby maximalizovaly vzájemnou kompatibilitu a výkon v rackovém formátu. Klíčovým prvkem je Vera CPU, postavený na 88 vlastních ARM jádrech Olympus s plnou kompatibilitou Armv9.2. Tento procesor je optimalizován pro AI továrny, kde řeší nároky na pohyb dat a agentické zpracování – tj. autonomní AI agenty schopné rozhodování a interakce. Vera CPU zdvojnásobuje výkon v datovém zpracování, kompresi a kompilaci kódu oproti předchozí Grace CPU a díky NVLink-C2C připojení dosahuje 1,8 TB/s šířky pásma k Rubin GPU, což je sedminásobek rychlosti PCIe Gen 6.

Pro srovnání s předchozí generací Blackwell Ultra NVL72:

| Specifikace              | GB300 NVL72 (Blackwell Ultra) | VR NVL72 (Vera Rubin) |
|---------------------------|-------------------------------|-----------------------|
| GPU počet                 | 72 Blackwell Ultra GPU       | 72 Rubin GPU         |
| CPU počet                 | 36 Grace CPU                 | 36 Vera CPU          |
| CPU jádra na CPU          | 72 ARM jádra                 | 88 Olympus ARM jádra |
| FP4 inference výkon       | 1,44 ExaFLOPS                | 3,6 ExaFLOPS         |
| NVFP4 na GPU (inference)  | 20 PFLOPS                    | 50 PFLOPS            |
| NVFP4 na GPU (trénink)    | 10 PFLOPS                    | 35 PFLOPS            |
| GPU paměť                 | HBM3e                        | HBM4                 |
| GPU paměťová šířka pásma  | ~8 TB/s                      | ~22 TB/s             |
| NVLink generace           | NVLink 5                     | NVLink 6             |
| NVLink šířka pásma na GPU | 1,8 TB/s                     | 3,6 TB/s             |

Rubin GPU přinášejí NVFP4 formát pro inference (50 PFLOPS na GPU) a trénink (35 PFLOPS), což umožňuje efektivnější zpracování velkých jazykových modelů (LLM) a jiných AI úloh. Systém je navržen pro datová centra, kde slouží k tréninku a nasazení AI modelů v měřítku exaFLOPS. NVIDIA plánuje dodávky od partnerů od léta 2026, což znamená, že reálné nasazení přijde až po validaci.

## Proč je to důležité
Tato platforma posiluje dominanci NVIDIA v hardwaru pro AI, kde rackové systémy jako NVL72 umožňují škálování na úrovni tisíců GPU bez ztráty efektivity. Pro průmysl to znamená rychlejší inference pro velké LLM, nižší spotřebu energie na FLOPS a lepší podporu agentických AI systémů, které simulují složité pracovní toky. V kontextu soutěže s AMD a Intel to udržuje NVIDIA náskok v NVLink propojení, ale závislost na HBM4 paměti zvyšuje náklady. Pro uživatele v enterprise segmentu to otevírá dveře k výkonnějším AI továrnám, avšak s dodací lhůtou 2026 to zatím neovlivní aktuální nasazení. Celkově urychluje přechod k hyperskálovým AI infrastrukturám potřebným pro pokročilé modely.

---

[Číst původní článek](https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack)

**Zdroj:** 📰 Storagereview.com
