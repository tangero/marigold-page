---
slug: "wqvga"
url: "/mobilnisite/slovnik/wqvga/"
type: "slovnik"
title: "WQVGA – Wide Quarter Video Graphics Array"
date: 2025-01-01
abbr: "WQVGA"
fullName: "Wide Quarter Video Graphics Array"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wqvga/"
summary: "Standardizované rozlišení displeje 400x240 pixelů, primárně definované pro testování mobilních zařízení v rámci 3GPP. Poskytuje konzistentní referenční bod pro hodnocení kvality videotelefonie a multi"
---

WQVGA je standardizované rozlišení displeje 3GPP o 400x240 pixelech používané jako referenční bod pro testování kvality videotelefonie a multimediálních služeb mobilních zařízení.

## Popis

Wide Quarter Video Graphics Array (WQVGA) je specifikace rozlišení displeje standardizovaná organizací 3GPP, konkrétně definovaná jako 400 pixelů na šířku a 240 pixelů na výšku. V rámci ekosystému 3GPP její primární role nespočívá v tom, že by byla povinnou hardwarovou specifikací pro komerční zařízení, ale slouží jako standardizovaný referenční model používaný v testovacích specifikacích. Představuje konzistentní, dobře definovaný video formát pro testování shody a hodnocení výkonu multimediálních služeb, zejména videotelefonie a streamování, napříč různými uživatelskými zařízeními (UE). Specifikace je dokumentována v 3GPP TS 26.938, která popisuje charakteristiky videokodeků a souvisejících multimediálních komponent pro služby s přepojováním okruhů a paketů.

V praktické aplikaci slouží WQVGA jako základní nebo referenční rozlišení při definování testovacích sekvencí a scénářů pro zařízení vyhovující 3GPP. Testovací zařízení a softwarové simulátory používají video streamy ve WQVGA k ověření, že funkce uživatelského zařízení pro kódování videa, dekódování, přenos a vykreslování fungují správně v souladu se standardy. To zahrnuje testování za různých síťových podmínek, jako jsou různé přenosové rychlosti, míry chyb a scénáře předávání spojení. Použitím pevného rozlišení, jako je WQVGA, se výsledky testů stávají reprodukovatelnými a srovnatelnými mezi různými laboratořemi a výrobci zařízení, což je klíčové pro certifikaci a zajištění konzistentního uživatelského zážitku.

Technická implementace zahrnuje generování a zpracování video sekvencí odpovídajících rozlišení WQVGA pomocí kodeků specifikovaných 3GPP, jako jsou H.263, MPEG-4 Visual nebo pozdější kodeky jako H.264/[AVC](/mobilnisite/slovnik/avc/). Testovací rámec vyhodnocuje klíčové ukazatele výkonu, jako je stabilita snímkové frekvence, efektivita kodeku, zpoždění a vizuální kvalita při omezené šířce pásma. Zatímco WQVGA samo o sobě je statický parametr rozlišení, jeho zařazení do standardů zajišťuje, že celý řetězec zpracování multimédií – od vstupu snímače kamery (pokud je relevantní pro testy kódování) až po výstup na displej (pro testy dekódování) – může být ověřen vůči společnému referenčnímu bodu. To je součástí širší strategie 3GPP oddělit testování kvality služeb od rychle se měnících specifikací displejů komerčních zařízení a zaměřit se místo toho na shodu se základními protokoly a kodeky.

## K čemu slouží

Primárním účelem standardizace WQVGA v rámci 3GPP bylo vytvořit stabilní, dobře definovaný referenční bod pro testování výkonu multimédií a ověřování interoperability. Jak se mobilní sítě vyvíjely, aby podporovaly videotelefonii a multimediální zprávy, výrobci začali vyrábět zařízení s širokou škálou rozlišení displejů a poměrů stran. Tato rozmanitost, ačkoliv prospěšná pro trh, vytvořila výzvu pro standardizované testování; použití skutečných rozlišení specifických pro konkrétní zařízení by učinilo výsledky testů nesrovnatelnými a certifikační procesy těžkopádnými.

Definováním konkrétního rozlišení, jako je WQVGA, poskytlo 3GPP společný technický 'jazyk' pro vývoj testovacích případů. To umožňuje výrobcům testovacího zařízení, síťovým operátorům a výrobcům zařízení sladit své postupy testování shody a výkonu. Řeší problém reprodukovatelnosti testů a zajišťuje, že zařízení certifikované jako shodné poskytne základní úroveň kvality video služeb bez ohledu na možnosti svého nativního displeje. Volba WQVGA (400x240) představovala v době jejího zavedení v Release 12 pragmatické střední rozlišení, vhodné pro testování možností sítí 3G a raného 4G, aniž by bylo příliš zatěžující pro zpracování nebo šířku pásma v testovacím prostředí.

Historicky se v dřívějších vydáních 3GPP odkazovalo na jiné běžné formáty, jako [QCIF](/mobilnisite/slovnik/qcif/) nebo [QVGA](/mobilnisite/slovnik/qvga/), pro testování. WQVGA, se svým širším poměrem stran (přibližně 15:9), bylo zavedeno, aby lépe odráželo vyvíjející se formáty mobilních zařízení, která přecházela od spíše čtvercových displejů k širokoúhlým obrazovkám. Tato aktualizace testovacího rámce zajistila, že hodnocení výkonu videokodeků a odolnosti vůči chybám zůstalo relevantní pro současné návrhy zařízení, a řešila tak omezení předchozích testovacích modelů, které nezohledňovaly širší poměry stran běžné u chytrých telefonů a tabletů.

## Klíčové vlastnosti

- Standardizované rozlišení 400 pixelů na šířku a 240 pixelů na výšku
- Definováno jako referenční formát pro testování shody a výkonu
- Používá se pro hodnocení výkonu videokodeků podle specifikací 3GPP
- Poskytuje konzistentní referenční bod pro kvalitu multimediálních služeb
- Podporuje testování interoperability napříč různými implementacemi UE
- Zdokumentováno v technické specifikaci 3GPP TS 26.938

## Související pojmy

- [QVGA – Quarter Video Graphics Array](/mobilnisite/slovnik/qvga/)

## Definující specifikace

- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [WQVGA na 3GPP Explorer](https://3gpp-explorer.com/glossary/wqvga/)
