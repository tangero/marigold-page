---
slug: "lqc"
url: "/mobilnisite/slovnik/lqc/"
type: "slovnik"
title: "LQC – Link Quality Control"
date: 2025-01-01
abbr: "LQC"
fullName: "Link Quality Control"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lqc/"
summary: "Link Quality Control (LQC) je mechanismus používaný v GSM/EDGE rádiové přístupové síti (GERAN) k optimalizaci výkonu rádiového spoje. Zahrnuje monitorování a úpravu přenosových parametrů, jako je říze"
---

LQC je mechanismus v sítích GSM/EDGE, který optimalizuje výkon rádiového spoje monitorováním kvality kanálu a úpravou přenosových parametrů, jako je řízení výkonu, za účelem zachování kvality hovoru a spektrální účinnosti.

## Popis

Link Quality Control (LQC) je základní funkcí v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové sítě ([GERAN](/mobilnisite/slovnik/geran/)), specifikovaná v dokumentu 3GPP TS 45.912. Jejím hlavním úkolem je udržovat a optimalizovat kvalitu rádiového spoje mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) v dynamickém rádiovém prostředí. LQC funguje tak, že průběžně shromažďuje měřicí hlášení jak od MS, tak od BTS. Tato hlášení obsahují klíčové metriky, jako je úroveň přijímaného signálu ([RXLEV](/mobilnisite/slovnik/rxlev/)), kvalita přijímaného signálu ([RXQUAL](/mobilnisite/slovnik/rxqual/)) a časový předstih. Síť, konkrétně řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), tato měření zpracovává, aby mohla činit rozhodnutí o přenosových parametrech v reálném čase.

Mezi základní mechanismy LQC patří Řízení výkonu a Řízení předávání spojení. Řízení výkonu dynamicky upravuje vysílací výkon MS a BTS tak, aby byla použita minimální nutná síla pro udržení přijatelné kvality spoje. Tím se snižuje interference, šetří se kapacita baterie v MS a zvyšuje se celková kapacita sítě. Řízení předávání spojení využívá měření kvality k rozhodnutí, kdy převést probíhající hovor z jedné buňky do druhé (např. kvůli zhoršující se síle nebo kvalitě signálu), aby byla zajištěna kontinuita služby. BSC vyhodnocuje měřicí hlášení vůči předdefinovaným prahovým hodnotám a algoritmům, aby tyto akce spustil.

LQC je hluboce integrováno do procedur správy rádiových prostředků GSM. Funguje ve spolupráci s dalšími funkcemi, jako je nespojitý přenos ([DTX](/mobilnisite/slovnik/dtx/)) a přeskakování kmitočtů. Algoritmy pro LQC jsou implementovány v softwaru BSC a využívají vstupy z měřicích procedur vrstvy 1 definovaných v rádiových specifikacích. Jeho role je klíčová pro autonomní a efektivní správu rádiového rozhraní, neboť zajišťuje spolehlivé hlasové a datové služby při maximalizaci využití omezeného rádiového spektra.

## K čemu slouží

Link Quality Control byl vytvořen, aby řešil základní výzvy spojené s poskytováním spolehlivých mobilních hlasových služeb přes sdílené, k interferencím náchylné rádiové médium. Rané mobilní rádiové systémy trpěly problémy, jako je interference na stejném a sousedním kanálu, rychlé úniky signálu a omezená kapacita baterií v přístrojích. Bez dynamického řízení by hovory často přerušovaly, kvalita by byla špatná a kapacita sítě by byla výrazně omezena.

Zavedení LQC v GSM a jeho pokračující definice v pozdějších vydáních včetně vývoje GERAN tyto problémy vyřešilo tím, že umožnilo síti přizpůsobovat se měnícím se rádiovým podmínkám v reálném čase. Automatizovalo optimalizační proces, který by jinak vyžadoval manuální inženýrské zásahy. Minimalizací vysílacího výkonu přímo řešilo interference, což je hlavní faktor omezující kapacitu v celulárních sítích. Řízením předávání spojení na základě kvality udržovalo kontinuitu služeb při pohybu uživatelů. Toto automatizované řízení založené na měření bylo klíčovou inovací, která přispěla ke komerčnímu úspěchu GSM a vysoké spektrální účinnosti sítí 2G.

## Klíčové vlastnosti

- Dynamické řízení výkonu v uplinku a downlinku založené na měřeních RXLEV/RXQUAL
- Algoritmy pro rozhodování o předání spojení založené na měřeních pro zajištění kontinuity služby
- Využití RXQUAL (chybovosti bitů) pro přesné hodnocení kvality spoje
- Integrace s nespojitým přenosem (DTX) pro snížení interference
- Podpora jak pomalých, tak rychlých přidružených řídicích kanálů pro signalizaci
- Provádění algoritmů v řadiči základnových stanic (BSC) pro centralizované řízení

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [RXLEV – Received Signal Level](/mobilnisite/slovnik/rxlev/)
- [RXQUAL – Received Signal Quality](/mobilnisite/slovnik/rxqual/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)

## Definující specifikace

- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [LQC na 3GPP Explorer](https://3gpp-explorer.com/glossary/lqc/)
