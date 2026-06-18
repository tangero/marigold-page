---
slug: "mcvideo"
url: "/mobilnisite/slovnik/mcvideo/"
type: "slovnik"
title: "MCVideo – Mission Critical Video"
date: 2026-01-01
abbr: "MCVideo"
fullName: "Mission Critical Video"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mcvideo/"
summary: "Služba 3GPP poskytující komunikaci reálného času pomocí videa pro scénáře s kritickými požadavky, jako je ochrana obyvatelstva a zásahy při mimořádných událostech. Zavedená ve vydání Rel-14 zajišťuje"
---

MCVideo je služba pro mise s kritickými požadavky (mission-critical) zavedená konsorciem 3GPP ve vydání Release-14, která poskytuje spolehlivou, nízkolatenční a prioritizovanou komunikaci reálného času pomocí videa přes mobilní sítě pro scénáře ochrany obyvatelstva a zásahů při mimořádných událostech.

## Popis

Mission Critical Video (MCVideo) je standardizovaná služba v rámci architektury 3GPP, která umožňuje komunikaci reálného času pomocí videa pro operace s kritickými požadavky, jako jsou ty, které provádějí složky integrovaného záchranného systému, první respondenti a průmyslové týmy. Funguje tak, že mezi uživateli nebo skupinami vytváří videos relace přes sítě LTE nebo 5G a využívá architekturu Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), aby zajistila vysokou spolehlivost, nízkou latenci a prioritní přístup. Architektura zahrnuje klíčové komponenty, jako je MCVideo klient na uživatelském zařízení, který zachycuje a kóduje video streamy, a MCVideo server v síti, který spravuje řízení relací, distribuci médií a interoperabilitu s dalšími službami pro mise s kritickými požadavky, jako jsou [MCPTT](/mobilnisite/slovnik/mcptt/) a MCData. Služba funguje ve spolupráci se základními síťovými funkcemi, jako je Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), k vynucení politik QoS, což zajišťuje, že video provoz obdrží vyšší prioritu než komerční provoz během mimořádných událostí. Jejím úkolem v síti je poskytovat bezpečnou a odolnou platformu pro video komunikaci, která podporuje funkce jako skupinové video hovory, video push-to-talk a integraci se službami určování polohy, což umožňuje lepší přehled o situaci. MCVideo využívá protokoly jako [SIP](/mobilnisite/slovnik/sip/) pro signalizaci a [RTP](/mobilnisite/slovnik/rtp/) pro přenos médií, s rozšířeními pro požadavky specifické pro mise, jako je přechod na úzkopásmové sítě nebo provoz v izolovaných prostředích. Standardizací této služby 3GPP usnadňuje interoperabilitu mezi různými dodavateli a sítěmi, což je klíčové pro efektivní spolupráci mezi různými složkami během kritických incidentů.

## K čemu slouží

MCVideo bylo vytvořeno ve vydání Rel-14, aby zaplnilo mezeru v standardizované video komunikaci pro scénáře s kritickými požadavky, kde stávající spotřebitelské video služby postrádaly spolehlivost, zabezpečení a prioritizaci potřebnou pro zásahy při mimořádných událostech. Před jeho zavedením organizace ochrany obyvatelstva často spoléhaly na proprietární video systémy nebo adaptované komerční řešení, které trpěly problémy s interoperabilitou, nekonzistentním výkonem při síťové zátěži a nedostatečnou integrací s hlasovými a datovými službami. Vývoj MCVideo byl motivován rostoucím využíváním videa v oblastech, jako je vymáhání práva, hasičství a řízení katastrof, kde vizuální informace v reálném čase mohou výrazně zlepšit rozhodování a koordinaci. Řeší problémy související s odolností sítě začleněním funkcí, jako je prioritizace QoS, kontinuita služby během předávání spojení a podpora pro degradované síťové podmínky. Historicky, když 3GPP rozšiřovalo svůj portfoli služeb pro mise s kritickými požadavky od [MCPTT](/mobilnisite/slovnik/mcptt/) (hlas) ve vydání Rel-13 tak, aby zahrnovalo data a video, představovalo MCVideo přirozenou evoluci směrem k poskytnutí komplexní sady komunikačních služeb. Odstraňuje omezení předchozích přístupů tím, že zajišťuje, aby video služby byly postaveny na stejné robustní architektuře jako ostatní komponenty pro mise s kritickými požadavky, což umožňuje bezproblémovou interoperabilitu a zvýšenou bezpečnost pro uživatele v prostředích s vysokými nároky.

## Klíčové vlastnosti

- Streamování videa v reálném čase s nízkou latencí a vysokou spolehlivostí
- Integrace se službami pro mise s kritickými požadavky (MCPTT, MCData) pro jednotnou komunikaci
- Prioritizace QoS přes mobilní sítě využitím síťového řezání (network slicing) nebo vyhrazených přenosových kanálů (dedicated bearers)
- Podpora skupinových video hovorů a funkce video push-to-talk
- Vylepšení zabezpečení včetně šifrování a autentizace
- Interoperabilita se staršími systémy a standardy ochrany obyvatelstva

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 23.281** (Rel-20) — MCVideo Functional Architecture and Flows
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MCVideo na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcvideo/)
