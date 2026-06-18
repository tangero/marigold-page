---
slug: "lmc"
url: "/mobilnisite/slovnik/lmc/"
type: "slovnik"
title: "LMC – Location Management Client"
date: 2026-01-01
abbr: "LMC"
fullName: "Location Management Client"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lmc/"
summary: "Klientská funkce zavedená ve specifikaci 3GPP Release 17 pro polohové služby, typicky umístěná v UE nebo AF. Interaguje se síťovým systémem správy polohy za účelem vyžádání a přijímání polohových info"
---

LMC je klientská funkce v UE nebo AF, která interaguje se síťovým systémem správy polohy za účelem vyžádání a přijímání polohových informací pro umožnění služeb založených na poloze.

## Popis

Location Management Client (LMC) je funkční entita definovaná v rámci architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) 3GPP pro polohové služby. Vystupuje jako žadatel a spotřebitel polohových informací. LMC může být implementována v uživatelském zařízení (UE), aplikační funkci ([AF](/mobilnisite/slovnik/af/)) nebo jiných síťových entitách, které vyžadují polohová data. Jejím hlavním úkolem je iniciovat požadavky na polohu směrem k síťovému systému správy polohy, konkrétně k funkci Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) nebo Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), v závislosti na architektuře a scénáři služby. LMC formuluje požadavky na polohové služby, které mohou zahrnovat parametry jako identifikátor cílového UE, požadovanou kvalitu služby (např. přesnost, doba odezvy) a typ potřebné polohové informace (např. okamžitá poloha, periodické sledování nebo hlášení spouštěné událostí).

Po odeslání požadavku LMC komunikuje přes standardizovaná rozhraní založená na službách, jako jsou Nlmf_Location nebo N5g-eir_LocationReporting, s příslušnou síťovou funkcí. Síť požadavek zpracuje, což může zahrnovat koordinaci s přístupovou rádiovou sítí (RAN) a samotným UE za účelem provedení polohových měření pomocí technik jako Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), Uplink Time Difference of Arrival ([UTDOA](/mobilnisite/slovnik/utdoa/)) nebo Assisted Global Navigation Satellite System ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Jakmile je poloha určena, síť doručí odhad polohy nebo hlášení zpět k LMC.

Architektura LMC je navržena flexibilně a podporuje jak postupy určování polohy založené na UE, tak na síti. Ve scénářích založených na UE může LMC uvnitř UE přímo interagovat s LMF za účelem získání pomocných dat pro určení polohy nebo nahlášení vlastní vypočtené polohy. Ve scénářích založených na AF externí aplikační server (hostující LMC) žádá o polohové informace pro cílové UE, čímž umožňuje služby jako sledování vozového parku, nouzové služby nebo reklamu založenou na poloze. LMC abstrahuje složitost podkladových polohovacích technologií od aplikace a poskytuje standardizované [API](/mobilnisite/slovnik/api/) pro využívání polohových služeb.

Klíčové součásti fungování LMC zahrnují vazby jejích servisních rozhraní, bezpečnostní kontext pro ověřování a autorizaci polohových požadavků a její schopnost zpracovávat různé typy polohových služeb definované v 3GPP, jako je Mobile Terminated Location Request (MT-LR), Mobile Originated Location Request (MO-LR) a Network Induced Location Request (NI-LR). Její role je klíčová pro umožnění ekosystému polohových služeb 5G, zajišťující, že aplikace mohou spolehlivě a bezpečně přistupovat k polohovým datům UE při respektování předpisů na ochranu soukromí a síťových politik.

## K čemu slouží

LMC byla zavedena za účelem standardizace a zjednodušení klientského rozhraní pro přístup k síťovým polohovým službám v 5G a dalších generacích. Před její definicí se polohové požadavky od aplikací nebo UE často opíraly o proprietární nebo méně integrované metody, což vedlo k fragmentaci a zvýšené složitosti pro vývojáře aplikací a síťové operátory. LMC poskytuje jednotný přístup založený na službách, který je v souladu s architektonickými principy 5G jádra sítě.

K jejímu vytvoření motivovala rostoucí poptávka po přesných polohových službách s nízkou latencí napříč různými vertikálami, včetně průmyslového IoT, automobilového průmyslu (V2X), rozšířené reality a veřejné bezpečnosti. Tyto aplikace vyžadují spolehlivý a efektivní mechanismus pro vyžádání a přijetí polohových dat. LMC to řeší tím, že nabízí standardizovanou klientskou funkci, kterou lze vložit do různých entit (UE, AF), což usnadňuje interoperabilitu a umožňuje nové obchodní modely pro služby založené na poloze.

Dále LMC podporuje regulatorní požadavky, jako je vylepšená lokalizace tísňových volajících (např. pro E911 v USA nebo E112 v Evropě), tím, že poskytuje definovanou cestu pro aplikace tísňových služeb k vyžádání polohy UE. Také zvyšuje ochranu soukromí a bezpečnost integrací s ověřovacími a autorizačními frameworky 3GPP, což zajišťuje, že polohové informace jsou zpřístupněny pouze autorizovaným klientům za povolených podmínek.

## Klíčové vlastnosti

- Iniciuje standardizované požadavky na polohové služby (např. MT-LR, MO-LR, NI-LR) směrem k síťovým funkcím, jako jsou LMF nebo GMLC.
- Může být implementována v uživatelském zařízení (UE) nebo externí aplikační funkci (AF) pro flexibilní nasazení.
- Podporuje různé parametry QoS pro určování polohy včetně přesnosti, doby odezvy a režimů hlášení (okamžité, periodické, spouštěné událostí).
- Komunikuje přes rozhraní založená na službách definovaná 3GPP (např. Nlmf_Location) v rámci architektury 5G jádra sítě.
- Umožňuje jak metody určování polohy s asistencí UE, tak metody založené na síti prostřednictvím interakce se zásobníkem protokolů pro určování polohy.
- Integruje se s bezpečnostními mechanismy 3GPP pro ověřování, autorizaci a ochranu soukromí polohových dat.

## Související pojmy

- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer

---

📖 **Anglický originál a plná specifikace:** [LMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/lmc/)
