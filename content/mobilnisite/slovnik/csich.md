---
slug: "csich"
url: "/mobilnisite/slovnik/csich/"
type: "slovnik"
title: "CSICH – CPCH Status Indicator Channel"
date: 2025-01-01
abbr: "CSICH"
fullName: "CPCH Status Indicator Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/csich/"
summary: "Downlinkový fyzický kanál v UMTS, který vysílá stav dostupnosti společných paketových kanálů (CPCH) k uživatelskému zařízení (UE). Informuje UE o tom, které zdroje CPCH jsou aktuálně volné nebo obsaze"
---

CSICH je downlinkový fyzický kanál v UMTS, který vysílá stav dostupnosti společných paketových kanálů (CPCH) k uživatelskému zařízení (UE) a informuje ho o tom, které zdroje CPCH jsou volné nebo obsazené, aby umožnil efektivní uplinkový přenos paketů.

## Popis

Kanál indikátoru stavu [CPCH](/mobilnisite/slovnik/cpch/) (CSICH) je vyhrazený downlinkový fyzický kanál v režimu UTRA s časovým duplexem (TDD) v UMTS, standardizovaný ve 3GPP Release 4. Funguje jako vysílací řídicí kanál, který nepřetržitě přenáší stavové informace o přidružených společných paketových kanálech (CPCH) ve směru uplink. CSICH je vnitřně propojen s přístupovým postupem CPCH, což je sporný mechanismus navržený pro přenos dávkových paketových dat s nízkou až střední rychlostí od UE k síti.

Z architektonického hlediska je CSICH mapován na sekundární společný řídicí fyzický kanál (S-CCPCH) ve směru downlink. Jeho přenos je charakterizován specifickým kanalizačním kódem a kódem pro rozprostření spektra. Kanál nese indikátor CSICH ([CI](/mobilnisite/slovnik/ci/)), což je vícebitové stavové slovo. Každý bit nebo skupina bitů v tomto CI odpovídá konkrétnímu zdroji CPCH nebo sadě zdrojů (jako specifický kanalizační kód, kód pro rozprostření spektra nebo kombinace přístupových slotů). Hodnota každého indikačního bitu signalizuje aktuální dostupnost přidruženého uplinkového zdroje CPCH: typicky '0' znamená, že zdroj je volný a dostupný pro přístup, zatímco '1' znamená, že je obsazený nebo rezervovaný.

Operační postup zahrnuje nepřetržité monitorování ze strany UE, která mají v úmyslu odesílat uplinková paketová data. Před zahájením pokusu o přístup na CPCH musí UE nejprve dekódovat vysílání CSICH z obsluhované buňky. Přečtením CI UE identifikuje, které konkrétní zdroje CPCH jsou aktuálně označeny jako nečinné. Poté náhodně vybere jeden z dostupných zdrojů pro přenos svého přístupového preambule. Tento mechanismus předvýběru je klíčový, protože zabraňuje UE v pokusech o přístup na již obsazené zdroje, čímž výrazně snižuje pravděpodobnost kolize během počáteční přístupové fáze. Síť aktualizuje indikátory CSICH v reálném čase na základě úspěchu nebo neúspěchu přístupových postupů CPCH a probíhajícího využití přidělených kanálů.

Role CSICH je zásadní pro efektivitu transportního mechanismu CPCH. Tím, že poskytuje dynamické informace o stavu zdrojů v rámci celé buňky, mění čistě náhodný přístup typu ALOHA na řízenější proces typu reservation-aloha. To snižuje potřebu dlouhých postupů detekce a řešení kolizí, zkracuje přístupové zpoždění pro úspěšné přenosy a zlepšuje celkovou propustnost a kapacitu uplinku pro sporadický datový provoz. Jeho návrh odráží potřebu efektivního signalizačního mechanismu pro podporu paketových služeb s nízkou latencí v raných systémech 3G.

## K čemu slouží

CSICH byl vytvořen, aby řešil základní problém správy kolizí ve sporných přístupových schématech pro uplink v sítích 3G UMTS. Před jeho specifikací poskytovaly náhodné přístupové kanály (RACH) základní metodu pro počáteční přístup, ale byly neefektivní pro trvalý přenos paketových dat kvůli vysoké pravděpodobnosti kolizí a nedostatku informací o stavu zdrojů. Zavedení společného paketového kanálu ([CPCH](/mobilnisite/slovnik/cpch/)) mělo za cíl poskytnout efektivnější uplink pro dávkový datový provoz, ale vyžadovalo doplňkový řídicí mechanismus pro koordinaci přístupu mezi více UE.

Primární motivací bylo umožnit efektivní podporu nově se objevujících paketově přepínaných datových služeb, jako je prohlížení webu a e-mail, které se vyznačovaly přerušovanými potřebami přenosu. Bez indikátoru stavu by všechna UE slepě zkoušela přistupovat na jakýkoli zdroj CPCH, což by vedlo k častým kolizím, zvýšené latenci a plýtvání uplinkovou kapacitou kvůli kolizím v přenosech a následným procedurám ústupu. CSICH to řeší tím, že poskytuje UE předchozí znalost o dostupnosti zdrojů, což jim umožňuje činit informovaná přístupová rozhodnutí.

Historicky byly CSICH a CPCH součástí snah 3GPP ve verzích 4 a 5 o vylepšení UTRA TDD pro asymetrický a paketově orientovaný provoz, než se řešení High-Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)) stalo dominantním ve verzi 6 pro režim [FDD](/mobilnisite/slovnik/fdd/). Řešil omezení jednoduchého RACH a poskytl standardizovanou, síťově řízenou metodu pro správu soutěžení, čímž zlepšil kvalitu služeb pro rané mobilní datové aplikace snížením přístupového zpoždění a zvýšením míry úspěšných přenosů.

## Klíčové vlastnosti

- Vysílá stav dostupnosti uplinkových zdrojů CPCH v reálném čase
- Mapován na sekundární společný řídicí fyzický kanál (S-CCPCH) ve směru downlink
- Nese vícebitový indikátor CSICH (CI) pro mapování stavu zdrojů
- Umožňuje UE předvýběr pro volbu nečinných zdrojů před pokusem o přístup
- Snižuje pravděpodobnost kolize ve fázi přístupu CPCH
- Podporuje dynamické aktualizace stavu ze strany sítě na základě aktuálního využití

## Související pojmy

- [CPCH – Common Packet Channel](/mobilnisite/slovnik/cpch/)

## Definující specifikace

- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [CSICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/csich/)
