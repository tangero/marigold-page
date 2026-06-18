---
slug: "idft"
url: "/mobilnisite/slovnik/idft/"
type: "slovnik"
title: "IDFT – Inverse Discrete Fourier Transform"
date: 2025-01-01
abbr: "IDFT"
fullName: "Inverse Discrete Fourier Transform"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/idft/"
summary: "Inverzní diskrétní Fourierova transformace (IDFT) je základní matematická operace používaná ve vlnových tvarech ortogonálního multiplexu s frekvenčním dělením (OFDM) a DFT-spread OFDM (DFT-s-OFDM) pro"
---

IDFT je základní matematická operace v sítích 4G a 5G, která převádí datové symboly z kmitočtové oblasti na signál v časové oblasti pro vysílání vlnových tvarů OFDM a DFT-s-OFDM.

## Popis

Inverzní diskrétní Fourierova transformace (IDFT) je klíčový algoritmus pro zpracování signálu v digitálních komunikacích, zejména pro vícekanálové modulační schémata jako je ortogonální multiplex s frekvenčním dělením ([OFDM](/mobilnisite/slovnik/ofdm/)). V kontextu 3GPP LTE a NR vysílač používá IDFT k transformaci bloku komplexních modulačních symbolů, které jsou mapovány na konkrétní podnosné v kmitočtové oblasti, na odpovídající sekvenci vzorků v časové oblasti. Tato časová sekvence tvoří základnový OFDM symbol připravený pro další zpracování (např. přidání cyklické předpony, převod z digitální na analogový signál a převod na rádiovou frekvenci).

Operace je definována matematicky. Pro vstupní sekvenci N komplexních symbolů v kmitočtové oblasti X[k], kde k = 0, 1, ..., N-1, IDFT vypočítá výstupní sekvenci v časové oblasti x[n] jako: x[n] = (1/√N) * Σ_{k=0}^{N-1} X[k] * e^{(j2πkn/N)} pro n = 0, 1, ..., N-1. Zde N odpovídá velikosti transformace, která přímo souvisí s počtem aktivních podnosných v OFDM symbolu. V praktických implementacích se toto počítá efektivně pomocí algoritmu inverzní rychlé Fourierovy transformace ([IFFT](/mobilnisite/slovnik/ifft/)), který snižuje výpočetní složitost z O(N²) na O(N log N). Specifikace 3GPP definují potřebné velikosti transformace (např. 128, 256, 512, 1024, 2048 pro LTE) odpovídající různým šířkám pásma systému.

Pro uplink zavedl LTE variantu známou jako DFT-spread OFDM (DFT-s-OFDM), také nazývanou Single-Carrier [FDMA](/mobilnisite/slovnik/fdma/) ([SC-FDMA](/mobilnisite/slovnik/sc-fdma/)). Zde proces zahrnuje dodatečný krok: nejprve je na časové modulační symboly aplikováno [DFT](/mobilnisite/slovnik/dft/) předkódování, které rozprostře jejich energii přes všechny podnosné, než je provedena větší IDFT (IFFT). To ve srovnání s konvenčním OFDM snižuje poměr špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)), což je výhodné pro účinnost výkonového zesilovače uživatelského zařízení (UE). V 5G NR zůstává IDFT klíčová pro vlnový tvar [CP-OFDM](/mobilnisite/slovnik/cp-ofdm/) (používaný v downlinku i uplinku) i pro vlnový tvar DFT-s-OFDM (volba pro uplink). NR podporuje flexibilnější numerologii s proměnným rozestupem podnosných, což je realizováno úpravou základních parametrů IDFT/IFFT a vzorkovací frekvence.

Správná aplikace IDFT zajišťuje ortogonalitu mezi podnosnými, což je klíčová vlastnost, která umožňuje demodulaci hustě uspořádaných, překrývajících se podnosných bez mezikanálového rušení ([ICI](/mobilnisite/slovnik/ici/)) v časově invariantním kanálu. Výstup IDFT tvoří jádro řetězce generování signálu fyzické vrstvy. Jeho inverzní operace, diskrétní Fourierova transformace (DFT), je prováděna na přijímači pro převod přijatých časových vzorků zpět na symboly v kmitočtové oblasti pro demodulaci a dekódování.

## K čemu slouží

IDFT se používá k řešení problému efektivního a robustního přenosu dat přes kmitočtově selektivní útlumové kanály. Před rozšířeným přijetím OFDM se modulační schémata s jedním nosným potýkala s vysokými datovými rychlostmi, protože kmitočtová selektivita kanálu způsobovala závažné mezisymbolové rušení (ISI), vyžadující složité ekvalizéry. Vícekanálová modulace, realizovaná prostřednictvím páru IDFT/DFT, rozdělí datový tok s vysokou rychlostí na mnoho paralelních toků s nízkou rychlostí, z nichž každý je vysílán na úzkopásmové podnosné. Díky tomu každá podnosná zažívá relativně plochý útlum, což zjednodušuje ekvalizaci kanálu na operaci škálování pro každou podnosnou.

Historická motivace vychází z potřeby spektrální účinnosti a odolnosti vůči vícecestnému šíření. IDFT umožňuje vytváření ortogonálních podnosných, jejichž spektra se překrývají, čímž je dosažena vyšší spektrální účinnost než u vícekanálových systémů bez překryvu. Tato ortogonalita, zachovaná dokud ji kanál nezničí (řešeno cyklickou předponou), umožňuje jednoduché zpracování v kmitočtové oblasti na přijímači. Výpočetní proveditelnost algoritmů IFFT/FFT učinila tento teoreticky elegantní přístup praktickým pro systémy komunikace v reálném čase.

V normách 3GPP bylo přijetí OFDM (a DFT-s-OFDM pro uplink) od vydání LTE Release 8 zásadním architektonickým odklonem od systémů 3G založených na CDMA. Bylo to hnací silou požadavků na vyšší datové rychlosti, lepší spektrální účinnost a flexibilnější přidělování šířky pásma. IDFT je motor, který tento vlnový tvar umožňuje, a její parametry (velikost, vzorkovací frekvence) jsou pečlivě standardizovány, aby byla zajištěna interoperabilita mezi základnovými stanicemi a uživatelskými zařízeními po celém světě, a zároveň poskytovaly flexibilitu potřebnou pro různé scénáře nasazení od úzkopásmového IoT po širokopásmový rozšířený mobilní širokopásmový přístup (eMBB).

## Klíčové vlastnosti

- Základní matematická operace pro generování vlnových tvarů OFDM a DFT-s-OFDM
- Efektivně implementována jako inverzní rychlá Fourierova transformace (IFFT)
- Velikost transformace (N) je konfigurovatelná na základě šířky pásma systému a numerologie
- Vynucuje ortogonalitu mezi hustě uspořádanými kmitočtovými podnosnými
- Nezbytná pro převod dat z kmitočtové mřížky zdrojů na časové vzorky pro vysílání
- Parametry standardizovány dle specifikace 3GPP pro zajištění interoperability

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [FFT – Fast Fourier Transformation](/mobilnisite/slovnik/fft/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 36.884** (Rel-13) — MMSE-IRC Receiver Performance for LTE BS
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec

---

📖 **Anglický originál a plná specifikace:** [IDFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/idft/)
