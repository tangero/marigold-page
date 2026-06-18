---
slug: "ssdt"
url: "/mobilnisite/slovnik/ssdt/"
type: "slovnik"
title: "SSDT – Site Selection Diversity Transmission"
date: 2025-01-01
abbr: "SSDT"
fullName: "Site Selection Diversity Transmission"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ssdt/"
summary: "Technika přenosové diverzity používaná ve WCDMA/UMTS ke zlepšení výkonu na downlinku a snížení interference. Umožňuje UE dynamicky vybírat nejlepší buňku pro přenos, čímž zvyšuje kvalitu signálu a kap"
---

SSDT je technika přenosové diverzity WCDMA/UMTS, při které UE dynamicky vybírá nejvhodnější buňku pro downlinkový přenos za účelem zlepšení kvality signálu, snížení interference a zvýšení kapacity sítě.

## Popis

Site Selection Diversity Transmission (SSDT) je specifická forma přenosové diverzity s výběrem místa definovaná ve standardech 3GPP UMTS, primárně pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)). Funguje během měkkého předávání, což je stav, kdy je uživatelské zařízení (UE) současně připojeno k více Node Bs (buňkám) ve své aktivní sadě. Základní princip SSDT spočívá v určení jedné z těchto buněk jako „primární“ pro downlinkový přenos v daném okamžiku, zatímco ostatní buňky v aktivní sadě dočasně utlumí nebo výrazně sníží svůj vysílací výkon pro dané UE. Tento výběr není statický; UE kontinuálně vyhodnocuje kvalitu přijímaného signálu od každé buňky ve své aktivní sadě a dynamicky signalizuje zpět do sítě, kterou buňku nominuje jako primární. Tato zpětná vazba je odesílána prostřednictvím uplinkového Dedicated Physical Control Channel ([DPCCH](/mobilnisite/slovnik/dpcch/)) pomocí krátkého, předem definovaného identifikačního kódu pro vybranou buňku.

Síť po přijetí tohoto ID primární buňky od UE instruuje nominovaný Node B, aby vysílal vyhrazené downlinkové kanály (jako [DPCH](/mobilnisite/slovnik/dpch/)) k tomuto UE na plný výkon. Ostatní neprimární Node Bs v aktivní sadě přepnou do režimu nízkého výkonu, často vysílají pouze nezbytné řídicí kanály nebo nízkovýkonový pilotní signál, čímž efektivně fungují jako záloha. Tento mechanismus snižuje celkovou downlinkovou interferenci v síti, protože více buněk nesoučasně nevysílá na plný výkon ke stejnému UE. Také šetří vysílací výkonové zdroje Node B. Kontinuální monitorování a rychlá zpětná vazba UE (v řádu milisekund) umožňují SSDT sledovat podmínky rychlého útlumu a zajišťují, že buňka s momentálně nejlepším rádiovým spojením aktivně přenáší uživatelská data.

Z architektonického hlediska je funkce SSDT rozdělena mezi UE a Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)). UE provádí měření kvality kanálu a generuje zpětnou vazbu s ID primární buňky. RNC konfiguruje parametry SSDT (jako sadu povolených ID primárních buněk a časování zpětné vazby) prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a spravuje aktivní sadu. Avšak provedení snížení výkonu v neprimárních buňkách je řízeno přímo Node Bs na základě uplinkové signalizace od UE, což umožňuje rychlou reakci bez zapojení RNC pro každé přepnutí. Klíčové součásti zahrnují měřicí a zpětnovazební jednotku UE, uplinkový DPCCH pro signalizaci primárního ID, jednotku řízení výkonu Node B a [RRM](/mobilnisite/slovnik/rrm/) algoritmy RNC pro celkový dohled a parametrizaci.

## K čemu slouží

SSDT bylo zavedeno k řešení specifických výzev vlastních mechanismu měkkého předávání v sítích [WCDMA](/mobilnisite/slovnik/wcdma/)/UMTS. Zatímco měkké předávání poskytuje významný zisk diverzity na uplinku a plynulou mobilitu tím, že umožňuje UE připojit se k více buňkám, vytváří zásadní nevýhodu na downlinku: stejná data jsou přenášena z více buněk, což spotřebovává dodatečný vysílací výkon sítě a vytváří nadměrnou downlinkovou interferenci. Tato interference snižuje celkovou kapacitu systému a může zhoršovat zážitek ostatních uživatelů v síti. Před technikami jako je SSDT měla síť omezené možnosti, jak tento „downlinkový overhead měkkého předávání“ zmírnit.

Hlavní motivací pro SSDT bylo zachovat výhody pokrytí a spolehlivosti měkkého předávání při radikálním snížení jeho downlinkové ceny. Dynamickým výběrem pouze nejlepší buňky pro primární přenos SSDT minimalizuje celkový vysílací výkon směřující k jednomu UE. To přímo vede k nižší intraceliové a intercelulární interferenci, která je limitujícím faktorem kapacity WCDMA. Uvolněné výkonové zdroje pak mohou být přiděleny jiným uživatelům, čímž se zvýší celkový počet podporovaných spojení nebo se zlepší jejich přenosové rychlosti. Navíc, z pohledu UE, je příjem silného signálu z jedné buňky často lepší než příjem více signálů střední síly, potenciálně interferujících, z několika buněk, což vede ke zlepšení výkonnosti downlinkové chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)).

Historicky SSDT představovalo vývoj od jednodušších schémat přenosové diverzity. Poskytovalo inteligentní, sítí asistovanou formu selektivní diverzity, která byla těsně integrována s procedurami měkkého předávání WCDMA. Jeho vytvoření bylo hnací potřebou spektrálně efektivnějšího provozu v sítích UMTS, zejména když se začaly objevovat datové služby. Řešilo problém neefektivního využití výkonu během měkkého předávání, stavu, ve kterém UE mohly trávit významnou část času, aniž by přidávalo nadměrnou složitost UE nebo vyžadovalo zásadní změny v architektuře core sítě.

## Klíčové vlastnosti

- Dynamický výběr primární buňky prováděný UE na základě měření kanálu v reálném čase
- Rychlá zpětná vazba ID primární buňky prostřednictvím uplinkového DPCCH pomocí krátkých kódů
- Snížení vysílacího výkonu v neprimárních Node Bs během měkkého předávání
- Významné snížení downlinkové interference, což zvyšuje kapacitu sítě
- Zlepšení kvality downlinkového signálu a chybovosti bloků (BLER) pro UE
- Plynulá integrace s existujícími procedurami měkkého předávání a řízení výkonu UMTS

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SSDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssdt/)
