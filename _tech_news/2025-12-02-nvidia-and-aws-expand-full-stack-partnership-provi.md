---
author: Marisa Aigen
category: umělá inteligence
companies:
- NVIDIA
- AWS
date: '2025-12-02 16:00:27'
description: Na konferenci AWS re:Invent NVIDIA a Amazon Web Services rozšířily strategickou
  spolupráci o nové integrace v propojovacích technologiích, cloudové infrastruktuře,
  otevřených modelech a fyzické umělé inteligenci. AWS začne podporovat platformu
  NVIDIA NVLink Fusion pro nasazení vlastního křemíku, včetně čipů Trainium4 pro odvozování
  a trénink agentických AI modelů.
importance: 4
layout: tech_news_article
original_title: NVIDIA and AWS Expand Full-Stack Partnership, Providing the Secure,
  High-Performance Compute Platform Vital for Future Innovation
publishedAt: '2025-12-02T16:00:27+00:00'
slug: nvidia-and-aws-expand-full-stack-partnership-provi
source:
  emoji: 📰
  id: null
  name: Nvidia.com
title: NVIDIA a AWS rozšiřují komplexní partnerství a poskytují bezpečnou výpočetní
  platformu s vysokým výkonem pro budoucí inovace
url: https://blogs.nvidia.com/blog/aws-partnership-expansion-reinvent/
urlToImage: https://blogs.nvidia.com/wp-content/uploads/2025/12/nvidia-aws-lockup-corp-blog-1280x680-1.png
urlToImageBackup: https://blogs.nvidia.com/wp-content/uploads/2025/12/nvidia-aws-lockup-corp-blog-1280x680-1.png
---

## Souhrn
Na konferenci AWS re:Invent oznámily NVIDIA a Amazon Web Services rozšíření svého partnerství. Zaměřují se na integraci technologií propojení, cloudové infrastruktury, otevřených modelů a fyzické umělé inteligence. Klíčovým prvkem je podpora platformy NVIDIA NVLink Fusion pro AWS vlastní čipy Trainium4, Graviton procesory a Nitro systém virtualizace.

## Klíčové body
- AWS integruje NVIDIA NVLink Fusion s vlastním křemíkem Trainium4 pro odvozování a trénink agentických AI modelů, Graviton CPU pro obecné úlohy a Nitro systém pro virtualizaci.
- Použití NVLink scale-up propojení a MGX rackové architektury zrychluje výkon a čas nasazení cloudových AI schopností.
- AWS již nasadilo MGX racky s NVIDIA GPU v měřítku a nyní rozšiřuje ekosystém dodavatelů pro plné rackové nasazení včetně chlazení a napájení.
- Podpora Elastic Fabric Adapteru a Nitro systému zajišťuje kompatibilitu s existující infrastrukturou AWS.
- Citát Jensena Huanga: „Poptávka po GPU výpočtech exploduje – více výpočtů znamená chytřejší AI, což pohání širší využití a další poptávku.“

## Podrobnosti
Partnerství mezi NVIDIA a AWS, dvěma klíčovými hráči v oblasti cloudových výpočtů a umělé inteligence, se rozšiřuje o platformu NVLink Fusion. Tato platforma umožňuje customizaci AI infrastruktury tím, že spojuje NVLink scale-up propojení – vysokorychlostní interkonect pro přímé propojení více GPU nebo čipů – s rackovou architekturou NVIDIA MGX. AWS tak může integrovat svůj vlastní křemík: čipy Trainium4 určené pro odvozování (inference) modelů umělé inteligence a trénink agentických AI modelů, které simulují autonomní agenty schopné složitých úkolů; Graviton procesory, které jsou ARM-based CPU optimalizované pro širokou škálu cloudových úloh od webových serverů po datové analýzy; a Nitro systém, což je hypervizorová vrstva pro bezpečnou virtualizaci instancí v cloudu AWS.

AWS plánuje Trainium4 navrhnout přímo pro kompatibilitu s NVLink a MGX, což je první krok v dlouhodobé spolupráci. Společnost již nasadila racky MGX s NVIDIA GPU v produkčním měřítku, například v regionech pro trénink velkých jazykových modelů. Integrace NVLink Fusion zjednoduší nasazení a správu systémů napříč platformami AWS, protože umožňuje využít ekosystém dodavatelů NVIDIA pro kompletní rackové řešení – od racků a šasi přes napájecí a chladicí systémy. Dále Vera Rubin architektura NVIDIA na AWS podpoří Elastic Fabric Adapter (EFA), síťovou technologii pro vysokovýkonné výpočty, a Nitro systém, čímž zákazníci získají robustní síťové možnosti při plné kompatibilitě s cloudovou infrastrukturou. To urychlí rollout nových AI služeb, jako jsou instance s vyšší propustností pro trénink modelů typu Llama nebo Gemini.

Tato spolupráce navazuje na předchozí integrace, kde AWS využívá NVIDIA GPU pro své služby jako EC2 P5 instances. NVLink Fusion řeší klíčový problém škálovatelnosti v AI: tradiční propojení jako PCIe nebo InfiniBand nestačí pro clustery tisíců čipů potřebných pro trénink modelů s biliony parametrů.

## Proč je to důležité
Rozšíření partnerství posiluje pozici AWS v soutěži s Azure a Google Cloud, kde NVIDIA dominuje v GPU výpočtech. AWS snižuje závislost na NVIDIA GPU tím, že optimalizuje vlastní Trainium a Inferentia čipy pro inference, ale spoléhá se na NVLink pro škálování, což zvyšuje výkon o řády oproti současným řešením. Pro průmysl to znamená rychlejší a levnější AI trénink v cloudu, což urychlí vývoj aplikací jako autonomní agenti nebo fyzická AI pro robotiku. Zákazníci, včetně firem trénujících vlastní modely, získají vyšší propustnost a nižší latenci, což je klíčové v éře rostoucí poptávky po výpočtech. Kriticky řečeno, toto prohlubuje ekosystém NVIDIA, kde i konkurenti jako AWS musí integrovat jejich technologie, což může brzdit diverzifikaci čipového trhu mimo NVIDIA Grace Hopper nebo Blackwell platformy.

---

[Číst původní článek](https://blogs.nvidia.com/blog/aws-partnership-expansion-reinvent/)

**Zdroj:** 📰 Nvidia.com
