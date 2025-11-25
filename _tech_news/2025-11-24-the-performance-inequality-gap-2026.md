---
author: Marisa Aigen
category: výkonnost webu
date: '2025-11-24 00:00:00'
description: Nová analýza ukazuje, že i přes lepší sítě a zařízení stále roste objem
  webových stránek, což negativně ovlivňuje uživatelskou zkušenost – zejména u méně
  výkonných zařízení a pomalejších sítí.
importance: 3
layout: tech_news_article
original_title: The Performance Inequality Gap, 2026
publishedAt: '2025-11-24T00:00:00+00:00'
slug: the-performance-inequality-gap-2026
source:
  emoji: 📰
  id: null
  name: Infrequently.org
title: Mezera ve výkonnosti webu, 2026
url: https://infrequently.org/2025/11/performance-inequality-gap-2026/
urlToImage: https://infrequently.org/2025/11/performance-inequality-gap-2026/single-core-scores.png
urlToImageBackup: https://infrequently.org/2025/11/performance-inequality-gap-2026/single-core-scores.png
---

## Souhrn
V roce 2026 jsou sítě i mobilní zařízení výrazně výkonnější než dříve, přesto průměrné webové stránky stále narůstají do extrémních velikostí. Nová doporučení pro testování výkonu webu počítají s reálnými podmínkami 75. percentilu uživatelů, avšak většina webů tyto limity překračuje, což vede k pomalému načítání a horší dostupnosti.

## Klíčové body
- Doporučené testovací parametry pro 2026: 9 Mbps download, 3 Mbps upload, 100 ms RTT.
- Referenční zařízení: Samsung Galaxy A24 4G a HP 14.
- Webové stránky by měly mít maximálně 2 MB pro načtení do 3 sekund (JS-light) nebo 1,2 MB (JS-heavy).
- Využití více než dvou TLS spojení výrazně snižuje dostupný rozpočet na data.
- Medián mobilní stránky je nyní větší než hra DOOM a 75. percentil přesahuje dvojnásobek této velikosti.

## Podrobnosti
Analýza vychází z dat CrUX (Chrome User Experience Report) a definuje realistické limity pro výkon webu v roce 2026. Cílem je emulovat zkušenost uživatele na 75. percentilu – tedy čtvrtina uživatelů má horší připojení nebo zařízení. Pro splnění cíle načtení stránky do tří sekund by měla být celková velikost stránky v případě „JS-light“ (15 % JavaScriptu) maximálně 2 MB, z toho 300 KB JavaScript. U „JS-heavy“ stránek (50 % JavaScriptu) je limit 1,2 MB celkem. Při použití čtyř TLS spojení místo dvou se tyto limity snižují o cca 350 KiB, což podtrhuje výhody HTTP/2 nebo HTTP/3, které umožňují multiplexing a snižují režii spojení.

Přestože technologie umožňují rychlé doručení obsahu, průměrné weby neustále narůstají. V dubnu 2026 překročil medián mobilní stránky velikost 2,3 MB – více než originální hra DOOM (cca 2,3 MB). Stránky na 75. percentilu jsou větší než dvě kopie DOOM a na 90. percentilu dokonce přesahují 10 MB. Pro srovnání: počítač použitý při misi Apollo měl celkovou paměť 72 KB – dnešní průměrná stránka je tedy přibližně 70× větší.

## Proč je to důležité
Růst velikosti stránek není jen technickým problémem, ale i etickou otázkou. Pomalé načítání a nadměrná spotřeba dat znevýhodňují uživatele v rozvojových zemích, seniory nebo lidi s omezeným příjmem. Navzdory dostupným nástrojům a znalostem stále chybí disciplína vývojářů a tlak ze strany firem na optimalizaci. Tento trend ohrožuje univerzální přístup k informacím a podkopává základní principy webové dostupnosti.

---

[Číst původní článek](https://infrequently.org/2025/11/performance-inequality-gap-2026/)

**Zdroj:** 📰 Infrequently.org
