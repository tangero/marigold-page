---
slug: "sl-bch"
url: "/mobilnisite/slovnik/sl-bch/"
type: "slovnik"
title: "SL-BCH – Sidelink Broadcast Channel"
date: 2025-01-01
abbr: "SL-BCH"
fullName: "Sidelink Broadcast Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-bch/"
summary: "Fyzický kanál v komunikaci postranním spojem (sidelink) pro vysílání informací přímo mezi blízkými zařízeními bez síťové infrastruktury. Umožňuje kritické služby, jako jsou varování pro veřejnou bezpe"
---

SL-BCH je fyzický kanál postranního spoje (sidelink) pro vysílání informací přímo mezi blízkými zařízeními, který umožňuje kritické služby, jako jsou varování pro veřejnou bezpečnost a zprávy V2X, bez potřeby síťové infrastruktury.

## Popis

Sidelink Broadcast Channel (SL-BCH) je vyhrazená struktura typu fyzického sdíleného kanálu pro downlink, používaná pro vysílací přenosy ve scénářích komunikace zařízení-zařízení ([D2D](/mobilnisite/slovnik/d2d/)) definovaných 3GPP. Fungující v rámci rozhraní postranního spoje (sidelink), SL-BCH přenáší zásadní systémové informace a řídicí data, která musí být rozšířena k více přijímajícím uživatelským zařízením (UE) v blízkosti, nezávisle na pokrytí mobilní sítí. Kanál je navržen s robustními modulačními a kódovacími schématy, aby zajistil spolehlivý příjem v náročných rádiových prostředích typických pro aplikace veřejné bezpečnosti a vozidlové komunikace.

Architektonicky existuje SL-BCH ve fyzické vrstvě (vrstva 1) zásobníku protokolů sidelink, mapovaný z transportních kanálů prostřednictvím specifického zpracování fyzické vrstvy definovaného v specifikacích jako 36.212 a 38.212. Kanál využívá vyhrazené časově-frekvenční zdroje v rámci fondu zdrojů sidelink, nakonfigurované buď sítí, nebo předkonfigurací. Mezi klíčové komponenty patří transportní blok SL-BCH, který nese vysílané informace, a přidružené referenční signály pro demodulaci ([DM-RS](/mobilnisite/slovnik/dm-rs/)), které umožňují odhad kanálu na přijímači. Kanál používá kvadraturní fázovou modulaci ([QPSK](/mobilnisite/slovnik/qpsk/)) s turbokódováním pro korekci chyb vpřed, čímž vyvažuje spektrální účinnost a spolehlivost příjmu.

Během provozu vysílající UE generuje přenosy SL-BCH obsahující kritické informace, jako jsou synchronizační signály sidelink, bloky systémových informací pro sidelink (SL-SIBs) nebo zprávy pro veřejnou bezpečnost. Kanál podporuje scénáře jak v pokrytí, tak mimo pokrytí sítě prostřednictvím síťově konfigurovaných nebo předkonfigurovaných alokací zdrojů. Pro sidelink založený na LTE (specifikovaný od Rel-12) funguje SL-BCH v přenosu založeném na podrámcích se specifickými vzory mapování zdrojových prvků. V NR sidelink (od Rel-16) využívá slotové struktury s podporou flexibilnější číselné soustavy. Vysílací povaha kanálu odstraňuje potřebu individuálních povolení k plánování pro každé přijímající UE, což jej činí efektivním pro skupinovou komunikaci, kde musí stejné informace dosáhnout více zařízení současně.

SL-BCH hraje zásadní roli v komunikačních systémech sidelink tím, že poskytuje základní vysílací mechanismus, který umožňuje objevování zařízení, systémovou synchronizaci a šíření nouzových upozornění. V sítích pro veřejnou bezpečnost umožňuje záchranářům sdílet kritické informace o situačním povědomí i v případě, že je buněčná infrastruktura poškozena nebo nedostupná. Pro vozidlovou komunikaci ([V2X](/mobilnisite/slovnik/v2x/)) SL-BCH usnadňuje periodické vysílání základních bezpečnostních zpráv obsahujících informace o poloze, rychlosti a trajektorii vozidla, které umožňují systémy pro předcházení kolizím. Návrh kanálu upřednostňuje spolehlivost před spektrální účinností, přičemž parametry přenosu jsou optimalizovány pro očekávané rozptyly Dopplerova jevu, rozptyly zpoždění a podmínky rušení typické pro scénáře přímé komunikace zařízení-zařízení.

## K čemu slouží

SL-BCH byl vytvořen, aby řešil kritickou potřebu spolehlivé vysílací komunikace mezi blízkými zařízeními v rámci architektur Device-to-Device ([D2D](/mobilnisite/slovnik/d2d/)) a sidelink od 3GPP. Před jeho zavedením v Rel-12 chyběly v mobilních sítích standardizované mechanismy pro přímou vysílací komunikaci zařízení-zařízení, což omezovalo aplikace v oblasti veřejné bezpečnosti, vozidlových sítí a služeb založených na blízkosti. Tradiční buněčné vysílací kanály, jako je [PBCH](/mobilnisite/slovnik/pbch/), byly navrženy pro komunikaci infrastruktura-zařízení a nemohly podporovat dynamickou, decentralizovanou povahu scénářů D2D, kde zařízení komunikují přímo, aniž by vždy využívala síťovou infrastrukturu.

Hlavní motivace pro SL-BCH vzešla z požadavků veřejné bezpečnosti identifikovaných po katastrofách, jako jsou zemětřesení a teroristické útoky, kdy je buněčná infrastruktura často poškozena nebo přetížena. Záchranáři potřebovali spolehlivé možnosti přímé komunikace, které by mohly fungovat nezávisle na síťové infrastruktuře. Navíc snahy automobilového průmyslu o komunikaci Vozidlo-se-vším ([V2X](/mobilnisite/slovnik/v2x/)) vyžadovaly efektivní vysílací mechanismy pro bezpečnostní zprávy mezi vozidly. SL-BCH tyto problémy vyřešil poskytnutím standardizovaného kanálu fyzické vrstvy optimalizovaného pro jedinečné výzvy vozidlového prostředí, kde vozidla potřebují vysílat bezpečnostní zprávy blízkým vozidlům s minimálním zpožděním.

SL-BCH řeší tyto problémy poskytnutím standardizovaného vysílacího kanálu fyzické vrstvy specificky optimalizovaného pro podmínky sidelink. Odstraňuje omezení dřívějších přístupů podporou jak síťově plánovaných, tak autonomních režimů výběru zdrojů, čímž vyhovuje různým úrovním zapojení sítě. Návrh kanálu bere v úvahu jedinečné výzvy šíření v D2D, včetně problémů blízko-daleko, scénářů s vysokou mobilitou a absence centralizované regulace výkonu, která existuje v buněčných downlink přenosech. Zavedením této základní vysílací schopnosti 3GPP umožnilo širokou škálu služeb založených na blízkosti, které tvoří základ pro pokročilé sidelink aplikace v následujících vydáních.

## Klíčové vlastnosti

- Schopnost vysílacího přenosu pro komunikaci postranním spojem (sidelink) bez síťové infrastruktury
- Podpora režimů provozu jak v pokrytí, tak mimo pokrytí sítě
- Robustní modulační a kódovací schémata (QPSK s turbokódováním) pro spolehlivý příjem
- Vyhrazené časově-frekvenční zdroje v rámci fondů zdrojů sidelink
- Přenáší zásadní systémové informace včetně synchronizačních signálů a SL-SIBs
- Podporuje implementace sidelink založené na LTE i na NR s odpovídajícími strukturami fyzické vrstvy

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [SL-BCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-bch/)
