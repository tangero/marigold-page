---
slug: "fbw"
url: "/mobilnisite/slovnik/fbw/"
type: "slovnik"
title: "FBW – Fractional Bandwidth"
date: 2025-01-01
abbr: "FBW"
fullName: "Fractional Bandwidth"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fbw/"
summary: "Bezrozměrný poměr vyjadřující šířku pásma signálu nebo kanálu vůči jeho střední frekvenci, klíčový pro charakterizaci širokopásmových a ultraširokopásmových systémů. V 5G NR je to klíčový parametr pro"
---

FBW je bezrozměrný poměr šířky pásma signálu k jeho střední frekvenci, používaný v 5G NR pro definici šířky kanálů a hodnocení RF výkonu, zejména na vysokých frekvencích.

## Popis

Fractional Bandwidth (FBW) je základní koncept v technice vysokých kmitočtů, definovaný jako poměr okamžité šířky pásma ([BW](/mobilnisite/slovnik/bw/)) signálu nebo provozní šířky pásma systému k jeho střední frekvenci (Fc), obvykle vyjádřený v procentech: FBW = (BW / Fc) * 100 %. Je to bezrozměrná veličina, která udává, jak je systém „širokopásmový“ vzhledem ke své provozní frekvenci. V kontextu 3GPP, zejména od Release 15 pro 5G New Radio (NR), je FBW kriticky důležitý pro specifikaci rádiových požadavků a metrik výkonu, zvláště když sítě využívají vyšší kmitočtová pásma (např. FR2 nad 24,25 GHz), kde šířky kanálů mohou být stovky MHz nebo několik GHz.

Aplikace FBW v rámci specifikací 3GPP řídí definici šířky kanálů pro různá kmitočtová pásma. Pro nižší frekvence (FR1) často stačí definice absolutní šířky pásma. Pro pásma mmWave v FR2 však stejná absolutní šířka pásma představuje mnohem větší FBW, což má významné důsledky pro návrh [RF](/mobilnisite/slovnik/rf/) komponent, jako jsou výkonové zesilovače a filtry, jejichž výkon (např. rovnoměrnost zesílení, účinnost) je často limitován právě FBW. Specifikace (např. 38.104) používají FBW k vymezení požadavků na kmitočtové charakteristiky základnových stanic a uživatelských zařízení.

Z pohledu provozu systému FBW ovlivňuje návrh vlnového tvaru a výběr numerologie. Vysoký FBW může přinášet výzvy, jako je zvýšený fázový šum a větší variace zisku antény v rámci pásma. 3GPP to zohledňuje definováním různých sad požadavků pro úzkopásmová a širokopásmová zařízení na základě jejich FBW. Měřící postupy pro vysílačové a přijímačové testy, jako nežádoucí emise nebo citlivost, jsou také přizpůsobeny na základě FBW konfigurovaného kanálu. Tím je zajištěno, že výkon je hodnocen za realistických podmínek, které odpovídají relativní šířce pásma provozního signálu.

## K čemu slouží

Fractional Bandwidth existuje jako koncept, který poskytuje normalizovanou míru šířky pásma nezávislou na absolutní provozní frekvenci. To je zásadní pro srovnání technických výzev a výkonu systémů pracujících na zcela odlišných kmitočtech nosné. Šířka pásma 100 MHz je považována za širokopásmovou na 2 GHz (FBW=5 %), ale je relativně úzkopásmová na 28 GHz (FBW≈0,36 %). Problémy, které řeší, souvisejí se škálovatelným a konzistentním návrhem rádiového vybavení napříč různorodým spektrem 5G.

Motivace pro jeho formální přijetí ve standardech 3GPP pro 5G pramení ze zavedení spektra mmWave. Předchozí generace mobilních sítí (2G, 3G, 4G) pracovaly primárně v pásmech pod 6 GHz, kde byl FBW obecně nízký a specifikace se mohly opírat o absolutní hodnoty šířky pásma. Rozšíření 5G do FR2 (24,25 GHz až 52,6 GHz a výše) znamenalo, že se standardizovaly šířky kanálů až 400 MHz (a potenciálně 1 GHz). Na těchto frekvencích takové šířky pásma představují významný FBW, což přímo ovlivňuje linearitu [RF](/mobilnisite/slovnik/rf/) front-endu, návrh filtrů a metodiku testování. Definice požadavků na základě FBW zajišťuje, že specifikace rádiového výkonu zůstávají fyzikálně smysluplné a dosažitelné v celém kmitočtovém rozsahu, což umožňuje efektivní a nákladově efektivní vývoj hardwaru jak pro základnové stanice, tak pro zařízení.

## Klíčové vlastnosti

- Bezrozměrný poměr: FBW = Šířka pásma / Střední frekvence
- Kritický pro definici širokopásmového vs. úzkopásmového provozu v RF specifikacích
- Používá se pro stanovení požadavků na RF výkon základnové stanice (BS) a uživatelského zařízení (UE)
- Ovlivňuje testovací modely a měřící postupy pro testy shody
- Klíčový parametr pro návrh systémů mmWave (FR2), kde jsou absolutní šířky pásma velké
- Ovlivňuje návrh RF komponent, jako jsou výkonové zesilovače a filtry

## Související pojmy

- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.115** (Rel-19) — NR Repeater RF Conformance Testing Part 1
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TR 38.877** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [FBW na 3GPP Explorer](https://3gpp-explorer.com/glossary/fbw/)
