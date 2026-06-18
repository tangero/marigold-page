---
slug: "pb"
url: "/mobilnisite/slovnik/pb/"
type: "slovnik"
title: "PB – Power Boosting"
date: 2025-01-01
abbr: "PB"
fullName: "Power Boosting"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pb/"
summary: "Technika, při které síť zvýší vysílací výkon na specifických blocích fyzických zdrojů nebo referenčních signálech v poměru k ostatním. Používá se ke zlepšení pokrytí, zvýšení kvality signálu pro uživa"
---

PB je technika, při které síť zvýší vysílací výkon na konkrétních blocích fyzických zdrojů nebo referenčních signálech za účelem zlepšení pokrytí, kvality signálu nebo zvýšení priority důležitých kanálů.

## Popis

Power Boosting (PB) je technika přidělování výkonu v downlinku používaná v systémech založených na [OFDMA](/mobilnisite/slovnik/ofdma/), jako jsou LTE a NR. V těchto systémech je celkový dostupný vysílací výkon základnové stanice (eNodeB/gNodeB) rozdělen mezi časově-frekvenční zdroje (Resource Blocks) a mezi různé fyzické kanály a referenční signály. Power Boosting označuje záměrné přidělení vyššího podílu tohoto celkového výkonu konkrétní podmnožině těchto zdrojů ve srovnání s nominální nebo základní úrovní výkonu. Nejde o zvýšení celkového výstupního výkonu základnové stanice, ale o přerozdělení dostupného výkonu ve prospěch určitých zdrojů.

Z architektonického hlediska je power boosting řízen plánovačem základnové stanice a algoritmy regulace výkonu. Systém definuje parametr, často označovaný jako faktor nebo poměr power boostingu, který určuje úroveň výkonu pro zvýhodněné zdroje vzhledem k ostatním zdrojům. Například v LTE lze výkon buněčně specifických referenčních signálů ([CRS](/mobilnisite/slovnik/crs/)) zvýšit (boostnout) za účelem zlepšení přesnosti odhadu kanálu, zejména na okraji buňky. Podobně mohou být zvýšeny synchronizační signály ([PSS](/mobilnisite/slovnik/pss/)/[SSS](/mobilnisite/slovnik/sss/)) nebo Physical Broadcast Channel ([PBCH](/mobilnisite/slovnik/pbch/)) pro rozšíření dosahu pro detekci buňky. Technika funguje tak, že se sníží výkon přidělený některým blokům zdrojů nebo symbolům, čímž se „uvolní“ výkonový rozpočet, který je následně přidán cílovým zdrojům při dodržení celkového výkonového omezení.

Mezi klíčové součásti patří výkonový zesilovač, plánovač na základnovém pásmu a definované vzorce pro přidělování výkonu ve specifikacích fyzické vrstvy. Například 3GPP TS 36.213 definuje přidělování výkonu pro Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) v přítomnosti CRS. Pokud je nakonfigurován CRS boosting, zvýší se výkon na prvek zdroje ([EPRE](/mobilnisite/slovnik/epre/)) pro CRS, což může vést k odpovídajícímu snížení EPRE pro PDSCH data v prvcích zdrojů, které se časově a frekvenčně překrývají s pozicemi CRS. Tento kompromis je pečlivě řízen, aby byla vyvážena kvalita referenčního signálu pro všechny uživatele a datová propustnost pro konkrétní uživatele. Jeho role je klíčová pro optimalizaci sítě, neboť umožňuje operátorům dynamicky tvarovat oblast pokrytí, zlepšovat výkonnost pro služby s vysokou prioritou a zvyšovat celkovou robustnost systému, zejména v heterogenních nasazeních sítě s malými buňkami.

## K čemu slouží

Power Boosting existuje pro řešení kompromisů mezi pokrytím a kapacitou v mobilních sítích, zejména pro uživatele na okraji buňky, kteří mají nízký poměr signálu k šumu a interferenci ([SINR](/mobilnisite/slovnik/sinr/)). Základním omezením je, že základnová stanice má konečný celkový vysílací výkon. Bez boostingu je tento výkon typicky rozprostřen rovnoměrně mezi všechny subnosné, což nemusí být optimální pro kanály klíčové pro počáteční přístup nebo pro uživatele ve špatných rádiových podmínkách. Power Boosting umožňuje síti strategicky koncentrovat výkon tam, kde je nejvíce potřeba.

Historicky byla tato technika motivována potřebou zlepšit výkonnost vysílacích a společných kanálů, které musí přijímat všichni uživatelé v buňce, jako jsou synchronizační signály a bloky systémových informací. V časných nasazeních LTE měli uživatelé na okraji buňky často potíže s dekódováním PBCH, což omezovalo poloměr buňky. Zvýšením výkonu na těchto kanálech mohli operátoři rozšířit pokrytí bez zvýšení celkového vyzařovaného výkonu, který je často omezen regulačními požadavky. Tato technika také řeší problém pilotní interference v hustých sítích; zvýšení výkonu buněčně specifických referenčních signálů (CRS) může zlepšit přesnost měření pro handover a výběr buňky.

Dále Power Boosting umožňuje sofistikovanější koordinaci interference v heterogenních sítích (HetNets). Například makrobuňka může snížit výkon (nebo použít negativní boosting, tj. snížení výkonu) na určitých blocích zdrojů, aby vytvořila chráněnou oblast pro uživatele pikobuňky, a zároveň zvýšit výkon na jiných zdrojích, aby udržela pokrytí pro své vlastní uživatele. Toto dynamické přidělování výkonu je klíčovým nástrojem pro Enhanced Inter-Cell Interference Coordination (eICIC) a další techniky řízení interference. Poskytuje síťovým operátorům zásadní stupeň volnosti pro optimalizaci řízení rádiových zdrojů, vyvažování zatížení a zlepšení kvality služeb pro konkrétní aplikace nebo skupiny uživatelů, což z něj činí nezbytnou funkci pro moderní a efektivní provoz RAN.

## Klíčové vlastnosti

- Dynamické přerozdělení dostupného vysílacího výkonu mezi časově-frekvenční zdroje
- Používá se ke zvýšení výkonu konkrétních kanálů, jako jsou CRS, PSS/SSS, PBCH nebo PDSCH, pro určité uživatele
- Definováno konfigurovatelnými poměry výkonu nebo offsetů v RRC signalizaci
- Musí fungovat v rámci celkového omezení vysílacího výkonu základnové stanice
- Klíčový prostředek pro rozšíření pokrytí a techniky řízení interference, jako je eICIC
- Specifikováno v postupech fyzické vrstvy pro přidělování výkonu (např. TS 36.213, 38.213)

## Související pojmy

- [EPRE – Energy Per Resource Element](/mobilnisite/slovnik/epre/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.116** (Rel-19) — LCR TDD Repeater RF Characteristics
- **TR 28.832** (Rel-18) — Technical Report on URLLC Management
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [PB na 3GPP Explorer](https://3gpp-explorer.com/glossary/pb/)
