---
slug: "rv"
url: "/mobilnisite/slovnik/rv/"
type: "slovnik"
title: "RV – Redundancy Version"
date: 2025-01-01
abbr: "RV"
fullName: "Redundancy Version"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rv/"
summary: "RV je parametr v HARQ, který určuje, která podmnožina zakódovaných bitů je přenášena při opakovaném vysílání, čímž umožňuje inkrementální redundanci. Optimalizuje opravu chyb kombinací různých verzí d"
---

RV je parametr v HARQ, který určuje, která podmnožina zakódovaných bitů je přenášena při opakovaném vysílání, aby umožnil inkrementální redundanci a zlepšil spolehlivost prostřednictvím kombinované opravy chyb.

## Popis

Redundancy Version (RV) je základní parametr v procesech Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)) používaných v bezdrátových technologiích 3GPP, jako jsou UMTS, LTE a 5G NR. Určuje, která část turbo-kódovaného nebo LDPC-kódovaného kódového slova je vybrána pro přenos během daného pokusu HARQ, což umožňuje strategie inkrementální redundancy ([IR](/mobilnisite/slovnik/ir/)), které zvyšují úspěšnost dekódování. Při počátečním kódování dat pro přenos vzniká sada systematických bitů (původní data) a paritních bitů (redundance pro opravu chyb). RV řídí počáteční bod a vzor v této zakódované sekvenci, které jsou skutečně přenášeny, přičemž různé RV odpovídají různým podmnožinám bitů, například převážně systematickým bitům v jednom přenosu a dodatečným paritním bitům v opakovaných přenosech.

Během provozu vysílač vybere index RV (např. 0, 1, 2, 3 v LTE) pro každý HARQ přenos, což podle předdefinovaného modelu kruhového bufferu určuje výběr bitů. Příjemce kombinuje měkké bity z více přenosů a využívá doplňující informace z různých RV k postupnému vytváření úplnější verze kódového slova. Tato kombinace probíhá v HARQ soft bufferu, kde se akumulují logaritmické poměry věrohodnosti (LLR), čímž se s každým opakovaným přenosem zvyšuje pravděpodobnost úspěšného dekódování. Mezi klíčové komponenty patří HARQ entita, která spravuje výběr RV, a funkce rate matching, která aplikuje RV pro generování vysílané sekvence.

RV hraje klíčovou roli v přizpůsobování se různým podmínkám kanálu a optimalizaci spektrální účinnosti. Přenášením různých verzí redundance může systém dosáhnout určité formy časové diverzity a kódového zisku bez nutnosti dodatečné šířky pásma. V LTE jsou typicky definovány čtyři RV, zatímco 5G NR to rozšiřuje flexibilnějšími konfiguracemi RV pro podporu různých případů užití, včetně ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)). Výběr sekvence RV může být předdefinován nebo dynamicky přizpůsobován na základě informace o stavu kanálu, což ovlivňuje výkonnostní metriky, jako je bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)) a propustnost. Celkově je RV nezbytný pro robustní doručování dat v mobilních sítích, neboť umožňuje efektivní obnovu od chyb a zlepšuje adaptaci spoje.

## K čemu slouží

RV byl zaveden za účelem zlepšení účinnosti opravy chyb v bezdrátové komunikaci, kde tradiční metody [ARQ](/mobilnisite/slovnik/arq/) pouze opakovaně přenášely stejná data, plýtvaly šířkou pásma a nabízely omezené zisky ve špatných podmínkách kanálu. Rané systémy jako GSM používaly základní opakované přenosy, ale s rostoucími datovými rychlostmi u 3G UMTS vznikla potřeba sofistikovanějších technik pro potlačení chyb bez nadměrné redundance. [HARQ](/mobilnisite/slovnik/harq/) s inkrementální redundancí, umožněný RV, to řešil tím, že umožňoval opakovaným přenosům vysílat různé zakódované bity, což při kombinaci v přijímači poskytovalo dodatečný kódový zisk.

Poprvé standardizován v 3GPP Release 5 pro [HSDPA](/mobilnisite/slovnik/hsdpa/) v UMTS, byl RV motivován požadavkem na vyšší propustnost a spolehlivost v paketových službách. Řeší problém neefektivních opakovaných přenosů tím, že umožňuje přijímači akumulovat informace napříč pokusy, čímž efektivně vytváří v čase silnější kód pro opravu chyb. Tento přístup snižuje potřebu nadměrné počáteční redundance, optimalizuje spektrální účinnost a podporuje vývoj směrem k vysokorychlostnímu mobilnímu broadbandu v LTE a 5G, kde je adaptivní modulace a kódování prvořadé.

## Klíčové vlastnosti

- Definuje výběr bitů pro HARQ opakované přenosy
- Umožňuje inkrementální redundanci pro opravu chyb
- Používá rate matching s kruhovým bufferem v LTE/NR
- Podporuje více indexů RV (např. 0-3 v LTE)
- Umožňuje měkké kombinování v přijímači
- Zvyšuje pravděpodobnost dekódování v proměnných podmínkách kanálu

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [LDPC – Low-Density Parity-Check](/mobilnisite/slovnik/ldpc/)

## Definující specifikace

- **TR 22.885** (Rel-14) — LTE support for V2X services
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TR 38.845** (Rel-17) — NR Positioning Use Cases Study

---

📖 **Anglický originál a plná specifikace:** [RV na 3GPP Explorer](https://3gpp-explorer.com/glossary/rv/)
