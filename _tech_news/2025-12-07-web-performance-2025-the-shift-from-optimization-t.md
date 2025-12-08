---
author: Marisa Aigen
category: výkon webu
date: '2025-12-07 07:26:00'
description: Článek popisuje přechod v optimalizaci webového výkonu od tradičních
  metod k prediktivnímu načítání stránek díky Speculation Rules API v prohlížečích
  na bázi Chromium. Díky agresivnímu přednačítání se podařilo výrazně zkrátit dobu
  načítání následných stránek na e-commerce webech.
importance: 3
layout: tech_news_article
original_title: 'Web Performance 2025: The Shift from Optimization to Prediction'
publishedAt: '2025-12-07T07:26:00+00:00'
slug: web-performance-2025-the-shift-from-optimization-t
source:
  emoji: 📰
  id: null
  name: Perfplanet.com
title: 'Webový výkon 2025: Posun od optimalizace k predikci'
url: https://calendar.perfplanet.com/2025/web-performance-2025-the-shift-from-optimization-to-prediction/
urlToImage: https://calendar.perfplanet.com/images/2025/fabian/i1.png
urlToImageBackup: https://calendar.perfplanet.com/images/2025/fabian/i1.png
---

## Souhrn
V roce 2025 přineslo dozrání Speculation Rules API v prohlížečích na bázi Chromium zásadní změnu v oblasti webového výkonu. Tato technologie umožňuje agresivní přednačítání a předvykreslování stránek, čímž se blíží k okamžitému načítání následných navigací. Data z reálného uživatelského měření (RUM) na stovkách e-commerce webů ukazují posun velkého objemu načítání do kategorie pod 300 ms.

## Klíčové body
- Dozrání Speculation Rules API umožňuje prohlížečům predikovat a přednačítat následující stránky na základě pravidel definovaných vývojáři.
- Agresivní předvykreslování (prerendering) zkracuje dobu Largest Contentful Paint (LCP) na následných stránech pod 300 ms.
- Nové kategorie výkonu LCP: Instant (<300 ms), Rychlé (<1000 ms), Přijatelné (<2500 ms).
- Standardní hranice „dobrý“ výkon (2,5 s) je zastaralý kvůli pokročilým API, výkonnějším zařízením a infrastruktuře.
- Psychologický argument: reakce do 100 ms působí okamžitě; obchodní dopady na e-commerce.

## Podrobnosti
Článek Web Performance Calendar 2025 od Fabiana Krumbhoze, konzultanta pro webový výkon ve společnosti Speed Kit a Google Developer Experta, analyzuje dlouhodobý cíl tvorby webových stránek s okamžitým načítáním. Po desetiletí optimalizace kritických cest vykreslování a snižování zpoždění Time to First Byte (TTFB) bránily fyzikální limity sítě dosažení skutečné rychlosti. V roce 2025 se situace změnila v prohlížečích Chromium (jako Chrome, Edge), kde Speculation Rules API dozrálo do fáze, kdy umožňuje efektivní predikci uživatelských akcí.

Tato API slouží k definování pravidel pro spekulativní načítání zdrojů nebo předvykreslování stránek na základě pravděpodobných navigací, například odkazů v menu nebo doporučených produktů na e-commerce. Agresivní prerendering vytváří kompletní verzi stránky v pozadí, kterou prohlížeč aktivuje ihned po kliknutí, což eliminuje většinu síťového zpoždění. Limity zůstávají: první stránka webu (landing page) se nedá přednačíst, protože není známa předem, a podpora je zatím omezena na Chromium – Firefox a Safari zaostávají.

Data RUM z stovek e-commerce webů ukazují, že prediktivní přednačítání posouvá významný podíl načítání do kategorie Instant (<300 ms). Krumbholz navrhuje rozdělit stávající „dobrou“ hranici LCP (2,5 s) na tři úrovně: Instant (<300 ms), Rychlé (<1000 ms) a Přijatelné (<2500 s). Tato změna odráží realitu moderních zařízení s lepší infrastrukturou a novými API. Psychologicky je klíčové zpoždění pod 100 ms, aby uživatel cítil okamžitou odezvu; nad 1 s dochází k frustraci. Obchodně to znamená vyšší konverze na e-commerce, kde každých 100 ms zkrácení zvyšuje prodeje o 1 %.

## Proč je to důležité
Tento posun ovlivňuje široký webový průmysl, zejména e-commerce a obsahové weby, kde navigace mezi stránkami tvoří většinu interakcí. Pro vývojáře znamená nutnost implementovat Speculation Rules API pro konkurenční výhodu, ale vyžaduje to pečlivé testování, aby se zabránilo zbytečnému plýtvání zdroji na nepravděpodobné predikce. V širším kontextu urychluje to konvergenci webu k nativním aplikacím, snižuje odliv uživatelů a tlačí na aktualizaci standardů Web Vitals od Google. Nicméně závislost na Chromium zdůrazňuje rizika monopolizace prohlížečového trhu a potřebu širší podpory. Pro uživatele to přináší rychlejší prohlížení, ale jen v podporovaných prohlížečích.

---

[Číst původní článek](https://calendar.perfplanet.com/2025/web-performance-2025-the-shift-from-optimization-to-prediction/)

**Zdroj:** 📰 Perfplanet.com
