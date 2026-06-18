---
slug: "capif"
url: "/mobilnisite/slovnik/capif/"
type: "slovnik"
title: "CAPIF – Common API Framework"
date: 2026-01-01
abbr: "CAPIF"
fullName: "Common API Framework"
category: "Interface"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/capif/"
summary: "CAPIF je standardizovaný rámec pro zpřístupňování schopností sítí 3GPP prostřednictvím northbound API. Poskytuje jednotné, bezpečné a zjistitelné rozhraní pro aplikace a poskytovatele služeb třetích s"
---

CAPIF je standardizovaný rámec pro bezpečné zpřístupňování a správu schopností sítí 3GPP prostřednictvím northbound API třetím stranám (aplikacím a poskytovatelům služeb).

## Popis

Common [API](/mobilnisite/slovnik/api/) Framework (CAPIF) je klíčovým prvkem architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) dle 3GPP, navrženým k poskytnutí jednotné, standardizované a bezpečné metody pro zpřístupnění síťových schopností externím subjektům. Funguje jako vrstva pro správu API, která se nachází mezi síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) jádra 3GPP a externími aplikačními funkcemi ([AF](/mobilnisite/slovnik/af/)) nebo poskytovateli služeb třetích stran. Hlavní úlohou CAPIF je abstrahovat složitost podkladové sítě a nabídnout konzistentní, dobře definovanou a zjistitelnou sadu northbound API. To umožňuje vývojářům vytvářet aplikace využívající síťové schopnosti – jako je řízení kvality služeb (QoS), informace o poloze, stav sítě nebo ověřování uživatele – bez nutnosti hluboké znalosti proprietárních rozhraní nebo interních protokolů sítě. Rámec je postaven na principech RESTful, typicky využívá [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/), což odpovídá moderním postupům webového vývoje pro snadnou adopci.

Z architektonického hlediska je CAPIF založen na několika klíčových logických funkcích. CAPIF Core Function ([CCF](/mobilnisite/slovnik/ccf/)) je centrální entita poskytující služby publikování, zjišťování a registrace API. Spravuje úložiště dostupných API z různých funkcí zpřístupňujících API. API Invoker je klientská entita (např. externí AF), která po řádném ověření a autorizaci zjišťuje a volá API. API Exposing Function ([AEF](/mobilnisite/slovnik/aef/)) je entita hostující a zpřístupňující skutečná API síťových schopností, jako je například Network Exposure Function (NEF) nebo Charging Function. CAPIF Provider Domain představuje administrativní doménu provozující rámec CAPIF, typicky mobilního operátora (MNO). Bezpečnost je zásadní a je řízena funkcí CAPIF Security Function, která zajišťuje ověřování, autorizaci a správu certifikátů pro všechny entity v rámci interakcí v rámci tohoto rámce.

Provoz CAPIF následuje definovaný životní cyklus. Nejprve poskytovatel API (jako je NEF) publikuje podrobnosti svého API rozhraní (definici API, koncové body a podporované operace) do CCF. Externí API Invoker (aplikační server) následně zjistí dostupná API dotazem na CCF. Před voláním se musí API Invoker zaregistrovat v rámci CAPIF a získat potřebné přihlašovací údaje a přístupové tokeny. CCF a Security Function provedou ověření a autorizaci na základě politik, aby zajistily, že volající je oprávněn přistupovat ke konkrétnímu API. Po autorizaci může API Invoker přímo volat API na příslušném AEF. CAPIF také podporuje správu životního cyklu API, včetně verzování a vyřazování, stejně jako logování a účtování za využití API. Tento řízený a bezpečný model brány zabraňuje neoprávněnému přístupu k citlivým síťovým funkcím a zároveň umožňuje kontrolované a zpoplatnitelné zpřístupnění.

Role CAPIF přesahuje pouhé zpřístupnění API; je hybatelem síťové programovatelnosti a otevřených inovací. Poskytnutím jednotného, standardizovaného rámce odstraňuje potřebu bilaterálních, vlastních integrací mezi poskytovateli aplikací a každým MNO. To snižuje vývojový čas a náklady pro třetí strany a umožňuje MNO konzistentně spravovat a monetizovat své síťové prostředky. V kontextu 5G a síťového řezání (network slicing) je CAPIF klíčový pro umožnění vertikálním odvětvím (např. automobilovému průmyslu, výrobě) vyžádat si a spravovat řezy nebo specifické síťové chování pro své aplikace prostřednictvím standardizovaných API. Funguje tedy jako most, který transformuje telekomunikační síť z uzavřeného monolitického systému na otevřenou platformu pro tvorbu služeb.

## K čemu slouží

CAPIF byl vytvořen, aby řešil historickou výzvu „uzavřených zahrad“ (walled gardens) v telekomunikačních sítích. Před jeho zavedením byly síťové schopnosti z velké části nedostupné nebo zpřístupňované prostřednictvím proprietárních, na operátora specifických rozhraní. To ztěžovalo a prodražovalo inovace a tvorbu služeb třetími stranami (vývojáři aplikací a podniky), které by využívaly síťovou inteligenci v reálném čase, jako je poloha uživatele, správa šířky pásma nebo stav připojení. Absence společného rámce vedla k fragmentovaným ekosystémům, duplicitním vývojovým úsilím a zpomalení tempa inovací služeb v mobilní doméně.

Primární problém, který CAPIF řeší, je poskytnutí standardizované, bezpečné a škálovatelné metody pro zpřístupnění sítě (Network Exposure). Jak se 3GPP vyvíjelo směrem k cloud-nativní, na službách založené architektuře (SBA) s 5G, potřeba formalizované expoziční vrstvy se stala kritickou. CAPIF tuto vrstvu poskytuje a definuje společná pravidla, bezpečnostní postupy, mechanismy zjišťování a správu životního cyklu pro všechna northbound API. Tím řeší problém složitosti integrace, což umožňuje aplikaci napsané pro síť jednoho operátora snadněji fungovat v síti jiného, a podporuje tak zdravější ekosystém aplikací.

CAPIF navíc umožňuje nové obchodní modely pro mobilní operátory (MNO). Nabídkou řízené a zpoplatnitelné brány k síťovým schopnostem mohou MNO monetizovat své síťové prostředky nad rámec základní konektivity. Umožňuje vertikálním odvětvím zapojeným do 5G ekonomiky – jako je IoT, automobilový průmysl nebo média – přímo interagovat se sítí za účelem splnění jejich specifických požadavků na nízkou latenci, vysokou spolehlivost nebo masivní připojení zařízení. CAPIF je v podstatě technologickým základem, který umožňuje, aby se síť 3GPP stala skutečnou platformou jako službou (PaaS), což pohání inovace a vytváří nové zdroje příjmů v éře 5G.

## Klíčové vlastnosti

- Standardizované publikování a zjišťování API
- Jednotný rámec pro ověřování a autorizaci
- Správa životního cyklu API (verzování, vyřazování)
- Izolace domény poskytovatele a podpora více domén
- Komplexní podpora logování a účtování
- RESTful architektura s HTTP/2 a JSON

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.433** (Rel-20) — SEAL Data Delivery (SEALDD) for Verticals
- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.438** (Rel-20) — SEAL Digital Asset Service for Metaverse
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.764** (Rel-17) — Study on V2X Application Layer Enhancements
- … a dalších 21 specifikací

---

📖 **Anglický originál a plná specifikace:** [CAPIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/capif/)
