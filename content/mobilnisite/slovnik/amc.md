---
slug: "amc"
url: "/mobilnisite/slovnik/amc/"
type: "slovnik"
title: "AMC – Adaptive Modulation and Coding"
date: 2025-01-01
abbr: "AMC"
fullName: "Adaptive Modulation and Coding"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/amc/"
summary: "AMC je technika adaptace spojení, která dynamicky upravuje řád modulace a rychlost kódování kanálu na základě aktuálních podmínek rádiového kanálu. Optimalizuje spektrální účinnost a propustnost přizp"
---

AMC je technika adaptace spojení, která dynamicky upravuje modulaci a kódování na základě aktuálních podmínek rádiového kanálu za účelem optimalizace spektrální účinnosti a propustnosti v mobilních sítích.

## Popis

Adaptive Modulation and Coding (AMC) je základní mechanismus fyzické vrstvy v bezdrátových systémech 3GPP, který primárně funguje v protokolech řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a fyzické vrstvy základnové stanice (eNodeB v LTE, gNB v NR). Jeho hlavní funkcí je odhadnout okamžitou kvalitu rádiového kanálu pro každé uživatelské zařízení (UE), typicky pomocí metrik jako je zpětná vazba indikátoru kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), a následně vybrat nejvhodnější kombinaci modulačního schématu (např. [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM, 1024QAM) a rychlosti kódování pro korekci chyb ([FEC](/mobilnisite/slovnik/fec/)) (např. od robustních kódů s nízkou rychlostí po efektivní kódy s vysokou rychlostí). Tento výběr si klade za cíl maximalizovat datovou propustnost při zachování cílové míry chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)), často kolem 10 %. Proces je kontinuální a probíhá pro každý přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/)) nebo slot, což systému umožňuje sledovat a reagovat na rychlé útlumy, změny rušení a změny v mobilitě uživatele.

Architektura zahrnuje úzkou interakci mezi UE a základnovou stanicí. UE měří kvalitu downlink kanálu, často na základě referenčních signálů jako CSI-RS, a hlásí index CQI základnové stanici prostřednictvím řídicích kanálů uplink. Tento index CQI odpovídá doporučenému schématu modulace a kódování (MCS), které je UE schopno dekódovat s přijatelnou spolehlivostí. Plánovač základnové stanice pak tuto informaci spolu s dalšími faktory, jako jsou dostupné zdroje a požadavky QoS, použije k finálnímu určení MCS pro následný downlink přenos. Zvolené MCS určuje velikost transportního bloku (TBS), což definuje, kolik datových bitů lze odeslat v rámci zdrojového bloku. V uplink probíhá podobný proces, kdy základnová stanice odhaduje kvalitu kanálu ze zkušebních referenčních signálů (SRS) a přidělí UE odpovídající MCS.

Klíčovými komponentami umožňujícími AMC jsou mechanismus hlášení CQI, tabulky MCS definované ve specifikacích 3GPP (které mapují indexy CQI/MCS na konkrétní modulaci a rychlosti kódování) a protokol hybridního automatického opakování (HARQ). HARQ poskytuje záchrannou síť; pokud přenos s příliš agresivním MCS selže, může být opakován, často s inkrementální redundancí. Role AMC je klíčová pro dosažení vysokých špičkových přenosových rychlostí a spektrální účinnosti slibovaných standardy 3GPP. Je to primární nástroj pro řízení kompromisu mezi datovou rychlostí a robustností přenosu, což přímo ovlivňuje uživatelský zážitek a kapacitu sítě. Jeho účinnost je základní pro funkce jako agregace nosných a MIMO, protože umožňuje nezávislou optimalizaci každé komponentní nosné nebo prostorové vrstvy.

## K čemu slouží

AMC bylo vytvořeno, aby řešilo základní výzvu časově proměnné a na umístění závislé povahy bezdrátového kanálu. Rané bezdrátové systémy používaly pevnou modulaci a kódování, které byly buď příliš konzervativní (plýtvaly kapacitou za dobrých podmínek), nebo příliš agresivní (způsobovaly vysokou míru chyb za špatných podmínek). Tato neefektivita omezovala jak špičkové datové rychlosti, tak celkovou kapacitu buňky. AMC to řeší zavedením inteligence a adaptability, což systému umožňuje "surfovat na vlnách" kvality kanálu: používat robustní modulaci nízkého řádu (QPSK) se silným kódováním při špatných podmínkách signálu k udržení konektivity a přepínat na modulaci vysokého řádu (např. 256QAM) s kódováním vysoké rychlosti za výborných podmínek k dosažení maximální propustnosti.

Historicky bylo jeho zavedení v 3GPP Release 8 (LTE) klíčovým prvkem pro skok k plně IP, vysokorychlostním paketovým datovým sítím. Řešilo to omezení dřívějších systémů 3G (UMTS), které jako hlavní prostředek pro potlačování útlumu používaly rychlé řízení výkonu. Zatímco řízení výkonu je efektivní pro hovory s přepojováním okruhů, je pro paketová data neefektivní, protože vytváří nadměrné rušení. AMC v kombinaci s HARQ a plánováním ve frekvenční oblasti vytvořilo základ pro efektivnější provoz na sdíleném kanálu v LTE a NR. Motivací bylo maximalizovat využití vzácného a drahého rádiového spektra, což je hnací cíl všech generací mobilních sítí, a to zajištěním, aby každý přenos využíval nejvyšší možnou datovou rychlost, kterou kanál v daném okamžiku spolehlivě podporuje.

## Klíčové vlastnosti

- Dynamický výběr modulačních schémat (od QPSK po 1024QAM)
- Adaptivní nastavení rychlosti kódování kanálu (např. Turbo kódy, LDPC)
- Závislost na zpětné vazbě indikátoru kvality kanálu (CQI) v reálném čase
- Těsná integrace s hybridním ARQ (HARQ) pro opravu chyb
- Adaptace pro každého uživatele a každý přenosový interval
- Základ pro cíle spektrální účinnosti a špičkové datové rychlosti

## Související pojmy

- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 25.706** (Rel-13) — Downlink Enhancements for UMTS Study
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 36.942** (Rel-19) — E-UTRA System Scenarios Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [AMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/amc/)
