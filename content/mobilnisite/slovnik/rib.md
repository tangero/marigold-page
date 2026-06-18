---
slug: "rib"
url: "/mobilnisite/slovnik/rib/"
type: "slovnik"
title: "RIB – Radiated Interface Boundary"
date: 2025-01-01
abbr: "RIB"
fullName: "Radiated Interface Boundary"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rib/"
summary: "Radiated Interface Boundary (RIB) je definovaná referenční rovina pro testování přes vzduch (OTA) rádiového zařízení, zejména pro ověření shody (conformance) a výkonu. Specifikuje přesný bod, ve které"
---

RIB je definovaná referenční rovina pro testování přes vzduch (over-the-air), která specifikuje přesný bod, ve kterém se měří vyzařované signály, aby bylo zajištěno standardizované ověření rádiového zařízení.

## Popis

Radiated Interface Boundary (RIB) je konceptuální a praktická referenční rovina zavedená ve specifikacích 3GPP za účelem standardizace metodologií testování přes vzduch ([OTA](/mobilnisite/slovnik/ota/)) pro rádiová zařízení, včetně uživatelských zařízení (UE) a základnových stanic (gNB/[eNB](/mobilnisite/slovnik/enb/)). Definuje přesnou prostorovou hranici, typicky kouli nebo plochu ve stanovené vzdálenosti od testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)), na které se měří vyzařované [RF](/mobilnisite/slovnik/rf/) charakteristiky, jako je výkon vysílače, citlivost přijímače, charakteristiky svazku a prostorový výkon. Tato hranice je zásadní, protože posouvá testování mimo vedené porty (jako koaxiální konektory) a umožňuje vyhodnocení kompletního integrovaného rádiového systému včetně antén způsobem, který odpovídá reálným provozním podmínkám. Koncept RIB je základní pro zajištění konzistentního hodnocení metrik výkonu, jako je celkový vyzařovaný výkon ([TRP](/mobilnisite/slovnik/trp/)), celková izotropní citlivost (TIS) a zisk beamformingu, napříč různými testovacími laboratořemi a dodavateli zařízení.

Z architektonického hlediska RIB není fyzickou součástí, ale definovaným referenčním bodem v rámci testovacích sestav, jako jsou bezodrazové komory nebo reverbní komory. Klíčové specifikace, zejména v řadě 38.8xx (např. 38.817, 38.820, 38.877), podrobně popisují aplikaci RIB pro kmitočtová pásma FR1 (pod 6 GHz) a FR2 (mmWave). Pro FR2, kde je beamforming klíčový, je RIB ústřední pro hodnocení kulového pokrytí, efektivního izotropního vyzařovaného výkonu ([EIRP](/mobilnisite/slovnik/eirp/)) a citlivosti přijímače v různých směrech. Testování zahrnuje umístění DUT do středu souřadnicového systému, přičemž sondy nebo měřicí antény jsou umístěny na povrchu RIB pro vzorkování vyzařovaného pole. To umožňuje charakterizaci jak vedeného, tak vyzařovaného výkonu a překlenuje propast mezi tradičním RF testováním a výkonem na systémové úrovni.

Úloha RIB v síťovém ekosystému je primárně ve fázi před nasazením, kde zajišťuje, že zařízení splňují požadavky 3GPP na vyzařovaný výkon. Poskytuje opakovatelný rámec pro testování shody (conformance), typové schvalování a akceptační testy operátorů. To je obzvláště důležité pro systémy massive [MIMO](/mobilnisite/slovnik/mimo/) a beamforming v 5G, kde jsou anténní pole integrována a nelze je testovat pouze vedenými metodami. Definováním RIB umožňuje 3GPP ověřování klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je efektivita prostorového multiplexování, spolehlivost předávání spojení (handover) za mobility a konzistence pokrytí, což přímo ovlivňuje uživatelský zážitek a efektivitu sítě.

## K čemu slouží

RIB byl zaveden, aby řešil rostoucí komplexitu rádiových systémů, zejména s nástupem integrovaných antén a pokročilých beamformingových technologií v 4G LTE a 5G NR. Předchozí přístupy se silně spoléhaly na vedené testování na RF portech, což se stalo nedostatečným, když se antény staly neoddělitelnými od transceiverů, zvláště v mmWave pásmech, kde je beamforming inherentní. Vedení testy nemohly zachytit reálné efekty, jako je účinnost antény, zkreslení charakteristik nebo prostorové vlastnosti, což vedlo k potenciálním nesouladům mezi laboratorními výsledky a výkonem v terénu. RIB poskytuje standardizovanou hranici pro OTA testování, což zajišťuje, že zařízení jsou hodnocena jako holistické systémy, což je klíčové pro interoperabilitu a záruky výkonu ve více-dodavatelských sítích.

Historicky absence jednotné referenční rovně pro OTA vedla k nekonzistentnostem v testovacích metodologiích napříč různými regiony a certifikačními orgány, což komplikovalo globální schvalování zařízení. RIB, zavedený v Release 15 spolu s 5G NR, tyto metodologie formalizoval a umožnil reprodukovatelná měření vyzařovaného výkonu, citlivosti a metrik svazku. Tím řeší problémy související s certifikací zařízení pro nová kmitočtová pásma, zejména v FR2, kde jsou tradiční konektory nepraktické. Podporuje také vývoj směrem k vyšším kmitočtům a integrovanějším návrhům a zajišťuje, že tvrzení o výkonu jsou ověřitelná a v souladu se scénáři nasazení sítě, což v konečném důsledku zlepšuje uživatelský zážitek prostřednictvím spolehlivých rádiových spojů.

## Klíčové vlastnosti

- Definuje standardizovanou referenční rovinu pro vyzařovaná měření přes vzduch (OTA)
- Podporuje testování integrovaných anténních systémů, což je zvláště kritické pro mmWave (FR2) kmitočty
- Umožňuje měření celkového vyzařovaného výkonu (TRP) a celkové izotropní citlivosti (TIS)
- Umožňuje charakterizaci beamformingových charakteristik a kulového pokrytí pro MIMO systémy
- Zajišťuje opakovatelnost a konzistenci napříč různými testovacími laboratořemi a prostředími
- Aplikovatelné pro testování shody (conformance) a výkonu jak uživatelských zařízení (UE), tak základnových stanic

## Související pojmy

- [TRP – Transmission and Reception Point](/mobilnisite/slovnik/trp/)

## Definující specifikace

- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.114** (Rel-19) — EMC for Active Antenna System Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [RIB na 3GPP Explorer](https://3gpp-explorer.com/glossary/rib/)
