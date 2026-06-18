---
slug: "nrm"
url: "/mobilnisite/slovnik/nrm/"
type: "slovnik"
title: "NRM – Network Resource Model"
date: 2026-01-01
abbr: "NRM"
fullName: "Network Resource Model"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nrm/"
summary: "Standardizovaný informační model používaný v řídicích systémech 3GPP k reprezentaci spravovaných síťových elementů a jejich zdrojů. Definuje objekty, atributy a vztahy, které lze řídit, a poskytuje ta"
---

NRM je standardizovaný informační model v 3GPP, který definuje spravované síťové elementy, jejich zdroje, atributy a vztahy pro konfigurační, poruchové, výkonnostní a inventární řízení v sítích s více dodavateli.

## Popis

Model síťových zdrojů (NRM) je klíčovým prvkem architektury Telekomunikační řídicí sítě ([TMN](/mobilnisite/slovnik/tmn/)) a Řídicího systému ([MS](/mobilnisite/slovnik/ms/)) dle 3GPP. Jde o komplexní objektově orientovaný informační model, který poskytuje abstraktní reprezentaci všech fyzických a logických zdrojů v rámci sítě 3GPP podléhajících řízení. NRM je definován pomocí diagramů tříd v Unified Modeling Language ([UML](/mobilnisite/slovnik/uml/)) a je implementován v řídicích rozhraních, typicky za použití protokolů jako [CORBA](/mobilnisite/slovnik/corba/), [SNMP](/mobilnisite/slovnik/snmp/), nebo v poslední době NETCONF/YANG a RESTful [API](/mobilnisite/slovnik/api/). Jeho primární funkcí je sloužit jako datové schéma pro referenční bod Rozhraní-N (Itf-N), který se používá pro komunikaci mezi vrstvou Řízení sítě ([NM](/mobilnisite/slovnik/nm/)) a vrstvou Řízení elementů ([EM](/mobilnisite/slovnik/em/)) nebo mezi různými doménami.

V jádru NRM funguje definováním tříd Spravovaných objektů (MO). Každá třída MO reprezentuje spravovatelnou síťovou entitu, jako je gNB, AMF, buňka, propojení nebo softwarová funkce. Tyto třídy mají atributy popisující vlastnosti entity (např. administrativní stav, provozní stav, kapacitní parametry), notifikace, které entita může vysílat (např. alarmy, změny stavu), a akce, které na ní lze vyvolat (např. reset, upgrade softwaru). Zásadní je, že model také definuje vztahy obsahování (např. gNB obsahuje buňky) a asociační vztahy (např. buňka je asociována s kmitočtovým pásmem) mezi těmito třídami MO. Tím vzniká hierarchická stromová struktura spravovaných objektů, která odráží fyzickou a funkční architekturu sítě.

Klíčovými komponentami NRM jsou definice Integračních referenčních bodů (IRP). 3GPP definuje více IRP, z nichž každý se zaměřuje na konkrétní oblast řízení: Konfigurační řízení (CM), Poruchové řízení (FM), Výkonnostní řízení (PM) a Inventární řízení (IM). Každý IRP specifikuje podmnožinu celkového NRM, podrobně popisuje třídy MO, atributy a chování relevantní pro danou řídicí funkci. Například IRP pro CM definuje MO a atributy pro konfiguraci síťových elementů, zatímco IRP pro PM definuje MO pro sběr výkonnostních měření, jako je míra ztracených hovorů nebo propustnost. NRM je rozšiřitelný, což umožňuje přidávání nových tříd MO a atributů v každé verzi 3GPP pro podporu nových síťových funkcí, jako je 5G NR, síťové slicing nebo edge computing.

Úloha NRM v síti spočívá v umožnění automatizovaného, standardizovaného a více-dodavatelského řízení sítě. Poskytnutím společného modelu zajišťuje, že řídicí systém od jednoho dodavatele může rozumět a ovládat síťové elementy od jiného dodavatele, pokud oba splňují specifikace 3GPP NRM. Je základem pro zřizování nových služeb, monitorování stavu sítě, sběr výkonnostních dat pro optimalizaci a udržování přesného inventáře síťových aktiv. Podrobnost a struktura modelu umožňují granulární řízení a přehlednost, od síťových slice na vysoké úrovni až po jednotlivé hardwarové komponenty uvnitř základnové stanice.

## K čemu slouží

NRM byl vytvořen, aby vyřešil kritický problém interoperability při řízení složitých telekomunikačních sítí s více dodavateli. V počátcích mobilních sítí každý dodavatel zařízení poskytoval proprietární řídicí rozhraní a datové modely pro své síťové elementy. To nutilo operátory používat oddělené, na dodavateli závislé řídicí systémy, což vedlo k provozní neefektivitě, vysokým nákladům na integraci a neschopnosti automatizovat end-to-end zřizování služeb a jejich zajištění napříč sítí.

Primárním účelem NRM je poskytnout standardizovaný, technologicky neutrální informační model, který slouží jako smlouva mezi poskytovateli síťového vybavení a vývojáři řídicích systémů. Řeší omezení proprietárních modelů definováním společného jazyka pro reprezentaci síťových zdrojů. To umožňuje vývoj obecných, více-dodavatelských Systémů pro řízení sítě (NMS) a Systémů pro podporu provozu (OSS), které mohou konfigurovat, monitorovat a odstraňovat závady na zařízeních od jakéhokoli kompatibilního dodavatele. Motivace byla hluboce zakořeněna v cíli vrstveného, standardizovaného řízení dle rámce TMN.

Historicky jeho vývoj začal ve verzi 3GPP Release 4, která formalizovala řízení pro sítě UMTS. Jeho vývoj byl poháněn zaváděním nových síťových architektur. Každá nová generace (3G, 4G, 5G) a každá nová funkce (IMS, LTE, NR, síťový slicing) si vyžádala rozšíření NRM, aby reprezentoval nové spravované entity a jejich parametry. NRM tak řeší neustálou výzvu udržování kroků mezi schopnostmi síťového řízení a rychlým síťovým vývojem, a zajišťuje, že operátoři mohou řídit celou svou heterogenní síťovou stopu prostřednictvím konzistentní, standardizované optiky.

## Klíčové vlastnosti

- Objektově orientovaný informační model definující třídy Spravovaných objektů (MO) pro všechny síťové zdroje
- Strukturován pomocí hierarchií obsahování a asociací, aby odrážel síťovou architekturu
- Definován dle Integračních referenčních bodů (IRP) pro Konfigurační, Poruchové, Výkonnostní a Inventární řízení
- Poskytuje technologicky neutrální abstrakci, použitelnou pro síťové elementy 2G, 3G, 4G a 5G
- Umožňuje více-dodavatelskou interoperabilitu pro systémy řízení sítě (NMS/OSS)
- Rozšiřitelný model aktualizovaný v každé verzi 3GPP pro podporu nových síťových funkcí a architektur

## Související pojmy

- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)
- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)
- [EMS – Enhanced Messaging Service](/mobilnisite/slovnik/ems/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.111** (Rel-19) — Fault Management Service Specification
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.601** (Rel-12) — Telecom management; CN and non-3GPP access NRM IRP Requirements
- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.611** (Rel-19) — EPC-WLAN Interworking NRM IRP Requirements
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- … a dalších 180 specifikací

---

📖 **Anglický originál a plná specifikace:** [NRM na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrm/)
