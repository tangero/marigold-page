---
slug: "down-link"
url: "/mobilnisite/slovnik/down-link/"
type: "slovnik"
title: "Down-link – Down-link"
date: 2025-01-01
abbr: "Down-link"
fullName: "Down-link"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/down-link/"
summary: "Signálová cesta v mobilní síti, kde základnová stanice (např. NodeB, eNB, gNB) vysílá signály k uživatelskému zařízení (UE). Je to základní směr komunikace, přenášející uživatelská data, řídicí inform"
---

Down-link je signálová cesta v mobilní síti, kde základnová stanice vysílá signály k uživatelskému zařízení (UE), přenášející uživatelská data a řídicí informace ze sítě do mobilního zařízení.

## Popis

Down-link, často psáno jako downlink ([DL](/mobilnisite/slovnik/dl/)), je klíčový koncept v rádiových přístupových sítích (RAN), který definuje směr přenosu od síťové infrastruktury k uživatelskému zařízení (UE). V systémech 3GPP to zahrnuje všechny rádiové signály vysílané základnovou stanicí – ať už jde o NodeB v UMTS, [eNB](/mobilnisite/slovnik/enb/) v LTE nebo gNB v NR – směrem k mobilnímu zařízení. Tato cesta přenáší více typů informací, včetně dat uživatelské roviny (např. internetové pakety nebo hlasové pakety), signalizace řídicí roviny (jako pagingové zprávy nebo bloky systémových informací) a referenčních signálů pro synchronizaci a odhad kanálu. Down-link funguje v rámci specifických kmitočtových pásem a časových zdrojů přidělených plánovací funkcí v základnové stanici, která dynamicky přiděluje zdroje na základě faktorů jako poptávka UE, podmínky kanálu a požadavky na kvalitu služby (QoS).

Z architektonického hlediska je down-link implementován ve fyzické vrstvě a vyšších vrstvách rádiového protokolového zásobníku. Na fyzické vrstvě zahrnuje modulační schémata (např. QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM), kódovací techniky (jako turbo kódy nebo [LDPC](/mobilnisite/slovnik/ldpc/) kódy v NR) a technologie více antén ([MIMO](/mobilnisite/slovnik/mimo/)) pro zvýšení přenosových rychlostí a spolehlivosti. Klíčové fyzické kanály v down-linku zahrnují Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) pro uživatelská data, Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) pro řídicí informace a synchronizační signály (PSS/SSS) pro vyhledávání buňky. Plánovač základnové stanice, klíčová součást v MAC vrstvě, určuje, která UE obdrží data v každém přenosovém časovém intervalu (TTI), optimalizuje tím kapacitu sítě a spravedlivost.

Jak down-link funguje, zahrnuje kontinuální proces plánování, kódování, modulace a vysílání rádiových rámců. Základnová stanice přijímá data od jádra sítě přes backhaulové spoje, zpracuje je přes protokolový zásobník – přidává hlavičky, segmentuje na přepravní bloky a aplikuje kanálové kódování – a poté je namapuje na fyzické zdroje. Techniky beamformingu a předkódování mohou být použity k nasměrování energie k určitým UE, čímž se zlepšuje kvalita signálu. UE na přijímací straně provádí inverzní operace: demodulaci, dekódování a opětovné sestavení. Výkon down-linku je kritický pro celkový síťový zážitek, ovlivňuje metriky jako propustnost, latence a pokrytí, a je úzce koordinován s uplinkem (opačný směr) pro efektivní duplexní komunikaci, ať už v režimech FDD nebo TDD.

## K čemu slouží

Down-link existuje jako základní součást bezdrátových komunikačních systémů, aby síť mohla doručovat informace mobilním uživatelům. Řeší základní problém jednosměrného toku dat od poskytovatelů služeb k účastníkům, podporuje nezbytné služby jako hlasové hovory, zasílání zpráv, přístup k internetu a multimediální streamování. Historicky, jak se mobilní sítě vyvíjely z 1G analogových systémů na 2G digitální, potřeba strukturovaného, efektivního down-linku se stala prvořadou pro zvládání rostoucích datových požadavků a podporu nových aplikací, což motivovalo jeho standardizaci v 3GPP od R99 dále.

Před standardizovanými definicemi down-linku měly rané celulární systémy proprietární implementace, které omezovaly interoperabilitu a škálovatelnost. Specifikace 3GPP pro down-link, jako jsou ty, které detailně popisují fyzické kanály a procedury, řeší tato omezení zajištěním konzistentního chování napříč výrobci a operátory. Tato standardizace umožňuje globální roaming, úspory z rozsahu ve výrobě zařízení a vývoj pokročilých funkcí jako agregace nosných nebo massive MIMO, které spoléhají na přesnou downlinkovou signalizaci.

Vytvoření konceptu down-linku bylo hnací silou duplexní povahy komunikace, kde jsou potřeba oddělené cesty pro provoz ze sítě do zařízení a ze zařízení do sítě. Umožňuje efektivní využití spektra pomocí technik jako frekvenční duplex (FDD) nebo časový duplex (TDD), optimalizuje přidělování zdrojů. Vývoj down-linku odráží pokračující snahy o zvýšení přenosových rychlostí, snížení latence a zlepšení spolehlivosti, čímž reaguje na požadavky uživatelů na rychlejší a citlivější mobilní zážitky v čím dál více propojeném světě.

## Klíčové vlastnosti

- Směr přenosu od základnové stanice k uživatelskému zařízení
- Přenáší uživatelská data, řídicí signalizaci a vysílací informace
- Využívá fyzické kanály jako PDSCH, PDCCH a synchronizační signály
- Podporuje pokročilé technologie jako MIMO a beamforming pro zvýšený výkon
- Dynamické plánování zdrojů MAC vrstvou základnové stanice
- Funguje v duplexních režimech FDD i TDD pro flexibilní využití spektra

## Související pojmy

- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing

---

📖 **Anglický originál a plná specifikace:** [Down-link na 3GPP Explorer](https://3gpp-explorer.com/glossary/down-link/)
