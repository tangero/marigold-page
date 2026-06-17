---
slug: "ne-dc"
url: "/mobilnisite/slovnik/ne-dc/"
type: "slovnik"
title: "NE-DC – NR E-UTRA Dual Connectivity"
date: 2026-01-01
abbr: "NE-DC"
fullName: "NR E-UTRA Dual Connectivity"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ne-dc/"
summary: "Režim duální konektivity, ve kterém Hlavní skupina buněk (MCG) používá 5G NR a Sekundární skupina buněk (SCG) používá 4G E-UTRA. Umožňuje zařízení současně se připojit k primárnímu uzlu 5G NR a sekund"
---

NE-DC je režim duální konektivity, ve kterém je hlavní spojení zařízení zajištěno 5G NR a sekundární spojení používá 4G E-UTRA, což zvyšuje datové přenosy pro nenaplno samostatné (non-standalone) 5G.

## Popis

NR [E-UTRA](/mobilnisite/slovnik/e-utra/) Dual Connectivity (NE-DC) je specifická architektura duální konektivity ([DC](/mobilnisite/slovnik/dc/)) standardizovaná organizací 3GPP, definovaná v rámci [MR-DC](/mobilnisite/slovnik/mr-dc/) (Multi-RAT Dual Connectivity). V NE-DC je uživatelské zařízení (UE) nakonfigurováno dvěma odlišnými skupinami buněk: Hlavní skupinou buněk ([MCG](/mobilnisite/slovnik/mcg/)) a Sekundární skupinou buněk (SCG). MCG je zajišťována hlavním uzlem ([MN](/mobilnisite/slovnik/mn/)) využívajícím přístupovou technologii 5G New Radio (NR). SCG je zajišťována sekundárním uzlem (SN) využívajícím přístupovou technologii 4G Evolved Universal Terrestrial Radio Access (E-UTRA neboli LTE). Hlavní uzel ukončuje řídicí rovinu spojení k jádru sítě, kterým je v této architektuře 5G Core (5GC). MN je zodpovědný za počáteční přístup, navázání spojení a správu mobility. Sekundární uzel poskytuje dodatečné rádiové prostředky pro uživatelskou rovinu, čímž zvyšuje propustnost. UE udržuje jediné spojení řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) s hlavním uzlem (NR), zatímco sekundární uzel je řízen pomocí RRC zpráv přenášených přes hlavní uzel. Data uživatelské roviny mohou být rozdělována a agregována v různých bodech, například na vrstvě PDCP (Packet Data Convergence Protocol) v hlavním uzlu (pro MCG split bearer) nebo v sekundárním uzlu (pro SCG split bearer). To vyžaduje těsnou koordinaci mezi uzly přes rozhraní Xn (mezi gNB a [eNB](/mobilnisite/slovnik/enb/)) pro správu rádiových zdrojů, předávání spojení a správu nosičů. NE-DC je základním prvkem pro možnost nasazení nenaplno samostatného (NSA) 5G podle možnosti 3, kde je vrstva 5G NR ukotvena v 5GC, ale využívá stávající infrastrukturu LTE pro pokrytí a kapacitu.

## K čemu slouží

NE-DC bylo zavedeno pro usnadnění plynulého zavedení služeb 5G NR využitím rozsáhlé, existující sítě 4G LTE. Řeší problém s omezeným počátečním pokrytím 5G NR tím, že umožňuje zařízení používat spojení 5G NR jako hlavní kotvu pro řízení a vysokorychlostní data, a současně využívat robustní spojení LTE pro dodatečnou datovou kapacitu a udržení kontinuity služeb na okraji buňky. Tento přístup umožňuje mobilním operátorům rychlejší a nákladově efektivnější zavádění služeb 5G, protože mohou využít své LTE prostředky jako doplňkovou vrstvu. Historicky byl koncept duální konektivity poprvé představen v LTE-Advanced (LTE-A) s intra-LTE [DC](/mobilnisite/slovnik/dc/) (kde jsou obě skupiny buněk LTE). NE-DC rozšiřuje tento princip na více-RAT scénáře, konkrétně zaměřené na migrační cestu k 5G. Odstraňuje tak omezení čistého samostatného (standalone) nasazení 5G, které by od prvního dne vyžadovalo všudypřítomné pokrytí NR pro zaručení služby, tím, že poskytuje praktický mezistupeň zajišťující lepší uživatelský zážitek prostřednictvím agregovaných zdrojů NR a LTE.

## Klíčové vlastnosti

- Hlavní skupina buněk (MCG) využívá technologii 5G New Radio (NR)
- Sekundární skupina buněk (SCG) využívá technologii 4G E-UTRA (LTE)
- Řídicí rovina je ukotvena v jádru sítě 5G (5GC) přes hlavní uzel NR
- Agregace uživatelské roviny z rádiových zdrojů NR i LTE
- Využívá rozhraní Xn pro koordinaci mezi gNB (MN) a eNB (SN)
- Podporuje různé typy nosičů (MCG, SCG, split bearers) pro flexibilní směrování dat

## Související pojmy

- [MR-DC – Multi-Radio Dual Connectivity](/mobilnisite/slovnik/mr-dc/)
- [EN-DC – E-UTRA NR Dual Connectivity with MCG using E-UTRA and SCG using NR](/mobilnisite/slovnik/en-dc/)

## Definující specifikace

- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 28.657** (Rel-19) — E-UTRAN NRM IRP Requirements
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.473** (Rel-19) — W1 Application Protocol (W1AP) Specification
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 37.717** — 3GPP TR 37.717
- **TS 37.718** — 3GPP TR 37.718
- **TS 37.719** (Rel-19) — 3GPP TR 37.719: Dual Connectivity Band Combinations
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [NE-DC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ne-dc/)
