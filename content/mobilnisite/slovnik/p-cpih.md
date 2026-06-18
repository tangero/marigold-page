---
slug: "p-cpih"
url: "/mobilnisite/slovnik/p-cpih/"
type: "slovnik"
title: "P-CPIH – Primary Common Pilot Channel"
date: 2025-01-01
abbr: "P-CPIH"
fullName: "Primary Common Pilot Channel"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/p-cpih/"
summary: "Primární společný pilotní kanál (P-CPIH) je downlinkový fyzický kanál v UMTS (WCDMA) používaný pro odhad kanálu a identifikaci buňky. Vysílá známou nemodulovanou sekvenci, která umožňuje uživatelskému"
---

P-CPIH je Primární společný pilotní kanál (Primary Common Pilot Channel), downlinkový fyzický kanál UMTS, který vysílá známou sekvenci pro identifikaci buňky, odhad kanálu a koherentní demodulaci uživatelským zařízením.

## Popis

Primární společný kanál pilotní (P-CPIH) je kritický downlinkový fyzický kanál definovaný v rámci režimu [UTRA](/mobilnisite/slovnik/utra/) [FDD](/mobilnisite/slovnik/fdd/) (UMTS Terrestrial Radio Access) standardizovaného 3GPP. Funguje jako nepřetržitý, nemodulovaný signál s rozprostřeným spektrem vysílaný každým Node B (základnovou stanicí) po celé oblasti pokrytí buňky. Primární funkcí kanálu je sloužit jako fázová reference pro koherentní demodulaci dalších downlinkových fyzických kanálů, jako je Vyhrazený fyzický kanál ([DPCH](/mobilnisite/slovnik/dpch/)) nebo Společný řídicí fyzický kanál ([CCPCH](/mobilnisite/slovnik/ccpch/)). Přenosem známé, pro buňku specifické sekvence skramblovacího kódu a kanalizačního kódu umožňuje P-CPIH uživatelskému zařízení (UE) odhadnout impulsní odezvu rádiového kanálu, včetně efektů jako je útlum, vícecestné šíření a interference. Tento odhad je zásadní pro to, aby přijímač v UE mohl správně dekódovat data modulovaná na jiných kanálech pomocí technik jako je RAKE kombinace.

Z hlediska architektury je P-CPIH mapován na konkrétní kanalizační kód (typicky kód 0) a je skramblován pomocí primárního skramblovacího kódu přiřazeného buňce. Tento kód je součástí identity buňky vysílané v systémových informacích. Kanál nepřenáší data vyšších vrstev; jeho struktura signálu se skládá z nepřetržitého proudu pilotních symbolů. UE používá tuto konstantní referenci k provádění kritických měření správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)), zejména výkonu kódového signálu přijímaného signálu ([RSCP](/mobilnisite/slovnik/rscp/)) a poměru energie na čip k hustotě šumu ([Ec](/mobilnisite/slovnik/ece-c/)/No). Tato měření jsou hlášena síti k podpoře funkcí jako je výběr buňky, převýběr a předávání hovoru.

V širším kontextu sítě je P-CPIH nezbytný pro počáteční hledání a synchronizaci buňky. Během tohoto procesu UE detekuje Primární synchronizační kanál (P-SCH) a Sekundární synchronizační kanál (S-SCH), čímž dosáhne synchronizace slotu a rámce, a poté identifikuje primární skramblovací kód buňky korelací s P-CPIH. Neustálá přítomnost tohoto kanálu také umožňuje UE monitorovat sousední buňky pro účely předávání hovoru bez nutnosti plně dekódovat jejich vysílací kanály. Jeho návrh zajišťuje zpětnou kompatibilitu a stabilní provoz ve všech verzích UMTS a tvoří základní vrstvu pro odhad downlinkového kanálu v 3G systémech založených na [WCDMA](/mobilnisite/slovnik/wcdma/).

## K čemu slouží

P-CPIH byl vytvořen k řešení zásadní výzvy koherentní demodulace v systémech s mnohonásobným přístupem s kódovým dělením a širokým pásmem (WCDMA), které tvoří základ sítí 3G UMTS. V systémech CDMA sdílí více uživatelů současně stejné frekvenční pásmo, jsou odděleni jedinečnými kódy. Pro přesné dekódování signálu uživatele musí přijímač mít přesný odhad charakteristik rádiového kanálu, které se neustále mění kvůli mobilitě a vlivům prostředí. P-CPIH poskytuje konstantní, známý referenční signál, který umožňuje UE odhadnout fázové a amplitudové zkreslení kanálu a umožňuje použití vysoce výkonné koherentní detekce. To ve srovnání s nekoherentními metodami používanými v dřívějších systémech 2G výrazně zlepšuje citlivost přijímače a datový propust.

Historicky GSM (2G) spoléhalo na kmitočtové a časové dělení (FDMA/TDMA) s odlišnou strukturou synchronizace a reference. Přechod na WCDMA pro 3G vyžadoval vyhrazený pilotní kanál pro zvládnutí zvýšené komplexity šíření spektra a vícecestného útlumu. P-CPIH vyřešil problém efektivního poskytnutí společné fázové reference pro všechny uživatele v buňce, aniž by bylo nutné věnovat pilotní symboly uvnitř každého uživatelského kanálu pro přenos, čímž optimalizoval kapacitu downlinku. Také sjednotil mechanismus pro identifikaci buňky a měření kvality signálu, což zjednodušilo implementaci UE a plánování sítě.

Bez robustního společného pilotního kanálu by byly funkce jako měkké předání hovoru – klíčová vlastnost CDMA, kdy UE komunikuje současně s více buňkami – extrémně obtížné. P-CPIH umožňuje UE přesně měřit kvalitu signálu z několika buněk a poskytuje data potřebná pro řídicí jednotku rádiové sítě (RNC) ke správě aktivních souborů. Jeho zavedení ve verzi 99 vytvořilo fyzickou vrstvu pro všechna následná vylepšení UMTS a umožnilo vyšší přenosové rychlosti a pokročilejší služby tím, že zajišťuje spolehlivý odhad downlinkového kanálu.

## Klíčové vlastnosti

- Poskytuje nepřetržitou, pro buňku specifickou fázovou referenci pro koherentní demodulaci všech downlinkových fyzických kanálů.
- Umožňuje odhad kanálu pro kombinaci v RAKE přijímači ke zmírnění efektů vícecestného útlumu.
- Podporuje kritická RRM měření jako RSCP a Ec/No pro výběr buňky a předání hovoru.
- Používá pevný kanalizační kód (typicky kód 0) a primární skramblovací kód buňky pro identifikaci.
- Zásadní pro počáteční procedury hledání a synchronizace buňky v UMTS.
- Vysílán po celém pokrytí buňky, přístupný všem UE bez vyhrazené alokace.

## Související pojmy

- [S-CPICH – Secondary Common Pilot Channel](/mobilnisite/slovnik/s-cpich/)
- [RSCP – Reference Signal Carrier Phase](/mobilnisite/slovnik/rscp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [P-CPIH na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-cpih/)
