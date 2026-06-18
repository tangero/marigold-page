---
slug: "ecgi"
url: "/mobilnisite/slovnik/ecgi/"
type: "slovnik"
title: "ECGI – E-UTRAN Cell Global Identification"
date: 2026-01-01
abbr: "ECGI"
fullName: "E-UTRAN Cell Global Identification"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ecgi/"
summary: "ECGI je globálně jednoznačný identifikátor buňky LTE, který se skládá z PLMN ID a Cell Identity. Je nezbytný pro správu sítě, mobilní procedury a služby založené na poloze, protože umožňuje přesnou id"
---

ECGI je globálně jednoznačný identifikátor buňky LTE, vytvořený spojením PLMN ID a Cell Identity.

## Popis

[E-UTRAN](/mobilnisite/slovnik/e-utran/) Cell Global Identification (ECGI) je klíčový identifikátor v architekturách LTE (E-UTRAN) a 5G NR (NG-RAN), definovaný pro jednoznačné určení konkrétní buňky v globálním měřítku. Jeho struktura je standardizována, aby zajišťovala jednoznačnost napříč sítěmi různých operátorů. ECGI se skládá ze dvou hlavních částí: Public Land Mobile Network Identity ([PLMN](/mobilnisite/slovnik/plmn/) ID) a E-UTRAN Cell Identity ([ECI](/mobilnisite/slovnik/eci/)). PLMN ID, které samo o sobě obsahuje Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)) a Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)), identifikuje síť operátora. ECI je 28bitová hodnota pevné délky přiřazená operátorem k jednoznačné identifikaci buňky v rámci daného PLMN. Tento konkatenovaný formát zaručuje globální jednoznačnost, protože rozsah PLMN ID je spravován mezinárodně a prostor ECI spravuje operátor interně.

Z architektonického hlediska je ECGI základním datovým prvkem používaným napříč četnými síťovými rozhraními a protokoly. Je přenášen v signalizaci [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control) mezi UE a [eNB](/mobilnisite/slovnik/enb/)/gNB a v signalizaci S1-AP a X2-AP mezi síťovými uzly. Například během procedur předávání spojení zdrojová buňka zahrnuje ECGI cílové buňky do zprávy žádosti o předání, aby jednoznačně identifikovala cíl. V jádru sítě je ECGI používáno ve zprávách rozhraní [S1-MME](/mobilnisite/slovnik/s1-mme/) a je hlášeno Mobility Management Entity (MME) a následně Home Subscriber Server (HSS) nebo Unified Data Management (UDM) pro sledování polohy a účely zákonného odposlechu.

Jeho role přesahuje základní mobilitu. ECGI je nedílnou součástí funkcí Self-Organizing Network (SON), jako je správa Automatic Neighbor Relation (ANR), kde eNB/gNB objevuje sousední buňky a jejich ECGI. Je také klíčovým parametrem pro Minimization of Drive Tests (MDT), kde jsou měření UE označena ECGI obsluhující a sousedních buněk pro optimalizaci sítě. V 5G tento koncept přetrvává jako NR Cell Global Identifier (NCGI), který má podobnou strukturu, ale pro NR buňky, což ukazuje na zásadní význam globálně jednoznačné identifikace buněk v celulárních sítích. ECGI není jen adresa; je to základní kámen pro automatizaci, optimalizaci sítě a poskytování služeb.

## K čemu slouží

ECGI bylo vytvořeno k řešení základní potřeby jednoznačné identifikace buněk v globálním ekosystému LTE. Předchozí celulární systémy, jako GSM a UMTS, měly identifikátory buněk (např. Cell Global Identity (CGI) v GSM), ale přechod na plně IP, plošší architekturu LTE (E-UTRAN) vyžadoval nový, robustní identifikátor, který by se mohl plynule integrovat s paketově orientovanými jádry sítí a podporovat pokročilé funkce, jako jsou předávání spojení založená na X2 a SON. Primární problém, který řeší, je spolehlivé a jednoznačné odkazování na konkrétní radiovou buňku napříč všemi síťovými operacemi, od jednoduchého radiového připojení po komplexní koordinaci mezi uzly a sledování účastníků v jádru sítě.

Bez globálně jednoznačného identifikátoru buňky by byly kritické funkce, jako je předávání spojení, náchylné k chybám, systémy správy sítě by měly potíže s korelací dat a služby založené na poloze by byly nepřesné. Konstrukce ECGI, která zahrnuje PLMN ID operátora, zajišťuje, že i když dva operátoři nezávisle přiřadí stejnou číselnou hodnotu ECI, zůstává celé ECGI globálně odlišné. To bylo motivováno zejména potřebou automatizovaného provozu a optimalizace sítě v LTE, kde se buňky musí samy konfigurovat a spravovat sousední vztahy bez manuálního zásahu. ECGI poskytuje nezbytnou „adresu“, která tuto automatizaci umožňuje, a vytváří tak spolehlivý klíč pro všechny databáze a procesy, které spravují radiový přístupový síť.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor pro buňky LTE/NR
- Konkatenovaná struktura z PLMN ID a 28bitového Cell Identity
- Povinný prvek v signalizaci RRC, S1-AP a X2-AP/N2-AP
- Základní prvek pro předávání spojení, sledování polohy a funkce SON
- Používá se pro MDT (Minimization of Drive Tests) a optimalizaci sítě
- Umožňuje přesné účtování na úrovni buňky a zákonný odposlech

## Související pojmy

- [PCI – Physical Cell Identity](/mobilnisite/slovnik/pci/)
- [TAC – Time Alignment Command](/mobilnisite/slovnik/tac/)
- [NCI – Native Code Identifier](/mobilnisite/slovnik/nci/)
- [CGI – Cell Global Identifier](/mobilnisite/slovnik/cgi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [ECGI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecgi/)
