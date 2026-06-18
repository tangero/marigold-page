---
slug: "smlcpp"
url: "/mobilnisite/slovnik/smlcpp/"
type: "slovnik"
title: "SMLCPP – SMLC Peer Protocol"
date: 2025-01-01
abbr: "SMLCPP"
fullName: "SMLC Peer Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/smlcpp/"
summary: "Protokol používaný pro přímou komunikaci mezi dvěma samostatnými centry polohové služby (SMLC) přes rozhraní Lp v sítích GSM. Definuje zprávy a procedury pro interakce mezi SMLC, což umožňuje koordina"
---

SMLCPP je protokol používaný pro přímou komunikaci mezi dvěma samostatnými centry polohové služby (Standalone Mobile Location Centers) přes rozhraní Lp v sítích GSM, který umožňuje jejich koordinaci pro služby určování polohy.

## Popis

[SMLC](/mobilnisite/slovnik/smlc/) Peer Protocol (SMLCPP) je specifický aplikační protokol definovaný ve specifikacích 3GPP pro GSM, který umožňuje přímou komunikaci mezi dvěma uzly typu Standalone Mobile Location Center (SMLC). Funguje přes rozhraní Lp, což je referenční bod propojující SMLC. Hlavním úkolem protokolu je umožnit SMLC vzájemně si vyměňovat informace a koordinovat polohovací aktivity pro mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) v případě, že obsluhující SMLC potřebuje pomoc od jiného SMLC nebo na něj potřebuje přenést odpovědnost, což je scénář typický při provozu mezi systémy nebo u některých metod určování polohy.

Architektonicky je SMLCPP peer-to-peer protokol. Každý SMLC implementující tento protokol může fungovat jako klient i server. Protokolový zásobník pro SMLCPP typicky využívá transportní mechanismy nižších vrstev, jako je [SS7](/mobilnisite/slovnik/ss7/) (Signaling System No. 7) se [SCCP](/mobilnisite/slovnik/sccp/) (Signaling Connection Control Part) a [TCAP](/mobilnisite/slovnik/tcap/) (Transaction Capabilities Application Part), jak je definováno v kontextu rozhraní Lp v GSM 08.31. Zprávy protokolu jsou přenášeny uvnitř komponent TCAP, což umožňuje strukturovaný dialog a správu transakcí mezi partnerskými SMLC.

Protokol funguje definicí souboru zpráv a souvisejících procedur. Mezi klíčové typy zpráv mohou patřit žádosti o polohové informace, přenosy měření, předávání kontextu určování polohy a oznámení o chybách. Například, pokud SMLC (SMLC-A) řídí určování polohy MS, ale zjistí, že se MS přesunula do oblasti, kde má jiný SMLC (SMLC-B) lepší informace o rádiovém prostředí nebo řídí příslušné základnové stanice, může SMLC-A použít SMLCPP k předání kontextu polohovací relace SMLC-B. SMLC-B by poté převzal výpočet polohy a případně vrátil výsledek zpět SMLC-A nebo přímo žadateli, v závislosti na použité proceduře.

Jeho úlohou je zajistit kontinuitu a přesnost služeb určování polohy přes hranice SMLC, což je klíčové pro bezproblémovou podporu polohování v rozsáhlých nebo více-dodavatelských síťových nasazeních. Standardizací této komunikace mezi partnery SMLCPP zabraňuje závislosti na konkrétním dodavateli a zajišťuje interoperabilitu mezi SMLC od různých výrobců. Jde o specializovaný protokol zaměřený na konkrétní provozní potřebu v rámci širší architektury Location Services ([LCS](/mobilnisite/slovnik/lcs/)), který doplňuje ostatní rozhraní SMLC s [BSC](/mobilnisite/slovnik/bsc/) (Lb), [MSC](/mobilnisite/slovnik/msc/) (Lg) a GMLC.

## K čemu slouží

SMLCPP byl vytvořen, aby vyřešil konkrétní mezeru v původní architektuře SMLC: absenci standardizovaného mechanismu pro přímou komunikaci mezi SMLC. V časných nasazeních SMLC typicky obsluhovalo konkrétní geografickou oblast nebo síťový segment. Pokud se mobilní stanice zapojená do polohovací procedury přesunula nebo vyžadovala měření z buněk řízených jiným SMLC, neexistoval efektivní způsob koordinace mezi těmito síťovými prvky. To mohlo vést k neúspěšným polohovacím požadavkům, snížené přesnosti nebo nutnosti spoléhat se na méně vhodné záložní metody.

Protokol řeší problém koordinace mezi SMLC pro služby určování polohy. Umožňuje scénáře jako předání polohovací relace, kooperativní určování polohy využívající měření z oblastí pokrytých různými SMLC a přenos pomocných dat nebo kontextu. To je obzvláště důležité pro polohovací techniky jako Enhanced Observed Time Difference (E-OTD) nebo Uplink-TDOA v GSM, kde jsou potřebná měření z více, potenciálně vzdálených základnových stanic, a tyto stanice mohou být spravovány různými SMLC.

Motivací bylo zvýšit robustnost, přesnost a úspěšnost síťového určování polohy, zejména pro nouzové služby a komerční aplikace vyžadující určení polohy bez ohledu na hranice síťové topologie. Definováním SMLCPP poskytlo 3GPP síťovým operátorům standardizovaný nástroj pro budování odolnějších a geograficky komplexnějších sítí služeb určování polohy, což zajišťuje, že funkce SMLC může být nasazena distribuovaným, avšak kooperativním způsobem.

## Klíčové vlastnosti

- Definuje peer-to-peer zprávy a procedury mezi dvěma uzly SMLC
- Funguje přes rozhraní Lp s využitím transportu SS7/SCCP/TCAP
- Umožňuje předání kontextu určování polohy mezi SMLC
- Podporuje přenos polohově relevantních měření a informací
- Umožňuje koordinaci pro metody určování polohy vyžadující data z více SMLC
- Zajišťuje interoperabilitu mezi SMLC od různých dodavatelů

## Související pojmy

- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [TCAP – Transaction Capabilities Application Part](/mobilnisite/slovnik/tcap/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [SMLCPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/smlcpp/)
