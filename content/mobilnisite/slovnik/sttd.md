---
slug: "sttd"
url: "/mobilnisite/slovnik/sttd/"
type: "slovnik"
title: "STTD – Space Time Transmit Diversity"
date: 2025-01-01
abbr: "STTD"
fullName: "Space Time Transmit Diversity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sttd/"
summary: "Technika přenosové diverzity pro WCDMA, která zlepšuje spolehlivost signálu vysíláním signálů ze dvou antén se specifickým časoprostorovým kódováním. Potlačuje útlum a zvyšuje výkon downlinku bez nutn"
---

STTD je technika přenosové diverzity pro WCDMA, která zlepšuje spolehlivost signálu v downlinku vysíláním kódovaných signálů ze dvou antén pro potlačení útlumu, aniž by vyžadovala další přijímací antény na straně UE.

## Popis

Space Time Transmit Diversity (STTD, prostorově-časová přenosová diverzita) je otevřená (open-loop) schéma přenosové diverzity standardizované pro [WCDMA](/mobilnisite/slovnik/wcdma/) (UMTS) downlink. Funguje tak, že kóduje proud komplexních modulačních symbolů (např. z [QPSK](/mobilnisite/slovnik/qpsk/)) přes dvě vysílací antény pomocí specifického prostorově-časového blokového kódu (STBC), konkrétně Alamoutiho kódu pro dvě antény. Základní operace spočívá ve vysílání původní posloupnosti symbolů z první antény a transformované posloupnosti z druhé antény. Pro dvojici po sobě jdoucích symbolů S1 a S2 vysílá anténa 1 S1 následovaný S2, zatímco anténa 2 vysílá -S2* následovaný S1*, kde * označuje komplexní sdružení. Toto ortogonální kódování umožňuje uživatelskému zařízení (UE) s jedinou anténou kombinovat signály z obou vysílacích antén pomocí jednoduchého lineárního přijímače, čímž efektivně vytváří virtuální systém MISO (Multiple-Input Single-Output) 2x1. Přijímač využívá inherentní ortogonalitu k oddělení datových proudů, čímž poskytuje zisk z diverzity, který zmírňuje účinky útlumu a zlepšuje poměr signálu k interferenci ([SIR](/mobilnisite/slovnik/sir/)).

Z architektonického hlediska je STTD implementována ve fyzické vrstvě Node B, konkrétně ve strukturách vyhrazeného fyzického kanálu ([DPCH](/mobilnisite/slovnik/dpch/)) a společného pilotního kanálu ([CPICH](/mobilnisite/slovnik/cpich/)). Schéma vyžaduje dvě fyzicky oddělené vysílací antény na stanovišti Node B. Kritickou součástí je společný pilotní kanál (CPICH), který musí být také vysílán s předem známým vzorem z obou antén, aby mohlo UE odhadnout impulsní odezvu kanálu pro každou anténu zvlášť. Tyto odhady kanálu jsou nezbytné pro koherentní kombinaci diverzních signálů. UE nemusí poskytovat zpětnou vazbu o stavu kanálu (channel state information) do Node B, což z STTD činí otevřenou (open-loop) techniku vhodnou pro mobilní scénáře s rychle se měnícími kanály.

Úlohou STTD v síti je zlepšit pokrytí a kapacitu downlinku, zejména pro hlasové a nízkorychlostní až středněrychlostní datové služby v UMTS. Zlepšením spolehlivosti spoje umožňuje použít nižší vysílací výkon pro danou kvalitu služby, čímž snižuje interferenci v buňce a zvyšuje celkovou kapacitu systému. Šlo o základní techniku [MIMO](/mobilnisite/slovnik/mimo/) (Multiple-Input Multiple-Output) v 3GPP, která do buněčných standardů zavedla koncepty prostorové diverzity a prostorově-časového kódování. Zatímco pozdější verze standardů zavedly pokročilejší techniky uzavřené smyčky (closed-loop) MIMO a beamforming, STTD poskytovala robustní a relativně jednoduchou metodu pro dosažení významných benefitů z diverzity, zejména pro UE na okrajích buněk nebo v náročných rádiových podmínkách.

## K čemu slouží

STTD byla vytvořena k řešení kritického problému vícecestného útlumu (multipath fading) v mobilních rádiových kanálech pro rané 3G systémy [WCDMA](/mobilnisite/slovnik/wcdma/). Koncem 90. let a na počátku tisíciletí bylo klíčovou výzvou zajištění spolehlivého výkonu downlinku pro vznikající datové služby. Jednoduchá přijímací diverzita na straně UE byla nákladná a zvětšovala rozměry zařízení. STTD poskytla řešení na straně sítě, které přesunulo složitost na Node B, což umožnilo i jednoduchým telefonům s jednou anténou těžit ze zisku přenosové diverzity. To byl hlavní motiv pro její zařazení do Release 99.

Technologie řešila omezení spočívající pouze v časové diverzitě (prostřednictvím prokládání a kódování) nebo frekvenční diverzitě v jednofrekvenčním systému WCDMA. Využitím prostorové diverzity prostřednictvím více vysílacích antén poskytovala konzistentnější a robustnější signál, který příčně potlačoval hluboké útlumy. Tím se zlepšil rozpočet downlinku, rozšířil dosah buňky a zvýšila se spolehlivost datových služeb, aniž by to vyžadovalo změny v hardwaru přijímače stávající populace UE. Její otevřená povaha (open-loop) znamenala, že efektivně fungovala pro všechna UE bez ohledu na jejich rychlost, na rozdíl od některých režimů uzavřené smyčky (closed-loop), které vyžadovaly stabilní podmínky kanálu a zpětnou vazbu.

Historicky byla STTD jedním z prvních praktických implementací teorie prostorově-časového kódování, zejména Alamoutiho schématu, v hlavním komerčním bezdrátovém standardu. Ukázala hmatatelné výhody víceanténních technik a připravila cestu pro sofistikovanější technologie [MIMO](/mobilnisite/slovnik/mimo/) a beamforming, které definují 4G a 5G. Její zavedení v R99 stanovilo základní úroveň robustnosti downlinku, která byla zásadní pro komerční životaschopnost datových služeb UMTS.

## Klíčové vlastnosti

- Otevřená (open-loop) přenosová diverzita využívající Alamoutiho prostorově-časové blokové kódování
- Vyžaduje dvě vysílací antény na Node B
- Nevyžaduje zpětnou vazbu o stavu kanálu (channel state information) od UE
- Kompatibilní s přijímači UE s jednou anténou
- Aplikována na vyhrazené fyzické kanály (DPCH) a přidružené řídicí kanály
- Využívá samostatně vysílané společné pilotní kanály (CPICH) pro každou anténu pro odhad kanálu

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [STTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sttd/)
