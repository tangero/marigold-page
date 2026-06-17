---
slug: "5gms"
url: "/mobilnisite/slovnik/5gms/"
type: "slovnik"
title: "5GMS – 5G Media Streaming"
date: 2025-01-01
abbr: "5GMS"
fullName: "5G Media Streaming"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/5gms/"
summary: "5GMS je rámec 3GPP pro poskytování služeb streamování médií přes sítě 5G. Definuje standardizovaná rozhraní a funkce pro přípravu, doručování a spotřebu obsahu, což umožňuje efektivní a kvalitní multi"
---

5GMS je rámec 3GPP pro poskytování služeb streamování médií přes sítě 5G, který definuje standardizovaná rozhraní a funkce pro přípravu, doručování a spotřebu obsahu.

## Popis

5G Media Streaming (5GMS) je komplexní servisní rámec 3GPP, který standardizuje doručování mediálního obsahu – včetně živého, na požádání (on-demand) a lineárního streamování – přes sítě 5G. Jeho architektura je postavena kolem dvou hlavních funkčních entit: 5GMS Application Provider (5GMS-AP) a 5GMS Application Function (5GMS-AF). 5GMS-AP je zodpovědný za mediálně orientované operace, jako je příprava obsahu, balení (packaging) a správa práv, a typicky se nachází v aplikační vrstvě. 5GMS-AF, integrovaný v jádru sítě 5G (5G Core), funguje jako zprostředkovatel služeb, který komunikuje s Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) a Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) systému 5G, aby vyžádal a spravoval síťové prostředky (jako je QoS) přizpůsobené pro mediální relace. Toto oddělení umožňuje poskytovatelům obsahu soustředit se na mediální logiku a zároveň využívat standardizované síťové schopnosti pro optimalizaci doručování.

Rámec funguje definicí souboru otevřených [API](/mobilnisite/slovnik/api/), především rozhraní M1, M2, M3, M4 a M5. Rozhraní M1 používá 5GMS-AF k poskytnutí (provisioning) politik pro mediální relace PCF. Rozhraní M2 umožňuje 5GMS-AF požadovat síťovou podporu (např. směrování provozu, QoS) od NEF. Rozhraní M3 je northbound API vystavené 5GMS-AF pro 5GMS-AP, které umožňuje aplikaci žádat o mediálně specifické síťové služby. Rozhraní M4 slouží ke konfiguraci a poskytování mezi řídicími funkcemi. Rozhraní M5 zpracovává řízení a události mediálního přehrávače. Tato architektura založená na API zajišťuje interoperabilitu mezi mediálními aplikacemi různých výrobců a komponentami sítě 5G.

Klíčové komponenty v ekosystému 5GMS zahrnují Media Session Handler, který spravuje životní cyklus relace streamování médií a s ní spojené síťové prostředky; Media Player, což je kompatibilní klientská aplikace; a Media Distribution Network, kterou může být Content Delivery Network ([CDN](/mobilnisite/slovnik/cdn/)) nebo služba multicast/broadcast. Kritickým aspektem je podpora jak unicastových (např. [DASH](/mobilnisite/slovnik/dash/), [HLS](/mobilnisite/slovnik/hls/)), tak broadcastových/multicastových (např. 5G Broadcast, 5G Multicast-Broadcast Services) metod doručování. Rámec také definuje postupy pro dynamické adaptivní streamování, kde klientský Media Player může přepínat mezi různými reprezentacemi kvality na základě aktuálních síťových podmínek, s možnou síťovou asistencí pro plynulejší přechody.

Jeho role v síti je fungovat jako standardizované pojítko mezi mediálními službami typu over-the-top ([OTT](/mobilnisite/slovnik/ott/)) a podkladovým systémem 5G. Umožňuje, aby se síť 5G stala „mediálně vědomou“ (media-aware), což jí dovoluje aplikovat optimalizované politiky pro mediální provoz, jako je garantovaná přenosová rychlost, cesty s nízkou latencí nebo efektivní multicastové doručování pro oblíbené živé události. Tím se přesahuje jednoduché doručování typu best-effort přes internet a poskytuje se řízená kvalita služby, kterou lze monetizovat. Rámec také usnadňuje scénáře edge computingu, kde může být zpracování nebo ukládání médií do mezipaměti prováděno na okraji sítě (prostřednictvím Edge-enabled 5GMS Application Server, neboli [EAS](/mobilnisite/slovnik/eas/)), čímž se snižuje latence a zatížení páteřní sítě, což je klíčové pro aplikace jako cloudové hraní nebo streamování VR v ultra vysokém rozlišení.

## K čemu slouží

5GMS byl vytvořen, aby řešil nedostatek standardizovaných, síťově integrovaných mechanismů pro doručování médií v předchozích generacích mobilních sítí. Před 5G bylo streamování médií přes mobilní sítě z velké části službou OTT běžící transparentně nad IP konektivitou typu best-effort. To vedlo k neefektivitám, nekonzistentní uživatelské zkušenosti (QoE) a neschopnosti síťových operátorů optimalizovat nebo monetizovat obrovský objem mediálního provozu. Exploze video provozu spolu s novými schopnostmi 5G (např. síťové řezy, edge computing, ultra nízká latence) vytvořila potřebu po rámci, který by tyto schopnosti dokázal odemknout speciálně pro mediální aplikace.

Primární problémy, které řeší, jsou fragmentace doručování médií a suboptimální využití zdrojů. Bez 5GMS by si každý poskytovatel médií musel vyvíjet proprietární integrace s různými mobilními operátory, aby získal přístup k pokročilým síťovým funkcím, což by vytvářelo složitost a bránilo škálování. 5GMS poskytuje společného, standardy řízeného „mediátora“, který abstrahuje složitost sítě. Řeší problém neefektivního doručování oblíbeného obsahu (jako jsou živé sportovní přenosy) standardizací použití 5G multicast/broadcast, který přenáší jeden datový proud k mnoha uživatelům současně, a tím šetří cenné rádiové a jádrové síťové prostředky ve srovnání s tisíci jednotlivých unicastových proudů.

Historicky vycházela motivace z touhy vytvořit životaschopnou, standardizovanou alternativu k tradičnímu televiznímu vysílání (např. DVB) využívající mobilní sítě, a zároveň vylepšit unicastové streamování. Řeší omezení předchozích přístupů tím, že se posouvá od pasivního, transparentního modelu „potrubí“ k aktivnímu, kolaborativnímu modelu, kde si aplikace a síť vyměňují informace a požadavky. To umožňuje proaktivní správu kvality, bezproblémovou podporu mobility pro streamovací relace a umožnění nových formátů imerzivních médií, která vyžadují přísné výkonnostní záruky, které může spolehlivě poskytnout pouze řízený systém 5G.

## Klíčové vlastnosti

- Standardizovaná API (M1-M5) pro interoperabilitu mezi mediálními aplikacemi a sítí 5G
- Podpora jak unicastového (DASH/HLS), tak multicastového/broadcastového doručování médií
- Integrace s funkcemi jádra sítě 5G (PCF, NEF) pro dynamické QoS a řízení politik
- Umožňuje síťově asistované dynamické adaptivní streamování pro lepší QoE
- Architektura podporující edge computing prostřednictvím Edge-enabled Application Server (EAS)
- Správa mediálních relací pro životní cyklus, mobilitu a koordinaci zdrojů

## Definující specifikace

- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 29.116** (Rel-19) — REST-based protocol for xMB reference point
- **TS 29.517** (Rel-19) — 5G AF Event Exposure Service Stage 3
- **TS 29.591** (Rel-19) — 5G NEF Southbound Services Stage 3
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [5GMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/5gms/)
