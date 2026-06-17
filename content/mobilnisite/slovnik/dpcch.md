---
slug: "dpcch"
url: "/mobilnisite/slovnik/dpcch/"
type: "slovnik"
title: "DPCCH – Dedicated Physical Control Channel"
date: 2025-01-01
abbr: "DPCCH"
fullName: "Dedicated Physical Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dpcch/"
summary: "Vyhrazený (dedikovaný) fyzický kanál v uplinku v UMTS/WCDMA, který přenáší řídicí informace pro jednotlivého uživatele. Vysílá pilotní bity pro odhad kanálu, indikátor kombinace transportního formátu"
---

DPCCH je vyhrazený (dedikovaný) fyzický kanál v uplinku v UMTS/WCDMA, který přenáší řídicí informace, jako jsou pilotní bity, TFCI, FBI a příkazy TPC, pro údržbu spojení jednotlivého uživatele, řízení výkonu a demodulaci.

## Popis

Dedicated Physical Control Channel (DPCCH) je základní součástí rozhraní UMTS/WCDMA, konkrétně v rámci UTRAN. Jedná se o vyhrazený (dedikovaný) fyzický kanál v uplinku, což znamená, že je přidělen jednotlivému uživatelskému zařízení (UE) po dobu trvání dedikovaného spojení. DPCCH je vždy vysílán paralelně s kanálem Dedicated Physical Data Channel ([DPDCH](/mobilnisite/slovnik/dpdch/)), když je aktivní vyhrazený transportní kanál ([DCH](/mobilnisite/slovnik/dch/)). Jeho hlavní rolí je přenášet nezbytné řídicí informace fyzické vrstvy, které umožňují Node B úspěšně přijímat a dekódovat uživatelská data na DPDCH.

DPCCH vysílá nepřetržitý proud řídicích symbolů organizovaných do slotů a rámců. Každý 10 ms rádiový rámec je rozdělen na 15 slotů. Informace vysílané na DPCCH zahrnují pilotní bity, indikátor kombinace transportního formátu (TFCI), zpětnovazební informaci ([FBI](/mobilnisite/slovnik/fbi/)) a příkaz pro řízení vysílacího výkonu (TPC). Pilotní bity jsou známé sekvence používané Node B pro odhad kanálu, což je klíčové pro koherentní demodulaci dat na DPDCH v podmínkách útlumu. TFCI informuje přijímač o kombinaci transportního formátu použité v odpovídajícím rámci DPDCH, což umožňuje správné demultiplexování a dekódování služeb s proměnnou přenosovou rychlostí. Bity FBI se používají pro podporu Site Selection Diversity Transmission (SSDT) a režimů uzavřené smyčky pro diverzitu vysílání. Bity TPC přenášejí příkazy pro řízení výkonu od UE k Node B, kterými mu nařizují zvýšit nebo snížit svůj vysílací výkon v downlinku, což je zásadní pro překonání problému blízko-daleko a udržení kvality spoje.

Z architektonického hlediska je DPCCH součástí mapování fyzické vrstvy definované v 3GPP TS 25.211. Používá samostatný kanalizační kód (rozprostírací kód) než DPDCH. V uplinku jsou DPCCH a DPDCH multiplexovány kódem I/Q; jsou vysílány současně pomocí různých větví kvadraturního fázového klíčování (QPSK). DPCCH je rozprostírán vlastním kanalizačním kódem a je vždy vysílán s pevným, nízkým rozprostíracím faktorem (typicky 256). Jeho výkonová úroveň je nastavována vzhledem k DPDCH, aby bylo zajištěno spolehlivé přijetí řídicích informací i při nízkém výkonu datového kanálu. Nepřetržité vysílání DPCCH, dokonce i v obdobích bez přenosu dat ([DTX](/mobilnisite/slovnik/dtx/)), umožňuje Node B udržovat synchronizaci, odhady kanálu a smyčky řízení výkonu, což zajišťuje, že dedikované spojení zůstává připraveno na okamžitý přenos dat.

## K čemu slouží

DPCCH byl vytvořen k řešení základních požadavků na řízení dedikovaných spojení v sítích UMTS založených na WCDMA. Předchozí mobilní systémy, jako GSM, používaly časový multiplex, kde se řídicí a datové informace mohly prolínat v čase. Použití mnohonásobného přístupu s kódovým dělením ([CDMA](/mobilnisite/slovnik/cdma/)) v WCDMA vyžadovalo jiný přístup pro nepřetržité řídicí signalizace s nízkou latencí, která by mohla koexistovat s uživatelskými daty s proměnnou rychlostí. DPCCH poskytuje pro každého aktivního uživatele vyhrazený, trvale aktivní řídicí kanál.

Jeho existence řeší několik klíčových problémů: umožňuje rychlé a přesné řízení výkonu pro zvládnutí interference v systému CDMA, poskytuje informace o stavu kanálu pro koherentní demodulaci v prostředí s útlumem a signalizuje okamžitý datový formát pro flexibilní a efektivní využití šířky pásma. Bez vyhrazeného řídicího kanálu, jako je DPCCH, by Node B postrádal informace v reálném čase potřebné k udržení stabilního, vysokokvalitního rádiového spoje, což by vedlo ke špatnému výkonu, přerušeným hovorům a neefektivnímu využití rádiových zdrojů. DPCCH je tedy základním kamenem návrhu fyzické vrstvy WCDMA, který umožňuje spolehlivou podporu vyhrazených služeb s přepojováním okruhů i paketů.

## Klíčové vlastnosti

- Přenáší řídicí informace fyzické vrstvy v uplinku (pilotní signál, TFCI, FBI, TPC).
- Používá pevný, nízký rozprostírací faktor (např. 256) pro robustní přenos.
- V uplinku je multiplexován kódem I/Q společně s DPDCH.
- Umožňuje rychlé řízení výkonu v uzavřené smyčce (1500 Hz).
- Poskytuje pilotní symboly pro odhad kanálu a koherentní demodulaci.
- Je vysílán nepřetržitě, aby udržoval synchronizaci spoje a řídicí smyčky.

## Související pojmy

- [DPDCH – Dedicated Physical Data Channel](/mobilnisite/slovnik/dpdch/)
- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)
- [FBI – Final Block Indicator](/mobilnisite/slovnik/fbi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 25.823** (Rel-8) — Synchronised E-DCH Study for UTRA FDD
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [DPCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpcch/)
