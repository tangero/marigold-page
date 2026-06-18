---
slug: "sae"
url: "/mobilnisite/slovnik/sae/"
type: "slovnik"
title: "SAE – System Architecture Evolution"
date: 2025-01-01
abbr: "SAE"
fullName: "System Architecture Evolution"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sae/"
summary: "Architektura jádrové sítě pro LTE a novější systémy, definující Evolved Packet Core (EPC). Poskytuje plně IP, plochou architekturu pro vysokorychlostní data, umožňuje efektivní mobilitu a poskytování"
---

SAE je architektura jádrové sítě 3GPP pro LTE (4G) a novější systémy, která definuje plně IP Evolved Packet Core (EPC) pro umožnění vysokorychlostního přenosu dat, efektivního řízení mobility a poskytování služeb.

## Popis

System Architecture Evolution (SAE) je standardizovaná architektura jádrové sítě vyvinutá 3GPP pro rádiový přístupový síť Long-Term Evolution (LTE), společně známá jako Evolved Packet System (EPS). Představuje zásadní posun od dvoudoménové architektury s přepojováním okruhů a paketů sítí 2G/3G ke zjednodušené, plně IP, ploché architektuře navržené pro vysokorychlostní paketová data. Hlavním cílem bylo snížit latenci, zvýšit datovou propustnost a zjednodušit provoz sítě pro podporu explozivního růstu služeb mobilního širokopásmového přístupu.

Architektura je založena na Evolved Packet Core (EPC), který se skládá z několika klíčových logických uzlů propojených standardizovanými rozhraními. Mezi základní komponenty patří Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) pro signalizaci řídicí roviny, Serving Gateway ([S-GW](/mobilnisite/slovnik/s-gw/)) a Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) pro směrování dat uživatelské roviny a vynucování politik a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) jako centrální databáze účastníků. S-GW funguje jako lokální kotva mobility při předávání mezi eNodeB, zatímco P-GW poskytuje rozhraní k externím paketovým datovým sítím (jako je internet) a vynucuje politiky Quality of Service (QoS) na základě profilů účastníků.

SAE funguje oddělením řídicí roviny (signalizace) od uživatelské roviny (datového přenosového kanálu), což umožňuje nezávislé škálování a optimalizaci. Když se User Equipment (UE) připojí k síti, MME ověří účastníka prostřednictvím HSS a vytvoří výchozí přenosový kanál s konkrétními charakteristikami QoS přes S-GW a P-GW. Tento kanál poskytuje 'vždy zapojené' IP připojení. Vyhrazené přenosové kanály s různými úrovněmi QoS lze na požádání vytvořit pro konkrétní služby, jako je voice over LTE (VoLTE). Architektura podporuje bezproblémovou mobilitu mezi 3GPP a ne-3GPP přístupovými sítěmi (jako je Wi-Fi) prostřednictvím důvěryhodných nebo nedůvěryhodných přístupových bran.

Její role v síti je klíčová jako centrum pro poskytování služeb a řízení mobility. Poskytuje rámec pro řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) prostřednictvím funkce Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), což operátorům umožňuje nabízet služby ve vrstvách. Konstrukční principy SAE, jako je zjednodušení sítě, plně IP přenos a podpora více rádiových přístupových technologií, přímo umožnily vysoký výkon a nízkou latenci u 4G LTE a položily architektonické základy, které se později vyvinuly v 5G Core (5GC) se zavedením služebně orientované architektury a síťového řezání.

## K čemu slouží

SAE byla vytvořena, aby řešila omezení architektur jádrové sítě před 4G, které nebyly vhodné pro očekávaný masivní růst mobilního datového provozu. Předchozí architektury 3GPP, jako [GPRS](/mobilnisite/slovnik/gprs/) Core Network, byly složité, s oddělenými síťovými prvky pro přepojování okruhů hlasu a přepojování paketů dat, což vedlo k neefektivnímu využití zdrojů a vyšší latenci. Vzestup chytrých telefonů a aplikací náročných na šířku pásma vyžadoval síť, která by mohla doručovat data rychleji, s nižší latencí a za nižší cenu za bit.

Hlavní motivací bylo navrhnout perspektivní, zjednodušenou jádrovou síť, která by mohla bezproblémově podporovat vysokorychlostní paketová data z nového rádiového rozhraní LTE založeného na [OFDMA](/mobilnisite/slovnik/ofdma/). Mezi klíčové problémy, které řešila, patřila architektonická složitost, úzká místa latence z více síťových skoků a neschopnost efektivně podporovat 'vždy zapojené' připojení a pokročilé mechanismy QoS pro různé služby. Přechodem na plochou, plně IP architekturu s oddělením řídicí a uživatelské roviny SAE drasticky snížila počet síťových uzlů zapojených do přenosu dat, minimalizovala latenci a zjednodušila správu a nasazení sítě pro operátory.

Historicky byl vývoj SAE v 3GPP Release 8 součástí paralelního projektu s rádiovou přístupovou sítí LTE. Byl hnán potřebou jádrové sítě, která by mohla odpovídat výkonnostnímu skoku nové rádiové technologie a podporovat případnou migraci hlasových služeb na IP (VoLTE). Cílem bylo také poskytnout jednotné jádro pro heterogenní přístup, včetně starších 3GPP (2G/3G) a ne-3GPP sítí, čímž se připravila cesta pro skutečnou konvergenci sítí. Tato evoluce byla pro operátory klíčová, aby mohli efektivně přejít své sítě na podporu éry mobilního širokopásmového přístupu.

## Klíčové vlastnosti

- Plně IP, plochá síťová architektura snižující latenci a složitost
- Jasné oddělení řídicí roviny (MME) a uživatelské roviny (S-GW/P-GW)
- Podpora bezproblémové mobility a předávání mezi 3GPP a ne-3GPP přístupovými sítěmi
- Vždy zapojené IP připojení prostřednictvím výchozích a vyhrazených EPS přenosových kanálů
- Integrovaný rámec řízení politik a účtování (PCC) prostřednictvím PCRF
- Centralizované ověřování účastníků a správa profilů prostřednictvím HSS

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [S-GW – Serving Gateway](/mobilnisite/slovnik/s-gw/)
- [P-GW – Packet Data Network Gateway](/mobilnisite/slovnik/p-gw/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 26.985** (Rel-19) — Media Handling for Advanced V2X Services
- **TR 29.909** (Rel-19) — Diameter Usage Guidelines for 3GPP
- **TS 32.582** (Rel-19) — HNB Management Information Model for Type 1 Interface
- **TS 32.584** (Rel-19) — HNB OAM&P XML Definitions for Type 1 Interface
- **TS 32.592** (Rel-19) — HeNB OAM&P Information Model
- **TS 32.594** (Rel-19) — Data definitions for HeNB to HeMS Type 1 interface
- **TS 32.821** (Rel-9) — SON OAM Architecture for Home NodeB
- **TS 33.821** (Rel-9) — LTE/SAE Security Threat Analysis and Countermeasures
- **TS 33.822** (Rel-8) — Security Architecture for Inter-Access Mobility
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [SAE na 3GPP Explorer](https://3gpp-explorer.com/glossary/sae/)
