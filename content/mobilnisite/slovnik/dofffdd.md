---
slug: "dofffdd"
url: "/mobilnisite/slovnik/dofffdd/"
type: "slovnik"
title: "DOFFFDD – FDD Default DPCH Offset value"
date: 2025-01-01
abbr: "DOFFFDD"
fullName: "FDD Default DPCH Offset value"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dofffdd/"
summary: "DOFFFDD je parametr v režimu UMTS FDD, který definuje výchozí časový posun mezi sestupným DPCH a vzestupným DPCH. Je klíčový pro navázání počáteční synchronizace a udržení správného časového zarovnání"
---

DOFFFDD (výchozí hodnota časového posunu DPCH pro FDD) je parametr UMTS, který definuje výchozí časový posun mezi sestupným a vzestupným DPCH pro počáteční synchronizaci a zarovnání mezi UE a Node B.

## Popis

Výchozí hodnota časového posunu [DPCH](/mobilnisite/slovnik/dpch/) pro [FDD](/mobilnisite/slovnik/fdd/) (DOFFFDD) je kritický časový parametr definovaný ve specifikacích 3GPP UMTS Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně v TS 25.402 (UTRAN Iur Interface: Signaling Transport). Platí pro provoz v režimu Frequency Division Duplex (FDD). Parametr určuje výchozí časový posun, měřený v čipech, mezi začátkem snímku sestupného vyhrazeného fyzického kanálu (DPCH) vysílaného z Node B a začátkem odpovídajícího snímku vzestupného DPCH vysílaného z uživatelského zařízení (UE). Tento posun se používá během počátečního navázání vyhrazeného kanálu, zejména když explicitní příkazy k časovému seřízení ze sítě ještě nejsou k dispozici, nebo jako záložní referenční hodnota.

DPCH přenáší uživatelská data a řídicí informace pro vyhrazená spojení. Přesné časování je nezbytné pro to, aby UE správně dekódovalo sestupné přenosy, a aby Node B přijímalo vzestupné přenosy v očekávaném časovém okně, čímž se předejde rušení ostatních uživatelů. Hodnota DOFFFDD poskytuje standardizovaný výchozí bod pro tento časový vztah. Když řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) nastavuje rádiové spojení přes rozhraní Iur nebo Iub, může signalizovat DOFFFDD řídicímu Node B. Node B pak tuto hodnotu použije k výpočtu přesného časování snímků pro sestupné DPCH vzhledem k primárnímu scrambling kódu buňky a implicitně definuje, kdy očekává začátek vysílání vzestupného DPCH od UE.

Mechanicky je posun aplikován v rámci procedur vrstvy 1 (fyzické vrstvy). UE po přijetí sestupného DPCH použije známý posun (signalizovaný prostřednictvím zpráv vyšších vrstev nebo odvozený z výchozí hodnoty) k určení času vysílání svého vzestupného DPCH. Tento proces je součástí širšího mechanismu časového předstihu v UMTS. Zatímco průběžné jemné doladění časování je dosaženo pomocí bitů řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)) a explicitních příkazů časového předstihu na zlomkovém vyhrazeném fyzickém kanálu ([F-DPCH](/mobilnisite/slovnik/f-dpch/)) v pozdějších verzích, DOFFFDD zajišťuje funkční počáteční zarovnání. Jeho hodnota je pečlivě zvolena tak, aby zohlednila typické zpoždění šíření signálu na cestě tam a zpět v pokrytí buňky, čímž zabraňuje příliš časnému nebo pozdnímu příchodu vzestupných přenosů na přijímač Node B.

## K čemu slouží

DOFFFDD byl zaveden k vyřešení základního problému počáteční časové synchronizace pro vyhrazené kanály v sítích UMTS [FDD](/mobilnisite/slovnik/fdd/). Bez předdefinovaného časového vztahu by UE nevědělo, kdy má zahájit své vzestupné vysílání vzhledem k sestupnému, což by vedlo ke kolizím, neúspěšnému navázání hovoru a neefektivnímu využití rádiového spektra. Před navázáním vyhrazeného kanálu je UE synchronizováno s buňkou prostřednictvím společného pilotního kanálu ([CPICH](/mobilnisite/slovnik/cpich/)) pro sestupné časování, ale časování vzestupného spojení pro vyhrazené připojení vyžaduje specifický posun. DOFFFDD poskytuje tento nezbytný referenční bod.

Řeší omezení spočívající v absenci počátečního časového návodu, což by nutilo UE k provádění složitých a pomalých procedur slepého hledání nebo by vyžadovalo okamžitý zásah sítě pomocí příkazů časového předstihu před odesláním jakýchkoli dat. Standardizací výchozího posunu specifikace 3GPP zajišťují předvídatelné a rychlé nastavení kanálu, čímž zlepšují úspěšnost navázání hovoru a snižují latenci. Tento parametr je obzvláště důležitý pro počáteční vstup do sítě, procedury předávání spojení a obnovu po selhání rádiového spoje, kde je známý výchozí bod pro časové zarovnání nezbytný pro robustní a spolehlivou komunikaci. Jeho definice jako součást signalizace rozhraní Iur (TS 25.402) zdůrazňuje jeho roli v podpoře plynulé mobility a správy rádiových zdrojů mezi různými Node B řízenými potenciálně různými RNC.

## Klíčové vlastnosti

- Definuje výchozí časový posun mezi snímky sestupného a vzestupného DPCH v UMTS FDD
- Měřený v čipech (1 čip ≈ 0,26 µs v UMTS)
- Používá se pro počáteční synchronizaci během navazování vyhrazeného kanálu
- Signalizován přes rozhraní Iur/Iub pro konzistentní nastavení rádiového spoje
- Poskytuje záložní referenční časovou hodnotu pro UE
- Nezbytný pro prevenci kolizí vzestupného vysílání v časové doméně

## Související pojmy

- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)
- [FDD – Frequency Division Duplexing](/mobilnisite/slovnik/fdd/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms

---

📖 **Anglický originál a plná specifikace:** [DOFFFDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/dofffdd/)
