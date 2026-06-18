---
slug: "nlsml"
url: "/mobilnisite/slovnik/nlsml/"
type: "slovnik"
title: "NLSML – Natural Language Semantics Markup Language"
date: 2025-01-01
abbr: "NLSML"
fullName: "Natural Language Semantics Markup Language"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nlsml/"
summary: "NLSML je značkovací jazyk založený na XML, definovaný konsorciem 3GPP, pro reprezentaci sémantických výsledků zpracování přirozeného jazyka (NLP) v hlasových službách. Standardizuje způsob, jakým je m"
---

NLSML je značkovací jazyk založený na XML, definovaný konsorciem 3GPP, pro reprezentaci sémantických výsledků zpracování přirozeného jazyka. Slouží ke standardizaci interpretace mluvených dotazů do strukturovaných dat pro síťové aplikace.

## Popis

Natural Language Semantics Markup Language (NLSML) je schéma [XML](/mobilnisite/slovnik/xml/) definované v 3GPP TS 23.333. Slouží jako standardizovaný datový formát pro předání sémantické interpretace přirozeného jazykového projevu uživatele, typicky pocházejícího ze systému rozpoznávání řeči. Když uživatel vysloví příkaz nebo dotaz směrem k síťové službě (např. "zavolej Janu Novákovi" nebo "jaké je počasí v Praze?"), automatické rozpoznávání řeči ([ASR](/mobilnisite/slovnik/asr/)) převede zvuk na text. Komponenty pro porozumění přirozenému jazyku (NLU) následně tento text analyzují, aby extrahovaly význam a záměr. NLSML poskytuje společnou strukturu pro reprezentaci této extrahované sémantiky ve strojově čitelném formátu.

Struktura dokumentu NLSML zahrnuje elementy pro popis výsledků interpretace. Mezi klíčové komponenty patří element 'interpretation', který obsahuje jednu nebo více možných interpretací promluvy, každou s přidruženým skóre spolehlivosti. V rámci jedné interpretace jsou zakódovány podrobnosti jako identifikovaná 'action' (např. 'dial', 'search'), 'input' módy a 'instance' data (např. jméno kontaktu 'Jan Novák' pro akci volání). Tato strukturovaná reprezentace umožňuje přijímající aplikační server (např. server pro řízení hlasových hovorů nebo informační služba) jednoznačně porozumět uživatelskému požadavku bez nutnosti znovu analyzovat původní text, což umožňuje spolehlivé provedení zamýšlené služby.

NLSML funguje v rámci širší architektury služeb IP Multimedia Subsystem (IMS) dle 3GPP pro hlasové aplikace. Je klíčovou součástí rozhraní mezi Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), která může hostovat prostředky pro zpracování řeči, a aplikačními servery, které poskytují vlastní servisní logiku. Standardizací tohoto sémantického rozhraní NLSML zajišťuje interoperabilitu mezi motory pro rozpoznávání řeči od různých dodavatelů a množstvím potenciálních aplikačních služeb, čímž podporuje ekosystém pokročilých hlasových služeb v mobilních sítích.

## K čemu slouží

NLSML byl vytvořen k řešení problému interoperability v hlasových službách. Před standardizací používali vývojáři hlasových aplikací a dodavatelé síťového vybavení proprietární formáty pro reprezentaci výsledků rozpoznávání a porozumění řeči. To uzamklo poskytovatele služeb k řešením konkrétních dodavatelů a ztížilo kombinaci nejlepších dostupných komponent pro [ASR](/mobilnisite/slovnik/asr/), NLU a aplikační logiku. Rozšíření interaktivních hlasových služeb a hlasem ovládaných funkcí v mobilních sítích si vyžádalo společný jazyk pro sémantiku.

Jeho vývoj, počínaje Release 7, byl motivován růstem IMS a snahou nabízet bohaté síťové hlasové služby, jako je hlasové vytáčení, hlasové vyhledávání a hlasová navigace, způsobem nezávislým na dodavateli. NLSML poskytuje jasnou smlouvu mezi komponentou, která rozumí uživatelské řeči (často v síti), a komponentou, která na základě tohoto porozumění jedná (aplikační služba). Toto oddělení odpovědností umožňuje inovace a specializaci jak v oblasti řečových technologií, tak v návrhu služeb, při zachování stabilního rozhraní. Řeší omezení předchozích ad-hoc přístupů tím, že poskytuje robustní, rozšiřitelný a standardizovaný značkovací jazyk, který dokáže reprezentovat složité uživatelské záměry a přidružená datová pole.

## Klíčové vlastnosti

- Schéma založené na XML pro reprezentaci sémantických interpretací přirozeného jazyka
- Podpora více alternativních interpretací se skóre spolehlivosti
- Kóduje uživatelský záměr (akci), relevantní entity (instance) a modalitu
- Umožňuje interoperabilitu mezi procesory řeči a aplikačními servery
- Integruje se s architekturou 3GPP IMS a Media Resource Function (MRF)
- Usnadňuje vývoj hlasových služeb nezávislých na dodavateli

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [ASR – Automatic Speech Recognition](/mobilnisite/slovnik/asr/)
- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements

---

📖 **Anglický originál a plná specifikace:** [NLSML na 3GPP Explorer](https://3gpp-explorer.com/glossary/nlsml/)
