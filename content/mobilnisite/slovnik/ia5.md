---
slug: "ia5"
url: "/mobilnisite/slovnik/ia5/"
type: "slovnik"
title: "IA5 – International Alphabet no. 5"
date: 2025-01-01
abbr: "IA5"
fullName: "International Alphabet no. 5"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ia5/"
summary: "IA5 je standardizované 7bitové kódování znaků definované ITU-T, používané v 3GPP pro textové služby jako SMS a USSD. Poskytuje základní, mezinárodně uznávanou abecedu pro reprezentaci alfanumerických"
---

IA5 je standardizované 7bitové kódování znaků definované ITU-T, používané v 3GPP pro textové služby jako SMS a USSD za účelem zajištění interoperability.

## Popis

International Alphabet no. 5 (IA5) je standard pro kódování znaků, ekvivalentní ASCII (American Standard Code for Information Interchange), definovaný v doporučení [ITU-T](/mobilnisite/slovnik/itu-t/) T.50. Jedná se o 7bitový kód umožňující 128 různých znaků, které zahrnují velká a malá písmena latinky (A-Z, a-z), číslice (0-9), sadu interpunkčních znamének a soubor řídicích znaků (netisknutelné znaky používané pro řízení zařízení). V kontextu specifikací 3GPP slouží IA5 jako základní schéma kódování pro reprezentaci textu v různých telekomunikačních službách a protokolech. Jeho hlavní úlohou je poskytnout společné a jednoznačné mapování mezi číselnými kódy a textovými znaky, což je zásadní pro spolehlivou výměnu informací.

V systémech 3GPP je IA5 explicitně uvedeno ve specifikacích jako 3GPP TS 27.002 pro služby přepojování okruhů a 3GPP TS 33.108 pro kryptografické požadavky na algoritmy. Používá se pro kódování textových informací ve službách jako Short Message Service ([SMS](/mobilnisite/slovnik/sms/)), Unstructured Supplementary Service Data ([USSD](/mobilnisite/slovnik/ussd/)) a v určitých polích signalizačních protokolů. Pro SMS lze pole TP-User-Data kódovat pomocí abecedy IA5, pokud schéma kódování dat (Data Coding Scheme) indikuje výchozí 7bitovou abecedu. Toto kódování zajišťuje, že základní textové zprávy složené z běžných latinských znaků mohou být příjemcem správně interpretovány bez ohledu na konkrétního výrobce nebo síťového operátora.

Technická implementace spočívá v mapování každého znaku v řetězci na jeho odpovídající 7bitovou binární hodnotu podle tabulky IA5. Protože se jedná o 7bitový kód, je pro ukládání latinského textu efektivnější než 8bitová nebo 16bitová kódování, pokud takové znaky postačují. Neobsahuje však podporu pro znaky z jiných písem (např. arabské, čínské, cyrilice). Pro ty 3GPP specifikuje jiná kódování, jako je [UCS2](/mobilnisite/slovnik/ucs2/) (16bitový Unicode). Použití IA5 je obvykle řízeno protokoly vyšší vrstvy nebo popisy služeb, které definují, kdy má být tato konkrétní abeceda použita. Jeho jednoduchost a široké historické přijetí z něj činí spolehlivý základ pro interoperabilitu v globálních telekomunikacích, i když jeho použití je obecně omezeno na aplikace, kde je přijatelná omezená znaková sada.

## K čemu slouží

Účelem specifikace IA5 v rámci standardů 3GPP je stanovit univerzální, minimální kódování znaků pro textová data vyměňovaná v mobilních sítích. V počátcích digitálních telekomunikací byl konzistentní způsob reprezentace základního textu nezbytný pro služby jako [SMS](/mobilnisite/slovnik/sms/), aby fungovaly bezproblémově přes mezinárodní hranice a mezi zařízeními různých výrobců. IA5 jako zavedený standard [ITU](/mobilnisite/slovnik/itu/) poskytlo tuto společnou půdu a zabránilo tak nesprávné interpretaci znaků kvůli proprietárním nebo regionálním rozdílům v kódování.

Před rozšířenou standardizací mohly různé systémy používat mírně odlišné znakové sady (jako různé národní varianty ASCII), což vedlo k potenciálním chybám v komunikaci. Povinným zavedením IA5 pro konkrétní aplikace 3GPP zajistilo, že zpráva 'Hello' odeslaná ze zařízení v jedné zemi bude na zařízení v jiné zemi dekódována jako 'Hello'. To bylo klíčové pro globální úspěch SMS. Navíc jeho 7bitová povaha dobře korespondovala s návrhem raných signalizačních systémů, což umožňovalo efektivní zabalení textu do binárních polí datových jednotek protokolu.

Zatímco IA5 řeší potřebu interoperability pro základní latinský text, jeho omezením je nedostatek podpory pro mezinárodní písma. To motivovalo pozdější přijetí a specifikaci komplexnějších schémat kódování, jako jsou [UCS2](/mobilnisite/slovnik/ucs2/) a [UTF-8](/mobilnisite/slovnik/utf-8/), v rámci 3GPP pro bohatší zasílání zpráv. Avšak kvůli podpoře starších systémů, efektivitě v sítích, kde jsou potřeba pouze základní znaky, a specifickým požadavkům protokolů zůstává IA5 definovanou a nezbytnou součástí ekosystému 3GPP.

## Klíčové vlastnosti

- 7bitové kódování znaků umožňující efektivní uložení základního latinského textu
- Standardizované mapování 128 znaků včetně písmen, číslic a řídicích kódů
- Ekvivalent ITU-T T.50 / ASCII zajišťující globální interoperabilitu
- Specifikováno pro použití ve službách 3GPP SMS a USSD
- Poskytuje základní kódování pro datová pole protokolů
- Umožňuje jednoznačnou interpretaci textu mezi síťovými prvky

## Související pojmy

- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)
- [UCS2 – Universal two byte coded Character Set](/mobilnisite/slovnik/ucs2/)

## Definující specifikace

- **TS 27.002** (Rel-19) — Terminal Adaptation Functions for Asynchronous Services
- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [IA5 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ia5/)
