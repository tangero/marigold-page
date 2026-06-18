---
slug: "tb"
url: "/mobilnisite/slovnik/tb/"
type: "slovnik"
title: "TB – Terrestrial Beacon"
date: 2025-01-01
abbr: "TB"
fullName: "Terrestrial Beacon"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tb/"
summary: "Pevný terestrický vysílač, který vysílá specifické signály pro účely synchronizace sítě, určování polohy a měření. Poskytuje stabilní referenční bod pro uživatelské zařízení (UE) pro určení jeho poloh"
---

TB je pevný terestrický vysílač, který vysílá signály pro synchronizaci sítě, určování polohy a měření, a poskytuje tak stabilní referenční bod pro uživatelské zařízení a správu rádiových zdrojů.

## Popis

Terestrický maják (Terrestrial Beacon, TB) je klíčová komponenta infrastruktury v sítích 3GPP, navržená jako stacionární, pozemní vysílač. Jeho primární funkcí je vysílat nepřetržité, dobře definované rádiové signály, které slouží jako referenční body v geografické oblasti. Tyto signály nesou specifické informace, jako je jedinečný identifikátor, časová data a potenciálně efemeridy nebo asistenční data. Architektura pro TB je definována v rámci širších rámců pro určování polohy a synchronizace standardů 3GPP, často s rozhraním k polohovým serverům (např. [E-SMLC](/mobilnisite/slovnik/e-smlc/), [LMF](/mobilnisite/slovnik/lmf/)) a uživatelským zařízením. Samotný TB je z protokolového hlediska relativně jednoduchý uzel, zaměřený na spolehlivé vysílání svého majákového signálu na určené nosné frekvenci.

Operační princip spočívá ve schopnosti UE detekovat a měřit signály z jednoho nebo více terestrických majáků. Provedením měření, jako je rozdíl pozorovaného času příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo síla přijímaného signálu ([RSS](/mobilnisite/slovnik/rss/)), může UE nebo síť vypočítat polohu zařízení. Majákové signály jsou navrženy tak, aby byly snadno rozlišitelné od běžných kanálů buněčného provozu, často používají specifické sekvence nebo modulační schémata pro zajištění vysoké pravděpodobnosti detekce a přesnosti měření. Ve scénářích zahrnujících neterestrické sítě ([NTN](/mobilnisite/slovnik/ntn/)) hrají TB klíčovou roli v poskytování terestrického časového referenčního signálu, který pomáhá kompenzovat velké a proměnlivé zpoždění šíření vlastní satelitním spojům, čímž napomáhá časové synchronizaci a procedurám předávání spojení.

Klíčové komponenty systému TB zahrnují hardwarový vysílač majáku, jeho synchronizační zdroj (typicky vysoce stabilní hodiny jako oscilátor řízený [GNSS](/mobilnisite/slovnik/gnss/)) a řídicí a správní rozhraní pro síťové operátory. Jeho role přesahuje čisté určování polohy; podporuje měření pro správu rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)), což umožňuje UE hlásit kvalitu signálu majáku obslužné základnové stanici (gNB/[eNB](/mobilnisite/slovnik/enb/)). Tyto informace mohou být použity pro výběr buňky, rozhodování o mobilitě a optimalizaci sítě. Specifikace podrobně popisují charakteristiky fyzické vrstvy (např. v 38.213, 38.214), měřicí procedury a mechanismy hlášení (např. v 36.355, 38.355), čímž zajišťují interoperabilitu mezi zařízeními různých výrobců.

## K čemu slouží

Terestrický maják byl zaveden, aby řešil rostoucí potřebu přesných a spolehlivých služeb určování polohy v rámci buněčných sítí, což je požadavek vyvolaný regulatorními nařízeními jako E911 a komerčními službami založenými na poloze. Rané metody určování polohy v buněčných sítích, jako je Cell-ID, nabízely špatnou přesnost, zatímco satelitní metody jako samostatný GNSS trpí omezeními v interiérech nebo městských kaňonech. TB poskytuje síťově řízený, terestrický zdroj referenčních signálů pro určování polohy, který je nezávislý na, ale může rozšířit, satelitní signály, čímž vytváří hybridní systém určování polohy pro zlepšenou dostupnost a přesnost.

Dále, s vývojem směrem k integrovaným terestrickým a neterestrickým sítím (NTN) v 5G, se role TB rozšířila. Vysoká mobilita a velké pokrytí satelitů přinášejí významné výzvy pro časovou synchronizaci a určování polohy UE. Síť terestrických majáků poskytuje pevné, známé referenční body na zemi. UE mohou použít měření těchto majáků ke spolehlivějšímu určení své vlastní polohy a k pomoci síti při kompenzaci zpoždění šíření signálu ze satelitů, což je nezbytné pro udržení synchronizace a umožnění efektivního předávání spojení mezi terestrickými a satelitními buňkami.

## Klíčové vlastnosti

- Vysílá stabilní, známé referenční signály pro měření UE
- Umožňuje techniky určování polohy založené na rozdílu pozorovaného času příchodu (OTDOA)
- Poskytuje terestrické časové reference pro synchronizaci neterestrických sítí (NTN)
- Podporuje měření správy rádiových zdrojů (RRM) UE pro mobilitu
- Je definován specifickými sekvencemi fyzické vrstvy pro spolehlivou detekci
- Komunikuje se síťovými polohovými servery (LMF/E-SMLC) pro výpočet polohy

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [TB na 3GPP Explorer](https://3gpp-explorer.com/glossary/tb/)
