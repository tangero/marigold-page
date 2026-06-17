---
slug: "eir"
url: "/mobilnisite/slovnik/eir/"
type: "slovnik"
title: "EIR – Equipment Identity Register"
date: 2025-01-01
abbr: "EIR"
fullName: "Equipment Identity Register"
category: "Security"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/eir/"
summary: "Equipment Identity Register (EIR) je bezpečnostní databáze v mobilních sítích, která ukládá a ověřuje mezinárodní identity mobilních zařízení (IMEI). Kontroluje, zda je zařízení na černé listině (ukra"
---

EIR je bezpečnostní databáze v mobilních sítích, která ukládá a ověřuje identity zařízení (IMEI), aby zkontrolovala, zda jsou na černé, šedé nebo bílé listině, a zabraňuje tak neoprávněným nebo problematickým zařízením v přístupu k síti.

## Popis

Equipment Identity Register (EIR) je klíčová bezpečnostní entita v jádru sítě systémů GSM, UMTS, LTE a 5G. Funguje jako centralizovaná databáze, která spravuje seznamy mezinárodních identit mobilních zařízení ([IMEI](/mobilnisite/slovnik/imei/)), což jsou jedinečné identifikátory přiřazené mobilním zařízením. EIR klasifikuje IMEI do tří seznamů: bílá listina pro známá platná zařízení, černá listina pro zařízení nahlášená jako ukradená, blokovaná nebo technicky vadná, a šedá listina pro zařízení pod dohledem (např. s anomáliemi). Když se uživatelské zařízení (UE) pokouší připojit k síti, Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G dotazuje EIR, aby ověřil IMEI zařízení.

EIR funguje tak, že přijímá požadavky na kontrolu IMEI prostřednictvím standardizovaných rozhraní, jako je rozhraní S13 v LTE (mezi MME a EIR) nebo servisní rozhraní N5g-eir v 5G (mezi AMF a EIR). Po přijetí požadavku EIR prohledá svou databázi a vrátí odpověď udávající stav IMEI v seznamech. Mezi klíčové komponenty patří databázový engine pro ukládání záznamů IMEI, moduly pro autentizaci a autorizaci pro zabezpečení přístupu a synchronizační mechanismy pro aktualizaci seznamů z externích zdrojů, jako je Central Equipment Identity Register ([CEIR](/mobilnisite/slovnik/ceir/)) nebo vstupy od operátora. V 5G je EIR implementována jako síťová funkce ([NF](/mobilnisite/slovnik/nf/)), kterou lze nasadit v cloud-nativních prostředích, což nabízí škálovatelnost a flexibilitu.

V síťové architektuře hraje EIR obrannou roli proti podvodům a krádežím souvisejícím se zařízeními. Blokováním zařízení na černé listině odrazuje od používání ukradených telefonů a snižuje pojistné události. Také pomáhá udržovat integritu sítě tím, že brání vadným zařízením v působení rušení nebo zhoršování služeb. Integrace EIR s dalšími bezpečnostními funkcemi, jako je Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), zvyšuje celkovou bezpečnostní úroveň sítě. Její činnost je řízena specifikacemi jako 29.272 a 29.273 pro rozhraní a 33.857 pro bezpečnostní aspekty, což zajišťuje interoperabilitu napříč různými generacemi mobilních sítí.

## K čemu slouží

EIR byla vytvořena pro boj s rostoucím problémem krádeží a klonování mobilních telefonů v raných sítích GSM. Před jejím zavedením bylo možné ukradená zařízení snadno znovu použít v sítích, což vedlo k finančním ztrátám uživatelů a operátorů a podporovalo kriminalitu. EIR poskytuje standardizovaný mechanismus pro sledování a blokování takových zařízení, čímž chrání spotřebitele a snižuje motivaci ke krádeži. Její vývoj byl hnán potřebou globálního, interoperabilního systému pro sdílení informací o ukradených zařízeních, který usnadňují subjekty jako Central Equipment Identity Register ([CEIR](/mobilnisite/slovnik/ceir/)) od GSMA.

Historicky, bez EIR, měli operátoři omezené možnosti, jak ověřit legitimitu zařízení, a spoléhali se na manuální hlášení a lokální černé listiny. EIR tento proces automatizovala a umožnila kontrolu v reálném čase během připojování k síti. V průběhu jednotlivých vydání se její účel rozšířil o řešení závad zařízení a regulatorních požadavků, jako je blokování nevyhovujících nebo padělaných zařízení. V 5G se EIR vyvinula tak, aby podporovala nové servisně orientované architektury a integrovala se s network slicing, čímž zajišťuje bezpečnost zařízení na úrovni jednotlivých řezů. Řeší problémy podvodů se zařízeními, zneužívání sítě a podporuje zákonné odposlechy tím, že poskytuje spolehlivou identifikaci zařízení, čímž zvyšuje důvěru v mobilní komunikaci.

## Klíčové vlastnosti

- Ukládání a správa bílých, černých a šedých listin IMEI pro ověřování zařízení
- Standardizovaná dotazovací rozhraní (např. S13 v LTE, N5g-eir v 5G) pro síťové funkce ke kontrole stavu zařízení
- Integrace s centrálními databázemi (např. CEIR) pro globální sledování ukradených zařízení
- Podpora ověřování IMEI v reálném čase během procedur připojování a registrace zařízení
- Bezpečnostní mechanismy pro ochranu dat v EIR a zajištění autorizovaného přístupu dle specifikace 33.857
- Možnost cloud-nativního nasazení v 5G se škálovatelností a servisně orientovanou architekturou

## Související pojmy

- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [CEIR – Central Equipment Identity Register](/mobilnisite/slovnik/ceir/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.511** (Rel-19) — 5G Equipment Identity Register Service Interface
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.140** (Rel-19) — Subscription Management (SuM) requirements
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [EIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/eir/)
