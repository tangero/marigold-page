---
author: Marisa Aigen
category: umělá inteligence
date: '2025-12-01 00:00:00'
description: Vědci představili model Cryo-EM Image Evaluation Foundation (Cryo-IEF),
  předtrénovaný na 65 milionech částicových obrazů nekontrolovaným způsobem. Tento
  model vyniká v úkolech zpracování dat kryogenní elektronové mikroskopie, automatizuje
  složitý workflow a činí technologii přístupnější.
importance: 3
layout: tech_news_article
original_title: Artificial intelligence foundation model automates cryo-EM structure
  determination
publishedAt: '2025-12-01T00:00:00+00:00'
slug: artificial-intelligence-foundation-model-automates
source:
  emoji: 📰
  id: null
  name: Nature.com
title: Základní model umělé inteligence automatizuje určení struktur v cryo-EM
url: https://www.nature.com/articles/s41592-025-02917-7
urlToImage: https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41592-025-02917-7/MediaObjects/41592_2025_2917_Fig1_HTML.png
urlToImageBackup: https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41592-025-02917-7/MediaObjects/41592_2025_2917_Fig1_HTML.png
---

## Souhrn
Výzkumníci vyvinuli model Cryo-IEF, základní model umělé inteligence určený pro zpracování dat z kryogenní elektronové mikroskopie (cryo-EM). Model byl předtrénován na 65 milionech obrazů částic v nekontrolovaném učení, což mu umožňuje automatizovat složité kroky určení 3D struktur biomolekul. Tím se cryo-EM stává robustnější a dostupnější pro laboratoře bez specializovaného know-how.

## Klíčové body
- Předtrénování na 65 milionech particle images z cryo-EM dat v unsupervised módu.
- Automatizace celého workflow od hodnocení obrazů po rekonstrukci struktur.
- Inspirace self-supervised vision transformers a metodami jako CryoDRGN-AI.
- Publikováno v Nature Methods s odkazy na EMPIAR databázi.
- Otevřený přístup k modelu pro široké využití v strukturální biologii.

## Podrobnosti
Kryogenní elektronová mikroskopie (cryo-EM) je klíčovou technikou v strukturální biologii, která umožňuje rekonstruovat trojrozměrné struktury proteinů a komplexů bez nutnosti krystalizace. Proces zahrnuje sběr tisíců obrazů zamrazených vzorků, identifikaci částic (particle picking), jejich klasifikaci, 2D/3D rekonstrukci a rafinaci. Tyto kroky jsou časově náročné a vyžadují expertizu, což omezuje šíření metody.

Model Cryo-IEF řeší tyto problémy pomocí foundation model přístupu, podobného velkým jazykovým modelům, ale zaměřeného na obrazy. Předtrénování proběhlo na masivním datasetu 65 milionů particle images z veřejné databáze EMPIAR, která shromažďuje cryo-EM a cryo-ET data. Použití unsupervised učení, inspirovaného pracemi jako self-supervised vision transformers od Chen et al. (2021), umožnilo modelu naučit se reprezentace bez označených dat. Výsledek je univerzální enkóder, který exceluje v úkolech jako hodnocení kvality obrazů, particle picking, klasifikace heterogenity a ab initio rekonstrukce.

Například v porovnání s předchozími metodami jako CryoDRGN-AI (Levy et al., 2025) Cryo-IEF zlepšuje zpracování náročných datasetů s vysokou heterogenitou. Model lze doladit (fine-tune) pro specifické úkoly, což snižuje potřebu manuálních zásahů. Autoři demonstrují aplikace na reálných datech, včetně těch z Nogalesovy recenze (2016) o vývoji cryo-EM do mainstream techniky. Přístup k plnému textu vyžaduje předplatné Nature Portfolio nebo jednorázový nákup za 39,95 USD, což odráží akademický charakter publikace.

## Proč je to důležité
Tento vývoj posiluje integraci AI do experimentální biologie, kde cryo-EM revolucionizovala objevování léků – například struktury spike proteinu SARS-CoV-2. Automatizace workflow urychlí výzkum o desítky procent, sníží chyby a umožní menším týmům konkurovat velkým laboratořím. V širším kontextu ukazuje, jak foundation models migruje z obecného AI do specializovaných domén, podobně jako v medicínském zobrazování. Nicméně závislost na kvalitních datech z EMPIAR znamená, že úspěch závisí na dostupnosti tréninkových sad; bez dalšího škálování může být omezen na standardní případy. Pro průmysl, jako farmaceutické firmy, to znamená rychlejší screening molekul, ale vyžaduje validaci na proprietárních datech.

---

[Číst původní článek](https://www.nature.com/articles/s41592-025-02917-7)

**Zdroj:** 📰 Nature.com
