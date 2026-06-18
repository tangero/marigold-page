---
slug: "ucs"
url: "/mobilnisite/slovnik/ucs/"
type: "slovnik"
title: "UCS – Universal Multiple-Octet Coded Character Set"
date: 2025-01-01
abbr: "UCS"
fullName: "Universal Multiple-Octet Coded Character Set"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ucs/"
summary: "Standardizovaný systém kódování znaků definovaný normou ISO/IEC 10646 a přijatý organizací 3GPP. Poskytuje univerzální repertoár znaků pro reprezentaci textu v globálních službách, což umožňuje konzis"
---

UCS je standardizovaný systém kódování znaků definovaný normou ISO/IEC 10646 a přijatý organizací 3GPP, který poskytuje univerzální repertoár znaků pro konzistentní globální reprezentaci textu v mobilních službách.

## Popis

Universal Multiple-Octet Coded Character Set (UCS), standardizovaný společně jako [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 10646, je mezinárodní norma definující komplexní, univerzální znakovou sadu navrženou tak, aby zahrnovala prakticky všechny znaky používané ve světových psaných jazycích, stejně jako symboly a speciální znaky. V ekosystému 3GPP je UCS přijata jako základní kódování znaků pro textové služby a prvky uživatelského rozhraní za účelem zajištění globální interoperability. Technicky UCS definuje rozsáhlý kódový prostor, kde je každému znaku přiřazen jedinečný číselný kódový bod. Primárními kódovacími formami jsou [UCS-2](/mobilnisite/slovnik/ucs-2/) (používající 2 oktety na znak) a UCS-4/UTF-32 (používající 4 oktety), které poskytují reprezentaci s pevnou délkou. Častěji používané kódování s proměnnou délkou odvozené od UCS je však [UTF-8](/mobilnisite/slovnik/utf-8/), které je zpětně kompatibilní s ASCII.

Ve specifikacích 3GPP funguje UCS jako povinná znaková sada pro různé protokoly a rozhraní. Například v IP Multimedia Subsystem (IMS) využívají protokol Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a rozhraní Cx/Dx založená na Diameteru UCS (často ve formě kódované UTF-8) pro přenos textových informací, jako jsou uživatelské identity (Public User Identities), zobrazovaná jména a parametry služby. To zajišťuje, že jméno japonského uživatele může být správně zobrazeno na zařízení německého uživatele a naopak, bez poškození nebo nahrazení zástupnými znaky. Síťové prvky, jako jsou Application Servers ([AS](/mobilnisite/slovnik/as/)), Proxies a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), zpracovávají tyto textové řetězce na základě standardu UCS.

Role UCS v síti je klíčová pro globalizaci a konzistenci služeb. Je základem pro Multimedia Messaging Service ([MMS](/mobilnisite/slovnik/mms/)), SMS s rozšířenými znakovými sadami a uživatelská síťová managementová rozhraní. Standardizací na UCS 3GPP eliminuje nejednoznačnost a nekompatibilitu více regionálních nebo proprietárních kódování znaků (jako jsou různé zastaralé 7bitové abecedy GSM). Poskytuje jediný rozšiřitelný rámec, který může pojmout nové znaky a písma, jak jsou přidávány do standardu Unicode (který je synchronizován s ISO/IEC 10646). Tento technický základ je zásadní pro vytváření skutečně globálních telekomunikačních služeb, které jsou kulturně a jazykově inkluzivní.

## K čemu slouží

UCS byla přijata organizací 3GPP k vyřešení základního problému nekompatibilních a omezených kódování znaků v raných mobilních telekomunikačních systémech. Před jejím rozšířeným přijetím služby jako SMS primárně používaly národní výchozí 7bitovou abecedu (podle GSM 03.38), která byla nedostatečná pro reprezentaci znaků z mnoha jazyků, včetně většiny východoasijských písem, a vedla k fragmentovaným uživatelským zkušenostem. Růst globálního roamingu a multimediálních služeb si vyžádal jednotný způsob zpracování textu.

Motivace pro integraci UCS do standardů 3GPP, počínaje Release 8, byla hnána evolucí směrem k plně IP sítím a IMS. IMS si kladla za cíl poskytovat bohaté, interoperabilní multimediální služby (hlas, video, text) přes IP, což vyžadovalo znakovou sadu schopnou podporovat jakýkoli jazyk pro uživatelské identifikátory, informace o stavu (presence) a instant messaging. Přijetí mezinárodně uznávaného standardu ISO/IEC 10646 tuto schopnost poskytlo a zajistilo síť odolnou vůči potřebě podpory nových jazyků a emotikonů.

Dále UCS řešila omezení předchozích přístupů tím, že poskytla jediný, jednoznačný kódový bod pro každý znak, oddělující identitu znaku od jeho vizuální reprezentace (glyfu). Toto oddělení je klíčové pro síťové prvky, které potřebují ukládat, směrovat a zpracovávat text bez nutnosti rozumět jeho vykreslování. Vyřešilo problémy se ztrátou dat během komunikace mezi sítěmi nebo zařízeními a stalo se základním kamenem pro umožnění rich communication services (RCS) a globální interoperability aplikací v rámci 3GPP.

## Klíčové vlastnosti

- Univerzální repertoár pokrývající znaky všech hlavních světových písem, symboly a emotikony
- Definuje jedinečné kódové body pro každý znak, nezávisle na platformě nebo jazyku
- Základ pro běžné kódovací formy jako UTF-8, UTF-16 a UTF-32
- Povinná znaková sada pro protokoly 3GPP IMS (SIP, Diameter) a uživatelské identity
- Umožňuje konzistentní zobrazení a zpracování textu v globálně nasazených sítích a zařízeních
- Synchronizována se standardem Unicode, což zajišťuje průběžné přidávání nových znaků

## Související pojmy

- [UTF-8 – Unicode Transformation Format - 8-bit](/mobilnisite/slovnik/utf-8/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 26.226** (Rel-19) — Cellular Text Telephone Modem (CTM)
- **TS 26.230** (Rel-19) — CTM C Code Implementation for Text Transmission
- **TS 29.229** (Rel-19) — Diameter Protocol for Cx/Dx Interfaces
- **TS 29.329** (Rel-19) — Diameter Protocol for Sh Interface
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [UCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ucs/)
