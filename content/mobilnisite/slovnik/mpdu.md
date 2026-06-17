---
slug: "mpdu"
url: "/mobilnisite/slovnik/mpdu/"
type: "slovnik"
title: "MPDU – MAC Protocol Data Unit"
date: 2025-01-01
abbr: "MPDU"
fullName: "MAC Protocol Data Unit"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mpdu/"
summary: "Protokolová datová jednotka (PDU) na vrstvě řízení přístupu k médiu (MAC), představující datový paket vyměňovaný mezi partnerskými entitami MAC. V kontextu 3GPP často označuje strukturovanou datovou j"
---

MPDU je protokolová datová jednotka (PDU) vrstvy MAC, strukturovaný paket obsahující hlavičku, volitelná data, výplň a CRC, který představuje základní jednotku pro přenos dat a multiplexování logických kanálů mezi partnerskými entitami MAC.

## Popis

[MAC](/mobilnisite/slovnik/mac/) protokolová datová jednotka (MPDU) je základním konceptem v komunikačních protokolech, představuje paket nebo rámec, který je zpracováván a přenášen vrstvou řízení přístupu k médiu (MAC). V architektuře 3GPP, zejména pro LTE a 5G NR, je vrstva MAC podsložkou protokolové vrstvy 2 (spolu s RLC a PDCP) jak v uživatelském zařízení (UE), tak v základnové stanici ([eNB](/mobilnisite/slovnik/enb/)/gNB). MPDU je datová jednotka, kterou vrstva MAC předává fyzické vrstvě pro přenos přes rozhraní rádiového přenosu, nebo kterou od fyzické vrstvy přijímá ke zpracování. Zapouzdřuje data z vyšších vrstev (MAC SDU, což jsou RLC PDU) přidáním MAC hlavičky obsahující řídicí informace nezbytné pro přijímající entitu MAC ke správnému zpracování paketu.

Z architektonického hlediska je MPDU vytvářena vysílající entitou MAC. Vrstva MAC přijímá datové jednotky služby (SDU) od vrstvy řízení rádiového spoje (RLC) prostřednictvím logických kanálů. Vrstva MAC vykonává funkce jako je prioritizace logických kanálů, multiplexování SDU z různých logických kanálů do jednoho transportního bloku a přidání MAC hlavičky. MAC hlavička se skládá z jednoho nebo více podhlaviček, z nichž každá odpovídá jednomu MAC SDU nebo řídicímu prvku MAC ([CE](/mobilnisite/slovnik/ce/)). Každá podhlavička obsahuje pole jako identifikátor logického kanálu ([LCID](/mobilnisite/slovnik/lcid/)), který identifikuje logický kanál nebo typ řídicí informace, a pole Délka (L) udávající velikost odpovídajícího SDU. Řídicí prvky MAC slouží pro řídicí signalizaci v pásmu, například pro požadavky na plánování, hlášení o stavu vyrovnávací paměti nebo příkazy časového předstihu. Za hlavičkou a SDU/CE může následovat výplň pro zarovnání MPDU na požadovanou velikost a může být připojen [CRC](/mobilnisite/slovnik/crc/) (Cyclic Redundancy Check) pro detekci chyb na fyzické vrstvě.

Jak to funguje: vrstva MAC v vysílači sestaví MPDU na základě přidělení zdrojů přijatého od fyzické vrstvy (prostřednictvím [DCI](/mobilnisite/slovnik/dci/) na [PDCCH](/mobilnisite/slovnik/pdcch/)/[MPDCCH](/mobilnisite/slovnik/mpdcch/)). Plánovač v základnové stanici určuje velikost transportního bloku (který nese jednu MPDU) a přidělené zdroje. Entita MAC vybere, které logické kanály obsloužit, v případě potřeby segmentuje nebo spojuje RLC PDU (ačkoliv segmentace je primárně funkcí RLC v LTE/NR) a vytvoří MPDU s příslušnou hlavičkou. Tato MPDU je poté předána fyzické vrstvě jako součást transportního bloku, který prochází kanálovým kódováním, modulací a mapováním na fyzické zdroje. Na přijímací straně fyzická vrstva dekóduje transportní blok a předá MPDU vrstvě MAC. Přijímající entita MAC analyzuje MAC hlavičku pomocí hodnot LCID, aby demultiplexovala SDU a doručila je správným entitám RLC nebo zpracovala případné řídicí prvky MAC. MPDU je tedy nástrojem pro veškerá data uživatelské roviny a kritickou řídicí signalizaci vrstvy MAC přes rozhraní rádiového přenosu, což umožňuje efektivní multiplexování, zpracování priorit a spolehlivý přenos dat.

## K čemu slouží

Koncept MPDU existuje jako základní část vrstvového návrhu protokolů a poskytuje standardizovaný formát pro výměnu dat na vrstvě MAC. V bezdrátových systémech jako 3GPP LTE a NR je vrstva MAC zodpovědná za kritické funkce, jako je mapování mezi logickými kanály (které reprezentují různé typy datových toků, např. hlas, video, signalizace) a transportními kanály (fyzickými zdroji), plánování a zpracování priorit. Struktura MPDU s hlavičkou obsahující LCID umožňuje vrstvě MAC efektivně multiplexovat data z více logických kanálů (např. SRB1 pro signalizaci RRC, DRB pro uživatelská data) do jednoho transportního bloku pro přenos a na přijímací straně je demultiplexovat. Tím řeší problém správy více souběžných datových toků s různými požadavky na QoS přes sdílený rádiový zdroj.

Historicky se formát MAC PDU vyvíjel napříč releasy 3GPP, aby podporoval nové funkce a vyšší efektivitu. V raných systémech 3GPP (UMTS) také vrstva MAC používala PDU, ale struktura a funkce byly přizpůsobeny pro transportní kanály založené na CDMA. S přechodem na LTE založené na OFDMA v Release 8 byla struktura MAC PDU přepracována, aby byla flexibilnější a efektivnější pro paketově přepínaný, plně IP provoz. Začlenění řídicích prvků MAC do MPDU umožňuje nízkolatenční řídicí signalizaci v pásmu bez nutnosti vyhrazených zdrojů, což je klíčové pro dynamické plánování a správu mobility.

Účelem MPDU je poskytnout dobře definované rozhraní mezi vrstvou MAC a fyzickou vrstvou, což zajišťuje spolehlivé provádění široké škály funkcí MAC (multiplexování, HARQ, plánování). Řeší potřebu efektivního využití rádiových zdrojů tím, že umožňuje společné zabalení dat z různých zdrojů, což snižuje režii ve srovnání s odesíláním dat každého logického kanálu v samostatných fyzických přenosech. Motivací návrhu je minimalizace režie hlavičky prostřednictvím efektivních struktur podhlaviček, podpora SDU s proměnnou velikostí a umožnění rychlého zpracování jak v základnových stanicích, tak v UE, což je zásadní pro komunikace s vysokou přenosovou rychlostí a nízkou latencí v moderních celulárních sítích.

## Klíčové vlastnosti

- Obsahuje MAC hlavičku s jednou nebo více podhlavičkami identifikovanými LCID
- Přenáší multiplexovaná datová jednotka služby MAC (SDU) z jednoho nebo více logických kanálů
- Může obsahovat řídicí prvky MAC pro signalizaci specifickou pro vrstvu (např. BSR, PHR)
- Podporuje výplň pro splnění požadavků na velikost transportního bloku
- Tvoří užitečné zatížení transportního bloku předávaného fyzické vrstvě
- Umožňuje efektivní zpracování priorit a prioritizaci logických kanálů (LCP)

## Související pojmy

- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [LCID – Logical Channel Identifier](/mobilnisite/slovnik/lcid/)

## Definující specifikace

- **TS 28.403** (Rel-19) — WLAN Performance Measurements

---

📖 **Anglický originál a plná specifikace:** [MPDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpdu/)
