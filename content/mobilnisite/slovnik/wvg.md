---
slug: "wvg"
url: "/mobilnisite/slovnik/wvg/"
type: "slovnik"
title: "WVG – Wireless Vector Graphics"
date: 2025-01-01
abbr: "WVG"
fullName: "Wireless Vector Graphics"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wvg/"
summary: "Specifikace 3GPP definující standardizovaný formát pro vektorovou grafiku (jako obrázky, animace a prvky uživatelského rozhraní) optimalizovaný pro přenos a vykreslování na mobilních zařízeních. Umožň"
---

WVG je specifikace 3GPP definující standardizovaný formát pro vektorovou grafiku optimalizovaný pro přenos a vykreslování na mobilních zařízeních přes buňkové sítě s omezenou přenosovou kapacitou.

## Popis

Wireless Vector Graphics (WVG) je standard 3GPP (TS 29.311), který definuje kompaktní binární formát pro reprezentaci dvourozměrné vektorové grafiky a základních animací. Na rozdíl od rastrových obrázků (např. [JPEG](/mobilnisite/slovnik/jpeg/), [PNG](/mobilnisite/slovnik/png/)), které popisují obraz jako mřížku pixelů, vektorová grafika popisuje tvary (čáry, křivky, polygony, text) pomocí matematických rovnic a atributů (barva výplně, šířka obrysu). To umožňuje WVG obrázkům škálování na libovolnou velikost bez ztráty kvality a typicky vede k výrazně menší velikosti souborů pro grafický obsah jako ikony, mapy, grafy a jednoduché animace. Specifikace podrobně popisuje syntaxi a sémantiku formátu souboru WVG, včetně jeho binárního kódování pro efektivní parsování, a odpovídající textové reprezentace založené na [XML](/mobilnisite/slovnik/xml/) pro tvorbu a výměnu.

Architektonicky je WVG technologií prezentační vrstvy. Soubor WVG je vytvořen poskytovatelem obsahu nebo aplikačním serverem a doručen do UE přes síť pomocí mechanismů jako Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)), [HTTP](/mobilnisite/slovnik/http/) nebo broadcast. UE obsahuje vykreslovací engine WVG (softwarovou komponentu často součástí multimediálního frameworku zařízení), který interpretuje příkazy WVG, zpracovává případné vestavěné skriptování (jako ECMAScript pro základní interaktivitu nebo animaci) a vykresluje grafiku na displej zařízení. Formát podporuje statickou grafiku, časované animace a uživatelem interaktivní grafiku. Mezi klíčové komponenty popsané ve specifikaci patří struktura scény (hierarchie grafických objektů), sada kreslicích primitiv, atributy stylu a animační elementy, které definují, jak se vlastnosti mění v čase.

Jeho úlohou v síti je umožnění služeb rich media. Poskytnutím standardizovaného, efektivního formátu pro grafiku umožňuje poskytovatelům služeb vytvářet vizuálně atraktivní obsah, který konzistentně funguje na široké škále mobilních zařízení s různými velikostmi a rozlišeními obrazovek. To bylo zvláště důležité pro rané služby mobilních dat jako MMS a mobilní prohlížení ([WAP](/mobilnisite/slovnik/wap/)), kde byla přenosová kapacita vzácná a schopnosti zařízení se výrazně lišily. WVG zajišťoval, že jeden grafický soubor může být odeslán na všechna zařízení a na každém z nich se příslušně vykreslí, což zjednodušilo tvorbu a doručování obsahu.

## K čemu slouží

WVG byl vyvinut pro řešení výzev spojených s doručováním grafického obsahu do heterogenního a omezeného světa mobilních telefonů v éře 2.5G/3G. Rastrové obrázky byly neefektivní: obrázek s vysokým rozlišením potřebný pro velkou obrazovku by byl plýtváním přenosové kapacity na malé obrazovce, zatímco malý obrázek by při zvětšení zobrazil pixely. Navíc vytváření více rastrových verzí pro různé velikosti obrazovek násobilo náklady na tvorbu a úložiště obsahu. Existovala potřeba grafického formátu, který by byl nezávislý na rozlišení, efektivní z hlediska přenosové kapacity a schopný podporovat jednoduché animace a interaktivitu pro zlepšení uživatelského zážitku.

Vytvoření WVG bylo motivováno úspěchem vektorové grafiky na desktopu (např. [SVG](/mobilnisite/slovnik/svg/)), ale se zaměřením na specifická omezení mobilních zařízení: omezený výpočetní výkon, paměť a výdrž baterie. Cílem bylo poskytnout podmnožinu funkcionality, kterou bylo praktické implementovat na široké škále přístrojů. Standardizací tohoto formátu v rámci 3GPP byla zajištěna interoperabilita, což umožnilo poskytovatelům obsahu investovat do tvorby WVG grafiky s jistotou, že bude fungovat na jakémkoli kompatibilním zařízení. Tím byl vyřešen problém fragmentace a umožněn růst bohatších služeb mobilního obsahu, od animovaných zpráv po sofistikovanější rozhraní mobilních aplikací, v rámci kontrolovaného ekosystému služeb operátorů před příchodem výkonných smartphonů a vysokorychlostního mobilního širokopásmového připojení.

## Klíčové vlastnosti

- Binární a XML-based formát pro 2D vektorovou grafiku a animace
- Nezávislé škálování na rozlišení pro zobrazení na jakékoli velikosti obrazovky
- Malá velikost souboru ve srovnání s ekvivalentními rastrovými obrázky, šetří přenosovou kapacitu
- Podpora základních časových os animací a uživatelské interakce prostřednictvím skriptování
- Definovaná sada kreslicích primitiv (cesty, text, základní tvary) a atributů stylu
- Standardizované chování vykreslování pro zajištění konzistentního zobrazení napříč zařízeními

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [SVG – Scalable Vector Graphics](/mobilnisite/slovnik/svg/)
- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)

## Definující specifikace

- **TS 29.311** (Rel-19) — Service Level Interworking for Messaging

---

📖 **Anglický originál a plná specifikace:** [WVG na 3GPP Explorer](https://3gpp-explorer.com/glossary/wvg/)
