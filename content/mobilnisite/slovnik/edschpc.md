---
slug: "edschpc"
url: "/mobilnisite/slovnik/edschpc/"
type: "slovnik"
title: "EDSCHPC – Enhanced Downlink Shared Channel Power Control"
date: 2025-01-01
abbr: "EDSCHPC"
fullName: "Enhanced Downlink Shared Channel Power Control"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/edschpc/"
summary: "Enhanced Downlink Shared Channel Power Control (EDSCHPC) je funkce UMTS/HSPA pro dynamické přizpůsobování vysílacího výkonu High-Speed Downlink Shared Channel (HS-DSCH). Optimalizuje využití výkonu v"
---

EDSCHPC je funkce UMTS/HSPA, která dynamicky upravuje vysílací výkon HS-DSCH za účelem optimalizace využití sestupné linky, čímž zvyšuje kapacitu buňky a propustnost pro lepší spektrální účinnost.

## Popis

Enhanced Downlink Shared Channel Power Control (EDSCHPC) je mechanismus definovaný pro UMTS Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně v rámci vývoje High-Speed Packet Access ([HSPA](/mobilnisite/slovnik/hspa/)). Působí na High-Speed Downlink Shared Channel ([HS-DSCH](/mobilnisite/slovnik/hs-dsch/)), který je primárním kanálem pro uživatelská data v sestupné lince v HSPA. Architektonicky zahrnuje EDSCHPC koordinaci mezi Node B (základnovou stanicí) a User Equipment (UE). Plánovač Node B, klíčová komponenta, využívá zpětnou vazbu od UE k určení optimální úrovně vysílacího výkonu pro HS-DSCH v každém Transmission Time Interval ([TTI](/mobilnisite/slovnik/tti/)).

Fungování EDSCHPC je založeno na principech uzavřené smyčky řízení výkonu upravených pro provoz sdíleného kanálu. UE průběžně měří kvalitu kanálu v sestupné lince, typicky na základě Common Pilot Channel ([CPICH](/mobilnisite/slovnik/cpich/)), a hlásí Node B indikátory Channel Quality Indicator ([CQI](/mobilnisite/slovnik/cqi/)). Plánovač Node B interpretuje tyto CQI spolu s dalšími faktory, jako je dostupný výkon, stav fronty a požadavky Quality of Service (QoS). Na základě těchto informací plánovač dynamicky přiděluje část celkového vysílacího výkonu Node B pro HS-DSCH. Na rozdíl od řízení výkonu na vyhrazeném kanálu, které cílí na specifický Signal-to-Interference Ratio ([SIR](/mobilnisite/slovnik/sir/)), se EDSCHPC snaží maximalizovat propustnost nebo prosadit spravedlivost přidělováním výkonu tam, kde je nejúčinnější, často zvýhodňováním uživatelů s dobrými rádiovými podmínkami.

Klíčovými komponentami jsou funkce měření kanálu a hlášení v UE, plánovač HS-DSCH v Node B a algoritmus přidělování výkonu. Specifikace 3GPP TS 25.423 podrobně popisuje signalizaci na rozhraní lur (mezi [RNC](/mobilnisite/slovnik/rnc/)), která může podporovat aspekty této koordinace, ačkoli primární řízení probíhá mezi Node B a UE. Role EDSCHPC je klíčová pro efektivní provoz HSPA; umožňuje síti rychle se přizpůsobovat útlumu a rušení a zajišťuje, že vzácný zdroj výkonu v sestupné lince je využit k dosažení nejvyšších možných datových rychlostí a kapacity systému, což přímo ovlivňuje uživatelský zážitek u mobilních širokopásmových služeb.

## K čemu slouží

EDSCHPC byl vytvořen k řešení neefektivit statických nebo jednoduchých schémat přidělování výkonu pro vysokorychlostní sdílený kanál v HSPA. Před jeho vylepšením bylo řízení výkonu pro kanály v sestupné lince navrženo primárně pro vyhrazené hlasové kanály s cílem konstantní kvality, což je suboptimální pro trhaný, vysokorychlostní datový provoz. Mezi omezení patřil plýtvaný výkon na uživatele ve špatných rádiových podmínkách a neschopnost plně využít multi-user diverzitu.

Historický kontext představuje zavedení a vývoj HSPA v 3GPP Releases 5 a 6, které dramaticky zvýšily špičkové datové rychlosti v sestupné lince. U HS-DSCH sdílí více uživatelů kanalizační kódy a výkon. EDSCHPC, představený v Release 8, vyřešil problém, jak nejlépe rozdělit dostupný vysílací výkon Node B mezi tyto konkurenční uživatele. Byl motivován potřebou současně zlepšit výkon na okraji buňky a celkovou propustnost buňky, což je klíčová výzva pro sítě orientované na data.

V konečném důsledku umožnil EDSCHPC inteligentnější strategii plánování citlivou na stav kanálu. Dynamickým přizpůsobováním výkonu HS-DSCH umožňuje síti obsluhovat uživatele poblíž středu buňky nižším výkonem (čímž uvolňuje zdroje) a v případě potřeby zvýšit výkon pro uživatele na okraji buňky, čímž vyvažuje spravedlivost a kapacitu. Toto byl klíčový krok v optimalizaci sítí UMTS/HSPA pro rostoucí poptávku po mobilním přístupu k internetu.

## Klíčové vlastnosti

- Dynamické přidělování výkonu pro HS-DSCH v každém TTI
- Jako primární vstup využívá indikátor Channel Quality Indicator (CQI) hlášený UE
- Implementováno v rámci rychlého plánovače Node B pro nízkou latenci
- Cílí na maximalizaci systémové propustnosti a/nebo prosazení spravedlivosti
- Působí ve spojení s Adaptive Modulation and Coding (AMC)
- Může být koordinováno s dalšími funkcemi RRM, jako je přidělování kódů

## Související pojmy

- [HS-DSCH – High Speed Downlink Shared Channel](/mobilnisite/slovnik/hs-dsch/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification

---

📖 **Anglický originál a plná specifikace:** [EDSCHPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/edschpc/)
