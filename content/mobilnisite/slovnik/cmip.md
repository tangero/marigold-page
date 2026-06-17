---
slug: "cmip"
url: "/mobilnisite/slovnik/cmip/"
type: "slovnik"
title: "CMIP – Common Management Information Protocol"
date: 2025-01-01
abbr: "CMIP"
fullName: "Common Management Information Protocol"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/cmip/"
summary: "CMIP je OSI protokol pro správu sítí, který umožňuje standardizovanou komunikaci mezi managementovými systémy a síťovými prvky. Poskytuje robustní rámec pro správu chyb, konfigurace, účtování, výkonu"
---

CMIP je síťový managementový protokol OSI, který umožňuje standardizovanou komunikaci pro FCAPS management mezi managementovými systémy a síťovými prvky pomocí strukturovaného objektově orientovaného modelu.

## Popis

Common Management Information Protocol (CMIP) je [OSI](/mobilnisite/slovnik/osi/) (Open Systems Interconnection) protokol standardizovaný pro telekomunikace a správu sítí. Funguje v rámci OSI managementového rámce a definuje model klient-server, kde manažer (klient) komunikuje s agenty (servery) umístěnými na spravovaných síťových prvcích. CMIP využívá spojově orientovanou transportní službu, typicky přes zásobník protokolů OSI, aby zajistil spolehlivé doručení managementových operací a notifikací. Hlavní síla protokolu spočívá v jeho sofistikovaném informačním modelu, který je založen na spravovaných objektech definovaných pomocí Guidelines for the Definition of Managed Objects ([GDMO](/mobilnisite/slovnik/gdmo/)). Každý spravovaný objekt reprezentuje zdroj uvnitř síťového prvku, jako je port, okruh nebo softwarový proces, a má atributy, akce, které může provádět, a notifikace, které může vysílat.

Komunikace v CMIP je usnadněna sadou servisních primitiv. Manažer může vyvolat operace jako M-GET pro získání hodnot atributů, M-SET pro jejich změnu, M-ACTION pro vyžádání provedení specifické funkce objektem, M-CREATE pro vytvoření nových spravovaných objektů a M-DELETE pro jejich odstranění. Agent může při detekci významných událostí, jako jsou poruchy nebo překročení prahových hodnot, asynchronně odeslat manažerovi notifikace (M-EVENT-REPORT). Tyto interakce jsou rozsahově a filtračně vymezeny, což umožňuje, aby jediný požadavek cílil na více spravovaných objektů na základě složitých kritérií, což snižuje síťový provoz ve srovnání s jednoduššími protokoly vyžadujícími individuální dotazy na každý atribut.

Architektura CMIP je vysoce strukturovaná a objektově orientovaná, což podporuje interoperabilitu mezi více-dodavatelskými managementovými systémy a síťovými prvky. Její komplexní sada služeb podporuje všechny aspekty modelu managementu FCAPS (Fault, Configuration, Accounting, Performance, Security). Přestože je výkonný, je CMIP také komplexní a vyžaduje značné procesní zdroje a plně implementovaný OSI zásobník. V kontextech 3GPP byl historicky specifikován pro určitá managementová rozhraní, zejména v raných verzích pro správu síťových prvků, před širším průmyslovým přechodem k internetovým managementovým protokolům, jako jsou SNMP a NETCONF/YANG, pro mnohé aplikace.

## K čemu slouží

CMIP byl vytvořen, aby řešil potřebu standardizovaného, robustního a komplexního protokolu pro správu složitých telekomunikačních sítí, které byly stále více více-dodavatelské a vyžadovaly interoperabilitu. Před jeho vývojem byly standardem proprietární managementové systémy, což vedlo k závislosti na dodavateli, vysokým nákladům na integraci a provozní neefektivitě. [OSI](/mobilnisite/slovnik/osi/) managementový rámec s CMIP jako svým protokolem měl za cíl poskytnout univerzální řešení založené na otevřených mezinárodních standardech, umožňující bezproblémovou správu různých typů síťových zařízení od různých výrobců.

Protokol byl navržen tak, aby řešil omezení jednodušších managementových nástrojů, kterým chyběla podrobnost, spolehlivost a sofistikované datové modelování potřebné pro rozsáhlé, kritické telekomunikační sítě. Spojově orientovaná povaha CMIP zajišťovala spolehlivé doručení kritických managementových příkazů a alarmů. Jeho výkonné schopnosti vymezení rozsahu a filtrování umožňovaly efektivní hromadné operace, což snižovalo režii správy v síti. Objektově orientovaný informační model ([GDMO](/mobilnisite/slovnik/gdmo/)) poskytoval formální, rozšiřitelný způsob reprezentace jakéhokoli síťového zdroje, což činilo systém připraveným na budoucnost a schopným spravovat nové technologie při jejich vzniku.

V rámci ekosystému 3GPP byl CMIP přijat pro splnění požadavků na standardizovaná rozhraní pro provoz, správu a údržbu (OAM), zejména v raných verzích pro správu prvků core sítě a rádiové přístupové sítě. Poskytoval potřebnou přísnost a strukturu pro složité úlohy správy v mobilních sítích 2G a 3G, podporoval detailní monitorování výkonu, správu chyb a řízení konfigurace, jak bylo definováno ve specifikacích 3GPP pro správu sítě.

## Klíčové vlastnosti

- Objektově orientovaný managementový model využívající GDMO pro definici spravovaných objektů
- Spojově orientovaný protokol zajišťující spolehlivou managementovou komunikaci
- Komplexní sada operací: M-GET, M-SET, M-ACTION, M-CREATE, M-DELETE
- Asynchronní hlášení událostí (M-EVENT-REPORT) pro alarmy a notifikace
- Výkonné vymezení rozsahu a filtrování pro provádění operací na více objektech jediným požadavkem
- Plná podpora modelu managementu FCAPS (Fault, Configuration, Accounting, Performance, Security)

## Související pojmy

- [GDMO – Guidelines for the Definition of Managed Objects](/mobilnisite/slovnik/gdmo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.154** (Rel-19) — Backward Compatibility for 3GPP IRP Specifications
- **TS 32.352** (Rel-19) — Communication Surveillance IRP Information Service
- **TS 32.722** (Rel-11) — Repeater NRM IRP: Network Resource Model
- **TS 32.824** (Rel-9) — SOA and IRP Gap Analysis
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study
- **TS 32.866** (Rel-15) — REST, HTTP, JSON for Management Interfaces

---

📖 **Anglický originál a plná specifikace:** [CMIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmip/)
