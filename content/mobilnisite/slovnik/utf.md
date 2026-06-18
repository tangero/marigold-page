---
slug: "utf"
url: "/mobilnisite/slovnik/utf/"
type: "slovnik"
title: "UTF – Unicode Transformation Format"
date: 2025-01-01
abbr: "UTF"
fullName: "Unicode Transformation Format"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/utf/"
summary: "Standardizovaný formát kódování znaků z normy Unicode, který přijal 3GPP pro reprezentaci textu v protokolech a rozhraních. Zajišťuje globální interoperabilitu pro textové informace, jako jsou jména ú"
---

UTF je standardizovaný formát kódování znaků z normy Unicode, který přijal 3GPP pro reprezentaci textu v protokolech a rozhraních, čímž zajišťuje globální interoperabilitu díky podpoře znaků všech světových jazyků.

## Popis

V rámci specifikací 3GPP se termín Unicode Transformation Format (UTF) vztahuje k přijetí konkrétních schémat kódování Unicode pro reprezentaci textových řetězců v různých protokolech, rozhraních a datových strukturách. Unicode sám o sobě je univerzální znaková sada, která přiřazuje každému znaku všech hlavních písemných systémů jedinečný kódový bod (číslo). UTF je mechanismus pro transformaci těchto abstraktních kódových bodů na posloupnost bajtů pro uložení nebo přenos. 3GPP primárně vyžaduje použití [UTF-8](/mobilnisite/slovnik/utf-8/), což je kódování s proměnnou délkou, a někdy [UTF-16](/mobilnisite/slovnik/utf-16/) nebo UTF-32, v závislosti na aplikačním kontextu.

Technická implementace zahrnuje zakódování textových dat podle pravidel daného schématu UTF před jejich umístěním do jednotky protokolových dat ([PDU](/mobilnisite/slovnik/pdu/)). Například v IP Multimedia Subsystem (IMS) se UTF-8 používá pro kódování textu v hlavičkách [SIP](/mobilnisite/slovnik/sip/) a tělech zpráv. V aplikační sadě Universal Subscriber Identity Module ([USIM](/mobilnisite/slovnik/usim/)) se pro textové řetězce zobrazované na UE může použít UTF-8 nebo UTF-16. Proces kódování UTF-8 je zvláště efektivní: znaky ASCII (kódové body 0–127) reprezentuje jako jeden bajt, shodně s ASCII, což zajišťuje zpětnou kompatibilitu. Znaky z jiných písem (jako Latin-1 Supplement, řecké, cyrilice nebo asijské ideogramy) jsou kódovány jako sekvence dvou, tří nebo čtyř bajtů. Každá bajtová sekvence je navržena jako samosynchronizující, což umožňuje robustní analýzu i v případě poškození dat nebo při zahájení čtení uprostřed znaku.

Z architektonického hlediska je použití UTF zakotveno v definicích Abstract Syntax Notation (ASN.1) a dokumentech specifikace protokolů. Když norma 3GPP definuje informační prvek ([IE](/mobilnisite/slovnik/ie/)) typu 'string' nebo 'text', explicitně odkazuje na kódování znaků, například 'UTF8String' v ASN.1. Toto zajišťuje, že když síťový prvek v jedné zemi (používající např. arabské písmo) odešle textový parametr prvku v jiné zemi (používající čínské písmo), oba konce správně interpretují bajtovou sekvenci na zamýšlené znaky. Tato globální interoperabilita je zásadní pro služby orientované na účastníka, jako je Short Message Service ([SMS](/mobilnisite/slovnik/sms/)), Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)) a informace o identitě účastníka (např. jméno uložené na SIM kartě), stejně jako pro správu sítě a konfigurační data, která mohou obsahovat popisný text.

## K čemu slouží

Účelem standardizace UTF v rámci 3GPP bylo vyřešit závažné problémy s interoperabilitou způsobené množstvím nekompatibilních národních a regionálních kódování znaků (např. ASCII, řada ISO-8859, Shift-JIS, GB2312). Rané mobilní systémy byly často omezeny na základní ASCII nebo na rozšíření specifická pro výrobce, což znemožňovalo globální výměnu textu v místních jazycích. Jak se celulární sítě rozšiřovaly po celém světě a služby jako SMS se staly všudypřítomnými, stala se kritickou potřeba jediného univerzálního kódování, které by mohlo reprezentovat jakýkoli znak z jakéhokoli jazyka.

UTF, konkrétně UTF-8, bylo přijato pro zajištění budoucí odolnosti systémů 3GPP. Umožňuje jedné implementaci zpracovat všechna současná i budoucí písma definovaná normou Unicode, čímž odstraňuje potřebu složité detekce a konverze znakových sad. To je nezbytné pro globalizaci telekomunikačních služeb, umožňuje účastníkovi v Japonsku odeslat SMS obsahující znaky kandži účastníkovi v Egyptě používajícímu arabské písmo, přičemž síť zprávu věrně přenáší a doručuje. Také podporuje správné zobrazení jmen účastníků v telefonních seznamech napříč různými výrobci zařízení a síťovými operátory.

Navíc volba UTF-8 je v souladu s internetovými standardy, kde je dominantním kódováním pro webové stránky, e-maily a další protokoly. Tato harmonizace zjednodušuje integraci telekomunikačních sítí s internetovými službami (např. IMS, webové zřizování). Tím, že 3GPP vyžaduje UTF, zajišťuje, že jeho sítě jsou schopny podporovat plnou jazykovou rozmanitost svých účastníků, což je základním požadavkem pro přijetí uživateli a pro umožnění skutečně globálních mobilních komunikačních služeb.

## Klíčové vlastnosti

- Podporuje celou znakovou sadu Unicode, což umožňuje globální reprezentaci textu
- UTF-8 poskytuje zpětnou kompatibilitu s ASCII pro efektivní kódování základních latinských znaků
- Definuje schémata kódování s proměnnou délkou (UTF-8, UTF-16) pro vyvážení efektivity a jednoduchosti
- Zajišťuje jednoznačnou výměnu textu napříč více dodavatelskými a více regionálními sítěmi
- Je vyžadováno v protokolech 3GPP pro textové informační prvky a parametry služeb
- Umožňuje robustní analýzu díky samosynchronizujícím hranicím znaků v bajtových tocích

## Související pojmy

- [UTF-8 – Unicode Transformation Format - 8-bit](/mobilnisite/slovnik/utf-8/)

## Definující specifikace

- **TS 26.230** (Rel-19) — CTM C Code Implementation for Text Transmission
- **TS 29.229** (Rel-19) — Diameter Protocol for Cx/Dx Interfaces
- **TS 29.329** (Rel-19) — Diameter Protocol for Sh Interface
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [UTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/utf/)
