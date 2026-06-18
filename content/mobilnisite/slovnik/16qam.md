---
slug: "16qam"
url: "/mobilnisite/slovnik/16qam/"
type: "slovnik"
title: "16QAM – 16-Quadrature Amplitude Modulation"
date: 2025-01-01
abbr: "16QAM"
fullName: "16-Quadrature Amplitude Modulation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/16qam/"
summary: "16QAM je digitální modulační schéma, které kóduje 4 bity na symbol pomocí změny amplitudy i fáze nosné vlny. Poskytuje vyšší datové rychlosti než jednodušší modulace jako QPSK, což umožňuje efektivněj"
---

16QAM je digitální modulační schéma, které kóduje 4 bity na symbol pomocí změny amplitudy i fáze nosné vlny, čímž poskytuje vyšší datové rychlosti v mobilních sítích 3GPP.

## Popis

16-Quadrature Amplitude Modulation (16QAM) je klíčová digitální modulační technika standardizovaná v rámci 3GPP pro bezdrátové komunikační systémy. Funguje tak, že moduluje dvě ortogonální nosné vlny, typicky složky ve fázi (I) a kvadratuře (Q), přičemž každý symbol představuje 4 bity dat. Konstelační diagram pro 16QAM se skládá z 16 diskrétních bodů uspořádaných do čtvercové mřížky, kde každý bod odpovídá jedinečné kombinaci amplitudy a fáze. To umožňuje přenos 4 bitů na symbol, čímž se zdvojnásobí datová rychlost ve srovnání s kvadraturní fázovou modulací ([QPSK](/mobilnisite/slovnik/qpsk/)), která přenáší 2 bity na symbol. Proces modulace zahrnuje mapování binárních dat na konkrétní konstelační body, které jsou následně převedeny na analogové signály pro přenos přes rádiový kanál.

V systémech 3GPP je 16QAM implementována na fyzické vrstvě, zejména v downlinku pro technologie jako High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) v UMTS a později v LTE a 5G NR. Vysílač používá modulátor ke generování signálů I a Q na základě vstupního bitového toku a aplikuje filtry pro tvarování impulsů k omezení šířky pásma. Na straně přijímače demodulace zahrnuje vzorkování přijatého signálu, odhad stavu kanálu a mapování vzorkovaných bodů zpět na nejbližší konstelační body k obnovení původních bitů. Kódování pro opravu chyb, jako jsou turbo kódy nebo [LDPC](/mobilnisite/slovnik/ldpc/), je často kombinováno s 16QAM ke zmírnění chyb způsobených šumem a interferencí, což zajišťuje spolehlivý přenos dat.

Výkon 16QAM se vyznačuje vyšší spektrální účinností, ale také zvýšenou citlivostí na poměr signálu k šumu ([SNR](/mobilnisite/slovnik/snr/)) ve srovnání s modulacemi nižšího řádu, jako je QPSK. Vyžaduje lepší kvalitu kanálu pro udržení nízké bitové chybovosti ([BER](/mobilnisite/slovnik/ber/)), protože konstelační body jsou blíže u sebe, což je činí náchylnějšími ke zkreslení. Ve specifikacích 3GPP je 16QAM definována v mnoha dokumentech, včetně TS 25.211 pro fyzické kanály a TS 37.902 pro testování. Její role je klíčová pro zvýšení propustnosti downlinku, podporu aplikací jako streamování videa a prohlížení webu a slouží jako základní modulační schéma, které připravilo cestu pro varianty [QAM](/mobilnisite/slovnik/qam/) vyššího řádu, jako jsou [64QAM](/mobilnisite/slovnik/64qam/) a 256QAM, v pokročilých vydáních.

## K čemu slouží

16QAM byla zavedena v 3GPP Release 5, aby řešila rostoucí poptávku po vyšších datových rychlostech v mobilních sítích, zejména s nasazením [HSDPA](/mobilnisite/slovnik/hsdpa/). Před jejím přijetím systémy primárně používaly QPSK, které nabízelo omezenou spektrální účinnost 2 bitů na symbol. Jak se očekávání uživatelů posunula k datově náročným službám, jako je prohlížení internetu a multimédia, vznikla potřeba modulačních schémat, která by mohla přenášet více bitů na symbol bez výrazného zvýšení šířky pásma. 16QAM to vyřešila tím, že umožnila 4 bity na symbol, čímž efektivně zdvojnásobila datovou rychlost ve srovnání s QPSK, a tím zlepšila kapacitu sítě a uživatelský zážitek.

Vytvoření 16QAM bylo motivováno omezeními dřívějších modulačních technik ve standardech 3GPP, jako byly ty v Release 99 UMTS, které se spoléhaly na QPSK pro uplink i downlink. Tyto systémy se potýkaly s efektivní podporou vysokorychlostních datových aplikací, což vedlo k úzkým místům v propustnosti downlinku. Začleněním 16QAM poskytlo 3GPP vyvážené řešení, které zvýšilo datové rychlosti při zachování zvládnutelné složitosti a požadavků na výkon. Umožnilo operátorům efektivněji využívat stávající spektrum, snížit potřebu dodatečných frekvenčních alokací a snížit náklady na nasazení.

Historicky představovala 16QAM významný krok ve vývoji mobilního širokopásmového přístupu, který překlenul propast mezi základními 3G službami a pokročilými 4G technologiemi. Řešila klíčové problémy, jako jsou omezené rychlosti downlinku a neefektivní využití spektra, což umožnilo rychlejší stahování a plynulejší streamování. V následujících vydáních zůstala 16QAM základním modulačním schématem, často používaným ve spojení s adaptivní modulací a kódováním k optimalizaci výkonu na základě podmínek kanálu, což zajišťuje robustní a efektivní komunikaci v různých síťových prostředích.

## Klíčové vlastnosti

- Přenáší 4 bity na symbol pro vyšší datové rychlosti
- Používá 16bodový čtvercový konstelační diagram pro modulaci amplitudy a fáze
- Zvyšuje spektrální účinnost ve srovnání s QPSK
- Vyžaduje vyšší SNR pro spolehlivý provoz kvůli menšímu rozestupu konstelačních bodů
- Implementována v downlinku pro HSDPA, LTE a 5G NR
- Podporuje adaptivní modulaci a kódování pro adaptaci spoje

## Související pojmy

- [QPSK – Quadrature Phase Shift Keying](/mobilnisite/slovnik/qpsk/)
- [64QAM – 64 Quadrature Amplitude Modulation](/mobilnisite/slovnik/64qam/)
- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)

## Definující specifikace

- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TR 37.902** (Rel-19) — OTA TRP/TRS Measurement for LTE Terminals

---

📖 **Anglický originál a plná specifikace:** [16QAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/16qam/)
