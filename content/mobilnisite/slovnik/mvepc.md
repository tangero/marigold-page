---
slug: "mvepc"
url: "/mobilnisite/slovnik/mvepc/"
type: "slovnik"
title: "MVEPC – MCVideo Emergency Private Call"
date: 2025-01-01
abbr: "MVEPC"
fullName: "MCVideo Emergency Private Call"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mvepc/"
summary: "Služba standardizovaná organizací 3GPP pro zahájení soukromého, párového videohovoru s nouzovou prioritou v rámci systému Mission Critical (MC). Zajišťuje okamžitou a bezpečnou komunikaci mezi dispeče"
---

MVEPC je služba standardizovaná organizací 3GPP pro zahájení soukromého, párového (jeden na jednoho) nouzového prioritního videohovoru v rámci systému Mission Critical, která zajišťuje okamžitou komunikaci mezi dispečerem a zasahujícím pracovníkem.

## Popis

[MCVideo](/mobilnisite/slovnik/mcvideo/) Emergency Private Call (MVEPC) je specializovaná služba definovaná v rámci standardů 3GPP pro Mission Critical služby přes LTE ([MCPTT](/mobilnisite/slovnik/mcptt/)) a 5G systémy. Umožňuje navázání soukromé, párové (jeden na jednoho) komunikace v reálném čase s nouzovou prioritou mezi autorizovanými uživateli, typicky dispečerem v řídicím středisku a zasahujícím pracovníkem v terénu. Služba je nedílnou součástí širší sady MCVideo, která rozšiřuje mission-critical hlasové služby (MCPTT) o video a datové schopnosti pro veřejnou bezpečnost a kritickou komunikaci.

Z architektonického hlediska MVEPC funguje v rámci architektury Mission Critical Services od 3GPP, která zahrnuje funkční entity jako Mission Critical Service Client ([MC](/mobilnisite/slovnik/mc/) klient) na uživatelském zařízení, Mission Critical Server (např. MCVideo Server) a rozhraní k podkladovému 3GPP Evolved Packet Core (EPC) nebo 5G Core (5GC). Zahájení hovoru spouští uživatel s příslušnou autorizací, často prostřednictvím vyhrazeného nouzového tlačítka nebo volby v menu aplikace MC klienta. Požadavek je signalizován na MCVideo server pomocí protokolů definovaných v 3GPP TS 24.281 (aplikační vrstva) a TS 37.579 (aspekty řízení a orchestrace). Server požadavek autentizuje, ověří uživatelská oprávnění pro nouzové soukromé hovory a orchestruje sestavení relace.

Jádro fungování MVEPC spočívá v jeho integraci s mechanismy Quality of Service (QoS) a priority sítě. Při zahájení služba využívá standardizované QoS Class Identifiers (QCIs) nebo 5G QoS Indicators (5QIs) specificky přidělené pro mission-critical komunikaci. Ty zajišťují, že video mediální toky jsou označeny pro vysokou prioritu, což jim poskytuje přednostní zacházení oproti běžnému uživatelskému provozu z hlediska přidělování zdrojů, řízení přístupu a plánování paketů napříč rádiovou přístupovou sítí (RAN) i páteřní sítí. To vede k nižší latenci, vyšší spolehlivosti a garantované šířce pásma pro nouzový video přenos. Aspekt 'Private' (soukromý) znamená, že hovor je navázán výhradně mezi dvěma stranami, žádní další uživatelé se nemohou připojit nebo naslouchat, což zajišťuje důvěrnost pro citlivou operační komunikaci. Relace je spravována end-to-end, přičemž MCVideo server zvládá řízení práva vysílat (floor control), distribuci médií a případně záznam pro operační logování.

## K čemu slouží

MVEPC byl vytvořen, aby řešil kritickou potřebu okamžité, spolehlivé a soukromé vizuální komunikace během zásahových operací. Před jeho standardizací se zasahující pracovníci spoléhali primárně na hlas (pozemní mobilní rádia) nebo komerční aplikace pro videohovory, kterým chyběla garantovaná priorita, zabezpečení a integrace s operačními protokoly pro veřejnou bezpečnost. Komerční služby mohly během rozsáhlých incidentů, právě když je komunikace nejdůležitější, trpět přetížením, zpožděním nebo výpadky.

Vývoj MVEPC byl motivován prací 3GPP na přizpůsobení technologií LTE a později 5G pro případy užití mission-critical, kterou řídí globální organizace pro veřejnou bezpečnost. Řeší problém navázání důvěryhodného vizuálního spojení mezi velením a personálem v terénu za účelem vyhodnocení situace, poskytnutí vzdáleného návodu nebo sdílení vizuálních důkazů v reálném čase. Tím, že jde o standardizovanou službu v rámci ekosystému 3GPP, zajišťuje interoperabilitu mezi zařízeními od různých výrobců a napříč různými síťovými operátory, což je klíčové pro společné operace během velkých katastrof. Přímo řeší omezení předchozích proprietárních nebo best-effort řešení tím, že poskytuje síťově vynucenou nouzovou prioritní cestu, integrovanou autentizaci a servisní architekturu navrženou pro robustnost a řízení.

## Klíčové vlastnosti

- Navázání párového (jeden na jednoho) soukromého videosession s nouzovou prioritou
- Integrace s mechanismy QoS od 3GPP pro garantované síťové zdroje (vysoce prioritní QCIs/5QIs)
- Autorizace a autentizace prostřednictvím frameworku Mission Critical Service
- Standardizované signalizační protokoly (TS 24.281) pro interoperabilitu
- Řízené ovládání relace včetně floor control pro přenos videa
- Navrženo pro provoz přes LTE EPC i 5G Core síťové architektury

## Související pojmy

- [MCVideo – Mission Critical Video](/mobilnisite/slovnik/mcvideo/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MVEPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mvepc/)
