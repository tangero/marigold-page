---
slug: "naptr"
url: "/mobilnisite/slovnik/naptr/"
type: "slovnik"
title: "NAPTR – Naming Authority Pointer"
date: 2025-01-01
abbr: "NAPTR"
fullName: "Naming Authority Pointer"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/naptr/"
summary: "NAPTR je záznam DNS používaný pro dynamickou delegaci a vyhledávání služeb, který umožňuje mapování doménových jmen na URI nebo jiná doménová jména na základě pravidel. V 3GPP je využíván pro ENUM (ma"
---

NAPTR je záznam DNS (Domain Name System) používaný pro dynamickou delegaci a vyhledávání služeb, který umožňuje mapování doménových jmen na URI a je využíván v 3GPP pro ENUM a výběr služeb IMS, například směrování SIP hovorů.

## Popis

Záznam NAPTR (Naming Authority Pointer) je typ záznamu [DNS](/mobilnisite/slovnik/dns/) definovaný v [RFC](/mobilnisite/slovnik/rfc/) 3403. Poskytuje mechanismus pro přepis doménových jmen na [URI](/mobilnisite/slovnik/uri/) nebo jiná doménová jména prostřednictvím sady uspořádaných pravidel. Každý záznam NAPTR obsahuje několik polí: pořadí (order), preference (preference), příznaky (flags), služby (services), regulární výraz (regexp) a náhrada (replacement). Pole pořadí určuje sekvenci zpracování záznamů, zatímco preference umožňuje vyrovnávání zátěže mezi záznamy stejného pořadí. Příznaky označují další krok po přepisu (např. 'S' pro vyhledání SRV, 'A' pro vyhledání A/AAAA, 'U' pro URI). Pole služby specifikuje použitelný protokol a službu (např. 'E2U+sip' pro [SIP](/mobilnisite/slovnik/sip/) [ENUM](/mobilnisite/slovnik/enum/)). Pole regexp obsahuje vzor regulárního výrazu pro přepis vstupního řetězce a pole replacement poskytuje doménové jméno pro další dotazy DNS, pokud není použit regulární výraz. V 3GPP se NAPTR primárně používá v IP Multimedia Subsystem (IMS) pro ENUM dotazy, kde jsou telefonní čísla E.164 převedena na SIP URI dotazem na DNS pomocí domény odvozené z čísla. To umožňuje mezispolečnostní směrování a vyhledávání služeb. Proces zahrnuje iterativní dotazy DNS: nejprve dotaz NAPTR vrátí záznamy s parametry služeb; na základě příznaků jsou následně provedeny dotazy SRV nebo A/AAAA pro rozlišení skutečného koncového bodu. Tento flexibilní mechanismus podporuje dynamický výběr služeb a vyjednávání protokolu, což je klíčové pro interoperabilitu IMS a poskytování multimediálních služeb.

## K čemu slouží

NAPTR byl v 3GPP přijat pro řešení potřeby flexibilního a dynamického vyhledávání služeb a směrování v plně IP sítích, zejména v rámci IMS. Když telekomunikace přešly na SIP-based multimediální služby, vznikla potřeba efektivně mapovat telefonní čísla (E.164) na IP adresy ([URI](/mobilnisite/slovnik/uri/)). Tradiční statické směrování nebo pevně zakódovaná mapování byla nedostatečná pro škálovatelná prostředí s více dodavateli. NAPTR jako součást architektury [DNS](/mobilnisite/slovnik/dns/) poskytuje standardizovaný způsob, jak toto mapování provádět pomocí DNS dotazů, což umožňuje operátorům delegovat autoritu a konfigurovat složitá směrovací pravidla. Řeší problémy spojené s přenositelností čísel, výběrem služeb (např. volba mezi [SIP](/mobilnisite/slovnik/sip/), tel nebo jinými protokoly) a vyrovnáváním zátěže mezi více servery. Jeho použití v ENUM usnadňuje globální propojení VoIP a IMS sítí a nahrazuje starší směrování v okruhově komutovaných sítích vyhledáváním založeným na DNS.

## Klíčové vlastnosti

- Záznam DNS pro dynamickou delegaci a vyhledávání služeb
- Podporuje uspořádané a preferenční zpracování pravidel pro směrování
- Umožňuje ENUM (mapování E.164 na URI) pro IMS a VoIP
- Integruje se se záznamy SRV a A/AAAA pro rozlišení koncového bodu
- Umožňuje přepis doménových jmen na základě regulárních výrazů
- Umožňuje vyjednávání protokolu a služeb prostřednictvím příznaků

## Související pojmy

- [ENUM – E.164 telephone NUmber Mapping](/mobilnisite/slovnik/enum/)
- [DNS – Directory Name Service](/mobilnisite/slovnik/dns/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.819** (Rel-13) — Diameter Base Protocol Update Analysis
- **TS 34.229** (Rel-19) — IMS SIP/SDP UE Conformance Testing for 5GS

---

📖 **Anglický originál a plná specifikace:** [NAPTR na 3GPP Explorer](https://3gpp-explorer.com/glossary/naptr/)
