---
slug: "ocng"
url: "/mobilnisite/slovnik/ocng/"
type: "slovnik"
title: "OCNG – OFDMA Channel Noise Generator"
date: 2025-01-01
abbr: "OCNG"
fullName: "OFDMA Channel Noise Generator"
category: "Physical Layer"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ocng/"
summary: "OFDMA Channel Noise Generator (OCNG) je testovací a měřicí nástroj definovaný v 3GPP pro LTE a NR. Používá se k zaplnění nevyužitých resource elementů v downlinkovém přenosu pseudonáhodným šumem, čímž"
---

OCNG je testovací nástroj 3GPP pro LTE/NR, který zaplňuje nevyužité resource elementy v downlinku pseudonáhodným šumem, aby vytvořil konzistentní úroveň interference pro testování výkonu přijímače.

## Popis

[OFDMA](/mobilnisite/slovnik/ofdma/) Channel Noise Generator (OCNG) je klíčová součást specifikací pro testování shody přijímačů uživatelských zařízení (UE) pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). Jeho hlavní funkcí je vytvořit řízené a reprodukovatelné interferenční prostředí v downlinku. V reálném provozu sítě přijímá UE požadované signály na specifických resource blocích, zatímco jiné resource bloky přenášejí data pro jiné uživatele nebo zůstávají prázdné, což vede k proměnlivé úrovni šumu. Pro standardizované testování výkonu je tato variabilita nežádoucí. OCNG tento problém řeší tak, že zaplní všechny resource elementy (RE) v downlinkovém subrámci, které nejsou alokovány pro požadovaný signál testovaného UE, pseudonáhodnými QPSK modulovanými symboly. Tyto symboly jsou generovány pomocí definovaného algoritmu a sekvence, takže se přijímači jeví jako aditivní bílý Gaussovský šum ([AWGN](/mobilnisite/slovnik/awgn/)). Tím vzniká rovnoměrná a známá spektrální hustota výkonu v celém šířce pásma kanálu. Testovací uspořádání zahrnuje simulátor základnové stanice vysílající požadovaný referenční měřicí kanál (např. [PDSCH](/mobilnisite/slovnik/pdsch/)) k UE. Současně je aktivován OCNG, aby zaplnil nevyužité časově-frekvenční zdroje. UE pak musí pod touto řízenou úrovní šumu a interference správně dekódovat požadovaný signál. Měří se klíčové výkonnostní metriky jako propustnost, bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)) a referenční úroveň výkonu citlivosti. Vlastnosti OCNG, jako je jeho výkonová úroveň vůči požadovanému signálu, jsou striktně definovány v testovacích specifikacích jako TS 36.101 (LTE) a TS 38.101 (NR). To zajišťuje, že všechna UE jsou testována proti stejnému interferenčnímu modelu, což umožňuje spravedlivé a srovnatelné hodnocení kvality přijímače napříč různými výrobci a modely zařízení.

## K čemu slouží

OCNG byl vytvořen za účelem stanovení přísné, standardizované a opakovatelné metodologie pro testování výkonu fyzické vrstvy přijímačů založených na [OFDMA](/mobilnisite/slovnik/ofdma/) v LTE a NR. Před jeho definicí mohlo být testování přijímačů nekonzistentní, protože 'úroveň šumu', kterou UE zažívala, závisela na nepředvídatelných faktorech, jako je počet nevyužitých resource bloků v testovacím přenosu. To ztěžovalo objektivní srovnání citlivosti a propustnosti různých implementací UE. OCNG tento problém řeší tím, že uměle vytváří scénář nejhoršího případu plného zatížení interference, který napodobuje plně vytíženou buňku, kde jsou všechny zdroje nevyužité testovaným UE obsazeny interferencí od ostatních uživatelů. Tím poskytuje konzistentní a náročnou testovací podmínku, která prověřuje schopnost UE oddělit požadovaný signál od šumu a interference. Jeho zavedení v LTE Release 8 bylo motivováno potřebou robustních výkonnostních požadavků pro nový OFDMA downlink, aby bylo zajištěno, že UE mohou spolehlivě fungovat na okraji buňky nebo v prostředí s vysokou interferencí. Je to základní nástroj pro ověření, že přijímače UE splňují minimální výkonnostní charakteristiky požadované 3GPP, což přímo ovlivňuje pokrytí sítě, její kapacitu a uživatelský zážitek.

## Klíčové vlastnosti

- Generuje pseudonáhodné QPSK symboly k zaplnění nevyužitých resource elementů v downlinku
- Vytváří řízenou a rovnoměrnou úroveň šumu a interference pro testování
- Používá standardizované algoritmy k zajištění reprodukovatelných testovacích podmínek globálně
- Nezbytný pro definici testů referenční citlivosti UE a maximální propustnosti
- Konfigurovatelná úroveň výkonu pro nastavení specifických poměrů nosná/interference (C/I)
- Použitelný pro testování shody jak pro LTE (E-UTRA), tak pro NR (New Radio)

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [AWGN – Additive White Gaussian Noise](/mobilnisite/slovnik/awgn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec
- **TR 38.922** (Rel-19) — Study on IMT Parameters for NR in Higher Bands

---

📖 **Anglický originál a plná specifikace:** [OCNG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ocng/)
