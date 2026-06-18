---
slug: "uml"
url: "/mobilnisite/slovnik/uml/"
type: "slovnik"
title: "UML – Unified Modeling Language"
date: 2026-01-01
abbr: "UML"
fullName: "Unified Modeling Language"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/uml/"
summary: "Standardizovaný obecný modelovací jazyk od skupiny Object Management Group (OMG), který je ve specifikacích 3GPP hojně používán pro vizuální návrh, dokumentaci a specifikaci systémové architektury, pr"
---

UML je standardizovaný obecný modelovací jazyk používaný ve specifikacích 3GPP pro vizuální návrh, dokumentaci a specifikaci systémové architektury, procesů a datových struktur telekomunikačních systémů.

## Popis

Unified Modeling Language (UML) není technologie specifická pro 3GPP, ale standardizovaný vizuální modelovací jazyk, který 3GPP přijalo pro práci na specifikacích. Poskytuje sadu grafických notací pro vytváření abstraktních modelů systémů, které jsou označovány jako UML modely. V rámci 3GPP je UML primárně používán při specifikaci managementových rozhraní, služeb a síťové architektury, zvláště v Technické specifikaci skupiny pro služby a systémové aspekty ([TSG](/mobilnisite/slovnik/tsg/) [SA](/mobilnisite/slovnik/sa/)) a jejích pracovních skupin. Jazyk umožňuje přesnou definici informačních modelů, rozhraní služeb a stavových automatů, které popisují chování síťových entit a managementových funkcí.

V praxi specifikace 3GPP využívají konkrétní UML diagramy pro sdělení technických informací. Diagramy tříd jsou hojně používané pro definici modelů řízených objektů pro management síťových elementů, detailně popisují atributy, operace a vztahy mezi řízenými entitami. Sekvenční diagramy ilustrují tok zpráv a interakce mezi síťovými funkcemi nebo mezi managementovými systémy a síťovými elementy. Diagramy stavových automatů definují životní cyklus a přípustné stavové přechody řízených zdrojů nebo entit protokolů. Tyto diagramy jsou vložené v Technických specifikacích (TS) a Technických reportech (TR) 3GPP a poskytují formální a jednoznačnou reprezentaci, která doplňuje textové popisy.

Role UML v 3GPP je základní pro zajištění interoperability a konzistentní implementace. Použitím standardizovaného modelovacího jazyka může 3GPP definovat komplexní managementové informační modely (např. pro Fault, Configuration, Accounting, Performance, and Security - FCAPS) a definice rozhraní (např. pro Itf-N nebo [OAM](/mobilnisite/slovnik/oam/) rozhraní) způsobem, který je neutrální vůči nástrojům a platformám. Tento formální modelovací přístup snižuje ambiguitu, usnadňuje automatickou generaci kódu a pomáhá při testování konformnosti implementací. Rozsáhlý seznam specifikací 3GPP, které odkazují na UML, počínaje Release 4, podtrhuje jeho kritickou roli při architektuře a managementu 3G, 4G a 5G sítí.

## K čemu slouží

UML byl přijat 3GPP, aby řešil rostoucí komplexnost specifikací telekomunikačních systémů a potřebu přesných, jednoznačných definic architektury a rozhraní. Před jeho širokým použitím specifikace závisely silně na textových popisech a neformálních diagramech, což mohlo vést k různým interpretacím výrobci zařízení a síťových operátorů a výsledkem byly problémy interoperability. Formální, grafická povaha UML poskytuje běžný jazyk, který zlepšuje jasnost, konzistenci a úplnost technických požadavků.

Motivace pro jeho integraci, zvláště od Release 4, se časově shodovala s vývojem více sofistikovaných frameworků pro síťový management a orchestrace. Jak se sítě vyvíjely, aby obsahovaly IP Multimedia Subsystem (IMS), řízení politik a následně síťové segmenty, informační modely a procedury se staly příliš komplexními, aby byly efektivně popsány pouze textem. UML nabídlo strukturovaný způsob modelování řízených objektů, jejich vztahů a jejich chování, což je esenciální pro automatizovanou provisioning, assurance a lifecycle management síťových služeb. Jeho použití podporuje model-driven development a je v souladu s průmyslovými trendy směřujícími ke standardizovanému informačnímu modelování pro Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)).

## Klíčové vlastnosti

- Standardizovaná grafická notace pro modelování systémů (diagramy tříd, sekvenční, stavové)
- Formální definice managementových informačních modelů a datových struktur
- Specifikace dynamického chování a sekvencí protokolových zpráv
- Reprezentace nezávislá na platformě a neutrální vůči nástrojům
- Podpora metodologií model-driven architektury a vývoje
- Zvyšuje jasnost a snižuje ambiguitu v technických specifikacích

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [TSG-SA – Technical Specification Group - Services and System Aspects](/mobilnisite/slovnik/tsg-sa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.625** (Rel-19) — State Management Data Definition IRP Information Service
- **TS 28.632** (Rel-19) — Inventory Management NRM Integration Reference Point
- **TS 28.652** (Rel-19) — UTRAN Network Resource Model (NRM) IRP Information Service
- **TS 28.655** (Rel-19) — GERAN NRM IRP Information Service
- **TS 28.682** (Rel-19) — WLAN Management NRM IRP Information Service
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 28.708** (Rel-19) — EPC NRM Integration Reference Point Information Service
- **TS 28.732** (Rel-19) — Transport Network NRM IRP Information Service
- **TS 28.735** (Rel-19) — STN Interface NRM IRP Information Service
- … a dalších 59 specifikací

---

📖 **Anglický originál a plná specifikace:** [UML na 3GPP Explorer](https://3gpp-explorer.com/glossary/uml/)
