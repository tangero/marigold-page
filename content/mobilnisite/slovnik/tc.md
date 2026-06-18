---
slug: "tc"
url: "/mobilnisite/slovnik/tc/"
type: "slovnik"
title: "TC – Transport Channel"
date: 2025-01-01
abbr: "TC"
fullName: "Transport Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tc/"
summary: "Transportní kanál (TC) je logický kanál v rádiovém rozhraní UMTS a LTE/5G NR, který definuje, jak jsou data přenášena vzduchem mezi vrstvou MAC a fyzickou vrstvou. Specifikuje charakteristiky přenosu"
---

TC je logický kanál v rádiovém rozhraní UMTS, LTE a 5G NR, který definuje, jak jsou data přenášena vzduchem mezi vrstvou MAC a fyzickou vrstvou, a specifikuje přenosové charakteristiky, jako je kódování a mapování na zdroje.

## Popis

V architekturách 3GPP UMTS a vyvinutých LTE/5G NR je Transportní kanál (TC) základním konceptem v protokolovém zásobníku vrstvy 2 rádiové přístupové sítě (RAN), konkrétně na rozhraní mezi podsložkou řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a fyzickou vrstvou (vrstva 1). Slouží jako logický kanál, který určuje formát a metodu pro přenos bloků dat (Transportních bloků) přes rádiové rozhraní. Fyzická vrstva je zodpovědná za skutečný přenos a příjem rádiových signálů, ale funguje na základě parametrů a procedur definovaných Transportním kanálem. Každý typ Transportního kanálu je charakterizován specifickou sadou atributů, včetně Transportního formátu ([TF](/mobilnisite/slovnik/tf/)), který definuje dynamické aspekty, jako je velikost Transportního bloku a typ kanálového kódování (např. konvoluční, turbo), a Sady transportních formátů ([TFS](/mobilnisite/slovnik/tfs/)), což je kolekce všech povolených Transportních formátů pro daný kanál.

Provoz zahrnuje doručení Transportního bloku ([TB](/mobilnisite/slovnik/tb/)) z vrstvy MAC na fyzickou vrstvu přes definovaný Transportní kanál v každém přenosovém časovém intervalu ([TTI](/mobilnisite/slovnik/tti/)). Fyzická vrstva následně aplikuje odpovídající řetězec zpracování: připojení kontrolního součtu cyklickou redundancí ([CRC](/mobilnisite/slovnik/crc/)), kanálové kódování, vyrovnání přenosové rychlosti, prokládání a modulace, jak určuje vybraný Transportní formát. Tato zpracovaná data jsou pak namapována na fyzické kanály (jako Fyzický sdílený kanál pro downlink - [PDSCH](/mobilnisite/slovnik/pdsch/)) pro skutečný rádiový přenos. Mezi klíčové typy Transportních kanálů patří Vyhrazený transportní kanál ([DCH](/mobilnisite/slovnik/dch/)) pro vyhrazená uživatelská data, Kanál náhodného přístupu (RACH) pro počáteční přístup v uplinku, Kanál pro vysílání (BCH) pro systémové informace a sdílené kanály jako Sdílený kanál pro downlink (DL-SCH) a Sdílený kanál pro uplink (UL-SCH) v LTE/5G NR, které umožňují efektivní přenos paketových dat.

V síťové architektuře jsou Transportní kanály kritickou součástí protokolového zásobníku rádiového rozhraní, spravovaného NodeB/gNB a UE. Jejich konfigurace a dynamický výběr (Výběr kombinace transportních formátů - TFCS) jsou řízeny vyššími vrstvami (RRC) na základě rádiových podmínek, požadavků QoS a dostupných zdrojů. Vývoj od UMTS k LTE a 5G NR přinesl zjednodušení a vylepšení konceptů Transportních kanálů s posunem k flexibilnějším a dynamičtějším sdíleným kanálům pro podporu vysokorychlostních paketových datových služeb, ale základní princip definování logických přenosových charakteristik mezi MAC a PHY zůstává pro provoz RAN ústřední.

## K čemu slouží

Koncept Transportního kanálu byl zaveden, aby abstrahoval a standardizoval metodu přenosu dat přes rádiové rozhraní, oddělil logické požadavky na přenos dat od detailů fyzického přenosu. Před jeho formalizací v 3GPP UMTS měly systémy 2G, jako GSM, rigidnější a méně vrstvené struktury kanálů. TC poskytuje jasné rozhraní mezi vrstvou 2 (MAC) a vrstvou 1 (PHY), což umožňuje nezávislý vývoj a optimalizaci technik rádiového přenosu (jako nové modulační nebo kódovací schéma ve fyzické vrstvě) bez radikální změny procedur zpracování dat ve vyšších vrstvách. Tento vrstvený přístup je základním kamenem moderních telekomunikačních standardů.

Řeší problém efektivní podpory různorodých služeb (hlas, video, data) s odlišnými požadavky na kvalitu služeb (QoS) přes sdílené rádiové médium. Definováním specifických Transportních kanálů s atributy, jako jsou proměnné přenosové rychlosti, úrovně ochrany proti chybám a načasování přenosu, může systém dynamicky přidělovat zdroje. Například hlasové volání využívá Vyhrazený kanál (DCH) s konstantním formátem s nízkou latencí, zatímco prohlížení webu využívá Sdílený kanál (DL-SCH) s adaptivní modulací a kódováním. Tato flexibilita byla klíčovou motivací pro 3G a následující generace, které se posunuly od okruhově přepínaného hlasu k paketově přepínaným multimédiím.

## Klíčové vlastnosti

- Definuje charakteristiky logického přenosu dat mezi vrstvami MAC a PHY
- Specifikuje atributy Transportního formátu, jako je velikost bloku, kódování a TTI
- Podporuje více typů kanálů (Vyhrazený, Sdílený, Pro vysílání, Pro náhodný přístup)
- Umožňuje dynamickou adaptaci prostřednictvím Výběru kombinace transportních formátů (TFCS)
- Usnadňuje zpracování QoS prostřednictvím konfigurací specifických pro kanál
- Poskytuje rámec pro mapování na fyzické kanály pro rádiový přenos

## Související pojmy

- [DL-SCH – Downlink Shared Channel](/mobilnisite/slovnik/dl-sch/)
- [UL-SCH – Uplink Shared Channel](/mobilnisite/slovnik/ul-sch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.867** (Rel-18) — Study on 5G Smart Energy and Infrastructure
- **TR 22.967** (Rel-19) — eCall Emergency Data Transmission
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization
- **TR 26.997** (Rel-19) — IVAS Codec Specification
- **TS 29.013** (Rel-19) — MAP-SSAP Interworking for CCBS Service
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 34.109** (Rel-19) — UE Conformance Test Functions for UMTS
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [TC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tc/)
