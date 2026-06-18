---
slug: "sgh"
url: "/mobilnisite/slovnik/sgh/"
type: "slovnik"
title: "SGH – Standard Gain Horn"
date: 2025-01-01
abbr: "SGH"
fullName: "Standard Gain Horn"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sgh/"
summary: "Standard Gain Horn (SGH) je typ mikrovlnné antény s přesně známými a stabilními charakteristikami zisku, používaný jako referenční standard pro kalibraci jiných antén a měření výkonu rádiového zařízen"
---

SGH (Standard Gain Horn) je mikrovlnná anténa s přesně známým a stabilním ziskem, používaná jako referenční standard pro kalibraci jiných antén a měření výkonu rádiového zařízení v testovacím prostředí.

## Popis

Standard Gain Horn (SGH) je pyramidální nebo kuželová rohová anténa navržená pro provoz v určitém frekvenčním pásmu s vysoce předvídatelným a opakovatelným vyzařovacím diagramem. Její zisk, definovaný jako poměr intenzity vyzařování v daném směru k intenzitě, kterou by vytvořil hypotetický izotropní zářič, je charakterizován pomocí důkladných teoretických výpočtů a měření. Díky tomu slouží jako 'standard', vůči kterému lze porovnávat jiné antény. V kontextu testování podle 3GPP se SGH primárně používají v anechoických komorách a jiných řízených prostředích k vytvoření známé referenční roviny pro měření vyzařovaného výkonu a citlivosti.

Při provozu je SGH připojen ke kalibrovanému vektorovému analyzátoru ([VNA](/mobilnisite/slovnik/vna/)) nebo měřicímu přijímači. Při testování zařízení, jako je UE, se SGH používá buď jako referenční vysílací anténa, nebo jako referenční přijímací anténa. Například pro měření celkového vyzařovaného výkonu ([TRP](/mobilnisite/slovnik/trp/)) UE se UE umístí na pozicionovací systém a SGH, fungující jako přijímač, měří výkon přijímaný od UE ze všech úhlů v prostoru. Protože je zisk SGH na testovací frekvenci přesně znám, lze přesně vypočítat absolutní výkon vysílaný UE. Opačně, pro měření celkové izotropní citlivosti (TIS) se ze SGH vysílá známá úroveň signálu a měří se citlivost přijímače UE.

Klíčem k jejímu využití je její stabilita a nízká nejistota měření. Na rozdíl od integrovaných antén v UE, které mají komplexní, nepravidelné vyzařovací diagramy, má SGH hladký, dobře prozkoumaný diagram s nízkými postranními laloky a dobře definovaným hlavním svazkem. Její fyzická konstrukce zajišťuje minimální odrazy a vysokou čistotu polarizace. Testovací specifikace 3GPP (např. pro vyzařovací výkonnost v pásmech FR1 a FR2) vyžadují použití takových referenčních antén, aby bylo zajištěno, že výsledky testů z různých laboratoří jsou srovnatelné. SGH tedy není součástí provozní sítě, ale základním nástrojem v testování shody, ověřování výkonnosti a typovém schvalování rádiového zařízení, které zajišťuje, že zařízení splňují regulační a standardy stanovené požadavky na vyzařovací výkonnost před uvedením do provozu.

## K čemu slouží

Standard Gain Horn existuje k vyřešení základního problému nejistoty měření při testování rádiových frekvencí ([RF](/mobilnisite/slovnik/rf/)). Před standardizací metodik [OTA](/mobilnisite/slovnik/ota/) testů využívajících referenční antény jako SGH se výkon zařízení často měřil pouze pomocí vedených testů (pomocí kabelových spojů), což ignorovalo kritické efekty integrované antény zařízení. To bylo nedostatečné, zejména když se zařízení zmenšovala a výkon jejich antén se stal nedílnou součástí celkové schopnosti zařízení. Potřeba přesných a opakovatelných měření vyzařovaných vlastností se stala prvořadou.

Její přijetí ve specifikacích 3GPP bylo motivováno snahou průmyslu zavést důsledné OTA testování pro regulační shodu (např. [FCC](/mobilnisite/slovnik/fcc/), [CE](/mobilnisite/slovnik/ce/) značení) a přijetí operátory. Různé zkušebny používající různé vybavení by bez společného referenčního standardu přinášely nesrovnatelné výsledky. SGH tuto společnou referenci poskytuje. Řeší omezení použití testovaného zařízení ([DUT](/mobilnisite/slovnik/dut/)) samotného nebo nereferenčních antén jako standardu, které zavádějí neznámé proměnné a znemožňují oddělit výkonnost testovacího systému od výkonnosti DUT.

Historicky se SGH používají v obecném RF inženýrství po desetiletí. Práce 3GPP, zejména od Release 13 se zaměřením na LTE-Advanced a později 5G NR, zahrnovala standardizaci testovacích metodik a uspořádání, které SGH začleňují. To zajišťuje, že když specifikace 3GPP stanoví požadavek na [TRP](/mobilnisite/slovnik/trp/), každá certifikovaná testovací laboratoř na světě jej měří metodou vztažitelnou ke stejnému základnímu standardu – známému zisku referenční rohové antény. To je klíčové pro globální interoperabilitu, spravedlivou konkurenci mezi výrobci zařízení a v konečném důsledku pro zajištění konzistentního a spolehlivého bezdrátového výkonu, který zažívají uživatelé sítí.

## Klíčové vlastnosti

- Přesně charakterizovaná a stabilní hodnota zisku v určeném frekvenčním pásmu
- Nízký poměr stojatých vln (VSWR) zajišťující efektivní přenos výkonu s minimálním odrazem
- Dobře definovaný vyzařovací diagram s hladkým hlavním lalokem a nízkými postranními laloky pro přesná směrová měření
- Vysoká čistota polarizace (typicky lineární) pro izolaci kopolarizovaných a křížově polarizovaných složek
- Odolná mechanická konstrukce pro konzistentní výkonnost a dlouhou životnost v testovacím prostředí
- Vztahovatelná kalibrace k národním nebo mezinárodním standardům (např. NIST) zajišťující integritu měření

## Definující specifikace

- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TR 38.871** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [SGH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgh/)
