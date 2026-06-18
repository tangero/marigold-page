---
slug: "vamos"
url: "/mobilnisite/slovnik/vamos/"
type: "slovnik"
title: "VAMOS – Voice services over Adaptive Multi-user Channels on One Slot"
date: 2025-01-01
abbr: "VAMOS"
fullName: "Voice services over Adaptive Multi-user Channels on One Slot"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/vamos/"
summary: "Funkce GSM/EDGE Radio Access Network (GERAN), která multiplexuje dva nebo čtyři hlasové uživatele do jednoho rádiového časového slotu. Významně zvyšuje hlasovou kapacitu a spektrální účinnost sítí GSM"
---

VAMOS je funkce GERAN, která multiplexuje dva nebo čtyři hlasové uživatele do jednoho rádiového časového slotu za účelem zvýšení kapacity a spektrální účinnosti sítě GSM.

## Popis

VAMOS je sofistikovaná funkce ve specifikacích [GERAN](/mobilnisite/slovnik/geran/), která zásadně zvyšuje kapacitu sítí GSM pro hlasové služby. Funguje tak, že umožňuje dvěma nebo dokonce čtyřem současným hlasovým hovorům sdílet jeden fyzický rádiový časový slot, což je základní jednotka vícečetného přístupu s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)) v GSM. Toho je dosaženo pomocí pokročilých technik zpracování signálu jak na základnové stanici ([BTS](/mobilnisite/slovnik/bts/)), tak na mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). Základním mechanismem je použití ortogonálních podkanálů (OSC), kde jsou dva uživatelé spárováni a přiřazeni ke stejnému časovému slotu, ale s různými, pečlivě vybranými tréninkovými sekvencemi ([TSC](/mobilnisite/slovnik/tsc/)), které jsou vzájemně ortogonální nebo téměř ortogonální. Tato ortogonalita umožňuje přijímači, využívajícímu pokročilé algoritmy pro potlačení interference, jako je Single Antenna Interference Cancellation ([SAIC](/mobilnisite/slovnik/saic/)) nebo schopnosti Downlink Advanced Receiver Performance ([DARP](/mobilnisite/slovnik/darp/)) fáze 2 v mobilu, oddělit dva překrývající se signály.

Systémová architektura zahrnuje úpravy BTS pro podporu generování složeného signálu v downlinku obsahujícího průběhy pro oba spárované uživatele. BTS musí také zvládnout příjem dvou simultánních signálů na stejné frekvenci a časovém slotu v uplinku. Klíčové síťové komponenty zahrnují BTS s transceivery (TRX) podporujícími VAMOS a mobilní stanice podporující DARP fázi 2 nebo lepší. Adaptivní vícerychlostní kodek ([AMR](/mobilnisite/slovnik/amr/)) je předpokladem, protože VAMOS využívá jeho robustnost. 'Adaptivní' aspekt VAMOS je klíčový: síť může dynamicky upravovat nerovnováhu výkonu mezi dvěma spárovanými podkanály na základě aktuálních podmínek přenosového kanálu a schopností spárovaných mobilů. Tato optimalizace řízení výkonu, řízená řadičem základnových stanic (BSC), je klíčová pro udržení kvality hovoru pro oba uživatele.

Během provozu BSC provádí párování uživatelů, vybírá dva mobily s kompatibilními schopnostmi přijímače a podmínkami kanálu. Poté nařídí BTS aktivovat režim VAMOS pro daný časový slot. BTS vysílá kombinovaný signál. V uplinku oba mobily vysílají současně a BTS, využívající své více antény pro příjem a techniky kombinace s potlačením interference (IRC), signály oddělí. Pro režim se čtyřmi uživateli (VAMOS Level II) je koncept rozšířen použitím modulace kvadraturní fázové manipulace (QPSK) namísto Gausovské minimální fázové manipulace (GMSK), čímž se efektivně vytvoří čtyři podkanály. Úlohou VAMOS je poskytnout nákladově efektivní zvýšení kapacity v rámci stávajícího spektra GSM, oddálit potřebu přerozdělení spektra pro jiné technologie a prodloužit životnost GSM infrastruktury pro hlasové a základní datové služby.

## K čemu slouží

VAMOS byl vytvořen, aby řešil kritickou výzvu zvýšení hlasové kapacity v sítích GSM bez nutnosti získání dalšího spektra. Jak počet mobilních účastníků exponenciálně rostl a spektrum se stalo vzácným a drahým zdrojem, potřebovali operátoři způsob, jak obsloužit více uživatelů ve svých stávajících přidělených kmitočtových pásmech GSM. Tradiční GSM přiděluje jeden časový slot na uživatele pro plnorychlostní hlasový hovor. Poloviční rychlostní kodeky nabízely zdvojnásobení kapacity, ale často za znatelné snížení kvality hlasu. VAMOS byl vyvinut jako nadřazené řešení, které dokáže zdvojnásobit nebo dokonce zečtyřnásobit spektrální účinnost při zachování kvality hlasu srovnatelné s plnorychlostním AMR, a to využitím pokroků v technologii mobilních přijímačů.

Historický kontext představuje dlouhý vývoj GSM souběžně s nasazením 3G a 4G. Operátoři často potřebovali udržovat rozsáhlé pokrytí GSM pro hlas, zejména ve venkovských oblastech a pro starší zařízení, a zároveň přerozdělovat cenná kmitočtová pásma (jako 900 MHz a 1800 MHz) pro UMTS a LTE pro vysokorychlostní data. VAMOS poskytl nástroj k 'vytěžení' větší hlasové kapacity ze zmenšené části spektra GSM, což umožnilo agresivnější přerozdělování spektra. Řešil problém spektrálního zahlcení pro hlasové služby, což operátorům umožnilo podporovat vyšší počet současných hovorů v hustě obydlených městských oblastech nebo během špičky provozu bez investic do nového spektra nebo dalších rádiových stanic. Přímo řešil omezení předchozích technik zvyšování kapacity, jako je přeskakování kmitočtů a kódování s poloviční rychlostí, tím, že nabídl efektivnější metodu multiplexování na fyzické vrstvě.

## Klíčové vlastnosti

- Párování dvou uživatelů do jednoho časového slotu pomocí ortogonálních podkanálů (OSC)
- Podpora adaptivního řízení nerovnováhy výkonu mezi spárovanými uživateli
- Volitelné multiplexování čtyř uživatelů pomocí modulace QPSK (VAMOS Level II)
- Vyžaduje podporu mobilní stanice pro DARP fázi 2 nebo SAIC
- Dynamické párování uživatelů a výběr režimu sítí (BSC)
- Zpětná kompatibilita se staršími mobilními zařízeními bez podpory VAMOS na časových slotech bez VAMOS

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [DARP – Downlink Advanced Receiver Performance](/mobilnisite/slovnik/darp/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 45.001** (Rel-19) — GSM Physical Layer Introduction
- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [VAMOS na 3GPP Explorer](https://3gpp-explorer.com/glossary/vamos/)
