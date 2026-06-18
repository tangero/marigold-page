---
slug: "hsn"
url: "/mobilnisite/slovnik/hsn/"
type: "slovnik"
title: "HSN – Hopping Sequence Number"
date: 2025-01-01
abbr: "HSN"
fullName: "Hopping Sequence Number"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hsn/"
summary: "Hopping Sequence Number (HSN) je parametr v systému GSM a příbuzných systémech, který určuje konkrétní pořadí přeskoků kmitočtu pro spojení. Je klíčový pro implementaci přeskoku kmitočtů, techniky ome"
---

HSN je parametr v systému GSM a příbuzných systémech, který určuje konkrétní pořadí přeskoků kmitočtu pro spojení za účelem omezení rušení a útlumu.

## Popis

Hopping Sequence Number (HSN) je základní parametr na fyzické vrstvě GSM (Global System for Mobile Communications), který definuje jeden ze dvou klíčových prvků potřebných pro generování sekvence přeskoku kmitočtů, přičemž tím druhým je Mobile Allocation Index Offset ([MAIO](/mobilnisite/slovnik/maio/)). Přeskok kmitočtů je rozprostřená spektrální technika, při které vysílač a přijímač mění nosný kmitočet rádiového přenosu podle předem stanovené pseudonáhodné sekvence. HSN spolu s MAIO tuto sekvenci jednoznačně určují pro daný časový slot na dané sadě přidělených kmitočtů.

Technicky je HSN 6bitové číslo, umožňující 64 možných sekvencí přeskoku (0-63). Hodnota 0 označuje cyklický přeskok, při kterém se kmitočty používají v jednoduchém sekvenčním pořadí. Hodnoty 1 až 63 označují pseudonáhodné sekvence přeskoku. Algoritmus generování sekvence používá jako vstupy HSN, MAIO (který poskytuje uživatelsky specifický posun pro zabránění kolizím) a číslo rámce (které zajišťuje časovou závislost) k určení přesného kmitočtu, který má být použit v daném [TDMA](/mobilnisite/slovnik/tdma/) rámci. Tento algoritmus je standardizován a musí být shodně implementován jak v základnové přenosové stanici ([BTS](/mobilnisite/slovnik/bts/)), tak v mobilní stanici ([MS](/mobilnisite/slovnik/ms/)), aby byla zachována synchronizace.

V architektuře sítě je HSN parametr na úrovni buňky, který je typicky konfigurován operátorem sítě pro každou buňku nebo skupinu přeskoku kmitočtů. Je vysílán na kanálu [BCCH](/mobilnisite/slovnik/bcch/) (Broadcast Control Channel) jako součást informací popisu kanálu. Když je mobilní stanici přidělen provozní kanál ([TCH](/mobilnisite/slovnik/tch/)) využívající přeskok kmitočtů, síť sdělí příslušné parametry: seznam kmitočtů v seznamu mobilního přidělení ([MA](/mobilnisite/slovnik/ma/)), HSN pro danou buňku a jedinečné MAIO přidělené tomuto konkrétnímu spojení časového slotu. MS následně použije tyto parametry k určení svého vzoru přeskoku.

Role HSN je klíčová pro výkon přeskoku kmitočtů. Přiřazením různých HSN sousedním buňkám nebo sektorům síť zajišťuje, že jejich sekvence přeskoku jsou ortogonální nebo minimálně korelované. Tato randomizace rozprostírá stejněkanálové rušení (rušení z buněk používajících stejný kmitočet) v čase na mnoho různých kmitočtů, čímž přeměňuje potenciálně konstantní rušení vysoké úrovně na rušení nižší, zprůměrované úrovně. Tento proces, známý jako průměrování rušení, přímo zvyšuje kapacitu systému a zlepšuje kvalitu hovoru. Dále přeskok kmitočtů poskytuje kmitočtovou diverzitu, která potlačuje vícecestný útlum, protože je nepravděpodobné, že by hluboký útlum nastal současně na všech přeskakovaných kmitočtech, čímž se zlepšuje spolehlivost spoje.

## K čemu slouží

Přeskok kmitočtů, a tím i parametr HSN, byl v GSM zaveden k řešení dvou hlavních problémů v celulárních rádiových sítích: kmitočtově selektivního útlumu a stejněkanálového rušení. Rané celulární systémy trpěly degradací signálu v důsledku vícecestného šíření, kdy odražené kopie signálu způsobují destruktivní interferenci na specifických kmitočtech (útlum). Statický kanál mohl zažít hluboký útlum, což vedlo k přerušení hovoru. Přeskakování signálu přes více kmitočtů zajišťuje, že pouze malá část přenosu je ztracena během útlumu na jakémkoli jednotlivém kmitočtu, a kódování pro opravu chyb může ztracené bity obnovit.

Druhým a možná významnějším problémem je stejněkanálové rušení, které je základním omezením kapacity v celulárních systémech. Pro opakované použití kmitočtů a obsluhu mnoha uživatelů musí být stejný kmitočet použit v různých buňkách oddělených opakovací vzdáleností. V systému bez přeskoku trpí mobilní stanice na okraji své buňky konstantním silným rušením ze vzdálené buňky používající stejný kmitočet. To omezuje, jak blízko od sebe mohou být kmitočty opakovány. S náhodným přeskokem kmitočtů je rušení z této vzdálené buňky rozprostřeno přes všechny kmitočty přeskoku používané požadovaným signálem. Dotčené spojení zažije trochu rušení na mnoha kmitočtech místo velkého rušení na jednom kmitočtu. Tento průměrovací efekt umožňuje těsnější vzory opakování kmitočtů (např. přechod z opakovacího faktoru 12 nebo 9 na 3 nebo dokonce 1), což dramaticky zvyšuje kapacitu sítě bez nutnosti dalšího spektra.

Historicky specifikace HSN a přidruženého algoritmu přeskoku poskytla standardizovanou robustní metodu pro dosažení těchto zisků. Před sofistikovanými adaptivními technikami šlo o jednoduchou, ale účinnou formu řízení rušení a diverzity. Mechanismus HSN dal plánovačům sítí přímý nástroj pro řízení vztahů rušení mezi buňkami. Přiřazení stejného HSN sousedním buňkám mohlo být použito ke koordinaci přeskoku pro ještě lepší výkon v synchronizovaných sítích, zatímco různé HSN poskytly de-korelaci v nesynchronizovaných nasazeních. Tato flexibilita učinila přeskok kmitočtů v GSM základním prvkem pro zlepšení kvality a kapacity.

## Klíčové vlastnosti

- 6bitové číslo definující jednu z 64 možných pseudonáhodných sekvencí přeskoku
- Hodnota '0' určuje cyklický (sekvenční) přeskok; hodnoty 1-63 určují pseudonáhodný přeskok
- Klíčový vstup spolu s MAIO a číslem rámce do standardizovaného algoritmu generování sekvence přeskoku
- Typicky parametr platný pro celou buňku, vysílaný na BCCH
- Umožňuje ortogonální nebo randomizované vzory přeskoku mezi různými buňkami pro řízení rušení
- Základní pro dosažení benefitů průměrování rušení a kmitočtové diverzity

## Související pojmy

- [MAIO – Mobile Allocation Index Offset](/mobilnisite/slovnik/maio/)
- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [HSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/hsn/)
