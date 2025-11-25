---
author: Marisa Aigen
category: ai infrastruktura
companies:
- Amazon
- NVIDIA
date: '2025-11-24 08:00:00'
description: Amazon SageMaker HyperPod nyní podporuje technologii NVIDIA Multi-Instance
  GPU (MIG), která umožňuje rozdělit jednu GPU na několik izolovaných instancí. Tato
  funkce zvyšuje využití hardwarových zdrojů při spouštění menších generativních AI
  úloh.
importance: 3
layout: tech_news_article
original_title: Amazon SageMaker HyperPod now supports NVIDIA Multi-Instance GPU (MIG)
  for generative AI tasks
publishedAt: '2025-11-24T08:00:00+00:00'
slug: amazon-sagemaker-hyperpod-now-supports-nvidia-mult
source:
  emoji: 📰
  id: null
  name: Amazon.com
title: Amazon SageMaker HyperPod nyní podporuje NVIDIA Multi-Instance GPU (MIG) pro
  generativní AI úlohy
url: https://aws.amazon.com/about-aws/whats-new/2025/11/sagemaker-hyperpod-nvidia-multi-instance-gpu/
---

## Souhrn
Amazon SageMaker HyperPod nyní podporuje technologii NVIDIA Multi-Instance GPU (MIG), díky níž lze jednu fyzickou GPU rozdělit na až sedm izolovaných virtuálních GPU. Tato funkce umožňuje efektivnější využití výpočetních zdrojů při provozu menších generativních AI (GenAI) úloh, jako jsou lehké inferenční modely nebo interaktivní notebooky.

## Klíčové body
- SageMaker HyperPod nyní podporuje MIG na clusterech s orchestrátorem EKS.
- Administrátoři mohou GPU dělit buď přes konzoli, nebo vlastní konfigurací pro přesné požadavky.
- Je možné alokovat kvóty pro spravedlivé rozdělení zdrojů mezi týmy.
- Systém poskytuje monitorovací dashboard s reálnými metrikami využití jednotlivých GPU partit.
- Funkce je dostupná v 17 regionech AWS po celém světě.

## Podrobnosti
NVIDIA Multi-Instance GPU (MIG) je hardwarová technologie dostupná na GPU řady A100 a H100, která umožňuje fyzicky izolovat jednotlivé části GPU – včetně paměti, cache a výpočetních jednotek – a přidělit je různým úlohám. V rámci Amazon SageMaker HyperPod, což je spravovaná platforma pro škálovatelné trénování a nasazení AI modelů, lze nyní tuto funkci využít pro optimalizaci nákladů a výkonu. Administrátoři mohou například spustit několik lehkých inferenčních služeb nebo Jupyter notebooků pro datové vědce paralelně na jedné GPU, aniž by docházelo ke vzájemnému ovlivňování výkonu. Platforma nabízí jak jednoduché nastavení přes webovou konzoli, tak pokročilé možnosti konfigurace pro specifické požadavky. Díky integrovanému monitorování lze sledovat vytížení jednotlivých partit a dynamicky upravovat alokaci zdrojů. Tato funkce je aktuálně dostupná pouze pro clustery SageMaker HyperPod využívající Kubernetes orchestrátor EKS a je nasazena v 17 regionech AWS, včetně Evropy (Ireland, Frankfurt, Londýn, Stockholm, Španělsko) a Asie (Tokyo, Seoul, Singapur, Sydney a další).

## Proč je to důležité
Efektivní využití GPU je klíčové pro ekonomiku provozu generativních AI modelů, které často nevyužívají plnou kapacitu drahých akcelerátorů. MIG v kombinaci se SageMaker HyperPod umožňuje organizacím snížit náklady a zároveň zkrátit čekací doby pro vývojáře a datové vědce. Tento krok posiluje konkurenceschopnost AWS v oblasti AI infrastruktury, zejména vůči Azure a Google Cloud, které nabízejí podobné mechanismy izolace zdrojů. Pro průmysl to znamená větší flexibilitu při nasazování hybridních úloh – od trénování velkých modelů po běh lehkých inferencí – na stejném hardwarovém základě.

---

[Číst původní článek](https://aws.amazon.com/about-aws/whats-new/2025/11/sagemaker-hyperpod-nvidia-multi-instance-gpu/)

**Zdroj:** 📰 Amazon.com
