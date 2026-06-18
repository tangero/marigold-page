---
slug: "psch"
url: "/mobilnisite/slovnik/psch/"
type: "slovnik"
title: "PSCH – Physical Synchronisation Channel"
date: 2025-01-01
abbr: "PSCH"
fullName: "Physical Synchronisation Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/psch/"
summary: "PSCH je downlinkový fyzický kanál v UMTS (3G) používaný pro vyhledávání buněk a počáteční synchronizaci. Vysílá primární a sekundární synchronizační kódy (PSC/SSC), které pomáhají uživatelskému zaříze"
---

PSCH je downlinkový fyzický kanál v UMTS používaný pro vyhledávání buněk a počáteční synchronizaci vysíláním primárních a sekundárních synchronizačních kódů.

## Popis

Fyzický synchronizační kanál (PSCH) je klíčovou součástí rozhraní UMTS ([WCDMA](/mobilnisite/slovnik/wcdma/)), konkrétně v režimu [UTRA](/mobilnisite/slovnik/utra/) [FDD](/mobilnisite/slovnik/fdd/). Jde o výhradně downlinkový, nemodulovaný kanál, který nepřenáší data vyšších vrstev, ale je určen pro počáteční proceduru vyhledávání buňky a synchronizace. PSCH se ve skutečnosti dělí na dva samostatné subkanály: primární synchronizační kanál (P-SCH) a sekundární synchronizační kanál (S-SCH). Ty jsou vysílány paralelně během prvních 256 čipů každého slotu o délce 2560 čipů. P-SCH nese jediný, v rámci celého systému jednotný primární synchronizační kód ([PSC](/mobilnisite/slovnik/psc/)), který je stejný pro každou buňku v síti. Tato společná vlastnost umožňuje uživatelskému zařízení (UE) provést počáteční synchronizaci slotu korelací přijímaného signálu se známým PSC, čímž detekuje začátek každého slotu. Jakmile je získáno časování slotu, UE naslouchá S-SCH. S-SCH vysílá v každém slotu jeden z 16 možných sekundárních synchronizačních kódů ([SSC](/mobilnisite/slovnik/ssc/)). Posloupnost 15 SSC v jednom 10ms rádiovém rámci tvoří jedinečnou sekvenci sekundárních synchronizačních kódů (SSC). Existuje 64 předdefinovaných SSC sekvencí, z nichž každá odpovídá jedné ze 64 skupin skramblovacích kódů používaných v síti. Detekcí vysílané SSC sekvence UE identifikuje skupinu skramblovacích kódů buňky. To drasticky snižuje počet skramblovacích kódů, které musí UE testovat v závěrečném kroku vyhledávání buňky, kdy koreluje společný pilotní kanál ([CPICH](/mobilnisite/slovnik/cpich/)) se skramblovacími kódy v rámci identifikované skupiny, aby našla přesný primární skramblovací kód a dosáhla synchronizace rámce. Konstrukce PSCH s jeho hierarchickou strukturou sekvencí PSC a SSC umožňuje rychlé a robustní vyhledávání buněk i v náročných rádiových podmínkách a představuje základní první krok při jakémkoli připojení UE k síti UMTS.

## K čemu slouží

PSCH byl vytvořen k řešení základního problému počátečního zachycení buňky a synchronizace v asynchronních [CDMA](/mobilnisite/slovnik/cdma/) sítích, jako je UMTS. V dřívějších synchronních systémech, jako je GSM, byla synchronizace jednodušší, protože buňky vysílaly zarovnané časovací signály. V UMTS [WCDMA](/mobilnisite/slovnik/wcdma/) buňky pracují asynchronně, což znamená, že časování každé buňky je nezávislé. Zapnuté UE nemá žádné předchozí znalosti o časování, frekvenci nebo skramblovacím kódu žádné buňky. Účelem PSCH je poskytnout deterministickou, předvídatelnou strukturu signálu, která umožňuje UE efektivně a rychle provést tříkrokovou proceduru vyhledávání buňky: synchronizaci slotu, synchronizaci rámce a identifikaci skupiny kódů a nakonec identifikaci skramblovacího kódu. Bez vyhrazeného, optimalizovaného synchronizačního kanálu, jako je PSCH, by byl proces vyhledávání buňky nepřijatelně pomalý a výpočetně náročný, protože by UE muselo slepě prohledávat všechna možná časování a obrovské množství skramblovacích kódů. Konstrukce PSCH, představená ve verzi 99, poskytla standardizovanou a efektivní metodu pro tuto kritickou proceduru, což umožnilo praktické nasazení a provoz sítí UMTS. Řešila omezení ad-hoc synchronizačních metod a byla nezbytná pro podporu mobility, předávání hovorů a celkovou dostupnost sítě.

## Klíčové vlastnosti

- Vysílá primární synchronizační kód (PSC) pro počáteční získání časování slotu.
- Vysílá sekvence sekundárních synchronizačních kódů (SSC) k identifikaci jedné ze 64 skupin skramblovacích kódů.
- Zabírá prvních 256 čipů každého slotu o délce 2560 čipů.
- Je nemodulovaný kanál, který nese pouze synchronizační kódy.
- Umožňuje tříkrokovou proceduru vyhledávání buňky v UMTS (synchronizace slotu, synchronizace rámce/identifikace skupiny kódů, identifikace skramblovacího kódu).
- Základní pro počáteční přístup UE, výběr buňky a měření pro předávání hovorů.

## Související pojmy

- [CPICH – Common Pilot Channel](/mobilnisite/slovnik/cpich/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 45.820** (Rel-13) — CIoT for Internet of Things

---

📖 **Anglický originál a plná specifikace:** [PSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/psch/)
