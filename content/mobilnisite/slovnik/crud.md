---
slug: "crud"
url: "/mobilnisite/slovnik/crud/"
type: "slovnik"
title: "CRUD – Create, Read, Update, Delete"
date: 2026-01-01
abbr: "CRUD"
fullName: "Create, Read, Update, Delete"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/crud/"
summary: "CRUD označuje čtyři základní operace manipulace s daty používané v 3GPP správě sítě a vystavování služeb. Tyto operace tvoří základ pro správu síťových prostředků, dat účastníků a parametrů služeb pro"
---

CRUD je soubor čtyř základních datových operací (Create, Read, Update, Delete) používaných v 3GPP pro správu síťových prostředků, dat účastníků a parametrů služeb prostřednictvím standardizovaných API.

## Popis

CRUD operace představují základní primitiva pro manipulaci s daty standardizovaná napříč rozhraními pro správu a vystavování služeb v 3GPP. V architektuře 3GPP jsou tyto operace implementovány prostřednictvím RESTful [API](/mobilnisite/slovnik/api/) využívajících metody [HTTP](/mobilnisite/slovnik/http/) (POST pro Create, GET pro Read, PUT/PATCH pro Update, DELETE pro Delete), jak je specifikováno v TS 29.501 a dalších specifikacích služebních rozhraní. Operace pracují na spravovaných objektech a prostředcích definovaných ve specifikacích 3GPP, které mohou zahrnovat instance síťových funkcí, profily účastníků, pravidla politik, parametry služeb a šablony síťových řezů.

Každá CRUD operace dodržuje specifické protokoly a datové formáty definované ve specifikacích 3GPP. Operace Create typicky zahrnují odeslání datové části [JSON](/mobilnisite/slovnik/json/) nebo [XML](/mobilnisite/slovnik/xml/) obsahující počáteční stav prostředku na specifický koncový bod, přičemž systém vrátí jedinečný identifikátor vytvořeného prostředku. Operace Read získávají aktuální stavy prostředků a podporují různé parametry dotazu pro filtrování, stránkování a selektivní získávání atributů. Operace Update modifikují existující prostředky, přičemž PUT typicky nahrazuje celý prostředek a PATCH aplikuje částečné změny. Operace Delete odstraňují prostředky ze systému, často s kaskádovými efekty na závislé prostředky.

Implementace CRUD operací v 3GPP sítích zahrnuje několik klíčových komponent včetně Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)) pro objevování služeb, Service Communication Proxy ([SCP](/mobilnisite/slovnik/scp/)) pro směrování a různých síťových funkcí vystavujících rozhraní pro správu. Tyto operace jsou zabezpečeny prostřednictvím mechanismů autentizace, autorizace a šifrování specifikovaných v bezpečnostních standardech 3GPP. Operace podporují idempotenci tam, kde je to vhodné (zejména pro operace Create a Update), aby bylo zajištěno spolehlivé fungování v distribuovaných systémech, kde mohou být požadavky retransmitovány.

CRUD operace hrají klíčovou roli v služební architektuře 3GPP tím, že poskytují konzistentní paradigma pro interakci síťových funkcí. Umožňují automatizované zřizování, správu konfigurace a monitorování síťových prostředků v reálném čase. Operace jsou nedílnou součástí síťového řezování, kde instance řezů, instance podsítí a přidružené prostředky jsou spravovány prostřednictvím CRUD operací na šablonách a instancích řezů. Také tvoří základ pro schopnosti vystavování, umožňující aplikacím třetích stran interagovat se síťovými funkcemi prostřednictvím standardizovaných API při zachování správné kontroly přístupu a vynucování politik.

## K čemu slouží

CRUD operace byly ve 3GPP standardizovány, aby řešily rostoucí složitost správy sítě v systémech 5G a novějších. Jak se sítě vyvíjely z monolitických architektur do cloud-nativních, na mikroslužbách založených návrhů, vznikla potřeba standardizovaných, programových rozhraní pro správu prostředků. Tradiční přístupy správy využívající proprietární protokoly a manuální konfiguraci nemohly škálovat tak, aby splňovaly požadavky dynamického síťového řezování, virtualizace síťových funkcí a automatizovaných požadavků orchestrace sítí 5G.

Zavedení CRUD operací ve vydání 15 vyřešilo několik klíčových problémů. Za prvé poskytlo konzistentní paradigma správy napříč různými síťovými funkcemi a doménami, čímž snížilo složitost integrace a umožnilo interoperabilní systémy správy. Za druhé umožnilo automatizaci poskytnutím rozhraní vhodných pro strojové zpracování, která mohou být využívána orchestračními systémy, platformami [OSS](/mobilnisite/slovnik/oss/)/[BSS](/mobilnisite/slovnik/bss/) a aplikacemi pro správu sítě. Za třetí podpořilo dynamickou povahu sítí 5G, kde musí být prostředky často vytvářeny, modifikovány a mazány, aby vyhověly měnícím se požadavkům služeb a stavům sítě.

Předchozí přístupy v sítích 3GPP se silně spoléhaly na dodavatelsky specifická rozhraní a protokoly pro správu, které bránily multi-vendorové interoperabilitě a automatizaci. Standardizace CRUD operací prostřednictvím RESTful API sjednotila 3GPP s osvědčenými postupy v cloud computingu a webových službách, což usnadnilo integraci telekomunikačních sítí s IT systémy a cloudovými platformami. Tento přístup také usnadnil adopci DevOps praktik v síťových operacích, umožňujících průběžnou integraci a nasazování síťových funkcí a služeb.

## Klíčové vlastnosti

- Standardizované operace RESTful API využívající metody HTTP
- Podpora datových formátů JSON a XML pro reprezentaci prostředků
- Komplexní zpracování chyb se standardizovanými kódy a zprávami
- Podpora parametrů dotazu včetně filtrování, stránkování a výběru atributů
- Idempotentní operace pro spolehlivé chování distribuovaných systémů
- Integrace s autentizačním a autorizačním rámcem 3GPP

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 28.111** (Rel-19) — Fault Management Service Specification
- **TR 28.836** (Rel-18) — Technical Report on Intent Driven Management
- **TS 28.871** (Rel-19) — Study on Service Based Management Architecture enhancement phase 3
- **TS 29.501** (Rel-19) — 5GC SBI API Design Principles & Guidelines
- **TS 29.891** (Rel-16) — CT4 Aspects of 5G System Phase 1
- **TS 32.158** (Rel-20) — Management and Orchestration REST Solution Sets

---

📖 **Anglický originál a plná specifikace:** [CRUD na 3GPP Explorer](https://3gpp-explorer.com/glossary/crud/)
