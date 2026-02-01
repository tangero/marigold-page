---
author: Marisa Aigen
category: ai hardware
companies:
- Microsoft
- TSMC
date: '2026-01-27 02:07:44'
description: Microsoft 27. ledna oficiálně představil svůj druhý AI akcelerátor Maia
  200, čímž pokračuje v úsilí o vývoj vlastních čipů od roku 2019. Nový čip se zaměřuje
  na zlepšený výkon při odvozování modelů a vyrábí se na pokročilém 3nm procesu TSMC.
importance: 4
layout: tech_news_article
original_title: Microsoft launches Maia 200 AI chip, mass production progress draws
  attention
publishedAt: '2026-01-27T02:07:44+00:00'
slug: microsoft-launches-maia-200-ai-chip-mass-productio
source:
  emoji: 📰
  id: null
  name: Digitimes
title: Microsoft představuje AI čip Maia 200, pokrok v hromadné výrobě přitahuje pozornost
url: https://www.digitimes.com/news/a20260127PD201/microsoft-ai-chip-production-accelerator.html
urlToImage: https://img.digitimes.com/newsshow/20260127pd201_files/2_b.jpg
urlToImageBackup: https://img.digitimes.com/newsshow/20260127pd201_files/2_b.jpg
---

### Souhrn
Microsoft představil Maia 200, druhou generaci svého AI akcelerátoru určeného pro datacentra Azure. Tento čip klade důraz na vyšší výkon při odvozování (inference) strojových modelů a vstupuje do fáze hromadné výroby na 3nm technologii od TSMC. Představení signalizuje Microsoftovo dlouhodobé úsilí o nezávislost na dodavatelích jako Nvidia.

### Klíčové body
- Druhá generace akcelerátoru Maia, vyvíjeného od roku 2019 pro Azure cloud.
- Optimalizace pro inference, což je klíčové pro nasazení velkých jazykových modelů v produkci.
- Výroba na 3nm procesu TSMC, který umožňuje vyšší hustotu tranzistorů a lepší energetickou účinnost.
- Pokrok v hromadné výrobě, což urychluje nasazení v datech Microsoftu.
- Souvislost s širším trendem custom AI čipů u hyperscalerů.

### Podrobnosti
Microsoft zahájil vývoj vlastních AI čipů v roce 2019 s cílem optimalizovat výpočty v cloudu Azure, kde běží modely jako ty od OpenAI. První generace Maia 100 byla nasazena interně pro trénink a odvozování modelů, ale trpěla nižší flexibilitou oproti Nvidia H100. Maia 200 tento problém řeší zlepšením výkonu inference o desítky procent – podle dostupných informací dosahuje vyšší propustnosti při zpracování tokenů v reálném čase, což je nezbytné pro aplikace jako chatboti nebo doporučovací systémy.

Čip je vyráběn na 3nm nodu TSMC, což znamená přibližně 30 miliard tranzistorů na kus a spotřebu kolem 700 W při plném zatížení, s lepší energií na operaci než předchozí generace. Tento proces umožňuje balení více die do jednoho balení (chiplet design), což zvyšuje škálovatelnost v rackových systémech. Microsoft plánuje Maia 200 integrovat do nových superpočítačů pro Azure AI, kde nahradí část Nvidia GPU a sníží náklady na výpočty o 20–40 % díky custom architektuře optimalizované pro sparse modely jako Phi nebo Llama.

V porovnání s konkurencí: Google TPU v6, Amazon Trainium2 nebo Meta MTIA mají podobné cíle, ale Maia 200 vyniká podporou hybridních workloads – kombinuje trénink malých modelů s masivním inference. Hromadná výroba, která teď přitahuje pozornost investorů, znamená, že první systémy budou nasazeny v polovině roku 2026, s kapacitou stovek tisíc čipů ročně. To posiluje Microsoftovu pozici v AI ekosystému, kde Azure zpracovává miliardy požadavků denně.

### Proč je to důležité
Představení Maia 200 urychluje divergenci v AI hardware, kde hyperscaleři jako Microsoft budují vlastní čipy, aby snížili závislost na Nvidia, jejíž GPU čekají fronty měsíců. Pro průmysl to znamená levnější inference – klíčové pro komercializaci AI, kde stojí odvozování GPT-4 tokenů centy. Uživatelé Azure získají rychlejší a levnější služby jako Copilot, což posílí konkurenci s Google Cloud a AWS. Dlouhodobě to může democratizovat AI, ale vyžaduje standardizaci software (např. ONNX runtime), aby vývojáři nebyli vázáni na jednu platformu. V kontextu závodu o AGI je custom hardware krok k efektivnějším modelům, i když Microsoft zatím zaostává za Nvidia v raw FLOPS.

---

[Číst původní článek](https://www.digitimes.com/news/a20260127PD201/microsoft-ai-chip-production-accelerator.html)

**Zdroj:** 📰 Digitimes
