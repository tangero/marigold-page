---
author: Marisa Aigen
category: ai hardware
companies:
- AWS
- NVIDIA
date: '2025-12-02 06:16:06'
description: S rostoucí poptávkou po AI hledají hyperscalers způsoby, jak urychlit
  nasazení specializované AI infrastruktury s vysokým výkonem. AWS spolupracuje s
  NVIDIA na integraci NVLink Fusion pro Trainium4 AI čipy, Graviton CPU a další komponenty.
importance: 4
layout: tech_news_article
original_title: AWS Integrates AI Infrastructure with NVIDIA NVLink Fusion for Trainium4
  Deployment
publishedAt: '2025-12-02T06:16:06+00:00'
slug: aws-integrates-ai-infrastructure-with-nvidia-nvlin
source:
  emoji: 📰
  id: null
  name: Nvidia.com
title: AWS integruje AI infrastrukturu s NVIDIA NVLink Fusion pro nasazení Trainium4
url: https://developer.nvidia.com/blog/aws-integrates-ai-infrastructure-with-nvidia-nvlink-fusion-for-trainium4-deployment/
urlToImage: https://developer-blogs.nvidia.com/wp-content/uploads/2025/12/grace-corp-blog-gb300-nvl72-1280x680-r1-2.png
urlToImageBackup: https://developer-blogs.nvidia.com/wp-content/uploads/2025/12/grace-corp-blog-gb300-nvl72-1280x680-r1-2.png
---

## Souhrn
Amazon Web Services oznámil na konferenci AWS re:Invent spolupráci s NVIDIA na integraci platformy NVLink Fusion. Tato racková řešení umožní rychlejší nasazení Trainium4 AI čipů, Graviton CPU, Elastic Fabric Adapters (EFA) a virtualizační infrastruktury Nitro System. Cílem je zefektivnit výstavbu custom AI racků s vysokou propustností a nízkou latencí.

## Klíčové body
- AWS navrhuje Trainium4 pro kompatibilitu s NVLink 6 a rackovou architekturou NVIDIA MGX, což je první krok v dlouhodobé spolupráci.
- NVLink Fusion poskytuje scale-up síťování pro propojení celých racků akcelerátorů v jediné fabric.
- Řešení snižuje vývojové cykly pro custom AI křemíky, zvyšuje návratnost investic a minimalizuje rizika nasazení.
- Podporuje rostoucí AI úlohy jako plánování, uvažování a agentickou AI na modelech s stovkami miliard až biliony parametrů.
- Ekosystém partnerů NVIDIA usnadňuje vývoj a nasazení.

## Podrobnosti
Trainium4 představuje čtvrtou generaci AI akcelerátorů od AWS, určených primárně pro trénink velkých jazykových modelů a jiných náročných AI úloh. Na rozdíl od NVIDIA GPU, které dominují trhu, Trainium čipy optimalizují náklady na trénink v cloudu AWS, kde slouží k výpočtům v paralelních clusterech. Nová integrace s NVLink Fusion, což je racková platforma NVIDIA, umožňuje propojit tyto čipy s vysokorychlostní interconnect technologiemi NVLink. NVLink 6 nabízí vyšší propustnost než předchozí verze a slouží k scale-up propojení akcelerátorů v rámci jednoho racku, což je klíčové pro modely typu mixture-of-experts (MoE) nebo agentické systémy.

AWS kombinuje Trainium4 s vlastními Graviton CPU (ARM-based procesory pro obecné výpočty), EFA (síťové adaptéry pro scale-out komunikaci mezi uzly) a Nitro System (virtualizační vrstva pro bezpečné izolované instance). NVIDIA MGX je modulární racková architektura, která umožňuje hyperscalerům jako AWS sestavovat custom řešení z komponent NVIDIA a partnerů. Tato spolupráce řeší hlavní výzvy: dlouhé vývojové cykly pro rackovou architekturu, nutnost vyvíjet vlastní scale-up a scale-out sítě i úložiště. Bez takového propojení by nasazení stovek akcelerátorů v paralelním fabric trvalo měsíce nebo roky.

Hyperscalers čelí tlaku od rostoucích AI workloadů – modely s biliony parametrů vyžadují tisíce akcelerátorů propojených nízkou latencí. NVLink Fusion toto umožňuje přímo v racku, což zkracuje čas na trh a snižuje náklady oproti plně proprietárním řešením. AWS tak posiluje svou pozici v AI cloudu, kde konkuruje NVIDIA H100 nebo Blackwell GPU, ale nabízí levnější alternativu pro zákazníky.

## Proč je to důležité
Tato integrace urychlí nasazení custom AI infrastruktury pro hyperscalery a enterprise zákazníky, což ovlivní cenu tréninku velkých modelů. AWS snižuje závislost na NVIDIA GPU tím, že Trainium4 kombinuje s NVLink, což zvyšuje efektivitu oproti čistě NVIDIA stackům. V širším kontextu posiluje to soutěž v AI hardware, kde hyperscalers jako AWS, Google (TPU) nebo Microsoft (Azure Cobalt) budují vlastní křemíky. Pro průmysl znamená rychlejší vývoj agentických AI a MoE modelů, menší rizika výpadků a vyšší ROI. Dlouhodobě to může democratizovat přístup k výkonné AI infrastruktuře, ale závisí na reálných benchmarkách Trainium4 oproti konkurenci.

---

[Číst původní článek](https://developer.nvidia.com/blog/aws-integrates-ai-infrastructure-with-nvidia-nvlink-fusion-for-trainium4-deployment/)

**Zdroj:** 📰 Nvidia.com
