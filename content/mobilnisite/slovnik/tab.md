---
slug: "tab"
url: "/mobilnisite/slovnik/tab/"
type: "slovnik"
title: "TAB – Transceiver Array Boundary"
date: 2025-01-01
abbr: "TAB"
fullName: "Transceiver Array Boundary"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tab/"
summary: "Transceiver Array Boundary (TAB) je konceptuální nebo fyzický demarkační bod definující rozhraní mezi jednotkou pro zpracování základního pásma (BBU) a polem rádiových transceiverů (často součást RRH"
---

TAB je demarkační bod definující rozhraní mezi jednotkou pro zpracování základního pásma a polem rádiových transceiverů v základnové stanici, což umožňuje standardizované víceanténní systémy.

## Popis

Transceiver Array Boundary (TAB) je základní architektonický koncept ve specifikacích 3GPP, který definuje funkční a fyzický oddělovací bod mezi jednotkou pro zpracování základního pásma ([BBU](/mobilnisite/slovnik/bbu/)) a polem rádiových transceiverů (často součást [RRH](/mobilnisite/slovnik/rrh/) nebo [AAU](/mobilnisite/slovnik/aau/)) v základnové stanici. Vytváří standardizované rozhraní, které vymezuje, kde končí digitální zpracování signálu základního pásma a začíná analogový přenos/příjem rádiových frekvencí ([RF](/mobilnisite/slovnik/rf/)). Tato hranice je klíčová pro disagregaci tradiční monolitické základnové stanice a umožňuje flexibilnější a škálovatelnější nasazení sítí.

Architektonicky se TAB nachází uvnitř gNB v 5G NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE. Na jedné straně hranice jednotka základního pásma zpracovává digitální signálové úlohy, jako je kódování kanálu, modulace/demodulace a mapování vrstev pro [MIMO](/mobilnisite/slovnik/mimo/). Na druhé straně pole transceiverů zahrnuje RF komponenty včetně digitálně-analogových převodníků ([DAC](/mobilnisite/slovnik/dac/)), analogově-digitálních převodníků ([ADC](/mobilnisite/slovnik/adc/)), výkonových zesilovačů, šumových zesilovačů, filtrů a fyzických anténních prvků. Rozhraní na úrovni TAB typně zahrnuje výměnu digitalizovaných časových vzorků IQ (fázového a kvadraturního signálu) nebo frekvenčních dat prvků zdrojů spolu s potřebnými řídicími a synchronizačními signály.

Role TAB je klíčová pro implementaci pokročilých anténních systémů (AAS) a massive MIMO. Její standardizací zajišťuje 3GPP interoperabilitu mezi jednotkami základního pásma a RF od různých výrobců, což podporuje konkurenceschopný ekosystém. Je základem klíčových technologií jako beamforming, který vyžaduje přesné řízení fáze a amplitudy signálu na každém anténním prvku. TAB definuje bod, do kterého lze beamformingové váhy aplikovat digitálně a kde přebírá kontrolu analogový RF řetězec. Toto oddělení je zásadní pro síťové architektury jako Centralized RAN (C-RAN), kde je zpracování základního pásma soustředěno v centrální lokalitě a propojeno přes fronthaul s dálkovými rádiovými jednotkami, přičemž TAB definuje možnosti funkčního rozdělení pro toto fronthaulové rozhraní.

## K čemu slouží

Transceiver Array Boundary byl zaveden, aby řešil rostoucí složitost a výkonnostní nároky víceanténních systémů v LTE-Advanced a 5G NR. Před jeho formální definicí byly implementace základnových stanic převážně integrovaná, výrobci specifická řešení, což znemožňovalo kombinovat jednotky základního pásma a rádiové jednotky od různých dodavatelů. Tento nedostatek standardizace brzdil inovace, zvyšoval náklady a omezoval flexibilitu nasazení pro operátory. TAB byl vytvořen, aby tyto komponenty oddělil a umožnil modulární přístup k návrhu základnových stanic.

Primární motivací byla podpora vývoje směrem k pokročilým anténním systémům (AAS) a massive MIMO, které vyžadují vysoký stupeň koordinace mezi četnými přenosovými cestami transceiverů. Standardizovaná hranice umožňuje specializovaný vývoj procesorů základního pásma (zaměřených na výpočetní výkon a algoritmy) a rádiových jednotek (zaměřených na RF výkon a energetickou účinnost) nezávisle na sobě. To je obzvláště důležité pro nové modely nasazení jako Cloud RAN (C-RAN), kde je zpracování základního pásma virtualizováno a centralizováno, což vyžaduje dobře definované, nízkolatencové a vysokokapacitní rozhraní k dálkovým rádiovým hlavám. TAB poskytuje architektonický základ pro tyto rozdělené architektury, specifikuje funkční rozdělení (jako Option 7-2x), které určuje, které zpracování probíhá před a za hranicí, což přímo ovlivňuje požadavky na fronthaul a celkový výkon systému.

## Klíčové vlastnosti

- Definuje funkční oddělení mezi zpracováním základního pásma a RF v základnové stanici
- Umožňuje standardizovaná rozhraní pro interoperabilní nasazení s více výrobci
- Základní pro implementaci technologií digitálního beamformingu a massive MIMO
- Podporuje flexibilní RAN architektury včetně D-RAN, C-RAN a vRAN
- Specifikuje bod pro výměnu IQ vzorků nebo frekvenčních dat
- Usnadňuje škálovatelnost a nezávislý vývoj zpracovatelských a rádiových jednotek

## Související pojmy

- [AAS – Active Antenna System](/mobilnisite/slovnik/aas/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [RU – Resource Utilization](/mobilnisite/slovnik/ru/)
- [DU – Triple DES Unwrap Plug-in](/mobilnisite/slovnik/du/)

## Definující specifikace

- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.114** (Rel-19) — EMC for Active Antenna System Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [TAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/tab/)
