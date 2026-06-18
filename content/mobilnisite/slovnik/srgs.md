---
slug: "srgs"
url: "/mobilnisite/slovnik/srgs/"
type: "slovnik"
title: "SRGS – Speech Recognition Grammar Specification"
date: 2025-01-01
abbr: "SRGS"
fullName: "Speech Recognition Grammar Specification"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/srgs/"
summary: "Standard W3C založený na XML, který přijala organizace 3GPP pro definování slov a vzorů, které může rozpoznat engine pro rozpoznávání řeči. Používá se v hlasem ovládaných službách (např. hlasové vytáč"
---

SRGS je standard W3C založený na XML, který přijala organizace 3GPP pro definování slov a vzorů, které může rozpoznat engine pro rozpoznávání řeči v hlasem ovládaných službách.

## Popis

Speech Recognition Grammar Specification (SRGS) je značkovací jazyk pro definování gramatik používaných enginy pro rozpoznávání řeči. V kontextu 3GPP je využíván v rámci IMS a dalších servisních rámců pro umožnění hlasem řízených aplikací. Gramatika SRGS je v podstatě soubor pravidel, která definují posloupnosti slov nebo frází (tokenů), které může uživatel vyslovit, a vzory, ve kterých je lze kombinovat. Tyto gramatiky lze psát ve dvou formátech: syntaxi [XML](/mobilnisite/slovnik/xml/) (striktní formát) a syntaxi Augmented BNF ([ABNF](/mobilnisite/slovnik/abnf/)) (kompaktní textový formát). Klíčovou součástí je definice pravidel, která mohou odkazovat na jiná pravidla, což umožňuje modulární a znovupoužitelné struktury gramatik. Gramatika specifikuje povolené výroky, které mohou zahrnovat volitelná slova, alternativy (např. "ano" nebo "jo"), sekvence a opakování. Může také asociovat sémantické interpretace s rozpoznanými frázemi, často za použití doprovodné specifikace Semantic Interpretation for Speech Recognition (SISR). Například, když uživatel řekne "zavolej Janovi na mobil", gramatika nejen rozpozná slova, ale může také vyprodukovat strukturovanou datovou interpretaci jako `{příkaz: "zavolej", kontakt: "Jan", typ: "mobil"}`. V síti 3GPP by se na gramatiku SRGS typicky odkazoval aplikační server (např. interpret VoiceXML nebo vlastní telekomunikační [AS](/mobilnisite/slovnik/as/)), a to buď inline, nebo prostřednictvím [URI](/mobilnisite/slovnik/uri/). Když uživatel promluví, je audio odesláno do prostředku pro rozpoznávání řeči (který může být součástí [MRFP](/mobilnisite/slovnik/mrfp/)/[SRF](/mobilnisite/slovnik/srf/)). Rozpoznávací engine použije aktivní gramatiku SRGS k omezení svého vyhledávání, což výrazně zlepšuje přesnost a rychlost tím, že omezí slovní zásobu a jazykový model pro rozpoznávání na kontext konkrétní služby. Výsledek rozpoznání, často ve formě XML dokumentu (jako Natural Language Semantics Markup Language, [NLSML](/mobilnisite/slovnik/nlsml/)), je pak vrácen aplikačnímu serveru ke zpracování.

## K čemu slouží

SRGS byl přijat organizací 3GPP za účelem standardizace a zlepšení vývoje hlasově interaktivních služeb v mobilních sítích. Před standardizací systémy pro rozpoznávání řeči často používaly proprietární, dodavatelem specifické formáty gramatik, což činilo aplikace nepřenositelnými a zvyšovalo složitost vývoje. Účelem specifikace SRGS bylo poskytnout jednotný, interoperabilní způsob, jak definovat, co může uživatel říci k ovládání síťové služby. Tím se řeší problém fragmentace ve vývoji hlasových aplikací a umožňuje se vytváření znovupoužitelných, v síti hostovaných gramatik pro běžné úlohy (jako sběr číslic nebo příkazová slova). Motivací byl růst hlasových služeb, jako jsou automatizovaná zákaznická podpora ([IVR](/mobilnisite/slovnik/ivr/)), hlasové vytáčení a hlasové vyhledávání. Použití standardu jako je SRGS umožňuje poskytovatelům služeb psát gramatiky nezávisle na dodavateli podkladového enginu pro rozpoznávání řeči, což podporuje konkurenci a inovace. Také umožňuje sofistikovanější a přirozenější dialogové interakce ve srovnání s jednoduchými menu založenými na DTMF, čímž zlepšuje uživatelský zážitek. Integrací standardu W3C organizace 3GPP sjednotila mobilní hlasové služby s širšími webovými a IT trendy, což usnadnilo konvergenci telekomunikačních a webových aplikací.

## Klíčové vlastnosti

- Syntaxe XML a ABNF pro definování gramatik pro rozpoznávání řeči.
- Definuje pravidla pro posloupnosti slov, alternativy, volitelné prvky a opakování.
- Podporuje značky pro sémantickou interpretaci (SISR) k extrahování významu z rozpoznané řeči.
- Umožňuje rozpoznávání omezené kontextem pro zlepšenou přesnost a výkon.
- Dokumenty gramatik lze referencovat pomocí URI, což umožňuje síťové ukládání a sdílení.
- Základní pro interaktivní hlasovou odezvu (IVR) založenou na VoiceXML a další služby hlasových příkazů.

## Související pojmy

- [MRFP – Multimedia Resource Function Processor](/mobilnisite/slovnik/mrfp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [IVR – Interactive Voice Response](/mobilnisite/slovnik/ivr/)
- [NLSML – Natural Language Semantics Markup Language](/mobilnisite/slovnik/nlsml/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements

---

📖 **Anglický originál a plná specifikace:** [SRGS na 3GPP Explorer](https://3gpp-explorer.com/glossary/srgs/)
