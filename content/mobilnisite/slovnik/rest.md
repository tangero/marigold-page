---
slug: "rest"
url: "/mobilnisite/slovnik/rest/"
type: "slovnik"
title: "REST – Representational State Transfer"
date: 2026-01-01
abbr: "REST"
fullName: "Representational State Transfer"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rest/"
summary: "REST je architektonický styl pro návrh síťových aplikací, který byl přijat organizací 3GPP pro northbound rozhraní a rozhraní založená na službách. Používá HTTP metody (GET, POST, PUT, DELETE) k opera"
---

REST je architektonický styl pro návrh síťových aplikací, který 3GPP využívá pro rozhraní založená na službách, aby umožnil flexibilní a webově přívětivá API prostřednictvím HTTP metod operujících na zdrojích identifikovaných pomocí URI.

## Popis

Representational State Transfer (REST) je architektonický styl, nikoli samotný protokol, který řídí návrh webových služeb. Byl formálně přijat organizací 3GPP počínaje Release 12 pro definici aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)), zejména pro northbound rozhraní (NBI) a později pro rozhraní založená na službách uvnitř 5G jádra sítě. RESTful API v 3GPP jsou typicky implementována pomocí [HTTP](/mobilnisite/slovnik/http/)/1.1 nebo HTTP/2 s datovými částmi ve formátu [JSON](/mobilnisite/slovnik/json/) nebo [XML](/mobilnisite/slovnik/xml/) a poskytují standardizovaný způsob pro interakci externích aplikací (Application Functions, [AF](/mobilnisite/slovnik/af/)) nebo interních síťových funkcí (Network Functions, [NF](/mobilnisite/slovnik/nf/)) s telekomunikační sítí.

V architektonickém stylu REST je vše modelováno jako zdroj, což je jakákoli informace, která může být pojmenována (např. relace účastníka, pravidlo politiky, instance síťového řezu). Každý zdroj je jednoznačně identifikovatelný prostřednictvím jednotného identifikátoru zdroje ([URI](/mobilnisite/slovnik/uri/)). Klienti s těmito zdroji interagují pomocí jednotné sady bezstavových operací, primárně standardních HTTP metod: GET pro získání reprezentace zdroje, POST pro vytvoření nového zdroje, PUT pro aktualizaci nebo nahrazení zdroje, DELETE pro odstranění zdroje a PATCH pro částečné aktualizace. Reprezentace zdroje (např. ve formátu JSON) obsahuje jeho stav nebo atributy. Odpovědi serveru jsou také bezstavové a mohou obsahovat hypertextové odkazy (princip [HATEOAS](/mobilnisite/slovnik/hateoas/)) pro označení možných následných akcí nebo souvisejících zdrojů, ačkoli to je v 3GPP specifikacích implementováno různě.

V rámci architektury 3GPP jsou RESTful principy aplikovány v několika klíčových oblastech. Funkce pro zpřístupnění schopností služeb (SCEF) v 4G a funkce pro zpřístupnění sítě (NEF) v 5G poskytují RESTful northbound API pro bezpečné zpřístupnění síťových schopností a informací autorizovaným aplikacím třetích stran. Dále je architektura 5G jádra sítě postavena kolem architektury založené na službách (SBA), kde základní síťové funkce (jako AMF, SMF, PCF) vzájemně komunikují pomocí rozhraní založených na službách. Tato rozhraní jsou často specifikována jako RESTful API s transportem přes HTTP/2, což umožňuje flexibilní, škálovatelnou a objevitelnou interakci mezi síťovými funkcemi. To představuje kontrast s dřívějšími protokolovými rozhraními typu point-to-point (jako Diameter) a nabízí výhody v jednoduchosti vývoje, podpoře nástrojů a souladu s cloud-nativními principy.

## K čemu slouží

3GPP přijalo REST, aby vyřešilo potřebu otevřenějších, flexibilnějších a pro vývojáře přívětivějších rozhraní pro interakci s telekomunikačními sítěmi. Tradiční telekomunikační rozhraní byla založena na komplexních binárních protokolech (jako MAP, Diameter), které bylo pro webové a IT vývojáře obtížné používat, což brzdilo inovace a tvorbu služeb. Vzestup cloud computingu a webových služeb si vyžádal posun k IT-přívětivějším technologiím.

Motivace pro zavedení REST v 3GPP byla mnohostranná. Cílem bylo zjednodušit integraci aplikací třetích stran (např. od poskytovatelů IoT služeb, podnikových zákazníků) se síťovými schopnostmi prostřednictvím standardizovaných API založených na HTTP. Toto zpřístupnění vytváří nové zdroje příjmů. Interně, pro 5G SBA, RESTful rozhraní umožňují více oddělené, škálovatelné a agilní jádro sítě, kde mohou být funkce vyvíjeny, nasazovány a škálovány nezávisle, což je v souladu s cloud-nativními principy a principy mikroslužeb. REST řeší problémy s komplexitou protokolů, závislostí na dodavateli a pomalým nasazováním služeb využitím široce známých webových standardů, rozsáhlého ekosystému nástrojů a umožněním rychlejších vývojových cyklů jak pro síťové operátory, tak pro vývojáře aplikací.

## Klíčové vlastnosti

- Architektura orientovaná na zdroje, kde jsou síťové entity modelovány jako zdroje
- Jednotné rozhraní využívající standardní HTTP metody (GET, POST, PUT, DELETE, PATCH)
- Bezstavové interakce klient-server pro škálovatelnost
- Zdroje identifikované a adresované pomocí URI
- Výměna dat ve standardních formátech, jako je JSON nebo XML
- Využívá všudypřítomné webové protokoly (HTTP/TLS) pro transport

## Související pojmy

- [HTTP – Hypertext Transfer Protocol](/mobilnisite/slovnik/http/)
- [JSON – JavaScript Object Notation](/mobilnisite/slovnik/json/)

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 28.890** (Rel-16) — ONAP-3GPP 5G Management Compatibility Study
- **TS 29.116** (Rel-19) — REST-based protocol for xMB reference point
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.201** (Rel-19) — RESTful Rx Interface for AF-PC Communication
- **TS 29.222** (Rel-19) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 29.501** (Rel-19) — 5GC SBI API Design Principles & Guidelines
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.530** (Rel-19) — AF AI/ML Services Stage 3 Protocol
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications
- **TS 29.817** (Rel-12) — Study on XML-based Rx interface for PCC
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- **TS 29.891** (Rel-16) — CT4 Aspects of 5G System Phase 1
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [REST na 3GPP Explorer](https://3gpp-explorer.com/glossary/rest/)
