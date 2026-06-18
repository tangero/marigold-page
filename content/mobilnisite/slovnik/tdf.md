---
slug: "tdf"
url: "/mobilnisite/slovnik/tdf/"
type: "slovnik"
title: "TDF – Traffic Detection Function"
date: 2025-01-01
abbr: "TDF"
fullName: "Traffic Detection Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tdf/"
summary: "Síťová funkce, která provádí detekci aplikací, uzavírání a přesměrování provozu. Je klíčovou součástí pro řízení politik a účtování (PCC), která umožňuje operátorům identifikovat aplikační provoz a up"
---

TDF je síťová funkce, která provádí detekci aplikací, uzavírání a přesměrování provozu za účelem umožnění řízení politik a účtování.

## Popis

Traffic Detection Function (TDF) je specializovaný síťový prvek v architektuře 3GPP Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)). Jeho hlavní úlohou je provádět hlubokou kontrolu paketů (DPI) na provozu v uživatelské rovině za účelem identifikace konkrétních aplikací a služeb, jako je streamované video, sociální média nebo peer-to-peer aplikace. TDF funguje tak, že analyzuje hlavičky a datovou část paketů vůči sadě předdefinovaných detekčních pravidel, která mohou být založena na signaturách, behaviorálních vzorcích nebo jiných heuristikách. Po detekci konkrétní aplikace může TDF tuto informaci nahlásit funkci Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) přes referenční bod Sd. PCRF pak může tyto informace použít k dynamické instalaci nebo modifikaci pravidel PCC ve funkci Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)), což umožňuje vynucování politik v reálném čase, jako je omezení šířky pásma, blokování nebo účtování pro detekovaný aplikační tok.

Architektonicky lze TDF nasadit ve dvou režimech: jako Application Function ([AF](/mobilnisite/slovnik/af/)) v rámci PCC frameworku nebo jako samostatný uzel. Při samostatném nasazení komunikuje přímo s PCRF. TDF obsahuje klíčové funkční komponenty včetně Traffic Detection Engine, která provádí samotnou DPI, a reportovací funkce, která komunikuje s PCRF. Udržuje také databázi pravidel pro detekci aplikací, kterou může operátor aktualizovat. Činnost TDF se řídí pravidly [ADC](/mobilnisite/slovnik/adc/) (Application Detection and Control), která zřizuje PCRF a která specifikují, jaké aplikace hledat a jaké akce provést po detekci, například hlášení, uzavření (blokování) nebo přesměrování provozu.

V síti je TDF typicky umístěn v datové cestě, často integrován s Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v 4G, nebo s User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G. Jeho integrace umožňuje detailní, na aplikaci zaměřené vynucování politik nad rámec jednoduchých řízení na úrovni přenosového kanálu. Například operátor může použít TDF k detekci služby streamování videa a uplatnit konkrétní politiku Quality of Service (QoS), aby zajistil plynulý uživatelský zážitek, nebo k identifikaci a omezení šířky pásma pro aplikaci sdílení souborů během zahlcení sítě. Schopnost TDF poskytovat viditelnost na úrovni aplikace je klíčová pro implementaci diferenciace služeb, nabídek zero-rating a rodičovských kontrol.

## K čemu slouží

TDF byl vytvořen, aby řešil rostoucí potřebu operátorů spravovat a monetizovat různorodý internetový aplikační provoz nad rámec možností tradičního PCC na úrovni přenosového kanálu. Před jeho zavedením bylo řízení politik primárně založeno na informacích IP 5-tice (zdrojová/cílová IP adresa/port, protokol), což je nedostatečné pro přesnou identifikaci konkrétních aplikací, zejména těch, které používají dynamické porty, šifrování nebo sdílejí společné servery. Toto omezení ztěžovalo operátorům implementaci politik spravedlivého využití, nabízení aplikačně specifických datových tarifů nebo zajištění kvality zážitku pro služby citlivé na zpoždění.

Motivací pro standardizaci TDF ve 3GPP Release 11 bylo poskytnout jednotnou, mezi dodavateli interoperabilní metodu pro hlubokou kontrolu paketů a vynucování politik zaměřených na aplikace v rámci PCC frameworku. Vyřešil problém neviditelnosti aplikací v jádrové síti a umožnil nové obchodní modely, jako je sponzorovaná data, kde poskytovatel aplikace platí za využití dat, nebo vrstvené služby, kde prémioví účastníci získávají lepší kvalitu pro konkrétní aplikace. TDF také poskytuje technický základ pro regulatorní požadavky, jako je zákonné odposlouchávání konkrétních služeb nebo dodržování pravidel síťové neutrality prostřednictvím transparentního řízení provozu.

Historicky se operátoři spoléhali na proprietární DPI řešení, která nebyla integrována se standardizovanou PCC architekturou, což vedlo k provozní složitosti a omezené škálovatelnosti. TDF standardizuje rozhraní (např. Sd, Gx) a procedury pro detekci a řízení aplikací, což operátorům umožňuje nasazovat řešení od více dodavatelů a zajišťuje, že rozhodnutí o politikách založená na detekci aplikací jsou konzistentní a vynutitelná v celé síti. Představuje klíčový vývoj od jednoduchého účtování založeného na objemu k inteligentnímu, na služby zaměřenému řízení sítě.

## Klíčové vlastnosti

- Hluboká kontrola paketů (DPI) pro identifikaci aplikací
- Vynucování pravidel Application Detection and Control (ADC) od PCRF
- Podpora akcí uzavření (blokování) a přesměrování provozu
- Generování hlášení o využití pro účtování (pomocí TDF-CDR)
- Integrace s PCC architekturou přes referenční bod Sd
- Provozní režimy: samostatný nebo integrovaný jako Application Function

## Související pojmy

- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.250** (Rel-19) — Nu Reference Point Stage 3 Specification
- **TS 29.251** (Rel-19) — Gw/Gwn Reference Points Stage 3 Specification
- **TS 29.810** (Rel-13) — Diameter Load Control Study
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [TDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdf/)
