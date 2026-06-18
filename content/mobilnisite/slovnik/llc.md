---
slug: "llc"
url: "/mobilnisite/slovnik/llc/"
type: "slovnik"
title: "LLC – SM Low Layer Source Specific Multicast (address)"
date: 2025-01-01
abbr: "LLC"
fullName: "SM Low Layer Source Specific Multicast (address)"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/llc/"
summary: "LLC je vrstva protokolu logického řízení spojení v sítích GPRS a UMTS, která poskytuje spolehlivý datový spoj mezi mobilní stanicí a uzlem SGSN. Zpracovává segmentaci, opětovné sestavování a opravu ch"
---

LLC je vrstva protokolu logického řízení spojení v sítích GPRS a UMTS, která zajišťuje spolehlivý přenos dat mezi mobilní stanicí a uzlem SGSN pomocí segmentace, opravy chyb a řízení toku.

## Popis

Vrstva Logical Link Control (LLC) je podvrstvou linkové vrstvy (vrstva 2) v protokolové architektuře [GPRS](/mobilnisite/slovnik/gprs/) a UMTS a funguje mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a uzlem [SGSN](/mobilnisite/slovnik/sgsn/) (Serving GPRS Support Node). Jejím hlavním úkolem je poskytnout spolehlivé, šifrované logické spojení pro přenos uživatelských dat a signalizačních zpráv. Vrstva LLC je nezávislá na podkladové technologii rádiového rozhraní, což jí umožňuje fungovat přes různé rádiové přístupové sítě, jako jsou GPRS, [EDGE](/mobilnisite/slovnik/edge/) a UMTS. V protokolovém zásobníku rádiového rozhraní se nachází nad vrstvou [RLC](/mobilnisite/slovnik/rlc/)/[MAC](/mobilnisite/slovnik/mac/) a rozhraní k vyšším vrstvám, jako je [SNDCP](/mobilnisite/slovnik/sndcp/) (Subnetwork Dependent Convergence Protocol) pro uživatelská data a [GMM](/mobilnisite/slovnik/gmm/) (GPRS Mobility Management) pro signalizaci.

LLC funguje ve dvou režimech: potvrzovaném a nepotvrzovaném. V potvrzovaném režimu poskytuje opravu chyb pomocí mechanismů ARQ (Automatic Repeat Request), číslování sekvencí a řízení toku, aby zajistila spolehlivé doručení dat. Tento režim se typicky používá pro signalizaci a ne-reálná uživatelská data. Nepotvrzovaný režim nabízí jednodušší, nespojovanou službu bez retransmisí, vhodnou pro citlivý na zpoždění provoz, jako je hlas přes IP nebo streamování. Struktura LLC rámce zahrnuje pole pro typ rámce (informační, dohledový nebo nečíslovaný), adresní pole pro identifikátory SAP (Service Access Point) pro multiplexování různých datových toků (např. uživatelská data, signalizace, SMS), sekvenční čísla pro potvrzované přenosy a pole pro užitečná data. Šifrování pro důvěrnost se také provádí na vrstvě LLC na základě klíčů stanovených během procedury připevnění (GPRS attach) a bezpečnostních procedur.

Klíčovou součástí je přístupový bod služby LLC (SAP), který definuje rozhraní mezi LLC a vyššími vrstvami. Mezi běžné SAP patří LLC-SAPI pro uživatelská data a LLGMM-SAPI pro signalizaci správy mobility GPRS. Vrstva LLC zpracovává segmentaci paketů z vyšších vrstev na LLC rámce a jejich opětovné sestavení na přijímací straně. Také spravuje zřizování, údržbu a uvolňování logického spojení. V síťové architektuře je spojení LLC ukončeno v SGSN, což znamená, že SGSN provádí zpracování LLC pro každou mobilní stanici. Tento centrální koncový bod umožňuje efektivní správu mobility a předávání spojení mezi SGSN bez přerušení logického spoje, protože kontext LLC lze přenést mezi SGSN.

## K čemu slouží

Vrstva LLC byla zavedena ve 3GPP Release 99, aby poskytla standardizovaný, spolehlivý datový spoj pro paketově orientované služby v sítích GPRS a UMTS. Před GPRS používaly okruhově orientované datové služby v GSM odlišný protokolový zásobník, který nebyl optimalizován pro paketová data a postrádal efektivní opravu chyb a schopnosti multiplexování pro více datových toků. LLC tyto nedostatky řeší tím, že nabízí robustní linkovou vrstvu, která zajišťuje integritu dat přes inherentně náchylné k chybám rádiové rozhraní, což je klíčové pro IP aplikace.

Její vytvoření bylo motivováno potřebou podporovat širokou škálu služeb, od trhaného internetového provozu po aplikace v reálném čase, přes sdílenou paketově orientovanou infrastrukturu. Tím, že poskytuje jak potvrzovaný, tak nepotvrzovaný režim přenosu, může LLC uspokojit různé požadavky na QoS. Nezávislost na podkladové rádiové technologii umožňuje plynulý vývoj od GPRS k UMTS a dále, čímž chrání investice do prvků jádra sítě, jako je SGSN. Dále schopnosti LLC šifrování zvyšují bezpečnost uživatelských dat přenášených přes vzdušné rozhraní.

LLC řeší problém udržování konzistentního logického spojení během mobility mobilní stanice. Protože spojení LLC je ukotveno v SGSN, zůstává stabilní i když se mobilní stanice pohybuje mezi různými základnovými stanicemi nebo buňkami rádiového přístupu, což zjednodušuje procedury předávání spojení. Tento návrh podporuje efektivní využití zdrojů a umožňuje funkce jako pozastavené a obnovené datové relace, které jsou klíčové pro provoz mobilních zařízení šetrný k baterii.

## Klíčové vlastnosti

- Poskytuje spolehlivý přenos dat pomocí ARQ v potvrzovaném režimu
- Podporuje nepotvrzovaný režim pro provoz citlivý na zpoždění
- Provádí šifrování dat pro důvěrnost přes rádiové rozhraní
- Nabízí multiplexování různých datových toků prostřednictvím přístupových bodů služby (SAP)
- Spravuje segmentaci a opětovné sestavování paketů z vyšších vrstev
- Nezávislá na podkladové technologii rádiového přístupu (GPRS/UMTS)

## Související pojmy

- [SNDCP – Sub-Network Dependent Convergence Protocol](/mobilnisite/slovnik/sndcp/)
- [GMM – Global Multimedia Mobility](/mobilnisite/slovnik/gmm/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.065** (Rel-4) — GPRS Subnetwork Dependent Convergence Protocol
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [LLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/llc/)
