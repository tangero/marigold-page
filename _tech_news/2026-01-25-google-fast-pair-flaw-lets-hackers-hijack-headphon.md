---
author: Marisa Aigen
category: kyberbezpečnost
companies:
- Google
date: '2026-01-25 12:02:55'
description: Výzkumníci z KU Leuven odhalili zranitelnosti v protokolu Google Fast
  Pair pod názvem WhisperPair, které umožňují tiché převzetí Bluetooth zařízení jako
  sluchátka nebo reproduktory. Google na to reaguje vydáním záplat pro výrobce a aktualizací
  certifikačních požadavků.
importance: 5
layout: tech_news_article
original_title: Google Fast Pair flaw lets hackers hijack headphones
publishedAt: '2026-01-25T12:02:55+00:00'
slug: google-fast-pair-flaw-lets-hackers-hijack-headphon
source:
  emoji: 📰
  id: fox-news
  name: Fox News
title: Chyba v protokolu Google Fast Pair umožňuje hackerům převzít sluchátka
url: https://www.foxnews.com/tech/google-fast-pair-flaw-lets-hackers-hijack-headphones
urlToImage: https://static.foxnews.com/foxnews.com/content/uploads/2026/01/google-fast-pair-hacking.jpg
urlToImageBackup: https://static.foxnews.com/foxnews.com/content/uploads/2026/01/google-fast-pair-hacking.jpg
---

## Souhrn
Výzkumníci z univerzity KU Leuven v Belgii objevili závažné bezpečnostní chyby v protokolu Google Fast Pair, který usnadňuje rychlé párování Bluetooth zařízení. Tyto zranitelnosti, nazvané WhisperPair, umožňují útočníkům v dosahu Bluetooth tiše připojit k sluchátkům, sluchátkům do uší nebo reproduktorům bez vědomí vlastníka. Google na problém reaguje poskytnutím záplat výrobcům a zpřísněním certifikačních standardů.

## Klíčové body
- Protokol Fast Pair vysílá identitu zařízení do okolí, což urychluje párování, ale mnohá zařízení ignorují pravidlo o autorizaci nových připojení při existujícím spojení.
- Útok WhisperPair probíhá v 10–15 sekundách pomocí běžného telefonu, notebooku nebo levného zařízení jako Raspberry Pi, bez potřeby specializovaného hardware.
- Útočník může přerušovat hovory, vkládat audio, aktivovat mikrofony a v některých případech sledovat polohu uživatele.
- Zranitelnost postihuje nejen Android zařízení, ale i iPhony a zařízení bez Google produktů.
- Google vydává záplaty a aktualizuje certifikaci pro nová zařízení.

## Podrobnosti
Protokol Fast Pair, který Google vyvinul pro Android zařízení, slouží k zjednodušení párování Bluetooth zařízení. Místo manuálního zadávání kódů nebo procházení nastavení stačí jedno poklepání na obrazovku – zařízení vysílá svou identitu do okolí, telefon ji rozpozná a naváže spojení. Tato zkratka však přináší rizika, jak ukázali výzkumníci z KU Leuven.

Jejich analýza odhalila, že mnohá Bluetooth zařízení – především sluchátka, sluchátka do uší a reproduktory – přijímají nové párování i při aktivním spojení s jiným zařízením, což porušuje základní bezpečnostní pravidla protokolu. Útočník v dosahu Bluetooth (typicky 10 metrů) tak může za 10 až 15 sekund navázat spojení bez jakýchkoli viditelných známek na zařízení vlastníka. Po připojení získá útočník plnou kontrolu: může přerušovat telefonní hovory, vkládat vlastní audio (například hlasové zprávy nebo rušivé zvuky), aktivovat mikrofony pro odposlech nebo v některých případech využít sledovací funkce zařízení k lokalizaci uživatele.

Co je klíčové, útok nevyžaduje pokročilý hardware. Stačí standardní smartphone s Bluetooth, notebook nebo levný počítač jako Raspberry Pi s příslušným softwarem. Zranitelnost není omezena na Android: postihuje i iOS zařízení a jakékoli Bluetooth reproduktory kompatibilní s Fast Pair, bez ohledu na to, zda uživatel vlastní Google produkty. Výzkumníci testovali desítky modelů od různých výrobců a zjistili, že chyba je rozšířená napříč značkami. KU Leuven je univerzita známá výzkumem v kyberbezpečnosti, její tým se specializuje na analýzu IoT a bezdrátových protokolů.

Google na objev reagoval rychle: poskytl výrobcům záplaty pro software zařízení a aktualizoval certifikační požadavky pro nové produkty kompatibilní s Fast Pair. Tyto změny zajistí, aby zařízení vyžadovala explicitní autorizaci při nových párováních a blokovala neoprávněné připojení. Výrobci musí záplaty implementovat, což může trvat měsíce u starších modelů.

## Proč je to důležité
Tato zranitelnost odhaluje systémové slabiny v Bluetooth ekosystému, který je základem miliard zařízení. Fast Pair je standardizován a široce používaný, takže WhisperPair ohrožuje miliony uživatelů – od běžných spotřebitelů po profesionály v call centrech. Dopady zahrnují nejen ztrátu soukromí (odposlech, sledování), ale i bezpečnostní rizika, jako je sabotáž hovorů v citlivých prostředích. V širším kontextu to podtrhuje nutnost přísnějších bezpečnostních standardů pro IoT a Bluetooth protokoly, kde pohodlí často převažuje nad ochranou. Průmysl musí investovat do robustnějších autentizačních mechanismů, jako je vícefaktorová verifikace při párování. Pro uživatele to znamená okamžitou kontrolu aktualizací zařízení a vypnutí Bluetooth mimo použití, dokud nejsou záplaty aplikovány. Objev z KU Leuven představuje zero-day exploit, který může inspirovat další útoky, pokud se výrobci oneskorí.

---

[Číst původní článek](https://www.foxnews.com/tech/google-fast-pair-flaw-lets-hackers-hijack-headphones)

**Zdroj:** 📰 Fox News
