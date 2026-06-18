---
slug: "s-cpich"
url: "/mobilnisite/slovnik/s-cpich/"
type: "slovnik"
title: "S-CPICH – Secondary Common Pilot Channel"
date: 2025-01-01
abbr: "S-CPICH"
fullName: "Secondary Common Pilot Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-cpich/"
summary: "S-CPICH je downlinkový fyzický kanál v UMTS (WCDMA) používaný k přenosu známé pilotní sekvence. Poskytuje dodatečnou fázovou referenci pro demodulaci, což umožňuje pokročilé funkce jako beamforming a"
---

S-CPICH je downlinkový fyzický kanál v UMTS, který vysílá známou pilotní sekvenci a poskytuje dodatečnou fázovou referenci pro demodulaci, což umožňuje funkce jako beamforming a transmisní diverzita.

## Popis

Sekundární společný pilotní kanál (Secondary Common Pilot Channel, S-CPICH) je downlinkový fyzický kanál v radiovém rozhraní UMTS/[WCDMA](/mobilnisite/slovnik/wcdma/). Podobně jako primární [CPICH](/mobilnisite/slovnik/cpich/) ([P-CPICH](/mobilnisite/slovnik/p-cpich/)) nepřetržitě vysílá předdefinovanou bitovou sekvenci (pilot), která je scramblována primárním scramblovacím kódem buňky nebo sekundárním scramblovacím kódem. Jeho hlavní funkcí je poskytovat koherentní fázovou referenci pro uživatelské zařízení (UE) k demodulaci jiných downlinkových fyzických kanálů. Na rozdíl od P-CPICH, který je vysílán v celé buňce a je povinný, je však S-CPICH volitelný kanál, který může být vysílán s jiným kanalizačním kódem a může pokrývat pouze část buňky, například konkrétní sektor nebo beam.

Z technického hlediska je S-CPICH charakterizován svým kanalizačním kódem a volitelně svým scramblovacím kódem. Vždy je vysílán s pevným rozprostíracím faktorem ([SF](/mobilnisite/slovnik/sf/)) 256. Buňka může mít nula, jeden nebo více S-CPICH. Každý S-CPICH může být asociován s jiným anténním beamem nebo specifickým přenosovým schématem. Například S-CPICH může být použit jako fázová reference pro skupinu sekundárních společných řídících fyzických kanálů ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)) přenášejících transportní kanály jako [FACH](/mobilnisite/slovnik/fach/) a [PCH](/mobilnisite/slovnik/pch-text-pch/), nebo pro downlinkový vyhrazený fyzický kanál ([DPCH](/mobilnisite/slovnik/dpch/)) přiřazený konkrétním UE. To umožňuje síti nasměrovat beamy nebo aplikovat techniky transmisní diverzity (jako Space Time Transmit Diversity - STTD) pro specifické oblasti nebo uživatele, přičemž S-CPICH slouží jako dedikovaný pilot pro tyto přenosy.

UE používá měření ze S-CPICH, konkrétně Received Signal Code Power (RSCP) a Ec/No, pro rozhodování o výběru buňky, převýběru a handoveru, podobně jako u P-CPICH. Síť může prostřednictvím signalizace vyšší vrstvy (RRC zprávy) informovat UE o tom, který S-CPICH má monitorovat a používat jako referenci. Tato flexibilita je klíčová pro pokročilé anténní systémy a optimalizaci sítě, umožňující operátorům zlepšit pokrytí a kapacitu v cílových zónách bez ovlivnění společného pilotního kanálu celé buňky.

## K čemu slouží

S-CPICH byl zaveden v Release 5 UMTS pro podporu nasazení pokročilých anténních technologií a zvýšení flexibility kapacity a pokrytí sítě. Primární CPICH (P-CPICH) je zdroj pro celou buňku, který poskytuje základní fázovou referenci pro všechna UE. Tento jediný, všudypřítomný pilot se však stává omezením při implementaci funkcí jako adaptivní anténní systémy (beamforming) nebo při potřebě přiřadit různé fázové reference různým logickým sektorům nebo skupinám uživatelů ve stejné buňce.

Před zavedením S-CPICH byly všechny downlinkové kanály demodulovány pomocí fázové reference z P-CPICH. To znamenalo, že jakýkoli beamforming nebo cílený přenos musel být zarovnán se společným pilotem buňky, což omezovalo optimalizaci. S-CPICH to vyřešil poskytnutím dodatečných, dedikovaných pilotních zdrojů. To umožnilo několik klíčových pokroků: umožnilo implementaci Site Selection Diversity Transmission (SSDT) v soft handoveru, podpořilo použití sekundárních scramblovacích kódů k překonání omezení kanalizačních kódů v buňkách s vysokou kapacitou a stalo se zásadním pro pozdější zavedení High-Speed Downlink Packet Access (HSDPA), kde mohl být použit jako fázová reference pro HS-PDSCH. S-CPICH v podstatě poskytl potřebnou granularitu v pilotní signalizaci k odemčení sofistikovanějších technik fyzické vrstvy a posunul se tak za přístup „jedna velikost pro všechny“ u primárního pilotu.

## Klíčové vlastnosti

- Poskytuje dodatečnou, volitelnou fázovou referenci pro demodulaci downlinkových kanálů v UMTS
- Vysílán s pevným rozprostíracím faktorem 256
- Může být asociován se specifickým anténním beamem, sektorem nebo přenosovým schématem
- Použit jako reference pro kanály S-CCPCH, DPCH a HSDPA
- Umožňuje pokročilé funkce jako beamforming a transmisní diverzitu (STTD)
- Měření UE na S-CPICH (RSCP/Ec/No) napomáhají procedurám mobility

## Související pojmy

- [P-CPICH – Primary Common Pilot Channel](/mobilnisite/slovnik/p-cpich/)
- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS

---

📖 **Anglický originál a plná specifikace:** [S-CPICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-cpich/)
