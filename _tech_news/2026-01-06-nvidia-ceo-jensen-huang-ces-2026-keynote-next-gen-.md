---
author: Marisa Aigen
category: grafické procesory
companies:
- Nvidia
date: '2026-01-06 03:12:44'
description: Jensen Huang představil nejnovější technologii Nvidia včetně nových čipů
  Rubin GPU. Architektura Vera Rubin řeší rostoucí poptávku po výpočetním výkonu pro
  AI, kde modely rostou 10násobně každý rok a uvažování přidává další výpočetní nároky.
importance: 4
layout: tech_news_article
original_title: Nvidia CEO Jensen Huang CES 2026 Keynote – Next Gen Rueben GPU in
  Full Production. 5X Blackwell FP
people:
- Jensen Huang
publishedAt: '2026-01-06T03:12:44+00:00'
slug: nvidia-ceo-jensen-huang-ces-2026-keynote-next-gen-
source:
  emoji: 📰
  id: next-big-future
  name: Next Big Future
title: Prezident Nvidia Jensen Huang na CES 2026 – Nová generace Rubin GPU v plné
  produkci. 5násobný výkon Blackwella v FP
url: https://www.nextbigfuture.com/2026/01/nvidia-ceo-jensen-huang-ces-2026-keynote-next-gen-rueben-gpu-in-full-production-5x-blackwell-fp.html
urlToImage: https://nextbigfuture.s3.amazonaws.com/uploads/2026/01/Screenshot-2026-01-05-at-7.18.27-PM.jpg
urlToImageBackup: https://nextbigfuture.s3.amazonaws.com/uploads/2026/01/Screenshot-2026-01-05-at-7.18.27-PM.jpg
---

## Souhrn
Na konferenci CES 2026 prezident Nvidia Jensen Huang oznámil, že nová generace čipů Rubin je již v plné produkci a nabízí pětinásobný výkon oproti předchozí architektuře Blackwell v plovoucí čárce (FP). Tato platforma, zahrnující Vera CPU a Rubin GPU, je navržena pro extrémní AI výpočty v podnicích s tisíci GPU. Oznámení přichází v době, kdy poptávka po výkonu pro trénink velkých jazykových modelů exploduje.

## Klíčové body
- Rubin GPU dosahuje 5násobného výkonu Blackwella v FP, s 1,6násobným počtem tranzistorů.
- Pod jedním rackem lze propojit 72 kusů Rubin GPU (každý s dvěma čipy), celkově 1152 GPU v 16 rackech.
- Vera CPU má 88 jader (176 vláken díky prostorovému multitheadingu) a dvojnásobný výkon na watt oproti špičkovým CPU.
- Síťové komponenty jako ConnectX-9 (1,6 TB/s) a NVLink 6 umožňují nízkou latenci pro velké AI klastry.
- Vývoj zapojil 15 000 inženýrských let a zahrnoval extrémní souběžný design všech čipů.

## Podrobnosti
Architektura Vera Rubin, pojmenovaná po americké astronomce, představuje komplexní platformu sestávající ze šesti čipů: Vera CPU, Rubin GPU, výpočetní desky (100 petaflopů AI, 5násobek předchozí generace), ConnectX-9 síťové karty s 1,6 TB/s propustností, BlueField-4 DPU pro odlehčení úložiště a bezpečnosti a NVLink-6 switche pro škálování 72 GPU jako jednoho. Rubin GPU je klíčovým prvkem, navrženým pro nízkou latenci při sdílení dat, s NVFP4 tensorovými jádry, která adaptivně upravují přesnost pro transformery – což by mohlo stanout novým standardem v AI akceleraci. Každý rack obsahuje 18 podnosů, 9 switchů, 220 bilionů tranzistorů a váží přibližně 2 tuny. Nvidia předvedla Rubin pod s 1152 GPU v 16 rackech, kde každý rack pojme 72 Rubinů (dva čipy na GPU).

Vývoj probíhal za pomoci přístupu "extreme co-design", při kterém byly všechny čipy navrženy souběžně, navzdory tradičním pravidlům, kvůli zpomalení Mooreova zákona. To umožnilo překonat limity tranzistorů optimalizací na úrovni systému. GB200 a GB300 jsou již v produkci, Vera Rubin následuje ihned. MGX šasi revolučně zjednodušila montáž z 2 hodin na 5 minut, bez kabelů, hadic či ventilátorů, s 100% kapalinovým chlazením. Síť Spectrum-X Ethernet Photonix podporuje 512 drah a 200 Gbit optiku pro AI továrny.

Tato platforma řeší realitu, kde AI modely rostou 10násobně ročně, tokeny v inferenci se zvyšují 5násobně a náklady klesají 10násobně díky konkurenci. Post-trénink využívá reinforcement learning, inferenční fáze multi-tokenovou predikci. Pro uživatele znamená rychlejší trénink větších modelů, nižší latency v produkčních AI službách a lepší škálovatelnost datacenter.

## Proč je to důležité
V éře, kdy AI vyžaduje exabyte dat a eksaflopové výpočty, Rubin posiluje dominanci Nvidia v AI hardwaru, umožňujíc hyperscalerům jako OpenAI nebo Google budovat klastry pro modely s miliardami parametrů. Zrychlení vývoje (plná produkce dříve než očekáváno) signalizuje závod o výpočetní převahu, kde hardware určuje tempo pokroku v LLM a uvažujících AI. Pro průmysl to znamená nižší náklady na AI nasazení, ale zároveň rizika koncentrace moci u jedné firmy. Kriticky: přestože 5násobný skok je působivý, dlouhodobě bude záviset na softwarové optimalizaci a energetické efektivitě, aby udržel tempo s datovou explozí.

---

[Číst původní článek](https://www.nextbigfuture.com/2026/01/nvidia-ceo-jensen-huang-ces-2026-keynote-next-gen-rueben-gpu-in-full-production-5x-blackwell-fp.html)

**Zdroj:** 📰 Next Big Future
