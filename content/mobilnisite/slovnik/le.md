---
slug: "le"
url: "/mobilnisite/slovnik/le/"
type: "slovnik"
title: "LE – Array Element Loss"
date: 2025-01-01
abbr: "LE"
fullName: "Array Element Loss"
category: "Physical Layer"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/le/"
summary: "LE kvantifikuje ztrátu výkonu signálu, ke které dochází na jednotlivých prvcích anténního pole v systému MIMO nebo beamformingu. Je to klíčový parametr pro modelování realistického výkonu anténního po"
---

LE je ztráta výkonu signálu na jednotlivých prvcích anténního pole, což je klíčový parametr pro modelování realistického výkonu pole v systémech MIMO a beamformingu podle 3GPP.

## Popis

Ztráta na prvku pole (LE) je parametr definovaný ve specifikacích 3GPP, který charakterizuje neideální, reálný výkon anténních polí používaných v pokročilých rádiových systémech, zejména pro vícevstupně vícevýstupní systémy ([MIMO](/mobilnisite/slovnik/mimo/)) a beamforming. V ideálním teoretickém poli se předpokládá, že každý vyzařovací prvek je identický a bezeztrátový. V praxi však výrobní tolerance, nedokonalosti materiálů, vzájemné vazby mezi prvky a ztráty ve výkonové síti způsobují odchylky. LE modeluje celkovou ztrátu výkonu na každém prvku, která snižuje efektivní izotropně vyzářený výkon ([EIRP](/mobilnisite/slovnik/eirp/)) a redukuje zisk pole. Tato ztráta je odlišná od celkové systémové ztráty a je specificky připisována anténnímu prvku a jeho bezprostřední napájecí struktuře.

Z architektonické a provozní perspektivy je LE integrována do výpočtů rozpočtu přenosové cesty a požadavků na výkon definovaných ve specifikacích jako 38.820 (pro NR) a 43.050 (pro scénáře [RF](/mobilnisite/slovnik/rf/) systémů). Když základnová stanice (gNB v 5G NR nebo [eNB](/mobilnisite/slovnik/enb/) v LTE) vytváří paprsek, je signál váhován a přiváděn na každý anténní prvek. Hodnota LE pro každý prvek signál před jeho vyzářením utlumí. Systémoví návrháři a plánovači sítí musí s touto ztrátou počítat, aby zajistili, že vysílaný výkon splňuje regulatorní limity a poskytuje zamýšlené pokrytí. Ovlivňuje také kalibrační procedury pro anténní pole, protože rozdíly v LE mezi prvky mohou vést ke zkreslení tvaru paprsku a zvýšeným úrovním bočních laloků.

Role LE v síti je zásadně spojena se zajištěním přesné predikce výkonu a standardizace. Definováním typických nebo maximálních přípustných hodnot LE umožňuje 3GPP konzistentní testování a benchmarkování zařízení od různých dodavatelů. To zajišťuje, že reálná nasazení základnových stanic poskytují slibované zisky ve spektrální účinnosti a pokrytí, které nabízejí technologie MIMO a beamformingu. V systémech massive MIMO s desítkami nebo stovkami prvků může být kumulativní dopad LE významný, což činí jeho přesnou charakterizaci nezbytnou pro predikci propustnosti na okraji buňky a celkové kapacity sítě.

## K čemu slouží

Koncept ztráty na prvku pole (LE) byl zaveden, aby překlenul propast mezi ideální teorií anténních polí a jejich praktickou implementací ve standardech 3GPP. Rané systémy [MIMO](/mobilnisite/slovnik/mimo/) a chytrých antén byly často modelovány s dokonalými prvky, což vedlo k optimistickým predikcím výkonu, které neodpovídaly výsledkům nasazení v terénu. Účelem definice LE je vnést do systémových specifikací realismus a zajistit, aby požadavky na výkon a testy shody odrážely dosažitelný výkon hardwaru. To umožňuje spravedlivé srovnání zařízení různých dodavatelů a stanovuje realistická očekávání pro operátory sítí.

Historicky, jak se buněčné systémy vyvíjely od jednoduchých transceiverů s jednou anténou ke komplexním víceanténním systémům v LTE (od Rel-8 dále) a zejména s nástupem beamformingu velkého rozsahu v 5G NR, se potřeba detailního modelování [RF](/mobilnisite/slovnik/rf/) parametrů stala klíčovou. Bez zohlednění ztrát na jednotlivých prvcích by vypočítaný zisk beamformingu a poměr signálu k šumu a rušení ([SINR](/mobilnisite/slovnik/sinr/)) byly nadhodnoceny. To by mohlo vést k poddimenzovaným sítím, mezerám v pokrytí a nesplnění cílů kvality služeb. Standardizací LE řeší 3GPP omezení předchozích zjednodušených modelů a poskytuje společný rámec pro specifikaci a testování vysokofrekvenčního výkonu anténních polí.

LE je navíc zásadní pro definování požadavků na vedený výkon transceiverů základnových stanic. Specifikace oddělují výkon aktivní rádiové jednotky od pasivního anténního pole. Definice LE umožňuje jasné rozhraní (jako je anténní konektor) a zajišťuje, že kombinovaný systém – aktivní a pasivní části – splňuje celkové standardy pro vyzařovaný výkon. Tento modulární přístup usnadňuje ekosystém více dodavatelů, kde lze rádiové jednotky a antény pořizovat nezávisle, za předpokladu, že splňují jednotlivé požadavky na LE a další parametry.

## Klíčové vlastnosti

- Modeluje ztrátu výkonu na jednotlivých anténních prvcích v poli
- Klíčová pro přesnou predikci výkonu systémů MIMO a beamformingu
- Integrována do specifikací 3GPP pro rozpočet přenosové cesty a testování shody RF
- Odlišná od celkové ztráty na přenosové cestě systému nebo ztráty v kabelu
- Ovlivňuje efektivní izotropně vyzářený výkon (EIRP) a zisk pole
- Nezbytná pro realistické simulační a síťové plánovací nástroje

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)
- [EIRP – Effective Isotropic Radiated Power](/mobilnisite/slovnik/eirp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services

---

📖 **Anglický originál a plná specifikace:** [LE na 3GPP Explorer](https://3gpp-explorer.com/glossary/le/)
