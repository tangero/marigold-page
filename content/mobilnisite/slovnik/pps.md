---
slug: "pps"
url: "/mobilnisite/slovnik/pps/"
type: "slovnik"
title: "PPS – Protocol and Parameter Select"
date: 2025-01-01
abbr: "PPS"
fullName: "Protocol and Parameter Select"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pps/"
summary: "PPS je odpovědní zpráva v inicializační sekvenci karty UICC/USIM, odesílaná jako odpověď na příkaz Answer To Reset (ATR). Umožňuje terminálu vyjednat a zvolit komunikační protokol a parametry pro rozh"
---

PPS je odpovědní zpráva v inicializační sekvenci karty UICC/USIM, která vyjednává a vybírá komunikační protokol a parametry čipové karty po příkazu Answer To Reset.

## Popis

Protocol and [Parameter](/mobilnisite/slovnik/parameter/) Select (PPS) je klíčový postup definovaný v normě [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816-3 pro karty s integrovaným obvodem ([ICC](/mobilnisite/slovnik/icc/)), který je převzat a specifikován organizací 3GPP pro operace s kartami UICC (Universal Integrated Circuit Card) a [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module). Výměna PPS proběhne bezprostředně po sekvenci Answer To Reset ([ATR](/mobilnisite/slovnik/atr/)), což je úvodní elektrické a protokolové handshake při zapnutí čipové karty. ATR informuje terminál (např. mobilní telefon) o základních schopnostech karty, jako jsou podporované přenosové protokoly (T=0 nebo T=1) a základní elektrické parametry. PPS je odpovědí terminálu, ve které může navrhnout konkrétní protokol a upravit parametry, jako je převodní faktor hodinového kmitočtu (F) a úpravný faktor přenosové rychlosti (D), aby optimalizoval rychlost přenosu dat a spotřebu energie pro konkrétní pár karta-terminál.

Procedura PPS je vyjednávacím mechanismem. Terminál analyzuje data z ATR, která zahrnují podporované protokoly karty (Typ protokolu T) a její maximální podporované přenosové rychlosti (definované parametry jako F a D). Na základě vlastních schopností a požadovaného výkonu terminál sestaví PPS požadavek. Tento požadavek obsahuje vybraný protokol (T=0 pro bajtově orientovaný přenos nebo T=1 pro blokově orientovaný přenos) a navrhované hodnoty pro F a D. Karta poté odpoví potvrzením PPS, pokud návrh přijme, nebo může zůstat nečinná či odeslat chybu; v takovém případě se použijí výchozí parametry z ATR. Tento handshake zajišťuje, že obě entity před výměnou jakýchkoli příkazů na aplikační úrovni (jako jsou příkazy pro síťovou autentizaci) pracují na vzájemně dohodnuté, optimální sadě komunikačních pravidel.

Z architektonického hlediska PPS funguje na fyzické a linkové vrstvě rozhraní čipové karty. Klíčovými zapojenými komponentami jsou ovladač rozhraní ICC v terminálu a správce I/O v kartě. Vyjednané parametry přímo ovlivňují elektrické signalizační vlastnosti a rámcování datových paketů. Například výběr T=1 umožňuje detekci a opravu chyb na úrovni bloků, což je pro některé operace robustnější. Role PPS v síti 3GPP je základní, ale často transparentní; je základem pro spolehlivou a efektivní komunikaci mezi mobilním zařízením a USIM, což je nezbytné pro všechny následné bezpečnostní procedury (jako je autentizace a dohoda o klíči) a přístup ke službám. Bez úspěšné výměny PPS (i když jde o implicitní přijetí výchozích hodnot) nemohou vyšší vrstvy protokolů fungovat správně.

## K čemu slouží

Procedura PPS existuje proto, aby řešila problém interoperability mezi širokou škálou čipových karet (UICC) a mobilních terminálů od různých výrobců. V počátcích čipových karet mohla karta podporovat pouze jeden pevný komunikační režim. S vývojem technologie karty získaly podporu pro více protokolů a vyšší přenosové rychlosti. Samotný [ATR](/mobilnisite/slovnik/atr/) byl nedostatečný, protože pouze uváděl schopnosti karty; neumožňoval terminálu aktivně zvolit nebo optimalizovat spojení. PPS byl zaveden, aby poskytl dynamickou vyjednávací fázi.

Toto vyjednávání řeší několik omezení. Za prvé umožňuje optimalizaci výkonu. Terminál schopný vyšších hodinových rychlostí může navrhnout vyšší datovou rychlost (úpravou F a D), pokud ji karta podporuje, což vede k rychlejší výměně dat pro přístup k souborům nebo aplikačním protokolovým datovým jednotkám ([APDU](/mobilnisite/slovnik/apdu/)). Za druhé zvyšuje spolehlivost tím, že umožňuje terminálu vybrat robustnější protokol T=1, pokud jej obě strany podporují, který obsahuje mechanismy řízení chyb, jež se v T=0 nevyskytují. Nakonec poskytuje cestu pro budoucí vývoj. Jak jsou v pozdějších verzích normy ISO definovány nové parametry nebo protokoly, lze rámec PPS rozšířit o jejich vyjednávání, čímž je zajištěna zpětná kompatibilita. Historický kontext je ukotven ve standardizaci čipových karet pro telekomunikace (GSM, poté 3GPP), kde se SIM/USIM stalo zabezpečeným programovatelným prvkem vyžadujícím efektivní a spolehlivou komunikaci s mobilním zařízením.

## Klíčové vlastnosti

- Dynamické vyjednávání protokolu (T=0 nebo T=1)
- Úprava parametrů pro datovou rychlost (faktory F a D)
- Řídí se normou ISO/IEC 7816-3 přejatou organizací 3GPP
- Zahajuje ji terminál po přijetí ATR
- Zajišťuje optimální a kompatibilní komunikaci s čipovou kartou
- Základ pro všechny následné aplikační příkazy USIM

## Související pojmy

- [ATR – Answer To Reset](/mobilnisite/slovnik/atr/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [PPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pps/)
