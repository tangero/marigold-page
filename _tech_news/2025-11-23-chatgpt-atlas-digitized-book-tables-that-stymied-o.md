---
author: Marisa Aigen
category: ocr technologie
companies:
- OpenAI
date: '2025-11-23 22:42:44'
description: Při snaze digitalizovat tréninkové tabulky z knihy pro běžeckou aplikaci
  se autor setkal s neúspěchem u běžných nástrojů OCR. Nástroj ChatGPT Atlas autonomně
  zpracoval pět fotografií stránek s prohnutým papírem a hustými sloupci a vytvořil
  z nich bezchybná CSV data.
importance: 3
layout: tech_news_article
original_title: ChatGPT Atlas Digitized Book Tables That Stymied Other OCR Tools
publishedAt: '2025-11-23T22:42:44+00:00'
slug: chatgpt-atlas-digitized-book-tables-that-stymied-o
source:
  emoji: 📰
  id: null
  name: TidBITS
title: ChatGPT Atlas úspěšně digitalizoval tabulky z knihy, které odolaly jiným nástrojům
  OCR
url: https://tidbits.com/2025/11/23/chatgpt-atlas-digitized-book-tables-that-stymied-other-ocr-tools/
urlToImage: https://tidbits.com/uploads/2025/11/Jack-Daniels-tables-scaled.jpg
urlToImageBackup: https://tidbits.com/uploads/2025/11/Jack-Daniels-tables-scaled.jpg
---

## Souhrn
Při vývoji webové aplikace pro běžecký klub se autor setkal s problémem digitalizace komplexních tabulek z knihy *Daniels’ Running Formula*. Běžné nástroje pro optické rozpoznávání znaků (OCR) selhaly, zatímco experimentální nástroj ChatGPT Atlas dokázal z pěti fotografií stránek s prohnutým papírem a hustým uspořádáním sloupců vygenerovat přesná CSV data.

## Klíčové body
- Tréninkové tabulky z běžecké literatury jsou strukturovány v mnoha sloupcích a na více stránkách, což komplikuje OCR.
- Běžné OCR nástroje (např. Google Keep, Adobe Scan) nezvládly zachovat strukturu dat kvůli prohnutí stránek a hustému formátování.
- ChatGPT Atlas – experimentální nástroj založený na multimodálních schopnostech LLM – autonomně zpracoval fotografie a vygeneroval čistá strukturovaná data.
- Výsledná data umožňují výpočet tréninkových temp podle systému VDOT, který vyvinul trenér Jack Daniels.

## Podrobnosti
Autor, trenér běžeckého klubu Finger Lakes Runners Club, potřeboval digitalizovat dvě klíčové tabulky z knihy *Daniels’ Running Formula*: jednu pro určení VDOT (odhad aerobní kondice na základě výsledku závodu) a druhou pro převod VDOT na konkrétní tréninková tempa pro různé vzdálenosti a typy tréninku (Easy, Marathon, Threshold, Interval, Repetition). Tyto tabulky zabírají téměř čtyři stránky a jsou formátovány v hustých sloupcích, často s prohnutým papírem u vazby knihy – což je pro OCR extrémně náročná situace.

Po neúspěchu s tradičními nástroji OCR (včetně mobilních aplikací a cloudových služeb) vyzkoušel autor ChatGPT Atlas – experimentální rozhraní umožňující LLM zpracovávat obrázky a extrahovat z nich strukturovaná data. Nástroj nejen správně rozpoznal text, ale i zachoval relace mezi řádky a sloupci, a výstupem bylo čisté CSV, připravené k integraci do webové aplikace. Tato aplikace nyní umožňuje běžcům zadat čas závodu, získat VDOT a následně vypočítat tempa pro netypické tréninkové série (např. schodovité série 200–400–600 m).

## Proč je to důležité
Případ ukazuje, že moderní multimodální LLM (Large Language Models) začínají překonávat limity tradičních OCR systémů, zejména v situacích, kdy jde o složitě strukturovaná data. Zatímco klasické OCR nástroje se zaměřují na přesnost rozpoznání znaků, LLM jako ChatGPT Atlas dokáží „chápat“ kontext a logickou strukturu tabulek. To má potenciál zjednodušit digitalizaci starých technických manuálů, vědeckých publikací nebo historických dokumentů, kde je formátování nepravidelné. Nicméně je třeba mít na paměti, že se jedná o experimentální nástroj – jeho spolehlivost a škálovatelnost pro komerční nasazení zatím nejsou ověřeny.

---

[Číst původní článek](https://tidbits.com/2025/11/23/chatgpt-atlas-digitized-book-tables-that-stymied-other-ocr-tools/)

**Zdroj:** 📰 TidBITS
