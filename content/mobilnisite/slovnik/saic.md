---
slug: "saic"
url: "/mobilnisite/slovnik/saic/"
type: "slovnik"
title: "SAIC – Single Antenna Interference Cancellation"
date: 2025-01-01
abbr: "SAIC"
fullName: "Single Antenna Interference Cancellation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/saic/"
summary: "Technologie přijímače, známá také jako Downlink Advanced Receiver Performance (DARP) fáze I, která zvyšuje kapacitu a pokrytí sítě GSM potlačením ko-kanálového rušení pomocí jedné antény. Umožňuje ter"
---

SAIC je technologie přijímače, která zvyšuje kapacitu a pokrytí sítě GSM potlačením ko-kanálového rušení pomocí jedné antény k dekódování požadovaných signálů i za přítomnosti silného rušení.

## Popis

Single Antenna Interference Cancellation (SAIC) je pokročilá technika přijímače na fyzické vrstvě standardizovaná pro sítě GSM/[EDGE](/mobilnisite/slovnik/edge/). Je navržena pro práci se standardním mobilním terminálem s jednou anténou, čímž se odlišuje od řešení s více anténami, jako jsou diverzitní přijímače. Základním principem SAIC je digitální zpracování signálu uvnitř přijímače za účelem oddělení a potlačení dominantního ko-kanálového rušiče – jiného signálu GSM vysílaného na stejném kmitočtu a ve stejném časovém slotu, ale z jiné buňky. Přijímač využívá skutečnost, že jak požadovaný signál, tak rušič jsou modulovány [GMSK](/mobilnisite/slovnik/gmsk/), což je modulace s konstantní obálkou používaná v GSM.

Algoritmus SAIC typicky pracuje tak, že modeluje přijatý signál jako kombinaci požadovaného signálu, jednoho silného rušiče a šumu v pozadí. Pomocí adaptivního filtrování a odhadovacích technik, jako jsou koncepty Joint Detection nebo Interference Rejection Combining ([IRC](/mobilnisite/slovnik/irc/)) upravené pro jednu anténu, přijímač odhadne parametry rušivého signálu. Následně rekonstruuje odhad rušiče a odečte jej od celkového přijatého signálu, čímž získá „čistší“ verzi požadovaného signálu pro demodulaci. Tento proces výrazně zlepšuje poměr Carrier-to-Interference ([C/I](/mobilnisite/slovnik/c-i/)) na vstupu demodulátoru.

Implementace SAIC je zcela v User Equipment (UE); na straně GSM Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)) nejsou vyžadovány žádné změny. To činí SAIC účinným nástrojem pro vylepšení sítě prostřednictvím vývoje terminálů. Tím, že umožňuje mobilním zařízením snášet vyšší úrovně rušení, mohou operátoři zvýšit faktory opakovaného využití kmitočtu – hustěji rozmístit buňky na stejné sadě kmitočtů – a tím zvýšit celkovou kapacitu sítě. Také rozšiřuje pokrytí na okrajích buněk, kde je rušení ze sousedních buněk typicky vysoké, čímž zlepšuje udržení hovoru a kvalitu hlasu. SAIC jako [DARP](/mobilnisite/slovnik/darp/) fáze I položil základy pro pokročilejší techniky potlačení rušení v pozdějším vývoji GSM a ovlivnil principy návrhu přijímačů pro následující technologie.

## K čemu slouží

SAIC byl vyvinut k řešení kritického omezení kapacity ve zralých sítích GSM. S růstem počtu účastníků se operátoři potýkali se silným ko-kanálovým rušením v důsledku těsného opakovaného využití kmitočtů, což zhoršovalo kvalitu hovoru a zvyšovalo míru přerušených hovorů, zejména v hustě obydlených městských oblastech. Tradiční techniky plánování sítě, jako je dělení buněk a přeskakování kmitočtů, se stávaly nedostatečnými nebo příliš nákladnými. Byla zde zřejmá potřeba řešení, které by mohlo zlepšit poměr signálu k rušení na straně přijímače bez nutnosti dalšího spektra nebo rozsáhlých změn infrastruktury.

Motivací pro SAIC v rámci iniciativy 3GPP [DARP](/mobilnisite/slovnik/darp/) bylo umožnit cestu k získání kapacitních výhod prostřednictvím vylepšeného výkonu terminálů formou „softwarového upgradu“. Před SAIC vyžadovalo zlepšení odolnosti vůči rušení diverzitní přijímače se dvěma anténami, které byly složitější, větší a dražší. SAIC ukázal, že významných zlepšení lze dosáhnout i s jednou anténou pomocí sofistikovaného digitálního zpracování signálu, což učinilo tuto technologii vhodnou pro masově vyráběné mobilní telefony. Řešil problém jednoho silného ko-kanálového rušiče, což byl běžný a limitující scénář v sítích GSM.

Tím, že efektivně zvýšil toleranci sítě vůči rušení, umožnil SAIC operátorům agresivněji využívat jejich stávající spektrální zdroje. To se přímo promítlo do schopnosti obsloužit více uživatelů na buňku nebo udržet kvalitu služeb při těsnějším opakovaném využití kmitočtů. Jeho zavedení ve verzi 8, dokonce i v době nasazování 3G, poskytlo klíčový nástroj pro zvýšení kapacity obrovské instalované základny sítí GSM, prodloužilo jejich životnost a zlepšilo kvalitu služeb.

## Klíčové vlastnosti

- Funguje se standardním mobilním terminálem s jednou anténou
- Potlačuje jednoho dominantního ko-kanálového GMSK rušiče
- Implementována zcela v přijímači UE prostřednictvím digitálního zpracování signálu
- Zlepšuje poměr Carrier-to-Interference (C/I) na vstupu demodulátoru
- Umožňuje těsnější opakované využití kmitočtů pro zvýšení kapacity sítě
- Zlepšuje pokrytí na okrajích buněk zvýšením odolnosti vůči rušení

## Definující specifikace

- **TS 45.015** (Rel-19) — DARP Phase II Requirements for Release 5 MS
- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [SAIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/saic/)
