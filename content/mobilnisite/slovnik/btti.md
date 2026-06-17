---
slug: "btti"
url: "/mobilnisite/slovnik/btti/"
type: "slovnik"
title: "BTTI – Basic Transmission Time Interval"
date: 2025-01-01
abbr: "BTTI"
fullName: "Basic Transmission Time Interval"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/btti/"
summary: "BTTI je základní časová jednotka pro přenos dat v GSM/EDGE rádiové přístupové síti (GERAN). Definuje minimální granularitu plánování pro rádiové bloky na kanálu pro přenos paketových dat (PDTCH), což"
---

BTTI je základní časová jednotka pro přenos dat v sítích GSM/EDGE, která definuje minimální granularitu plánování pro rádiové bloky, aby umožnila efektivní multiplexování a předvídatelné řízení zdrojů.

## Popis

Základní přenosový časový interval (BTTI) je klíčový časový koncept v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)), který konkrétně řídí přenos paketově přepínaných dat přes kanál pro přenos paketových dat (PDTCH). Představuje nejkratší časové období, po které lze přenést přenosový blok (jednotka dat pro fyzickou vrstvu). Prakticky jeden BTTI odpovídá době přenosu čtyř po sobě jdoucích normálních výbuchů na jedné časové štěrbině, což ve standardní rámcové struktuře GSM (sestávající z 4,615 ms TDMA rámců) činí 20 ms. Tento 20ms interval je atomickou jednotkou pro plánování rádiových bloků v službách [GPRS](/mobilnisite/slovnik/gprs/) a EDGE.

Na fyzické vrstvě implementace BTTI zahrnuje přesnou synchronizaci mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a subsystémem základnové stanice ([BSS](/mobilnisite/slovnik/bss/)). Každý BTTI zabírá jedno období rádiového bloku v rámci 52-vícenásobné rámcové struktury používané pro kanály paketových dat. Vrstva řízení rádiového spoje (RLC) segmentuje protokolové datové jednotky (PDU) vyšších vrstev na datové bloky RLC, které se vejdou do jednoho BTTI. Tyto bloky jsou pak zakódovány kanálovým kódováním (konvoluční kódování pro GPRS, s pokročilejšími schématy jako [MCS](/mobilnisite/slovnik/mcs/) pro EDGE) a namapovány na čtyři výbuchy BTTI. Vrstva řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) využívá hranice BTTI pro rozhodování o plánování, přiděluje rádiové zdroje více uživatelům prostřednictvím dočasných blokových toků (TBF) na sdílených časových štěrbinách.

Pevná doba trvání BTTI vytváří předvídatelný časový rámec pro několik klíčových síťových funkcí. Umožňuje efektivní multiplexování dat různých uživatelů na stejném fyzickém kanálu prostřednictvím časově děleného plánování. Konzistentní časování umožňuje spolehlivé operace hybridního [ARQ](/mobilnisite/slovnik/arq/) (HARQ) v sítích EDGE, kde mohou být retransmise plánovány v známých intervalech. Dále hranice BTTI definují, kdy mají být prováděna a hlášena měření kvality kanálu (jako RXQUAL), a synchronizují úpravy řízení výkonu. Toto standardizované časování je klíčové pro interoperabilitu mezi síťovými zařízeními od různých výrobců a pro konzistentní uživatelský zážitek napříč různými nasazeními GERAN.

## K čemu slouží

BTTI byl vytvořen, aby poskytl standardizovanou, efektivní časovou strukturu pro přenos paketových dat v sítích GSM, jak se vyvíjely pro podporu GPRS (General Packet Radio Service) a později EDGE (Enhanced Data rates for GSM Evolution). Před schopnostmi paketového přepínání bylo GSM primárně okruhově přepínané, s časováním optimalizovaným pro hlasové hovory pomocí odlišných kanálových struktur. Zavedení datových služeb vyžadovalo nový časový model, který by dokázal zvládnout přerušovaný, proměnlivý provoz při efektivním sdílení rádiových zdrojů mezi více uživateli.

Základní problém, který BTTI řeší, je vytvoření předvídatelných přenosových intervalů pro paketová data, které jsou v souladu s existující TDMA rámcovou strukturou GSM. Bez takového standardizovaného intervalu by bylo plánování datových přenosů chaotické a neefektivní. BTTI umožňuje statistické multiplexování uživatelů na sdílených kanálech definováním jasných hranic, kdy mohou být přenášena data různých uživatelů. Poskytuje také časový základ pro klíčové vlastnosti datových služeb, jako je adaptace spojení (přepínání mezi různými kódovacími schématy na základě stavu kanálu) a přírůstková redundance v EDGE.

Historicky BTTI představoval kompromis mezi přenosovou účinností a flexibilitou plánování. Kratší intervaly by umožnily jemnější granularitu plánování, ale zvýšily by režii z častějšího řídicího signalizování. Delší intervaly by snížily režii, ale snížily by odezvu pro interaktivní aplikace. 20ms BTTI bylo zvoleno jako optimální pro typické požadavky na latenci a podmínky kanálu služeb mobilních dat 2G/2.5G, vyvažující tyto protichůdné faktory při zachování zpětné kompatibility se základní rámcovou strukturou GSM.

## Klíčové vlastnosti

- Pevná doba trvání 20 ms v souladu se strukturou 52-vícenásobného rámce GSM
- Definuje minimální plánovací jednotku pro rádiové bloky PDTCH
- Umožňuje časové dělení více uživatelů na sdílených časových štěrbinách
- Poskytuje časový referenční bod pro operace vrstvy RLC/MAC a procesy HARQ
- Synchronizuje měření kvality kanálu a úpravy řízení výkonu
- Tvoří základ pro adaptaci spojení mezi různými kódovacími schématy (CS-1 až CS-4 v GPRS, MCS-1 až MCS-9 v EDGE)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 45.001** (Rel-19) — GSM Physical Layer Introduction
- **TS 45.002** (Rel-19) — GSM/EDGE Radio Physical Layer Specification
- **TS 45.003** (Rel-19) — Channel Coding and Multiplexing for GSM/EDGE
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [BTTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/btti/)
