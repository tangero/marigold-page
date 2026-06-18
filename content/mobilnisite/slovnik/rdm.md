---
slug: "rdm"
url: "/mobilnisite/slovnik/rdm/"
type: "slovnik"
title: "RDM – Reference Data Model"
date: 2025-01-01
abbr: "RDM"
fullName: "Reference Data Model"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rdm/"
summary: "Standardizovaný, hierarchický datový model definovaný 3GPP pro správu síťových prvků a služeb. Poskytuje společnou strukturu a sémantiku pro konfigurační správu, správu poruch, výkonu a inventáře, což"
---

RDM je standardizovaný, hierarchický datový model definovaný 3GPP pro správu síťových prvků a služeb, který poskytuje společnou strukturu pro konfigurační správu, správu poruch, výkonu a inventáře.

## Popis

Referenční datový model (RDM) v 3GPP je komplexní, technologicky neutrální informační rámec, který definuje spravované objekty, jejich atributy, vztahy a chování pro správu telekomunikačních sítí. Slouží jako kanonická šablona pro všechna 3GPP definovaná Management Data ([MD](/mobilnisite/slovnik/md/)) napříč různými síťovými doménami, včetně 5G Core, NG-RAN a IMS. RDM je specifikován pomocí metodologie diagramu tříd v Unified Modeling Language ([UML](/mobilnisite/slovnik/uml/)), která je následně převedena do konkrétních implementací, jako jsou YANG datové modely pro správu založenou na NETCONF/YANG nebo Structure of Management Information ([SMI](/mobilnisite/slovnik/smi/)) pro [SNMP](/mobilnisite/slovnik/snmp/). Model je organizován hierarchicky, počínaje síťovými funkcemi a službami vysoké úrovně až po fyzické a logické komponenty, jako jsou gNB, [AMF](/mobilnisite/slovnik/amf/), řezy sítě (slices) a [PDU](/mobilnisite/slovnik/pdu/) relace. Každá třída spravovaného objektu v RDM má definované atributy (např. administrativní stav, provozní stav), notifikace (pro události poruch a výkonu) a akce (operace, které lze vyvolat). RDM pokrývá klíčové oblasti správy: správu poruch (alarmy, dohled nad poruchami), správu konfigurace (provisioning, správa softwaru), správu výkonu (čítače, měření) a správu inventáře. Například RDM pro gNB by definoval objekty reprezentující jeho buňky, kmitočty nosných, konfigurace beamformingu a související [KPI](/mobilnisite/slovnik/kpi/). Systémy správy, jako jsou Network Management Systems ([NMS](/mobilnisite/slovnik/nms/)) nebo Element Management Systems (EMS), komunikují se síťovými prvky pomocí protokolů jako NETCONF, které přenášejí instance dat odvozených z YANG modelů RDM. To zajišťuje, že správce od dodavatele A může konfigurovat a monitorovat síťový prvek od dodavatele B, protože oba dodržují stejné definice RDM. RDM je průběžně rozšiřován, aby podporoval nové 3GPP funkce, jako jsou síťové řezy (network slicing), edge computing a nesatelitní sítě, čímž zajišťuje, že schopnosti správy se vyvíjejí spolu se síťovou architekturou.

## K čemu slouží

RDM byl vytvořen, aby vyřešil kritické výzvy v oblasti interoperability a integrace v telekomunikačních sítích s více dodavateli. Před jeho standardizací každý dodavatel zařízení používal proprietární datové modely pro správu svých síťových prvků, což nutilo operátory vyvíjet složité, dodavatelsky specifické integrace pro jejich OSS/BSS systémy. To vedlo k vysokým provozním nákladům, dlouhým cyklům nasazování nových služeb a závislosti na dodavateli. 3GPP RDM, zahájený ve verzi 10, poskytl společný jazyk pro management informací, což umožnilo skutečnou multi-vendor plug-and-play operaci. Umožňuje operátorům automatizovat správu životního cyklu sítě – od provisioning a uvedení do provozu až po zajištění kvality a optimalizaci – pomocí standardizovaných rozhraní a datových struktur. To je obzvláště důležité pro moderní sítě, jako je 5G, které jsou softwarově řízené, cloud-nativní a podporují dynamické funkce, jako jsou síťové řezy, které vyžadují rychlé, programovatelné změny konfigurace napříč doménami. RDM také usnadňuje adopci moderních, modelově řízených paradigmat správy, jako je Software-Defined Networking (SDN) a Network Function Virtualization (NFV), kde je datový model centrální smlouvou mezi kontrolérem a síťovými prvky. Tím, že poskytuje jediný zdroj pravdy pro sémantiku správy, RDM snižuje chyby, urychluje nasazování služeb a tvoří páteř pro autonomní sítě a intent-based management v budoucích verzích.

## Klíčové vlastnosti

- Technologicky neutrální, na UML založený hierarchický model definující spravované objekty a jejich vztahy
- Pokrývá oblasti správy poruch, konfigurace, výkonu a inventáře (FCPI)
- Umožňuje multi-vendor interoperabilitu pro rozhraní správy sítě
- Slouží jako zdroj pro odvození konkrétních implementačních datových modelů (např. YANG, SMI)
- Rozšiřitelný pro podporu nových síťových funkcí a služeb, jako jsou síťové řezy
- Usnadňuje automatizovanou, modelově řízenou správu a orchestraci sítě

## Definující specifikace

- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TR 29.935** (Rel-19) — HSS Reference Data Model for Ud Interface
- **TR 32.901** (Rel-19) — UDC Application Data Models Study

---

📖 **Anglický originál a plná specifikace:** [RDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/rdm/)
