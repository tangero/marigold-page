---
slug: "prcf"
url: "/mobilnisite/slovnik/prcf/"
type: "slovnik"
title: "PRCF – Positioning Radio Co-ordination Function"
date: 2025-01-01
abbr: "PRCF"
fullName: "Positioning Radio Co-ordination Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/prcf/"
summary: "Síťová funkce odpovědná za koordinaci rádiových zdrojů a procedur pro služby založené na poloze. Řídí interakce mezi jádrem sítě (Core) a rádiovou přístupovou sítí (RAN) pro podporu metod určování pol"
---

PRCF je síťová funkce, která koordinuje rádiové zdroje a procedury pro lokalizační služby, řídí interakce mezi jádrem sítě (Core) a rádiovou přístupovou sítí, aby podpořila lokalizační metody jako Cell-ID, OTDOA a A-GPS.

## Popis

Positioning Radio Co-ordination Function (PRCF) je funkční entita definovaná v architektuře 3GPP pro zajištění lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)). Funguje jako prostředník mezi servisním mobilním lokalizačním centrem ([SMLC](/mobilnisite/slovnik/smlc/)) nebo bránovým mobilním lokalizačním centrem ([GMLC](/mobilnisite/slovnik/gmlc/)) v jádru sítě a rádiovou přístupovou sítí (RAN). Její hlavní úlohou je řídit rádiově specifické aspekty určování polohy a odstiňovat složitosti různých technologií RAN (jako [UTRAN](/mobilnisite/slovnik/utran/) nebo [GERAN](/mobilnisite/slovnik/geran/)) od jádra sítě. PRCF přijímá požadavky na určení polohy z jádra sítě, které zahrnují požadované parametry kvality služeb (QoS), jako je přesnost a doba odezvy. Tyto požadavky pak překládá do konkrétních rádiových procedur, vybírá a koordinuje příslušnou lokalizační metodu na základě schopností UE, stavu sítě a požadované QoS.

Z architektonického hlediska může být PRCF integrována do uzlu RAN, jako je řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UTRAN nebo řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) v GERAN. Rozhraní k jádru sítě zprostředkovává přes rozhraní Iupc (ke SMLC) a k dalším prvkům RAN. Mezi klíčové součásti její činnosti patří řízení příkazů k měření. Například pro metodu [OTDOA](/mobilnisite/slovnik/otdoa/) (Observed Time Difference of Arrival) PRCF nařídí UE provedení měření na lokalizačních referenčních signálech ze sousedních buněk a může také koordinovat s těmito buňkami, aby zajistila vysílání potřebných referenčních signálů. Shromažďuje surová měřicí data (např. časové předstižení, sílu signálu) od UE a případně od sítě, provádí jejich předběžné zpracování a předává výsledky lokalizačnímu uzlu v jádře sítě pro konečný výpočet polohy.

PRCF hraje klíčovou roli při podpoře více lokalizačních metod definovaných 3GPP. Mezi ně patří metody založené na síti, jako je Cell-ID (s časovým předstižením nebo bez něj), metody s asistencí UE, jako je OTDOA a Assisted-GNSS (A-GPS), a metody prováděné přímo v UE. U metod s asistencí UE PRCF zajišťuje doručení pomocných dat (např. efemerid satelitů pro A-GPS nebo informací o sousedních buňkách pro OTDOA) do UE. Řídí také nezbytná období ticha nebo konfiguraci speciálních lokalizačních podrámců pro zajištění přesných měření. Centralizací této rádiové koordinace PRCF umožňuje efektivní využití rádiových zdrojů, minimalizuje latenci určování polohy a zajišťuje hladký provoz lokalizačních služeb napříč různými nasazeními RAN a generacemi UE, čímž tvoří základní prvek pro komerční a regulatorní služby založené na poloze.

## K čemu slouží

PRCF byla zavedena jako odpověď na rostoucí potřebu standardizovaných, spolehlivých a přesných lokalizačních služeb v mobilních sítích, poháněnou zpočátku regulatorními požadavky na lokalizaci volajícího při tísňovém volání (např. E911 v USA) a následně komerčními aplikacemi. Před její standardizací existovaly proprietární nebo nekoordinované metody sběru rádiových měření pro určování polohy, což vedlo k problémům s interoperability, neefektivnímu využití zdrojů a nekonzistentní kvalitě služeb napříč různými dodavateli síťového vybavení a technologiemi RAN.

Její vznik byl motivován nutností oddělit lokalizační logiku v jádru sítě od rádiově specifických implementačních detailů. Bez PRCF by si lokalizační server v jádru sítě musel udržovat detailní znalost měřicích procedur a signalizace každé technologie RAN, což by systém učinilo složitým a nepružným. PRCF tuto vrstvu abstrahuje, což umožňuje jádru sítě vydávat obecné požadavky na určení polohy. Tato abstrakce činí architekturu připravenou na budoucnost a umožňuje zavádění nových lokalizačních metod (jako je UTDOA nebo lokalizace s podporou senzorů) v RAN bez nutnosti zásadních změn v entitách jádra sítě. Řeší problém koordinované alokace zdrojů pro určování polohy a zajišťuje, že když je UE vyzvána k měření sousedních buněk pro OTDOA, jsou tyto buňky vhodně nakonfigurovány k vysílání potřebných lokalizačních referenčních signálů, což je klíčové pro přesnost v hustých nebo synchronizovaných sítích.

## Klíčové vlastnosti

- Koordinuje alokaci rádiových zdrojů pro lokalizační měření.
- Podporuje více lokalizačních metod podle 3GPP (Cell-ID, OTDOA, A-GNSS).
- Tvoří rozhraní mezi SMLC/GMLC jádra sítě (Core Network) a rádiovou přístupovou sítí (RAN).
- Řídí doručení lokalizačních pomocných dat do UE.
- Zajišťuje sběr a předběžné zpracování měření z UE a ze sítě.
- Abstrahuje RAN-specifické procedury pro lokalizační služby jádra sítě.

## Související pojmy

- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [PRCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/prcf/)
