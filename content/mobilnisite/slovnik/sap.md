---
slug: "sap"
url: "/mobilnisite/slovnik/sap/"
type: "slovnik"
title: "SAP – Service Access Point"
date: 2025-01-01
abbr: "SAP"
fullName: "Service Access Point"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sap/"
summary: "Konceptuální bod v rámci protokolové vrstvy, kde jsou poskytovány služby vrstvě nadřazené. Definuje rozhraní a primitiva (např. request, indication, response, confirm) pro komunikaci mezi sousedními v"
---

SAP je konceptuální bod v rámci protokolové vrstvy, kde jsou poskytovány služby vrstvě nadřazené, a který definuje rozhraní a primitiva pro komunikaci mezi sousedními vrstvami.

## Popis

Service Access Point (SAP) je základní architektonický koncept ve vrstvených komunikačních systémech, včetně 3GPP protokolových zásobníků pro UE, RAN a Core Network. Představuje logické rozhraní na hranici mezi dvěma sousedními protokolovými vrstvami (např. mezi vrstvami [RLC](/mobilnisite/slovnik/rlc/) a [MAC](/mobilnisite/slovnik/mac/), nebo mezi vrstvami [NAS](/mobilnisite/slovnik/nas/) a [RRC](/mobilnisite/slovnik/rrc/)). SAP není fyzické spojení, ale definovaná sada abstraktních komunikačních primitiv a přidružených datových struktur, prostřednictvím kterých nižší vrstva (poskytovatel služby) nabízí své služby bezprostředně vyšší vrstvě (uživatel služby).

Fungování SAP je definováno výměnou služebních primitiv. Ta jsou typicky kategorizována jako Request, Indication, Response a Confirm. Například, když vrstva RRC (uživatel) potřebuje odeslat zprávu, vydá prostřednictvím jejich SAP primitivum DATA.request směrem k nižší vrstvě RLC (poskytovatel) a předá zprávu jako parametr. Vrstva RLC následně zpracuje přenos. Po přijetí dat od protistrany vrstva RLC vydá prostřednictvím stejného SAP primitivum DATA.indication směrem nahoru k vrstvě RRC. Tato abstrakce skrývá implementační detaily nižší vrstvy, což umožňuje vyšším vrstvám fungovat výhradně na základě nabízené služby.

Klíčovými komponentami konceptu SAP jsou samotná Služební primitiva a Service Data Unit ([SDU](/mobilnisite/slovnik/sdu/)). SDU je paket dat předávaný dolů přes SAP. Nižší vrstva může k tomuto SDU přidat vlastní hlavičky a zápatí, čímž jej přemění na Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)) pro svou vlastní komunikaci mezi protějšky. SAP jsou definována pro každé mezivrstvové rozhraní v 3GPP specifikacích, například Service Access Point Identifier ([SAPI](/mobilnisite/slovnik/sapi/)) pro linkovou vrstvu LAPDm v GSM, nebo logické kanály mezi MAC a RLC v LTE/NR. Jejich úlohou je vytvořit čisté, standardizované a interoperabilní oddělení funkcí, což je zásadní pro modulární návrh sítě, nezávislý vývoj vrstev a kompatibilitu zařízení od různých výrobců.

## K čemu slouží

Koncept SAP existuje proto, aby umožnil strukturovaný, vrstvený návrh zásobníků komunikačních protokolů, což je základním kamenem moderní telekomunikace a počítačových sítí (inspirováno [OSI](/mobilnisite/slovnik/osi/) modelem). Před vrstvenými architekturami byl protokolový software často monolitický a těsně integrovaný, což ztěžovalo úpravy, upgrade nebo výměnu jednotlivých funkčních komponent bez dopadu na celý systém.

SAP řeší kritický problém definice toho, jak spolu různé vrstvy komplexního systému, potenciálně vyvinuté různými týmy nebo výrobci, interagují předvídatelným a standardizovaným způsobem. Poskytuje formální kontrakt mezi vrstvami. To umožňuje nezávislý vývoj vrstev; například technologie fyzické vrstvy se může vyvíjet od GSM přes UMTS a LTE až po 5G NR, zatímco signalizační protokoly core network nad transportními vrstvami mohou zůstat v zásadě konzistentní nebo se vyvíjet samostatně.

Historicky bylo jeho přijetí ve standardech 3GPP (od GSM R99 dále) motivováno potřebou rigorózní specifikace pro zajištění globální interoperability. Řešilo omezení ad-hoc komunikace mezi vrstvami tím, že poskytlo přesný jazyk primitiv a parametrů. Tato formalizace snížila nejednoznačnost implementace, umožnila testování shody a v konečném důsledku umožnila úspěšné nasazení mobilních sítí s více výrobci, kde musí UE od jednoho výrobce bezproblémově fungovat s infrastrukturou od jiného.

## Klíčové vlastnosti

- Definuje abstraktní rozhraní a hranici služeb mezi dvěma sousedními protokolovými vrstvami.
- Funguje prostřednictvím výměny standardizovaných služebních primitiv (Request, Indication, Response, Confirm).
- Umožňuje předávání Service Data Units (SDU) z vyšší vrstvy do nižší vrstvy ke zpracování.
- Poskytuje nezávislost na implementaci, skrývá mechanismy nižší vrstvy před vrstvami vyššími.
- Základní prvek vrstvené architektury všech 3GPP protokolových zásobníků pro rádiovou síť i core network.
- Zásadní pro zajištění interoperability mezi síťovými prvky a uživatelskými zařízeními od různých výrobců.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- … a dalších 37 specifikací

---

📖 **Anglický originál a plná specifikace:** [SAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sap/)
