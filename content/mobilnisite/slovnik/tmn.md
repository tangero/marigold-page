---
slug: "tmn"
url: "/mobilnisite/slovnik/tmn/"
type: "slovnik"
title: "TMN – Telecommunications Management Network"
date: 2026-01-01
abbr: "TMN"
fullName: "Telecommunications Management Network"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/tmn/"
summary: "Standardizovaný rámec, definovaný ITU-T, pro interoperabilní správu telekomunikačních sítí a služeb. Poskytuje architektonické principy, funkční oblasti a informační modely, které operátorům umožňují"
---

TMN je standardizovaný rámec ITU-T pro interoperabilní správu telekomunikačních sítí a služeb, který poskytuje architekturu a modely pro FCAPS správu v prostředí více dodavatelů.

## Popis

Telecommunications Management Network (TMN) je koncepční rámec standardizovaný [ITU-T](/mobilnisite/slovnik/itu-t/) v doporučení M.3010. Není to fyzická síť, ale logicky oddělená nadřazená architektura, která komunikuje s telekomunikační sítí, kterou spravuje. Základním principem TMN je poskytnout organizované, strukturované a standardizované způsoby pro dosažení interoperability a automatizované správy heterogenních síťových prvků ([NE](/mobilnisite/slovnik/ne/)) a síťových systémů. Jeho architektura je postavena na vrstveném modelu zahrnujícím čtyři logické vrstvy: Business Management Layer (BML), Service Management Layer ([SML](/mobilnisite/slovnik/sml/)), Network Management Layer ([NML](/mobilnisite/slovnik/nml/)) a Element Management Layer ([EML](/mobilnisite/slovnik/eml/)), přičemž Network Element Layer (NEL) představuje skutečné spravované zdroje.

TMN definuje klíčové funkční oblasti, shrnuté v modelu FCAPS: správu poruch (detekce, izolace, náprava), správu konfigurace (zřizování, řízení stavu), správu účtování (měření využití a účtování), správu výkonu (sběr dat o kvalitě a provozu) a správu zabezpečení (řízení přístupu, integrita). Komunikace mezi systémy správy a síťovými prvky probíhá přes standardizovaná rozhraní, primárně rozhraní Q3, které používá Common Management Information Protocol ([CMIP](/mobilnisite/slovnik/cmip/)) nad [OSI](/mobilnisite/slovnik/osi/) zásobníky, a jednodušší rozhraní Qx. Informace jsou modelovány pomocí Guidelines for the Definition of Managed Objects ([GDMO](/mobilnisite/slovnik/gdmo/)) a Abstract Syntax Notation One (ASN.1), což umožňuje společný popis spravovaných zdrojů.

V rámci 3GPP tvoří principy a modely TMN historický základ pro rámec Operations, Administration, and Maintenance (OAM) a referenční body označené pro správu (Itf-N). Zatímco systémy 3GPP se vyvinuly k používání modernějších protokolů, jako jsou SNMP a NETCONF/YANG, koncepty TMN týkající se vrstev správy, funkčního oddělení a standardizované výměny informací zůstávají hluboce vlivné. Umožňuje integraci Network Management Systems (NMS) a Operations Support Systems (OSS) k automatizaci úloh, jako je zřizování služeb, monitorování výkonu a korelace poruch v celé doméně sítě 3GPP, od rádiového přístupu po core.

## K čemu slouží

TMN byl vytvořen k řešení kritického problému provozní složitosti a nákladů v telekomunikačních sítích více dodavatelů. Před jeho standardizací poskytoval každý dodavatel zařízení proprietární systémy správy s jedinečnými rozhraními, což nutilo síťové operátory spravovat scénář 'ostrůvků správy'. To vedlo k vysokým integračním nákladům, manuálním procesům, neschopnosti automatizovat end-to-end zřizování služeb a obtížím při korelaci poruch napříč různými síťovými doménami. Rámec TMN poskytl univerzální 'předlohu' pro interoperabilní správu.

Jeho přijetí 3GPP, počínaje ranými releasy, bylo motivováno potřebou spravovat komplexní, vrstvené mobilní sítě skládající se z rádiových, přepínacích a servisních platforem od více dodavatelů. Vrstvená architektura TMN (BML, SML, NML, EML) dokonale odpovídala organizačnímu a funkčnímu oddělení uvnitř telekomunikačního operátora, oddělujíc obchodní a servisní logiku od technické správy specifické pro síť a prvky. Standardizací informačních modelů (pomocí GDMO) a komunikačních protokolů (CMIP/CMIS přes Q3) měl umožnit OSS operátora spravovat síťové prvky od různých dodavatelů prostřednictvím jediného konzistentního rozhraní, čímž se snížily provozní výdaje (OPEX) a umožnilo rychlejší nasazování služeb.

## Klíčové vlastnosti

- Vrstvená architektura (BML, SML, NML, EML) oddělující obchodní, servisní, síťovou a správu na úrovni prvků
- Definuje model FCAPS jako pět klíčových funkčních oblastí správy sítě
- Standardizuje rozhraní správy, primárně rozhraní Q3 používající protokoly OSI CMIP/CMIS
- Používá GDMO a ASN.1 pro standardizované, objektově orientované modelování spravovaných zdrojů
- Poskytuje rámec pro integraci Operations Support Systems (OSS) a Network Management Systems (NMS)
- Umožňuje interoperabilní, multi-vendor správu sítě a automatizaci

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [GDMO – Guidelines for the Definition of Managed Objects](/mobilnisite/slovnik/gdmo/)
- [CMIP – Common Management Information Protocol](/mobilnisite/slovnik/cmip/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.632** (Rel-19) — Inventory Management NRM Integration Reference Point
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 29.816** (Rel-10) — PCRF Failure & Restoration Study
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 32.300** (Rel-19) — 3GPP Network Resource Naming Convention
- **TS 32.306** (Rel-19) — Configuration Management Notification IRP Solution Set
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [TMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmn/)
