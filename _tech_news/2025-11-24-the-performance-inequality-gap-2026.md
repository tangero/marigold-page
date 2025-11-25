---
author: Marisa Aigen
category: výkonnost webu
date: '2025-11-24 00:00:00'
description: Nová analýza ukazuje, že i přes rychlejší sítě a zařízení stále více
  webů selhává v dodržení základních výkonnostních limitů, což negativně ovlivňuje
  uživatele s nižším výkonem zařízení.
importance: 3
layout: tech_news_article
original_title: The Performance Inequality Gap, 2026
publishedAt: '2025-11-24T00:00:00+00:00'
slug: the-performance-inequality-gap-2026
source:
  emoji: 📰
  id: null
  name: Infrequently.org
title: Propast ve výkonnosti webu v roce 2026
url: https://infrequently.org/2025/11/performance-inequality-gap-2026/
urlToImage: https://infrequently.org/2025/11/performance-inequality-gap-2026/single-core-scores.png
urlToImageBackup: https://infrequently.org/2025/11/performance-inequality-gap-2026/single-core-scores.png
---

## Souhrn
I když se v roce 2026 výrazně zlepšily parametry mobilních sítí a dostupných zařízení, většina webových stránek stále překračuje rozumné limity pro rychlé načítání. Analýza založená na datech CrUX (Chrome User Experience Report) ukazuje, že velikost stránek neustále roste, až k extrémním hodnotám – medián mobilní stránky je nyní větší než celá hra DOOM.

## Klíčové body
- Doporučená testovací konfigurace pro rok 2026: 9 Mbps download, 3 Mbps upload, 100 ms RTT a zařízení jako Samsung Galaxy A24 4G nebo HP 14.
- Výkonnostní rozpočty pro 3- a 5-sekundové načtení zahrnují limity pro celkovou velikost stránky a podíl JavaScriptu.
- Použití více než dvou TLS spojení výrazně snižuje dostupný rozpočet na data.
- Medián mobilní stránky dosáhl velikosti přesahující 2 MB, což je 70× více než celková paměť palubního počítače Apollo 11.
- Růst velikosti stránek je považován nejen za technický, ale i etický problém.

## Podrobnosti
Pro rok 2026 byly aktualizovány referenční parametry pro testování výkonnosti webu. Cílem je napodobit zkušenost uživatele na 75. percentilu – tedy čtvrtina uživatelů má horší zařízení nebo síť. Pro třísekundové načtení stránky by měla být celková velikost maximálně 2,0 MB u „lehkých“ stránek (15 % JavaScript) nebo 1,2 MB u „těžkých“ (50 % JavaScript). U pětisekundového cíle jsou limity 3,7 MB a 2,3 MB. Tyto limity předpokládají pouze dvě TLS spojení; při čtyřech klesají o více než 350 KiB.

Přestože jsou tyto rozpočty považovány za velmi štědré, většina webů je překračuje. V dubnu 2026 překročila mediánová mobilní stránka velikost 2,3 MB – více než dvojnásobek hry DOOM (původní verze z roku 1993 měla cca 2,4 MB). Stránky na 90. percentilu jsou dokonce 4,5× větší než medián. Tento trend trvá více než deset let a má zásadní dopady na přístupnost, spotřebu dat i baterie, zejména pro uživatele v rozvojových zemích nebo s levnějšími zařízeními.

## Proč je to důležité
Nadměrná velikost webů nejen zpomaluje načítání, ale také zvyšuje nároky na síťovou infrastrukturu, spotřebu energie a finanční náklady uživatelů. V kontextu globální digitální nerovnosti se jedná o etický problém: technologie, která by měla sloužit všem, se stává méně přístupnou pro ty, kteří na ní závisí nejvíce. Vývojáři by měli prioritně optimalizovat kritickou cestu načítání, minimalizovat JavaScript a využívat moderní protokoly jako HTTP/2 nebo HTTP/3 pro konsolidaci spojení.

---

[Číst původní článek](https://infrequently.org/2025/11/performance-inequality-gap-2026/)

**Zdroj:** 📰 Infrequently.org
