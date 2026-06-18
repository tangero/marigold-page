---
slug: "pdfi"
url: "/mobilnisite/slovnik/pdfi/"
type: "slovnik"
title: "PDFI – Potentially Degraded Frame Indication"
date: 2025-01-01
abbr: "PDFI"
fullName: "Potentially Degraded Frame Indication"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/pdfi/"
summary: "Mechanismus v adaptivním vícekanálovém (AMR) kodeku 3GPP pro signalizaci, že přijatý řečový rámec může mít degradovanou kvalitu kvůli přenosovým chybám. Umožňuje přijímači aplikovat techniky skrytí ch"
---

PDFI je mechanismus v kodeku AMR, který signalizuje potenciálně degradovaný řečový rámec kvůli přenosovým chybám, což umožňuje skrytí chyb pro zlepšení vnímané kvality hlasu.

## Popis

Indikace potenciálně degradovaného rámce (PDFI) je řídicí mechanismus zabudovaný do rámce adaptivního vícekanálového ([AMR](/mobilnisite/slovnik/amr/)) řečového kodeku, standardizovaný v 3GPP TS 26.091. Funguje na rozhraní mezi fyzickou vrstvou a řečovým kodekem. Když je řečový rámec přijat přes rozhraní vzdušného přenosu, fyzická vrstva provede detekci chyb, obvykle pomocí cyklického redundantního součtu ([CRC](/mobilnisite/slovnik/crc/)). Pokud CRC indikuje, že rámec obsahuje bitové chyby, ale je stále dekódovatelný ('špatný' rámec), předá fyzická vrstva rámec řečovému dekodéru spolu s příznakem PDFI nastaveným na 'pravda'. Tento příznak je binární indikátor, že datová část rámce je 'potenciálně degradovaná' a neměla by být plně důvěryhodná.

Při přijetí rámce s nastaveným PDFI přechází dekodér AMR do specifického stavu skrytí chyb. Dekodér rámec nevyřazuje úplně, ale používá jeho obsah obezřetně. Používá algoritmy pro maskování degradace, jako je zeslabení energie syntetizované řeči nebo prolínání přijatých parametrů s extrapolovanými parametry z předchozích dobrých rámců. Základním principem je vyhnout se náhlým změnám ve zvukovém výstupu, které způsobují slyšitelné kliknutí nebo zkreslení, a poskytnout tak plynulejší a přirozenější degradaci kvality hlasu. Je spuštěna interní rutina dekodéru pro zpracování špatných rámců ([BFH](/mobilnisite/slovnik/bfh/)), která spravuje interpolaci řečových parametrů a postupné ztlumení výstupu, pokud jsou přijaty po sobě jdoucí degradované rámce.

PDFI se liší od 'indikace vymazání rámce' (FEI), kdy je rámec považován za zcela ztracený. PDFI se zabývá 'šedou zónou' poškozených, ale použitelných dat. Jeho implementace je klíčová pro robustnost kodeku AMR, zejména v systémech GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) a UMTS, kde se podmínky kanálu mohou rychle měnit. Mechanismus je úzce integrován s funkcemi adaptace rychlosti a generování komfortního šumu kodeku AMR a tvoří tak komplexní sadu pro udržení kvality hlasové služby za všech síťových podmínek. Jeho specifikace zajišťuje interoperabilitu mezi síťovým zařízením a uživatelskými zařízeními od různých výrobců.

## K čemu slouží

PDFI bylo vytvořeno k řešení specifické výzvy zpracování částečně poškozených řečových rámců v digitálních buněčných systémech. V raných digitálních hlasových systémech se často používal jednoduchý přístup vyhovuje/nevyhovuje (dobrý rámec/špatný rámec). Radiové kanály jsou však náchylné k bitovým chybám a vyřazení každého rámce s [CRC](/mobilnisite/slovnik/crc/) chybou by mohlo vést k nadměrné ztrátě rámců a vážnému přerušování hlasu, zejména během útlumů. Naopak bezmyšlenkovité použití všech přijatých bitů by mohlo vstřiknout významný šum do zvukového proudu, pokud by chyby ovlivnily kritické parametry kodeku.

Účelem PDFI je poskytnout jemně odstíněný střední přístup. Umožňuje fyzické vrstvě informovat řečový dekodér, že rámec obsahuje chyby, ale není zcela neobnovitelný. To umožňuje chytřejší skrytí chyb. Historická motivace vychází z vývoje kodeku [AMR](/mobilnisite/slovnik/amr/) pro GSM a jeho evoluce do 3G/UMTS, kde bylo klíčovým konkurenčním faktorem maximalizování kvality hlasu a kapacity v různých rádiových podmínkách. PDFI jako součást specifikací AMR vyřešilo problém, jak elegantně degradovat kvalitu hlasu při mezních podmínkách signálu, a zlepšilo tak vnímaný zážitek koncového uživatele ve srovnání se systémy, které měly pouze binární indikátory dobrého/špatného rámce.

## Klíčové vlastnosti

- Signalizuje potenciální degradaci kvality v přijatém řečovém rámci
- Umožňuje aplikaci pokročilých algoritmů skrytí chyb v dekodéru AMR
- Funguje ve spojení s detekcí chyb CRC na fyzické vrstvě
- Rozlišuje mezi potenciálně degradovanými rámci a zcela vymazanými rámci
- Zlepšuje vnímanou kvalitu hlasu při občasných chybách rádiového spoje
- Standardizováno jako součást kodeku AMR pro zajištění interoperability mezi výrobci

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)

## Definující specifikace

- **TS 26.091** (Rel-19) — AMR Error Concealment Procedure

---

📖 **Anglický originál a plná specifikace:** [PDFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdfi/)
