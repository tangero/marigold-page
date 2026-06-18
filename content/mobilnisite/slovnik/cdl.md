---
slug: "cdl"
url: "/mobilnisite/slovnik/cdl/"
type: "slovnik"
title: "CDL – Clustered Delay Line"
date: 2025-01-01
abbr: "CDL"
fullName: "Clustered Delay Line"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cdl/"
summary: "CDL je standardizovaný model kanálu pro simulaci šíření rádiového signálu v 5G a dalších generacích. Reprezentuje bezdrátový kanál pomocí shluků vícecestných složek s definovanými zpožděními, úhly a v"
---

CDL je standardizovaný model rádiového kanálu pro 5G, který simuluje šíření rádiového signálu reprezentací bezdrátového prostředí pomocí shluků (clusterů) vícecestných složek s definovanými zpožděními, úhly a výkony.

## Popis

Model Clustered Delay Line (CDL) je statistický model kanálu definovaný ve specifikacích 3GPP pro New Radio (NR). Jedná se o geometrický stochastický model kanálu (GSCM), který matematicky reprezentuje prostředí šíření rádiového signálu mezi vysílačem a přijímačem. Základním principem CDL je modelovat bezdrátový kanál jako soubor diskrétních vícecestných shluků. Každý shluk odpovídá skupině rozptylovačů ve fyzickém prostředí, které způsobují odrazy, ohyby nebo rozptyl rádiového signálu. Shluk je charakterizován sadou parametrů včetně jeho absolutního zpoždění vůči první přijaté cestě, jeho průměrného výkonu a jeho úhlových vlastností (azimutální a zenitové úhly příchodu a odchodu).

V rámci každého shluku model dále definuje určitý počet dílčích cest. Tyto dílčí cesty mají mírné odchylky v zpoždění, úhlu a výkonu vůči centrálním hodnotám shluku, což poskytuje podrobnější a realističtější reprezentaci charakteristik útlumu kanálu. Model generuje časově proměnné impulsní odezvy kanálu aplikací specifických Dopplerových spekter na každý shluk a dílčí cestu, čímž simuluje vliv mobility. Model CDL podporuje jak podmínky s přímou viditelností ([LOS](/mobilnisite/slovnik/los/)), tak bez přímé viditelnosti ([NLOS](/mobilnisite/slovnik/nlos/)), přičemž jsou definovány různé sady parametrů (CDL-A, CDL-B, CDL-C atd.) pro reprezentaci konkrétních prostředí, jako je Urban Macro (UMa), Urban Micro (UMi) a Rural Macro (RMa).

Implementace modelu CDL zahrnuje generování komplexních koeficientů kanálu pro každý anténní prvek, dílčí cestu a shluk, které jsou následně konvoluovány s vysílaným signálem za účelem vytvoření přijímaného signálu. Tento proces zohledňuje parametry velkého rozsahu, jako je útlum na dráze a stínový útlum, stejně jako útlum malého rozsahu způsobený vícecestným šířením. Model je plně definován tabulkami normalizovaných profilů zpoždění a výkonu, úhlových rozptylů a dalších statistických rozdělení, což zajišťuje reprodukovatelnost napříč různými simulacemi a testovacími laboratořemi. Jeho role je zásadní ve vrstvě rádiového přístupového sítě pro hodnocení výkonu, neboť poskytuje společný, dohodnutý referenční rámec pro porovnávání výsledků simulací na úrovni spoje a systému pro zařízení 5G NR, algoritmy formování svazku a [MIMO](/mobilnisite/slovnik/mimo/) techniky v široké škále standardizovaných scénářů.

## K čemu slouží

CDL byl vytvořen, aby řešil kritickou potřebu standardizovaného, přesného a výpočetně efektivního modelu kanálu pro vývoj a ověřování výkonu systémů 5G New Radio. Před 5G se pro 3G a 4G používaly modely kanálů jako modely [ITU-R](/mobilnisite/slovnik/itu-r/) IMT-Advanced nebo dřívější 3GPP Spatial Channel Model ([SCM](/mobilnisite/slovnik/scm/)). Nicméně 5G přineslo nové výzvy včetně použití frekvencí milimetrových vln (mmWave), massive [MIMO](/mobilnisite/slovnik/mimo/) s velkými anténními poli a pokročilých technik formování svazku. Stávající modely byly nedostatečné, protože přesně nezachycovaly jedinečné charakteristiky šíření na vyšších frekvencích, jako je vyšší útlum na dráze, odlišná atmosférická absorpce a zvýšený význam stínování a prostorové konzistence.

Hlavním problémem, který CDL řeší, je poskytnutí společného simulačního rámce, který zajišťuje spravedlivost a srovnatelnost při hodnocení výkonu prováděném různými výrobci, operátory a normalizačními orgány. Bez standardizovaného modelu by každý subjekt mohl používat proprietární nebo mírně odlišné modely, což by znemožnilo objektivní srovnání výkonnostních tvrzení různých řešení 5G. Model CDL spolu se složitějšími modely kanálů Tapped Delay Line ([TDL](/mobilnisite/slovnik/tdl/)) a Integrated Access and Backhaul ([IAB](/mobilnisite/slovnik/iab/)) tvoří hierarchii modelů pro různé testovací účely. Shluková struktura CDL je zvláště vhodná pro hodnocení algoritmů prostorového zpracování a správy svazků, protože explicitně modeluje úhlové charakteristiky vícecestných shluků, což je zásadní pro simulaci systémů založených na svazcích. Jeho vytvoření bylo motivováno požadavkem podporovat celé spektrum případů užití 5G, od rozšířeného mobilního širokopásmového připojení (eMBB) přes hromadnou komunikaci mezi stroji (mMTC) až po ultra-spolehlivou komunikaci s nízkou latencí (URLLC), napříč různými kmitočtovými pásmy od pod 6 GHz až do 100 GHz.

## Klíčové vlastnosti

- Modeluje bezdrátový kanál jako diskrétní shluky vícecestných složek
- Definuje specifické profily zpoždění, výkonu a úhlů pro každý shluk
- Podporuje podmínky šíření jak s přímou viditelností (LOS), tak bez přímé viditelnosti (NLOS)
- Zahrnuje časový vývoj prostřednictvím Dopplerova spektra pro simulaci mobility
- Poskytuje standardizované sady parametrů pro různá prostředí (např. UMa, UMi, RMa)
- Umožňuje reprodukovatelné testování výkonu a srovnávací analýzu zařízení 5G NR

## Definující specifikace

- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [CDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdl/)
