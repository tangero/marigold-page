---
slug: "bsic"
url: "/mobilnisite/slovnik/bsic/"
type: "slovnik"
title: "BSIC – Base transceiver Station Identity Code"
date: 2025-01-01
abbr: "BSIC"
fullName: "Base transceiver Station Identity Code"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bsic/"
summary: "Jedinečný identifikátor základnové stanice (BTS) v sítích GSM, skládající se z Network Colour Code (NCC) a Base Station Colour Code (BCC). Umožňuje mobilním stanicím rozlišit buňky na stejném kanálu,"
---

BSIC je jedinečný identifikátor základnové stanice v síti GSM, který kombinuje kódy NCC a BCC a umožňuje mobilním zařízením rozlišit buňky na stejném kanálu pro výběr buňky, předávání hovoru (handover) a správu interference.

## Popis

Base transceiver Station Identity Code (BSIC) je základní identifikátor v GSM (Global System for Mobile Communications) a jeho vývojových standardech, definovaný specifikacemi 3GPP. Jedná se o 6bitový kód, který se skládá z 3bitového Network Colour Code ([NCC](/mobilnisite/slovnik/ncc/)) a 3bitového Base Station Colour Code ([BCC](/mobilnisite/slovnik/bcc/)). BSIC je vysílán základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) na synchronizačním kanálu ([SCH](/mobilnisite/slovnik/sch/)) jako součást rámcové struktury GSM, což umožňuje mobilním stanicím ([MS](/mobilnisite/slovnik/ms/)) jej dekódovat a identifikovat vysílající buňku. Tento kód je nezbytný pro to, aby mobilní stanice mohla rozlišit více buněk, které mohou vysílat na stejné rádiové frekvenci (buňky na stejném kanálu), což je běžný scénář v celulárních sítích s frekvenčním opakováním.

Z architektonického hlediska BSIC funguje v rámci GSM rádiového rozhraní, konkrétně rozhraní Um mezi MS a BTS. Část NCC je přiřazena operátorem sítě a typicky identifikuje skupinu BTS v určité geografické oblasti nebo segmentu sítě, což napomáhá administrativnímu a provoznímu seskupování. BCC je přiřazen každému BTS jednotlivě a v kombinaci s NCC zajišťuje jedinečnost v místním rádiovém prostředí. Mobilní stanice používá BSIC během procedur výběru a převýběru buňky, stejně jako při předávání hovoru (handover). Při měření sousedních buněk MS čte BSIC ze SCH každé buňky, aby potvrdila, že měří správnou buňku a nikoli rušivou buňku na stejném kanálu, což je zásadní pro přesné hlášení měření síti.

Během provozu je BSIC vysílán v každém GSM multiframe na SCH, který nese číslo rámce a BSIC. Mobilní stanice se synchronizuje se SCH, aby získala časové informace a BSIC. To umožňuje MS identifikovat obsluhující buňku a sousední buňky. Při předávání hovoru může síť nařídit MS, aby se předala do buňky identifikované konkrétní frekvencí a BSIC, čímž se zajistí, že se MS připojí k zamýšlené cílové buňce. BSIC také hraje roli v sekvencích frekvenčního přeskakování v GSM, protože BCC se používá k určení offsetu přeskakovací sekvence, což dále napomáhá randomizaci a správě interference v celé síti.

## K čemu slouží

BSIC byl vytvořen k řešení zásadních výzev v raném návrhu celulárních sítí, konkrétně správě interference a identifikaci buněk v systémech GSM. Před GSM čelily analogové celulární systémy, jako je AMPS, významným problémům s interferencí na stejném kanálu kvůli opakování frekvencí, ale postrádaly standardizovanou, robustní metodu, jak mobilní stanice jedinečně identifikovaly základnové stanice na stejné frekvenci. To vedlo k problémům se spolehlivostí předávání hovorů a výkonem sítě. BSIC zavedl digitální, kódovaný identifikátor, který mohly mobilní stanice rychle dekódovat ze synchronizačního kanálu, což umožnilo přesné rozlišení mezi buňkami sdílejícími stejnou nosnou frekvenci.

Jeho primárním účelem je řešit problém interference na stejném kanálu v celulárních sítích s frekvenčním opakováním. Přiřazením jedinečného BSIC každému [BTS](/mobilnisite/slovnik/bts/) v rámci opakovacího clusteru mohou mobilní stanice rozlišit mezi požadovanými signály a rušivými signály na stejné frekvenci. To je nezbytné pro přesná měření sousedních buněk, která jsou podkladem pro rozhodování o předání hovoru a převýběru buňky. Bez BSIC by mobilní stanice mohla nesprávně hlásit měření od rušivé buňky na stejném kanálu jako cílovou buňku, což by vedlo k neúspěšným předáním hovoru nebo přerušeným hovorům. BSIC tak zvyšuje spolehlivost sítě, kvalitu hovoru a celkovou kapacitu systému tím, že umožňuje efektivní frekvenční plánování a zmírňování interference.

Historicky zavedení BSIC v GSM Rel-5 (ačkoli koncepčně přítomný dříve) standardizovalo tento identifikační mechanismus v celém odvětví a podpořilo růst digitálních celulárních sítí. Vyřešil omezení dřívějších přístupů, které se spoléhaly pouze na sílu signálu nebo základní kódy, a poskytl strukturované, škálovatelné řešení, které se integruje se synchronizačními a přeskakovacími mechanismy. BSIC zůstává relevantní v GSM a jeho vývojových verzích, neboť tvoří základní prvek identity buňky v sítích 2G a ovlivňuje pozdější koncepty ve standardech 3GPP.

## Klíčové vlastnosti

- 6bitový jedinečný identifikátor (3bitový NCC + 3bitový BCC)
- Vysílán na synchronizačním kanálu (SCH) v GSM rámech
- Umožňuje mobilním stanicím rozlišit buňky na stejném kanálu
- Podporuje procedury výběru, převýběru a předání buňky (handover)
- Integruje se s sekvencemi frekvenčního přeskakování prostřednictvím BCC
- Usnadňuje správu interference a plánování sítě

## Související pojmy

- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)
- [NCC – Network (PLMN) Colour Code](/mobilnisite/slovnik/ncc/)
- [BCC – Base Transceiver Station Colour Code](/mobilnisite/slovnik/bcc/)
- [SCH – Synchronization Channel](/mobilnisite/slovnik/sch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [BSIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bsic/)
