---
slug: "sgf"
url: "/mobilnisite/slovnik/sgf/"
type: "slovnik"
title: "SGF – Signalling Gateway Function"
date: 2025-01-01
abbr: "SGF"
fullName: "Signalling Gateway Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sgf/"
summary: "Funkce signalizační brány (Signalling Gateway Function, SGF) je síťová funkce, která usnadňuje vzájemnou spolupráci mezi signalizačními protokoly založenými na IP (jako je SIP) a staršími signalizační"
---

SGF je síťová funkce, která zprostředkovává vzájemnou spolupráci signalizačních protokolů založených na IP se staršími signalizačními protokoly s přepojováním okruhů, aby umožnila bezproblémovou komunikaci mezi sítěmi 4G/5G a staršími sítěmi 2G/3G.

## Popis

Funkce signalizační brány (Signalling Gateway Function, SGF) funguje jako kritický uzel pro vzájemnou spolupráci v architektuře IP Multimedia Subsystem (IMS) a 5G Core (5GC). Jejím hlavním úkolem je překládat a přeposílat signalizační zprávy mezi přenosem signalizace založeným na IP (např. využívajícím protokoly SIGTRAN jako [SCTP](/mobilnisite/slovnik/sctp/)/IP) používaným v moderních sítích a tradičním signalizačním systémem č. 7 ([SS7](/mobilnisite/slovnik/ss7/)) založeným na časovém multiplexu ([TDM](/mobilnisite/slovnik/tdm/)) používaným v starších sítích s přepojováním okruhů. Z architektonického hlediska je SGF definována jako funkční entita, která může být implementována jako samostatný síťový prvek nebo integrována s jinými funkcemi řídicí roviny. Slouží jako koncový bod pro signalizační spoje SS7 (např. využívající [MTP2](/mobilnisite/slovnik/mtp2/)/[MTP3](/mobilnisite/slovnik/mtp3/)) ze starší sítě s přepojováním okruhů a mapuje tyto zprávy na příslušné transportní toky IP směrem k funkci řídicího uzlu mediální brány (Media Gateway Controller Function, [MGCF](/mobilnisite/slovnik/mgcf/)) nebo jiným entitám IMS/5GC.

Z architektonického hlediska je SGF definována jako samostatná logická funkce, i když může být umístěna společně s jinými síťovými funkcemi, jako je MGCF nebo Session Border Controller (SBC). Zpracovává konverzi protokolů nižších vrstev (vrstvy 1-3 modelu [OSI](/mobilnisite/slovnik/osi/)) pro signalizaci. Například převádí signalizaci MTP2/MTP3 ze spoje SS7 na [M3UA](/mobilnisite/slovnik/m3ua/) (MTP3 User Adaptation) přes SCTP/IP, která je následně přenesena do MGCF. MGCF zpracovává vzájemnou spolupráci aplikačních protokolů vyšších vrstev (např. mezi ISUP a SIP). Toto oddělení úkolů umožňuje škálovatelná a flexibilní nasazení sítě.

V kontextu 5G se role SGF rozšiřuje o podporu vzájemné spolupráce s jádrem sítě 5G pro služby jako kontinuita hlasových hovorů. Zatímco 5GC primárně využívá rozhraní založená na službách (service-based interfaces) na bázi HTTP/2, vzájemná spolupráce se staršími sítěmi pro hlasové služby stále vyžaduje konektivitu SS7 pro funkce jako roamování a propojení s telefonními sítěmi veřejné komunikační sítě (PSTN). SGF to umožňuje tím, že poskytuje nezbytnou schopnost signalizační brány, což zajišťuje, že uživatelé 5G mohou uskutečňovat a přijímat hovory do/z starších sítí. Její provoz je podrobně specifikován v mnoha technických specifikacích 3GPP, které definují její rozhraní, procedury a mapování protokolů, aby byla zajištěna interoperabilita mezi implementacemi různých výrobců a generacemi sítí.

## K čemu slouží

SGF byla zavedena, aby řešila zásadní výzvu ve vývoji sítí: koexistenci nových, plně IP architektur sítí (jako jsou IMS a 5GC) s rozsáhlou a zavedenou infrastrukturou starších sítí s přepojováním okruhů (2G/3G/PSTN). Tyto starší sítě používají sadu signalizačních protokolů SS7, která se zásadně liší od protokolů založených na IP (jako jsou SIP a Diameter) používaných v IMS a 5G. Přímá komunikace mezi těmito odlišnými signalizačními doménami je bez brány nemožná.

Před standardizací funkcí jako je SGF se operátoři spoléhali na proprietární řešení bran nebo integrované signalizační schopnosti v rámci mediálních bran. Tento nedostatek standardizace vedl k problémům s interoperabilitou, zvýšené složitosti a vyšším nákladům na nasazení sítí s více dodavateli. SGF jako standardizovaná funkce 3GPP poskytuje jasné architektonické oddělení mezi signalizační branou a řídicím uzlem mediální brány (MGCF). Toto oddělení podporuje síťovou flexibilitu, což operátorům umožňuje škálovat a aktualizovat tyto funkce nezávisle na základě charakteru provozu (signalizace vs. média).

Její vytvoření bylo motivováno dlouhým přechodným obdobím od služeb s přepojováním okruhů k paketovým hlasovým a multimediálním službám. Operátoři nemohli okamžitě nahradit své sítě založené na SS7; potřebovali plynulou migrační cestu. SGF to umožňuje tím, že dovoluje, aby byla základní signalizační inteligence (v MGCF/IMS) nasazena na moderních IP platformách, zatímco stále zůstává připojena ke globální síti SS7/PSTN pro nezbytné služby jako směrování hovorů, roamování a přenos čísel. Je základním kamenem pro zajištění kontinuity služeb a úspěšného přechodu na VoLTE a VoNR.

## Klíčové vlastnosti

- Konverze protokolů mezi vrstvami SS7 MTP2/MTP3 a adaptačními vrstvami SIGTRAN (např. M3UA) přes IP
- Ukončení fyzických signalizačních spojů SS7 (časové sloty E1/T1) nebo připojení SS7 založených na IP
- Přeposílání signalizačních zpráv mezi staršími sítěmi SS7 a síťovými funkcemi jádra založenými na IP, jako je MGCF
- Podpora nezbytných signalizačních procedur SS7 potřebných pro navázání a ukončení hovoru s PSTN
- Škálovatelná architektura umožňující samostatné nebo společné nasazení s jinými síťovými funkcemi
- Standardizovaná rozhraní a procedury dle specifikací 3GPP pro zajištění interoperability mezi různými výrobci

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture

---

📖 **Anglický originál a plná specifikace:** [SGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgf/)
