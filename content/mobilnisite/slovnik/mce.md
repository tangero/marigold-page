---
slug: "mce"
url: "/mobilnisite/slovnik/mce/"
type: "slovnik"
title: "MCE – Multi-cell/multicast Coordination Entity"
date: 2025-01-01
abbr: "MCE"
fullName: "Multi-cell/multicast Coordination Entity"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mce/"
summary: "Logická funkce v LTE RAN zodpovědná za koordinaci rádiové konfigurace a alokace zdrojů pro služby eMBMS napříč více buňkami v rámci oblasti MBSFN. Zajišťuje synchronizovaný přenos a konzistentní param"
---

MCE je logická funkce LTE RAN, která koordinuje rádiovou konfiguraci a alokaci zdrojů pro eMBMS napříč více buňkami, aby umožnila synchronizovaný broadcastový/multicastový přenos MBSFN.

## Popis

Multi-cell/multicast Coordination Entity (MCE) je klíčová funkce řídicí roviny v architektuře LTE Evolved Universal Terrestrial Radio Access Network ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) pro službu evolved Multimedia Broadcast Multicast Service (eMBMS). Nejde o samostatný fyzický uzel, ale o logickou entitu, která může být implementována jako součást eNodeB (základnové stanice) nebo jako samostatný síťový prvek. Jejím primárním úkolem je spravovat a koordinovat všechny rádiové aspekty doručování eMBMS v rámci definované oblasti [MBSFN](/mobilnisite/slovnik/mbsfn/) ([MBMS](/mobilnisite/slovnik/mbms/) Single Frequency Network). Oblast MBSFN se skládá ze skupiny buněk, které jsou časově synchronizovány pro vysílání identických vlnových forem pro službu MBMS, čímž vytvářejí bezproblémovou broadcastovou zónu, kde se signály z více buněk na přijímači UE konstruktivně skládají.

Architektonicky se MCE nachází mezi MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) v core síti a eNodeB v RAN. S MBMS-GW komunikuje přes rozhraní M3 (založené na IP) a s eNodeB přes rozhraní M2 (také IP, s využitím protokolu M2AP). Při zahájení MBMS relace odešle MBMS-GW požadavek na zahájení relace do MCE. MCE je pak zodpovědná za rozhodnutí o alokaci rádiových zdrojů. Vypočítá a rozhodne o společných rádiových konfiguračních parametrech, které musí použít všechny eNodeB v oblasti MBSFN. Tyto parametry zahrnují úroveň [MCS](/mobilnisite/slovnik/mcs/) (Modulation and Coding Scheme), přidělení subrámců pro přenos MBSFN (vzor MBSFN subframů), plánovací periodu [MCH](/mobilnisite/slovnik/mch/) (Multicast Channel) a alokaci zdrojů mezi různými službami MBMS ([MTCH](/mobilnisite/slovnik/mtch/)) multiplexovanými na stejném MCH.

Po provedení těchto rozhodnutí použije MCE rozhraní M2 k odeslání MBMS Scheduling Information ([MSI](/mobilnisite/slovnik/msi/)) a rádiové konfigurace každému zúčastněnému eNodeB. Tím zajišťuje absolutní konzistenci v celé oblasti MBSFN, což je klíčové pro úspěšný provoz SFN. UE pohybující se v oblasti přijímá od každé buňky identické parametry fyzické vrstvy, což jí umožňuje považovat kombinované přenosy za jediný silný signál s diverzitou vícecestného šíření, nikoli za rušivé signály. MCE také spravuje přístupovou kontrolu pro nové MBMS relace a před přijetím požadavku na zahájení relace z core sítě kontroluje dostupnost dostatečných rádiových zdrojů v oblasti MBSFN.

Pokud jde o provoz, koordinace MCE je průběžná. Během relace může v případě potřeby upravovat parametry a také zpracovává procedury ukončení relace. Pro každou oblast MBSFN je zodpovědná jedna MCE. V nasazeních může jedna MCE řídit více oblastí MBSFN. Její funkce jsou čistě řídicí roviny; uživatelská data pro MBMS proudí přímo z MBMS-GW do eNodeB přes rozhraní M1, čímž se MCE vyhýbají. Toto oddělení zajišťuje, že multimediální provoz s vysokou šířkou pásma nezatěžuje koordinační entitu. MCE je základním kamenem efektivity eMBMS, který mění skupinu jednotlivých buněk v jednotnou, synchronizovanou broadcastovou síť.

## K čemu slouží

MCE byla vytvořena k vyřešení základního koordinačního problému, který je vlastní implementaci Single Frequency Network (SFN) pro broadcast v rámci buněčné architektury. V tradiční unicastové buněčné síti pracuje každá buňka nezávisle a plánuje zdroje pro své připojené UE. Pro broadcast, kde musí být stejný obsah doručován z mnoha buněk současně, by tato nezávislá činnost vedla ke chaosu: buňky by používaly různé rádiové parametry (MCS, časování), což by způsobovalo destruktivní interference na hranicích buněk a znemožňovalo UE kombinovat signály. MCE poskytuje nezbytnou centralizovanou kontrolu rádiových zdrojů, aby tento problém překonala.

Před standardizovanou MCE v LTE Release 9 měla MBMS v UMTS (Release 6) omezené multicastové schopnosti a nepodporovala skutečný SFN provoz ve velkém měřítku, což vedlo k nižší spektrální efektivitě a mezerám v pokrytí. Zavedení eMBMS s MBSFN v LTE slibovalo významné zisky ve spektrální efektivitě a pokrytí pro broadcastové služby, ale vyžadovalo nový architektonický prvek, aby se tento slib naplnil. MCE byla tímto prvkem, navrženým k centrální správě 'synchronizovaného' aspektu MBSFN.

Její účel přesahuje pouhou synchronizaci. Také optimalizuje využití vzácných rádiových zdrojů pro MBMS. Tím, že centrálně rozhoduje o MCS a alokaci zdrojů, může MCE zvolit nejrobustnější parametry, které vyhovují i nejhoršímu případu UE na okraji oblasti MBSFN, a tím zajistit kontinuitu služby pro všechny účastníky. Také umožňuje efektivní statistický multiplex více služeb MBMS na sdílené rádiové zdroje (MCH). Bez MCE by bylo dosažení konzistentního, efektivního a spolehlivého broadcastu napříč více-dodavatelským RAN extrémně obtížné, protože každý eNodeB by vyžadoval složité peer-to-peer koordinační protokoly. MCE tuto složitost abstrahuje, poskytuje jediný bod kontroly a umožňuje škálovatelné nasazení broadcastových služeb, jako je mobilní TV a oznámení pro veřejnou bezpečnost, přes LTE sítě.

## Klíčové vlastnosti

- Centralizovaná správa a alokace rádiových zdrojů pro všechny eNodeB v oblasti MBSFN.
- Určuje společné rádiové parametry včetně MCS, alokace MBSFN subframů a plánovací periody MCH.
- Implementuje přístupovou kontrolu pro MBMS relace na základě dostupných rádiových zdrojů v oblasti.
- Komunikuje s eNodeB přes rozhraní M2 s využitím protokolu M2AP pro distribuci konfigurace.
- Komunikuje s MBMS Gateway v core síti přes rozhraní M3 pro řízení relací.
- Zajišťuje dokonale synchronizované parametry přenosu pro konstruktivní skládání signálů v SFN provozu.

## Související pojmy

- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MBMS-GW – MBMS Gateway](/mobilnisite/slovnik/mbms-gw/)
- [MCH – Multast Channel](/mobilnisite/slovnik/mch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.246** (Rel-19) — MBMS Bearer Service Stage 2 Description
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 28.405** (Rel-19) — QoE Measurement Control & Configuration
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.440** (Rel-19) — E-UTRAN MBMS Architecture Description
- **TS 36.444** (Rel-19) — M3AP Protocol Specification for M3 Interface
- **TS 36.896** (Rel-14) — Study on Flexible eNB-ID and Cell-ID in E-UTRAN
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.890** (Rel-17) — NR QoE Management and Optimization

---

📖 **Anglický originál a plná specifikace:** [MCE na 3GPP Explorer](https://3gpp-explorer.com/glossary/mce/)
