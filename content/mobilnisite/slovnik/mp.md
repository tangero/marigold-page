---
slug: "mp"
url: "/mobilnisite/slovnik/mp/"
type: "slovnik"
title: "MP – Mandatory Present"
date: 2025-01-01
abbr: "MP"
fullName: "Mandatory Present"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mp/"
summary: "Indikátor pole protokolu, který určuje, že konkrétní informační prvek nebo parametr musí být v zprávě obsažen, aby byla zpráva považována za platnou a zpracovatelnou. Zajišťuje syntaktickou a sémantic"
---

MP je indikátor pole protokolu, který určuje, že konkrétní informační prvek musí být v zprávě obsažen, aby byla považována za platnou a zpracovatelnou.

## Popis

Mandatory Present (MP) je základní koncept v návrhu protokolů 3GPP, konkrétně v rámci kódování založeného na Abstract Syntax Notation One (ASN.1) a definic signalizačních zpráv. Není to samostatný protokol, ale kritický atribut nebo příznak aplikovaný na informační prvky ([IE](/mobilnisite/slovnik/ie/)) v rámci protokolových datových jednotek (PDU). Když je IE označen jako MP, znamená to, že přítomnost tohoto prvku je povinná pro úspěšné parsování, interpretaci a zpracování obsahující zprávy přijímající entitou. Absence MP IE představuje chybu protokolu, která typicky vede k zamítnutí zprávy, často s odpovídajícím kódem příčiny indikujícím chybějící povinný parametr.

Vynucování MP je řešeno na vrstvě protokolu během kódování a dekódování zpráv. Při konstrukci zprávy musí vysílající entita zahrnout všechny IE označené jako MP s platným obsahem. Při příjmu zprávy dekódovací logika zkontroluje přítomnost těchto povinných prvků. Tato kontrola se často provádí proti formální definici struktury zprávy, jako je schéma ASN.1 PER (Packed Encoding Rules) nebo [BER](/mobilnisite/slovnik/ber/) (Basic Encoding Rules). Označení MP je součástí statické definice specifikace protokolu, nacházející se v technických specifikacích jako TS 25.331 ([RRC](/mobilnisite/slovnik/rrc/)), TS 29.060 ([GTP](/mobilnisite/slovnik/gtp/)) a dalších. Liší se od podmíněné přítomnosti, kde zařazení IE závisí na hodnotě jiných polí nebo kontextu zprávy.

MP hraje klíčovou roli při zajišťování interoperability mezi síťovými prvky od různých dodavatelů. Přísným definováním, které parametry jsou pro daný postup nezbytné, zaručuje 3GPP základní společnou úroveň porozumění. Například v zprávě pro nastavení spojení Radio Resource Control (RRC) by byly kritické parametry, jako počáteční identita UE nebo bezpečnostní informace, označeny jako MP. V žádosti o vytvoření sezení v [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol (GTP) by [IMSI](/mobilnisite/slovnik/imsi/) nebo [APN](/mobilnisite/slovnik/apn/) mohly být MP. Tato přísnost zabraňuje nejednoznačné nebo neúplné signalizaci, která by mohla vést k nestabilním stavům sítě, neúspěšným procedurám nebo bezpečnostním slabinám. Koncept je analogický 'povinným polím' ve schématech dat v jiných výpočetních oblastech.

## K čemu slouží

Označení MP existuje za účelem vynucení robustnosti, spolehlivosti a jednoznačné komunikace protokolu mezi síťovými uzly. Ve složitých telekomunikačních systémech s četnými volitelnými funkcemi a konfiguracemi by povolení zpráv s chybějícími kritickými informacemi vedlo k nepředvídatelnému chování, chybám interpretace a obtížně diagnostikovatelným selháním. MP poskytuje jasnou, strojově ověřitelnou smlouvu mezi odesílatelem a příjemcem.

Historicky, jak se protokoly vyvíjely z jednodušších zpráv s pevným formátem na vysoce rozšiřitelné a funkčně bohaté struktury (používající ASN.1 a podobné metody), byl potřebný mechanismus k rozlišení mezi základními podstatnými parametry a volitelnými rozšířeními. MP to řeší definováním nezbytného jádra zprávy. Řeší problém 'tichých selhání', kdy by se přijímač mohl pokusit zpracovat neúplnou zprávu pomocí výchozích nebo zastaralých hodnot, což by potenciálně mohlo způsobit nesprávné přechody stavů, úniky prostředků nebo degradaci služeb. Povinným požadavkem na přítomnost klíčových dat MP zajišťuje, že procedury mají všechny potřebné informace pro správné provedení, což je zásadní pro kritické operace jako předávání, zřizování relace a aktivace zabezpečení.

## Klíčové vlastnosti

- Definuje povinné zahrnutí informačních prvků do protokolových zpráv
- Vynucováno během procesů kódování a dekódování ASN.1
- Způsobuje zamítnutí zprávy, pokud povinný prvek chybí
- Zajišťuje syntaktickou úplnost a sémantickou platnost signalizace
- Kritické pro interoperabilitu mezi zařízeními více dodavatelů
- Odlišeno od volitelných (OP) a podmíněně volitelných prvků

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain

---

📖 **Anglický originál a plná specifikace:** [MP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mp/)
