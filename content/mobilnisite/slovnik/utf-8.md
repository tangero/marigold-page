---
slug: "utf-8"
url: "/mobilnisite/slovnik/utf-8/"
type: "slovnik"
title: "UTF-8 – Unicode Transformation Format - 8-bit"
date: 2025-01-01
abbr: "UTF-8"
fullName: "Unicode Transformation Format - 8-bit"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/utf-8/"
summary: "UTF-8 je proměnlivě dlouhé kódování znaků pro Unicode, které pro jeden znak používá jeden až čtyři 8bitové bajty. Je široce používáno v 3GPP pro zprávové, presence a multimediální služby díky zpětné k"
---

UTF-8 je proměnlivě dlouhé kódování znaků pro Unicode, které pro jeden znak používá jeden až čtyři bajty a je v rámci 3GPP široce používáno pro zprávové a multimediální služby díky své kompatibilitě s ASCII a efektivitě.

## Popis

UTF-8 je kódování znaků, které mapuje body kódu Unicode na sekvenci 8bitových bajtů. Je proměnlivé šířky, k reprezentaci znaku používá 1 až 4 bajty. Znaky ASCII (U+0000 až U+007F) jsou zakódovány jako jeden bajt, shodně se svou reprezentací v ASCII, což zajišťuje plnou zpětnou kompatibilitu. Znaky mimo tento rozsah používají vícebajtové sekvence, kde první bajt udává počet navazujících bajtů a navazující bajty mají specifický bitový vzor. Tento návrh umožňuje efektivní zpracování a vyhýbá se problémům s pořadím bajtů, protože UTF-8 je na pořadí bajtů nezávislé.

Ve specifikacích 3GPP je UTF-8 definováno v mnoha technických specifikacích (TS) pro různé služby. Například TS 26.140 (Multimediální zprávová služba; Mediální formáty a kodeky) a TS 26.141 (Služba presence; Datové formáty) definují jeho použití pro text ve zprávách a informacích o přítomnosti. TS 26.234 (Transparentní koncově koncová paketově spínaná streamovací služba; Protokoly) a TS 26.245/246/247 (vztahující se ke streamování a formátu souborů) specifikují UTF-8 pro metadata, popis relace a textové stopy. Toto kódování se používá v protokolech jako [SIP](/mobilnisite/slovnik/sip/), [HTTP](/mobilnisite/slovnik/http/) a v multimediálních kontejnerech, aby bylo zajištěno univerzální interpretování textových dat.

Kódování funguje tak, že rozdělí hodnotu bodu kódu Unicode na bity a distribuuje je podle definovaného vzoru napříč bajty. Znak s jedním bajtem má nejvyšší bit nastaven na 0. U vícebajtových znaků má první bajt několik nejvyšších bitů nastaveno na 1 následovaných 0, což udává celkový počet bajtů, a navazující bajty začínají vzorem '10'. Tato struktura umožňuje snadnou validaci a parsování. V rámci síťové architektury 3GPP je text kódovaný v UTF-8 typicky přenášen v užitečném zatížení protokolů aplikační vrstvy. Jeho role je klíčová pro služby vyžadující výměnu textu, jako jsou [MMS](/mobilnisite/slovnik/mms/), IMS messaging a streamovací služby, protože podporuje globální jazyky a zároveň je efektivní pro text s vysokým podílem ASCII a kompatibilní s existující internetovou infrastrukturou.

## K čemu slouží

UTF-8 bylo vyvinuto, aby poskytlo kódování Unicode, které je zpětně kompatibilní s široce používaným standardem ASCII a efektivní pro síťový přenos. Před Unicode způsobovala více nekompatibilních kódování (jako řada ISO-8859) problémy s interoperabilitou, zejména na internetu. Vytvoření UTF-8 Kenem Thompsonem a Robem Pikem nabídlo řešení, kde text v ASCII zůstává platným UTF-8, což usnadnilo adopci. Jeho návrh minimalizuje režii pro angličtinu a další jazyky s latinkou, a přitom je schopné zakódovat všechny znaky Unicode.

3GPP přijalo UTF-8 počínaje Release 8, aby se sladilo s internetovými protokoly a zajistilo bezproblémovou integraci s webovými službami. Jak se mobilní sítě vyvíjely k podpoře služeb založených na IP (IMS, streamování), stalo se používání UTF-8 nezbytným pro protokoly jako [SIP](/mobilnisite/slovnik/sip/) a [HTTP](/mobilnisite/slovnik/http/), které dominují internetové komunikaci. Vyřešilo problém s poškozením textu při výměně zpráv mezi různými systémy a regiony. Pro multimediální služby umožnilo UTF-8 efektivní kódování metadat a titulků, což bylo zvláště výhodné pro služby, kde je text převážně v ASCII, a snižovalo tak šířku pásma ve srovnání s kódováním s pevnou šířkou, jako je [UTF-16](/mobilnisite/slovnik/utf-16/).

Motivace byla hnána potřebou univerzálního, efektivního a robustního kódování textu pro globální mobilní služby. Bajtově orientovaná povaha UTF-8 se vyhýbá problémům s pořadím bajtů a zjednodušuje zpracování. Specifikací UTF-8 v klíčových specifikacích zajistilo 3GPP, že mobilní zařízení a síťové prvky mohou interoperovat se servery a službami na širším internetu, čímž podpořilo trend směrem k plně IP sítím a pokročilým komunikačním službám.

## Klíčové vlastnosti

- Proměnlivě široké kódování používající 1 až 4 bajty na znak
- Plná zpětná kompatibilita s ASCII (ASCII je podmnožinou UTF-8)
- Nezávislost na pořadí bajtů, což ve většině kontextů eliminuje potřebu značek pořadí bajtů (BOM)
- Široce používáno v 3GPP pro zprávové služby (MMS), presence, streamovací protokoly a metadata
- Efektivní pro text s mnoha znaky ASCII, což snižuje velikost oproti UTF-16 pro takový obsah
- Návrh s vlastní synchronizací umožňuje obnovu z částečných datových proudů a snadnou validaci

## Související pojmy

- [UTF-16 – Unicode Transformation Format - 16-bit](/mobilnisite/slovnik/utf-16/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.245** (Rel-19) — 3GPP Timed Text Format Specification
- **TS 26.246** (Rel-19) — 3GPP SMIL Language Profile Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP

---

📖 **Anglický originál a plná specifikace:** [UTF-8 na 3GPP Explorer](https://3gpp-explorer.com/glossary/utf-8/)
