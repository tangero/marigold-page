---
slug: "xer"
url: "/mobilnisite/slovnik/xer/"
type: "slovnik"
title: "XER – XML Encoding Rules"
date: 2025-01-01
abbr: "XER"
fullName: "XML Encoding Rules"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/xer/"
summary: "XER je soubor standardizovaných pravidel pro kódování datových struktur Abstract Syntax Notation One (ASN.1) do formátu XML. Poskytuje čitelnou a platformně nezávislou XML reprezentaci zpráv a dat pro"
---

XER je soubor standardizovaných pravidel pro kódování datových struktur ASN.1 do čitelných a platformně nezávislých XML formátů, používaných pro rozhraní správy a výměnu dat v telekomunikačních sítích.

## Popis

[XML](/mobilnisite/slovnik/xml/) Encoding Rules (XER) je standardizovaná metoda kódování definovaná [ITU-T](/mobilnisite/slovnik/itu-t/) a přijatá ve specifikacích 3GPP. Určuje, jak se datové typy a hodnoty definované pomocí Abstract Syntax Notation One (ASN.1) převádějí na ekvivalentní XML dokument. ASN.1 je formální notace používaná k definování struktury protokolových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)), konfiguračních dat a informací o správě způsobem nezávislým na konkrétním programovacím jazyku nebo hardwarové platformě. Zatímco jiná pravidla kódování ASN.1, jako Basic Encoding Rules ([BER](/mobilnisite/slovnik/ber/)) nebo Packed Encoding Rules ([PER](/mobilnisite/slovnik/per/)), vytvářejí kompaktní binární výstupy optimalizované pro přenos, XER produkuje podrobný textový XML výstup.

Proces kódování se řídí přesným mapováním definovaným v ITU-T Rec. X.693. Každý typ ASN.1 (např. SEQUENCE, CHOICE, INTEGER, OCTET STRING) má odpovídající XML reprezentaci. Například ASN.1 SEQUENCE se stane XML elementem, přičemž její pole jsou reprezentována jako podřízené elementy nebo atributy. Výsledný XML dokument je dobře formován a může být volitelně validován proti XML schématu ([XSD](/mobilnisite/slovnik/xsd/)), které je mechanicky odvozeno z původních definic ASN.1. To umožňuje, aby data definovaná v rigorózním, telekomunikačně prověřeném formalismu ASN.1 mohla být manipulována, ukládána a přenášena pomocí všudypřítomných XML nástrojů a knihoven.

V systémech 3GPP se XER primárně používá v rozhraních pro správu a konfiguraci, zejména v rámci domény Network Management ([NM](/mobilnisite/slovnik/nm/)) a pro rozhraní Itf-N. Protokoly jako specifická verze Simple Network Management Protocol ([SNMP](/mobilnisite/slovnik/snmp/)) pro 3GPP nebo formát souboru Bulk CM (Configuration Management) mohou využívat XER pro kódování informací o správě. Čitelná povaha XML usnadňuje ladění, manuální kontrolu konfiguračních výpisů a testování interoperability. Dále umožňuje integraci s podnikovými IT systémy a webovými službami, které nativně zpracovávají XML, čímž překlenuje propast mezi telekomunikačně specifickými OSS/BSS a širšími IT ekosystémy.

## K čemu slouží

XER byl vyvinut pro uspokojení potřeby čitelného, textového kódovacího formátu pro data ASN.1, který doplňuje existující binární kódování jako BER a PER. Binární kódování, ačkoli jsou vysoce efektivní pro přenos po rádiovém rozhraní a strojové zpracování, jsou neprůhledná a pro inženýry obtížně kontrolovatelná, laditelná nebo ručně vytvářená během vývoje a testování. To vytvářelo bariéru pro úkoly provozu, správy a údržby (OAM), kde bylo třeba prohlížet konfigurační soubory nebo hlášení o poruchách.

Vzestup XML jako univerzálního formátu pro výměnu dat na počátku 21. století poskytl impuls pro jeho přijetí v telekomunikačních standardech. XER tento problém vyřešil tím, že umožnil reprezentaci bohatých, přesně definovaných datových struktur ASN.1 – již široce používaných v protokolech 3GPP pro signalizaci a správu – ve formátu XML. To umožnilo spojit to nejlepší z obou světů: formální přísnost a jednoznačnou definici ASN.1 spolu s ekosystémem nástrojů, čitelností a kompatibilitou s IT prostředím, které poskytuje XML. Jeho zavedení v 3GPP Release 8 usnadnilo lepší interoperabilitu v rovině správy, snazší integraci s OSS systémy založenými na XML a zjednodušilo testování shody protokolů prostřednictvím čitelných tras zpráv.

## Klíčové vlastnosti

- Transformuje definice typů a hodnot ASN.1 na standardní XML dokumenty
- Produkuje čitelný, textový výstup pro ladění a kontrolu
- Umožňuje validaci zakódovaných dat pomocí XML schématu (XSD) odvozeného z ASN.1
- Podporuje jak kanonickou (striktní), tak základní (flexibilnější) variantu kódování
- Usnadňuje integraci telekomunikačních dat správy s IT systémy založenými na XML
- Definováno ITU-T X.693 a sladěno s normami ISO/IEC

## Související pojmy

- [BER – Basic Encoding Rules](/mobilnisite/slovnik/ber/)
- [PER – Printable character Error Rate](/mobilnisite/slovnik/per/)

## Definující specifikace

- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification

---

📖 **Anglický originál a plná specifikace:** [XER na 3GPP Explorer](https://3gpp-explorer.com/glossary/xer/)
