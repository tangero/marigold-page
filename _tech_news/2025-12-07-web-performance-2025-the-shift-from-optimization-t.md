---
author: Marisa Aigen
category: webová výkonnost
date: '2025-12-07 07:26:00'
description: Vývoj webové výkonnosti v roce 2025 přináší díky Speculation Rules API
  v prohlížečích na bázi Chromium přechod od tradiční optimalizace k prediktivnímu
  načítání stránek. Tento přístup umožňuje zkrátit čas načítání následných stránek
  na pod 300 ms, což nutí přehodnotit stávající měřítka výkonu.
importance: 3
layout: tech_news_article
original_title: 'Web Performance 2025: The Shift from Optimization to Prediction'
publishedAt: '2025-12-07T07:26:00+00:00'
slug: web-performance-2025-the-shift-from-optimization-t
source:
  emoji: 📰
  id: null
  name: Perfplanet.com
title: 'Webová výkonnost 2025: Posun od optimalizace k predikci'
url: https://calendar.perfplanet.com/2025/web-performance-2025-the-shift-from-optimization-to-prediction/
urlToImage: https://calendar.perfplanet.com/images/2025/fabian/i1.png
urlToImageBackup: https://calendar.perfplanet.com/images/2025/fabian/i1.png
---

## Souhrn
V roce 2025 došlo v prohlížečích na bázi Chromium k významnému pokroku díky dozrávání Speculation Rules API a agresivnímu přednačítání stránek. Tento vývoj umožňuje blížit se k okamžitému načítání následných stránek, i když první stránka webu zůstává mimo dosah. Na základě dat z reálného uživatelského měření (RUM) z stovek e-commerce stránek se podíl načítání pod 300 ms výrazně zvýšil.

## Klíčové body
- Dozrání Speculation Rules API umožňuje prediktivní přednačítání stránek v Chromium prohlížečích.
- Výrazné zlepšení výkonu u následných navigací, s časy pod 300 ms pro významný podíl načítání.
- Nové kategorie pro Largest Contentful Paint (LCP): Instant (<300 ms), Fast (<1000 ms), OK (<2500 ms).
- Kritika stávajících prahů výkonu jako zastaralých vzhledem k psychologickým a obchodním faktorům.
- Omezení: Nelze přednačíst první stránku webu (landing page).

## Podrobnosti
Autor článku, Fabian Krumbholz, webový konzultant pro výkon u společnosti Speed Kit a uznávaný Google Developer Expert, popisuje dlouhodobý cíl dosáhnout okamžitého načítání webových stránek. Po desetiletí úsilí o optimalizaci kritických cest vykreslování a snižování času do prvního bajtu (Time to First Byte) bránily fyzické limity sítě plnému úspěchu. Situace se v roce 2025 změnila díky Speculation Rules API, což je standardní rozhraní prohlížeče umožňující definovat pravidla pro spekulativní načítání a vykreslování stránek na základě predikcí uživatelského chování. Tato API slouží k předvýpočtu potenciálně navštívených stránek v pozadí, což dramaticky zkracuje viditelnou latenci při navigaci.

Krumbholz uvádí data z RUM měření stovek e-commerce webů, kde prediktivní přednačítání posunulo značnou část načítání do kategorie pod 300 ms. To vedlo k přepracování hodnocení Largest Contentful Paint (LCP), metriky měřící čas zobrazení největšího viditelného obsahu. Původní hranice „dobrého“ výkonu 2,5 sekundy, stanovená před pěti lety jako motivační cíl, je nyní neadekvátní v éře výkonnějších zařízení a infrastruktury. Nové vrstvy – Instant (<300 ms), Fast (<1000 ms) a OK (<2500 ms) – lépe odrážejí realitu. Psychologicky je reakce pod 100 ms vnímána jako okamžitá, což podporuje lepší uživatelskou zkušenost. Obchodně to znamená vyšší konverze v e-commerce, kde každý milisekundový rozdíl ovlivňuje příjmy.

Omezením zůstává neschopnost přednačíst první stránku webu, což omezuje dopad na celý uživatelský cyklus. Tento pokrok je zatím omezen na Chromium-based prohlížeče jako Chrome nebo Edge, což vytváří fragmentaci oproti Firefoxu nebo Safari. Speed Kit, firma zaměřená na zrychlení webových zkušeností, tyto technologie integruje do svých řešení pro firmy.

## Proč je to důležité
Tento posun ovlivňuje webový průmysl tím, že zvyšuje tlak na aktualizaci nástrojů měření výkonu, jako jsou Core Web Vitals od Google. Pro uživatele znamená rychlejší navigaci na složitých webech, zejména e-commerce, kde pomalost vede k opuštění košíku. V širším kontextu urychluje adopci moderních API a nutí vývojáře přejít od reaktivní optimalizace k prediktivním technikám, což může zefektivnit vývoj, ale zároveň zvyšuje závislost na proprietárních prohlížečích. Dlouhodobě to může vést k přehodnocení standardů Web Vitals a lepší konkurenceschopnosti otevřeného webu oproti nativním aplikacím.

---

[Číst původní článek](https://calendar.perfplanet.com/2025/web-performance-2025-the-shift-from-optimization-to-prediction/)

**Zdroj:** 📰 Perfplanet.com
