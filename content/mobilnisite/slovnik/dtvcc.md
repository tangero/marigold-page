---
slug: "dtvcc"
url: "/mobilnisite/slovnik/dtvcc/"
type: "slovnik"
title: "DTVCC – DTV Closed Caption"
date: 2025-01-01
abbr: "DTVCC"
fullName: "DTV Closed Caption"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dtvcc/"
summary: "DTVCC je systém skrytých titulků specifikovaný pro služby digitální televize (Digital TeleVision) v sítích 3GPP. Poskytuje textové překryvy pro dialog a popisy zvuku, aby byl video obsah přístupný pro"
---

DTVCC je systém skrytých titulků pro služby digitální televize (Digital TeleVision) v sítích 3GPP, který poskytuje textové překryvy pro dialog a popisy zvuku, aby byl video obsah přístupný pro diváky se sluchovým postižením.

## Popis

[DTV](/mobilnisite/slovnik/dtv/) Closed Caption (DTVCC) je standardizovaný mechanismus pro doručování dat skrytých titulků jako součást služeb digitální televize 3GPP. Skryté titulky jsou textovou reprezentací zvukového obsahu (dialog, zvukové efekty) synchronizovanou s videem, což je klíčové pro přístupnost a vícejazyčnou podporu. V rámci architektury 3GPP je DTVCC definováno ve specifikaci požadavků na služby TS 26.953, která podrobně popisuje, jak jsou data titulků zakódována, multiplexována do mediálního proudu a zobrazována na přijímacích zařízeních.

Technická implementace zahrnuje vložení dat titulků do transportního proudu videa. Pro služby DTV využívající eMBMS jsou titulky typicky přenášeny jako časované textové stopy podle formátů jako 3GPP Timed Text (3GPP [TT](/mobilnisite/slovnik/tt/)) nebo adaptací jiných standardů jako CEA-708. Data titulků jsou paketizována spolu s video a audio snímky, často za použití formátů [MPEG-2](/mobilnisite/slovnik/mpeg-2/) Transport Stream (TS) nebo Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Synchronizace je dosažena pomocí časových značek mediální prezentace, což zajišťuje, že se titulky objeví ve správných okamžicích během přehrávání.

Klíčové komponenty zahrnují kodér titulků ve vysílacím zdroji, který převádí text a časové informace na standardizovaný bitový proud, a dekodér titulků v uživatelském zařízení (UE), který data extrahuje, zpracuje a překryje text na video. Specifikace pokrývá aspekty jako znakové kódování (např. [UTF-8](/mobilnisite/slovnik/utf-8/)), stylování (písmo, barva, pozice) a řídicí kódy pro zobrazovací okna. DTVCC se integruje do širšího životního cyklu služby DTV, od přípravy obsahu v Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) po dekódování v mediálním přehrávači mobilního zařízení, čímž zajišťuje konzistentní funkci přístupnosti napříč různými sítěmi a zařízeními.

## K čemu slouží

DTVCC bylo vytvořeno za účelem zavedení a standardizace skrytých titulků pro služby mobilní digitální televize, aby se splnily právní a regulační požadavky na přístupnost (např. pro diváky se sluchovým postižením) a zlepšil se uživatelský zážitek díky titulkům. Bez jednotného standardu by byly implementace titulků roztříštěné, což by vedlo k problémům s kompatibilitou napříč zařízeními a sítěmi.

Motivace vychází z potřeby učinit vysílací služby 3GPP inkluzivními a v souladu se zákony o přístupnosti v mnoha regionech. Předchozí přístupy spoléhaly na proprietární nebo neinteroperabilní metody titulkování, což bránilo jejich širokému přijetí. Specifikací DTVCC v rámci 3GPP je zajištěno, že vysílatelé mohou efektivně doručovat titulky pomocí stejné infrastruktury eMBMS a přijímače je mohou jednotně dekódovat. To také podporuje vícejazyčné publikum umožněním více jazykových stop, čímž rozšiřuje atraktivitu služby.

## Klíčové vlastnosti

- Standardizované kódování pro data skrytých titulků v rámci proudů 3GPP DTV
- Podporuje synchronizaci s videem/zvukem pomocí mediálních časových značek
- Umožňuje více jazykových stop a možnosti stylování (písmo, barva)
- Integruje se s transportními protokoly eMBMS jako MPEG-2 TS a DASH
- Poskytuje soulad s požadavky na přístupnost pro uživatele se sluchovým postižením
- Usnadňuje interoperabilitu napříč různými zařízeními a sítěmi

## Související pojmy

- [DTV – Digital TeleVision](/mobilnisite/slovnik/dtv/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [DTVCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtvcc/)
