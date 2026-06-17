---
slug: "moi"
url: "/mobilnisite/slovnik/moi/"
type: "slovnik"
title: "MOI – Managed Object Instance"
date: 2026-01-01
abbr: "MOI"
fullName: "Managed Object Instance"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/moi/"
summary: "Konkrétní, vytvořená instance spravovaného objektu (MO) v systému správy telekomunikační sítě, která reprezentuje skutečný síťový prvek (např. základnovou stanici nebo port směrovače) a lze ji monitor"
---

MOI je konkrétní, vytvořená instance spravovaného objektu, která reprezentuje skutečný síťový prvek (např. základnovou stanici) a je základní jednotkou dat pro monitorování a řízení v rámci správy sítě.

## Popis

Instance spravovaného objektu (MOI) je konkrétní reprezentace fyzického nebo logického síťového prvku v rámci systému správy, strukturovaná podle definovaného informačního modelu. Každá MOI je instancí třídy spravovaného objektu ([MO](/mobilnisite/slovnik/mo/)), což je šablona definující atributy, oznámení a operace použitelné pro daný typ prvku. Například třída MO "ManagedElement" může definovat atributy jako "userLabel", "vendorName" a "locationName". Konkrétní MOI této třídy by pak reprezentovala skutečný síťový prvek, například "eNodeB-12345" v Londýně, s konkrétními hodnotami přiřazenými těmto atributům.

MOI jsou organizovány ve stromu správy informací ([MIT](/mobilnisite/slovnik/mit/)), což je hierarchický jmenný prostor, kde je každá MOI jednoznačně identifikována svým rozlišujícím jménem ([DN](/mobilnisite/slovnik/dn/)). DN je složeno z relativních rozlišujících jmen (RDN) sebe samé a všech jejích nadřazených MOI ve stromu. Tato struktura odráží vztahy obsahové hierarchie; například MOI reprezentující sektor buňky může být potomkem MOI reprezentující buňku, která je zase potomkem MOI reprezentující základnovou stanici. Tato hierarchie umožňuje efektivní, rozsahem omezené řídicí operace. MOI komunikují se systémem správy (správce sítě, [NM](/mobilnisite/slovnik/nm/), nebo správce prvku, [EM](/mobilnisite/slovnik/em/)) prostřednictvím standardizovaných rozhraní, především Itf-N (založeného na [CORBA](/mobilnisite/slovnik/corba/)/XML) v dřívějších verzích a RESTful 3GPP Management Services (MnS) v 5G.

Životní cyklus MOI zahrnuje vytvoření, konfiguraci, monitorování a odstranění. Operace nad MOI zahrnují GET (načtení hodnot atributů), SET (změna konfigurace), CREATE, DELETE a ACTION (vyvolání konkrétní procedury). MOI také generují oznámení (asynchronní alarmy nebo hlášení o změně stavu), aby upozornily systém správy na události. Klíčovými součástmi konceptu MOI jsou informační model (např. 3GPP NRM - Network Resource Model), schéma pojmenování a adresování (DN/RDN) a protokolové vazby pro rozhraní směrem k vyšším systémům. V 5G jsou MOI ústřední pro architekturu správy založenou na službách (SBMA), kde jsou instance spravovaných objektů vystaveny jako spravovatelné zdroje prostřednictvím vztahů producent-konzument využívajících [HTTP](/mobilnisite/slovnik/http/)/[JSON](/mobilnisite/slovnik/json/).

## K čemu slouží

MOI existují proto, aby poskytly standardizovaný, abstrahovaný a programovatelný způsob správy nesčetných heterogenních síťových prvků v telekomunikačním prostředí s více dodavateli. Před zavedením takových standardizovaných informačních modelů používal každý dodavatel proprietární řídicí rozhraní a datové modely, což činilo integrovanou správu sítě, automatizovanou provizi a interoperabilitu mezi více dodavateli pro operátory extrémně složitou a nákladnou. Koncept MOI jako součást širšího rámce spravovaných objektů to řeší definováním společného jazyka a struktury pro reprezentaci síťových zdrojů.

Hlavním řešeným problémem je složitost integrace systémů správy sítě. Definováním zdrojů jako MOI se standardizovanými atributy a chováním mohou systémy správy objevovat, konfigurovat a monitorovat zařízení od různých dodavatelů pomocí stejné sady operací. To umožňuje jednotnou správu poruch, konfigurace, účtování, výkonu a zabezpečení (FCAPS). Také usnadňuje automatizovanou správu životního cyklu sítě, což je zásadní pro moderní koncepty, jako je dělení sítě nebo správa sítě a služeb s nulovou obslužností (ZSM).

Historicky byla řídicí rozhraní často založena na příkazovém řádku a byla specifická pro dodavatele. Přechod k objektově orientovaným modelům správy, ovlivněný rámcem Telekomunikační sítě pro správu (TMN) a později prací 3GPP v oblasti správy sítě (NM), stanovil spravovaný objekt jako klíčový princip. Instancování těchto objektů jako MOI poskytlo konkrétní "úchyt" pro řídicí software. Jeho vývoj napříč verzemi 3GPP směřoval k většímu sladění s IT postupy (jako jsou RESTful API a YANG datové modely v pozdější správě 5G), ale základní koncept MOI jako instance modelovaného zdroje zůstává základní datovou entitou pro všechny interakce správy.

## Klíčové vlastnosti

- Instance třídy spravovaného objektu reprezentující skutečný síťový prvek
- Definována sadou atributů s konkrétními hodnotami
- Jednoznačně identifikována rozlišujícím jménem (DN) v rámci hierarchie
- Podporuje operace CRUD (vytvořit, přečíst, aktualizovat, odstranit) a akce
- Může generovat oznámení pro alarmy a změny stavu
- Základní datová entita ve standardizovaných řídicích rozhraních (Itf-N, 3GPP MnS)

## Definující specifikace

- **TS 28.510** (Rel-19) — NFV Configuration Management Requirements
- **TS 28.561** (Rel-20) — Management and Orchestration; Network Digital Twin
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TS 28.701** (Rel-19) — Core Network NRM IRP Requirements
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 28.802** (Rel-15) — Management Study for 5G Network Architecture
- **TR 28.812** (Rel-17) — Study on Intent Driven Management Services
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 32.257** (Rel-19) — Edge Computing Charging Management
- **TS 32.300** (Rel-19) — 3GPP Network Resource Naming Convention
- **TS 32.306** (Rel-19) — Configuration Management Notification IRP Solution Set
- **TS 32.333** (Rel-9) — Notification Log IRP CORBA Solution Set
- **TS 32.336** (Rel-19) — Notification Log IRP Solution Set Definitions
- **TS 32.600** (Rel-19) — 3GPP Configuration Management Specification
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [MOI na 3GPP Explorer](https://3gpp-explorer.com/glossary/moi/)
