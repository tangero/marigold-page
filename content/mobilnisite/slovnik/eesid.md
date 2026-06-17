---
slug: "eesid"
url: "/mobilnisite/slovnik/eesid/"
type: "slovnik"
title: "EESID – Edge Enabler Server Identification"
date: 2026-01-01
abbr: "EESID"
fullName: "Edge Enabler Server Identification"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eesid/"
summary: "Edge Enabler Server Identification (EESID) je jedinečný identifikátor instance serveru Edge Enablement Server (EES) v systému edge computingu 3GPP. Síťové funkce a klienti jej používají k jednoznačném"
---

EESID je jedinečný identifikátor instance serveru Edge Enablement Server používaný v rámci edge computingu 3GPP pro směrování požadavků na zjišťování služeb a správu relací.

## Popis

Edge Enabler Server Identification (EESID) je klíčový parametr v architektuře edge computingu 3GPP, který poskytuje globálně nebo lokálně jedinečný štítek pro instanci serveru Edge Enablement Server. Funguje jako síťová adresa nebo název pro entitu [EES](/mobilnisite/slovnik/ees/) samotnou, odlišně od služeb, které hostuje. EESID se používá v různých signalizačních zprávách a servisních operacích k identifikaci zdrojového nebo cílového EES. Například když se Edge Application Server ([EAS](/mobilnisite/slovnik/eas/)) zaregistruje u EES, registrace je asociována s EESID tohoto EES. Podobně, když Edge Configuration Server ([ECS](/mobilnisite/slovnik/ecs/)) poskytuje konfiguraci UE, může zahrnovat EESID EES, který má UE kontaktovat pro zjišťování služeb.

Struktura a formát EESID jsou definovány tak, aby zajistily jeho směrovatelnost v rámci edge ekosystému. Typicky následuje hierarchickou konvenci pojmenování, která může zahrnovat domény pro usnadnění rozlišení. V žádostech o zjišťování služeb od Edge Application Client ([EAC](/mobilnisite/slovnik/eac/)) lze EESID použít k určení preferovaného nebo předem nakonfigurovaného EES. Síť na základě politik a polohy UE může také vybrat vhodný EES a poskytnout jeho EESID klientovi. Během událostí mobility, pokud se UE přesune do oblasti obsluhované jiným EES, může být UE poskytnut nový EESID pro zajištění kontinuity zjišťování edge služeb.

Z protokolového hlediska je EESID přenášen v hlavičkách [HTTP](/mobilnisite/slovnik/http/) nebo v rámci [JSON](/mobilnisite/slovnik/json/) datových částí zpráv rozhraní založených na službách (např. v [API](/mobilnisite/slovnik/api/) Ees_Service definovaném v TS 29.558). Jeho přítomnost umožňuje sofistikované síťové chování, jako je výběr EES na základě vyrovnávání zátěže, geografické příslušnosti nebo specifických smluv o úrovni služeb. Je to základní prvek, který umožňuje škálovatelnost edge architektury, umožňuje nasazení více instancí EES bez konfliktů a zajišťuje správné vymezení registrací a zjišťování služeb.

## K čemu slouží

EESID byl definován k řešení problému adresování a identifikace v multi-vendorovém, multi-doménovém prostředí edge computingu. S tím, jak se edge nasazení škálují, bude operátor nebo federace operátorů nasazovat četné instance [EES](/mobilnisite/slovnik/ees/). Bez standardizovaného, jedinečného identifikátoru by nebylo možné spolehlivě nasměrovat registraci EAS na konkrétní EES nebo navést UE ke správnému EES pro zjišťování služeb. Tento identifikátor předchází nejednoznačnosti a zajišťuje integritu registru služeb.

Řeší omezení pouhého použití IP adres nebo FQDN tím, že poskytuje logický identifikátor, který je stabilní a může být prostřednictvím rozlišovacích mechanismů mapován na různé fyzické nebo síťové lokace. To je obzvláště důležité pro mobilitu a redundanci; pokud EES selže, jeho funkce mohou převzát záložní instance s jinou síťovou adresou, ale potenciálně s příbuznou logickou identitou, a klienti nakonfigurovaní s EESID mohou být přesměrováni. EESID také umožňuje administrativní a provozní segregaci, což umožňuje jasně rozlišit různé EES (např. jeden pro veřejné edge služby a jeden pro privátní podnikový edge) v rámci stejné sítě.

V podstatě EESID poskytuje nezbytný prostředek pro síť, aby mohla spravovat životní cyklus a dostupnost serveru Edge Enablement Server, který je centrálním nervovým systémem pro orchestraci edge služeb. Je to klíčová komponenta, která činí architekturu edge computingu robustní, spravovatelnou a škálovatelnou.

## Klíčové vlastnosti

- Globálně nebo lokálně jedinečný identifikátor pro instanci EES
- Používá se pro směrování žádostí o registraci a zjišťování služeb
- Umožňuje výběr EES a vyrovnávání zátěže ze strany sítě
- Podporuje procedury mobility UE a opětovného výběru EES
- Přenášen v zprávách rozhraní založených na službách (SBI)
- Umožňuje nasazení více EES a administrativní domény

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [EESID na 3GPP Explorer](https://3gpp-explorer.com/glossary/eesid/)
