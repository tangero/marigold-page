---
slug: "sdma"
url: "/mobilnisite/slovnik/sdma/"
type: "slovnik"
title: "SDMA – Spatial Division Multiple Access"
date: 2025-01-01
abbr: "SDMA"
fullName: "Spatial Division Multiple Access"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sdma/"
summary: "Technika mnohonásobného přístupu, která umožňuje současnou obsluhu více uživatelských zařízení na stejném kmitočtově-časovém zdroji díky využití prostorového oddělení. Je to základní koncept pro víceu"
---

SDMA je technika mnohonásobného přístupu, která využívá prostorového oddělení k současné obsluze více uživatelů na stejném kmitočtově-časovém zdroji a tvoří základ pro MU-MIMO v mobilních sítích.

## Popis

Spatial Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (SDMA) je technika rádiového přístupu, která umožňuje základnové stanici (např. eNodeB v LTE, gNB v NR) komunikovat současně s více uživatelskými zařízeními (UE) využívajícími stejné časové a kmitočtové zdroje. Toho dosahuje využitím prostorové dimenze – rozdílů ve fyzické poloze uživatelů a výsledných cestách šíření rádiových vln. Základním principem je, že signály určené pro různé uživatele lze oddělit v prostoru, a to buď použitím směrových antén, nebo častěji pokročilým digitálním zpracováním signálu aplikovaným na anténní řady.

SDMA funguje jako klíčová aplikace technologie Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)), konkrétně Multi-User MIMO ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)). Základnová stanice je vybavena více anténami, které tvoří řadu. Používá informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)), hlášené UE nebo odhadnuté pomocí sondování v uplinku, k charakterizaci prostorového kanálu ke každému uživateli. Pomocí těchto informací vysílač základnové stanice používá techniky předkódování. Předkódování matematicky tvaruje vysílaný signál z každé antény tak, že po průchodu bezdrátovým kanálem je energie signálu zaměřena na zamýšleného uživatele, zatímco v místech ostatních současně plánovaných uživatelů vznikají nulové body nebo je interference snížena. Na uplinku základnová stanice používá prostorové filtry nebo algoritmy potlačení interference (např. filtr s minimální střední kvadratickou chybou – [MMSE](/mobilnisite/slovnik/mmse/)) k oddělení překrývajících se signálů přijatých od více UE.

Implementace SDMA vyžaduje sofistikovanou koordinaci na fyzické a [MAC](/mobilnisite/slovnik/mac/) vrstvě. Plánovač v základnové stanici musí identifikovat skupiny UE, které lze prostorově multiplexovat s přijatelnou úrovní vzájemné interference. To závisí na faktorech, jako je prostorové oddělení UE, stav kanálu a mobilita. Beamforming, technika vytváření fokusovaných vyzařovacích charakteristik, je s SDMA vnitřně propojen. V 5G NR jsou koncepty SDMA rozšířeny o massive MIMO, kde velmi velký počet anténních prvků (např. 64, 128 nebo více) umožňuje vysoce přesné prostorové zaměření, což dovoluje SDMA obsloužit desítky či více uživatelů na stejných zdrojích a dramaticky tak zvýšit kapacitu buňky.

## K čemu slouží

SDMA byla vyvinuta k řešení zásadní výzvy omezeného rádiového spektra. Tradiční schémata mnohonásobného přístupu jako [FDMA](/mobilnisite/slovnik/fdma/), [TDMA](/mobilnisite/slovnik/tdma/) a CDMA dělí zdroje ve kmitočtové, časové nebo kódové doméně, což ukládá pevný limit na počet současných uživatelů. SDMA zavádí novou, ortogonální dimenzi – prostor – a umožňuje tak opakované využití stejného kmitočtově-časového zdroje vícekrát v rámci stejné buňky. To přímo zvyšuje spektrální účinnost (bit/s/Hz) a celkovou kapacitu sítě bez nutnosti získání dalšího licencovaného spektra.

Motivace pro SDMA zesílila se zavedením LTE (Rel-8) a potřebou vyšších přenosových rychlostí a kapacity pro podporu mobilního broadbandu. Rané MIMO techniky v Rel-8 se zaměřovaly na jednouživatelské prostorové multiplexování pro zvýšení špičkových rychlostí. SDMA, neboli MU-MIMO, tento koncept rozvinula tak, aby prospěla propustnosti na okraji buňky a průměrné uživatelské propustnosti tím, že umožnila více uživatelům sdílet prostorové vrstvy. Řeší problém neefektivního využití zdrojů, kdy jediný uživatel nedokáže využít všechny dostupné prostorové proudy poskytované víceanténovou základnovou stanicí.

SDMA dále zlepšuje výkon sítě v hustých městských prostředích, kde je uživatelů mnoho a spektrum je vzácné. Umožněním současné obsluhy více uživatelů snižuje plánovací zpoždění a zlepšuje latenci. Vývoj směrem k massive MIMO v 5G NR je přímým pokračováním principu SDMA, využívajícím výrazně zvýšený počet antén k dosažení přesnějšího prostorového oddělení a podpoře extrémních kapacitních požadavků budoucích mobilních sítí.

## Klíčové vlastnosti

- Umožňuje současné sdílení stejného kmitočtově-časového zdroje mezi více uživateli
- Spoléhá se na víceanténní řady a digitální beamforming/předkódování
- Využívá informace o stavu kanálu (CSI) pro prostorové oddělení uživatelů
- Klíčová umožňující technologie pro víceuživatelský MIMO (MU-MIMO)
- Implementována jak na downlinku (předkódování), tak na uplinku (prostorové filtrování)
- Dynamicky plánována na základě geometrie uživatelů a stavu kanálu

## Související pojmy

- [MU-MIMO – Multi-User Multiple Input Multiple Output](/mobilnisite/slovnik/mu-mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services

---

📖 **Anglický originál a plná specifikace:** [SDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/sdma/)
