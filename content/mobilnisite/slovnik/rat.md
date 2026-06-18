---
slug: "rat"
url: "/mobilnisite/slovnik/rat/"
type: "slovnik"
title: "RAT – Radio Access Technology"
date: 2026-01-01
abbr: "RAT"
fullName: "Radio Access Technology"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rat/"
summary: "Základní metoda fyzického připojení a síťová architektura pro bezdrátovou komunikaci. Definuje standardy rádiového rozhraní, jako jsou GSM, UMTS, LTE a NR. RAT je základním stavebním kamenem mobilních"
---

RAT je základní metoda fyzického připojení a síťová architektura, jako je GSM, UMTS, LTE nebo NR, která definuje standardy rádiového rozhraní pro bezdrátovou komunikaci v mobilních sítích.

## Popis

Technologie rádiového přístupu (RAT) je kompletní soubor technických specifikací a implementací, které definují rozhraní vzduchu a přidružené síťové funkce pro bezdrátovou komunikaci mezi uživatelským zařízením (UE) a jádrem sítě. Zahrnuje fyzickou vrstvu (modulace, kódování, duplexování), vrstvu spojení dat (řízení přístupu k médiu, řízení rádiového spoje) a klíčové procedury správy rádiových prostředků. Každá RAT, jako GSM (2G), UMTS (3G), LTE (4G) a NR (5G), má odlišnou architekturu: GSM používá [TDMA](/mobilnisite/slovnik/tdma/)/[FDMA](/mobilnisite/slovnik/fdma/) s podsystémy základnových stanic; UMTS využívá [W-CDMA](/mobilnisite/slovnik/w-cdma/) s NodeB a [RNC](/mobilnisite/slovnik/rnc/); LTE využívá [OFDMA](/mobilnisite/slovnik/ofdma/)/[SC-FDMA](/mobilnisite/slovnik/sc-fdma/) se zjednodušeným eNodeB; NR používá flexibilní OFDMA s gNB. RAT definuje konkrétní protokoly pro náhodný přístup, zřizování kanálů, předávání spojení, řízení výkonu a plánování. Funguje tak, že převádí digitální data na rádiové vlny vysílané v určitých kmitočtových pásmech, přičemž základnová stanice (eNodeB, gNB) spravuje rádiové prostředky pro více UE. Mezi klíčové komponenty patří rádiový transceiver UE, rádiová jednotka a základnový procesor základnové stanice a definované struktury kanálů (fyzické, transportní, logické). Jejím úkolem je poskytovat bezdrátový spoj, který přenáší uživatelská data a signalizaci, a tvořit tak nezbytný most mezi mobilními zařízeními a jádrem sítě. Moderní sítě jsou multi-RAT, přičemž UE a sítě jsou schopny pracovat napříč několika RAT (např. LTE a NR), což je řízeno mechanismy jako je mobilita mezi RAT a agregace nosných. RAT zásadně určuje klíčové ukazatele výkonu, jako je datový tok, latence, pokrytí a kapacita.

## K čemu slouží

RAT existují za účelem standardizace bezdrátové komunikace, což umožňuje globální interoperabilitu mezi zařízeními a sítěmi. Každá nová generace RAT je vytvářena, aby vyřešila omezení svých předchůdců, a je hnána rostoucími požadavky na vyšší datové toky, nižší latenci, větší kapacitu a nové typy služeb. GSM (2G) zavedlo digitální hlas a [SMS](/mobilnisite/slovnik/sms/), což znamenalo posun od analogových systémů. UMTS (3G) řešilo potřebu mobilního širokopásmového přenosu dat. LTE (4G) bylo vyvinuto, aby poskytovalo vysokorychlostní data plně v IP s jednodušší architekturou a překonalo tak složitost a neefektivitu vyhrazených kanálů UMTS. NR (5G) je navrženo pro extrémní šířku pásma, ultra-spolehlivou nízkou latenci a hromadný IoT, a řeší tak omezení LTE v latenci a flexibilitě pro různé případy užití. Vývoj RAT je motivován zlepšováním efektivity využití spektra, technologickým pokrokem (jako je [MIMO](/mobilnisite/slovnik/mimo/), pokročilé kódování) a měnícími se požadavky uživatelů. Multi-RAT provoz je klíčový pro plynulou kontinuitu služeb, umožňuje sítím využívat stávající infrastrukturu (např. pokrytí LTE) při zavádění nových technologií (NR). Standardizační orgány jako 3GPP tyto RAT definují, aby zajistily soudržný ekosystém, zabránily fragmentaci a umožnily úspory z rozsahu.

## Klíčové vlastnosti

- Definuje vlnový tvar fyzické vrstvy, modulaci (např. QPSK, 256QAM) a metodu mnohonásobného přístupu (např. OFDMA, CDMA)
- Specifikuje zásobník rádiových protokolů včetně vrstev MAC, RLC, PDCP a RRC
- Řídí procedury správy rádiových prostředků: plánování, předání spojení, řízení výkonu
- Určuje podporovaná kmitočtová pásma a metody duplexování (FDD, TDD)
- Umožňuje správu mobility v rámci stejné RAT (intra-RAT) a mezi různými RAT (inter-RAT)
- Poskytuje základ pro síťové funkce jako agregace nosných, duální konektivita a síťové segmentování

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [E-UTRAN – Evolved Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/e-utran/)

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- … a dalších 69 specifikací

---

📖 **Anglický originál a plná specifikace:** [RAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/rat/)
