---
slug: "mdea"
url: "/mobilnisite/slovnik/mdea/"
type: "slovnik"
title: "MDEA – MCData Emergency Alert"
date: 2025-01-01
abbr: "MDEA"
fullName: "MCData Emergency Alert"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mdea/"
summary: "MDEA je služba kritická pro plnění úkolu, která oprávněným orgánům umožňuje vysílat naléhavá upozornění cílené skupině uživatelů služby MCData. Je součástí architektury MCX podle 3GPP a zajišťuje spol"
---

MDEA (výstraha pro nouzové situace služby MCData) je služba kritická pro plnění úkolu v rámci architektury MCX podle 3GPP, která oprávněným orgánům umožňuje vysílat naléhavá upozornění cílené skupině uživatelů služby MCData pro účely veřejné bezpečnosti.

## Popis

MCData Emergency Alert (MDEA) je standardizovaná služba v rámci sady služeb Mission Critical Services ([MCX](/mobilnisite/slovnik/mcx/)) podle 3GPP, konkrétně pod hlavičkou Mission Critical Data (MCData) definované od vydání 16. Poskytuje mechanismy pro oprávněný personál (např. velitele zásahu, orgány veřejné bezpečnosti) k vytváření a rozesílání časově citlivých nouzových upozornění definované skupině uživatelů nebo skupin služby MCData. Služba je navržena tak, aby zaručila doručení i v přetížených nebo degradovaných síťových podmínkách, a to využitím mechanismů kvality služeb (QoS) a priority podkladové sítě LTE nebo 5G.

Funkcionalita MDEA je realizována prostřednictvím sady logických funkcí a referenčních bodů, jak je specifikováno v TS 24.282 (MCData fáze 3) a TS 37.579 (testování shody). Mezi klíčové komponenty patří klient MDEA, který sídlí na uživatelském zařízení (UE), a server MDEA, který je typicky součástí infrastruktury systému MCData. Proces vytvoření upozornění zahrnuje oprávněného uživatele, který sestaví zprávu upozornění; ta může obsahovat text, předdefinované šablony, geografické cílové oblasti, úrovně závažnosti a požadavky na potvrzení. Tento požadavek je odeslán prostřednictvím servisní vrstvy MCData na server MDEA, který následně spravuje distribuci.

Server využívá funkce správy skupin a distribuce k identifikaci cílových příjemců na základě kritérií upozornění, jako je členství ve skupině, poloha nebo role. Poté zahájí doručení pomocí spolehlivých transportních protokolů s explicitními prioritami. Upozornění jsou zasílána na klientská zařízení, kde spouštějí výrazná vizuální a sluchová oznámení, aby zajistila okamžitou pozornost uživatele. Architektura podporuje end-to-end šifrování pro zabezpečení a zahrnuje mechanismy pro hlášení stavu doručení a potvrzení od uživatele, což umožňuje původci sledovat dosah a účinnost upozornění. Tento end-to-end proces je integrován s jádrovou architekturou MCData a sdílí společné prvky, jako je správa identit, správa skupin a zabezpečení, čímž zajišťuje soudržný ekosystém služeb kritických pro plnění úkolu.

## K čemu slouží

MDEA byla vytvořena, aby vyřešila kritickou mezeru v komunikacích pro veřejnou bezpečnost: potřebu standardizované, síťové schopnosti hromadného varování pro uživatele služeb kritických pro plnění úkolu. Před její standardizací byla nouzová upozornění často doručována prostřednictvím různorodých systémů, jako jsou sirény, televizní vysílání nebo proprietární rádiové pagingy, kterým chyběla přesnost cílení, potvrzení o doručení a integrace s moderními datovými službami používanými záchranáři. Vývoj MDEA v rámci architektury [MCX](/mobilnisite/slovnik/mcx/) podle 3GPP byl motivován globálním úsilím o využití komerčních sítí LTE/5G pro veřejnou bezpečnost, což vyžadovalo funkční paritu s tradičními systémy pozemní mobilní rádiové komunikace ([LMR](/mobilnisite/slovnik/lmr/)).

Tato technologie řeší problém rychlého sdělení naléhavých informací o situačním povědomí (např. únik nebezpečných látek, lokalizace aktivního střelce, evakuační rozkazy) dynamické skupině zasahujících osob v terénu. Její vytvoření bylo motivováno poznatky z velkých katastrof, kde poruchy komunikace bránily záchranným pracím. MDEA poskytuje digitální, IP-based systém varování, který lze integrovat s dalšími službami MCX, jako je mission-critical push-to-talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) a mission-critical video ([MCVideo](/mobilnisite/slovnik/mcvideo/)), čímž vytváří jednotnou platformu velení a řízení.

MDEA navíc využívá inherentní výhody sítí 3GPP, jako je široké geografické pokrytí, vysoká přenosová kapacita pro bohatá upozornění a sofistikované ekosystémy zařízení. Odstraňuje omezení předchozích přístupů tím, že nabízí detailní cílení (podle skupiny, polohy nebo role), povinné prioritní zacházení se síťovými prostředky a zaručené potvrzení o doručení. To zajišťuje, že kritické informace spolehlivě a promptně dorazí ke správnému personálu, čímž se zlepšuje operační koordinace a bezpečnost zasahujících osob během mimořádných událostí.

## Klíčové vlastnosti

- Oprávněné vytváření a vysílání nouzových upozornění cíleným skupinám uživatelů služby MCData
- Podpora bohatého obsahu upozornění včetně textu, předdefinovaných šablon a geografických cílových oblastí
- Zaručené doručení s vysokou prioritou využitím QoS mechanismů podkladové sítě 3GPP
- End-to-end zabezpečení včetně šifrování a ochrany integrity zpráv upozornění
- Hlášení stavu doručení a mechanismy povinného/nepovinného potvrzení od příjemce
- Integrace s širší architekturou služby MCData pro správu identit, skupin a zabezpečení

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MDEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdea/)
