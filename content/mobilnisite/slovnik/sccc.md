---
slug: "sccc"
url: "/mobilnisite/slovnik/sccc/"
type: "slovnik"
title: "SCCC – Serial Concatenated Convolutional Code"
date: 2025-01-01
abbr: "SCCC"
fullName: "Serial Concatenated Convolutional Code"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sccc/"
summary: "SCCC je schéma kódování pro opravu chyb vpřed používané v systémech 3GPP UMTS a HSPA, které kombinuje dvě konvoluční kódy sériově s prokladačem za účelem zlepšení výkonu opravy chyb na šumových kanále"
---

SCCC je schéma kódování pro opravu chyb vpřed používané v systémech 3GPP UMTS a HSPA, které kombinuje dvě konvoluční kódy sériově s prokladačem za účelem zlepšení výkonu opravy chyb na šumových kanálech.

## Popis

Serial Concatenated Convolutional Code (SCCC) je technika kódování kanálu definovaná ve specifikacích 3GPP pro UMTS a [HSPA](/mobilnisite/slovnik/hspa/), konkrétně v kontextu vysokorychlostního přístupu k paketovým datům na downlinku ([HSDPA](/mobilnisite/slovnik/hsdpa/)). Funguje tak, že sériově zřetězuje dva konvoluční kodéry s prokladačem umístěným mezi nimi, čímž vytváří turbokódu podobnou strukturu poskytující silné možnosti opravy chyb. Vnější konvoluční kodér zpracovává vstupní datový tok a generuje paritní bity, které jsou následně prokládány, aby rozptýlily chyby ve shlucích, než jsou předány do vnitřního konvolučního kodéru pro další kódování. Toto sériové uspořádání v kombinaci s iterativním dekódováním na straně přijímače umožňuje SCCC dosáhnout výkonu blízkého Shannonově limitu, což jej činí velmi účinným v boji proti degradacím kanálu, jako je útlum a interference.

V praxi je SCCC implementováno ve fyzické vrstvě systémů UMTS/HSPA, kde se používá pro kódování transportních kanálů vyžadujících vysokou spolehlivost, jako jsou ty, které přenášejí uživatelská data v HSDPA. Proces kódování zahrnuje propichování nebo opakování bitů pro dosažení požadované kódové rychlosti, čímž optimalizuje kompromis mezi redundancí a propustností. Na straně přijímače provádí dekodér se soft-vstupem a soft-výstupem, často založený na BCJR algoritmu nebo jeho aproximacích, iterativní dekódování výměnou externí informace mezi vnitřním a vnějším dekodérem, čímž s každou iterací zpřesňuje odhady přenesených bitů. Tento iterativní proces výrazně snižuje míru bitových chyb, zejména v podmínkách nízkého poměru signálu k šumu.

Klíčovými součástmi SCCC jsou dílčí konvoluční kodéry, které jsou typicky rekurzivní systematické konvoluční ([RSC](/mobilnisite/slovnik/rsc/)) kódy s definovanými délkami omezení a generujícími polynomy, a prokladač, který může být náhodný nebo strukturovaný pro maximalizaci distančních vlastností. Flexibilita tohoto schématu mu umožňuje podporovat proměnné kódové rychlosti a přizpůsobit se různým podmínkám kanálu, což přispívá k spektrální účinnosti sítí 3G. Zvýšením odolnosti vůči chybám umožňuje SCCC vyšší datové rychlosti a lepší kvalitu služeb pro mobilní širokopásmové aplikace a tvoří základní prvek fyzické vrstvy ve standardech 3GPP.

## K čemu slouží

SCCC bylo zavedeno ve 3GPP Release 4 jako součást vylepšení UMTS, aby řešilo potřebu efektivnější opravy chyb ve vysokorychlostních datových službách, jako je [HSDPA](/mobilnisite/slovnik/hsdpa/). Předchozí kódovací schémata, jako jsou samostatné konvoluční kódy nebo paralelně zřetězené konvoluční kódy (turbokódy), měla v určitých scénářích omezení, zejména pro vyšší kódové rychlosti nebo specifické podmínky kanálu. SCCC poskytuje alternativu, která nabízí lepší výkon v konfiguracích se sériovým zřetězením a řeší problémy spojené s chybovými patry a složitostí dekódování.

Jeho zavedení bylo motivováno požadavkem na spolehlivý přenos paketových dat přes bezdrátové kanály, kde šum a útlum mohou výrazně degradovat výkon. Díky využití iterativního dekódování a prokládání SCCC snižuje míry bitových chyb bez nutnosti nadměrného vyzařovaného výkonu, čímž zlepšuje kapacitu sítě a uživatelský zážitek. Tím řešilo omezení dřívějších přístupů tím, že nabízelo flexibilní kódovací řešení, které lze optimalizovat pro různé datové rychlosti a požadavky služeb v se vyvíjejících systémech 3G.

## Klíčové vlastnosti

- Sériově zřetězuje dva konvoluční kodéry s prokladačem
- Podporuje iterativní dekódování pro výkon blízký Shannonově limitu
- Používá se v UMTS/HSPA pro vysokorychlostní přístup k paketovým datům na downlinku
- Umožňuje proměnné kódové rychlosti prostřednictvím propichování
- Zlepšuje opravu chyb na šumových bezdrátových kanálech
- Jako komponenty zahrnuje rekurzivní systematické konvoluční kódy

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding

---

📖 **Anglický originál a plná specifikace:** [SCCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/sccc/)
