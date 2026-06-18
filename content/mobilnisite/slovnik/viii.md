---
slug: "viii"
url: "/mobilnisite/slovnik/viii/"
type: "slovnik"
title: "VIII – UTRA Absolute Radio Frequency Channel Number (UARFCN) for Band VIII"
date: 2025-01-01
abbr: "VIII"
fullName: "UTRA Absolute Radio Frequency Channel Number (UARFCN) for Band VIII"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/viii/"
summary: "VIII je identifikátor absolutního čísla rádiového kanálu UTRA (UARFCN) pro pásmo UMTS VIII (900 MHz). Reprezentuje konkrétní rozsah kmitočtů pro uplink 880–915 MHz používaný v tomto pásmu. Toto číslov"
---

VIII je identifikátor absolutního čísla rádiového kanálu UTRA (UARFCN) pro pásmo UMTS VIII, který reprezentuje rozsah kmitočtů pro uplink 880–915 MHz používaný v převedeném spektru GSM 900 MHz.

## Popis

VIII označuje označení absolutního čísla rádiového kanálu [UTRA](/mobilnisite/slovnik/utra/) ([UARFCN](/mobilnisite/slovnik/uarfcn/)) pro pásmo UMTS VIII, které pracuje v kmitočtovém rozsahu 900 MHz. Na rozdíl od pásma [VII](/mobilnisite/slovnik/vii/), které používá vzorec, se 'VIII' v tomto kontextu typicky vztahuje k samotnému pásmu a jeho přidruženému rozsahu UARFCN. Rozsah kmitočtů pro uplink pásma VIII je 880–915 MHz a odpovídající downlink je 925–960 MHz. Každému konkrétnímu kmitočtu nosné v tomto rozsahu je přiřazeno jedinečné celé číslo UARFCN. UARFCN pro pásmo VIII se vypočítává pomocí standardního vzorce definovaného pro toto pásmo, podobně jako u jiných pásem UTRA, který mapuje fyzickou hodnotu v MHz na číslo kanálu.

Systém UARFCN pro pásmo VIII je implementován v softwaru UE a Node B (základnové stanice). Když síť vysílá systémové informace, zahrnuje UARFCN obsluhované buňky. UE, která prohledává sítě, používá toto číslování k naladění svého přijímače na správný kmitočet. Pro pásmo VIII nabízí relativně nízký kmitočet ve srovnání s vyššími pásmy, jako je 2100 MHz, lepší vlastnosti šíření, což vede k lepšímu pokrytí a průniku do budov. To jej činí velmi cenným pro širokoplošné pokrytí UMTS/[HSPA](/mobilnisite/slovnik/hspa/), často prostřednictvím převodu stávajícího spektra GSM.

Technické specifikace, zejména TS 25.141, definují požadavky a testovací případy pro základnové stanice pracující v pásmu VIII, včetně přesného generování kmitočtů odpovídajících správným UARFCN. Síťoví operátoři používají plán UARFCN k přidělení konkrétních čísel kanálů různým buňkám, čímž zajišťují strukturovanou a rušení řízenou rádiovou síť. Použití pásma VIII bylo klíčové pro vývoj sítí 3G, protože umožnilo využít výhody pokrytí nízkokmitočtového spektra původně přiděleného pro služby 2G.

## K čemu slouží

Účelem pásma VIII a jeho přidruženého schématu [UARFCN](/mobilnisite/slovnik/uarfcn/) bylo umožnit nasazení technologie UMTS (a později [HSPA](/mobilnisite/slovnik/hspa/)) v kmitočtovém pásmu 900 MHz. Toto pásmo bylo historicky používáno pro sítě GSM po celém světě a nabízelo vynikající pokrytí a průnik. Vzhledem k tomu, že služby 3G vyžadovaly širší pokrytí a efektivnější využití spektra, regulační orgány v mnoha regionech umožnily převod částí pásma 900 MHz pro UMTS.

Tím se řešilo klíčové omezení raných nasazení 3G, která primárně používala pásmo 2100 MHz (pásmo I). Zatímco 2100 MHz poskytovalo dostatečnou šířku pásma, jeho dosah byl menší, což vyžadovalo více buněčných stanic pro ekvivalentní geografické pokrytí, což zvyšovalo kapitálové výdaje. Nasazení UMTS v pásmu VIII umožnilo operátorům poskytovat služby 3G na větších plochách s menším počtem stanovišť, což výrazně zlepšilo dostupnost služeb v předměstských a venkovských oblastech. Také usnadnilo plynulejší migrační cesty z 2G na 3G tím, že umožnilo sdílené využití stávajících anténních systémů a infrastruktury stanovišť.

Standardizovaný UARFCN pro pásmo VIII zajišťoval, že UE a síťová zařízení od různých dodavatelů mohou na tomto převedeném spektru bezproblémově spolupracovat. Poskytoval jasnou a jednoznačnou metodu pro identifikaci nosných 900 MHz v rámci protokolového zásobníku UMTS, podporující kritické funkce jako předávání mezi pásmy (např. z 2100 MHz na 900 MHz pro rozšíření pokrytí) a agregaci nosných v pozdějších vylepšeních HSPA+. Jednalo se o strategický vývoj, který prodloužil ekonomickou životnost a schopnost pokrytí sítí 3G.

## Klíčové vlastnosti

- Reprezentuje pásmo UMTS VIII pracující v rozsahu uplink 880–915 MHz / downlink 925–960 MHz.
- Využívá schéma číslování kanálů UTRA UARFCN pro identifikaci nosné.
- Umožňuje nasazení UMTS/HSPA v převedeném spektru GSM 900 MHz.
- Poskytuje lepší pokrytí a průnik do budov ve srovnání s vyššími pásmy 3G.
- Nezbytné pro procedury předávání mezi pásmy a správy mobility.
- Specifikováno v 3GPP TS 25.141 pro shodu základnových stanic v tomto pásmu.

## Související pojmy

- [UARFCN – UTRA Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/uarfcn/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [VIII na 3GPP Explorer](https://3gpp-explorer.com/glossary/viii/)
