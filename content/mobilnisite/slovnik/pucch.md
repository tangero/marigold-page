---
slug: "pucch"
url: "/mobilnisite/slovnik/pucch/"
type: "slovnik"
title: "PUCCH – Physical Uplink Control Channel"
date: 2025-01-01
abbr: "PUCCH"
fullName: "Physical Uplink Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pucch/"
summary: "PUCCH je kritický fyzický kanál pro uplink v LTE a NR. Přenáší zásadní řídicí informace od UE k síti, včetně potvrzení HARQ ACK/NACK pro downlinková data, hlášení o stavu kanálu (CSI) a žádostí o napl"
---

PUCCH je fyzický kanál pro uplink v LTE a 5G NR, který přenáší zásadní řídicí informace od uživatelského zařízení (UE) k síti, včetně potvrzení HARQ, hlášení o stavu kanálu a žádostí o naplánování.

## Popis

Physical Uplink Control Channel (PUCCH) je základní kanál fyzické vrstvy v rádiových přístupových sítích LTE (od Release 8) i NR (5G). Je určen pro přenos řídicích informací pro uplink ([UCI](/mobilnisite/slovnik/uci/)) od uživatelského zařízení (UE) k gNB (v NR) nebo [eNB](/mobilnisite/slovnik/enb/) (v LTE). Na rozdíl od kanálu [PUSCH](/mobilnisite/slovnik/pusch/) (Physical Uplink Shared Channel), který přenáší uživatelská data, je PUCCH specificky navržen pro signalizaci, která je klíčová pro udržení rádiového spoje, podporu zpětnovazebních mechanismů a umožnění efektivního dynamického plánování.

V LTE zabírá PUCCH specifické bloky zdrojů na okrajích systémové šířky pásma, zatímco v NR je jeho umístění flexibilnější a konfigurovatelné v rámci části pásma. Používá specifické formáty (PUCCH formáty 0-4 v NR, formáty 1-5 v LTE) optimalizované pro různé velikosti přenášených dat a požadavky na spolehlivost. Tyto formáty využívají různé modulační schémata, od jednoduché klíčování zapnutí/vypnutí ([OOK](/mobilnisite/slovnik/ook/)) pro 1bitové [ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/) až po π/2-BPSK nebo [QPSK](/mobilnisite/slovnik/qpsk/) pro rozsáhlejší hlášení [CSI](/mobilnisite/slovnik/csi/). Kanálové kódování se liší podle formátu, přičemž některé používají blokové kódy a jiné pro ochranu proti chybám využívají Reed-Mullerovy nebo polární kódy (v NR).

Hlavními typy UCI přenášenými na PUCCH jsou: potvrzení hybridního automatického opakování (HARQ ACK/NACK) pro downlinkové transportní bloky, které je klíčové pro protokoly opakovaného přenosu; informace o stavu kanálu (CSI), včetně indikátoru kvality kanálu (CQI), indikátoru předkódovací matice (PMI) a indikátoru hodnosti (RI), které řídí downlinkové plánování a konfiguraci MIMO; a žádosti o naplánování (SR), které UE používá k oznámení, že má data k odeslání a potřebuje pro ně zdroje pro uplink. PUCCH je plánovaný kanál, ale jeho zdroje jsou polostaticky konfigurovány prostřednictvím signalizace RRC, s dynamickou indikací pro určité formáty. Jeho návrh představuje kompromis mezi režií řídicí signalizace, pokrytím, kapacitou a latencí, což vedlo k vytvoření více formátů přizpůsobených různým scénářům nasazení a schopnostem UE.

## K čemu slouží

PUCCH byl vytvořen, aby poskytoval spolehlivý a efektivní mechanismus pro přenos zásadní řídicí signalizace od UE k síti v systémech založených na OFDMA, jako jsou LTE a NR. Jeho zavedení s LTE Release 8 bylo motivováno potřebou kanálu odděleného od uživatelských dat pro přenos časově kritické zpětné vazby. Toto řeší několik klíčových problémů: umožňuje rychlou zpětnou vazbu HARQ ACK/NACK pro downlinkové pakety, která je zásadní pro dosažení vysoké propustnosti s nízkou latencí; poskytuje síti aktuální CSI pro provádění plánování závislého na stavu kanálu a adaptivní modulace a kódování, čímž maximalizuje spektrální účinnost; a dává UE prostředek k vyžádání zdrojů pro uplink bez nutnosti mít předem vyhrazené naplánované zdroje, což zlepšuje latenci uplinku pro sporadický provoz.

Před vyhrazenými řídicími kanály, jako je PUCCH, systémy používaly pro řídicí signalizaci integrovanější nebo méně efektivní metody. Vyhrazený návrh PUCCH umožňuje optimalizované přenosové charakteristiky (výkon, kódování) nezávislé na provozu uživatelských dat. Toto oddělení zajišťuje, že kritické informace pro údržbu spoje jsou přenášeny spolehlivě, i když UE nemá žádná uplinková data k odeslání na sdíleném kanálu. Je to základní kámen dynamického provozu řízeného zpětnou vazbou, který definuje moderní buněčné systémy, a umožňuje pokročilé funkce jako agregace nosných, massive MIMO a komunikaci s ultra spolehlivou nízkou latencí (URLLC) tím, že poskytuje potřebný řídicí spoj s nízkou latencí.

## Klíčové vlastnosti

- Přenáší řídicí informace pro uplink (UCI): HARQ ACK/NACK, CSI, žádosti o naplánování
- Více formátů optimalizovaných pro různé velikosti přenášených dat (1-2 bity až >10 bitů) a potřeby spolehlivosti
- Používá specifické, konfigurované bloky zdrojů na okrajích pásma (LTE) nebo flexibilně v rámci části pásma (NR)
- Využívá modulační schémata jako OOK, π/2-BPSK a QPSK vhodná pro řídicí signalizaci
- Podporuje simultánní přenos HARQ-ACK a CSI na stejném zdroji
- Umožňuje klíčové síťové funkce jako adaptaci spoje, konfiguraci MIMO a dynamické plánování

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [UCI – Uplink Control Information](/mobilnisite/slovnik/uci/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- … a dalších 24 specifikací

---

📖 **Anglický originál a plná specifikace:** [PUCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pucch/)
