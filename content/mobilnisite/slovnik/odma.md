---
slug: "odma"
url: "/mobilnisite/slovnik/odma/"
type: "slovnik"
title: "ODMA – Opportunity Driven Multiple Access"
date: 2025-01-01
abbr: "ODMA"
fullName: "Opportunity Driven Multiple Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/odma/"
summary: "Koncept síťové architektury založený na přenosu (relay), v němž může uživatelské zařízení (UE) fungovat jako přenosový uzel (relay node) pro rozšíření síťového pokrytí a kapacity. Umožňuje více-skokov"
---

ODMA je koncept síťové architektury založený na přenosu (relay), v němž může uživatelské zařízení (UE) fungovat jako přenosový uzel (relay node) a umožnit tak více-skokovou komunikaci, čímž rozšiřuje pokrytí a kapacitu vytvořením dynamické, samoorganizující se přístupové sítě.

## Popis

Opportunity Driven [Multiple Access](/mobilnisite/slovnik/multiple-access/) (ODMA) je koncept síťové architektury a protokolu standardizovaný v raných vydáních 3GPP (především pro 3G/UMTS), který zavádí více-skokovou přenosovou schopnost (multi-hop relay) do buněčných systémů. Jeho základní princip spočívá v tom, že uživatelské zařízení (UE) může nejen komunikovat přímo se základnovou stanicí (Node B), ale také fungovat jako přenosový uzel (relay) pro jiná UEs. V síti ODMA může UE se špatným přímým rádiovým spojením do sítě objevit a připojit se prostřednictvím mezilehlého UE (přenosového uzlu), které má lepší spojení. Tento proces může pokračovat přes více skoků a vytvářet tak dynamické, ad-hoc rozšíření rádiové přístupové sítě.

Z architektonického hlediska ODMA zavádí nové logické role: Vzdálené UE (Remote UE, které se nemůže přímo připojit k síti), Přenosové UE (Relay UE, které má spojení a může přenášet provoz) a standardní infrastrukturu (Node B a RNC). Protokol funguje ve dvou odlišných fázích: fázi objevování přístupu (Access Discovery Phase) a fázi komunikace (Communication Phase). Během objevování UEs vysílají a skenují ODMA objevovací kódy (discovery codes), aby identifikovaly potenciální přenosové partnery na základě síly signálu a schopností. Jakmile je trasa navázána, fáze komunikace zahrnuje směrování datových paketů přes přenosový řetězec. Každé přenosové UE provádí demodulaci a dekódování signálu z předchozího skoku před jeho znovu modulací a vysláním do dalšího skoku, což vyžaduje, aby mělo plnou schopnost protokolového zásobníku.

Jak to funguje, zahrnuje distribuované směrovací algoritmy. ODMA definuje specifickou signalizaci na rádiovém rozhraní pro objevování tras, jejich údržbu a ukončení. Vrstva pro směrování a přenos (Routing and Relay Layer, RRL), což je podvrstva přidaná k rádiovému protokolovému zásobníku, tyto funkce spravuje. Činí rozhodnutí na základě metrik, jako je přijímaný výkon signálu, počet skoků a úroveň baterie přenosového UE. Systém je "řízený příležitostmi" (opportunity driven), protože přenosová spojení jsou vytvářena příležitostně na základě blízkosti a schopností okolních UEs, místo aby byla předem plánována sítí. Pro síťový řadič (RNC) se více-skokové ODMA spojení může jevit jako jediný, byť potenciálně složitější, rádiový přístupový nosič (radio access bearer). RNC spravuje prostředky pro celý řetězec, ale nemusí být vědom jednotlivých přenosových skoků, v závislosti na variantě implementace. Tato architektura výrazně mění tradiční hvězdicovou topologii buněčných sítí a vytváří na okraji strukturu podobnou mesh síti.

## K čemu slouží

ODMA bylo koncipováno k řešení základních omezení pokrytí a kapacity raných 3G buněčných sítí, zejména na okrajích buněk a v dírách pokrytí. Tradiční buněčné sítě vyžadují přímé, dostatečně silné rádiové spojení mezi UE a základnovou stanicí. To si vynucuje husté a nákladné nasazení základnových stanic pro zajištění všudypřítomného pokrytí, zvláště v náročných prostředích, jako jsou venkovské oblasti, vnitřky budov nebo během katastrofických scénářů, kdy je infrastruktura poškozena. ODMA to chtělo vyřešit využitím stávající populace UEs k organickému rozšíření sítě.

Historický kontext je jeho vývoj v éře UMTS jako pokrokového konceptu pro integraci ad-hoc sítí. Byl motivován snahou zvýšit síťovou kapacitu a pokrytí bez úměrného zvýšení nákladů na infrastrukturu. Umožněním více-skokové komunikace mohlo ODMA zlepšit kvalitu signálu pro okrajové uživatele jejich připojením přes přenosový uzel s lepším spojením, čímž se zvýšila celková kapacita systému a snížil se potřebný vysílací výkon koncových zařízení, což prodlužuje životnost baterie. Řešilo omezení rigidní buněčné topologie zavedením flexibility a odolnosti, čímž vznikla samoopravná síť, kde si uživatelé mohli navzájem pomáhat udržovat konektivitu. Přestože nebylo v 3G široce komerčně nasazeno, koncepty představené ODMA přímo ovlivnily pozdější technologie 3GPP, jako je komunikace zařízení-zařízení (Device-to-Device, [D2D](/mobilnisite/slovnik/d2d/)) a postranní přenos (sidelink relay) v 4G LTE a 5G NR pro služby založené na blízkosti (Proximity Services, ProSe) a pro veřejnou bezpečnost.

## Klíčové vlastnosti

- Umožňuje více-skokovou přenosovou komunikaci, kde UEs mohou přeposílat provoz pro jiná UEs.
- Rozšiřuje síťové pokrytí a kapacitu bez dodatečné pevné infrastruktury.
- Funguje s 'příležitostným' (opportunistic) objevovacím protokolem pro dynamické vytváření přenosových řetězců.
- Zavádí vrstvu pro směrování a přenos (Routing and Relay Layer, RRL) do protokolového zásobníku UE.
- Podporuje jak transparentní, tak netransparentní režimy přenosu vůči síťovému řadiči.
- Může zlepšit kvalitu spojení pro okrajové uživatele a snížit celkový vysílací výkon UE.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [ODMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/odma/)
