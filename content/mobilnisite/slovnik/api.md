---
slug: "api"
url: "/mobilnisite/slovnik/api/"
type: "slovnik"
title: "API – Application Programming Interface"
date: 2026-01-01
abbr: "API"
fullName: "Application Programming Interface"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/api/"
summary: "Standardizovaná sada definic a protokolů pro vytváření a integraci softwarových aplikací v systémech 3GPP. Umožňuje vystavování služeb, interakci síťových funkcí a přístup třetích stran a tvoří základ"
---

API je standardizovaná sada definic a protokolů pro vytváření a integraci softwarových aplikací v systémech 3GPP, která umožňuje vystavování služeb, interakci síťových funkcí a přístup třetích stran.

## Popis

V kontextu standardů 3GPP je aplikační programové rozhraní (Application Programming Interface – API) formálně specifikované rozhraní, které definuje, jak spolu mohou interagovat různé softwarové komponenty, síťové funkce nebo externí aplikace. Poskytuje smlouvu, která specifikuje metody komunikace, včetně datových formátů (požadavky a odpovědi), operací, které lze vyvolat, a podkladových protokolů (často RESTful [HTTP](/mobilnisite/slovnik/http/) nebo gRPC). API abstrahují složitou vnitřní implementaci síťových funkcí a vystavují dobře definované schopnosti jako znovupoužitelné služby. Tato abstrakce je zásadní pro architektury založené na službách (service-based architectures – [SBA](/mobilnisite/slovnik/sba/)) přijaté v 5G Core (5GC), kde síťové funkce (Network Functions – NFs) jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) a [UDM](/mobilnisite/slovnik/udm/) interagují prostřednictvím rozhraní založených na službách, což jsou v podstatě sady standardizovaných API.

Architektura API 3GPP je podrobně dokumentována v technických specifikacích, které detailně popisují vše od [URL](/mobilnisite/slovnik/url/) adres koncových bodů API a HTTP metod (GET, POST, PUT, DELETE) až po přesné schéma [JSON](/mobilnisite/slovnik/json/) nebo [XML](/mobilnisite/slovnik/xml/) pro vyměňované zprávy. Klíčové komponenty zahrnují producenta API (síťovou funkci, která hostuje a implementuje API), konzumenta API (entitu, která API vyvolává) a vrstvu správy API, která může řešit aspekty jako autentizace, autorizace, omezení rychlosti (rate limiting) a analytika. API jsou často popisována pomocí strojově čitelných formátů, jako je OpenAPI Specification (OAS), což umožňuje automatizovanou generaci kódu a validaci. Fungují přes rozhraní založené na službách (Service-Based Interface – SBI) uvnitř 5G Core, využívají pro přenos HTTP/2 a pro serializaci datové části JSON, čímž zajišťují efektivní a flexibilní komunikaci.

Role API v síti je mnohostranná. Interně umožňují modulární, oddělený návrh základní sítě, což operátorům dovoluje nasazovat a upgradovat síťové funkce nezávisle. Externě jsou mechanismem pro vystavování služeb, umožňujícím autorizovaným poskytovatelům aplikací třetích stran (např. v podnikových, IoT nebo edge computing scénářích) přistupovat k síťovým schopnostem, jako je správa kvality služeb (quality of service – QoS), informace o poloze nebo stav sítě, kontrolovaným způsobem prostřednictvím frameworků jako je Network Exposure Function (NEF). API jsou také klíčová pro správu a orchestraci sítě, umožňují automatizované poskytování, konfiguraci a správu životního cyklu síťových zdrojů jako součást širších frameworků, jako je ETSI NFV-MANO. V konečném důsledku API transformují síť ze statické infrastruktury na programovatelnou platformu, což podporuje inovace a vytváření nových služeb.

## K čemu slouží

Standardizace API v rámci 3GPP byla motivována potřebou odklonu od monolitických, dodavatelům specifických síťových architektur směrem k otevřeným, interoperabilním a softwarově řízeným systémům. Před rozšířeným přijetím API spolu síťové funkce komunikovaly prostřednictvím rigidních, bod-bod, protokolově specifických rozhraní (často založených na binárních protokolech jako SS7 nebo Diameter), což činilo integraci složitou, zpomalovalo inovace a vytvářelo závislost na dodavateli. Účelem definice společných API je tyto problémy řešit stanovením univerzálního 'jazyka' pro komunikaci softwarových komponent, čímž se umožní interoperabilita mezi více dodavateli, rychlejší nasazování služeb a síťová agilita.

Historicky koncept získal významnou podporu s nástupem webových technologií a cloud-native principů. Přechod na plně IP sítě a poptávka po programovatelnosti ve stylu internetu vedly 3GPP k přijetí RESTful API a architektur založených na službách, zejména od 4G Evolved Packet Core (EPC) pro některá rozhraní a plně v 5G Core. API řeší omezení předchozích 'uzavřených' systémů tím, že poskytují standardizovanou, dobře dokumentovanou a často na HTTP založenou metodu interakce, která je známá obrovskému ekosystému vývojářů softwaru. To snižuje bariéru vstupu pro inovace a umožňuje jak síťovým operátorům, tak externím vývojářům vytvářet nové aplikace a služby, které využívají jedinečné schopnosti mobilních sítí, jako je nízká latence, vysoká přenosová kapacita a podpora mobility.

Navíc jsou API nezbytná pro umožnění klíčových paradigmat 5G, jako je síťové dělení (network slicing), edge computing a massive IoT. Poskytují potřebné háčky pro orchestrační systémy, aby na požádání instancovaly a spravovaly end-to-end síťové řezy. Umožňují edge aplikacím žádat o specifické síťové zacházení. Stručně řečeno, API existují proto, aby transformovaly telekomunikační sítě na otevřené platformy, řeší problémy složité integrace, provozní rigidity a omezené inovace služeb, a tím odemykají plný ekonomický a technologický potenciál systémů 3GPP.

## Klíčové vlastnosti

- Standardizovaná rozhraní založená na službách pro komunikaci mezi síťovými funkcemi (např. Nnrf, Nsmf)
- Návrh podle principů RESTful s využitím HTTP/2 a JSON pro datovou část
- Strojově čitelná definice prostřednictvím OpenAPI Specification (OAS) 3.0
- Podpora vystavování síťových schopností třetím stranám prostřednictvím NEF
- Umožňuje správu životního cyklu a orchestraci síťového dělení (network slicing)
- Usnadňuje cloud-native nasazení síťových funkcí založené na mikroslužbách

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.127** (Rel-9) — Open Service Access (OSA) Requirements
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- … a dalších 75 specifikací

---

📖 **Anglický originál a plná specifikace:** [API na 3GPP Explorer](https://3gpp-explorer.com/glossary/api/)
