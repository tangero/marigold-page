---
category: kybernetická bezpečn
date: '2025-10-22 22:35:41'
description: Vývojáři nejpoužívanějšího DNS softwaru BIND odhalili dvě kritické zranitelnosti
  umožňující otrávení cache a přesměrování uživatelů na falešné stránky. Připomínají
  slavný Kaminského útok z roku 2008.
importance: 4
layout: tech_news_article
original_title: BIND warns of bugs that could bring DNS cache attack back from the
  dead - Ars Technica
publishedAt: '2025-10-22T22:35:41+00:00'
slug: bind-warns-of-bugs-that-could-bring-dns-cache-atta
source:
  emoji: 🔬
  id: ars-technica
  name: Ars Technica
title: BIND varuje před chybami, které mohou oživit útoky na DNS cache
url: https://arstechnica.com/security/2025/10/bind-warns-of-bugs-that-could-bring-dns-cache-attack-back-from-the-dead/
urlToImage: https://cdn.arstechnica.net/wp-content/uploads/2025/06/browser-security-threat-1152x627.jpg
urlToImageBackup: https://cdn.arstechnica.net/wp-content/uploads/2025/06/browser-security-threat-1152x627.jpg
---

## Souhrn

Vývojáři BIND, nejrozšířenějšího softwaru pro překlad doménových jmen na internetu, varují před dvěma kritickými zranitelnostmi s hodnocením závažnosti 8,6 z 10. Chyby umožňují útočníkům otrávit celou cache DNS resolverů a přesměrovat uživatele na podvodné stránky, které jsou k nerozeznání od skutečných. Podobné zranitelnosti byly objeveny i v konkurenčním softwaru Unbound.

## Klíčové body

- Zranitelnosti CVE-2025-40778 a CVE-2025-40780 vznikly kvůli logické chybě a slabosti v generování pseudonáhodných čísel
- Útoky připomínají slavný Kaminského útok z roku 2008, který tehdy představoval jednu z nejzávažnějších bezpečnostních hrozeb internetu
- Útočníci mohou nahradit legitimní IP adresy (například 3.15.119.63 pro arstechnica.com) vlastními škodlivými adresami
- Záplaty pro všechny tři zranitelnosti byly vydány ve středu
- Software Unbound hlásí podobnou zranitelnost s nižším hodnocením závažnosti 5,6

## Podrobnosti

DNS (Domain Name System) funguje jako telefonní seznam internetu - překládá lidsky čitelné doménové názvy na IP adresy, které počítače používají ke komunikaci. BIND je dominantním softwarem pro tuto úlohu a používají ho tisíce organizací po celém světě.

Obě nově objevené zranitelnosti umožňují provést útok zvaný DNS cache poisoning (otrávení DNS cache). Při něm útočník dokáže podstrčit DNS resolveru falešné záznamy, které se uloží do cache a následně jsou poskytovány všem uživatelům dané organizace. Pokud by například útočník otrávil cache pro doménu banky, všichni zaměstnanci nebo zákazníci by byli přesměrováni na podvodnou stránku vypadající identicky jako ta skutečná.

První zranitelnost (CVE-2025-40778) vznikla kvůli logické chybě v kódu, zatímco druhá (CVE-2025-40780) je způsobena nedostatečně kvalitním generátorem pseudonáhodných čísel. Tento problém je obzvláště závažný, protože náhodná čísla jsou klíčová pro bezpečnostní mechanismy DNS.

Situace připomína rok 2008, kdy bezpečnostní výzkumník Dan Kaminsky odhalil podobnou zranitelnost, která představovala existenční hrozbu pro bezpečnost internetu. Tehdy bylo nutné koordinované úsilí tisíců poskytovatelů DNS služeb a výrobců prohlížečů, aby byla implementována ochrana. Problém tehdy spočíval v použití UDP paketů, které jsou jednosměrné a neumožňují DNS resolverům ověřit identitu autoritativních serverů pomocí hesel nebo jiných přihlašovacích údajů.

## Proč je to důležité

Objevení těchto zranitelností ukazuje, že DNS cache poisoning zůstává reálnou hrozbou i po sedmnácti letech od Kaminského objevu. Úspěšný útok by mohl mít devastující důsledky - útočníci by mohli přesměrovat miliony uživatelů na phishingové stránky bank, e-shopů nebo jiných služeb bez jakéhokoli viditelného varování. Organizace používající BIND nebo Unbound by měly okamžitě aplikovat dostupné záplaty. Vysoké hodnocení závažnosti 8,6 odráží potenciální dopad na bezpečnost celého internetu a nutnost rychlé reakce administrátorů po celém světě.

---

[Číst původní článek](https://arstechnica.com/security/2025/10/bind-warns-of-bugs-that-could-bring-dns-cache-attack-back-from-the-dead/)

**Zdroj:** 🔬 Ars Technica
