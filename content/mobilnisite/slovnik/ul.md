---
slug: "ul"
url: "/mobilnisite/slovnik/ul/"
type: "slovnik"
title: "UL – Uplink"
date: 2026-01-01
abbr: "UL"
fullName: "Uplink"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ul/"
summary: "Směr přenosu od uživatelského zařízení (UE) k základnové stanici sítě. Je základním prvkem všech mobilních komunikací, umožňuje nahrávání dat, signalizaci a řídicí zpětnou vazbu. Jeho výkon přímo ovli"
---

UL je směr přenosu od uživatelského zařízení (UE) k základnové stanici sítě, který umožňuje nahrávání dat, signalizaci a řídicí zpětnou vazbu v mobilních komunikacích.

## Popis

Uplink ([UL](/mobilnisite/slovnik/up-link/)) označuje rádiovou přenosovou cestu od uživatelského zařízení (UE) k základnové stanici sítě (Node B, [eNB](/mobilnisite/slovnik/enb/) nebo gNB). Tento směr je klíčový pro všechny formy komunikace iniciované uživatelem, včetně hovorů, nahrávání dat a přenosu řídicí signalizace z UE do sítě. UL funguje ve specifických kmitočtových pásmech přidělených sítí a je řízen složitými plánovacími algoritmy v základnové stanici za účelem optimalizace využití zdrojů, správy rušení a zajištění kvality služby (QoS). Z architektonického hlediska je UL součástí rozhraní Uu (vzdušného rozhraní), definovaného v řadě 3GPP technických specifikací, které stanovují jeho charakteristiky fyzické vrstvy, strukturu kanálů a protokoly. Klíčové součásti UL zahrnují fyzické kanály, jako je Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)) pro data, Physical Uplink Control Channel ([PUCCH](/mobilnisite/slovnik/pucch/)) pro řídicí informace, a referenční signály, jako jsou Sounding Reference Signals ([SRS](/mobilnisite/slovnik/srs/)) pro odhad kanálu. Plánovač základnové stanice dynamicky přiděluje časově-frekvenční zdroje (Resource Blocks) jednotlivým UE na základě faktorů, jako je stav vyrovnávací paměti, indikátory kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) a požadavky QoS. Kriticky důležité jsou také mechanismy řízení výkonu, které zajišťují, že UE vysílá s dostatečným výkonem pro spolehlivý příjem, aniž by způsobovalo nadměrné rušení ostatním uživatelům. Výkon UL se měří metrikami, jako je propustnost, latence a spolehlivost, které jsou zásadní pro služby od prohlížení webu až po ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)). Jeho návrh a optimalizace jsou ústřední pro celkovou kapacitu a uživatelský zážitek v celulárních sítích.

## K čemu slouží

Uplink existuje proto, aby umožnil obousměrnou komunikaci v celulárních sítích, což uživatelským zařízením dovoluje odesílat data, hlas a řídicí informace do sítě. Bez robustního [UL](/mobilnisite/slovnik/up-link/) by mobilní sítě byly systémy pouze pro příjem, neschopné interaktivních služeb, uživatelského obsahu nebo responzivních řídicích smyček. Historicky měly rané mobilní systémy, jako 1G, pouze základní UL schopnosti primárně pro hlas. Vytvoření a kontinuální vývoj UL v normách 3GPP bylo motivováno potřebou podporovat stále asymetričtější, ale vitální provoz v uplinku, jako je odesílání e-mailů, nahrávání fotografií a videí a poskytování zpětné vazby v reálném čase pro síťově řízené procedury, jako je předávání hovoru (handover) a adaptace spoje. Řeší výzvu efektivního řízení sdíleného média, kde více zařízení soutěží o přenosové příležitosti, což vyžaduje sofistikované plánování, koordinaci rušení a řízení výkonu pro maximalizaci spektrální účinnosti a kapacity sítě při současném šetření životnosti baterie UE.

## Klíčové vlastnosti

- Směr přenosu od UE k základnové stanici (gNB/eNB/Node B)
- Využívá vyhrazené fyzické kanály (např. PUSCH, PUCCH, PRACH)
- Používá dynamické plánování ze strany sítě pro přidělování zdrojů
- Zahrnuje řízení výkonu pro správu rušení a životnosti baterie UE
- Používá referenční signály (např. DM-RS, SRS) pro odhad kanálu a synchronizaci
- Podporuje různé modulační schémata a kódovací rychlosti pro adaptivní datové rychlosti

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)
- [SRS – Space Radiocommunication Stations](/mobilnisite/slovnik/srs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.916** (Rel-16) — Rel-16 Description Summary
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- … a dalších 35 specifikací

---

📖 **Anglický originál a plná specifikace:** [UL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ul/)
