---
slug: "ees"
url: "/mobilnisite/slovnik/ees/"
type: "slovnik"
title: "EES – Edge Enablement Server"
date: 2026-01-01
abbr: "EES"
fullName: "Edge Enablement Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ees/"
summary: "Edge Enablement Server (EES) je funkční entita v architektuře Edge Computingu 3GPP, která poskytuje registraci služeb, jejich vyhledávání a správu konektivity pro Edge aplikace (EAs) a klienty edge ap"
---

EES je funkční entita v edge computingu 3GPP, která poskytuje registraci služeb, jejich vyhledávání a správu konektivity pro aplikace a klienty, aby mohli využívat služby s nízkou latencí na okraji sítě.

## Popis

Edge Enablement Server (EES) je základní síťová funkce definovaná v rámci frameworku Edge Computingu ([EC](/mobilnisite/slovnik/ec/)) 3GPP, konkrétně pro architekturu založenou na službách (service-based architecture). Funguje jako registr služeb a zprostředkovatel konektivity, který se logicky nachází mezi klienty edge aplikací (EACs) – typicky běžícími na uživatelském zařízení (UE) – a servery edge aplikací (EASs), které hostují vlastní aplikační logiku na okraji sítě. EES je zodpovědný za správu životního cyklu registrací služeb [EAS](/mobilnisite/slovnik/eas/). EAS se u EES registruje se svým servisním profilem, schopnostmi a umístěním (např. spojeným s konkrétní Edge Data Network). Tato registrace zahrnuje metadata jako [API](/mobilnisite/slovnik/api/) endpointy služby, podporované protokoly a geografická nebo síťová topologická omezení.

Když [EAC](/mobilnisite/slovnik/eac/) potřebuje objevit edge službu, odešle žádost o vyhledání služby, často prostřednictvím své obslužné sítě (např. přes Edge Configuration Server nebo [ECS](/mobilnisite/slovnik/ecs/)), která je směrována na příslušný EES. EES tuto žádost zpracovává na základě kontextu EAC (jako je jeho umístění, síťové podmínky a předplatné) a registrovaných servisních profilů dostupných EAS. Provede výběr služby a vrátí EAC seznam vhodných endpointů EAS. EES typicky nezpracovává samotný uživatelský provoz (user plane traffic); místo toho usnadňuje navázání přímého nebo optimalizovaného datového spojení mezi EAC a vybraným EAS.

Architektura zahrnuje několik klíčových referenčních bodů. EES vystavuje northbound API (např. Ees_Service) pro registraci EAS a vyhledání EAC. Komunikuje s Edge Configuration Serverem (ECS), aby poskytoval informace o EAS pro konfiguraci UE. Pro mobilitu a kontinuitu relace může EES komunikovat s funkcí Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) 5G Core sítě, aby ovlivnil směrovací politiky provozu ([URSP](/mobilnisite/slovnik/ursp/)) nebo byl informován o událostech mobility UE. To umožňuje EES doporučit převýběr EAS, pokud se UE přesune, a zajistit tak nepřetržitou službu s nízkou latencí. Jeho role je klíčová v abstrakci složitosti distribuované edge topologie od aplikací a poskytuje jednotný mechanismus pro vyhledávání služeb napříč různými síťmi operátorů a edge lokalitami.

## K čemu slouží

EES byl vytvořen, aby řešil základní výzvu vyhledávání a dostupnosti služeb v distribuovaném prostředí edge computingu. Tradiční cloud computing spoléhá na centralizované, dobře známé domény, ale edge computing rozptyluje aplikační servery do mnoha lokalit blíže uživatelům. Bez mechanismu vyhledávání nemohou klienti dynamicky najít nejbližší nebo nejoptimálnější instanci služby, což ruší výhody edge computingu v podobě nízké latence a vysoké propustnosti. EES to řeší poskytováním standardizovaného, síťově integrovaného registru služeb.

Jeho vývoj motivoval vzestup aplikací citlivých na latenci a náročných na data, jako jsou autonomní vozidla, průmyslový IoT a imerzivní média, které vyžadují, aby výpočetní zdroje byly geograficky blízko koncového uživatele. Předchozí přístupy, jako použití DNS nebo proprietárních protokolů pro vyhledávání, nebyly integrovány se znalostí mobilní sítě o poloze uživatele, stavu mobility a síťových podmínkách. EES jako součást standardu 3GPP umožňuje síťovému operátorovi řídit a optimalizovat vystavování edge služeb, což umožňuje nové obchodní modely jako Network as a Service (NaaS) a monetizaci edge služeb.

Dále řeší problém vázanosti na dodavatele nebo aplikaci tím, že poskytuje standardizované rozhraní (definované např. ve specifikaci TS 23.558) pro registraci a vyhledávání služeb. To umožňuje poskytovatelům aplikací z různých odvětví nasadit své EAS na edge platformách operátorů nebo třetích stran a mít je bezproblémově objevovány autorizovanými klienty, což podporuje ekosystém edge služeb. Je klíčovým prvkem pro naplnění vize federovaného edge, kde lze služby objevovat napříč administrativními doménami.

## Klíčové vlastnosti

- Centralizovaný registr služeb pro servery edge aplikací (EAS)
- Kontextově-aware vyhledávání služeb pro klienty edge aplikací (EAC)
- Integrace s 5G Core pro správu politik a mobility (prostřednictvím NEF/SMF)
- Podpora správy servisního profilu EAS (schopnosti, umístění, API)
- Umožňuje ovlivňování směrování provozu UE prostřednictvím URSP
- Umožňuje federaci edge služeb napříč různými sítěmi nebo poskytovateli

## Definující specifikace

- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.548** (Rel-19) — 5G System Edge Computing Enhancements
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 24.558** (Rel-19) — Edge Enabler APIs Stage 3
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 28.815** (Rel-17) — Charging Study for Edge Computing
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [EES na 3GPP Explorer](https://3gpp-explorer.com/glossary/ees/)
