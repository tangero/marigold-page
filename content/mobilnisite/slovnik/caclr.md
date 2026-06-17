---
slug: "caclr"
url: "/mobilnisite/slovnik/caclr/"
type: "slovnik"
title: "CACLR – Cumulative Adjacent Channel Leakage Ratio"
date: 2025-01-01
abbr: "CACLR"
fullName: "Cumulative Adjacent Channel Leakage Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/caclr/"
summary: "CACLR je klíčový parametr výkonu vysílače v 3GPP, který měří celkový nežádoucí únik výkonu z vysílače do více sousedních rádiových kanálů vzhledem k výkonu v jeho vlastním přiděleném kanálu. Je zásadn"
---

CACLR je metrika 3GPP, která měří celkový nežádoucí únik výkonu vysílače do více sousedních rádiových kanálů vzhledem k výkonu v jeho vlastním přiděleném kanálu.

## Popis

Cumulative Adjacent Channel Leakage Ratio (CACLR) je přísný parametr konformního rádiového testu (RF) definovaný ve specifikacích 3GPP pro základnové stanice (Node B, [eNB](/mobilnisite/slovnik/enb/), gNB) a uživatelská zařízení. Kvantifikuje schopnost vysílače udržet vyzářený výkon v rámci přiděleného kanálového pásma, konkrétně měřením celkového výkonu úniku, který přetéká do definované sady sousedních frekvenčních kanálů. Na rozdíl od jednoduššího Adjacent Channel Leakage Ratio ([ACLR](/mobilnisite/slovnik/aclr/)), který obvykle uvažuje pouze první sousední kanál, CACLR sčítá výkon úniku přes několik sousedních kanálů (např. první, druhý a někdy i třetí sousední kanál) a porovnává tento kumulativní nežádoucí výkon s výkonem v hlavním vysílaném kanálu. To poskytuje komplexnější hodnocení spektrální čistoty vysílače a jeho potenciálu způsobit širokopásmovou interferenci.

Metodika měření CACLR je podrobně popsána v dokumentech 3GPP TS 25.104, 36.104 a 38.104 pro UTRA, [E-UTRA](/mobilnisite/slovnik/e-utra/) a NR. Testovací sestava zahrnuje kalibrovaný analyzátor signálu nebo specializovaný testovací přijímač. Testované zařízení vysílá standardizovaný testovací signál při určeném výstupním výkonu. Přijímač následně změří výkon v pásmu přiděleného kanálu (P_assigned) a integrovaný výkon v pásmech určených sousedních kanálů (P_adj1, P_adj2, ...). CACLR se pak vypočítá jako poměr součtu výkonů v sousedních kanálech k výkonu v přiděleném kanálu, obvykle vyjádřený v decibelech (dB). Nižší hodnota CACLR znamená lepší výkon, tedy menší únik výkonu do sousedních pásem. Přesný počet uvažovaných sousedních kanálů a požadované limitní hodnoty jsou specifikovány podle rádiového přístupového standardu (RAT), frekvenčního pásma a šířky kanálu.

Úloha CACLR je zásadní pro výkon fyzické vrstvy sítě. Přímo ovlivňuje kapacitu a kvalitu služeb v prostředích s více operátory a více nosnými. Vysoká hodnota CACLR může způsobit významnou interferenci přijímačům v sousedních kanálech, zhoršit jejich poměr signálu k interferenci a šumu (SINR) a vést k přerušeným hovorům, snížené datové propustnosti a neefektivnímu využití spektra. Vynucováním přísných požadavků na CACLR zajišťuje 3GPP, že základnové stanice a zařízení mohou koexistovat ve stejné geografické oblasti bez způsobení nepřijatelného zhoršení služeb ostatních. To je obzvláště důležité pro nasazení s časovým duplexem (TDD), kde mohou základnové stanice vysílat současně na sousedních kanálech, a pro scénáře agregace nosných ([CA](/mobilnisite/slovnik/ca/)), kde zařízení nebo základnová stanice agreguje více komponentních nosných, které jsou blízko u sebe ve frekvenci.

## K čemu slouží

CACLR byl zaveden, aby řešil omezení měření úniku do jednoho kanálu ([ACLR](/mobilnisite/slovnik/aclr/)) v moderních, spektrem přeplněných celulárních sítích. Jak se sítě vyvíjely z nasazení s jednou nosnou ke složitějším architekturám, jako je agregace nosných, sdílení sítí a hustá nasazení malých buněk, potenciál pro kumulativní interferenci od jednoho vysílače do více blízkých kanálů se stal kritickým problémem. Vysílač může projít jednotlivými testy ACLR pro každý sousední kanál, ale stále generovat významné celkové množství nežádoucího vyzařování mimo pásmo, když se jeho úniky přes několik kanálů sečtou. Tento kumulativní efekt mohl desenzibilizovat přijímače pracující na nepřímých sousedních kanálech, což scénář, který tradiční metriky adekvátně nezachycovaly.

Vytvoření CACLR bylo motivováno potřebou holističtějšího a realističtějšího nástroje pro hodnocení interference. Řeší problém zajištění předvídatelných a zvládnutelných úrovní interference v reálných scénářích, kde je více kanálů od stejného nebo různých operátorů nasazeno v těsné spektrální blízkosti. Stanovením limitu pro celkový nežádoucí výkon, který může vysílač vyzářit do bloku spektra sousedícího s jeho alokací, CACLR chrání celkovou integritu rádiového prostředí. To umožňuje regulátorům a operátorům těsněji zabalit kanály, zlepšit celkovou spektrální účinnost a umožnit vyšší kapacitu sítě, což je nezbytné pro uspokojení rostoucí poptávky po mobilních širokopásmových službách. Představuje vývoj v RF konformním testování od analýzy na úrovni komponent k řízení interference na systémové úrovni.

## Klíčové vlastnosti

- Měří celkový únik vysílače do více sousedních kanálů
- Poskytuje komplexnější hodnocení interference než jednokanálové ACLR
- Definován pro UTRA, E-UTRA a NR v příslušných specifikacích 3GPP pro základnové stanice
- Zásadní pro zajištění koexistence v nasazeních s více nosnými a více operátory
- Klíčový parametr pro konformní testování a typové schvalování rádiového zařízení
- Podporuje efektivní využití spektra v hustých síťových scénářích

## Související pojmy

- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)

## Definující specifikace

- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.809** (Rel-11) — E-UTRA & MSR BS Class Requirements
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [CACLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/caclr/)
