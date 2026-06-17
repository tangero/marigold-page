---
slug: "gpsi"
url: "/mobilnisite/slovnik/gpsi/"
type: "slovnik"
title: "GPSI – Generic Public Subscription Identifier"
date: 2026-01-01
abbr: "GPSI"
fullName: "Generic Public Subscription Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gpsi/"
summary: "Globálně jednoznačný veřejný identifikátor předplatného 3GPP, například MSISDN nebo externí identifikátor, používaný k adresování uživatele napříč různými síťovými doménami a při komunikaci s externím"
---

GPSI je globálně jednoznačný veřejný identifikátor předplatného 3GPP, například MSISDN, používaný k adresování uživatele napříč různými síťovými doménami a u externích aplikací.

## Popis

Generic Public Subscription Identifier (GPSI) je klíčový identifikátor v systému 5G (5GS) definovaný v 3GPP TS 23.501. Slouží jako veřejná, globálně jednoznačná adresa předplatného, kterou používají externí aplikační funkce ([AF](/mobilnisite/slovnik/af/)) a uvnitř sítě k odkazování na uživatele. Existují dva hlavní formáty: [MSISDN](/mobilnisite/slovnik/msisdn/) (Mobile Subscriber Integrated Services Digital Network Number), což je telefonní číslo ve formátu E.164, a externí identifikátor, což je řetězec ve formátu 'uživatelské_jméno@doména'. GPSI je uloženo v Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) jako součást dat předplatného a je asociováno se SUPI (Subscription Permanent Identifier). Jeho klíčová role spočívá ve vystavování služeb prostřednictvím Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a ve scénářích edge computingu. Když externí AF potřebuje interagovat se sítí pro konkrétního uživatele (např. pro ovlivnění směrování provozu pro aplikace s nízkou latencí), použije v žádostech k NEF GPSI daného uživatele. NEF následně tento veřejný GPSI přeloží na interní SUPI pro síťové operace, čímž zajišťuje soukromí. GPSI se také používá v konfiguraci politiky UE, pro SMS přes [NAS](/mobilnisite/slovnik/nas/) a jako parametr v službách Nnef_. Jeho zpracování zahrnuje přísná opatření na ochranu soukromí; například GPSI se nepoužívá přes rozhraní rádiového přístupu a je mapováno na SUPI uvnitř zabezpečené domény jádra sítě.

## K čemu slouží

GPSI bylo zavedeno v 5GS, aby naplnilo potřebu stabilního, veřejného a uživatelsky přívětivého identifikátoru, který mohou používat poskytovatelé aplikací třetích stran a v rámci síťových služebních [API](/mobilnisite/slovnik/api/), a který odděluje adresování služeb od interních síťových identifikátorů. Předchozí systémy pro tento účel používaly [MSISDN](/mobilnisite/slovnik/msisdn/), což však svazovalo služby s konkrétním číselným formátem (E.164) a bylo méně flexibilní pro netelefonní služby nebo uživatele bez telefonního čísla. GPSI, s podporou jak MSISDN, tak externího identifikátoru (jako je e-mailová adresa), tento problém řeší poskytnutím obecného schématu. To je zásadní pro službami řízenou architekturu 5G a edge computing, kde externí aplikace potřebují konzistentní způsob identifikace účastníků bez nutnosti znát jejich privátní SUPI nebo dočasný [5G-GUTI](/mobilnisite/slovnik/5g-guti/). Řeší omezení používání interních identifikátorů navenek (což představuje riziko pro soukromí a bezpečnost) a nepružnost spoléhání se pouze na MSISDN, což umožňuje nové obchodní modely a bezproblémovou integraci s internetovými službami a federacemi identit.

## Klíčové vlastnosti

- Globálně jednoznačný veřejný identifikátor pro předplatné 3GPP
- Dva formáty: MSISDN (E.164) nebo externí identifikátor (uživatelské_jméno@doména)
- Uloženo v UDM a asociováno s privátním SUPI
- Používáno externími aplikačními funkcemi (AF) prostřednictvím NEF pro služební žádosti
- Klíčový prvek pro vystavování služeb 5G, edge computing a doručování politiky UE
- Chráněno prostřednictvím mapování na SUPI uvnitř sítě za účelem zachování soukromí účastníka

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.540** (Rel-19) — 5G Service Based SMS Stage 2
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.583** (Rel-19) — Application Layer Support for Personal IoT Network
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 28.204** (Rel-18) — Charging management
- **TR 28.840** (Rel-18) — Technical Report
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.504** (Rel-19) — Nudr Service Based Interface Stage 3 Protocol
- … a dalších 31 specifikací

---

📖 **Anglický originál a plná specifikace:** [GPSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/gpsi/)
