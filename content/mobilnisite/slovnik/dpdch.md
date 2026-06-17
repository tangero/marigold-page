---
slug: "dpdch"
url: "/mobilnisite/slovnik/dpdch/"
type: "slovnik"
title: "DPDCH – Dedicated Physical Data Channel"
date: 2025-01-01
abbr: "DPDCH"
fullName: "Dedicated Physical Data Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dpdch/"
summary: "Dedicated Physical Data Channel (DPDCH) je základní fyzický kanál pro uplink v UMTS (WCDMA), který přenáší vyhrazená uživatelská data z uživatelského zařízení (UE) do Node B. Jde o kanál s kódovým mul"
---

DPDCH je základní fyzický kanál pro uplink v UMTS (WCDMA), který přenáší vyhrazená uživatelská data z UE do Node B a tvoří jádrový transportní mechanismus pro služby s přepojováním okruhů a přepojováním paketů.

## Popis

DPDCH je klíčovou součástí fyzické vrstvy rádiového rozhraní WCDMA. Je zodpovědný za přenos vyhrazených uživatelských dat generovaných na vrstvě 2 a výše (z transportního kanálu Dedicated Channel - [DCH](/mobilnisite/slovnik/dch/)) přes rádiové spojení. V uplinku může UE vysílat jeden nebo více DPDCH paralelně s jediným Dedicated Physical Control Channel ([DPCCH](/mobilnisite/slovnik/dpcch/)). DPCCH nese nezbytné řídicí informace, jako jsou pilotní bity pro odhad kanálu, indikátor kombinace transportního formátu (TFCI) a příkazy pro řízení výkonu.

Kanál funguje pomocí Direct-Sequence Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([DS-CDMA](/mobilnisite/slovnik/ds-cdma/)). Každý DPDCH je rozprostřen kanalizačním kódem (Orthogonal Variable Spreading Factor code), aby byl oddělen od ostatních kanálů ze stejné UE. DPDCH a DPCCH jsou následně zkombinovány pomocí [IQ](/mobilnisite/slovnik/iq/)/kódového multiplexu. DPDCH je mapován na I (In-phase) nebo Q (Quadrature) větev, zatímco DPCCH je mapován na druhou z nich. Tento IQ multiplex umožňuje kontinuální přenos, což je výhodné pro stabilitu řízení výkonu a snižuje elektromagnetické rušení. Datová rychlost na DPDCH je proměnná a řízena rozprostíracím faktorem, který může být dynamicky přizpůsoben tak, aby odpovídal požadované datové rychlosti služby.

Z architektonického pohledu existuje DPDCH mezi UE a Node B. V přijímači Node B jsou po desprezování a demodulaci data z DPDCH předána výše do vrstvy Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). Konfigurace DPDCH, včetně jeho rozprostíracího faktoru a počtu paralelních kanálů, je stanovena Radio Network Controllerem (RNC) prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) na základě kvality a datové rychlosti požadované služby. Jeho role byla klíčová pro poskytování vyhrazené šířky pásma pro hlasové hovory a rané mobilní datové služby v sítích UMTS.

## K čemu slouží

DPDCH byl vytvořen, aby poskytoval vyhrazené, spolehlivé a proměnné fyzické spojení pro uživatelská data v systému UMTS WCDMA. Řešil problém efektivní podpory širokého spektra služeb – od nízkorychlostního hlasu po vyšší rychlosti paketových dat – ve sdíleném spektru pomocí [CDMA](/mobilnisite/slovnik/cdma/). Na rozdíl od časově děleného přístupu GSM byl kódově multiplexovaný a kontinuální přenos DPDCH navržen tak, aby lépe zvládal proměnné datové rychlosti a využil statistické zisky multiplexu CDMA.

Řešil potřebu struktury vyhrazeného kanálu, která mohla koexistovat s nezbytnou řídicí signalizací. Oddělení dat (DPDCH) a řízení (DPCCH) na různé kódy (a IQ větve) umožnilo nezávislé řízení výkonu a robustní výkon řídicího kanálu, což je klíčové pro udržení spojení v prostředí s rychlým útlumem. Tento návrh představoval významný vývoj od jednodušších kanálových struktur.

Historický kontext představuje přechod z 2G na 3G s cílem dosáhnout skutečných širokopásmových mobilních služeb. DPDCH byl úhelným kamenem architektury UMTS Rel-99 a umožnil první 3G datové služby. Jeho schopnost flexibilní datové rychlosti řízená proměnnými rozprostíracími faktory byla klíčovou vlastností, která umožnila UMTS prezentovat se jako systém schopný podporovat jak služby s přepojováním okruhů (hlas), tak nově se objevující aplikace s přepojováním paketů (data) na jediném, jednotném rádiovém rozhraní.

## Klíčové vlastnosti

- Přenáší vyhrazená uživatelská data (z transportního kanálu DCH) v uplinku UMTS
- Využívá IQ/kódový multiplex s DPCCH pro kontinuální přenos
- Podporuje proměnné datové rychlosti prostřednictvím dynamického přizpůsobení rozprostíracího faktoru (SF)
- Umožňuje více paralelních DPDCH (přenos s více kódy) pro dosažení vyšších datových rychlostí
- Používá se jak v doméně služeb s přepojováním okruhů (CS), tak s přepojováním paketů (PS)
- Základní prvek fyzické vrstvy WCDMA, využívající kanalizační kódy pro oddělení uživatelů

## Související pojmy

- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.823** (Rel-8) — Synchronised E-DCH Study for UTRA FDD
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B
- **TR 26.902** (Rel-19) — Video Codec Performance for 3GPP Packet Services
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [DPDCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpdch/)
