---
slug: "uarfcn"
url: "/mobilnisite/slovnik/uarfcn/"
type: "slovnik"
title: "UARFCN – UTRA Absolute Radio Frequency Channel Number"
date: 2025-01-01
abbr: "UARFCN"
fullName: "UTRA Absolute Radio Frequency Channel Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/uarfcn/"
summary: "Číselný identifikátor, který jednoznačně určuje kmitočet nosné v systému UTRA (UMTS Terrestrial Radio Access), používaný pro režimy FDD i TDD. Poskytuje standardizovaný způsob odkazování na rádiové ka"
---

UARFCN je číselný identifikátor, který jednoznačně určuje kmitočet nosné v systému UTRA, používaný pro režimy FDD i TDD v sítích UMTS.

## Popis

[UTRA](/mobilnisite/slovnik/utra/) Absolute Radio Frequency Channel Number (UARFCN) je základní parametr v sítích UMTS (3G), který definuje střední kmitočet rádiové nosné. Jedná se o celočíselnou hodnotu, která se podle vzorců definovaných ve specifikacích 3GPP mapuje na konkrétní kmitočet v MHz. Použití čísla kanálu namísto přímé hodnoty kmitočtu zjednodušuje konfiguraci sítě, implementaci UE a hlášení měření. Pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)) jsou přiřazeny samostatné hodnoty UARFCN pro nosnou uplink ([UL](/mobilnisite/slovnik/ul/)) a downlink ([DL](/mobilnisite/slovnik/dl/)), které jsou spárovány s pevným duplexním odstupem. Pro režim Time Division Duplex ([TDD](/mobilnisite/slovnik/tdd/)) definuje jediná hodnota UARFCN kmitočet nosné používaný pro oba směry přenosu.

Výpočet skutečného kmitočtu z UARFCN (N) se řídí vzorcem: F (MHz) = F_Offset + (N * Channel_Spacing). Hodnoty pro F_Offset a Channel_Spacing se liší mezi provozními pásmy a duplexními režimy. Například v hlavním pásmu UMTS Band I (2100 MHz FDD) používá výpočet UARFCN pro downlink F_Offset = 0 MHz a krok 0,2 MHz, takže UARFCN N=10562 odpovídá 2112,4 MHz. Toto systematické mapování umožňuje jednoznačně adresovat každou možnou nosnou v definovaném rozsahu pásma. UARFCN se hojně používá v blocích systémových informací ([SIB](/mobilnisite/slovnik/sib/)) vysílaných Node B, které informují UE o kmitočtech obslužné a sousedních buněk, v řídicích zprávách měření od [RNC](/mobilnisite/slovnik/rnc/) a v hlášeních měření odesílaných UE.

Jeho role přesahuje pouhou identifikaci. UARFCN je klíčový pro výběr a převýběr buňky, procedury předávání hovoru (handover) a plánování sítě. Hlášením naměřené kvality signálu (např. [CPICH](/mobilnisite/slovnik/cpich/) RSCP, Ec/No) vůči konkrétnímu UARFCN poskytuje UE síti jasný obraz o rádiovém prostředí. RNC tyto informace využívá k rozhodování o mobilitě. Koncept ARFCN byl později rozšířen na E-UTRA s EARFCN pro LTE a NR-ARFCN pro 5G NR, přičemž zachovává stejný princip číslování kanálů, ale s odlišnými vzorci a rozsahy, aby pokryl nová spektra a širší šířky kanálů.

## K čemu slouží

UARFCN byl vytvořen, aby poskytl standardizovanou, jednoznačnou metodu pro identifikaci kmitočtů nosných v systému UTRA, která nahradila potřebu používat v signalizaci a konfiguraci přímé hodnoty kmitočtů. V raných buňkových systémech sice čísla kanálů existovala, ale rychlá expanze kmitočtových pásem a zavedení širokopásmového CDMA s UMTS si vyžádaly flexibilnější a škálovatelnější číslovací schéma. Používání přímých hodnot kmitočtů ve zprávách by bylo neefektivní, náchylné k chybám a neelegantně by zvládalo různorodost globálních kmitočtových pásem s různými duplexními odstupymi a posuny.

Hlavním problémem, který UARFCN řeší, je zajištění interoperability a jednotného odkazu na kmitočet napříč všemi síťovými zařízeními a uživatelskými terminály, bez ohledu na výrobce nebo konkrétní používané kmitočtové pásmo. Abstrahuje fyzický kmitočet, což umožňuje protokolům a procedurám vyšších vrstev pracovat s jednoduchými celočíselnými hodnotami. To zjednodušuje implementaci UE pro globální roaming, protože zařízení potřebuje znát pouze mapovací vzorce UARFCN na kmitočet pro podporovaná pásma. Pro síťové operátory zefektivňuje plánování kmitočtů, konfiguraci seznamů sousedních buněk a analýzu testů pokrytí. Vytvoření UARFCN spolu s podrobnými specifikacemi pásem bylo klíčovým předpokladem pro globální nasazení UMTS, neboť poskytlo jasný a efektivní společný jazyk pro rádiovou vrstvu, který byl převzat i všemi následujícími rádiovými přístupovými technologiemi 3GPP.

## Klíčové vlastnosti

- Jednoznačný celočíselný identifikátor pro kmitočet nosné UTRA
- Samostatné číslování pro UL a DL v režimu FDD; jediné číslo pro TDD
- Definován vzorcem: Kmitočet = Posun + (N * Velikost kroku)
- Používá se ve vysílání systémových informací a v řízení měření RRC
- Základní prvek pro vyhledávání buněk, hlášení měření a předávání hovoru (handover)
- Poskytuje na pásmu nezávislý referenční bod pro signalizační protokoly

## Související pojmy

- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)
- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)
- [NR-ARFCN – NR Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/nr-arfcn/)
- [UTRA – Universal Terrestrial Radio Access](/mobilnisite/slovnik/utra/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 34.124** (Rel-19) — EMC Requirements for 3G UTRA Terminals
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [UARFCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/uarfcn/)
