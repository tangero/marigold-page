---
slug: "ich"
url: "/mobilnisite/slovnik/ich/"
type: "slovnik"
title: "ICH – Indicator Channel"
date: 2025-01-01
abbr: "ICH"
fullName: "Indicator Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ich/"
summary: "Indikátorový kanál (ICH) je fyzický kanál na downlinku v UMTS Terrestrial Radio Access Network (UTRAN). Používá se k přenosu řídicích informací vrstvy 1, konkrétně indikátorů kombinací transportních f"
---

ICH je fyzický kanál na downlinku v UTRAN, který přenáší indikátory kombinací transportních formátů (TFCIs), aby informoval UE o transportním formátu použitém na přidruženém DPDCH pro správnou demodulaci a dekódování.

## Popis

Indikátorový kanál (ICH) je specifický typ fyzického kanálu na downlinku definovaný v rozhraní UMTS [WCDMA](/mobilnisite/slovnik/wcdma/), jak je specifikováno v 3GPP TS 25.211. Funguje spolu s vyhrazenými datovými kanály, aby usnadnil spolehlivý přenos dat. Na downlinku [UTRAN](/mobilnisite/slovnik/utran/) se uživatelská data přenášejí na vyhrazeném fyzickém datovém kanálu ([DPDCH](/mobilnisite/slovnik/dpdch/)). Samotný DPDCH však explicitně nenese informace o svém vlastním přenosovém formátu (např. rozprostírací faktor, schéma kódování kanálu). Tyto informace o formátu jsou klíčové pro přijímač (UE), aby úspěšně demoduloval a dekódoval datový proud.

ICH přenáší tyto zásadní řídicí informace vrstvy 1, především indikátor kombinace transportních formátů ([TFCI](/mobilnisite/slovnik/tfci/)). TFCI je kód, který odkazuje na konkrétní předem definovanou kombinaci transportních formátů ([TFC](/mobilnisite/slovnik/tfc/)) ze sady dohodnuté během nastavení rádiového přenosového okruhu. TFC popisuje okamžité parametry transportních kanálů multiplexovaných na DPDCH, včetně velikostí bloků, kódovacích rychlostí a dalších. ICH je vysílán paralelně s DPDCH, využívá samostatný kanalizační kód, ale sdílí stejný skramblovací kód. To umožňuje UE současně přijímat jak nezpracovaná data, tak instrukce, jak je interpretovat.

Z provozního hlediska pro každý 10ms rádiový rámec Node-B (základnová stanice) určí vhodný TFC na základě dat, která mají být odeslána, a aktuálních rádiových podmínek. Zakóduje odpovídající hodnotu TFCI a přenese ji na ICH. UE kontinuálně monitoruje ICH, extrahuje TFCI a použije vyhledávací tabulku (sadu kombinací transportních formátů) k určení přesných parametrů fyzické vrstvy doprovázejícího rámce DPDCH. Tento mechanismus umožňuje dynamickou adaptaci přenosového formátu po rámcích bez signalizace na vyšších vrstvách, což umožňuje efektivní využití rádiového zdroje pro služby s proměnnou rychlostí. ICH je základní součástí fyzické vrstvy WCDMA, která odděluje řídicí signalizaci od uživatelských dat, čímž zvyšuje robustnost a flexibilitu.

## K čemu slouží

ICH byl vytvořen k řešení základního problému v UMTS založeném na [WCDMA](/mobilnisite/slovnik/wcdma/): jak efektivně a spolehlivě signalizovat vysoce proměnný přenosový formát vyhrazeného datového kanálu mobilnímu terminálu v reálném čase. WCDMA podporuje více simultánních služeb s různými datovými rychlostmi a požadavky na kvalitu na jediném spojení (multiplexování transportních kanálů). Přenosový formát se může měnit každých 10 ms rámec na základě okamžité poptávky po datech a rozhodnutí síťového plánování.

Bez vyhrazeného kanálu s nízkou latencí, jako je ICH, by bylo UE slepé vůči formátu přijímaných dat. Alternativní přístupy, jako je vložení informací o formátu do samotného datového kanálu (in-band signalizace) nebo použití signalizace na vyšších vrstvách, byly nepraktické. In-band signalizace by zkomplikovala návrh přijímače, snížila datovou efektivitu a byla by náchylná k chybám, které by mohly poškodit jak řídicí, tak datové informace. Signalizace na vyšších vrstvách by byla příliš pomalá (stovky milisekund) a nemohla by podporovat rychlou adaptaci potřebnou pro efektivní služby paketových dat.

ICH poskytuje robustní, out-of-band řešení na vrstvě 1. Jeho vytvoření bylo motivováno potřebou rychlé a spolehlivé adaptace spoje, což je klíčová vlastnost pro podporu vysokorychlostních paketových dat a multimediálních služeb ve 3G. Vyčleněním samostatného kanálu s vlastním rozprostíracím kódem získávají informace [TFCI](/mobilnisite/slovnik/tfci/) známou a potenciálně robustnější úroveň ochrany, což zajišťuje, že UE téměř vždy správně určí, jak dekódovat data, i když samotný datový kanál zaznamená chyby. Toto oddělení řídicích a datových informací je klasický návrhový vzor v telekomunikacích, který zvyšuje celkový výkon a spolehlivost systému.

## Klíčové vlastnosti

- Přenáší indikátor kombinace transportních formátů (TFCI) pro přidružený DPDCH
- Vysílán paralelně s DPDCH na downlinku pomocí samostatného kanalizačního kódu
- Umožňuje dynamickou adaptaci přenosových parametrů po rámcích bez signalizace na vyšších vrstvách
- Nezbytný pro správnou demodulaci a dekódování vyhrazených datových kanálů s proměnnou rychlostí
- Funguje na 10ms rádiové rámcové struktuře synchronizované s DPDCH
- Poskytuje robustní řídicí kanál vrstvy 1 oddělený od uživatelských dat pro zvýšení spolehlivosti

## Související pojmy

- [DPDCH – Dedicated Physical Data Channel](/mobilnisite/slovnik/dpdch/)
- [TFCI – Transport Format Combination Indicator](/mobilnisite/slovnik/tfci/)
- [DCH – Dedicated Channel](/mobilnisite/slovnik/dch/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels

---

📖 **Anglický originál a plná specifikace:** [ICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ich/)
