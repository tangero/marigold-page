---
slug: "frc"
url: "/mobilnisite/slovnik/frc/"
type: "slovnik"
title: "FRC – Fixed Reference Measurement Channel"
date: 2025-01-01
abbr: "FRC"
fullName: "Fixed Reference Measurement Channel"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/frc/"
summary: "FRC je standardizovaná, přesně definovaná sada parametrů fyzické vrstvy používaná pro konzistentní a opakovatelné testování rádiového výkonu uživatelského zařízení (UE) a základnové stanice. Specifiku"
---

FRC je standardizovaná sada parametrů fyzické vrstvy používaná pro konzistentní testování rádiového výkonu tím, že specifikuje velikost transportního bloku, modulaci, kódování a mapování na zdroje.

## Popis

Fixed Reference Measurement Channel (FRC) je základní nástroj pro testování shody definovaný v mnoha technických specifikacích 3GPP. Nejde o funkční kanál používaný v provozní síti, ale o testovací konfiguraci. FRC poskytuje úplnou a jednoznačnou definici přenosu na fyzickém downlinkovém sdíleném kanálu ([PDSCH](/mobilnisite/slovnik/pdsch/)) nebo fyzickém uplinkovém sdíleném kanálu (PUSCH) pro účely testování rádiofrekvenčního (RF) výkonu a demodulace. Definice zahrnuje všechny potřebné parametry pro generování předvídatelného signálu: přesnou velikost transportního bloku (TBS), modulační schéma (např. QPSK, [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM), kódovací rychlost kanálu (založenou na konkrétní redundantní verzi), alokaci fyzických bloků zdrojů (PRB) a konfiguraci referenčního signálu. Během testování testovací zařízení (emulátor základnové stanice) generuje signál přesně podle specifikace FRC a testované zařízení (UE nebo gNB) jej musí úspěšně demodulovat a dekódovat s chybovostí pod stanovenou mezí (např. blokovou chybovostí 10 %). Klíčovými součástmi FRC jsou jeho jedinečný identifikátor (např. FRC A1-1, FRC A3-3), přidružená konfigurační tabulka referenčního měřicího kanálu ve specifikaci a odpovídající tabulka požadavků na výkon. Jeho úlohou je izolovat a měřit specifické schopnosti přijímače, jako je citlivost, maximální vstupní úroveň nebo selektivita sousedního kanálu, za kontrolovaných a opakovatelných podmínek, což zajišťuje, že všichni výrobci testují svá zařízení proti stejnému referenčnímu bodu.

## K čemu slouží

FRC existuje pro řešení problému nekonzistentního a neporovnatelného testování rádiového výkonu zařízení založených na 3GPP. Bez pevné reference by různé testovací laboratoře nebo výrobci mohli používat mírně odlišné konfigurace signálu, což by vedlo k výsledkům, které nelze spravedlivě porovnat, a potenciálně by umožnilo, aby podstandardní zařízení prošla testy využitím mezer v testovacích postupech. Vytvoření FRC bylo motivováno potřebou přísného typového zkušebnictví, které garantuje základní úroveň výkonu sítě a spektrální účinnosti. Historicky, jak se buněčné technologie vyvíjely od GSM přes UMTS k LTE, testovací složitost exponenciálně rostla. FRC poskytují standardizovaný 'testovací vektor', který zajišťuje, že každé UE nebo základnová stanice je hodnoceno za identických, náročných rádiových podmínek. To garantuje, že zařízení splňující výkonnostní specifikace 3GPP budou v reálných sítích spolehlivě interoperabilní, čímž se udržuje celková kvalita sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Přesně definovaná velikost a obsah transportního bloku
- Pevné modulační a kódovací schéma (MCS)
- Specifická alokace fyzických bloků zdrojů (PRB) a doba trvání
- Přidružená konfigurace referenčního signálu (DM-RS)
- Propojení se specifickými požadavky na RF výkon a demodulaci (např. citlivost, ACS)
- Definováno pro různé šířky kanálů a případy použití (např. MIMO, agregace nosných)

## Související pojmy

- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.113** (Rel-19) — EMC Requirements for E-UTRA Base Stations
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [FRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/frc/)
