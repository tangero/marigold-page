---
slug: "cp-ofdm"
url: "/mobilnisite/slovnik/cp-ofdm/"
type: "slovnik"
title: "CP-OFDM – Cyclic Prefix Orthogonal Frequency Division Multiplexing"
date: 2025-01-01
abbr: "CP-OFDM"
fullName: "Cyclic Prefix Orthogonal Frequency Division Multiplexing"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cp-ofdm/"
summary: "CP-OFDM je základní vlnová forma pro 5G NR, která využívá ortogonální subnosné a cyklický prefix k umožnění efektivního vysokorychlostního přenosu dat. Bojuje proti rozprostření vícecestného zpoždění"
---

CP-OFDM je základní vlnová forma pro 5G NR, která využívá ortogonální subnosné a cyklický prefix k umožnění efektivního vysokorychlostního přenosu dat bojem proti vícecestnému zpoždění a zjednodušením ekvalizace.

## Popis

Cyclic Prefix Orthogonal Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) (CP-OFDM) je primární vlnová forma přijatá pro rozhraní 5G New Radio (NR) pro downlink i uplink (s některými doplňkovými možnostmi pro uplink). Jedná se o vícekanálový modulační systém, kde je vysokorychlostní datový tok rozdělen na mnoho pomalejších toků, z nichž každý moduluje samostatnou ortogonální subnosnou. Tyto subnosné jsou úzce rozmístěny ve frekvenci a jejich ortogonalita – zajištěná přesným frekvenčním odstupem rovným převrácené hodnotě doby trvání symbolu – zabraňuje interferenci mezi nosnými ([ICI](/mobilnisite/slovnik/ici/)). Klíčovou architektonickou složkou je cyklický prefix ([CP](/mobilnisite/slovnik/cp/)), což je kopie koncové části [OFDM](/mobilnisite/slovnik/ofdm/) symbolu připojená na jeho začátek. Tím se lineární konvoluce vysílaného signálu s vícecestným kanálem transformuje na kruhovou konvoluci, což je klíčová vlastnost, která zjednodušuje ekvalizaci kanálu na přijímací straně na prosté násobení komplexním zesílením pro každou subnosnou.

Při provozu vysílač provede inverzní rychlou Fourierovu transformaci ([IFFT](/mobilnisite/slovnik/ifft/)), aby převedl frekvenční datové symboly (mapované na subnosné) na časový OFDM symbol. Poté je připojen cyklický prefix. Po přenosu rádiovým kanálem přijímač nejprve odstraní CP. Zbývající vzorky, představující kruhovou konvoluci, jsou zpracovány rychlou Fourierovou transformací ([FFT](/mobilnisite/slovnik/fft/)) pro obnovení frekvenčních symbolů. Odhad kanálu, typicky využívající referenční signály jako [DM-RS](/mobilnisite/slovnik/dm-rs/), poskytuje komplexní koeficienty kanálu pro každou subnosnou, což umožňuje jednoduchou jednooperandovou ekvalizaci pro kompenzaci amplitudových a fázových zkreslení. Tato efektivní ekvalizace je hlavní výhodou v širokopásmových kanálech s výrazným rozprostřením zpoždění.

Role CP-OFDM v síti 5G je základní. Její konstrukční parametry, známé jako numerologie, jsou definovány rozestupem subnosných a dobou trvání symbolu, které jsou škálovatelné (např. 15, 30, 60, 120, 240 kHz). Tato škálovatelnost, spojená se strukturou rámce, je zásadní pro podporu různorodých případů užití 5G: širší rozestup subnosných pro přenosy s nízkou latencí a robustní vysokorychlostní mobilitu a užší efektivní rozestup (prostřednictvím větších velikostí FFT) pro vylepšený mobilní širokopásmový přístup s širokou šířkou kanálového pásma. Kompatibilita vlnové formy s pokročilými víceanténními technikami, jako je Massive [MIMO](/mobilnisite/slovnik/mimo/) a beamforming, je také klíčovou předností, protože umožňuje přesné precoding a kombinování ve frekvenční oblasti. Dále její spektrální účinnost a schopnost zvládat frekvenčně selektivní útlum z ní činí hlavní technologii fyzické vrstvy 5G pro všechny scénáře nasazení.

## K čemu slouží

CP-OFDM byla přijata jako vlnová forma 5G NR, aby řešila omezení předchozích buněčných technologií a splnila přísné a různorodé výkonnostní cíle IMT-2020. V 4G LTE byl CP-OFDM používán pouze v downlinku, zatímco uplink využíval Single-Carrier FDMA (SC-FDMA) pro dosažení lepší účinnosti výkonového zesilovače na uživatelském zařízení (UE) za cenu určité ztráty flexibility plánování a složitosti víceuživatelského MIMO. Klíčovou motivací pro standardizaci CP-OFDM pro oba směry v 5G bylo sjednotit vlnovou formu, čímž se zjednoduší návrh systému, umožní efektivnější a flexibilnější víceuživatelské MIMO v uplinku a neortogonální víceuživatelské přístupové schémata a plně využije širší šířky pásma dostupné na vyšších frekvencích.

Technologie zásadně řeší problém intersymbolové interference (ISI) způsobené vícecestným šířením v bezdrátových kanálech. Cyklický prefix funguje jako ochranný interval, který absorbuje rozprostření zpoždění kanálu. Pokud délka CP překročí maximální rozprostření zpoždění kanálu, je ISI z předchozího symbolu omezena na část CP, která je na přijímači odstraněna. Tímto elegantním způsobem se zmírňuje jedna z hlavních překážek širokopásmové bezdrátové komunikace. Dále tím, že umožňuje jednoduchou ekvalizaci ve frekvenční oblasti, snižuje složitost přijímače pro vysokorychlostní přenosy přes frekvenčně selektivní kanály, což je scénář, který se stává výraznějším s širšími šířkami pásma používanými v 5G.

Historicky byl OFDM úspěšný ve standardech jako IEEE 802.11 (Wi-Fi) a 4G LTE downlink. Jeho rozšíření jako sjednocená 5G vlnová forma bylo hnací silou potřeby dopředné kompatibility, extrémní flexibility v numerologii pro podporu služeb od massive IoT po vylepšený mobilní širokopásmový přístup a ultra-spolehlivou nízkolatenční komunikaci (URLLC) a vnitřní vhodnosti pro pokročilé anténní systémy. CP-OFDM poskytuje robustní, spektrálně účinný a výpočetně zvládnutelný základ, na kterém jsou postaveny všechny ostatní pokroky fyzické vrstvy 5G.

## Klíčové vlastnosti

- Používá cyklický prefix jako ochranný interval pro boj proti rozprostření vícecestného zpoždění a eliminaci intersymbolové interference
- Umožňuje jednoduchou jednooperandovou ekvalizaci ve frekvenční oblasti pro každou subnosnou díky vlastnosti kruhové konvoluce
- Podporuje škálovatelnou numerologii s proměnným rozestupem subnosných a dobou trvání symbolu pro různorodé případy užití 5G
- Poskytuje vysokou spektrální účinnost prostřednictvím ortogonálních subnosných a kompatibility se širokými kanálovými šířkami pásma
- Umožňuje pokročilé víceanténní techniky jako Massive MIMO a beamforming s precodingem ve frekvenční oblasti
- Přijata jako sjednocená vlnová forma pro downlink i uplink v 5G NR, což zjednodušuje návrh transceiveru

## Související pojmy

- [SC-FDMA – Single Carrier – Frequency Division Multiple Access](/mobilnisite/slovnik/sc-fdma/)

## Definující specifikace

- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [CP-OFDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cp-ofdm/)
