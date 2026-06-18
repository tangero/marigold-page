---
slug: "phich"
url: "/mobilnisite/slovnik/phich/"
type: "slovnik"
title: "PHICH – Physical Hybrid-ARQ Indicator Channel"
date: 2025-01-01
abbr: "PHICH"
fullName: "Physical Hybrid-ARQ Indicator Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/phich/"
summary: "Downlinkový fyzický řídicí kanál v LTE a NR používaný k přenosu potvrzení Hybrid Automatic Repeat reQuest (HARQ) (ACK/NACK) pro uplinkové datové přenosy. Poskytuje rychlou zpětnou vazbu uživatelskému"
---

PHICH je downlinkový fyzický řídicí kanál v LTE a NR, který přenáší potvrzení HARQ (ACK/NACK) pro uplinkové datové přenosy, aby poskytoval rychlou zpětnou vazbu uživatelskému zařízení (UE).

## Popis

Physical Hybrid-ARQ Indicator Channel (PHICH) je klíčový downlinkový fyzický kanál v systémech LTE (Long-Term Evolution) i NR (New Radio), specifikovaný od 3GPP Release 8. Jeho jediným účelem je přenášet indikátory potvrzení Hybrid Automatic Repeat reQuest ([HARQ](/mobilnisite/slovnik/harq/)) – konkrétně [ACK](/mobilnisite/slovnik/ack/) (potvrzení) nebo [NACK](/mobilnisite/slovnik/nack/) (negativní potvrzení) – ze základnové stanice (eNodeB v LTE, gNB v NR) k uživatelskému zařízení (UE). Tato zpětná vazba je odesílána v reakci na uplinkové datové přenosy přijaté na Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)). PHICH umožňuje rychlý mechanismus retransmise s nízkou latencí, který je zásadní pro dosažení vysoké spolehlivosti a efektivního využití rádiového spektra ve směru uplink.

Z architektonického hlediska je PHICH mapován na specifické zdrojové prvky v rámci downlinkového subrámce. V LTE je vysílán v řídicí oblasti subrámce, typicky zabírá prvních několik symbolů Orthogonal Frequency-Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) ([OFDM](/mobilnisite/slovnik/ofdm/)). Více PHICH je multiplexováno dohromady do skupin PHICH (PHICH groups) pro úsporu zdrojů řídicího kanálu. Každý PHICH ve skupině je rozlišen ortogonální sekvencí (Walshovým kódem) rozprostřenou přes více zdrojových prvků. Klíčové parametry definující PHICH zahrnují číslo skupiny PHICH, index ortogonální sekvence v rámci této skupiny a dobu trvání PHICH (normální nebo rozšířenou). eNodeB vypočítává tyto parametry na základě nejnižšího indexu Physical Resource Block ([PRB](/mobilnisite/slovnik/prb/)) odpovídajícího přenosu PUSCH a cyklického posunu [DM-RS](/mobilnisite/slovnik/dm-rs/) (Demodulation Reference Signal) používaného UE, čímž zajišťuje jednoznačné mapování.

Princip fungování: Když UE vysílá datový blok na PUSCH, naslouchá odpovědi PHICH v předem určeném downlinkovém subrámci (typicky o 4 ms později v LTE FDD). eNodeB dekóduje přenos PUSCH a vygeneruje ACK, pokud byla data dekódována správně, nebo NACK, pokud ne. Tento jednobitový indikátor je následně modulován BPSK, opakován a rozprostřen s ortogonální sekvencí před mapováním na přiřazené zdrojové prvky. UE, které zná vlastní parametry přenosu PUSCH, může odvodit přesné zdroje PHICH, které má monitorovat. Po přijetí NACK provede UE retransmisi stejné nebo redundantní verze dat (inkrementální redundance) podle synchronního HARQ procesu definovaného pro uplink. Tento uzavřený proces pokračuje, dokud není přijato ACK nebo dokud není dosaženo maximálního počtu retransmisí.

## K čemu slouží

PHICH byl vytvořen k řešení základní výzvy zajištění spolehlivého přenosu uplinkových dat přes šumový a útlumový bezdrátový kanál. Před HARQ s rychlou zpětnou vazbou PHICH se oprava chyb více spoléhala pouze na dopřednou korekci chyb (FEC), která je méně spektrálně účinná, protože vyžaduje vysílání nadměrné redundance pro nejhorší podmínky kanálu. PHICH umožňuje uplinkový HARQ protokol typu stop-and-wait, poskytuje rychlou zpětnou vazbu (ACK/NACK), která umožňuje UE retransmisi pouze v případě potřeby. To dramaticky zlepšuje propustnost uplinku a spektrální účinnost přizpůsobováním se okamžitým podmínkám kanálu.

Historicky byl návrh PHICH v LTE Release 8 motivován potřebou řídicího kanálu s nízkou latencí vyhrazeného pro HARQ zpětnou vazbu. Předchozí systémy 3G, jako HSPA, používaly pro podobné účely vyhrazené kanály nebo signalizaci v pásmu, ale architektura LTE založená na all-IP a OFDMA vyžadovala nový, efektivní návrh fyzické vrstvy. PHICH řeší problém poskytování včasné a spolehlivé zpětné vazby pro více UE současně bez spotřeby nadměrných downlinkových zdrojů. Jeho skupinová struktura s ortogonálními sekvencemi umožňuje multiplexování potvrzení pro mnoho UE na minimální sadu zdrojových prvků.

Vytvoření PHICH bylo hnací silou nadřazených cílů LTE: vyšších datových rychlostí, nižší latence a lepší spektrální účinnosti. Tím, že umožňuje rychlé retransmise na fyzické vrstvě (na rozdíl od pomalejších retransmisí na RLC vrstvě), PHICH snižuje dobu zpáteční cesty pro obnovu po chybě, což je klíčové pro aplikace citlivé na latenci. Tvoří páteř uplinkového HARQ procesu, spolupracuje s PUSCH a uplinkovými plánovacími povoleními (grants) k vytvoření robustního a adaptivního datového kanálu pro uplink. V NR se koncept vyvinul, ale zachoval si stejný základní účel, přizpůsobivý flexibilnější numerologii a struktuře slotů.

## Klíčové vlastnosti

- Přenáší HARQ ACK/NACK pro uplinkové přenosy na PUSCH
- Využívá rozprostření ortogonální sekvence v rámci skupin PHICH pro multiplexování
- Poskytuje zpětnou vazbu s nízkou latencí (např. 4 ms doba odezvy v LTE FDD)
- Podporuje jak normální, tak rozšířenou dobu trvání PHICH pro pokrytí
- Mapování zdrojů je jednoznačně odvozeno z parametrů PUSCH uživatelského zařízení (UE)
- Základní pro synchronní provoz uplinkového HARQ v LTE

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [PHICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/phich/)
