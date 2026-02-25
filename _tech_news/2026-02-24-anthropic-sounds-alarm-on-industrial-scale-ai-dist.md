---
author: Marisa Aigen
category: bezpečnost ai
companies:
- Anthropic
- DeepSeek
- Moonshot AI
- MiniMax
date: '2026-02-24 00:00:00'
description: Anthropic obviňuje DeepSeek, Moonshot AI a MiniMax z průmyslově velkých
  útoků na destilaci AI, které měly ukrást schopnosti modelu Claude. Rostou obavy
  z krádeže duševního vlastnictví a národní bezpečnosti.
importance: 5
layout: tech_news_article
original_title: Anthropic Sounds Alarm on “Industrial-Scale” AI Distillation Attacks
  Threatening Model Security
publishedAt: '2026-02-24T00:00:00+00:00'
slug: anthropic-sounds-alarm-on-industrial-scale-ai-dist
source:
  emoji: 📰
  id: null
  name: C-sharpcorner.com
title: Anthropic varuje před „průmyslově velkými“ útoky na destilaci AI ohrožujícími
  bezpečnost modelů
url: https://www.c-sharpcorner.com/news/anthropic-sounds-alarm-on-industrialscale-ai-distillation-attacks-threatening-model-security
urlToImage: https://www.c-sharpcorner.com/images/csharp-corner-new.png
urlToImageBackup: https://www.c-sharpcorner.com/images/csharp-corner-new.png
---

## Souhrn
Společnost Anthropic, tvůrce jazykového modelu Claude, zveřejnila bezpečnostní zprávu o průmyslově velkých útocích na destilaci, které usnadnily konkurentům extrakci znalostí z jejich systému. Obviňuje z toho čínské firmy DeepSeek, Moonshot AI a MiniMax, které prý použily přes 24 000 falešných účtů k vygenerování 16 milionů interakcí. Tyto akce porušily podmínky služby a regionální omezení, protože Claude není v Číně komerčně dostupný.

## Klíčové body
- Anthropic identifikoval koordinovaný útok ze strany DeepSeek (vývojář open-source modelů jako DeepSeek-V2), Moonshot AI (chatbot Kimi) a MiniMax (model Hailuo).
- Útočníci použili proxy sítě k maskování a zaměřili se na schopnosti Claude v uvažování, kódování a používání nástrojů.
- Celkem přes 24 000 falešných účtů vygenerovalo více než 16 milionů dotazů.
- Porušení podmínek služby Anthropic a zákaz komerčního přístupu v Číně.
- Dopady zahrnují krádež duševního vlastnictví a rizika pro národní bezpečnost.

## Podrobnosti
Destilace v kontextu strojového učení znamená trénink menšího „studentského“ modelu na výstupech většího „učitelského“ modelu, což umožňuje snížit výpočetní nároky při zachování výkonu. Anthropic však toto označuje za nelegitimní útok, kdy konkurenti masivně dotazují proprietární systém bez souhlasu, aby získali data pro vlastní trénink. Tímto způsobem mohou obejít roky výzkumu a miliardy dolarů investovaných do vývoje Claude, který se vyznačuje pokročilým uvažováním, generováním kódu a integrací nástrojů jako prohlížeče nebo databáze.

Podle zprávy Anthropic útočníci koordinovaně nasadili proxy sítě k obcházení detekce a regionálních blokád. Claude je v Číně blokován kvůli licenčním omezením a exportním regulacím, což činí tyto akce nejen porušením smluvních podmínek, ale i potenciálně mezinárodních předpisů. DeepSeek je čínská firma specializující se na open-source velké jazykové modely, jako DeepSeek-V2 s 236 miliardami parametrů, který konkuruje GPT-4 v kódování. Moonshot AI vyvíjí chatbot Kimi s dlouhou kontextovou pamětí až 128 tisíc tokenů, zaměřený na složité úlohy. MiniMax vytváří multimodální model Hailuo pro text, obrázky a video.

Anthropic detekoval tyto aktivity analýzou vzorců chování, jako opakované dotazy na specifické úlohy, a implementoval obranná opatření včetně lepší detekce proxy a omezení rychlosti dotazů. Tento případ odhaluje slabiny v ochraně proprietárních AI modelů, kde výstupy slouží jako cenná tréninková data.

## Proč je to důležité
Tento incident nastavuje precedent pro budoucí konflikty v AI průmyslu, kde uzavřené modely jako Claude čelí riziku kopírování schopností. Pro vývojáře znamená nutnost investovat do pokročilých detekčních systémů, vodoznaků ve výstupech nebo legálních modelů knowledge distillation. V širším kontextu ohrožuje národní bezpečnost, protože extrakce schopností z pokročilých modelů může urychlit vývoj vojenských AI v nepřátelských státech. Pro uživatele to znamená potenciální zhoršení kvality služeb kvůli omezením přístupu a pro průmysl zesílení napětí mezi západními a čínskými firmami, což může vést k fragmentaci AI ekosystému a zpomalení globálního pokroku.

---

[Číst původní článek](https://www.c-sharpcorner.com/news/anthropic-sounds-alarm-on-industrialscale-ai-distillation-attacks-threatening-model-security)

**Zdroj:** 📰 C-sharpcorner.com
