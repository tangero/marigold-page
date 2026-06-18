---
slug: "cpl"
url: "/mobilnisite/slovnik/cpl/"
type: "slovnik"
title: "CPL – Call Processing Language"
date: 2025-01-01
abbr: "CPL"
fullName: "Call Processing Language"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cpl/"
summary: "CPL je standardizovaný skriptovací jazyk definovaný 3GPP pro popis a řízení telefonních služeb v IP sítích. Umožňuje poskytovatelům služeb vytvářet přizpůsobené chování při zpracování hovorů bez nutno"
---

CPL je standardizovaný skriptovací jazyk 3GPP pro popis a řízení telefonních služeb, jako je přesměrování a filtrování hovorů, v IP sítích, který umožňuje přizpůsobené zpracování hovorů.

## Popis

Call Processing Language (CPL) je skriptovací jazyk založený na [XML](/mobilnisite/slovnik/xml/), standardizovaný 3GPP pro popis telefonních služeb v IP Multimedia Subsystem (IMS) a dalších IP telefonních sítích. Tento jazyk poskytuje standardizovaný způsob, jak specifikovat, jak mají být zpracovávány příchozí a odchozí hovory, což umožňuje poskytovatelům služeb implementovat přizpůsobenou logiku zpracování hovorů bez nutnosti proprietárních řešení. Skripty CPL jsou vykonávány síťovými elementy nazývanými CPL servery, které skripty interpretují a aplikují specifikovaná pravidla pro zpracování hovorů na signalizační zprávy [SIP](/mobilnisite/slovnik/sip/).

CPL funguje prostřednictvím strukturovaného XML schématu, které definuje různé akce a podmínky pro zpracování hovorů. Jazyk zahrnuje dva hlavní typy uzlů: signalizační akce (jako proxy, přesměrování, odmítnutí) a modifikátory lokace (jako lokace, vyhledání). Tyto uzly lze kombinovat s podmíněnými příkazy založenými na parametrech hovoru, jako je identita volajícího, denní doba, stav přítomnosti nebo volané číslo. Skripty jsou typicky uloženy v databázi uživatelských profilů a staženy na CPL server při potřebě zpracování hovoru.

Architektonicky se CPL integruje do sítí založených na SIP prostřednictvím CPL serverů, které lze nasadit jako samostatné entity nebo integrovat v rámci Application Serverů ([AS](/mobilnisite/slovnik/as/)) nebo SIP proxy. Když dorazí SIP požadavek, CPL server načte příslušný skript, zpracuje strukturu XML a vykoná logiku sekvenčně. Jazyk podporuje zpracování jak příchozích, tak odchozích hovorů s oddělenými sekcemi skriptu pro každý směr. Klíčové komponenty zahrnují interpret CPL, úložiště skriptů a rozhraní k databázím účastníků pro získávání uživatelsky specifických skriptů.

Role CPL v sítích 3GPP přesahuje základní řízení hovorů a umožňuje pokročilé telefonní služby v IMS. Poskytuje standardizovaný mechanismus pro implementaci služeb, které byly tradičně pevně zabudovány do přepojovacích zařízení, což umožňuje větší flexibilitu a rychlejší nasazení služeb. Základ jazyka v XML jej činí čitelným pro člověka a zpracovatelným strojem, což usnadňuje jak ruční tvorbu návrháři služeb, tak automatické generování prostředími pro tvorbu služeb. Skripty CPL lze měnit dynamicky bez dopadu na podkladovou síťovou infrastrukturu, což podporuje rychlé aktualizace a přizpůsobení služeb.

## K čemu slouží

CPL byl vytvořen pro řešení potřeby standardizované, na dodavateli nezávislé metody implementace telefonních služeb v IP sítích. Před CPL se poskytovatelé služeb spoléhali na proprietární skriptovací jazyky nebo pevně zabudovanou servisní logiku v síťovém zařízení, což vytvářelo problémy s interoperabilitou a závislost na dodavateli. Nástup telefonie založené na [SIP](/mobilnisite/slovnik/sip/) a architektur IMS si vyžádal společný jazyk, který by mohl fungovat napříč zařízeními různých dodavatelů při zachování bezpečnosti a spolehlivosti.

Primární motivací pro vývoj CPL bylo oddělení servisní logiky od síťové infrastruktury, což umožňuje rychlejší nasazení služeb a větší inovace. Tradiční telefonní služby vyžadovaly rozsáhlé testování a integraci s konkrétním zařízením dodavatele, což zpomalovalo uvedení nových funkcí na trh. CPL poskytlo standardizované rozhraní, které umožnilo poskytovatelům služeb vytvářet služby jednou a nasazovat je napříč více-dodavatelskými sítěmi. To bylo obzvláště důležité, protože telekomunikace směřovaly k plně IP sítím, kde služby musely fungovat konzistentně napříč různými přístupovými technologiemi.

CPL také řešilo rostoucí poptávku po službách řízených uživatelem v sítích nové generace. Na rozdíl od tradičních služeb Intelligent Network ([IN](/mobilnisite/slovnik/in/)), které byly plně pod kontrolou operátorů, CPL umožnilo koncovým uživatelům přizpůsobovat své chování při zpracování hovorů prostřednictvím webových rozhraní nebo jiných nástrojů správy. Toto posílení uživatelů bylo v souladu se širším trendem personalizovaných komunikačních služeb v sítích 3GPP. Design jazyka upřednostňoval bezpečnost a zabezpečení, aby uživatelsky vytvořené skripty nemohly způsobit nestabilitu sítě nebo bezpečnostní průniky, a zároveň poskytoval smysluplné možnosti přizpůsobení.

## Klíčové vlastnosti

- Skriptovací jazyk pro telefonní služby založený na XML
- Podpora zpracování příchozích i odchozích hovorů
- Podmíněná logika založená na parametrech hovoru a stavu uživatele
- Standardizované akce pro hovory včetně proxy, přesměrování a odmítnutí
- Integrace se signalizací SIP v IMS sítích
- Možnosti přizpůsobení služeb řízené uživatelem

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.218** (Rel-19) — IMS Call Model Specification

---

📖 **Anglický originál a plná specifikace:** [CPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpl/)
