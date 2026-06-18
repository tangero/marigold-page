---
slug: "ucs-2"
url: "/mobilnisite/slovnik/ucs-2/"
type: "slovnik"
title: "UCS-2 – Universal Character Set (the two octet form)"
date: 2025-01-01
abbr: "UCS-2"
fullName: "Universal Character Set (the two octet form)"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ucs-2/"
summary: "Pevně šířková, 16bitová znaková kódovací forma standardu UCS/Unicode. Každý znak je reprezentován přesně dvěma oktety (16 bitů), pokrývající základní vícejazyčnou rovinu (BMP). Bylo široce používáno v"
---

UCS-2 je pevně šířková, 16bitová znaková kódování, kde je každý znak reprezentován přesně dvěma oktety, pokrývající základní vícejazyčnou rovinu Unicode (BMP), a bylo široce používáno v raných systémech 3GPP pro SMS a signalizaci.

## Popis

UCS-2, což znamená 'Universal Character Set - 2 oktetová forma', je pevně šířkové znakové kódování specifikované v [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 10646. Přímo reprezentuje kódový bod každého znaku v repertoáru [UCS](/mobilnisite/slovnik/ucs/) pomocí přesně dvou oktetů (16 bitů). Toto kódování je omezeno na reprezentaci znaků ze základní vícejazyčné roviny (BMP) Unicode/UCS, která zahrnuje většinu běžně používaných znaků moderních jazyků, ale vylučuje doplňkové znaky, jako jsou mnohé historické písma, symboly a emoji, které se nacházejí v jiných rovinách. V systémech 3GPP bylo UCS-2 historicky implementováno jako specifické kódování pro text, zejména v kontextu služby krátkých textových zpráv ([SMS](/mobilnisite/slovnik/sms/)) a některých signalizačních parametrů.

Technicky je fungování UCS-2 přímočaré: posloupnost 16bitových kódových jednotek přímo odpovídá posloupnosti znaků z BMP. Například latinskému velkému písmenu 'A' (U+0041) odpovídá dvouoktetová sekvence 0x00 0x41. Tato vlastnost pevné šířky zjednodušovala zpracování v raných systémech, protože operace s řetězci, jako je počítání znaků nebo indexování, mohly být prováděny přímo na základě pozice bajtů. V rámci 3GPP specifikace, jako jsou ty pro službu multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)) a paketově spínanou streamovací službu ([PSS](/mobilnisite/slovnik/pss/)), odkazovaly na UCS-2 jako na přípustné nebo požadované znakové kódování pro obsah a metadata, aby podpořily širší škálu jazyků než původní 7bitová abeceda GSM.

Role UCS-2 se však vyvinula. Jeho hlavním omezením je neschopnost zakódovat jakýkoli znak mimo BMP (kódové body nad U+FFFF). Pro řešení tohoto problému bylo vyvinuto kódování [UTF-16](/mobilnisite/slovnik/utf-16/) s proměnnou délkou, které je zpětně kompatibilní s UCS-2 pro znaky z BMP, ale pro reprezentaci doplňkových znaků používá náhradní dvojice (dvě 16bitové kódové jednotky). V důsledku toho se v moderních specifikacích 3GPP termín 'UCS-2' často používá historicky nebo zaměnitelně s kódováním UTF-16BE (Big Endian), pokud jsou použity pouze znaky z BMP. Pro skutečně univerzální pokrytí je nyní doporučovaným kódováním UTF-16, ale porozumění UCS-2 zůstává důležité pro interoperabilitu se staršími zařízeními a sítěmi, které striktně implementovaly pevnou dvouoktetovou formu.

## K čemu slouží

UCS-2 bylo zavedeno, aby poskytlo významný upgrade oproti omezeným 7bitovým a 8bitovým znakovým sadám používaným v raném GSM. Řešilo bezprostřední problém podpory široké škály mezinárodních jazyků, včetně těch s rozsáhlými znakovými sadami, jako je čínština, japonština a korejština (CJK), v rámci mobilních služeb zasílání zpráv, jako je [SMS](/mobilnisite/slovnik/sms/). Před UCS-2 bylo odeslání SMS v těchto jazycích nemožné nebo vyžadovalo proprietární, neinteroperabilní rozšíření.

Motivací pro jeho přijetí ve specifikacích 3GPP Release 8 a souvisejících specifikacích bylo stanovit konkrétní, implementovatelnou podmnožinu plného UCS pro použití v prostředích s omezenou šířkou pásma a výpočetním výkonem. UCS-2 nabízelo dobrý kompromis: podporovalo desetitisíce znaků s jednoduchým, pevně šířkovým formátem, který bylo snazší zpracovat ve firmwaru zařízení a síťové signalizaci než kódování s proměnnou délkou. Umožnilo první vlnu skutečné internacionalizace pro textové mobilní služby.

Omezení UCS-2 se však stala zřejmými s rostoucí potřebou podpory ještě většího množství znaků (např. pro starověká písma, specializované symboly a později emoji). Nemohlo reprezentovat znaky mimo BMP, což vedlo k vývoji a následné preferenci UTF 16. Zatímco UCS-2 tedy splnilo kritický přechodový účel při globalizaci mobilní textové komunikace, jeho vývoj byl hnán potřebou skutečně úplného znakového kódování, což z něj činí základní, ale převážně historický krok v textové strategii 3GPP.

## Klíčové vlastnosti

- Pevně šířkové kódování používající přesně dva oktety (16 bitů) na znak
- Kóduje znaky ze základní vícejazyčné roviny Unicode (BMP, rovina 0)
- Jednoduchý model zpracování díky konzistentní velikosti znaků
- Historicky používáno pro SMS a MMS k podpoře mezinárodních znakových sad
- Zpětně kompatibilní základ pro schéma kódování UTF-16
- Definováno se specifickým pořadím bajtů (často Big Endian) v přenosu 3GPP

## Související pojmy

- [UCS – Universal Multiple-Octet Coded Character Set](/mobilnisite/slovnik/ucs/)
- [UTF-16 – Unicode Transformation Format - 16-bit](/mobilnisite/slovnik/utf-16/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.246** (Rel-19) — 3GPP SMIL Language Profile Specification

---

📖 **Anglický originál a plná specifikace:** [UCS-2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ucs-2/)
