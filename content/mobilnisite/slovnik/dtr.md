---
slug: "dtr"
url: "/mobilnisite/slovnik/dtr/"
type: "slovnik"
title: "DTR – Dynamic Timeslot Reduction"
date: 2025-01-01
abbr: "DTR"
fullName: "Dynamic Timeslot Reduction"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dtr/"
summary: "Dynamic Timeslot Reduction (DTR) je funkce GERAN (GSM/EDGE Radio Access Network) zavedená ve specifikaci 3GPP Release 10. Dynamicky snižuje počet časových slotů přidělených mobilní stanici pro přenos"
---

DTR je funkce GERAN, která dynamicky snižuje počet časových slotů přidělených mobilní stanici pro přenos dat, aby optimalizovala využití rádiových zdrojů a přizpůsobila se proměnlivým požadavkům na přenos.

## Popis

Dynamic Timeslot Reduction (DTR) je mechanismus definovaný ve specifikacích [GERAN](/mobilnisite/slovnik/geran/), konkrétně v 3GPP TS 44.060, která řídí protokoly Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) pro rádiové rozhraní [GPRS](/mobilnisite/slovnik/gprs/). Jeho hlavní funkcí je správa přidělování paketových datových kanálů ([PDCH](/mobilnisite/slovnik/pdch/)) přiřazených mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) pro služby GPRS/[EDGE](/mobilnisite/slovnik/edge/). DTR funguje tak, že umožňuje síti dynamicky snížit počet časových slotů v přiřazeném dočasném blokovém toku ([TBF](/mobilnisite/slovnik/tbf/)) MS na základě aktuální datové aktivity a dostupnosti zdrojů.

Z architektonického hlediska je DTR implementováno v podsystému základnové stanice (BSS), což zahrnuje BTS a BSC. BSC monitoruje datový tok na aktivním TBF. Když objem dat poklesne, BSC může zahájit proceduru DTR, aby překonfigurovalo TBF na použití menšího počtu časových slotů. To je signalizováno MS prostřednictvím specifických řídicích zpráv MAC na kanálu PACCH (Packet Associated Control Channel). MS musí podporovat DTR, aby tyto příkazy správně interpretovala a odpovídajícím způsobem upravila svůj příjem/vysílání, přičemž přejde do stavu, kdy monitoruje pouze redukovanou sadu časových slotů.

Procedura je úzce integrována s dalšími funkcemi GERAN, jako je Dynamic Allocation a Extended Dynamic Allocation. Funguje ve spojení s plánovacími algoritmy sítě. Snížením aktivní sady časových slotů uvolňuje DTR zdroje PDCH, které mohou být okamžitě přeřazeny jiným uživatelům, čímž se zvyšuje celková kapacita buňky. Také pomáhá snižovat spotřebu energie v MS, protože přijímač může být aktivní po kratší dobu. Dynamická povaha umožňuje rychlé znovu-rozšíření přidělení časových slotů, pokud se datový provoz z MS opět zvýší, což zajišťuje rychlou reakci na požadavky uživatele bez výrazného přerušení služby.

Úloha DTR je v zásadě o optimalizaci rádiových zdrojů v přepojování okruhů připomínající TDMA struktuře GERAN. V systému, kde jsou fyzické časové sloty omezeným zdrojem, je efektivní přizpůsobení přidělení skutečné potřebě prvořadé pro podporu vysokého počtu současných datových uživatelů. DTR poskytuje BSS podrobný nástroj k dosažení tohoto cíle, posouvá se tak za statická nebo polostatická přidělení směrem k agilnějšímu a efektivnějšímu využití spektra GSM, což je zvláště cenné s tím, jak se datové služby staly na sítích 2G běžnějšími.

## K čemu slouží

DTR bylo vytvořeno k řešení neefektivit vlastních statickému nebo polostatickému přidělování časových slotů pro relace GPRS/EDGE v sítích GERAN. Před DTR mohl být TBF navázán s určitým počtem časových slotů na základě počáteční poptávky nebo profilu předplatného, ale toto přidělení mohlo zůstat po dobu trvání relace fixní, i když se skutečný přenos dat stal sporadickým nebo nízkým. Tento problém „zadržování zdrojů“ znamenal, že cenné PDCH byly monopolizovány uživateli, kteří je plně nevyužívali, což vedlo k zahlcení a blokování pro ostatní uživatele, zejména v buňkách s omezenou kapacitou.

Historický kontext je evoluce sítí GSM směrem k bohatým datovým službám. Jak GPRS a EDGE umožnily mobilní internet, vzorce provozu se oproti hlasu staly více „bursty“ (přerušovanými) a nepředvídatelnými. Síť potřebovala chytřejší mechanismy, aby tento charakter zvládla. DTR bylo motivováno potřebou zlepšit spektrální efektivitu a celkovou kapacitu systému bez nutnosti dodatečného spektra – což je pro operátory kritický požadavek. Umožňuje síti být pružnější a vytěžit maximální užitek z každého časového slotu.

Řešením problému zadržování zdrojů DTR přímo zlepšuje zážitek koncového uživatele dvěma způsoby. Za prvé zvyšuje pravděpodobnost, že může být navázána nová datová relace, protože zdroje jsou uvolňovány rychleji. Za druhé, pro uživatele, jehož přidělení je sníženo, to může vést k nižší spotřebě baterie, protože přijímač mobilního zařízení je aktivní méně často. DTR tedy představuje důležitou optimalizaci v dospělé technologii GERAN, která prodlužuje její životaschopnost a kvalitu služeb tváří v tvář rostoucím datovým požadavkům.

## Klíčové vlastnosti

- Dynamická rekonfigurace počtu časových slotů aktivního TBF na základě aktuálního zatížení provozem
- Signalizováno prostřednictvím řídicích zpráv MAC na kanálu PACCH
- Vyžaduje podporu jak ze strany sítě (BSS), tak mobilní stanice
- Uvolňuje nevyužité zdroje PDCH pro okamžité přeřazení jiným uživatelům
- Snižuje spotřebu energie MS omezením období aktivity přijímače
- Možnost plynulého a rychlého opětovného rozšíření při zvýšení datové aktivity uživatele

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [PDCH – Packet Data Channel](/mobilnisite/slovnik/pdch/)
- [PACCH – Packet Associated Control Channel](/mobilnisite/slovnik/pacch/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)

## Definující specifikace

- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DTR na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtr/)
