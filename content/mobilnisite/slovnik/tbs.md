---
slug: "tbs"
url: "/mobilnisite/slovnik/tbs/"
type: "slovnik"
title: "TBS – Terrestrial Beacon Systems"
date: 2026-01-01
abbr: "TBS"
fullName: "Terrestrial Beacon Systems"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tbs/"
summary: "TBS jsou pozemní majákové signály používané pro určování polohy, časování a synchronizaci v mobilních sítích. Zlepšují služby založené na poloze, koordinaci sítě a podporují technologie jako Assisted"
---

TBS je systém pozemních majákových signálů používaný pro určování polohy, časování a synchronizaci v mobilních sítích za účelem vylepšení lokalizačních služeb a koordinace sítě.

## Popis

Terrestrial Beacon Systems (TBS) označují pozemní majákové signály nasazené v mobilních sítích za účelem poskytování služeb určování polohy, časování a synchronizace. Tyto systémy vysílají známé referenční signály z pevných pozemních lokalit, které může uživatelské zařízení (UE) detekovat a měřit, aby určilo svou polohu nebo se synchronizovalo se sítí. TBS funguje napříč různými technologiemi 3GPP, včetně UMTS, LTE a 5G NR, a je specifikováno v řadě technických specifikací, jako jsou TS 22.071, TS 36.213 a TS 38.305. Architektura zahrnuje majákové vysílače strategicky umístěné v síťové infrastruktuře, často integrované s základnovými stanicemi nebo jako samostatné jednotky, které vysílají signály nesoucí informace o čase a poloze.

Princip fungování TBS spočívá v tom, že UE přijímá majákové signály z více pozemních zdrojů. Měřením parametrů, jako je čas příchodu ([TOA](/mobilnisite/slovnik/toa/)), časový rozdíl příchodu (TDOA) nebo síla signálu, může UE vypočítat svou polohu pomocí triangulace nebo multilaterace. Tato měření jsou často kombinována se satelitními systémy, jako je [GPS](/mobilnisite/slovnik/gps/), pro zvýšení přesnosti, čímž vznikají hybridní lokalizační řešení. Klíčové komponenty zahrnují majákový vysílač, který generuje a vysílá standardizované signály; přijímač v UE, který tyto signály zpracovává; a síťové entity, jako je Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)), které pomáhají s výpočtem polohy a správou dat.

TBS hraje klíčovou roli při umožňování vysoce přesných lokalizačních služeb, zejména v prostředích, kde jsou satelitní signály slabé nebo nedostupné, jako jsou vnitřní prostory nebo městské kaňony. Podporuje různé aplikace včetně služeb tísňového volání (např. E-911), navigace, sledování majetku a optimalizace sítě. Integrace systému s mobilními sítěmi umožňuje plynulý přechod mezi různými metodami určování polohy a zajišťuje nepřetržitou dostupnost služeb. Poskytováním spolehlivých pozemních referencí TBS zvyšuje celkovou robustnost a přesnost služeb založených na poloze v moderní telekomunikaci.

## K čemu slouží

TBS bylo vyvinuto, aby řešilo omezení satelitních lokalizačních systémů, jako je [GPS](/mobilnisite/slovnik/gps/), které mohou trpět blokací signálu ve vnitřních nebo hustě zastavěných městských oblastech. Potřeba spolehlivých, vysoce přesných lokalizačních služeb pro tísňová volání, navigaci a komerční aplikace motivovala vytvoření pozemních doplňkových systémů. TBS poskytuje komplementární řešení, které zajišťuje dostupnost určování polohy i při degradaci satelitních signálů, čímž zlepšuje bezpečnost uživatelů a kvalitu služeb.

Historicky měly rané mobilní sítě omezené lokalizační schopnosti, spoléhající se primárně na metody buněčného ID nebo časového předstihu s nízkou přesností. Zavedení TBS ve 3GPP Release 4 představovalo významný pokrok, umožňující přesnější určování polohy pomocí pozemních majáků. Tím byly splněny regulační požadavky na služby tísňového volání, jako jsou nařízení [FCC](/mobilnisite/slovnik/fcc/) pro E-911, která vyžadovala zlepšenou přesnost lokalizace. TBS také podporuje potřeby synchronizace sítě, napomáhající koordinovanému vícebodovému přenosu a správě rušení.

Integrací pozemních majáků mohou systémy 3GPP nabízet hybridní určování polohy, které kombinuje výhody satelitních i pozemních technologií. Tím se řeší problémy související s mezerami v pokrytí a vylepšují se aplikace jako sledování majetku v IoT, autonomní vozidla nebo reklama založená na poloze. Vývoj TBS napříč jednotlivými releasy odráží pokračující snahy o zlepšení přesnosti, snížení latence a podporu nových případů užití ve stále více propojeném světě.

## Klíčové vlastnosti

- Poskytuje pozemní referenční zdroje pro určování polohy a časování
- Podporuje hybridní určování polohy se satelitními systémy, jako je GPS
- Zvyšuje přesnost lokalizace ve vnitřních a městských prostředích
- Umožňuje synchronizaci a koordinaci sítě
- Integruje se s mobilní infrastrukturou pro plynulý provoz
- Podporuje služby tísňového volání a splnění regulatorních požadavků

## Související pojmy

- [A-GPS – Assisted Global Positioning System](/mobilnisite/slovnik/a-gps/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.878** (Rel-18) — Technical Report on 5G Timing Resiliency
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 25.874** (Rel-11) — HSPA Feedback & Signalling Efficiency for LCR TDD
- **TS 33.814** (Rel-16) — Security aspects of enhanced Location Services (eLCS)
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [TBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tbs/)
