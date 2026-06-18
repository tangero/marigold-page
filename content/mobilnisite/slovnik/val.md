---
slug: "val"
url: "/mobilnisite/slovnik/val/"
type: "slovnik"
title: "VAL – Vertical Application Layer"
date: 2026-01-01
abbr: "VAL"
fullName: "Vertical Application Layer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/val/"
summary: "Služební vrstva definovaná 3GPP, která poskytuje standardizovaný rámec pro aplikace vertikálních odvětví (např. automatizace výroby, distribuce elektřiny) pro propojení se sítěmi 5G. Nabízí API specif"
---

VAL je služební vrstva definovaná 3GPP, která poskytuje standardizovaný rámec s API a datovými modely specifickými pro vertikály (odvětví) pro propojení průmyslových aplikací s funkcemi 5G sítě a jejich využívání.

## Popis

Vertikální aplikační vrstva (VAL) je komplexní služební architektura specifikovaná 3GPP, primárně v dokumentu TS 23.434 a souvisejících specifikacích. Je navržena jako mezivrstva, která stojí mezi aplikacemi vertikálních odvětví (klienty) a funkcemi pro vystavení sítě 3GPP (jako je [NEF](/mobilnisite/slovnik/nef/)) nebo službami datové sítě. VAL poskytuje abstrakci základních schopností sítě 5G, správy dat a služeb správy zařízení specifickou pro vertikály. Její architektura typicky zahrnuje VAL Server, VAL Klienty (uvnitř vertikálních zařízení/senzorů) a VAL Management System.

Jádrem funkcionality VAL je správa služeb vertikální aplikační vrstvy (VAL Services). VAL Service je logická entita reprezentující sadu schopností nabízených vertikální aplikaci, jako je skupinová správa zařízení, hlášení a odběr dat, doručování příkazů nebo sledování polohy. VAL definuje standardizované datové modely (např. pro senzory, aktuátory, roboty) a komunikační procedury využívající RESTful [API](/mobilnisite/slovnik/api/), často s použitím [HTTP](/mobilnisite/slovnik/http/)/2 nebo MQTT. Mezi klíčové komponenty patří VAL Service Management Function, která spravuje životní cyklus (vytvoření, aktualizace, smazání) VAL Services; VAL Configuration Management, která konfiguruje parametry pro VAL Klienty; a VAL Data Management, která spravuje ukládání, agregaci a vystavení dat shromážděných z vertikálních zařízení.

Jak to funguje: Vertikální aplikace, například řídicí systém továrny, komunikuje přes svá API se VAL Serverem, aby vytvořila VAL Service, například službu 'Robot Fleet Management Service'. VAL Server následně nakonfiguruje příslušné VAL Klienty (software na robotech) parametry služby. Roboti (VAL Klienti) používají protokoly VAL k registraci, hlášení telemetrických dat (jako je poloha, stav) a přijímání příkazů od aplikace prostřednictvím VAL Serveru. VAL vrstva zajišťuje překlad mezi záměrem aplikace a potřebnými síťovými akcemi. Zásadní je, že může komunikovat s funkcí pro vystavení sítě (NEF) jádra 5G, aby vyžádala síťové schopnosti, jako jsou záruky QoS pro konkrétní skupinu robotů, nebo aktivaci síťového řezu (network slice) přizpůsobeného pro danou továrnu. To umožňuje, aby byla vertikální aplikace z velké části nezávislá na konkrétních detailech implementace sítě 3GPP, a přitom mohla využívat pokročilé funkce 5G.

## K čemu slouží

VAL byla vytvořena, aby řešila klíčovou výzvu integrace různorodých a specializovaných aplikací vertikálních odvětví s obecným systémem 5G. Předchozí generace mobilních sítí byly primárně navrženy pro komunikaci zaměřenou na člověka (hlas, internet). Slib 5G služeb pro vertikály, jako je Průmysl 4.0, chytré sítě a zdravotnictví, přinesl novou sadu požadavků: ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), komunikaci pro hromadné strojové připojení (mMTC) a přesnou kontrolu síťových zdrojů. Bez standardizované aplikační vrstvy by si každé vertikální odvětví muselo vyvíjet vlastní, proprietární integrace s jádrem 5G, což by vedlo ke složitosti, vysokým nákladům a nedostatku interoperability.

Motivací pro VAL ve verzi Rel-16 bylo poskytnout vertikálům společný, standardizovaný 3GPP 'vjezd' do sítě 5G. Řeší problém fragmentace tím, že nabízí jednotnou sadu [API](/mobilnisite/slovnik/api/) a datových modelů pro vertikály a chrání je před složitostí podkladové sítě. To umožňuje poskytovatelům vertikálních aplikací vyvíjet jednou a nasazovat u různých mobilních operátorů a v různých zemích. VAL také umožňuje síťovým operátorům vystavovat a spravovat pokročilé funkce 5G (např. síťové dělení, edge computing, QoS) pro zákazníky z vertikálních odvětví řízeným, automatizovaným a zúčtovatelným způsobem prostřednictvím dobře definované služební vrstvy. Je to klíčový prvek pro ekosystém 5G business-to-business ([B2B](/mobilnisite/slovnik/b2b/)) a business-to-business-to-consumer (B2B2C), který mění síťové schopnosti na spotřebitelné služby pro průmyslová odvětví.

## Klíčové vlastnosti

- Standardizovaná API a datové modely pro zařízení a aplikace vertikálních odvětví
- Správa životního cyklu služeb vertikální aplikační vrstvy (VAL Services)
- Skupinová správa vertikálních zařízení (vytvoření, úprava, smazání)
- Hlášení dat, odběr a správa ukládání dat z vertikálních odvětví
- Integrace s jádrem 5G pro vystavení síťových schopností (např. prostřednictvím NEF)
- Podpora komunikačních protokolů založených na HTTP/2 i MQTT

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.438** (Rel-20) — SEAL Digital Asset Service for Metaverse
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 24.542** (Rel-19) — SEAL Notification Management Protocol
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 24.545** (Rel-19) — SEAL Location Management Protocol Specification
- **TS 24.547** (Rel-19) — SEAL Identity Management Protocol
- **TS 24.548** (Rel-19) — SEAL Network Resource Management Protocol
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [VAL na 3GPP Explorer](https://3gpp-explorer.com/glossary/val/)
