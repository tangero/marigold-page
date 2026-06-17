---
slug: "eas"
url: "/mobilnisite/slovnik/eas/"
type: "slovnik"
title: "EAS – Enterprise Application Server"
date: 2026-01-01
abbr: "EAS"
fullName: "Enterprise Application Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eas/"
summary: "Enterprise Application Server (EAS) je síťová funkce, která hostuje a provádí podnikové aplikace v rámci systému 5G. Umožňuje podnikům nasazovat vlastní služby blízko svých uživatelů a využívat síťové"
---

EAS je síťová funkce, která hostuje a provádí podnikové aplikace v rámci systému 5G, aby umožnila poskytování vlastních služeb v blízkosti uživatelů.

## Popis

Enterprise Application Server (EAS) je klíčová architektonická komponenta zavedená ve specifikaci 3GPP Release 15 jako součást podpory systému 5G pro vertikální odvětví a podnikové služby. Jedná se v podstatě o server nebo platformu umístěnou v prostorách podniku nebo na síťové hraně (edge), která hostuje aplikační logiku a služby šité na míru konkrétním obchodním potřebám. EAS komunikuje se síťovým jádrem 5G prostřednictvím standardizovaných rozhraní, což mu umožňuje využívat síťové schopnosti, jako je kvalita služeb (QoS), lokalizační služby a informace o stavu sítě. Jeho architektura je navržena flexibilně a podporuje nasazení v privátních sítích 5G, ve vyhrazených řezech (slices) veřejné sítě nebo v hybridních modelech.

Fungování EAS zahrnuje několik klíčových komponent a procedur. EAS se registruje v síťovém jádru 5G, konkrétně u funkce Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)), čímž se jeho služby stanou zjistitelné pro autorizované koncové zařízení (UE) a další síťové funkce. Když UE potřebuje přístup k podnikové aplikaci, síťové jádro 5G může směrovat provoz na příslušný EAS na základě politik, uživatelského předplatného a požadavků aplikace. EAS může také prostřednictvím NEF žádat o síťové schopnosti, například aby vyvolal změny QoS nebo získal informace o poloze UE, což umožňuje kontextově citlivé aplikace. Komunikaci mezi UE a EAS lze optimalizovat pro nízkou latenci nasazením EAS na hraně sítě, blízko koncových uživatelů.

Role EAS v síti spočívá v překlenutí mezery mezi obecnou mobilní konektivitou a specializovanými podnikovými aplikacemi. Umožňuje podnikům přesáhnout pouhou konektivitu a nabízet integrované služby využívající vlastní schopnosti systému 5G. Například v továrně může EAS hostovat aplikaci pro řízení strojů v reálném čase, která vyžaduje ultra-spolehlivou komunikaci s nízkou latencí (URLLC) a přístup k datům ze senzorů na provozní hale. EAS může komunikovat se sítí, aby zajistil potřebnou QoS pro řídicí provoz. Také umožňuje kontinuitu služeb a mobilitu, protože UE může udržovat relaci s EAS i při pohybu mezi různými přístupovými body v rámci podnikové domény.

## K čemu slouží

Enterprise Application Server byl vytvořen jako odpověď na rostoucí poptávku průmyslových odvětví po vlastních výkonných aplikacích využívajících schopnosti sítě 5G. Před jeho zavedením byly podnikové služby přes mobilní sítě často omezeny na základní konektivitu nebo spoléhaly na aplikace typu "over-the-top" ([OTT](/mobilnisite/slovnik/ott/)), které nebyly přímo integrovány se sítí. Tento přístup neumožňoval garantovat výkon, využívat síťovou inteligenci nebo nabízet bezproblémovou mobilitu v podnikovém prostředí. Vzestup konceptů Průmysl 4.0, chytrých továren a privátních sítí zdůraznil potřebu standardizovaného způsobu hostování podnikových aplikací v rámci síťové architektury.

Hlavní problémy, které EAS řeší, zahrnují umožnění edge computingu s nízkou latencí pro podnikové aplikace, poskytování bezpečného a izolovaného prostředí pro služby a možnost pro podniky řídit a spravovat své vlastní služby. Hostováním aplikací blíže koncovým uživatelům (na hraně sítě) EAS snižuje latenci a provoz na páteřní síti, což je klíčové pro aplikace v reálném čase, jako je rozšířená realita, průmyslová automatizace a autonomní vozidla. Také řeší omezení univerzálních síťových služeb tím, že umožňuje vertikálním odvětvím nasazovat aplikace na míru, které mohou přímo komunikovat se síťovými funkcemi 5G prostřednictvím vystavených [API](/mobilnisite/slovnik/api/).

Historicky vychází motivace pro EAS z práce 3GPP na síťových řezech (network slicing) a edge computingu, která položila základy pro vlastní síťové služby. EAS poskytuje prvek pro hostování aplikací, který dokončuje vizi komplexních síťových řezů pro podniky. Umožňuje operátorům nabízet nejen řezy pro konektivitu, ale také platformy pro přidanou hodnotu jako službu. To vytváří nové obchodní modely a umožňuje podnikům nasazovat vlastní iniciativy digitální transformace na spolehlivém a výkonném základě 5G bez nutnosti vše stavět od nuly.

## Klíčové vlastnosti

- Hostuje aplikační logiku a služby specifické pro podnik v rámci sítě 5G
- Integruje se s jádrem 5G prostřednictvím NEF a NRF pro zjišťování služeb a zpřístupňování schopností
- Podporuje nasazení na hraně sítě (edge) pro přístup k aplikacím s nízkou latencí
- Může žádat o síťové schopnosti, jako je vynucování QoS nebo lokalizační služby
- Umožňuje kontinuitu služeb a mobilitu v rámci podnikových domén
- Umožňuje scénáře privátních sítí a síťových řezů (slicing) pro vertikální odvětví

## Související pojmy

- [EASDF – Edge Application Server Discovery Function](/mobilnisite/slovnik/easdf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.548** (Rel-19) — 5G System Edge Computing Enhancements
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.748** (Rel-17) — Edge Computing Enhancement Study for 5GC
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 24.558** (Rel-19) — Edge Enabler APIs Stage 3
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- … a dalších 23 specifikací

---

📖 **Anglický originál a plná specifikace:** [EAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/eas/)
