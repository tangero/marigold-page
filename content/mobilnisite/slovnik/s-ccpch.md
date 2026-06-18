---
slug: "s-ccpch"
url: "/mobilnisite/slovnik/s-ccpch/"
type: "slovnik"
title: "S-CCPCH – Secondary Common Control Physical Channel"
date: 2025-01-01
abbr: "S-CCPCH"
fullName: "Secondary Common Control Physical Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-ccpch/"
summary: "Fyzický kanál pro přenos směrem k uživateli (downlink) v UMTS (UTRA) používaný k přenosu společných řídicích informací a uživatelských dat. Primárně přenáší přenosové kanály FACH (Forward Access Chann"
---

S-CCPCH je fyzický kanál pro přenos směrem k uživateli (downlink) v UMTS, který přenáší přenosové kanály FACH a PCH za účelem vysílání systémových informací, stránkovacích zpráv a uživatelských dat, čímž umožňuje přístup k síti a signalizaci.

## Popis

Sekundární společný řídicí fyzický kanál (Secondary Common Control Physical Channel, S-CCPCH) je základní downlinkový kanál ve vzdušném rozhraní [WCDMA](/mobilnisite/slovnik/wcdma/) (Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)) systému UMTS podle standardu 3GPP. Funguje na fyzické vrstvě (Layer 1) a slouží jako přenašeč na fyzické vrstvě pro dva klíčové přenosové kanály: Kanál pro přístup v dopředném směru (Forward Access Channel, [FACH](/mobilnisite/slovnik/fach/)) a Stránkovací kanál (Paging Channel, [PCH](/mobilnisite/slovnik/pch-text-pch/)). Na rozdíl od primárního kanálu [CCPCH](/mobilnisite/slovnik/ccpch/), který přenáší pevnou sadu vysílaných informací ([BCH](/mobilnisite/slovnik/bch/)), je S-CCPCH flexibilnější. Jeho struktura je podobná dedikovanému fyzickému kanálu ([DPCH](/mobilnisite/slovnik/dpch/)), ale je určen pro společný přístup více uživatelů. Kanál je charakterizován svým rozprostíracím kódem, který je přiřazen ze stromu kódů společných kanálů, a svým časováním, které je posunuto vzhledem k primárnímu CCPCH.

Z technické perspektivy vysílá S-CCPCH kontinuální proud rádiových rámců. Každý 10ms rádiový rámec je rozdělen do 15 slotů. Kanál může být nakonfigurován s nebo bez příkazů řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)). Při přenosu FACHu se používá k vysílání řídicí signalizace a malého množství uživatelských dat k uživatelským zařízením (UE) ve stavu CELL_FACH (stav bez dedikovaného spojení). To zahrnuje zprávy o nastavení RRC spojení, potvrzení o aktualizaci buňky a přímý přenos dat pro služby s nízkou aktivitou. Při přenosu PCH slouží k vysílání stránkovacích zpráv pro upozornění uživatelských zařízení na příchozí hovory nebo relace. Síť může v jedné buňce nakonfigurovat více S-CCPCH kanálů, každý s různou datovou rychlostí a rozprostíracím faktorem, aby zvládl proměnlivou zátěž z provozu společných kanálů.

Činnost S-CCPCH je úzce propojena se stavovým automatem uživatelského zařízení (UE). Uživatelské zařízení v režimu nečinnosti (UTRA_IDLE) sleduje přes S-CCPCH kanál PCH kvůli stránkovacím indikacím. Při zahájení spojení může uživatelské zařízení přijímat počáteční signalizaci na FACHu přenášeném S-CCPCH, než je převedeno na dedikovaný kanál. Kanál používá modulaci QPSK. Jeho datová rychlost je proměnná a je určena rozprostíracím faktorem (v rozsahu od 4 do 256) a použitím přizpůsobení rychlosti (rate matching) a kanálového kódování (konvoluční nebo Turbo kódování). S-CCPCH je klíčovou součástí pro efektivitu sítě, protože umožňuje systému obsloužit mnoho uživatelů s potřebou občasné signalizace bez přidělení dedikovaných kanálových prostředků, čímž šetří cenné kódové a výkonové prostředky na downlinku.

## K čemu slouží

S-CCPCH byl vytvořen, aby poskytl flexibilní a efektivní mechanismus pro přenos společných řídicích signalizačních zpráv a malých datových paketů více uživatelům v síti UMTS. Řeší omezení spočívající v existenci pouze jediného primárního CCPCH s pevným formátem pro vysílání informací. Síť potřebovala kanál, který by mohl přenášet řídicí zprávy s proměnnou rychlostí, specifické pro uživatele (jako je signalizace RRC pro správu spojení), a vysílat stránkovací zprávy bez nutnosti vytvářet pro každé uživatelské zařízení dedikované spojení, což by bylo značně neefektivní z hlediska využití prostředků. S-CCPCH tento problém řeší tím, že nabízí pro tyto účely sdílený prostředek.

Historicky v GSM podobné funkce zajišťovaly samostatné logické kanály mapované na fyzické časové sloty. Koncepce WCDMA v UMTS zavedla kódový multiplex (code-division multiplexing), což vyžadovalo novou strukturu fyzických kanálů. S-CCPCH společně s P-CCPCH tvořil páteř rámce společných kanálů. Jeho zavedení ve verzi Release 4 bylo součástí základní architektury UMTS. Umožnil efektivní podporu paketových datových služeb v režimu „stále zapnuto“ tím, že umožnil uživatelským zařízením zůstávat ve stavu nízké aktivity (CELL_FACH), přičemž mohla stále vysílat a přijímat malé dávky dat přes FACH bez režie spojené s přechodem na dedikovaný kanál. To bylo zvláště důležité pro rané „always-on“ aplikace a pro správu signalizačního provozu pro velkou populaci neaktivních uživatelů prostřednictvím PCH, což zajišťovalo spolehlivé stránkování a aktualizace systémových informací.

## Klíčové vlastnosti

- Přenáší přenosový kanál FACH (Forward Access Channel) pro signalizaci a data.
- Přenáší přenosový kanál PCH (Paging Channel) pro kontakt iniciovaný sítí.
- Používá modulaci QPSK s proměnnými rozprostíracími faktory (4 až 256).
- Podporuje jak konvoluční, tak Turbo kanálové kódování pro různé typy dat.
- Může být nakonfigurován s nebo bez bitů pro řízení vysílacího výkonu (TPC).
- Umožňuje více instancí na buňku pro zvládnutí zatížení provozem.

## Související pojmy

- [P-CCPCH – Primary Common Control Physical Channel](/mobilnisite/slovnik/p-ccpch/)
- [FACH – Forward Access Channel](/mobilnisite/slovnik/fach/)
- [PCH – Paging Channel](/mobilnisite/slovnik/pch/)
- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)
- [UTRA – Universal Terrestrial Radio Access](/mobilnisite/slovnik/utra/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B
- **TR 25.929** (Rel-19) — Continuous Connectivity for Packet Data Users

---

📖 **Anglický originál a plná specifikace:** [S-CCPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-ccpch/)
