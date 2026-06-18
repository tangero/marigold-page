---
slug: "utf-16"
url: "/mobilnisite/slovnik/utf-16/"
type: "slovnik"
title: "UTF-16 – Unicode Transformation Format - 16-bit"
date: 2025-01-01
abbr: "UTF-16"
fullName: "Unicode Transformation Format - 16-bit"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/utf-16/"
summary: "UTF-16 je kódování znaků s proměnnou délkou pro Unicode, které většinu znaků reprezentuje jako jedinou 16bitovou kódovou jednotku a ostatní jako pár (náhradní pár). Je základním kódováním pro reprezen"
---

UTF-16 je kódování znaků s proměnnou délkou pro Unicode, používané ve službách 3GPP jako je zasílání zpráv, které většinu znaků reprezentuje jedním 16bitovým jednotkou a ostatní pomocí náhradního páru (surrogate pair).

## Popis

UTF-16 je standard kódování znaků definovaný konsorciem Unicode a přijatý 3GPP pro reprezentaci textových dat. Jde o kódování s proměnnou šířkou, což znamená, že může k reprezentaci jednoho znaku použít jednu nebo dvě 16bitové kódové jednotky (každá o 2 bytech). Pro znaky v základní vícejazyčné rovině (BMP), která zahrnuje většinu běžných znaků, postačuje jedna 16bitová kódová jednotka. Znaky mimo BMP, jako jsou některé emotikony nebo historická písma, jsou reprezentovány pomocí páru 16bitových kódových jednotek známého jako náhradní pár (surrogate pair). Tento pár se skládá z vysokého náhradníku (v rozsahu 0xD800–0xDBFF) a nízkého náhradníku (0xDC00–0xDFFF). Kódování může být uloženo v pořadí bajtů big-endian nebo little-endian a na začátku datového proudu se často používá značka pořadí bajtů (BOM) k určení tohoto pořadí.

V rámci architektury 3GPP je UTF-16 specifikováno primárně v kontextu multimediálních služeb. Specifikace jako 3GPP TS 26.245 (Transparent end-to-end packet-switched streaming service; Protocols and codecs) a TS 26.246 (Transparent end-to-end packet-switched streaming service; 3GPP file format) definují jeho použití pro textové stopy, titulky a metadata ve streamovaných a souborových médiích. Zajišťuje, že text spojený s multimediálním obsahem může reprezentovat globální sadu znaků, čímž podporuje internacionalizaci.

Role tohoto kódování je klíčová pro zajištění interoperability a správného zobrazení textu na různých zařízeních a sítích. Když 3GPP-kompatibilní zařízení přijme multimediální soubor nebo stream, musí správně dekódovat text kódovaný v UTF-16 na základě specifikovaného nebo detekovaného pořadí bajtů. Použití UTF-16, na rozdíl od jednodušších kódování jako ASCII, umožňuje službám podporovat obrovské množství jazyků a symbolů, což je nezbytné pro globální telekomunikace. Jeho implementace je řešena na aplikační a prezentační vrstvě protokolového zásobníku, což abstrahuje složitost od transportních protokolů nižších vrstev.

## K čemu slouží

UTF-16 bylo vytvořeno, aby poskytlo praktickou kódovací formu pro celou znakovou sadu Unicode, vyvažující efektivitu a jednoduchost pro široké spektrum znaků. Předchozí kódování jako ASCII nebo rodina ISO-8859 byla omezena na 7 nebo 8 bitů a pokrývala pouze malou podmnožinu světových písemných systémů. Standard Unicode si kladl za cíl vytvořit univerzální znakovou sadu, ale pro ukládání a přenos bylo potřeba efektivní kódování. UTF-16 tento problém řeší použitím 16bitových kódových jednotek jako přirozené velikosti pro mnoho výpočetních systémů, což umožňuje přímou reprezentaci většiny běžných znaků bez režie převodu.

V kontextu 3GPP bylo přijetí UTF-16, počínaje Release 8, hnací silou potřeby multimediálních služeb (jako je streamování a zasílání zpráv) podporovat globální text. Jak se mobilní služby rozšiřovaly mezinárodně, stala se podpora různorodých jazyků a symbolů (včetně emotikonů) požadavkem. UTF-16 poskytlo standardizovaný způsob, jak tento text zakódovat v multimediálních kontejnerech a protokolech pro zasílání zpráv, a zajistilo, aby japonský uživatel mohl přijmout zprávu s arabským písmem nebo video s korejskými titulky bez ztráty nebo poškození dat. Vyřešilo tak problém nekompatibilních starších kódování, který sužoval ranou digitální komunikaci.

Motivace byla také v souladu se širšími průmyslovými trendy směrem k Unicode. Specifikací UTF-16 v klíčových multimediálních specifikacích zajistilo 3GPP interoperabilitu s dalšími standardy (jako jsou formáty médií založené na [ISO](/mobilnisite/slovnik/iso/)) a výpočetními platformami, které běžně používají UTF-16 nativně (např. Windows [API](/mobilnisite/slovnik/api/), Java). Tím se snížila složitost implementace pro výrobce zařízení a poskytovatele služeb a poskytl se konzistentní základ pro zpracování textu napříč ekosystémem.

## Klíčové vlastnosti

- Kódování s proměnnou šířkou používající 16bitové kódové jednotky
- Podporuje celý repertoár znaků Unicode pomocí náhradních párů pro znaky mimo základní vícejazyčnou rovinu (BMP)
- Může být uloženo v pořadí bajtů big-endian nebo little-endian, často označené značkou pořadí bajtů (BOM)
- Specifikováno v 3GPP pro text v multimediálních službách (např. titulky, metadata)
- Umožňuje internacionalizaci reprezentací širokého spektra globálních písem a symbolů
- Poskytuje rovnováhu mezi paměťovou efektivitou a jednoduchostí zpracování pro běžné znaky

## Související pojmy

- [UTF-8 – Unicode Transformation Format - 8-bit](/mobilnisite/slovnik/utf-8/)

## Definující specifikace

- **TS 26.245** (Rel-19) — 3GPP Timed Text Format Specification
- **TS 26.246** (Rel-19) — 3GPP SMIL Language Profile Specification

---

📖 **Anglický originál a plná specifikace:** [UTF-16 na 3GPP Explorer](https://3gpp-explorer.com/glossary/utf-16/)
