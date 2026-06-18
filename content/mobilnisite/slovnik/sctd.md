---
slug: "sctd"
url: "/mobilnisite/slovnik/sctd/"
type: "slovnik"
title: "SCTD – Space Code Transmit Diversity"
date: 2025-01-01
abbr: "SCTD"
fullName: "Space Code Transmit Diversity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sctd/"
summary: "SCTD je technika diverzity přenosu používaná v UMTS/WCDMA ke zlepšení kvality signálu na downlinku a potlačení úniků (fadingu), aniž by vyžadovala více přijímacích antén na UE. Vysílá různě zakódované"
---

SCTD je technika diverzity přenosu pro UMTS/WCDMA, která zlepšuje spolehlivost signálu na downlinku vysíláním různě zakódovaných verzí stejných dat ze dvou antén.

## Popis

Space Code Transmit Diversity (SCTD) je uzavřená smyčka (closed-loop) schématu diverzity přenosu specifikovaného pro downlink UMTS (Universal Mobile Telecommunications System) založeného na technologii [WCDMA](/mobilnisite/slovnik/wcdma/) (Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)). Je navrženo ke zlepšení výkonu spojení v prostředí s úniky (fadingem) využitím prostorové diverzity pomocí dvou vysílacích antén na Node B (základnové stanici). Základní princip spočívá v současném vysílání dvou různě zakódovaných verzí stejného datového proudu uživatele ze dvou antén. Na rozdíl od jiných schémat SCTD používá pro dvě vysílací antény různé kanalizační (rozprostírací) kódy, zatímco se provádí scramblování stejným primárním scramblovacím kódem.

Fungování závisí na zpětné vazbě od uživatelského zařízení (UE). UE průběžně odhaduje podmínky downlink kanálu od obou vysílacích antén a vypočítává optimální komplexní váhy (fázové úpravy). Tyto váhy jsou kvantovány a odesílány zpět na Node B na uplinku pomocí pole [FBI](/mobilnisite/slovnik/fbi/) (Feedback Information) na [DPCCH](/mobilnisite/slovnik/dpcch/) (Dedicated Physical Control Channel). Node B následně tyto váhy aplikuje na signály před vysíláním ze dvou antén. Tento proces si klade za cíl maximalizovat přijímaný výkon signálu na UE konstruktivním sloučením signálů ze dvou cest, čímž efektivně směruje vysílací paprsek.

SCTD je aplikováno na Dedicated Physical Channel ([DPCH](/mobilnisite/slovnik/dpch/)) a je transparentní pro vyšší vrstvy. Zlepšuje poměr signálu k interferenci ([SIR](/mobilnisite/slovnik/sir/)) na downlinku, což umožňuje snížení vysílacího výkonu při zachování stejné kvality služby, zvětšení pokrytí buňky a zvýšení datové propustnosti. Je zvláště výhodné pro pomalu se pohybující uživatele na okrajích buněk. Toto schéma je součástí rodiny technik diverzity přenosu UMTS definovaných ve 3GPP Release 99 a novějších, která zahrnuje také Space Time Transmit Diversity ([STTD](/mobilnisite/slovnik/sttd/)), metodu s otevřenou smyčkou (open-loop).

## K čemu slouží

SCTD bylo vyvinuto pro zvýšení výkonu downlinku v sítích UMTS, konkrétně pro zmírnění účinků vícecestného úniku (multipath fadingu) a zlepšení spolehlivosti signálu bez zvýšení složitosti nebo nákladů na mobilním terminálu. Rané mobilní systémy často spoléhaly na přijímací diverzitu na základnové stanici pro zlepšení uplinku, ale zlepšení downlinku byla omezená. Techniky diverzity přenosu jako SCTD řeší tuto asymetrii přesunutím zátěže diverzity na stranu sítě, která může být snadněji vybavena více anténami.

Řeší problém špatné kvality downlinku na okrajích buněk a v náročných rádiových podmínkách, což přímo ovlivňuje uživatelský zážitek a kapacitu sítě. Zlepšením rozpočtu spoje (link budget) umožňuje SCTD vyšší datové rychlosti, lepší pokrytí a snížení míry spadlých hovorů. Jeho vznik byl motivován potřebou maximalizovat spektrální účinnost [WCDMA](/mobilnisite/slovnik/wcdma/) a poskytovat konzistentní kvalitu služeb při zavádění sítí UMTS. Ve srovnání s diverzitou s otevřenou smyčkou (STTD) poskytuje uzavřená povaha SCTD lepší výkon přizpůsobováním se rychlým změnám kanálu, což jej činí vhodným pro širší škálu scénářů mobility uživatelů.

## Klíčové vlastnosti

- Uzavřená smyčka (closed-loop) diverzity přenosu pro downlink UMTS
- Používá dvě vysílací antény na Node B
- Aplikuje různé kanalizační kódy na každou anténu
- Spoléhá se na zpětnou vazbu od UE pro úpravu fázových vah
- Přenášeno přes pole FBI v uplink DPCCH
- Zlepšuje downlink SIR, pokrytí a kapacitu

## Související pojmy

- [STTD – Space Time Transmit Diversity](/mobilnisite/slovnik/sttd/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)
- [FBI – Final Block Indicator](/mobilnisite/slovnik/fbi/)

## Definující specifikace

- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [SCTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sctd/)
