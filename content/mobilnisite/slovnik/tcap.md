---
slug: "tcap"
url: "/mobilnisite/slovnik/tcap/"
type: "slovnik"
title: "TCAP – Transaction Capabilities Application Part"
date: 2025-01-01
abbr: "TCAP"
fullName: "Transaction Capabilities Application Part"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tcap/"
summary: "TCAP je signalizační protokol používaný v sítích SS7 a SIGTRAN k usnadnění transakčně orientované, bezspojové komunikace mezi síťovými uzly. Umožňuje výměnu informací nesouvisejících s přepojováním ok"
---

TCAP (Transaction Capabilities Application Part) je signalizační protokol, který umožňuje transakčně orientovanou komunikaci pro informace nesouvisející s přepojováním okruhů, jako jsou databázové dotazy a služby inteligentní sítě.

## Popis

Transaction Capabilities Application Part (TCAP) je protokol vrstvy 4 v rámci zásobníku protokolů signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)), který pracuje nad Signaling Connection Control Part ([SCCP](/mobilnisite/slovnik/sccp/)). Jeho hlavní funkcí je podpora výměny transakčně založených, bezspojových zpráv mezi aplikacemi v různých síťových uzlech bez nutnosti trvalého koncově-koncového signalizačního spojení. 'Transakce' v terminologii TCAP je krátkodobý dialog skládající se z požadavku a jedné či více odpovědí. TCAP poskytuje strukturovaný způsob zabalení dat aplikační úrovně, správy dialogu a zpracování chyb.

TCAP funguje pomocí struktury založené na komponentách. Aplikace vyvolá operaci (např. dotaz) odesláním zprávy TCAP obsahující jednu nebo více komponent. Klíčové typy komponent jsou: Invoke (pro vyžádání operace), Return Result (pro poskytnutí úspěšné odpovědi), Return Error (pro indikaci selhání) a Reject (pro indikaci chyby protokolu). Tyto komponenty jsou svázány do zprávy TCAP, která je sama zapouzdřena ve zprávě SCCP Unitdata ([UDT](/mobilnisite/slovnik/udt/)) pro směrování v síti. TCAP spravuje transakci pomocí jedinečného Transaction ID, což mu umožňuje korelovat požadavky a odpovědi. Protokol definuje dvě podvrstvy: Component Sub-layer, která zpracovává jednotlivé operační komponenty, a Transaction Sub-layer, která spravuje celkový dialog mezi dvěma uzly.

V architektuře 3GPP Core Network, zejména v okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) doméně a pro starší signalizaci, je TCAP klíčovým prvkem pro služby inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) a správu mobility. Například když Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) potřebuje dotázat Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) na data účastníka nebo spustit Camel službu pro předplacené účtování, použije protokol Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)). Zprávy MAP jsou přenášeny jako aplikačně specifická data uvnitř komponent TCAP. TCAP tedy slouží jako spolehlivý transportní a dialogový mechanismus pro MAP a další aplikační protokoly, jako je INAP (Intelligent Network Application Part). S vývojem směrem k plně IP sítím je TCAP často přenášen přes IP pomocí adaptačních vrstev SIGTRAN jako je M3UA, čímž si zachovává svou funkčnost v sítích nové generace.

## K čemu slouží

TCAP byl vytvořen k řešení potřeby efektivní signalizace nesouvisející s přepojováním okruhů v telefonních sítích. Tradiční signalizace SS7 (jako ISUP) byla těsně svázána se stavěním a rušením hovorových okruhů. Když sítě zaváděly pokročilé funkce, jako jsou bezplatná čísla, volání na platební kartu a později mobilní roamování, vznikla potřeba, aby uzly komunikovaly pro účely nesouvisející s konkrétní hovorovou cestou – například pro dotazování na centralizovanou databázi. TCAP poskytl standardizovaný, transakčně orientovaný protokol k naplnění této potřeby, oddělující servisní logiku od základního řízení hovoru.

Řešil problém, jak mohou různé síťové aplikace komunikovat strukturovaným způsobem typu požadavek-odpověď bez nutnosti navázat pro každou interakci trvalý signalizační spoj. Před TCAP byla taková funkcionalita ad-hoc nebo vestavěná do jiných protokolů, což omezovalo škálovatelnost a interoperabilitu. Návrh TCAP založený na komponentách a správě dialogu umožnil vývoj robustních služeb inteligentní sítě (IN) a byl zásadní pro úspěch správy mobility v GSM prostřednictvím MAP. Jeho zavedení umožnilo jasné oddělení přepojovací funkce a servisní logiky, což je základním kamenem moderní telekomunikační architektury.

## Klíčové vlastnosti

- Poskytuje bezspojové, transakčně orientované zasílání zpráv pro SS7/SIGTRAN
- Používá strukturu založenou na komponentách (Invoke, Return Result, Return Error, Reject)
- Spravuje dialogy pomocí jedinečných Transaction ID pro korelaci požadavku a odpovědi
- Slouží jako transportní vrstva pro aplikační protokoly jako MAP a INAP
- Podporuje strukturované (konverzační) i nestrukturované (dotaz-odpověď) dialogy
- Může být přenášen přes tradiční SS7 MTP nebo přes IP pomocí SIGTRAN (např. M3UA)

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)
- [INAP – Intelligent Network Application Protocol](/mobilnisite/slovnik/inap/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 49.008** (Rel-19) — BSSAP on E-interface for inter-MSC handover

---

📖 **Anglický originál a plná specifikace:** [TCAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tcap/)
