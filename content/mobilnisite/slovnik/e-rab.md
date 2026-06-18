---
slug: "e-rab"
url: "/mobilnisite/slovnik/e-rab/"
type: "slovnik"
title: "E-RAB – E-UTRAN Radio Access Bearer"
date: 2025-01-01
abbr: "E-RAB"
fullName: "E-UTRAN Radio Access Bearer"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-rab/"
summary: "Logické spojení v LTE/5G NR, které poskytuje garantovaný tok dat s QoS mezi UE a jádrem sítě (EPC/5GC). Jedná se o zřetězení radiového přenosového kanálu přes rozhraní Uu a přenosového kanálu S1 přes"
---

E-RAB je logické spojení v LTE/5G NR, které zajišťuje garantovaný tok dat s QoS mezi UE a jádrem sítě prostřednictvím zřetězení radiového přenosového kanálu (radio bearer) a přenosového kanálu S1 (S1 bearer).

## Popis

[E-UTRAN](/mobilnisite/slovnik/e-utran/) Radio Access Bearer (E-RAB) je základním konceptem architektury Evolved Packet System (EPS) a představuje logickou přenosovou cestu pro data uživatelské roviny se specifickými charakteristikami kvality služby (QoS). Je zřizován mezi uživatelským zařízením (UE) a Serving Gateway ([S-GW](/mobilnisite/slovnik/s-gw/)) v EPS, respektive User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC. E-RAB je jednoznačně identifikován identifikátorem E-RAB ID a v podstatě se jedná o zřetězení dvou podkladových přenosových kanálů: radiového přenosového kanálu ([RB](/mobilnisite/slovnik/rb/)) přes rozhraní Uu (vzdušné) mezi UE a eNodeB/gNB a přenosového kanálu S1 (nebo N3 v 5G) přes rozhraní [S1-U](/mobilnisite/slovnik/s1-u/) (nebo N3) mezi eNodeB/gNB a S-GW/UPF. Jádro sítě, konkrétně [MME](/mobilnisite/slovnik/mme/) (nebo [AMF](/mobilnisite/slovnik/amf/) v 5G), je zodpovědné za zřizování, modifikaci a uvolňování E-RAB na základě požadavků správy relace, které jsou typicky spouštěny zřízením připojení [PDN](/mobilnisite/slovnik/pdn/) nebo procedurou aktivace vyhrazeného přenosového kanálu iniciovanou funkcí Policy and Charging Rules Function (PCRF) nebo Policy Control Function (PCF). eNodeB/gNB je zodpovědný za aspekt správy radiových prostředků, což zahrnuje mapování požadavků QoS E-RAB (např. QCI, ARP, GBR, MBR) na příslušné radiové konfigurace, algoritmy plánování a linkové protokoly, aby byly splněny požadované výkonnostní parametry. Životní cyklus E-RAB je úzce spjat s mobilitou UE; během procedur předávání řízení (handover) jsou E-RAB spravovány tak, aby byla zajištěna kontinuita služby, přičemž cílový uzel připravuje prostředky předtím, než je uvolní uzel zdrojový. Tato architektura založená na přenosových kanálech poskytuje jasné oddělení řídicí a uživatelské roviny a umožňuje efektivní zpracování provozu s ohledem na QoS napříč celou cestou přes rádiový přístup a jádro sítě.

## K čemu slouží

E-RAB byl zaveden spolu s LTE ve 3GPP Release 8, aby poskytl zjednodušený, plně IP model přenosového kanálu pro paketově orientované služby, který nahradil složitější koncepty přenosových kanálů orientované na přepojování okruhů z 2G/3G (jako Radio Access Bearers a Radio Bearers v UMTS). Jeho primárním účelem je vytvořit jasný, kvalitou služeb (QoS) garantovaný přenosový kanál pro uživatelský datový provoz, který pokrývá rádiovou přístupovou síť a bezproblémově se napojuje na transportní tunely jádra sítě. Tím se řeší problém poskytování konzistentní, od konce ke konci zajištěné kvality služby pro různé aplikace (např. VoIP, streamování videa, prohlížení webu) přes sdílenou paketovou infrastrukturu. Definováním E-RAB jako klíčové datové cesty specifické pro účastníka a službu může síť uplatňovat přesné zásady správy provozu, prioritizace a účtování. Architektura také odděluje konfigurace specifické pro rádiové rozhraní od transportu v jádru sítě, což zjednodušuje vývoj sítě a umožňuje nezávislou optimalizaci rádiové a transportní vrstvy. Koncept E-RAB je klíčový pro dosažení cíle EPS v podobě vyšších přenosových rychlostí, nižší latence a efektivnějšího využití prostředků ve srovnání s předchozími systémy 3GPP.

## Klíčové vlastnosti

- Logické spojení od konce ke konci mezi UE a S-GW/UPF
- Jednoznačně identifikován identifikátorem E-RAB ID
- Zřetězení radiového přenosového kanálu (Radio Bearer) a přenosového kanálu S1/N3 (S1/N3 bearer)
- Přenáší specifický tok QoS definovaný parametry QCI/5QI a dalšími
- Spravován MME/AMF prostřednictvím signalizace S1-AP/N2
- Podporuje procedury zřizování, modifikace a uvolňování

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 32.450** (Rel-19) — E-UTRAN Key Performance Indicators (KPI) Definitions
- **TS 32.451** (Rel-19) — KPI Requirements for E-UTRAN
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.414** (Rel-19) — S1 Interface User Plane Transport
- **TS 36.420** (Rel-19) — X2 Interface Introduction for E-UTRAN
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 36.424** (Rel-19) — X2 Interface User Plane Transport Protocols
- **TS 36.425** (Rel-19) — X2 User Plane Protocol for Dual Connectivity
- **TS 36.444** (Rel-19) — M3AP Protocol Specification for M3 Interface
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [E-RAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-rab/)
