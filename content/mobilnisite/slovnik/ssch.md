---
slug: "ssch"
url: "/mobilnisite/slovnik/ssch/"
type: "slovnik"
title: "SSCH – Secondary Synchronisation Channel"
date: 2025-01-01
abbr: "SSCH"
fullName: "Secondary Synchronisation Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ssch/"
summary: "Fyzický kanál v UMTS (3G) používaný pro vyhledávání buňky a synchronizaci. Vysílá sekvenci sekundárního synchronizačního kódu (SSC), která v kombinaci s primárním SCH umožňuje UE identifikovat skupinu"
---

SSCH je fyzický kanál UMTS, který vysílá sekundární synchronizační kód a umožňuje UE identifikovat skupinu skramblovacích kódů buňky a časování rámce během vyhledávání buňky.

## Popis

Sekundární synchronizační kanál (SSCH) je klíčovou součástí rozhraní UMTS (Universal Mobile Telecommunications System) [WCDMA](/mobilnisite/slovnik/wcdma/) (Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)), jak je definováno ve specifikacích 3GPP. Funguje ve spojení s primárním synchronizačním kanálem (P-SCH) a umožňuje uživatelskému zařízení (UE) provádět vyhledávání buňky a dosáhnout synchronizace s Node B (základnovou stanicí). SSCH je výhradně downlinkový fyzický kanál, který je vysílán současně s P-SCH během specifických časových slotů.

Technicky SSCH vysílá sekvenci známou jako sekundární synchronizační kód ([SSC](/mobilnisite/slovnik/ssc/)). Na rozdíl od jediného pevného kódu používaného na P-SCH existuje 16 možných SSC. Těchto 16 kódů se nepoužívá jednotlivě, ale je uspořádáno do 64 unikátních sekvencí po 15 SSC, přičemž každá sekvence odpovídá jedné ze 64 skupin skramblovacích kódů používaných v systému. Sekvence se opakuje každých 10 ms rádiového rámce. UE po prvotní detekci P-SCH pro dosažení slotové synchronizace koreluje s možnými sekvencemi SSC na SSCH. Identifikací konkrétní přijaté 15-SSC sekvence UE určí skupinu skramblovacích kódů (což zúží vyhledávání z 512 možných primárních skramblovacích kódů na pouhých 8) a, což je klíčové, dosáhne synchronizace rámce identifikací začátku 10 ms rámce.

Jakmile je známa skupina skramblovacích kódů a časování rámce, UE přistoupí k závěrečné fázi vyhledávání buňky, ve které provádí korelaci s 8 možnými primárními skramblovacími kódy v rámci identifikované skupiny na společném pilotním kanálu ([CPICH](/mobilnisite/slovnik/cpich/)), aby našla přesný primární skramblovací kód buňky. Konstrukce SSCH, využívající pečlivě vybranou sadu ortogonálních sekvencí, zajišťuje spolehlivou detekci i v náročných rádiových podmínkách. Jeho funkce je základní, nízkourovňovou procedurou, která podmiňuje veškerý síťový přístup vyšších vrstev, mobilitu a konektivitu v sítích UMTS, což UE umožňuje přihlásit se k buňce a zahájit komunikaci.

## K čemu slouží

SSCH byl vytvořen k řešení kritického problému počátečního zachycení buňky a synchronizace v asynchronních [CDMA](/mobilnisite/slovnik/cdma/) sítích, jako je UMTS. V takových sítích nejsou základnové stanice vzájemně časově synchronizovány, na rozdíl od synchronních systémů jako GSM. Uživatelské zařízení při zapnutí tedy nemá žádnou předchozí znalost o časování ani o konkrétních kódech používaných okolními buňkami. Účelem dvoustupňového návrhu [SCH](/mobilnisite/slovnik/sch/) (P-SCH a S-SCH) je efektivně provést UE tímto vyhledáváním.

P-SCH poskytuje jednoduchý, všeobecně známý signál pro hrubé časování slotů. SSCH na to navazuje tím, že přenáší dva klíčové informační prvky: skupinu skramblovacích kódů a hranici rámce. Přenos skupiny skramblovacích kódů drasticky snižuje složitost finálního vyhledávání kódu. Identifikace časování rámce je zásadní, protože všechny systémové informace vyšších vrstev jsou vysílány ve strukturovaných rámcích; bez znalosti začátku rámce je UE nemůže dekódovat. Konstrukce sekvencí SSCH také poskytuje určitou odolnost vůči chybě frekvence. Před UMTS existovala jednodušší synchronizační schémata, ale asynchronní povaha a širší šířka pásma [WCDMA](/mobilnisite/slovnik/wcdma/) si vyžádaly tento sofistikovanější, hierarchický přístup, aby bylo zajištěno rychlé a spolehlivé vyhledávání buňky, což je klíčové pro zkrácení doby navazování hovoru a pro plynulou mobilitu.

## Klíčové vlastnosti

- Vysílá sekvenci 15 sekundárních synchronizačních kódů (SSC) na 10 ms rádiový rámec
- Identifikuje jednu z 64 možných skupin skramblovacích kódů, čímž zužuje vyhledávání primárního skramblovacího kódu
- Poskytuje synchronizaci rámce tím, že označuje začátek rádiového rámce
- Pro SSC používá ortogonální kódy s proměnným rozprostřením (OVSF)
- Je vždy vysílán současně s primárním synchronizačním kanálem (P-SCH)
- Základní pro druhý krok třístupňové procedury vyhledávání buňky v UMTS

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [SSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssch/)
