---
slug: "egprs"
url: "/mobilnisite/slovnik/egprs/"
type: "slovnik"
title: "EGPRS – Enhanced GPRS"
date: 2025-01-01
abbr: "EGPRS"
fullName: "Enhanced GPRS"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/egprs/"
summary: "Vylepšení paketově orientované datové služby GPRS v sítích GSM/EDGE, známé také jako EDGE. Používá pokročilou modulaci (8PSK) a kódovací schémata k výraznému zvýšení datových rychlostí a spektrální úč"
---

EGPRS je vylepšení paketově orientované datové služby GPRS v sítích GSM/EDGE, které využívá pokročilé modulační a kódovací schémata k výraznému zvýšení datových rychlostí a spektrální účinnosti.

## Popis

Enhanced [GPRS](/mobilnisite/slovnik/gprs/) (EGPRS), běžně uváděné na trh jako [EDGE](/mobilnisite/slovnik/edge/) (Enhanced Data rates for GSM Evolution), je klíčová aktualizace GSM rádiové přístupové sítě, která dramaticky zlepšila její paketově orientované datové schopnosti. Je definována jako evoluce standardu GPRS (General Packet Radio Service), která zavádí nové modulační techniky a flexibilnější mechanismy adaptace spojení do existující struktury [TDMA](/mobilnisite/slovnik/tdma/) (Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)) rámců GSM.

V jádru si EGPRS zachovává šířku pásma nosné 200 kHz a strukturu TDMA rámců GSM, ale nahrazuje modulaci Gaussian Minimum Shift Keying ([GMSK](/mobilnisite/slovnik/gmsk/)) používanou GPRS spektrálně účinnější modulací 8-Phase Shift Keying (8PSK). To umožňuje přenášet 3 bity na symbol místo 1, čímž se ztrojnásobí hrubá rychlost symbolů. V kombinaci s tím EGPRS zavedlo devět modulačních a kódovacích schémat (MCS-1 až MCS-9), která kombinují modulaci GMSK a 8PSK s různými úrovněmi kódování pro dopřednou opravu chyb. Síť a mobilní stanice dynamicky vybírají optimální [MCS](/mobilnisite/slovnik/mcs/) na základě aktuálních podmínek rádiového kanálu (proces zvaný adaptace spojení), přepínají mezi GMSK a 8PSK a upravují kódovací poměr pro maximalizaci propustnosti nebo spolehlivosti.

Z architektonického hlediska se EGPRS bezproblémově integruje do existující sítě GSM/GPRS. Vyžaduje aktualizace na [BTS](/mobilnisite/slovnik/bts/) (Base Transceiver Station) a [BSC](/mobilnisite/slovnik/bsc/) (Base Station Controller) pro podporu nové modulace a složitějšího zpracování signálu, stejně jako nový hardwarový terminál. Jádrová síť (SGSN, GGSN) zůstává z velké části nezměněna a zachází s EGPRS jako s přístupovým přenašečem vyšší rychlosti. Mezi klíčové provozní vlastnosti patří přírůstková redundance (také nazývaná Hybrid ARQ Type II), kde původně odeslané datové pakety obsahují data s vysokým kódovacím poměrem, a pokud dekódování selže, jsou v následných přenosech odeslány dodatečné paritní bity a kombinovány s originálem pro robustnější dekódování, což zlepšuje účinnost při špatném spojení.

## K čemu slouží

EGPRS bylo vyvinuto, aby řešilo závažná omezení šířky pásma původní technologie GPRS, která nabízela teoretické maximální datové rychlosti pouze kolem 115 kbps, ale v praxi často dosahovala mnohem nižších rychlostí. S růstem využívání internetu na počátku 21. století prudce vzrostla poptávka po rychlejších mobilních datech na všudypřítomné infrastruktuře sítí GSM. Nasazení zcela nových sítí 3G UMTS bylo nákladné a časově náročné, což vytvořilo naléhavou potřebu významné evoluční aktualizace existujícího spektra a hardwaru GSM.

EGPRS to vyřešilo poskytnutím 'přidavného' vylepšení, které mohlo ztrojnásobit datovou propustnost ve stejném 200 kHz rádiovém kanálu, čímž efektivně zvýšilo spektrální účinnost. Vyřešilo omezení pevných kódovacích schémat a jediného typu modulace GPRS zavedením adaptivní modulace a kódování, což umožnilo systému prosperovat jak v excelentních, tak v špatných rádiových podmínkách. Toto efektivně využilo vzácný spektrální zdroj a prodloužilo komerční životnost sítí GSM tím, že jim umožnilo nabízet konkurenceschopné datové služby '2.75G', jako je mobilní e-mail a základní prohlížení webu, roky předtím, než se rozšířilo pokrytí 3G.

Jeho zavedení, počínaje 3GPP Release 99, poskytlo operátorům jasnou a nákladově efektivní migrační cestu. Umožnilo jim nabízet vylepšené datové služby při ochraně jejich stávajících investic do infrastruktury, překlenulo mezeru mezi základním GPRS a vysokorychlostním paketovým přístupem UMTS/HSPA a uspokojilo rostoucí spotřebitelskou poptávku po mobilním přístupu k internetu.

## Klíčové vlastnosti

- Zavádí modulaci 8PSK vedle GMSK, čímž ztrojnásobuje přenosovou rychlost na symbol
- Definuje devět modulačních a kódovacích schémat (MCS-1 až MCS-9) pro flexibilní datové rychlosti
- Používá dynamickou adaptaci spojení pro výběr optimálního MCS na základě rádiových podmínek
- Využívá přírůstkovou redundanci (Hybrid ARQ Type II) pro zlepšenou účinnost přenosu
- Zachovává zpětnou kompatibilitu se sítěmi a kmitočtovým plánováním GSM/GPRS
- Teoretické špičkové datové rychlosti až 473,6 kbps na časový slot (s 8PSK, bez kódování)

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [EGPRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/egprs/)
