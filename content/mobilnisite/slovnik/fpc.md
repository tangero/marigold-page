---
slug: "fpc"
url: "/mobilnisite/slovnik/fpc/"
type: "slovnik"
title: "FPC – Fast Power Control"
date: 2025-01-01
abbr: "FPC"
fullName: "Fast Power Control"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fpc/"
summary: "Rychlé řízení výkonu (FPC) je mechanismus v sítích GSM/EDGE pro rychlé přizpůsobení vysílacího výkonu mobilní stanice (MS) a základnové stanice (BTS) v rámci každého časového slotu. Je klíčové pro pot"
---

FPC je mechanismus v sítích GSM/EDGE pro rychlé přizpůsobení vysílacího výkonu mobilního zařízení a základnové stanice v rámci každého časového slotu za účelem potlačení rychlého útlumu, snížení rušení a šetření baterie.

## Popis

Rychlé řízení výkonu (FPC) je základní funkce v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)) specifikované v dokumentu 3GPP TS 43.051. Funguje na principu uzavřené smyčky řízení výkonu, kde přijímač (mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) nebo základnová přenosová stanice ([BTS](/mobilnisite/slovnik/bts/))) průběžně měří kvalitu přijímaného signálu a nařídí vysílači, aby odpovídajícím způsobem upravil svou výkonovou hladinu. Tento proces probíhá vysokou rychlostí, typicky synchronizovaně se strukturou rámců GSM, což umožňuje úpravy v rámci každého časového slotu pro potlačení rychlých změn signálu známých jako rychlý útlum.

Architektura zahrnuje klíčové komponenty v MS i v BTS. Přijímač obsahuje měřicí jednotky (např. pro indikaci síly přijímaného signálu (RSSI) a míru bitových chyb ([BER](/mobilnisite/slovnik/ber/))) a algoritmus řízení výkonu. Na základě těchto měření a předdefinovaných prahových hodnot přijímač generuje příkazy pro řízení výkonu (PC). Tyto příkazy jsou následně přenášeny k protější entitě prostřednictvím specifických řídicích kanálů. V uplinku posílá BTS příkazy PC k MS na pomalém přidruženém řídicím kanálu (SACCH). V downlinku posílá MS příkazy PC k BTS, také typicky prostřednictvím SACCH. Po přijetí příkazu výkonový zesilovač vysílače upraví svůj výstupní výkon v rámci definovaného dynamického rozsahu (např. v krocích po 2 dB).

Role FPC je mnohostranná. Primárně udržuje kvalitu spojení na minimální nezbytné úrovni pro splnění cílové míry chybovosti rámců ([FER](/mobilnisite/slovnik/fer/)) nebo kvality služeb (QoS). Snížením výkonu při dobrých podmínkách na rádiovém kanále minimalizuje ko-kanálové a přilehlé kanálové rušení v celé síti, což je klíčové pro frekvenční opakování v celulárních systémech. Toto snížení rušení přímo vede ke zvýšení systémové kapacity. Dále, pro MS dynamické snížení výkonu významně šetří energii baterie a prodlužuje dobu hovoru. Algoritmus musí vyvážit rychlost reakce se stabilitou, aby se předešlo nežádoucím oscilacím výkonu („ping-pong“ efekt), a musí spolupracovat s dalšími funkcemi správy rádiových zdrojů, jako je předávání spojení a pomalé řízení výkonu.

## K čemu slouží

Rychlé řízení výkonu bylo zavedeno, aby řešilo významné výzvy způsobené mobilním rádiovým prostředím, konkrétně rychlý útlum. V raných mobilních systémech bez dynamického řízení výkonu vysílače pracovaly na pevných nebo pomalu přizpůsobovaných výkonových úrovních. To bylo velmi neefektivní: při hlubokých útlumech mohl signál klesnout pod požadovanou úroveň, což způsobovalo přerušení hovorů nebo špatnou kvalitu hlasu. Naopak, při silných signálových podmínkách nadměrný vysílací výkon plýtval energií a vytvářel zbytečné rušení pro ostatní uživatele na stejných nebo přilehlých frekvencích, což omezovalo celkovou kapacitu sítě.

Vytvoření FPC bylo motivováno potřebou spektrální efektivity a lepší uživatelské zkušenosti v hustě rozmístěných sítích GSM. Umožněním vysílačům rychle přizpůsobovat výkon – v řádu každých 480 ms (perioda rámce SACCH) nebo rychleji – systém dokázal „sledovat“ obálku útlumu. Tím bylo zajištěno, že se použije právě tolik výkonu, kolik je třeba k udržení spojení, což je koncept známý jako optimalizace výkonové rezervy spojení. Řešení problému rychlého útlumu bylo klíčovým předpokladem pro dosažení vysoké kapacity a kvality, díky kterým se GSM stalo celosvětovým úspěchem. Odstranilo omezení předchozích zjednodušených přístupů a stanovilo precedens pro pokročilé mechanismy řízení výkonu v pozdějších systémech 3G (UMTS) a 4G (LTE), kde se vyvinulo v rychlejší a jemněji granulované procesy.

## Klíčové vlastnosti

- Řízení v uzavřené smyčce založené na měřeních přijímače v reálném čase (RSSI, BER)
- Úprava výkonu v rámci každého časového slotu, synchronizovaná s TDMA rámcovou strukturou
- Nezávislý provoz pro oba směry – uplink (výkon MS) i downlink (výkon BTS)
- Pro přenos příkazů řízení výkonu využívá pomalý přidružený řídicí kanál (SACCH)
- Definovaný dynamický rozsah výkonu a velikost kroků (např. po 2 dB) pro úpravu vysílače
- Cílí na udržení cílové kvality spojení (např. FER) při minimalizaci vysílaného výkonu a rušení

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description

---

📖 **Anglický originál a plná specifikace:** [FPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fpc/)
