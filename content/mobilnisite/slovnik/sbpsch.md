---
slug: "sbpsch"
url: "/mobilnisite/slovnik/sbpsch/"
type: "slovnik"
title: "SBPSCH – Shared Basic Physical Sub CHannel"
date: 2025-01-01
abbr: "SBPSCH"
fullName: "Shared Basic Physical Sub CHannel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sbpsch/"
summary: "Fyzický rádiový zdroj v sítích GPRS a EDGE vytvořený rozdělením základního fyzického kanálu. Umožňuje více uživatelům sdílet jednu časovou štěrbinu přidělením různých subkanálů, čímž zvyšuje spektráln"
---

SBPSCH je sdílený základní fyzický subkanál v sítích GPRS/EDGE, který rozděluje základní kanál, aby umožnil více uživatelům sdílet jednu časovou štěrbinu, čímž zvyšuje spektrální účinnost a kapacitu pro paketová data.

## Popis

Sdílený základní fyzický subkanál (SBPSCH) je klíčový mechanismus přidělování zdrojů na fyzické vrstvě definovaný ve specifikacích GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), zejména pro službu General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)) a Enhanced Data rates for GSM Evolution (EDGE). Funguje na základní fyzické struktuře GSM, kde je rádiový kmitočtový kanál rozdělen na 4,615ms rámce, z nichž každý obsahuje 8 časových štěrbin. Základní fyzický kanál je definován jako jedna časová štěrbina opakující se v každém rámci. SBPSCH vzniká dalším rozdělením tohoto základního kanálu v kódové doméně, což umožňuje jeho sdílení mezi více mobilními stanicemi ([MS](/mobilnisite/slovnik/ms/)).

Technicky je sdílení dosaženo kombinací principů časového a kódového dělení, nejedná se však o [CDMA](/mobilnisite/slovnik/cdma/) ve smyslu [WCDMA](/mobilnisite/slovnik/wcdma/). V praxi síť přiděluje konkrétní rádiové zdroje dočasnému blokovému toku ([TBF](/mobilnisite/slovnik/tbf/)), což je logické spojení pro přenos paketových dat. SBPSCH je jedním z možných typů zdrojů, které mohou být TBF přiděleny. Představuje podíl na kapacitě fyzické časové štěrbiny. Na jedné fyzické časové štěrbině může existovat více SBPSCH, přičemž každý SBPSCH přenáší paketové datové bloky pro různé uživatele. Síť toto sdílení spravuje pomocí příznaků stavu uplink ([USF](/mobilnisite/slovnik/usf/)) na downlinku nebo explicitních povolení plánování, které řídí, které MS smí vysílat nebo je naplánováno k příjmu v daném období rádiového bloku.

Z architektonického pohledu SBPSCH existuje v rámci struktury Paketového datového fyzického kanálu (PDCH). PDCH používá strukturu 52mnohorámce a rádiové bloky (každý sestávající ze 4 normálních výbuchů) jsou jednotkami přenosu dat. SBPSCH definuje, jak je přístup k těmto rádiovým blokům rozdělen mezi uživatele. Jeho role je klíčová pro statistickou výhodu multiplexování v paketově přepínaných sítích. Tím, že umožňuje dynamické, jemně odstupňované sdílení fyzické časové štěrbiny, umožňuje SBPSCH síti efektivně obsloužit mnoho uživatelů dat s nízkou aktivitou nebo přerušovaným přenosem bez nutnosti vyhradit každému z nich celou časovou štěrbinu. To ve srovnání s okruhově přepínanými spojeními významně zvyšuje celkovou kapacitu a spektrální účinnost sítě GERAN pro datové služby.

## K čemu slouží

SBPSCH byl vyvinut pro efektivní podporu trhavé, přerušované povahy paketového datového provozu v rámci infrastruktury GSM optimalizované primárně pro hlas. Před GPRS používalo GSM okruhově přepínaná spojení, kde jeden uživatel po dobu hovoru obsadil celou časovou štěrbinu, což bylo pro datové aplikace se sporadickými přenosovými potřebami neefektivní. Vytvoření SBPSCH tuto neefektivitu řešilo tím, že umožnilo skutečné sdílení zdrojů.

Primární problém, který řeší, je nízká spektrální účinnost pro data. Tím, že umožňuje více uživatelům sdílet jednu fyzickou časovou štěrbinu, může síť statisticky multiplexovat mnoho datových relací, což vede k mnohem vyšší kapacitě a lepšímu využití vzácného rádiového spektra. Jednalo se o zásadní posun od vyhrazených ke sdíleným zdrojům. Motivací byla rostoucí poptávka po mobilních datových službách na konci 90. let a začátku 21. století, jako je prohlížení webu a e-mail, které vyžadovaly efektivnější mechanismus rádiového rozhraní, než jaký mohla poskytnout okruhově přepínaná data. SBPSCH jako součást standardů GPRS a později EDGE tento mechanismus poskytl a přeměnil sítě GSM na životaschopné platformy pro mobilní přístup k internetu bez nutnosti zcela nové rádiové technologie.

## Klíčové vlastnosti

- Umožňuje více uživatelům sdílet jednu fyzickou časovou štěrbinu GSM/EDGE (Základní fyzický kanál)
- Základní jednotka zdroje pro paketový datový provoz GPRS/EDGE (TBF)
- Zvyšuje kapacitu sítě a spektrální účinnost prostřednictvím statistického multiplexování
- Dynamicky spravován sítí pomocí příznaků stavu uplink (USF) a plánování
- Funguje v rámci struktury 52mnohorámce Paketového datového kanálu (PDCH)
- Podporuje přenos paketových dat jak na uplinku, tak na downlinku

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [PDCH – Packet Data Channel](/mobilnisite/slovnik/pdch/)
- [USF – Uplink State Flag](/mobilnisite/slovnik/usf/)

## Definující specifikace

- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SBPSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbpsch/)
