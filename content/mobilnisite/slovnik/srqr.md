---
slug: "srqr"
url: "/mobilnisite/slovnik/srqr/"
type: "slovnik"
title: "SRQR – Spherical Region-wise Quality Ranking"
date: 2025-01-01
abbr: "SRQR"
fullName: "Spherical Region-wise Quality Ranking"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/srqr/"
summary: "SRQR je standardizovaná metrika definovaná 3GPP pro hodnocení vizuální kvality imerzivních médií, jako je 360stupňové video. Kvalitu posuzuje rozdělením sférického videa na regiony a jejich seřazením"
---

SRQR je standardizovaná metrika 3GPP pro hodnocení kvality imerzivních médií, která rozděluje sférické video na regiony a řadí je na základě jejich důležitosti závislé na výřezu (viewportu).

## Popis

Spherical Region-wise Quality Ranking (SRQR) je metodologie hodnocení kvality standardizovaná v 3GPP Technical Specification 26.118 pro služby imerzivních médií. Je navržena speciálně pro všesměrový (360stupňový) videoobsah, který je promítán na sféru, z níž uživatel vybírá výřez (omezené zorné pole) ke sledování. Na rozdíl od tradičních metrik kvality 2D videa, které hodnotí celý snímek jednotně, SRQR uznává, že různé regiony sférického videa mají různou percepční důležitost v závislosti na aktuálním a potenciálním budoucím pohledu uživatele.

Metodologie funguje tak, že nejprve rozdělí sférický povrch na sadu nepřekrývajících se regionů, typicky definovaných standardizovaným schématem dlaždic (např. na základě segmentace ekvirektangulární projekce). Pro každý z těchto prostorových regionů je vypočítáno nebo přiřazeno skóre pořadí kvality. Toto pořadí odráží relativní vizuální kvalitu daného regionu ve srovnání s ostatními ve stejné mediální prezentaci. Pořadí může být založeno na objektivních metrikách (jako [PSNR](/mobilnisite/slovnik/psnr/), [SSIM](/mobilnisite/slovnik/ssim/) aplikované na region), výsledcích subjektivního testování nebo jejich kombinaci. Výstupem je mapa kvality nebo datová struktura, která spojuje každý prostorový region s pořadím.

SRQR funguje ve dvou hlavních režimech: v režimu tvorby obsahu, kde jsou generována pořadí kvality a vkládána jako metadata do mediálního souboru (např. do stopy [ISOBMFF](/mobilnisite/slovnik/isobmff/)), a v režimu spotřeby, kde tato pořadí používá klient nebo síťový prvek. Během streamování mohou tato metadata řídit strategie adaptivního streamování podle výřezu. Streamovací server nebo klient může upřednostnit doručování dat vysoké kvality pro regiony, které jsou aktuálně ve výřezu nebo se předpokládá, že do něj vstoupí, zatímco může potenciálně snížit kvalitu pro regiony mimo výřez za účelem úspory šířky pásma. To umožňuje efektivní využití síťových zdrojů při maximalizaci vnímané kvality pro uživatele.

## K čemu slouží

SRQR bylo vytvořeno, aby řešilo jedinečné výzvy streamování imerzivního 360stupňového videa, které generuje obrovská množství dat (často v rozlišení 4K-8K nebo vyšším). Streamování celého sférického videa s jednotně vysokou kvalitou je neúměrně náročné na šířku pásma. Klíčovým poznatkem je, že uživatel v daném okamžiku sleduje pouze část (typicky 90x90 stupňů). Předchozí metriky kvality videa (např. [MOS](/mobilnisite/slovnik/mos/), [PSNR](/mobilnisite/slovnik/psnr/) pro celý snímek) byly nedostatečné, protože nezohledňovaly toto vnímání závislé na výřezu.

Technologie byla motivována vzestupem služeb virtuální reality ([VR](/mobilnisite/slovnik/vr/)) a rozšířené reality v éře 5G, kde 3GPP usilovalo o standardizaci efektivních mechanismů doručování. Řeší problém, jak objektivně popsat, porovnat a optimalizovat kvalitu takového obsahu způsobem, který odpovídá lidskému vnímání. Poskytnutím standardizovaného regionálního pořadí umožňuje interoperabilitu mezi tvůrci obsahu, poskytovateli sítí a klientskými zařízeními pro streamování s ohledem na kvalitu.

Odstraňuje omezení nestandardizovaných proprietárních metod adaptivního streamování pro VR. SRQR poskytuje společný jazyk pro kvalitu, usnadňuje funkce jako síťově asistované streamování (kde 5G Core může být informováno o důležitých regionech) a reportování kvality zážitku ([QoE](/mobilnisite/slovnik/qoe/)). Jeho zavedení ve verzi 15 bylo součástí širší pracovní položky 3GPP o imerzivních médiích s cílem zajistit, aby vysoce kvalitní zážitky VR/[AR](/mobilnisite/slovnik/ar/) mohly být prakticky doručovány přes mobilní sítě.

## Klíčové vlastnosti

- Definuje standardizovanou metodologii pro rozdělení sférického videa na regiony pro hodnocení kvality
- Přiřazuje relativní pořadí kvality každému prostorovému regionu imerzivního obsahu
- Podporuje jak objektivní výpočet, tak subjektivní odvození pořadí kvality regionů
- Umožňuje generování a ukládání metadat pořadí kvality uvnitř mediálních souborů (např. ISOBMFF)
- Usnadňuje strategie adaptivního streamování podle výřezu identifikací regionů s vysokou prioritou
- Poskytuje základ pro měření a reportování QoE specifické pro služby 360stupňového videa

## Související pojmy

- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)
- [ISOBMFF – International Organization for Standards, Base Media File Format](/mobilnisite/slovnik/isobmff/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats

---

📖 **Anglický originál a plná specifikace:** [SRQR na 3GPP Explorer](https://3gpp-explorer.com/glossary/srqr/)
