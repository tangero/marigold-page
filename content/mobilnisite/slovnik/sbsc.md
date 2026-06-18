---
slug: "sbsc"
url: "/mobilnisite/slovnik/sbsc/"
type: "slovnik"
title: "SBSC – Serving Base Station Controller"
date: 2025-01-01
abbr: "SBSC"
fullName: "Serving Base Station Controller"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sbsc/"
summary: "Serving Base Station Controller (SBSC) je síťový prvek v GSM/EDGE Radio Access Network (GERAN), který řídí jednu nebo více základnových stanic (BTS). Spravuje rádiové prostředky, zpracovává sestavení"
---

SBSC je síťový prvek v GERAN, který řídí jednu nebo více BTS za účelem správy rádiových prostředků, zpracování sestavení hovorů, mobility a předávání spojení pro mobilní zařízení.

## Popis

Serving Base Station Controller (SBSC) je hlavní komponenta architektury GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), definovaná ve specifikacích 3GPP. Působí jako inteligentní řadič umístěný mezi základnovými stanicemi ([BTS](/mobilnisite/slovnik/bts/)) a jádrem sítě, konkrétně Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)). SBSC je zodpovědný za správu a alokaci rádiových prostředků ve své určené oblasti. Řídí více BTS, což jsou fyzické rádiové jednotky, které komunikují přímo s mobilními stanicemi ([MS](/mobilnisite/slovnik/ms/)). Mezi hlavní funkce SBSC patří správa rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)), která zahrnuje přidělování a uvolňování rádiových kanálů pro hlasové a datové hovory. Zpracovává přeskakování frekvencí, řízení výkonu a výpočty časového předstihu pro optimalizaci kvality signálu a kapacity sítě.

Klíčovou operační rolí SBSC je správa předávání spojení. Když se mobilní stanice přesune z pokrytí jedné BTS do jiné, SBSC vyhodnotí měření síly a kvality signálu hlášená MS a okolními BTS. Poté rozhodne, zda a kdy zahájit předání spojení, a koordinuje tento proces, aby zajistil plynulý přechod probíhajícího hovoru nebo datové relace bez přerušení. Toto předání může být intra-BSC (mezi BTS řízenými stejným SBSC) nebo inter-BSC (vyžadující koordinaci s jiným SBSC). SBSC také provádí transkódování a adaptaci přenosové rychlosti, převádějící řečové kódování používané na rádiovém rozhraní (např. Full Rate, Half Rate) na standardní 64 kbit/s [PCM](/mobilnisite/slovnik/pcm/) používané v jádru sítě, a naopak.

Z pohledu síťové architektury se SBSC připojuje k BTS přes rozhraní Abis, které přenáší provoz a řídicí signalizaci. K MSC v jádru sítě se připojuje přes rozhraní A. SBSC obsahuje několik klíčových funkčních jednotek: přepínač pro propojování provozních kanálů, transkodér ([TC](/mobilnisite/slovnik/tc/)) pro převod řečového kódování a rozhraní Operation and Maintenance Center (OMC) pro správu sítě. Obsahuje také databáze pro správu rádiových prostředků svých připojených BTS. V kontextu datových služeb GPRS a EDGE SBSC spolupracuje s Packet Control Unit (PCU), která je často umístěna společně s ním nebo do něj integrována. PCU zpracovává plánování paketů a spravuje rozhraní Gb směrem k SGSN v jádru sítě. SBSC je tedy klíčovým prvkem, který propojuje domény rádiové a jádrové sítě a zajišťuje efektivní, spolehlivé a mobilně orientované poskytování služeb v sítích 2G a 2.5G.

## K čemu slouží

SBSC byl vytvořen, aby řešil základní potřebu centralizovaného řízení a efektivní správy rádiových prostředků v buněčných sítích, konkrétně ve standardu GSM. Rané buněčné systémy vyžadovaly způsob, jak zvládnout složitost správy více rádiových buněk, koordinovat předávání spojení při pohybu uživatelů a optimalizovat využití omezeného dostupného rádiového spektra. Architektura SBSC oddělila řídicí inteligenci (v BSC) od jednoduchých funkcí rádiového vysílání/příjmu (v BTS), což umožnilo škálovatelnější, lépe spravovatelná a nákladově efektivnější nasazení sítí.

Před takovými centralizovanými řadiči byly sítě méně efektivní a náchylnější k přerušeným hovorům při mobilitě. SBSC vyřešil kritický problém plynulé mobility inteligentní správou předávání spojení na základě měření rádiového signálu v reálném čase. Také centralizoval úlohy, jako je přidělování frekvencí, řízení výkonu a přiřazování kanálů, což vedlo k významnému zlepšení kapacity sítě a kvality služeb ve srovnání s decentralizovanými přístupy. Zpracováním transkódování izoloval jádro sítě od specifických, často komprimovaných kodeků používaných na rádiovém spoji, a poskytl standardizované rozhraní.

Jeho vytvoření bylo motivováno cíli projektu GSM vytvořit panevropský digitální buněčný standard s vysokou kapacitou, dobrou kvalitou hlasu a podporou mezinárodního roamingu. SBSC jako součást Base Station Subsystem (BSS) byla klíčovou inovací, která tyto cíle umožnila tím, že poskytla robustní a flexibilní řídicí vrstvu pro rádiovou přístupovou síť. Tvořil základ, na kterém byly později přidány datové služby jako GPRS a EDGE, přičemž integrace Packet Control Unit (PCU) rozšířila jeho účel o zpracování paketově přepínaného provozu.

## Klíčové vlastnosti

- Centralizovaná správa rádiových prostředků pro více BTS
- Plynulé řízení předávání spojení (intra-buněčné a inter-buněčné)
- Transkódování a adaptace přenosové rychlosti mezi rádiovým a jádrovým síťovým rozhraním
- Řízení výkonu a správa přeskakování frekvencí
- Správa rozhraní (rozhraní Abis k BTS, rozhraní A k MSC)
- Integrace s Packet Control Unit (PCU) pro datové služby GPRS/EDGE

## Související pojmy

- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 43.130** (Rel-19) — Iur-g Interface Overview

---

📖 **Anglický originál a plná specifikace:** [SBSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbsc/)
