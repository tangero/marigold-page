---
slug: "geran"
url: "/mobilnisite/slovnik/geran/"
type: "slovnik"
title: "GERAN – GSM EDGE Radio Access Network"
date: 2025-01-01
abbr: "GERAN"
fullName: "GSM EDGE Radio Access Network"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/geran/"
summary: "Rádiová přístupová síť 2. generace zahrnující subsystémy základnových stanic (BSS), které podporují technologie GSM a EDGE. Poskytuje služby přepojování okruhů pro hlas a přepojování paketů pro data ("
---

GERAN je rádiová přístupová síť 2. generace zahrnující subsystémy základnových stanic (BSS), které podporují technologie GSM a EDGE a poskytují služby přepojování okruhů pro hlas a přepojování paketů pro data.

## Popis

GSM [EDGE](/mobilnisite/slovnik/edge/) Radio Access Network (GERAN) je souhrnný termín pro infrastrukturu rádiové sítě, která implementuje rádiové technologie GSM, [GPRS](/mobilnisite/slovnik/gprs/) a EDGE, jak je definuje 3GPP. Architektonicky se GERAN skládá z subsystémů základnových stanic ([BSS](/mobilnisite/slovnik/bss/)). Každý BSS se skládá ze dvou hlavních prvků: základnové stanice ([BTS](/mobilnisite/slovnik/bts/)), která obsahuje rádiové transceivery a antény pro jednu nebo více buněk, a řídicí jednotky základnové stanice ([BSC](/mobilnisite/slovnik/bsc/)), která spravuje rádiové zdroje, řeší předávání hovorů a řídí BTS. BSC vykonává klíčové funkce, jako je přidělování kmitočtů, řízení výkonu a správa kanálů pro přenos hovorů a signalizaci (např. SDCCH, TCH).

GERAN se připojuje k jádru sítě přes dvě klíčová rozhraní. Pro služby přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)), jako je hlas a SMS, používá rozhraní A pro propojení BSC s ústřednou mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)). Pro služby přepojování paketů (PS) pro data přes GPRS a EDGE používá rozhraní Gb pro připojení BSC (nebo vyčleněné jednotky řízení paketů – PCU) k podpůrnému uzlu SGSN. Rádiové rozhraní, známé jako rozhraní Um, používá kombinaci [FDMA](/mobilnisite/slovnik/fdma/) (dělení spektra na nosné o šířce 200 kHz) a TDMA (dělení každé nosné na 8 časových slotů). EDGE (Enhanced Data rates for GSM Evolution) zavedlo pokročilou modulaci (8-PSK vedle GMSK) a kódovací schémata, což výrazně zvýšilo datové rychlosti v rámci stejné TDMA struktury.

V prostředí s více RAT (Radio Access Technology) se role GERAN vyvinula z původně jediné RAN na spolupráci se sítěmi UMTS (UTRAN) a LTE (E-UTRAN). Specifikace definují mechanismy pro předávání hovorů a převýběr buněk mezi GERAN a těmito novějšími sítěmi, což umožňuje kontinuitu služeb. BSC spravuje jak CS, tak PS zdroje a se zavedením EDGE také řídí adaptivní modulaci a kódování, které definují vyšší propustnost EDGE. Specifikace GERAN pokrývají vše od fyzické vrstvy (modulace, struktury burstů) ve specifikacích řady 45, přes protokoly vrstvy 2 a 3 (např. RLC/MAC, BSSGP přes Gb) v řadách 44 a 48, až po požadavky na výkon v řadě 51.

## K čemu slouží

GERAN byl formálně definován jako termín zahrnující vyvinutou rádiovou přístupovou síť 2. generace, která zahrnovala jak původní standard GSM, tak jeho vylepšení pro paketová data, GPRS a EDGE. Jeho vytvoření vyřešilo problém poskytnutí jasné architektonické definice pro rádiovou síť, která pod jednou střechou podporovala jak služby přepojování okruhů zaměřené na hlas, tak vznikající služby přepojování paketů pro internet. Před tímto sjednocením se specifikace často zvlášť zmiňovaly o aspektech GSM a GPRS.

Historickým motivem byla potřeba vyvinout úspěšnou síť GSM tak, aby efektivně zvládala data, což vedlo nejprve k GPRS (paketová nadstavba) a poté k EDGE (rádiové vylepšení). GERAN představuje vyvrcholení tohoto vývoje, které maximalizuje využití nasazené infrastruktury TDMA s nosnými o šířce 200 kHz. Vyřešil omezení pomalých dat přepojováním okruhů (CSD) zavedením trvalého paketového připojení (GPRS) a následným výrazným zvýšením jeho rychlosti (EDGE), což umožnilo rané zkušenosti s mobilním internetem. S nástupem 3G (UMTS) umožnila definice GERAN jasnější specifikace toho, jak bude tato starší síť spolupracovat a koexistovat s novou sítí UTRAN založenou na WCDMA, což zajistilo plynulý přechod a globální roaming napříč více generacemi technologií.

## Klíčové vlastnosti

- Založeno na mnohonásobném přístupu FDMA (nosné 200 kHz) a TDMA (8 časových slotů na nosnou)
- Podporuje hlas přepojováním okruhů (GSM) a data přepojováním paketů (GPRS, EDGE)
- Architektonickými komponentami jsou základnová stanice (BTS) a řídicí jednotka základnové stanice (BSC)
- Připojuje se k jádru sítě přes rozhraní A (k MSC) pro CS a přes rozhraní Gb (k SGSN) pro PS
- Vylepšení EDGE využívá modulaci 8-PSK pro vyšší datové rychlosti v rámci stávajících časových slotů
- Definované postupy spoluprace se sítěmi UTRAN a E-UTRAN pro mobilitu a kontinuitu služeb

## Související pojmy

- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.034** (Rel-19) — HSCSD Stage 2 Service Description
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- … a dalších 80 specifikací

---

📖 **Anglický originál a plná specifikace:** [GERAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/geran/)
