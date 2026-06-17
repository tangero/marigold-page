---
slug: "fdm"
url: "/mobilnisite/slovnik/fdm/"
type: "slovnik"
title: "FDM – Frequency Division Multiplexing"
date: 2025-01-01
abbr: "FDM"
fullName: "Frequency Division Multiplexing"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fdm/"
summary: "FDM (Frequency Division Multiplexing, multiplex s frekvenčním dělením) je základní přenosová technika, při níž je více signálů zkombinováno pro současný přenos sdíleným médiem přidělením každému signá"
---

FDM (Frequency Division Multiplexing, multiplex s frekvenčním dělením) je přenosová technika, při níž je více signálů současně přenášeno sdíleným médiem přidělením každému signálu odlišného, nepřekrývajícího se frekvenčního pásma.

## Popis

Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) (FDM, multiplex s frekvenčním dělením) je klasické analogové i digitální multiplexní schéma, které rozděluje celkovou dostupnou přenosovou šířku pásma na více užších, nepřekrývajících se frekvenčních subpásem neboli subnosných. Každá subnosná je modulována nezávislým datovým tokem. Tyto modulované subnosné jsou následně zkombinovány (multiplexovány) do složeného signálu pro přenos jediným sdíleným kanálem, jako je kabel, vlákno nebo rádiové frekvenční pásmo. Na přijímací straně pásmové propusti oddělí složený signál na jeho jednotlivé subnosné, které jsou následně demodulovány pro obnovení původních datových toků.

V kontextu systémů 3GPP se FDM typicky nepoužívá jako primární metoda vícenásobného přístupu na úrovni uživatele (tuto roli přebírají [FDMA](/mobilnisite/slovnik/fdma/), [OFDMA](/mobilnisite/slovnik/ofdma/), SC-FDMA). Místo toho je FDM základním konceptem pro kanalizaci a agregaci nosných. Například v LTE a 5G NR je systémová šířka pásma (např. 20 MHz) rozdělena na četné ortogonální subnosné (s rozestupem 15 kHz nebo širším v NR), což je v podstatě aplikace principů FDM, která je díky ortogonalitě efektivnější ([OFDM](/mobilnisite/slovnik/ofdm/)). Dále, když jsou pro jednoho uživatele agregovány vícekomponentní nosné ([CC](/mobilnisite/slovnik/cc/)) pomocí agregace nosných, jsou tyto CC často odděleny ve frekvenci, čímž se efektivně využívá FDM pro jejich kombinaci do širšího agregovaného kanálu.

Klíčové komponenty v systému založeném na FDM zahrnují modulátor/demodulátor pro každou subnosnou, multiplexor (kombinátor), který signály sčítá, a demultiplexor (banka filtrů), který je odděluje. V moderních digitálních implementacích se toto často provádí v základním pásmu pomocí technik digitálního zpracování signálu ([DSP](/mobilnisite/slovnik/dsp/)), jako je inverzní rychlá Fourierova transformace ([IFFT](/mobilnisite/slovnik/ifft/)) pro multiplexování a [FFT](/mobilnisite/slovnik/fft/) pro demultiplexování, jako v OFDM. Kritickým požadavkem je zachování dostatečných ochranných pásem mezi subnosnými, aby se zabránilo mezikanálovému rušení (ICI), které je v OFDM minimalizováno díky ortogonalitě.

Role FDM v sítích 3GPP je základní. Umožňuje rozdělení širokého bloku licencovaného spektra na zvládnutelné jednotky pro přenos. Je konceptuálním základem vícesystémových systémů. V plánování sítí se principy FDM používají k přiřazení různých frekvenčních kanálů sousedním buňkám (frekvenční plánování) za účelem řízení ko-kanálového rušení. Zatímco je jednodušší než metody s časovým dělením, čisté FDM může být méně spektrálně efektivní kvůli potřebným ochranným pásmům. Jeho vývoj do ortogonálních frekvenčně dělených technik (OFDM, OFDMA) z něj však učinil dominantní širokopásmovou přenosovou metodu ve 4G a 5G.

## K čemu slouží

Účelem FDM je umožnit více informačním tokům sdílet jediné fyzické přenosové médium bez vzájemného rušení. Před zavedením multiplexování vyžadoval přenos více signálů samostatné fyzické kanály (dráty, kabely nebo vyhrazené rádiové spoje), což bylo nákladné a neefektivní. FDM tento problém vyřešil využitím faktu, že různé signály mohou koexistovat, pokud zaujímají různé části frekvenčního spektra. To bylo revoluční pro ranou telekomunikaci a umožnilo přenášet více telefonních hovorů jediným hlavním vedením nebo kabelem.

V rádiové komunikaci FDM řešilo výzvu efektivního využití přiděleného bloku spektra. Namísto jednoho širokopásmového signálu pro jediného uživatele mohlo být spektrum rozděleno na mnoho úzkopásmových kanálů, z nichž každý sloužil jinému uživateli nebo službě. To je základní princip za systémy první generace (1G) analogových celulárních sítí, jako byl AMPS. Jednoduché FDM však mělo omezení: vyžadovalo analogové filtry, které byly složité, a ochranná pásma mezi kanály představovala promrhané spektrum.

Motivace pro jeho zařazení a vývoj ve standardech 3GPP pramení z jeho konceptuální přehlednosti a role jako odrazového můstku k pokročilejším technikám. Zatímco čistě analogové FDM je v digitálním rozhraní vzduchu z velké části zastaralé, základní myšlenka dělení frekvenčních zdrojů přetrvává. Je základem kanalizace systémů, konceptu agregace nosných a je přímým předchůdcem ortogonálního multiplexu s frekvenčním dělením (OFDM). Porozumění FDM je zásadní pro pochopení toho, jak moderní spektrálně efektivní technologie, jako je OFDMA, vyvinuté k překonání jeho neefektivit, dosáhly ortogonality subnosných, čímž odstranily potřebu ochranných pásem mezi nimi.

## Klíčové vlastnosti

- Dělí celkovou šířku pásma na nepřekrývající se frekvenční subpásma (subnosné)
- Umožňuje současný přenos více signálů sdíleným médiem
- Používá ochranná pásma k prevenci rušení mezi sousedními subnosnými
- Základ pro vícesystémové a kanalizované komunikační systémy
- Konceptuální základ pro OFDM, OFDMA a agregaci nosných
- Umožňuje frekvenční plánování a opakované využití v celulárních sítích

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [FDMA – Frequency Division Multiple Access](/mobilnisite/slovnik/fdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.755** (Rel-19) — NR FR1 DL Fragmented Carriers Study
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.787** (Rel-19) — UE Radio Transmission for Sidelink CA in ITS Band
- **TS 38.793** (Rel-19) — Simultaneous Rx/Tx Band Combinations TR
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 38.839** (Rel-17) — Simultaneous Rx/Tx band combinations
- **TR 38.868** (Rel-17) — Optimizations of pi/2 BPSK uplink power in NR
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [FDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/fdm/)
