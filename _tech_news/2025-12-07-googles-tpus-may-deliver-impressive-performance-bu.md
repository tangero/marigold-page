---
author: Marisa Aigen
category: ai čipy
companies:
- Google
date: '2025-12-07 13:34:06'
description: Sedmá generace TPU Ironwood od Google vzbudila zájem firem jako Meta
  a Anthropic díky slibnému výkonu pro AI inferenci, avšak problémy s dodávkami pokročilého
  balení od TSMC ohrožují možnost škálování pro externí zákazníky.
importance: 4
layout: tech_news_article
original_title: Google’s TPUs May Deliver ‘Impressive’ Performance, But One Overlooked
  Bottleneck Could Bring External Scaling to a Halt Before It Even Begins
publishedAt: '2025-12-07T13:34:06+00:00'
slug: googles-tpus-may-deliver-impressive-performance-bu
source:
  emoji: 📰
  id: null
  name: Wccftech
title: TPU od Google mohou přinést působivý výkon, ale přehlížené omezení v dodavatelském
  řetězci by mohlo zastavit externí škálování ještě před zahájením
url: https://wccftech.com/google-tpu-may-deliver-impressive-performance-but-one-overlooked-bottleneck-could-bring-external-scaling-to-a-halt/
urlToImage: https://cdn.wccftech.com/wp-content/uploads/2025/12/Ironwood.original-scaled.jpg
urlToImageBackup: https://cdn.wccftech.com/wp-content/uploads/2025/12/Ironwood.original-scaled.jpg
---

## Souhrn
Google nedávno představil sedmou generaci svých AI čipů TPU pod názvem Ironwood, které slibují lepší celkové náklady na vlastnictví (TCO) a vyšší výkon při inferenci velkých jazykových modelů. Firmy jako Meta a Anthropic projevily zájem o jejich integraci do svých systémů, což naznačuje rostoucí externí adopci. Nicméně zprávy odhalují klíčové omezení v dodavatelském řetězci, zejména nedostatek pokročilého balení CoWoS od TSMC, které brání masové výrobě.

## Klíčové body
- Google TPUv7 Ironwood přijímá design MCM (Multi-Chip Module) s více křemíkovými čipy na interposeru pro vyšší výkon oproti monolithickým die.
- Zájem od Meta, Anthropic a dokonce partnerů NVIDIA jako Foxconn, kteří objednávají TPU racky.
- Hlavní bottleneck: Nedostatek CoWoS balení od TSMC, nutného pro MCM strukturu.
- To ohrožuje Google v expanzi na trh AI infrastruktury mimo vlastní cloud.
- Srovnání s NVIDIA: TPUs by mohly dominovat v inferenci díky lepšímu TCO.

## Podrobnosti
Google Cloud představil TPUv7 Ironwood jako další krok v optimalizaci AI výpočtů, zaměřený především na inferenci – fázi, kdy trénovaní modely jako GPT nebo Gemini generují odpovědi na požadavky uživatelů. Na rozdíl od předchozích generací TPUv7 nepoužívá velký monolithický čip, ale MCM design: několik menších křemíkových die je spojeno na křemíkovém interposeru pomocí mikrobumps. Tato technologie umožňuje vyšší hustotu transistorů, lepší škálovatelnost a nižší spotřebu energie, což je klíčové pro datová centra s tisíci AI akcelerátorů.

Zprávy z ChinaTimes upozorňují, že Google má problém s objemem výroby kvůli závislosti na TSMC, největším výrobci pokročilých polovodičů. Technologie CoWoS (Chip on Wafer on Substrate) je nezbytná pro MCM balení – umožňuje spojit více čipů do jednoho balíčku s vysokorychlostními spojnicemi. TSMC však čelí obrovskému poptávce po CoWoS od NVIDIA (pro GPU jako H100/B200), Apple a dalších, což vede k nedostatku kapacity. Výsledkem je, že Google nemůže rychle rampovat produkci TPUv7 pro externí zákazníky.

Tento problém se projevuje v kontextu širšího zájmu o TPUs. Meta a Anthropic, kteří dosud spoléhali na NVIDIA GPU, testují TPUs pro své workloady. Dokonce partneři NVIDIA jako Foxconn objednávají TPU racky, což signalizuje posun v ekosystému. TPUs jsou optimalizovány pro Google frameworky jako JAX nebo TensorFlow, což usnadňuje nasazení v cloudových službách, ale pro on-premise nasazení vyžadují specifickou infrastrukturu. Pokud Google nedokáže dodat dostatek čipů, externí adopce se zpomalí, což posílí dominanci NVIDIA na trhu AI hardware.

## Proč je to důležité
Tento bottleneck podtrhuje zranitelnost AI trhu vůči dodavatelským řetězcům. TPUs by mohly snížit závislost na NVIDIA GPU, které dominují 80-90 % trhu s AI akcelerátory díky univerzálnosti a CUDA ekosystému. Lepší TCO TPU (nižší cena za FLOPS při inferenci) by umožnilo firmám jako Anthropic (vývojáři modelu Claude) nebo Meta (Llama modely) efektivněji škálovat AI služby. Pokud se Google nepodělí o trh, zpomalí to diverzifikaci hardware, zvýší ceny a oddálí pokroky v AGI. Pro průmysl to znamená nutnost sledovat alternativy jako AMD MI300 nebo čipové továrny v Číně, zatímco uživatelé cloudových AI služeb pocítí vyšší latency při nedostatku kapacity.

---

[Číst původní článek](https://wccftech.com/google-tpu-may-deliver-impressive-performance-but-one-overlooked-bottleneck-could-bring-external-scaling-to-a-halt/)

**Zdroj:** 📰 Wccftech
