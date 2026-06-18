---
slug: "dom"
url: "/mobilnisite/slovnik/dom/"
type: "slovnik"
title: "DOM – Document Object Model"
date: 2025-01-01
abbr: "DOM"
fullName: "Document Object Model"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dom/"
summary: "Platformově a jazykově neutrální rozhraní, které umožňuje programům a skriptům dynamicky přistupovat a aktualizovat obsah, strukturu a styl dokumentů. V 3GPP se používá pro definici a zpracování struk"
---

DOM je platformově a jazykově neutrální rozhraní používané v 3GPP pro definici a zpracování strukturovaných datových formátů, které umožňuje programům dynamicky přistupovat a aktualizovat obsah, strukturu a styl dokumentu.

## Popis

Document Object Model (DOM) je multiplatformní a jazykově nezávislá konvence pro reprezentaci a interakci s objekty v dokumentech [HTML](/mobilnisite/slovnik/html/), [XHTML](/mobilnisite/slovnik/xhtml/) a [XML](/mobilnisite/slovnik/xml/). V kontextu standardizace 3GPP není DOM síťový prvek, ale základní programovací rozhraní používané ve specifikacích týkajících se servisních enablerů, multimediálních zpráv a formátů obsahu. Poskytuje strukturovanou, stromovou reprezentaci dokumentu, kde každý uzel je objekt reprezentující část dokumentu. Tento model umožňuje aplikacím programově procházet strukturu dokumentu, přistupovat k jeho obsahu a měnit jej, což je nezbytné pro dynamické generování a zpracování obsahu.

Ve specifikacích 3GPP je DOM odkazováno v technických zprávách a specifikacích, které definují servisní schopnosti a datové formáty. Například se používá v kontextu služby multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)) pro manipulaci s obsahem zpráv nebo v architekturách servisních enablerů pro definici způsobu, jakým mohou aplikace interagovat se strukturovanými daty. Rozhraní DOM definuje logickou strukturu dokumentů a způsob přístupu k dokumentu a jeho manipulace. Mezi klíčové komponenty patří základní specifikace DOM, která definuje základní typy objektů a jejich vztahy, a rozšíření pro konkrétní typy dokumentů, jako je HTML DOM nebo XML DOM.

Z architektonického pohledu je DOM [API](/mobilnisite/slovnik/api/), které se nachází mezi aplikační logikou a reprezentací dat. Abstrahuje dokument do hierarchie uzlů, jako jsou uzly elementů, atributů a textu. Tato hierarchická stromová struktura umožňuje efektivní procházení a manipulaci pomocí standardních metod, jako jsou getElementById nebo getElementsByTagName. V systémech 3GPP je toto klíčové pro zajištění interoperability mezi různými síťovými prvky a uživatelskými zařízeními (UE) při zpracování složitých datových formátů, protože poskytuje konzistentní způsob parsování, generování a transformace strukturovaných dat napříč různými platformami a programovacími jazyky.

## K čemu slouží

Document Object Model byl vytvořen, aby poskytl standardizovaný, platformově nezávislý způsob přístupu a manipulace s obsahem a strukturou dokumentů, primárně pro webové technologie. Jeho přijetí ve specifikacích 3GPP řeší potřebu konzistentního zpracování dat v multimediálních službách a aplikačních enablerech napříč heterogenními mobilními sítěmi a zařízeními. Před DOM vedly proprietární [API](/mobilnisite/slovnik/api/) a ad-hoc metody parsování k fragmentaci, což ztěžovalo zajištění interoperability mezi implementacemi služeb různých dodavatelů, jako je [MMS](/mobilnisite/slovnik/mms/) nebo dynamické doručování obsahu.

V historickém kontextu mobilních komunikací, jak se služby vyvíjely od jednoduchého hlasu k bohatým multimédiím, rostl požadavek na společné rozhraní pro zpracování strukturovaných datových formátů, jako jsou [XML](/mobilnisite/slovnik/xml/) a HTML. DOM to řeší tím, že nabízí dobře definovaný objektový model, který odděluje strukturu dokumentu od aplikační logiky, což vývojářům umožňuje psát přenositelný kód fungující v různých provozních prostředích. Tato standardizace je obzvláště důležitá v ekosystému 3GPP, kde musí více síťových prvků, od aplikačních serverů po uživatelská zařízení (UE), spolehlivě vyměňovat a zpracovávat složitá data bez problémů s kompatibilitou.

Motivace pro odkazování na DOM ve specifikacích 3GPP vychází z potřeby využití zavedených webových standardů pro urychlení vývoje služeb a zajištění široké kompatibility. Začleněním DOM se 3GPP sladí s širšími průmyslovými postupy, což usnadňuje integraci mobilních sítí s internetovými technologiemi. Tento přístup řeší omezení dřívějších nestandardizovaných metod, které byly náchylné k chybám a omezovaly škálovatelnost a flexibilitu implementací služeb, čímž podporuje vývoj směrem k dynamičtějším a interaktivnějším mobilním službám.

## Klíčové vlastnosti

- Platformově a jazykově neutrální rozhraní pro přístup k dokumentům
- Stromová reprezentace dokumentů jako hierarchie uzlů
- Programové procházení, přístup a úprava obsahu dokumentu
- Podpora dynamických aktualizací struktury a stylu dokumentu
- Standardizované metody pro dotazování a manipulaci s elementy
- Umožňuje interoperabilitu při zpracování dat XML a HTML v systémech 3GPP

## Související pojmy

- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [API – Application Programming Interface](/mobilnisite/slovnik/api/)

## Definující specifikace

- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [DOM na 3GPP Explorer](https://3gpp-explorer.com/glossary/dom/)
