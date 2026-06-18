---
slug: "riv"
url: "/mobilnisite/slovnik/riv/"
type: "slovnik"
title: "RIV – Resource Indication Value"
date: 2025-01-01
abbr: "RIV"
fullName: "Resource Indication Value"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/riv/"
summary: "Kompaktní indexová hodnota používaná v řídicích informacích pro downlink (DCI) v LTE a NR k označení konkrétní sady fyzických bloků zdrojů (PRB) přidělených uživateli. Umožňuje efektivní signalizaci p"
---

RIV je kompaktní indexová hodnota používaná v řídicích informacích pro downlink v LTE a NR k označení konkrétní sady fyzických bloků zdrojů přidělených uživateli, což umožňuje efektivní signalizaci přidělení zdrojů.

## Popis

Hodnota indikace zdrojů (RIV) je kódovací mechanismus definovaný ve specifikacích LTE (3GPP TS 36.213) a NR (3GPP TS 38.214) pro signalizaci přidělení bloků zdrojů v povoleních pro downlink a uplink přenášených řídicími informacemi pro downlink ([DCI](/mobilnisite/slovnik/dci/)). Když plánovač na gNB (nebo eNodeB) rozhodne přidělit UE souvislou sadu fyzických bloků zdrojů ([PRB](/mobilnisite/slovnik/prb/)), musí toto přidělení efektivně sdělit. Přenos začátku a délky přidělení jako dvou samostatných čísel by plýtval vzácnými bity užitečného zatížení DCI. RIV tento problém řeší sloučením počátečního bloku zdrojů ([RB](/mobilnisite/slovnik/rb/)_start) a délky přidělení v souvislých PRB (L_RBs) do jedné celočíselné hodnoty.

Kódovací algoritmus je definován tak, že pro danou část šířky pásma o velikosti N_RB PRB se jakákoli platná kombinace počátečního indexu a délky (kde start + délka <= N_RB) mapuje na jedinečný RIV. Vzorec je: pokud (L_RBs - 1) <= floor(N_RB / 2), pak RIV = N_RB * (L_RBs - 1) + RB_start, jinak RIV = N_RB * (N_RB - L_RBs + 1) + (N_RB - 1 - RB_start). Tím vzniká vzájemně jednoznačné mapování. UE po přijetí DCI extrahuje pole RIV a dekóduje jej pomocí známého N_RB, aby odvodilo přesné hodnoty RB_start a L_RBs, a tím pochopilo přidělené frekvenční zdroje.

Tento mechanismus je klíčovou součástí přidělení zdrojů typu 0 (na bázi bitmapy) a typu 1 (na bázi RIV pro souvislá přidělení) v LTE a podobné principy platí v NR pro přidělení zdrojů typu 1. Jeho role je zásadní pro efektivitu dynamického plánování. Minimalizací režie řídicí signalizace pro nejběžnější typ přidělení (souvislé bloky) šetří kapacitu DCI, což umožňuje síti plánovat více uživatelů na oblast řídicího kanálu, čímž se zvyšuje celková kapacita systému a snižuje latence.

## K čemu slouží

RIV byl vytvořen k řešení problému režie řídicích kanálů v buňkových systémech založených na [OFDMA](/mobilnisite/slovnik/ofdma/), jako jsou LTE a NR. Řídicí kanály ([PDCCH](/mobilnisite/slovnik/pdcch/) v LTE, PDCCH v NR) mají omezenou kapacitu. Každý bit použitý k signalizaci přidělení zdrojů je bit, který nelze použít pro jiné účely, což omezuje počet uživatelů, které lze naplánovat na subrámec/slot. Naivní metoda signalizace přidělení zdrojů by vyžadovala až log2(N_[RB](/mobilnisite/slovnik/rb/)) bitů pro počáteční index a dalších log2(N_RB) bitů pro délku, což je neefektivní.

RIV poskytuje kompaktní, bezztrátové kódování, které využívá omezení, že přidělení jsou souvislá. Řeší problém rozvláčné signalizace zabalením dvou informací do jediné hodnoty, jejíž maximální velikost je právě dostatečná k jednoznačnému vyjádření všech možných souvislých přidělení v rámci šířky pásma. Tato optimalizace byla motivována potřebou vysoce efektivního dynamického plánování, které je základním kamenem paketově orientovaného, nízkolatenčního návrhu LTE a NR. Umožňuje síti činit rychlá, granulární plánovací rozhodnutí bez zatížení nadměrnou řídicí signalizací, což přímo přispívá k vysoké spektrální efektivitě a schopnostem multiplexování uživatelů v sítích 4G a 5G.

## Klíčové vlastnosti

- Kóduje počáteční index bloku zdrojů a počet souvislých bloků do jediného celého čísla
- Poskytuje bezztrátovou, kompaktní reprezentaci pro minimalizaci velikosti užitečného zatížení DCI
- Definován pro schémata přidělení zdrojů v LTE i NR
- Umožňuje efektivní signalizaci pro souvislá přidělení zdrojů ve frekvenční oblasti
- Dekódovací algoritmus je standardizován, což zajišťuje interoperabilitu mezi UE a sítí
- Základní prvek pro efektivitu dynamického plánování v systémech OFDMA

## Definující specifikace

- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data

---

📖 **Anglický originál a plná specifikace:** [RIV na 3GPP Explorer](https://3gpp-explorer.com/glossary/riv/)
