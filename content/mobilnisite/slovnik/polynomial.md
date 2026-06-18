---
slug: "polynomial"
url: "/mobilnisite/slovnik/polynomial/"
type: "slovnik"
title: "Polynomial – Polynomial"
date: 2025-01-01
abbr: "Polynomial"
fullName: "Polynomial"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/polynomial/"
summary: "Matematická funkce používaná v kodecích 3GPP, zejména pro zpracování řeči a zvuku. Je definována s odstraněnými specifickými kořeny, aby zajistila stabilitu a výkon při návrhu digitálních filtrů. Toto"
---

Polynom je matematická funkce používaná v kodecích 3GPP, definovaná s odstraněnými specifickými kořeny za účelem zajištění stability a výkonu při návrhu digitálních filtrů pro zpracování řeči a zvuku.

## Popis

Ve specifikacích 3GPP je polynom matematický konstrukt zásadního významu pro digitální zpracování signálu, zejména v rámci řečových a zvukových kodeků. Nejde o obecný polynom, ale o polynom specifického tvaru, ve kterém jsou určité kořeny – typicky ty, které by mohly způsobit nestabilitu nebo nežádoucí frekvenční charakteristiku – explicitně odstraněny nebo omezeny. Tím je zajištěno, že výsledné digitální filtry (např. filtry lineární prediktivní kódování ([LPC](/mobilnisite/slovnik/lpc/))) jsou stabilní a splňují požadovaná výkonnostní kritéria pro hlasovou komunikaci. Koeficienty polynomu jsou odvozeny z analýzy řečového signálu a jsou klíčové pro reprezentaci spektrální obálky.

Hlavní uplatnění nachází v rámci rodiny algoritmů Algebraic Code-Excited Linear Prediction ([ACELP](/mobilnisite/slovnik/acelp/)), používaných v kodecích jako Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Zde polynom definuje syntézní filtr. Proces zahrnuje výpočet koeficientů lineární predikce ze vstupního zvukového rámce. Tyto koeficienty jsou následně transformovány do robustnější reprezentace, jako jsou Line Spectral Pairs ([LSP](/mobilnisite/slovnik/lsp/)) nebo Immittance Spectral Frequencies ([ISF](/mobilnisite/slovnik/isf/)), což jsou v podstatě kořeny specifických polynomů. Kvantizace a přenos těchto reprezentací kořenů je efektivnější a zajišťuje stabilitu filtru po dekódování.

Specifikace (např. TS 26.090 pro řečový kodek AMR) detailně popisují přesné tvary polynomů a procesy eliminace kořenů. Například kontrola stability zahrnuje ověření, že kořeny polynomu leží uvnitř jednotkové kružnice v z-rovině. 'Odstraněné' kořeny jsou ty, které jsou matematicky odstraněny nebo omezeny během procesu převodu z LPC koeficientů na přenosové parametry. Toto rigorózní matematické zpracování je tím, co zaručuje, že syntetizovaná řeč je prostá artefaktů a udržuje vysokou kvalitu i po kompresi a vlivu chyb na kanálu.

## K čemu slouží

Účelem definice polynomů s odstraněnými kořeny v 3GPP je zajistit algoritmickou stabilitu a efektivitu řečových kodeků. Digitální filtry, které jsou základním prvkem syntézy řeči v kodecích, se mohou stát nestabilními, pokud jejich póly přenosové funkce leží mimo jednotkovou kružnici. Nestabilní filtr by učinil kodek nepoužitelným, což by vedlo k neohraničenému výstupu nebo silnému zkreslení. Matematickým omezením polynomické reprezentace standard zaručuje, že všechny syntetizované filtry jsou inherentně stabilní, což je nezbytný požadavek pro spolehlivou telekomunikaci.

Historicky čelily rané digitální řečové kodeky výzvám se stabilitou při přímé kvantizaci a přenosu koeficientů filtru. Inovace reprezentace filtru pomocí kořenů specifických polynomů (jako [LSP](/mobilnisite/slovnik/lsp/)) poskytla robustnější sadu parametrů. Tyto reprezentace mají přirozené vlastnosti uspořádání a interpolace a jejich kvantizace je méně citlivá na chyby. Explicitní 'eliminace' určitých kořenů v definici zefektivňuje proces kódování a dekódování, zajišťuje konzistentní chování napříč všemi implementacemi a předchází okrajovým případům, které by mohly degradovat kvalitu. Tato matematická přísnost byla zásadní pro dosažení vysokých kompresních poměrů při zachování kvality řeči na úrovni veřejné telefonní sítě v mobilních sítích od 3G dále.

## Klíčové vlastnosti

- Zajišťuje stabilitu digitálních syntézních filtrů v řečových kodecích
- Definován s odstraněnými specifickými kořeny, aby se zabránilo nežádoucím frekvenčním charakteristikám
- Klíčový pro reprezentaci koeficientů lineární prediktivní kódování (LPC)
- Používán při převodu na robustní spektrální reprezentace, jako jsou Line Spectral Pairs (LSP)
- Základní prvek pro kodeky založené na ACELP, jako jsou AMR a EVS
- Detailně specifikován, aby byla zaručena interoperabilita mezi různými dodavateli

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [ACELP – Algebraic Code-Excited Linear Prediction](/mobilnisite/slovnik/acelp/)

## Definující specifikace

- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec

---

📖 **Anglický originál a plná specifikace:** [Polynomial na 3GPP Explorer](https://3gpp-explorer.com/glossary/polynomial/)
