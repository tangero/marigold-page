---
slug: "srtp-mki"
url: "/mobilnisite/slovnik/srtp-mki/"
type: "slovnik"
title: "SRTP-MKI – Secure Real-time Transport Protocol Master Key Identifier"
date: 2025-01-01
abbr: "SRTP-MKI"
fullName: "Secure Real-time Transport Protocol Master Key Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/srtp-mki/"
summary: "Identifikátor hlavního klíče SRTP je jedinečný štítek používaný k asociaci šifrovaných mediálních paketů SRTP s konkrétním hlavním klíčem SRTP. Umožňuje efektivní správu a obměnu klíčů během relace, t"
---

SRTP-MKI je jedinečný štítek používaný k asociaci šifrovaných mediálních paketů SRTP s konkrétním hlavním klíčem SRTP, což umožňuje efektivní správu klíčů a jejich obměnu tím, že přijímačům umožňuje vybrat správný klíč pro dešifrování.

## Popis

SRTP-MKI (Secure Real-time Transport Protocol Master Key Identifier) je pole proměnné délky ve formátu paketu [SRTP](/mobilnisite/slovnik/srtp/), které slouží jako ukazatel na konkrétní hlavní klíč SRTP ([SRTP-MK](/mobilnisite/slovnik/srtp-mk/)) a hlavní sůl ([SRTP-MS](/mobilnisite/slovnik/srtp-ms/)) použitou k vygenerování relakových klíčů pro daný paket. Je to volitelná, ale klíčová součást pro správu klíčů v dlouhotrvajících nebo dynamických mediálních relacích. Pokud je přítomen, je [MKI](/mobilnisite/slovnik/mki/) připojen na konec paketu SRTP nebo [SRTCP](/mobilnisite/slovnik/srtcp/). Hodnota MKI je dohodnuta komunikujícími koncovými body během signalizace navázání relace, typicky v rámci výměny [SDP](/mobilnisite/slovnik/sdp/) nabídky/odpovědi. Identifikuje konkrétní kontext klíče mezi potenciálně několika aktivními nebo uloženými.

Provozně SRTP-MKI funguje ve spojení s procesem odvozování klíčů. Každému odlišnému hlavnímu klíči SRTP (a přidružené hlavní soli SRTP-MS) je přiřazena jedinečná hodnota MKI. Když odesílatel šifruje paket, zahrne MKI odpovídající hlavnímu klíči použitému pro odvození klíčů tohoto paketu. Příjemce, který udržuje vyhledávací tabulku mapující hodnoty MKI na skutečné SRTP-MK a SRTP-MS, přečte MKI z příchozího paketu. Poté načte správný hlavní klíč a sůl, znovu odvodí potřebné relakové klíče (šifrovací klíč, autentizační klíč) a pokračuje v dešifrování a ověření paketu. Tento mechanismus je zásadní pro scénáře jako je obnova klíčů, kdy je nový SRTP-MK zřízen uprostřed relace; pakety zašifrované starým klíčem a novým klíčem mohou na lince koexistovat, odlišené svým MKI.

V architektuře 3GPP je použití a formát SRTP-MKI řízeno profily a síťovými politikami. Pro IMS mediální služby může [P-CSCF](/mobilnisite/slovnik/p-cscf/) nebo jiné funkce pro správu politik vyžadovat jeho použití, aby usnadnily síťově řízené aktualizace klíčů, jako jsou ty vyvolané změnami bezpečnostní politiky nebo handovery. Samotné MKI nenesou žádný kryptografický tajný údaj; jeho účel je čistě identifikační. Jeho přenos v nešifrované podobě tedy neoslabuje zabezpečení. Délka pole MKI je vyjednávána, což umožňuje rovnováhu mezi režií (protože přidává bajty ke každému paketu) a rozsahem potřebných identifikátorů klíčů. Jeho implementace je klíčovým prvkem pro robustní a spravovatelné zabezpečení médií, které se může v čase přizpůsobovat bez přerušení toku médií v reálném čase.

## K čemu slouží

SRTP-MKI bylo zavedeno, aby vyřešilo provozní problém správy životního cyklu kryptografických klíčů v probíhající mediální relaci v reálném čase. Bez identifikátoru musí být všechny pakety v relaci šifrovány klíči odvozenými z jediného statického hlavního klíče. Pro změnu klíče by bylo nutné relaci znovu vyjednat, což by způsobilo přerušení – což je pro hlasový nebo video hovor nepřijatelný výsledek. [MKI](/mobilnisite/slovnik/mki/) poskytuje elegantní mechanismus v pásmu pro rotaci klíčů a identifikaci kontextu.

Historicky, když bylo SRTP převzato ze standardů IETF do 3GPP pro služby na úrovni operátora, stala se zřejmou potřeba škálovatelné správy klíčů. Sítě vyžadují schopnost pravidelně aktualizovat klíče z důvodu dopředného utajení nebo v reakci na bezpečnostní události. MKI řeší omezení jediného aktivního kontextu klíče tím, že umožňuje, aby více kontextů klíčů bylo platných současně. Jeho vytvoření bylo motivováno požadavkem na nepřerušenou službu během handoverů mezi přístupovými sítěmi nebo po vypršení životnosti klíče podle síťové politiky. Pouhým označením paketů identifikátorem se vyhne složité koordinaci přesných hranic paketů pro přepnutí klíče. Příjemce může asynchronně spravovat více sad klíčů, což výrazně zjednodušuje synchronizaci stavu mezi odesílatelem a příjemcem a zvyšuje spolehlivost a zabezpečení mediální roviny.

## Klíčové vlastnosti

- Jedinečný identifikátor pro aktivní pár SRTP-MK a SRTP-MS
- Přenášen v pásmu v závěrečné části paketu SRTP/SRTCP
- Umožňuje více aktivních kryptografických kontextů v rámci jedné relace RTP
- Podporuje plynulou obnovu a přechod klíčů bez přerušení služby
- Délka je vyjednatelná během navazování relace pro optimalizaci režie
- Nezbytné pro síťově řízenou správu klíčů a scénáře handoveru v 3GPP

## Související pojmy

- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)
- [SRTP-MK – Secure Real-time Transport Protocol Master Key](/mobilnisite/slovnik/srtp-mk/)
- [SRTP-MS – Secure Real-time Transport Protocol Master Salt](/mobilnisite/slovnik/srtp-ms/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems

---

📖 **Anglický originál a plná specifikace:** [SRTP-MKI na 3GPP Explorer](https://3gpp-explorer.com/glossary/srtp-mki/)
