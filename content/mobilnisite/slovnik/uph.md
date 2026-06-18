---
slug: "uph"
url: "/mobilnisite/slovnik/uph/"
type: "slovnik"
title: "UPH – UE transmission Power Headroom"
date: 2025-01-01
abbr: "UPH"
fullName: "UE transmission Power Headroom"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/uph/"
summary: "Měření hlášené uživatelským zařízením (UE) síti, které udává rozdíl mezi maximálním vysílacím výkonem UE a jeho aktuálně využívaným vysílacím výkonem. Je klíčové pro řízení výkonu v uplinku, efektivit"
---

UPH je měření hlášené UE síti, které udává rozdíl mezi jeho maximálním vysílacím výkonem a aktuálně využívaným výkonem. Tento údaj je klíčový pro řízení výkonu v uplinku, plánování a správu interference.

## Popis

UE transmission Power Headroom (UPH) je klíčové měření na fyzické vrstvě v celulárních sítích, definované zejména v LTE (od Release 11) a zachované v 5G NR. Kvantifikuje v decibelech (dB) dostupný výkonový rezervu, kterou má UE pro uplinkový přenos. Konkrétně se vypočítá jako rozdíl mezi maximálním povoleným vysílacím výkonem UE (P_CMAX) a odhadovaným výkonem potřebným pro aktuální přenos na fyzickém kanálu [PUSCH](/mobilnisite/slovnik/pusch/) (Physical Uplink Shared Channel). UE tuto hodnotu hlásí obsluhující základnové stanici ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR) prostřednictvím řídicích prvků [MAC](/mobilnisite/slovnik/mac/) (Medium Access Control Control Elements) nebo v rámci žádostí o plánování.

Hlášení může být periodické nebo spouštěné událostmi, například při výrazné změně výkonové rezervy. Existují různé typy hlášení výkonové rezervy ([PHR](/mobilnisite/slovnik/phr/)): Typ 1 pro PUSCH, Typ 2 pro simultánní PUSCH a [PUCCH](/mobilnisite/slovnik/pucch/) (Physical Uplink Control Channel) v LTE a Typ 3 pro [SRS](/mobilnisite/slovnik/srs/) (Sounding Reference Signal) v pozdějších releasech. V 5G NR je koncept rozšířen o vylepšené mechanismy hlášení pro podporu širších šířek pásma a více komponentních nosných ve scénářích agregace nosných. gNB využívá nahlášenou UPH k inteligentním rozhodnutím o plánování, určuje modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) a alokaci bloků prostředků, které UE dokáže podpořit bez překročení svých výkonových limitů.

Tento mechanismus je nedílnou součástí algoritmů řízení výkonu v uplinku, jejichž cílem je zajistit dostatečnou kvalitu signálu na přijímači při minimalizaci interference do jiných buněk a šetření životnosti baterie UE. Díky znalosti UPH se síť může vyhnout přidělování prostředků, na kterých UE nemůže vysílat s dostatečným výkonem, čímž předchází plýtvání přidělenými zdroji a zlepšuje celkovou propustnost a spolehlivost systému. Je obzvláště důležitý ve scénářích na okraji buňky nebo v prostředí s vysokou interferencí.

## K čemu slouží

Hlášení UPH bylo zavedeno k řešení problému neefektivní alokace uplinkových prostředků v sítích LTE. Před Release 11 měla síť omezený přehled o výkonové situaci UE a spoléhala se hlavně na odhady útlumu na trase a příkazy pro řízení výkonu. To mohlo vést k suboptimálnímu plánování, kdy síť mohla přidělit větší šířku pásma nebo vyšší [MCS](/mobilnisite/slovnik/mcs/), než které UE mohlo se svým dostupným výkonem skutečně podpořit, což mělo za následek selhání přenosu nebo špatnou kvalitu signálu.

Motivací bylo zvýšit spektrální efektivitu uplinku a kapacitu systému umožněním přesnější adaptace spojení. Poskytnutím přímé zpětné vazby o výkonové rezervě může eNB přizpůsobit uplinková přidělení aktuálním výkonovým možnostem UE, čímž zajišťuje spolehlivé přenosy a snižuje potřebu retransmisí. To je zvláště kritické pro zařízení napájená baterií, aby šetřila energii, a pro udržení kvality služeb v náročných rádiových podmínkách. Tato funkce se stala základem pro pokročilé techniky, jako je agregace nosných a uplinkový MIMO, kde je třeba pečlivě spravovat sdílení výkonu mezi více nosnými nebo vrstvami.

## Klíčové vlastnosti

- Udává dostupnou výkonovou rezervu pro vysílání UE
- Hlášeno prostřednictvím řídicích prvků MAC (MAC Control Elements)
- Podporuje více typů (např. Typ 1, Typ 2) pro různé kanály
- Umožňuje síťové plánování uplinku a adaptaci spojení
- Spouštěno na základě periodických časovačů nebo prahových hodnot událostí
- Nezbytné pro řízení výkonu v uplinku a koordinaci interference

## Související pojmy

- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)

## Definující specifikace

- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 25.707** (Rel-14) — Multi-Carrier Enhancements for UMTS Study
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview

---

📖 **Anglický originál a plná specifikace:** [UPH na 3GPP Explorer](https://3gpp-explorer.com/glossary/uph/)
