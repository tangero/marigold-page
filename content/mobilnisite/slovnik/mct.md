---
slug: "mct"
url: "/mobilnisite/slovnik/mct/"
type: "slovnik"
title: "MCT – Multi-channel Coding Tool"
date: 2025-01-01
abbr: "MCT"
fullName: "Multi-channel Coding Tool"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mct/"
summary: "Nástroj 3GPP pro kódování více zvukových kanálů do jediného bitového toku, zavedený ve verzi Rel-18. Umožňuje efektivní, vysoce kvalitní imerzivní zvukové zážitky, jako je prostorový zvuk, pro služby"
---

MCT je nástroj 3GPP zavedený ve verzi Rel-18 pro efektivní kódování více zvukových kanálů do jediného bitového toku, který umožňuje vysoce kvalitní imerzivní zvukové zážitky, jako je prostorový zvuk.

## Popis

Multi-channel Coding Tool (MCT) je standardizovaná součást zvukového kodeku definovaná ve specifikacích 3GPP, navržená pro zpracování komprese a přenosu vícekanálových zvukových signálů. Funguje tak, že kóduje více samostatných zvukových kanálů do jediného sjednoceného bitového toku, který je následně přenášen přes síť. Architektura MCT se integruje s existujícími rámci pro doručování médií v 3GPP, jako jsou ty definované pro kodek Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) nebo budoucí imerzivní zvukové kodeky, což umožňuje jeho použití spolu s dalšími moduly pro zpracování zvuku, jako je rozšíření šířky pásma nebo maskování chyb. Mezi klíčové komponenty patří kodér kanálů, který aplikuje principy percepčního kódování ke snížení redundance mezi kanály, extraktor parametrů prostorového zvuku, který zachycuje směrové informace, a multiplexor bitového toku, který kombinuje všechna data pro efektivní paketizaci. Jeho role v síti je primárně v médiové rovině uživatelského zařízení (UE) a aplikačních serverů, kde zpracovává zvuk před přenosem nebo po příjmu, a zajišťuje tak, že imerzivní zvukové aplikace mohou fungovat s vysokou kvalitou a nízkou latencí vyžadovanou pro interakce v reálném čase. Nástroj podporuje různé konfigurace kanálů, jako je prostorový zvuk 5.1 nebo formáty Ambisonics, což jej činí univerzálním pro různé případy užití od zábavy po komunikaci. Standardizací tohoto nástroje 3GPP zajišťuje interoperabilitu napříč zařízeními a sítěmi a usnadňuje tak široké přijetí pokročilých zvukových služeb v 5G a dalších generacích.

## K čemu slouží

MCT byl vytvořen, aby řešil rostoucí poptávku po imerzivních zvukových zážitcích v mobilních sítích, poháněnou aplikacemi jako Extended Reality (XR), virtuální schůzky a zábava ve vysoké věrnosti. Před jeho zavedením byly zvukové kodeky 3GPP, jako je [EVS](/mobilnisite/slovnik/evs/), optimalizovány primárně pro mono nebo stereo kanály a postrádaly efektivní nativní podporu pro vícekanálový prostorový zvuk, což často vyžadovalo proprietární řešení nebo neefektivní přenos více nezávislých toků. Toto omezení bránilo kvalitě a škálovatelnosti imerzivních služeb, protože spotřebovávaly nadměrnou přenosovou kapacitu a trpěly problémy s interoperabilitou. Vývoj MCT ve verzi Rel-18 byl motivován potřebou standardizovat nástroj, který by dokázal kódovat více zvukových kanálů s vysokou kompresní účinností, čímž by snížil zatížení sítě při zachování percepční kvality. Řeší problémy související s omezeními přenosové kapacity v sítích 5G, kde náročné aplikace na data, jako je XR, vyžadují optimalizované zpracování médií pro zajištění plynulého uživatelského zážitku. Historicky, jak se 3GPP vyvíjelo od služeb zaměřených na hlas k službám bohatým na média, přidání MCT odráží posun směrem k podpoře složitých zvukových prostředí, což umožňuje nové zdroje příjmů pro operátory a vylepšenou funkčnost pro koncové uživatele v oblastech, jako jsou hry, teleprezence a rozšířená realita.

## Klíčové vlastnosti

- Efektivní kódování více zvukových kanálů do jediného bitového toku
- Podpora různých konfigurací kanálů (např. 5.1, Ambisonics)
- Integrace se zvukovými kodeky 3GPP, jako je EVS, pro zpětnou kompatibilitu
- Techniky percepčního kódování pro snížení redundance mezi kanály
- Zpracování s nízkou latencí vhodné pro komunikaci v reálném čase
- Standardizovaný formát bitového toku zajišťující interoperabilitu napříč zařízeními

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.254** (Rel-19) — IVAS Rendering Functions Specification
- **TS 26.255** (Rel-19) — IVAS Frame Loss Concealment Procedure

---

📖 **Anglický originál a plná specifikace:** [MCT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mct/)
