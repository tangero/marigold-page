---
slug: "rtbs"
url: "/mobilnisite/slovnik/rtbs/"
type: "slovnik"
title: "RTBS – Recommended Transport Block Size"
date: 2025-01-01
abbr: "RTBS"
fullName: "Recommended Transport Block Size"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rtbs/"
summary: "RTBS je parametr v signalizaci UMTS HSDPA, který navrhuje vhodnou velikost transportního bloku pro přenos dat na downlinku na základě aktuálních rádiových podmínek. Je součástí zpětné vazby o kvalitě"
---

RTBS je parametr v signalizaci UMTS HSDPA, ve kterém UE doporučuje Node B vhodnou velikost transportního bloku na základě aktuálních rádiových podmínek, aby pomohl optimalizovat propustnost a spolehlivost na downlinku.

## Popis

Recommended Transport Block Size (RTBS) je specifický informační prvek, který uživatelské zařízení (UE) hlásí Node B jako součást mechanismu zpětné vazby o kvalitě kanálu v UMTS High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)). Transportní blok je základní jednotkou dat předávanou z vrstvy [MAC](/mobilnisite/slovnik/mac/) do fyzické vrstvy pro přenos přes rozhraní vzduchu. Jeho velikost přímo určuje datový tok pro daný interval přenosu času. RTBS představuje odhad UE o největší možné velikosti [TBS](/mobilnisite/slovnik/tbs/), kterou lze přijmout s mírou chybovosti transportních bloků nepřekračující cílovou hodnotu (typicky 10 %) za současných podmínek kanálu.

Architektonicky je hlášení RTBS klíčovou součástí rychlé smyčky adaptace spojení v HSDPA. Proces funguje následovně: UE průběžně měří kvalitu downlink pilotního kanálu. Na základě tohoto měření, svých přijímacích schopností a aktuální konfigurace HSDPA vypočítá fyzická vrstva UE, jaká velikost TBS by byla podporovatelná. Tento výpočet zohledňuje efektivní poměr signálu k šumu a interferenci a převádí jej na podporovaný datový tok. UE následně namapuje tento vypočítaný tok na konkrétní hodnotu TBS definovanou v tabulkách 3GPP TS 25.214. Tato hodnota TBS je RTBS. Je kvantována a odeslána na uplinku k Node B na High-Speed Dedicated Physical Control Channel jako součást hlášení [CQI](/mobilnisite/slovnik/cqi/), typicky každé 2 ms.

Plánovač HSDPA v Node B využívá RTBS spolu s dalšími faktory, jako je stav vyrovnávací paměti UE a priorita, k přijetí konečného rozhodnutí o velikosti TBS pro další downlink přenos. Plánovač není povinen použít doporučenou velikost; může zvolit menší TBS pro UE s nižší prioritou nebo při vysokém systémovém vytížení, nebo může opatrně vyzkoušet i větší velikost. RTBS však poskytuje zásadní, rychlý a uživatelsky specifický pohled na kvalitu rádiového spojení, který umožňuje adaptivní modulaci a kódování. Úpravou TBS a odpovídajícím způsobem modulačního schématu a kódovacího poměru tak, aby odpovídaly momentálnímu stavu kanálu, HSDPA maximalizuje spektrální účinnost a uživatelskou propustnost. Tato dynamická úprava je mnohem efektivnější než pevné datové toky používané v dřívějších verzích UMTS, což z RTBS činí základní kámen vysokovýkonných datových schopností HSDPA.

## K čemu slouží

RTBS byl zaveden spolu s [HSDPA](/mobilnisite/slovnik/hsdpa/) v 3GPP Release 5, aby vyřešil problém neefektivního statického přenosu dat v podmínkách rychle se měnících rádiových kanálů. V UMTS před HSDPA byly datové toky na downlinku pro paketově orientované služby relativně statické a řízené [RNC](/mobilnisite/slovnik/rnc/) procesem rekonfigurace rádiového nosiče, což je pomalý proces nevhodný pro kanály s rychlým únikem. To vedlo buď ke konzervativním přidělením s nízkou rychlostí (plýtvání kapacitou), nebo agresivním přidělením způsobujícím vysokou chybovost a opakované přenosy. Motivací bylo umožnit rychlou adaptaci spojení v závislosti na kanálu přímo na Node B, aby bylo možné využít časové změny kanálu a dosáhnout špičkových datových toků až 14,4 Mbps.

Zavedení mechanismu zpětné vazby RTBS přímo řešilo potřebu včasných informací o stavu kanálu na straně vysílače. Tím, že UE doporučuje [TBS](/mobilnisite/slovnik/tbs/) každé 2 ms, získává plánovač v Node B detailní a nízkolatenční přehled o tom, co každé UE může spolehlivě přijmout. To umožňuje systému pracovat mnohem blíže Shannonově limitní kapacitě časově proměnného kanálu. Vyřešilo to klíčové omezení staršího přístupu řízeného RNC, kde byla adaptace spojení příliš pomalá na to, aby sledovala rychlé úniky. RTBS jako součást [CQI](/mobilnisite/slovnik/cqi/) vybavil Node B informacemi potřebnými k přijímání rozhodnutí o plánování a adaptaci rychlosti na úrovni milisekund, což je základní pro paketově orientovanou filozofii sdíleného kanálu HSDPA, která dramaticky zvýšila spektrální účinnost downlinku a uživatelské datové toky.

## Klíčové vlastnosti

- Parametr hlášený UE jako součást zpětné vazby CQI na HS-DPCCH
- Představuje největší podporovatelnou velikost TBS při cílové míře BLER (např. 10 %)
- Umožňuje rychlou adaptaci spojení a adaptivní modulaci a kódování
- Hlášen častě (např. každé 2 ms) pro sledování změn kanálu
- Používán plánovačem HSDPA v Node B pro přidělování downlink zdrojů
- Kvantovaná hodnota namapovaná na standardizované tabulky TBS v 25.214

## Související pojmy

- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [AMC – Adaptive Modulation and Coding](/mobilnisite/slovnik/amc/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding

---

📖 **Anglický originál a plná specifikace:** [RTBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtbs/)
