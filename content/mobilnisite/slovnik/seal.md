---
slug: "seal"
url: "/mobilnisite/slovnik/seal/"
type: "slovnik"
title: "SEAL – Service Enabler Architecture Layer for Verticals"
date: 2026-01-01
abbr: "SEAL"
fullName: "Service Enabler Architecture Layer for Verticals"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/seal/"
summary: "SEAL je standardizovaná vrstva aplikačních schopností podle 3GPP, která poskytuje společné zprostředkovatele pro vertikální aplikace (např. V2X, IoT, drony). Abstrahuje složitost podkladové sítě a nab"
---

SEAL je standardizovaná vrstva aplikačních schopností (service capability layer) podle 3GPP, která poskytuje společné zprostředkovatele (enablers) a API pro vertikální aplikace tím, že abstrahuje složitost podkladové sítě, aby urychlila vývoj a zajistila interoperabilitu.

## Popis

Service Enabler Architecture Layer for Verticals (SEAL) je komplexní architektura definovaná 3GPP pro usnadnění vývoje a nasazení služeb pro různé průmyslové vertikály, jako je automobilový průmysl ([V2X](/mobilnisite/slovnik/v2x/)), IoT, drony a průmyslová automatizace. Nejde o jedinou síťovou funkci, ale o vrstvenou architekturu sestávající ze souboru společných zprostředkovatelů služeb, které zpřístupňují standardizovaná aplikační rozhraní ([API](/mobilnisite/slovnik/api/)) vertikálním aplikacím. SEAL se nachází nad funkcemi jádra sítě a abstrahuje podkladové schopnosti sítě 3GPP, čímž poskytuje jednotné a zjednodušené rozhraní pro vývojáře služeb. Klíčové komponenty architektury SEAL zahrnují zprostředkovatele pro správu skupin, správu konfigurace, správu identit, správu polohy, správu síťových zdrojů a funkci SEAL Data Delivery ([SEALDD](/mobilnisite/slovnik/sealdd/)). Tito zprostředkovatelé spolupracují; například zprostředkovatel správy skupin umožňuje aplikaci definovat logickou skupinu uživatelských zařízení (UE) (například všechny drony ve flotile) a zprostředkovatel správy polohy pak může poskytnout pozice všech členů této skupiny. SEAL funguje tak, že přijímá požadavky od vertikálních aplikací prostřednictvím svých northbound API a následně orchestruje potřebné interakce s funkcemi sítě 3GPP (jako jsou [NEF](/mobilnisite/slovnik/nef/), [UDM](/mobilnisite/slovnik/udm/), [GMLC](/mobilnisite/slovnik/gmlc/)) nebo s dalšími zprostředkovateli SEAL, aby požadavek splnil. Zpracovává aspekty jako autorizaci služeb, vynucování politik a transformaci dat. Jeho úlohou je fungovat jako middleware, který skrývá heterogenitu a složitost síťových rozhraní, což umožňuje vertikálám rychle inovovat bez nutnosti hlubokých znalostí telekomunikací, a zároveň zajišťuje efektivní, bezpečné a spolehlivé využívání síťových prostředků 3GPP.

## K čemu slouží

SEAL byl vytvořen v 3GPP Release 16, aby řešil kritickou mezeru v ekosystému 5G: obtížnost, se kterou se vertikální průmysl potýká při využívání pokročilých schopností sítí 3GPP. Před zavedením SEAL musely vertikály realizovat komplexní, bodově propojené integrace s různými síťovými funkcemi (např. [NEF](/mobilnisite/slovnik/nef/), [SCEF](/mobilnisite/slovnik/scef/)), což vedlo k fragmentovaným, neinteroperabilním řešením a pomalému uvedení na trh. Růst vertikálně specifických architektur (například pro V2X) také hrozil vytvořením izolovaných řešení. Primárním účelem SEAL je poskytnout jednotnou, standardizovanou a znovupoužitelnou vrstvu společných zprostředkovatelů služeb, která je agnostická vůči konkrétním vertikálám. Tím řeší problémy integrační složitosti, nedostatku interoperability a redundantního vývoje. Tím, že nabízí konzistentní sadu API pro běžné potřeby, jako je skupinová komunikace, lokalizace a správa zařízení, SEAL výrazně snižuje vstupní bariéru pro poskytovatele vertikálních aplikací. Byl motivován vizí 5G umožnit širokou škálu služeb nad rámec mobilního širokopásmového přístupu, aby byla síť efektivně zpřístupněna a monetizována, a zároveň aby vertikály dostaly nástroje potřebné k vytváření škálovatelných a spolehlivých služeb.

## Klíčové vlastnosti

- Poskytuje standardizovanou sadu northbound API pro využití vertikálními aplikacemi
- Zahrnuje zprostředkovatele pro správu skupin, identit, polohy a konfigurace
- Abstrahuje podkladové síťové funkce 3GPP (NEF, UDM, PCF, GMLC)
- Podporuje více vertikálních domén (V2X, IoT, UAV, průmysl) pomocí společné architektury
- Umožňuje efektivní zpřístupnění síťových zdrojů a vynucování politik pro vertikální služby
- Usnadňuje interoperabilitu služeb a snižuje integrační složitost pro vývojáře

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [SEALDD – Service Enabler Architecture Layer – Data Delivery](/mobilnisite/slovnik/sealdd/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.438** (Rel-20) — SEAL Digital Asset Service for Metaverse
- **TS 23.482** (Rel-20) — AIML Enablement Service Architecture
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.486** (Rel-19) — V2X Application Enabler (VAE) Protocol Spec
- **TS 24.538** (Rel-19) — MSGin5G Service Protocol Specification
- **TS 24.542** (Rel-19) — SEAL Notification Management Protocol
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 24.544** (Rel-19) — SEAL Group Management Protocol
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [SEAL na 3GPP Explorer](https://3gpp-explorer.com/glossary/seal/)
