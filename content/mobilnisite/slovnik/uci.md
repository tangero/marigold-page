---
slug: "uci"
url: "/mobilnisite/slovnik/uci/"
type: "slovnik"
title: "UCI – Uplink Control Information"
date: 2025-01-01
abbr: "UCI"
fullName: "Uplink Control Information"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/uci/"
summary: "Řídicí signalizace vysílaná uživatelským zařízením (UE) v uplinku do sítě. Přenáší kritické informace jako potvrzení Hybrid ARQ (ACK/NACK), informace o stavu kanálu (CSI) a žádosti o naplánování (SR),"
---

UCI je řídicí signalizace v uplinku od uživatelského zařízení (UE), která přenáší klíčové informace jako potvrzení Hybrid ARQ, informace o stavu kanálu (CSI) a žádosti o naplánování (SR) pro adaptaci spojení, retransmise a plánování prostředků.

## Popis

Uplink Control Information (UCI) je základní součástí řídicí signalizace fyzické vrstvy v 3GPP LTE a NR. Představuje soubor řídicích dat, která uživatelské zařízení (UE) vysílá k základnové stanici (eNodeB/gNB) pro podporu provozu datových kanálů v uplinku a downlinku. UCI je primárně přenášeno na Physical Uplink Control Channel ([PUCCH](/mobilnisite/slovnik/pucch/)) a v určitých případech může být multiplexováno s uplink daty na Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)). Obsah, kódování a mapování prostředků pro UCI jsou detailně definovány ve specifikacích fyzické vrstvy (např. 3GPP TS 36.212/38.212 pro kódování kanálu a TS 36.213/38.213 pro procedury fyzické vrstvy).

Z architektonického hlediska se UCI skládá z několika odlišných typů informací, z nichž každá plní specifický účel v řídicí smyčce rádiového spoje. Klíčovými komponentami jsou: potvrzení Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)) ([ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)), které informuje gNB, zda byl downlink transportní blok přijat správně; Channel State Information ([CSI](/mobilnisite/slovnik/csi/)), které zahrnuje Channel Quality Indicator ([CQI](/mobilnisite/slovnik/cqi/)), Precoding Matrix Indicator ([PMI](/mobilnisite/slovnik/pmi/)) a Rank Indicator (RI) pro hlášení podmínek downlink kanálu; a Scheduling Request (SR), což je jednobitový indikátor používaný UE k žádosti o uplink prostředky pro přenos dat. Fyzická vrstva zpracovává tyto bity prostřednictvím specifických schémat kódování kanálu (např. Reed-Mullerovy kódy, polární kódy v NR) a moduluje je pro přenos.

Fungování UCI je těsně propojeno s plánovacím časováním a rámcovou strukturou. gNB naplánuje downlink data a přidělí specifické prostředky pro UE, aby odeslalo odpovídající HARQ-ACK zpětnou vazbu po pevném časovém odstupu. Pro periodické hlášení CSI nakonfiguruje gNB UE s konfigurací hlášení, která určuje, kdy a na kterých prostředcích má UE CSI odeslat. Prostředky pro SR jsou semistaticky konfigurovány. Síť musí UCI správně přijmout a dekódovat, aby mohla adaptovat své přenosy (prostřednictvím adaptace spojení založené na CSI), iniciovat retransmise (na základě HARQ-ACK) a přidělovat uplink prostředky (na základě SR). Jeho role je tedy klíčová pro udržení robustního, adaptivního a efektivního rádiového spoje a přímo ovlivňuje propustnost a latenci.

## K čemu slouží

UCI bylo vytvořeno, aby poskytlo spolehlivý a efektivní mechanismus pro odesílání klíčové řídicí zpětné vazby od UE do sítě. V paketově orientované, plánované architektuře LTE a NR potřebuje základnová stanice včasné informace od UE, aby mohla činit optimální rozhodnutí o plánování. Předchozí systémy měly méně dynamickou řídicí signalizaci. UCI řeší potřebu nízkolatenční, časté zpětné vazby pro umožnění pokročilých funkcí, jako je rychlá adaptace spojení, HARQ s měkkým kombinováním a dynamické plánování.

Problémy, které řeší, jsou mnohostranné. Bez HARQ-ACK by síť nevěděla, zda přenos selhal, což by vedlo k retransmisím na vyšších vrstvách s mnohem větší latencí. Bez CSI nemůže síť adaptovat modulační a kódovací schéma (MCS) na aktuální rádiové podmínky, což vede buď k plýtvání kapacitou (při příliš konzervativním nastavení), nebo k vysoké chybovosti (při příliš agresivním nastavení). Bez SR by se UE muselo spoléhat na náhodný přístup nebo předem přidělené periodické prostředky pro žádosti o uplink přidělení, což zvyšuje latenci a snižuje efektivitu pro trhavý provoz.

Jeho zavedení a vývoj byly motivovány rostoucími požadavky na vyšší datové rychlosti, nižší latenci a spolehlivější spojení. Jak se technologie vyvíjely z LTE na NR, mechanismy UCI byly vylepšeny, aby podporovaly více anténních portů (pro MIMO), širší šířky pásma, ultra-spolehlivou nízkolatenční komunikaci (URLLC) s velmi krátkými časovými lhůtami pro zpětnou vazbu a provoz v nelicencovaném spektru. Návrh UCI je klíčovým faktorem pro dosažení spektrální efektivity a responsivity, které definují systémy 4G a 5G.

## Klíčové vlastnosti

- Přenáší potvrzení HARQ (ACK/NACK) pro downlink data
- Přenáší Channel State Information (CQI, PMI, RI) pro adaptaci spojení
- Obsahuje Scheduling Request (SR) pro přidělení uplink prostředků
- Primárně vysíláno na Physical Uplink Control Channel (PUCCH)
- Může být multiplexováno s daty na Physical Uplink Shared Channel (PUSCH)
- Používá specifické kódování kanálu (např. polární kódování v NR pro spolehlivost)

## Související pojmy

- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)

## Definující specifikace

- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TS 38.824** (Rel-16) — NR URLLC Physical Layer Enhancements Study
- **TR 38.830** (Rel-17) — NR Coverage Enhancements Study
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [UCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/uci/)
