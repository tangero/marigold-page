---
slug: "bsic-ncell"
url: "/mobilnisite/slovnik/bsic-ncell/"
type: "slovnik"
title: "BSIC-NCELL – Base Station Identity Code of a Neighbour Cell"
date: 2025-01-01
abbr: "BSIC-NCELL"
fullName: "Base Station Identity Code of a Neighbour Cell"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bsic-ncell/"
summary: "BSIC-NCELL je kód pro identifikaci základnové stanice (Base Station Identity Code) přiřazený sousední buňce v sítích GSM a UMTS. Jednoznačně identifikuje sousední buňky, aby umožnil správná rozhodnutí"
---

BSIC-NCELL je kód pro identifikaci základnové stanice (Base Station Identity Code) přiřazený sousední buňce v sítích GSM a UMTS, který ji jednoznačně identifikuje pro rozhodování o předávání hovoru a správu interference.

## Popis

BSIC-NCELL představuje kód pro identifikaci základnové stanice ([BSIC](/mobilnisite/slovnik/bsic/)) sousední buňky v sítích GSM a UMTS. Samotný BSIC je 6bitový kód skládající se ze dvou částí: síťového barevného kódu ([NCC](/mobilnisite/slovnik/ncc/), 3 bity) a barevného kódu základnové stanice ([BCC](/mobilnisite/slovnik/bcc/), 3 bity). NCC identifikuje [PLMN](/mobilnisite/slovnik/plmn/), ke kterému buňka patří, zatímco BCC rozlišuje mezi různými základnovými stanicemi v rámci stejné sítě. Když mobilní zařízení měří sousední buňky pro potenciální předání hovoru, hlásí hodnoty BSIC-NCELL spolu s měřeními síly signálu obsluhující buňce.

BSIC-NCELL hraje klíčovou roli v procesu předávání hovoru. Když mobilní stanice provádí měření na sousedních buňkách, musí každou buňku správně identifikovat, aby se předešlo záměně mezi buňkami s podobnými kmitočty. BSIC-NCELL poskytuje tuto jedinečnou identifikaci, což síti umožňuje rozlišit mezi buňkami, které by se jinak mohly jevit stejné pouze na základě kmitočtových měření. To je obzvláště důležité v hustých městských nasazeních, kde může více buněk pracovat na stejném kmitočtu.

V síťové architektuře je informace BSIC-NCELL vysílána každou buňkou jako součást její systémové informace. Mobilní zařízení tuto informaci dekódují ze sousedních buněk a hlásí ji zpět své obsluhující základnové stanici. Síť tyto hlášení používá k vytváření a udržování seznamů sousedních buněk, které jsou nezbytné pro přípravu a provedení předání hovoru. BSIC-NCELL také pomáhá řešit konflikty opakovaného využití kmitočtů a spravovat ko-kanálovou interferenci v celulárních sítích.

Technická implementace zahrnuje pečlivé plánování přiřazení BSIC v celé síti, aby sousední buňky měly odlišné hodnoty BSIC. Tím se zabrání nejednoznačnosti během měření a rozhodování o předání hovoru. Mobilní zařízení používá pro dekódování BSIC ze sousedních buněk synchronizační bity, které zahrnují jak vzory kmitočtově korekčního bitu, tak synchronizačního bitu nesoucí informaci o BSIC.

BSIC-NCELL zůstává relevantní i v pozdějších vydáních 3GPP jako součást procedur mobility mezi různými rádiovými přístupovými technologiemi (inter-RAT), kde sítě GSM/UMTS interagují se sítěmi LTE a 5G. Ačkoli se konkrétní implementační detaily vyvíjejí, základní koncept jednoznačné identifikace sousedních buněk pro správu mobility přetrvává napříč celulárními generacemi.

## K čemu slouží

BSIC-NCELL byl vytvořen k vyřešení kritického problému identifikace buněk během procedur předávání hovoru v celulárních sítích. V raných nasazeních GSM potřebovala mobilní zařízení spolehlivě identifikovat sousední buňky, aby zajistila úspěšné předání hovoru bez přerušení služby. Bez jedinečného identifikátoru, jako je BSIC-NCELL, by síť mohla zaměnit různé buňky pracující na stejném kmitočtu, což by vedlo k neúspěšným předáním hovoru nebo přerušeným hovorům.

Historický kontext vychází z omezení analogových celulárních systémů, kde se rozhodnutí o předání hovoru zakládala primárně na měření síly signálu. Tento přístup se ukázal jako nedostatečný v digitálních celulárních sítích se vzory opakovaného využití kmitočtů, kde mohlo více buněk sdílet stejný kmitočtový kanál. BSIC-NCELL poskytl mechanismus pro jednoznačnou identifikaci každé sousední buňky, což umožnilo spolehlivější rozhodování o předání hovoru a lepší výkon sítě.

BSIC-NCELL řeší několik praktických výzev v provozu celulární sítě. Pomáhá řešit nejednoznačnost, když více sousedních buněk používá stejný kmitočet kanálu pro vysílání řídicích informací. Umožňuje síti rozlišit mezi buňkami různých operátorů v pohraničních oblastech. Také podporuje efektivní správu a optimalizaci seznamů sousedních buněk, což je nezbytné pro udržení kvalitní služby při pohybu mobilních zařízení sítí. Tento koncept se ukázal jako tak zásadní, že podobné mechanismy identifikace sousedních buněk existují ve všech následujících celulárních technologiích.

## Klíčové vlastnosti

- 6bitový jedinečný identifikátor pro sousední buňky
- Skládá se ze síťového barevného kódu (NCC) a barevného kódu základnové stanice (BCC)
- Umožňuje jednoznačnou identifikaci buněk během měření pro předání hovoru
- Podporuje plánování opakovaného využití kmitočtů a správu interference
- Nezbytný pro vytváření a údržbu seznamů sousedních buněk
- Používá se v algoritmech pro rozhodování o předání hovoru a optimalizaci sítě

## Související pojmy

- [BSIC – Base transceiver Station Identity Code](/mobilnisite/slovnik/bsic/)
- [NCC – Network (PLMN) Colour Code](/mobilnisite/slovnik/ncc/)
- [BCC – Base Transceiver Station Colour Code](/mobilnisite/slovnik/bcc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [BSIC-NCELL na 3GPP Explorer](https://3gpp-explorer.com/glossary/bsic-ncell/)
