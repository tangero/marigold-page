---
author: Marisa Aigen
category: ai hardware
companies:
- NVIDIA
- Groq
date: '2025-12-25 17:41:54'
description: Nvidia a Groq oznámily 24. prosince 2025 dohodu za 20 miliard dolarů,
  která zahrnuje neexkluzivní licenci na inference technologii Groq a přechod klíčových
  zaměstnanců do Nvidia. Groq zůstává nezávislou společností a její platforma GroqCloud
  bude fungovat dál.
importance: 5
layout: tech_news_article
original_title: Nvidia Does $20 Billion Deal With Groq
publishedAt: '2025-12-25T17:41:54+00:00'
slug: nvidia-does-20-billion-deal-with-groq
source:
  emoji: 📰
  id: next-big-future
  name: Next Big Future
title: Nvidia uzavírá dohodu v hodnotě 20 miliard dolarů s Groq
url: https://www.nextbigfuture.com/2025/12/nvidia-does-20-billion-deal-with-groq.html
urlToImage: https://nextbigfuture.s3.amazonaws.com/uploads/2025/12/Screenshot-2025-12-25-at-9.40.58-AM.jpg
urlToImageBackup: https://nextbigfuture.s3.amazonaws.com/uploads/2025/12/Screenshot-2025-12-25-at-9.40.58-AM.jpg
---

## Souhrn
Nvidia uzavřela s firmou Groq dohodu v hodnotě 20 miliard dolarů, oznámenou 24. prosince 2025. Jedná se o neexkluzivní licenční smlouvu na technologii inference Groq, doplněnou o přechod klíčových zaměstnanců do Nvidia. Groq si zachovává nezávislost pod novým vedením.

## Klíčové body
- Neexkluzivní licence na Language Processing Unit (LPU) Groq, optimalizovanou pro inference velkých jazykových modelů (LLM).
- Přechod zakladatele a bývalého CEO Jonathana Rossa (dříve hlavní projektant Google TPU), prezidenta Sunnyho Madru a dalších seniorních členů týmu do Nvidia.
- Groq pokračuje jako samostatná firma pod novým CEO Simonem Edwardsem s nepretržitým provozem platformy GroqCloud.
- Struktura dohody připomíná acqui-hire kombinovaný s licencí, nikoli plné převzetí společnosti.
- LPU vyniká SRAM architekturou pro rychlý přístup k váhám modelu, což snižuje latenci oproti standardním GPU.

## Podrobnosti
Dohoda mezi Nvidii a Groq představuje strategický krok v soutěži o dominance v hardware pro umělou inteligenci, konkrétně v oblasti inference, tedy fáze, kdy AI modely generují odpovědi na základě trénovacích dat. Groq, startup založený v roce 2016, se specializuje na vývoj specializovaných čipů pro rychlou inferenci LLM, jako jsou modely typu GPT nebo Llama. Jejich klíčový produkt, Language Processing Unit (LPU), je aplikační specifický integrovaný obvod (ASIC), navržený od základu pro sekvenční zpracování dat v transformerních modelech. Na rozdíl od univerzálních grafických procesorů (GPU) od Nvidia, které původně sloužily k grafice a paralelním výpočtům, LPU řeší specifické požadavky inference: deterministickou nízkou latenci, vysoký výkon v tokenech za sekundu, energetickou úspornost a zpracování sekvenčních závislostí.

Hlavní inovací LPU je SRAM-centrická architektura, kde se stovky megabajtů statické paměti SRAM používají jako primární úložiště vah modelu, nikoli jen jako mezipaměť. V GPU musí váhy neustále přecházet mezi pomalou vysokofrekvenční pamětí HBM a výpočetními jádry, což způsobuje úzká hrdla v přenosu dat. LPU zajišťuje okamžitý přístup k vahám, což umožňuje plnou rychlost výpočtů a dramaticky snižuje latenci. Data se pohybují v modelu producent-spotřebitel s "pásovým dopravníkem" mezi SIMD funkčními jednotkami, kde je plánování statické a deterministické. To znamená předvídatelné chování bez dynamického řízení paměti, což je klíčové pro real-time aplikace jako chatboti nebo hlasoví asistenti.

Jonathan Ross, zakladatel Groq a bývalý hlavní projektant Google Tensor Processing Unit (TPU), přinese do Nvidia zkušenosti s optimalizací hardware pro AI. TPU slouží k akceleraci tréninku a inference neuronových sítí v Google cloudu. Přechod Rossa, Madru a dalších posílí tým Nvidia, který bude integrovat LPU technologii do svých řešení, jako jsou platformy pro AI inference v datových centrech. GroqCloud, cloudová platforma pro inference LLM, zůstane dostupná pro zákazníky bez přerušení a bude konkurovat službám jako AWS Inferentia nebo Google Cloud TPU.

Tato struktura dohody umožňuje Nvidii získat konkurenční výhodu bez plného převzetí Groq, které by mohlo vyvolat regulační problémy. Groq si udržuje svou nezávislost a může dále licencovat technologii třetím stranám díky neexkluzivnímu charakteru smlouvy.

## Proč je to důležité
Tato dohoda za 20 miliard dolarů posiluje pozici Nvidia v inference, kde roste poptávka po efektivním hardware kvůli explozivnímu růstu LLM. Inference tvoří většinu provozu AI služeb, jako ChatGPT, a spotřebovává méně energie než trénink, ale vyžaduje specializaci. Integrace LPU umožní Nvidii konkurovat AMD (s MI300X) a Intelu (Gaudi3) v energetické efektivitě a latenci, což ovlivní ceny cloudových AI služeb. Pro průmysl znamená akceleraci nasazení velkých modelů v reálném čase, například v autonomních vozidlech nebo robotice. Groq jako nezávislý hráč udrží konkurenci, ale Nvidia získá klíčovou technologii, což může urychlit vývoj směrem k efektivnějšímu AI ekosystému. V širším kontextu to podtrhuje trend konsolidace v AI hardware, kde giganti absorbují inovace startupů pro udržení dominance.

---

[Číst původní článek](https://www.nextbigfuture.com/2025/12/nvidia-does-20-billion-deal-with-groq.html)

**Zdroj:** 📰 Next Big Future
