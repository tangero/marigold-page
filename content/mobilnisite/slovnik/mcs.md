---
slug: "mcs"
url: "/mobilnisite/slovnik/mcs/"
type: "slovnik"
title: "MCS – Modulation and Coding Schemes"
date: 2026-01-01
abbr: "MCS"
fullName: "Modulation and Coding Schemes"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mcs/"
summary: "Předdefinovaná kombinace řádu modulace a kódové rychlosti, která určuje, jak se datové bity mapují na rádiové symboly pro přenos. Jedná se o základní mechanismus adaptace spojení v bezdrátových systém"
---

MCS je předdefinovaná kombinace řádu modulace a kódové rychlosti, která určuje, jak se datové bity mapují na rádiové symboly, a dynamicky vyvažuje přenosovou rychlost a robustnost na základě stavu rádiového kanálu.

## Popis

Modulační a kódová schémata (MCS) jsou klíčovým prvkem fyzické vrstvy ve všech bezdrátových technologiích 3GPP od GSM po 5G NR. Index MCS odkazuje na konkrétní pár modulačního formátu (např. QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM, 1024QAM) a kódové rychlosti pro dopřednou korekci chyb ([FEC](/mobilnisite/slovnik/fec/)). Řád modulace definuje, kolik bitů je přenášeno na jeden symbol (např. 2 bity pro QPSK, 10 bitů pro 1024QAM), zatímco kódová rychlost představuje poměr informačních bitů k celkovému počtu přenesených bitů (včetně redundance). Vyšší index MCS typicky značí modulaci vyššího řádu a/nebo vyšší (méně robustní) kódovou rychlost, což poskytuje vyšší teoretickou datovou propustnost, ale vyžaduje lepší poměr signálu k šumu (SNR) pro úspěšné dekódování.

Během provozu síť (konkrétně plánovač základnové stanice) dynamicky vybírá MCS pro každého uživatele a každý přenosový časový interval na základě ukazatelů kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) hlášených uživatelským zařízením (UE). Tento proces se nazývá adaptace spojení. UE měří kvalitu downlink kanálu a prostřednictvím zpětné vazby CQI doporučuje index MCS. Základnová stanice jej spolu s dalšími faktory, jako je stav vyrovnávací paměti a požadavky na QoS, využívá k přidělení zdrojů a k instruktáži UE, které MCS má použít pro nadcházející downlink přenos (nebo uplink grant). Zvolené MCS přímo určuje velikost transportního bloku (TBS), což je množství dat odeslaných v rámci alokace fyzického zdrojového bloku.

Úlohou MCS v síti je maximalizovat spektrální účinnost při zachování přijatelné chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)). Při dobrých podmínkách kanálu se používá vysoké MCS pro dosažení špičkových datových rychlostí. Při špatných podmínkách (např. na okraji buňky) je zvoleno nižší, robustnější MCS pro zajištění spolehlivosti na úkor okamžité propustnosti. Toto dynamické přizpůsobování je kontinuální a probíhá v řádu milisekund. Tabulky MCS jsou definovány ve specifikacích 3GPP (např. TS 36.213 pro LTE, TS 38.214 pro NR), přičemž různé tabulky jsou optimalizovány pro různé scénáře, jako je provoz s normální nebo nízkou spektrální účinností, a pro různé typy kanálů ([PDSCH](/mobilnisite/slovnik/pdsch/), PUSCH). Vývoj MCS byl klíčový pro zvyšování špičkových datových rychlostí napříč generacemi, a to zavedením modulací vyššího řádu (až po 1024QAM v 5G) a efektivnějšího kódování (jako je [LDPC](/mobilnisite/slovnik/ldpc/) v NR).

## K čemu slouží

MCS existuje k řešení základní výzvy v bezdrátových komunikacích: časově proměnlivé a na poloze závislé povahy rádiového kanálu. Pevně nastavená modulace a kódování by byla vysoce neefektivní; používání robustního schématu s nízkou rychlostí všude by plýtvalo kapacitou, zatímco používání schématu s vysokou rychlostí všude by vedlo k častým selháním při špatných podmínkách. Adaptace spojení prostřednictvím MCS umožňuje systému přizpůsobit přenosové parametry okamžité kvalitě kanálu každého uživatele, čímž optimalizuje kompromis mezi datovou rychlostí a spolehlivostí na úrovni každého paketu.

Historicky byla adaptivní modulace a kódování zavedena v 3GPP s technologií [EDGE](/mobilnisite/slovnik/edge/) (Enhanced Data rates for GSM Evolution) a stala se ústředním prvkem v UMTS HSDPA/HSUPA. Řešila tak omezení schémat s pevnou rychlostí v dřívějších celulárních systémech. Motivací pro její kontinuální vývoj byl neustálý tlak na vyšší spektrální účinnost a datové rychlosti pro uspokojení rostoucí uživatelské poptávky. Každá nová technologie rádiového přístupu (LTE, 5G NR) rozšířila rozsah MCS zavedením modulací vyššího řádu (64QAM, 256QAM, 1024QAM) a efektivnějších schémat kanálového kódování (Turbo kódy ve 3G/4G, LDPC a Polar kódy v 5G). Tato vylepšení spolu se širšími šířkami pásma a masivním MIMO umožnila víceGbps datové rychlosti slibované moderními celulárními sítěmi. MCS je přímým nástrojem, který přeměňuje zlepšenou kvalitu signálu na vyšší propustnost pro uživatele.

## Klíčové vlastnosti

- Dynamický výběr na základě zpětné vazby o kvalitě kanálu v reálném čase (CQI)
- Definuje pár řádu modulace (např. od QPSK po 1024QAM) a kódové rychlosti
- Přímo určuje velikost transportního bloku (TBS) pro danou alokaci zdrojů
- Implementováno prostřednictvím standardizovaných tabulek indexovaných indexem MCS
- Základní prvek adaptace spojení, vyvažující datový tok a robustnost přenosu
- Vyvíjí se s každou verzí 3GPP pro podporu vyšší spektrální účinnosti a nových případů užití

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.119** (Rel-19) — Maritime Communication Service Requirements
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management
- **TS 24.482** (Rel-19) — Mission Critical Services Identity Management
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- … a dalších 49 specifikací

---

📖 **Anglický originál a plná specifikace:** [MCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcs/)
