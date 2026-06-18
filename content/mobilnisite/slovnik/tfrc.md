---
slug: "tfrc"
url: "/mobilnisite/slovnik/tfrc/"
type: "slovnik"
title: "TFRC – Transport Format and Resource Combination"
date: 2025-01-01
abbr: "TFRC"
fullName: "Transport Format and Resource Combination"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tfrc/"
summary: "TFRC je základní koncept v UMTS (WCDMA), který definuje konkrétní mapování velikosti datového bloku transportního kanálu, kódovacího schématu a prostředků fyzické vrstvy (jako jsou rozprostřovací kódy"
---

TFRC je základní entita 3GPP UMTS, která definuje mapování velikosti datového bloku transportního kanálu, kódovacího schématu a fyzických prostředků pro plánovaný přenos.

## Popis

Transport Format and Resource Combination (TFRC, kombinace transportního formátu a prostředků) je centrální plánovací entita v UMTS rádiové přístupové síti ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně na rozhraní vzduchu [WCDMA](/mobilnisite/slovnik/wcdma/). Představuje kompletní sadu parametrů, které definují, jak jsou data z transportního kanálu (TrCH) doručena přes fyzickou vrstvu v daném přenosovém časovém intervalu ([TTI](/mobilnisite/slovnik/tti/)). TFRC zahrnuje tři klíčové aspekty: Transportní formát ([TF](/mobilnisite/slovnik/tf/)), který specifikuje velikost bloku a typ kanálového kódování/řízení rychlosti; fyzické prostředky, primárně kanalizační kód (nebo kódy) a pro [TDD](/mobilnisite/slovnik/tdd/) časový slot(y); a pro některé konfigurace i vysílací výkon. Plánovač Node B vybírá TFRC pro každé aktivní uživatelské zařízení (UE) každý TTI (např. každé 2 ms, 10 ms) na základě faktorů jako kvalita kanálu (hlašování [CQI](/mobilnisite/slovnik/cqi/)), dostupný výkon buňky, kódové prostředky a požadavky QoS. Vybraný TFRC přímo určuje okamžitou přenosovou rychlost (Transport Format Combination, [TFC](/mobilnisite/slovnik/tfc/)) pro UE. Proces zahrnuje konfiguraci sady povolených TFRC pro každé UE rádiovým síťovým řadičem ([RNC](/mobilnisite/slovnik/rnc/)) během zřizování rádiového přenosového kanálu. Node B pak z této sady dynamicky vybírá. To umožňuje rychlé plánování na úrovni buňky, které se přizpůsobuje rychlým změnám kanálu, maximalizuje spektrální efektivitu a zajišťuje QoS. Výběr TFRC je úzce spojen s rychlým řízením výkonu a je klíčovým rozlišovacím znakem paketových schopností WCDMA (HSDPA/HSUPA tento koncept dále rozvinuly s jemnějším plánováním).

## K čemu slouží

TFRC byl vyvinut pro umožnění efektivních paketových datových služeb přes rozhraní vzduchu WCDMA v UMTS. Předchozí systémy s přepojováním okruhů alokovaly pevné prostředky po dobu trvání hovoru, což bylo pro prchavý datový provoz neefektivní. Koncept TFRC zavedl flexibilní, plánovaný přístup k alokaci prostředků. Vyřešil problém, jak dynamicky sdílet omezené a proměnlivé fyzické prostředky (rozprostřovací kódy, vysílací výkon) mezi více uživateli s různými podmínkami kanálu a datovými nároky. Tím, že Node B mohl každých několik milisekund vybrat optimální kombinaci transportního formátu a fyzických prostředků, mohl systém úzce přizpůsobit alokovanou kapacitu okamžitým potřebám a stavu kanálu každého uživatele. To byl radikální odklon od GSM/GPRS a byl to zásadní předpoklad pro poskytování vysokorychlostních datových služeb. Poskytl základ pro adaptaci rychlosti, QoS-aware plánování a efektivní využití CDMA rozhraní vzduchu, což příře řešilo klíčovou výzvu podpory jak v reálném čase (hlas, video), tak mimo reálný čas (prohlížení webu, email) probíhajících služeb přes sdílený kanál.

## Klíčové vlastnosti

- Definuje kompletní mapování z Transportního kanálu na přenos fyzické vrstvy
- Kombinuje Transportní formát (velikost bloku, kódování) s fyzickými prostředky (kódy, časové sloty)
- Dynamicky vybírán plánovačem Node B každý přenosový časový interval (TTI)
- Umožňuje rychlou adaptaci na měnící se podmínky rádiového kanálu (pomocí CQI)
- Klíčový mechanismus pro implementaci QoS-aware paketového plánování v UTRAN
- Přímo určuje okamžitou datovou rychlost uživatele (Transport Format Combination)

## Definující specifikace

- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization

---

📖 **Anglický originál a plná specifikace:** [TFRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfrc/)
