---
slug: "bfn"
url: "/mobilnisite/slovnik/bfn/"
type: "slovnik"
title: "BFN – Node B Frame Number"
date: 2025-01-01
abbr: "BFN"
fullName: "Node B Frame Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bfn/"
summary: "BFN je 12bitový čítač používaný v UTRAN pro číslování 10ms rádiových rámců na Node B. Poskytuje společný časový referenční signál pro synchronizaci mezi Node B a RNC, což umožňuje koordinované plánová"
---

BFN je 12bitový čítač v UTRAN, který čísluje 10ms rádiové rámce na Node B a poskytuje společný časový referenční signál pro synchronizaci mezi Node B a RNC.

## Popis

Node B Frame Number (BFN) je základní časový mechanismus v architektuře UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně definovaný v kontextu rozhraní Iub mezi Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a Node B (základnovou stanicí). Jedná se o 12bitový cyklický čítač, který přiřazuje jedinečné číslo každému 10ms rádiovému rámci vysílanému Node B. Rozsah BFN je od 0 do 4095, což odpovídá časovému cyklu 40,96 sekundy (4096 rámců * 10 ms). Tento čítač je generován lokálně na Node B na základě jeho interního hodinového signálu, který je obvykle synchronizován se společným referenčním zdrojem, jako je [GPS](/mobilnisite/slovnik/gps/) nebo síťový časový protokol, aby byla zajištěna časová shoda v celé síti.

Z architektonického hlediska slouží BFN jako primární časová reference pro vysílací a přijímací činnosti Node B na rádiovém rozhraní. Používá se k časovému označení různých událostí a měření. Například když RNC posílá Node B příkazy pro plánování nebo řídicí zprávy pro měření, tyto příkazy mohou být asociovány s konkrétními hodnotami BFN, aby určily, kdy mají být akce na rádiovém rozhraní provedeny. Naopak, hlášení o měřeních od Node B k RNC, jako je Received Signal Code Power ([RSCP](/mobilnisite/slovnik/rscp/)) nebo Signal-to-Interference Ratio ([SIR](/mobilnisite/slovnik/sir/)), jsou časově označena hodnotou BFN, která udává přesný rádiový rámec, během něhož bylo měření provedeno. Tato přesná časová korelace je klíčová pro funkce jako je předávání hovoru (handover), kde RNC musí koordinovat přesný okamžik, kdy User Equipment (UE) přepne z jedné buňky do druhé.

Z procesního hlediska je BFN základem několika klíčových procesů v UTRAN. Při nastavování buňky a synchronizaci si RNC a Node B sladí svou znalost BFN, aby zajistily konzistentní číslování rámců. Při měkkém předání hovoru (soft handover) RNC používá hodnoty BFN k synchronizaci vysílání stejných dat z více Node B k UE, což vyžaduje přesné časové sladění na zlomky rámce. BFN je také nedílnou součástí rámcových protokolů pro Common Transport Channel ([CCH](/mobilnisite/slovnik/cch/)) a Dedicated Transport Channel ([DCH](/mobilnisite/slovnik/dch/)) definovaných ve specifikacích rozhraní Iub. Transportní bloky přenášející uživatelská data nebo řídicí informace jsou asociovány s Connection Frame Number ([CFN](/mobilnisite/slovnik/cfn/)), který je následně mapován na skutečný čas vysílání definovaný BFN a časovým posunem, což umožňuje RNC přesně plánovat přenos dat.

Jeho role sahá i do správy a optimalizace sítě. Analýzou hlášení o měřeních označených BFN mohou operátoři sítě diagnostikovat problémy související s časováním, jako jsou chyby synchronizace mezi Node B nebo nadměrné zpoždění přenosu. BFN tedy není pouze čítačem, ale úhelným kamenem pro časovou koordinaci všech činností správy rádiových prostředků v UTRAN, který zajišťuje, že toky dat, řídicí příkazy a procedury fyzické vrstvy probíhají v přesně správný okamžik pro udržení kvality služeb a efektivity sítě.

## K čemu slouží

BFN byl vytvořen, aby řešil základní výzvu časové synchronizace a koordinace v asynchronních sítích UMTS založených na CDMA. Před 3G se sítě GSM spoléhaly na synchronizované základnové stanice používající přesné hodinové zdroje, ale přechod na WCDMA v UMTS přinesl složitější rádiové rozhraní, kde je přesné časování klíčové pro kódový multiplex (code division multiplexing) a měkké předání hovoru (soft handover). Bez společné časové reference na úrovni rámců mezi řídicím RNC a distribuovanými Node B by bylo nemožné koordinovat plány vysílání, provádět plynulá předání hovoru nebo přesně korelovat data měření. BFN tuto zásadní společnou časovou základnu poskytuje.

Historicky vývoj UTRAN vyžadoval oddělenou architekturu, kde je inteligence (RNC) oddělena od bodů rádiového přenosu (Node B). Toto oddělení si vyžádalo robustní časový mechanismus přes rozhraní Iub pro udržení koordinace. BFN řeší problém sladění akcí v tomto distribuovaném systému. Umožňuje RNC zadávat budoucí akce (např. 'začněte vysílat v rámci číslo 1050') a Node B hlásit minulé události s přesným časováním ('měření provedeno v rámci číslo 1048'). Tato schopnost je životně důležitá pro funkce jako je makro-diverzitní kombinování (macro-diversity combining) při měkkém předání hovoru, kde musí být stejná data vyslána z více Node B přesně ve stejný čas, a pro plánovací algoritmy, které spravují interferenci a kapacitu.

Vytvoření BFN bylo motivováno potřebou deterministického a předvídatelného chování v rádiové přístupové síti. Řeší omezení jednodušších mechanismů řízených událostmi nebo relativního časování tím, že poskytuje absolutní cyklický čítač rámců. To umožňuje pokročilou správu rádiových prostředků, podporuje požadavky na QoS tím, že umožňuje přesné plánování provozu citlivého na zpoždění, a tvoří základ pro složitější časová vylepšení v pozdějších release 3GPP. V podstatě je BFN časovým lepidlem, které spojuje logickou řídicí rovinu v RNC s fyzickými přenosovými událostmi na Node B.

## Klíčové vlastnosti

- 12bitový cyklický čítač poskytující časový cyklus 40,96 sekundy
- Základní časová reference pro 10ms rádiové rámce na rozhraní Uu
- Umožňuje přesné časové označování hlášení o měřeních a provádění řídicích příkazů
- Nezbytný pro synchronizaci měkkého předání hovoru (soft handover) a operací makro-diverzity
- Mapuje logické Connection Frame Number (CFN) na skutečný čas vysílání na rádiovém rozhraní
- Podporuje synchronizaci sítě a diagnostiku prostřednictvím časově sladěné korelace událostí

## Související pojmy

- [CFN – Connection Frame Number](/mobilnisite/slovnik/cfn/)
- [SFN – System Frame Number](/mobilnisite/slovnik/sfn/)

## Definující specifikace

- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements

---

📖 **Anglický originál a plná specifikace:** [BFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/bfn/)
