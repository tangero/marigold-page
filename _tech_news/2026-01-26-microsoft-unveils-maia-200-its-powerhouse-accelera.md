---
author: Marisa Aigen
category: ai hardware
companies:
- Microsoft
date: '2026-01-26 16:00:00'
description: Maia 200 s více než 100 miliardami tranzistorů nabízí vysoký výkon pro
  AI inferencing, překonává konkurenty od AWS a Google Cloud.
importance: 4
layout: tech_news_article
original_title: Microsoft unveils Maia 200, its 'powerhouse' accelerator looking to
  unlock the power of large-scale AI
publishedAt: '2026-01-26T16:00:00+00:00'
slug: microsoft-unveils-maia-200-its-powerhouse-accelera
source:
  emoji: 📰
  id: techradar
  name: TechRadar
title: Microsoft představuje Maia 200, svůj 'powerhouse' akcelerátor pro velkoškálovou
  AI
url: https://www.techradar.com/pro/microsoft-unveils-maia-200-its-powerhouse-accelerator-looking-to-unlock-the-power-of-large-scale-ai
urlToImage: https://cdn.mos.cms.futurecdn.net/BSVBEAGEWfwryuSnecEAQm-970-80.jpg
urlToImageBackup: https://cdn.mos.cms.futurecdn.net/BSVBEAGEWfwryuSnecEAQm-970-80.jpg
---

## Souhrn
Microsoft představil Maia 200, nástupce čipu Maia 100, který je určen pro zpracování inference u velkých AI modelů. Tento akcelerátor s více než 100 miliardami tranzistorů na TSMC 3nm procesu dosahuje výkonu přes 10 PFLOPS v 4bitové přesnosti (FP4) a kolem 5 PFLOPS v 8bitové (FP8), což umožňuje efektivní provoz i největších současných modelů.

## Klíčové body
- Více než 100 miliard tranzistorů na TSMC 3nm procesu s nativními FP8/FP4 tensor cores pro rychlé vektorové operace v AI.
- Přepracovaný paměťový systém: 216 GB HBM3e při přenosové rychlosti 7 TB/s a 272 MB on-chip SRAM pro lokální ukládání dat.
- Výkon: přes 10 PFLOPS (FP4) a asi 5 PFLOPS (FP8), což je 3x více v FP4 než třetí generace Amazon Trainium a lepší v FP8 než sedmá generace Google TPU.
- Optimalizace pro inference: specializovaný DMA engine, NoC fabric pro vysokorychlostní přenos dat a zaměření na úzkopřesné datové typy.
- Použití: interně pro zlepšení Copilotu v Azure, dostupné i pro zákazníky.

## Podrobnosti
Maia 200 představuje významný krok v hardwarové infrastruktuře Microsoftu pro umělou inteligenci, konkrétně pro fázi inference, kdy se trénované AI modely používají k generování odpovědí v reálném čase. Na rozdíl od trénovacích čipů jako Nvidia H100 se Maia 200 soustředí na efektivitu při opakovaném spouštění modelů, což je klíčové pro služby jako ChatGPT nebo Microsoft Copilot. Čip je vyroben na pokročilém 3nm procesu od TSMC, což umožňuje vysokou hustotu tranzistorů a nižší spotřebu energie.

Klíčovou inovací je paměťový subsystém optimalizovaný pro úzkopřesné datové typy jako FP4 a FP8, které snižují velikost dat bez výrazné ztráty přesnosti u velkých jazykových modelů (LLM). HBM3e paměť o objemu 216 GB s bandwidth 7 TB/s zajišťuje rychlý přístup k velkým objemům dat, zatímco 272 MB SRAM na čipu minimalizuje latenci tím, že drží většinu vah modelů lokálně. Specializovaný DMA engine a NoC (Network-on-Chip) fabric usnadňují přenos dat mezi jádry, což vede k potřebě méně čipů pro spuštění stejného modelu – například oproti předchozí generaci nebo konkurenčním řešením.

Microsoft tvrdí, že Maia 200 dramaticky mění ekonomiku velkoškálové AI tím, že zvyšuje výkon a snižuje náklady na provoz v cloudu Azure. Bude sloužit k internímu zlepšení Copilotu, což je AI asistent integrovaný do Office a Windows, ale stane se dostupným i pro zákazníky Azure, kteří chtějí rychleji a levněji spouštět vlastní modely. V porovnání s konkurencí: 3x vyšší FP4 výkon než Amazon Trainium3 (určený pro trénink i inference v AWS) a vyšší FP8 než Google TPUv7 (Tensor Processing Unit pro Google Cloud). To posiluje pozici Azure v soutěži o AI workloady, kde Nvidia stále dominuje, ale cloudoví giganti budují vlastní čipy pro nezávislost.

## Proč je to důležité
V éře explodujících nároků na výpočetní výkon pro AI inference, kde modely jako GPT-4o nebo Llama 3 vyžadují obrovské zdroje, Maia 200 umožňuje škálovat služby bez proporcionalního růstu nákladů. Pro průmysl znamená větší efektivitu v cloudu, méně závislosti na Nvidia a konkurenční tlak na AWS a GCP k inovacím. Pro uživatele Azure to přinese rychlejší AI aplikace, jako lepší Copilot v Teams nebo Edge, a potenciálně nižší ceny. Dlouhodobě posiluje Microsoft v závodě o AI dominanci, kde hardware rozhoduje o maržích a rychlosti nasazení nových modelů. Celkově přispívá k demokratizaci velké AI tím, že snižuje bariéry pro enterprise nasazení.

---

[Číst původní článek](https://www.techradar.com/pro/microsoft-unveils-maia-200-its-powerhouse-accelerator-looking-to-unlock-the-power-of-large-scale-ai)

**Zdroj:** 📰 TechRadar
