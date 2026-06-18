---
slug: "lcr"
url: "/mobilnisite/slovnik/lcr/"
type: "slovnik"
title: "LCR – Low Chip Rate"
date: 2025-01-01
abbr: "LCR"
fullName: "Low Chip Rate"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lcr/"
summary: "Low Chip Rate (LCR) označuje rychlost šíření 1,28 Mcps používanou v rozhraní TD-SCDMA (Time Division-Synchronous Code Division Multiple Access), což je standard 3G. Definuje základní časování a rychlo"
---

LCR je frekvence šíření (chip rate) 1,28 Mcps používaná v rozhraní TD-SCDMA, která definuje základní časování a rychlost rozprostření spektra pro tuto technologii 3. generace.

## Popis

Low Chip Rate (LCR), konkrétně 1,28 Megachipů za sekundu (Mcps), je definující parametr fyzické vrstvy pro [TD-SCDMA](/mobilnisite/slovnik/td-scdma/) (Time Division-Synchronous Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)), technologii rádiového přístupu standardizovanou 3GPP. TD-SCDMA je standard 3G využívající časový duplex ([TDD](/mobilnisite/slovnik/tdd/)) a fungující primárně v nepárových kmitočtových pásmech. Rychlost šíření je základním parametrem každého systému založeného na [CDMA](/mobilnisite/slovnik/cdma/), určuje šířku pásma signálu s rozprostřeným spektrem a časovou granularitu rozhraní. Rychlost 1,28 Mcps má za následek nominální šířku nosné přibližně 1,6 MHz, což je méně než 3,84 Mcps používané u [WCDMA](/mobilnisite/slovnik/wcdma/) ([UTRA](/mobilnisite/slovnik/utra/) [FDD](/mobilnisite/slovnik/fdd/)).

Rámová struktura TD-SCDMA je na této rychlosti šíření založena. Rádiový rámec o délce 10 ms je rozdělen na dva podrámce po 5 ms. Každý podrámec obsahuje několik časových slotů (obvykle 7 za normálního provozu), které lze přidělit pro vysílání ve směru uplink nebo downlink, což poskytuje flexibilní a asymetrickou kapacitu. Uvnitř každého časového slotu jsou jednotliví uživatelé rozlišeni pomocí různých kódu pro rozprostření spektra (kanalizační kódy) s rozprostíracím faktorem, který je celočíselnou mocninou dvou, a to až do 16. 'Synchronní' aspekt TD-SCDMA je umožněn synchronizací ve směru uplink, kdy uživatelská zařízení (UE) upravují své časování vysílání na základě pokynů sítě, aby zajistily, že všechny uplink signály dorazí do Node B přibližně ve stejný čas. Tím se snižuje vnitrobuněčný interference a zvyšuje kapacita.

Mezi klíčové fyzické kanály patří DwPCH (Downlink Pilot Channel), UpPCH (Uplink Pilot Channel) a [FPACH](/mobilnisite/slovnik/fpach/) (Fast Physical Access Channel) pro počáteční přístup a synchronizaci. Data jsou přenášena na kanálech jako je DCH (Dedicated Channel). Kombinace TDD, nižší rychlosti šíření, chytrých antén a technik společné detekce dávala TD-SCDMA konkrétní výhody v určitých scénářích nasazení, jako je efektivní podpora asymetrického provozu a potenciálně vyšší spektrální efektivita v kontrolovaných prostředích. Její architektura byla integrována do specifikací 3GPP UMTS jako alternativní režim rádiového přístupu.

## K čemu slouží

LCR TD-SCDMA byl vyvinut za účelem vytvoření standardu mobilní sítě 3G optimalizovaného pro provoz s časovým duplexem (TDD), který řešil specifické tržní a technické potřeby, zejména v Číně. Primárním motivem bylo umožnit efektivní využití nepárových přidělení spektra, která byla k dispozici a nebyla dostatečně využita. Na rozdíl od párového spektra používaného WCDMA (FDD) nevyžaduje TDD spektrum symetrická pásma pro uplink a downlink, což umožňuje flexibilnější přidělování regulátory.

Volba nízké rychlosti šíření 1,28 Mcps oproti 3,84 Mcps u WCDMA byla podmíněna několika faktory. Nižší rychlost šíření zjednodušuje návrh přijímače, zejména pro pokročilé techniky víceuživatelské detekce a chytrých antén, které byly ústřední pro výkonnostní parametry TD-SCDMA. Také umožňuje užší šířku pásma nosné (1,6 MHz), což usnadňuje nasazení v fragmentovaném spektru a poskytuje podrobnější stavební kámen pro plánování sítě. Technologie měla za cíl nabídnout nákladově efektivní migrační cestu ze sítí GSM 2G v Číně, podporující služby s vysokou přenosovou rychlostí při využití domácích inovací. Řešila omezení čistě FDD 3G tím, že poskytovala řešení šité na míru pro asymetrický internetový provoz a scénáře pokrytí v interiérech.

## Klíčové vlastnosti

- Rychlost šíření 1,28 Mcps definující šířku pásma nosné přibližně 1,6 MHz
- Provoz s časovým duplexem (TDD) pro flexibilní přidělování uplink/downlink
- Synchronizace ve směru uplink pro snížení vnitrobuněčné interference
- Integrace možností chytrých antén a společné detekce
- Rámová struktura založená na podrámcích 5 ms s více přepínacími body
- Standardizováno jako součást 3GPP UTRA TDD 1.28 Mcps

## Související pojmy

- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)
- [3G – Third Generation Mobile Telecommunications System](/mobilnisite/slovnik/3g/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services

---

📖 **Anglický originál a plná specifikace:** [LCR na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcr/)
