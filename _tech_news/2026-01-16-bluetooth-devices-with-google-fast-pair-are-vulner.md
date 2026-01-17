---
author: Marisa Aigen
category: kybernetika
companies:
- Google
date: '2026-01-16 19:39:31'
description: Výzkumníci z belgické univerzity KU Leuven odhalili zranitelnosti v technologii
  Google Fast Pair, která slouží k rychlému párování Bluetooth zařízení na systémech
  Android a ChromeOS. Nový útok nazvaný WhisperPair umožňuje hackerům převzít kontrolu
  nad sluchátky, reproduktory a mikrofony zařízení od výrobců jako Sony, Anker nebo
  Nothing, včetně sledování polohy uživatele.
importance: 5
layout: tech_news_article
original_title: Bluetooth devices with Google Fast Pair are vulnerable to new hack
publishedAt: '2026-01-16T19:39:31+00:00'
slug: bluetooth-devices-with-google-fast-pair-are-vulner
source:
  emoji: 📰
  id: null
  name: MobileSyrup
title: Bluetooth zařízení s technologií Google Fast Pair jsou zranitelná vůči novému
  útoku
url: https://mobilesyrup.com/2026/01/16/google-fast-pair-devices-hack/
urlToImage: https://production-static.mobilesyrup.com/uploads/2024/10/Google-pixel-buds-header-4-scaled.jpg
urlToImageBackup: https://production-static.mobilesyrup.com/uploads/2024/10/Google-pixel-buds-header-4-scaled.jpg
---

## Souhrn
Výzkumníci z Katolické univerzity v Louvainu (KU Leuven) v Belgii identifikovali závažné zranitelnosti v technologii Google Fast Pair, která umožňuje jednoduše připojit Bluetooth zařízení k zařízením s Androidem nebo ChromeOS jedním dotykem. Nově objevený útok s názvem WhisperPair umožňuje hackerům neoprávně se připojit k sluchátkům, reproduktorům nebo mikrofonům na vzdálenost až 14 metrů, převzít kontrolu nad nimi, přehrávat vlastní zvuk, poslouchat přes mikrofon oběti nebo sledovat její polohu. Tato zranitelnost postihuje i majitele iPhonů, kteří Fast Pair aktivně nepoužívají.

## Klíčové body
- Technologie Fast Pair je zranitelná vůči útoku WhisperPair, který umožňuje rychlé neoprávněné připojení bez souhlasu uživatele.
- Dosah útoku dosahuje až 14 metrů, což umožňuje ovládání na veřejných místech.
- Hackeři mohou zastavit přenos zvuku, přehrát vlastní audio, aktivovat mikrofon pro odposlech nebo využít sledování polohy.
- Postižená zařízení zahrnují produkty od Sony, Anker (výrobce nabíjecích příslušenství a audio zařízení) a Nothing (startup zaměřený na bezdrátová sluchátka).
- Seznam všech zranitelných zařízení je dostupný na webu výzkumného projektu.

## Podrobnosti
Google Fast Pair je služba integrovaná do operačních systémů Android a ChromeOS, která zjednodušuje párování Bluetooth zařízení. Funguje tak, že zařízení jako sluchátka nebo reproduktory vysílají speciální Bluetooth signály obsahující identifikátory, které Android rozpozná a zobrazí uživateli možnost připojení jedním stiskem. Tento proces je navržen pro pohodlí, ale výzkumníci z KU Leuven zjistili, že signály lze snadno zfalšovat pomocí levného Bluetooth vysílače. Útok WhisperPair tedy nevyžaduje fyzický přístup k oběti – hacker stačí být v dosahu 14 metrů a vyslat upravené signály, které oklamou protokol párování.

Jakmile je hacker připojen, získává plnou kontrolu. Může přerušit stávající audio stream, spustit přehrávání vlastního zvuku (například hlasového vyzvánění nebo dezinformací), aktivovat mikrofon pro skryté odposlešování nebo využít vestavěné senzory pro sledování polohy uživatele. Zajímavé je, že tato zranitelnost není omezena jen na Android: i majitelé iPhonů jsou ohrozeni, protože útok zneužívá standardní Bluetooth protokoly, které jsou cross-platformní. Celý proces trvá sekundy a nevyžaduje žádné další oprávnění.

Výzkumníci testovali desítky zařízení a potvrdili zranitelnost modelů od Sony (např. WF-1000XM série sluchátek), Anker (Soundcore reproduktory) a Nothing (Ear série). Google zatím na objev nereagoval oficiálně, ale výzkumníci doporučují dočasně deaktivovat Fast Pair v nastavení Bluetooth a čekat na aktualizace firmwaru od výrobců. Plný technický popis a seznam zařízení je k dispozici na webu projektu WhisperPair. Zdroj: Wired, přes Ars Technica.

## Proč je to důležité
Tato zranitelnost odhaluje dlouhodobé slabiny v Bluetooth ekosystému, kde pohodlí často převažuje nad bezpečností. Fast Pair používají miliony uživatelů denně pro připojování sluchátek a reproduktorů, což zvyšuje riziko masového ohrožení soukromí – od krádeže konverzací přes mikrofony až po fyzické sledování. V širším kontextu posiluje to trendy v kyberbezpečnosti, kde výzkumy jako tento (podobně jako minulé BlueBorne nebo KNOB útoky) nutí výrobce přehodnotit Bluetooth stacky. Pro uživatele to znamená okamžité riziko na veřejných místech, jako jsou letiště nebo kanceláře, a zdůrazňuje potřebu rychlých patchů od Google i výrobců. Bez aktualizací zůstávají zařízení exponovaná, což může vést k reálným incidentům špionáže nebo obtěžování.

---

[Číst původní článek](https://mobilesyrup.com/2026/01/16/google-fast-pair-devices-hack/)

**Zdroj:** 📰 MobileSyrup
