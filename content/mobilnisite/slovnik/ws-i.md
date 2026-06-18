---
slug: "ws-i"
url: "/mobilnisite/slovnik/ws-i/"
type: "slovnik"
title: "WS-I – Web Services Interoperability Organization"
date: 2025-01-01
abbr: "WS-I"
fullName: "Web Services Interoperability Organization"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ws-i/"
summary: "WS-I je průmyslové konsorcium (ne technologie 3GPP), jehož profily jsou odkazovány ve specifikacích 3GPP za účelem zajištění interoperability webových služeb používaných pro správu a provisioning síťo"
---

WS-I je průmyslový konsorcium, jehož interoperability profily jsou odkazovány ve specifikacích 3GPP za účelem zajištění standardizovaných webových služeb pro správu a provisioning síťových systémů.

## Popis

Web Services Interoperability Organization (WS-I) je otevřená průmyslová organizace založená za účelem podpory interoperability webových služeb mezi různými platformami, operačními systémy a programovými jazyky. V kontextu 3GPP není WS-I technologií vyvinutou tímto standardizačním orgánem, ale externím konsorcium, jehož výstupy – konkrétně dokumenty základního profilu (Basic Profile) – jsou normativně odkazovány. Tyto profily poskytují implementační pokyny pro základní specifikace webových služeb, jako jsou [SOAP](/mobilnisite/slovnik/soap/) (Simple Object Access Protocol), [WSDL](/mobilnisite/slovnik/wsdl/) (Web Services Description Language) a [UDDI](/mobilnisite/slovnik/uddi/) (Universal Description, Discovery, and Integration). Specifikace 3GPP, zejména ty v oblasti Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)) (řada TS 32), přijímají tyto profily k definici rozhraní webových služeb pro funkce správy síťových systémů, jako je provisioning, správa chyb a správa výkonu.

Architektura systému kompatibilního s WS-I, jak je používán v 3GPP, zahrnuje poskytovatele služeb, kteří zpřístupňují funkce správy jako webové služby popsané pomocí WSDL. Konzumenti služeb, jako jsou systémy správy síťových systémů ([NMS](/mobilnisite/slovnik/nms/)) nebo element managers ([EM](/mobilnisite/slovnik/em/)), komunikují s těchto službami pomocí SOAP zpráv přes [HTTP](/mobilnisite/slovnik/http/)/[HTTPS](/mobilnisite/slovnik/https/). WS-I Basic Profile stanovuje přesné pravidla pro konstrukci těchto SOAP envelopů, zahrnující použití dokument/literal binding stylu, zpracování SOAP headers a faults a serializaci XML Schema datových typů. Tato striktní shoda zajišťuje, že management klient od jednoho výrobce může úspěšně vyvolat operaci na serveru od jiného výrobce bez interoperability problémů vznikajících z ambiguózních nebo volitelných částí základních standardů webových služeb.

Klíčové komponenty vyžadované WS-I profily zahrnují standardizovanou strukturu dokumentu WSDL, specifický formát SOAP zprávy a použití HTTP jako transportního protokolu s specifickými bezpečnostními požadavky. Jeho role v síti 3GPP je základní pro northbound rozhraní síťových elementů a management systémů, umožňující integraci více výrobců, automatizovaný provisioning a standardizované reportování chyb. Outsourcing definice interoperability webových služeb na WS-I umožnil 3GPP zaměřit se na telekomunikačně specifické datové modely a operace, a zároveň využívat stabilní, průmyslově přijímaný základ pro podkladovou komunikační mechaniku. Toto oddělení zájmů zrychluje standardizaci a zajišťuje, že management rozhraní 3GPP zůstává kompatibilní s širším IT ekosystémem enterprise service-oriented architektur.

## K čemu slouží

Účelem odkazování na WS-I ve specifikacích 3GPP bylo řešení kritického problému interoperability systémů správy síťových systémů a provisioning, které využívají webové služby. Před přijetím těchto profilů obsahovaly standardy webových služeb jako SOAP a WSDL mnoho volitelných funkcí a ambiguózních implementačních bodů. Tato flexibilita, přínosná pro inovace, vedla k vážným interoperability problémům, kdy systémy různých výrobců, i když tvrdily, že podporují stejné standardy, nemohly efektivně komunikovat. Tím vznikala závislost na výrobce, zvýšené náklady na integraci a narušovala se automatizace síťových operací.

Historicky, jak se síťové systémy 3GPP vyvíjely směrem k IP-based management (významně začínající v Release 8 s System Architecture Evolution – SAE), existoval silný tlak na sjednocení správy síťových systémů s IT praxemi. Webové služby nabídly platformně neutrální, jazykově agnostický framework pro remote procedure calls, což je ideální pro management rozhraní. Avšak samotné standardy byly nedostatečné pro garantovanou interoperability. Konsorcium WS-I bylo vytvořeno hlavními průmyslovými subjekty za účelem vytvoření těchto potřebných implementačních profilů. Normativním odkazováním na WS-I Basic Profiles mohlo 3GPP využívat tuto již existující, průmyslově validovanou práci, zajišťující, že rozhraní webových služeb definované pro OAM funkce budou od počátku fungovat spolehlivě v prostředí více výrobců.

Tento přístup řešil omezení předchozích proprietárních nebo méně strukturovaných management protokolů (jako některé CORBA-based nebo SNMP-based řešení, které měly své vlastní interoperability problémy). Poskytoval jasný, testovatelný set požadavků na shodu. Motivací bylo snížení operačních nákladů (OPEX) umožněním plug-and-play integrace síťových elementů do management systémů, facilitace rychlejšího nasazení služeb a podpora vize více automatizované a flexibilní síťové infrastruktury, jak je vyžadována pro následující koncepty jako Network Functions Virtualization (NFV) a Software-Defined Networking (SDN).

## Klíčové vlastnosti

- Definuje požadavky na shodu pro implementace SOAP 1.1 a WSDL 1.1
- Specifikuje použití HTTP 1.1 jako transportního binding pro webové služby
- Nařizuje WS-I Basic Profile pro document/literal style messaging
- Poskytuje pokyny pro konstrukci interoperabilních dokumentů WSDL
- Definuje pravidla pro strukturu SOAP envelope, zpracování header a reportování faults
- Obsahuje testovací nástroje a vzorové aplikace pro validaci shody s profilem

## Související pojmy

- [SOAP – Simple Object Access Protocol](/mobilnisite/slovnik/soap/)
- [WSDL – Web Services Description Language](/mobilnisite/slovnik/wsdl/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)

## Definující specifikace

- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 32.306** (Rel-19) — Configuration Management Notification IRP Solution Set
- **TS 32.307** (Rel-9) — Notification IRP SOAP Solution Set
- **TS 32.316** (Rel-19) — Generic IRP Management Solution Set Definitions
- **TS 32.317** (Rel-9) — Generic IRP management SOAP Solution Set
- **TS 32.607** (Rel-9) — CM IRP SOAP Solution Set Mapping
- **TS 32.667** (Rel-9) — Kernel CM IRP SOAP Solution Set

---

📖 **Anglický originál a plná specifikace:** [WS-I na 3GPP Explorer](https://3gpp-explorer.com/glossary/ws-i/)
