---
slug: "dl-sch"
url: "/mobilnisite/slovnik/dl-sch/"
type: "slovnik"
title: "DL-SCH – Downlink Shared Channel"
date: 2025-01-01
abbr: "DL-SCH"
fullName: "Downlink Shared Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dl-sch/"
summary: "Hlavní transportní kanál v LTE a NR pro downlink uživatelských dat a řídicí informace. Přenáší dynamicky plánovaná data pro více uživatelských zařízení (UE) využívající sdílené časově-frekvenční prost"
---

DL-SCH je hlavní transportní kanál pro downlink v LTE a NR, který přenáší dynamicky plánovaná uživatelská data a řídicí informace pro více uživatelských zařízení (UE) využívající sdílené časově-frekvenční prostředky.

## Popis

Downlink Shared Channel (DL-SCH) je hlavní transportní kanál pro downlink v rádiových přístupových sítích LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) i NR (5G). Používá se k přenosu dat uživatelské roviny (z vrstvy [PDCP](/mobilnisite/slovnik/pdcp/)), řídicích informací (např. zpráv [RRC](/mobilnisite/slovnik/rrc/)) a bloků systémových informací ([SIB](/mobilnisite/slovnik/sib/)) ze základnové stanice (eNodeB v LTE, gNodeB v NR) k uživatelskému zařízení (UE). DL-SCH je charakteristický svým sdíleným charakterem; rádiové prostředky v časové a frekvenční doméně jsou dynamicky přidělovány plánovačem ve vrstvě [MAC](/mobilnisite/slovnik/mac/) základnové stanice více uživatelským zařízením po dílčích rámečcích (LTE) nebo po sloty (NR). Tento přístup se sdíleným kanálem je základním kamenem paketově orientované architektury, umožňuje statistické multiplexování a vysoce efektivní využití rádiového spektra.

Z architektonického pohledu se DL-SCH nachází mezi vrstvami MAC a fyzickou vrstvou. Vrstva MAC přijímá MAC [PDU](/mobilnisite/slovnik/pdu/), která obsahují data z vyšších logických kanálů (jako [DTCH](/mobilnisite/slovnik/dtch/) a [DCCH](/mobilnisite/slovnik/dcch/)), a mapuje je na transportní kanál (DL-SCH). Fyzická vrstva následně zpracovává transportní blok z DL-SCH řetězcem operací zahrnujících kanálové kódování (Turbo kód v LTE, LDPC v NR), přizpůsobení rychlosti, skramblování, mapování modulace a mapování vrstev pro MIMO. Výsledné symboly jsou mapovány na zdrojové elementy v rámci fyzického downlink sdíleného kanálu (PDSCH). Mezi klíčové součásti patří mechanismus Hybrid Automatic Repeat Request (HARQ) pro opravu chyb, proces adaptace spojení (který vybírá vhodný schéma modulace a kódování - MCS) a dynamická plánovací povolení doručovaná přes PDCCH.

V provozu sítě rozhoduje plánovač gNB/eNB, kterému uživatelskému zařízení (UE) bude obsluhovat v každém přenosovém časovém intervalu (TTI). Bere v úvahu faktory jako indikátory kvality kanálu (CQI) hlášené uživatelskými zařízeními, požadavky QoS, stav vyrovnávací paměti a algoritmy spravedlivosti. Jakmile je uživatelské zařízení naplánováno, monitoruje PDCCH pro formát Downlink Control Information (DCI), který indikuje přidělení prostředků na PDSCH (který nese DL-SCH). Uživatelské zařízení následně demoduluje a dekóduje PDSCH, aby získalo transportní blok, zpracuje jej prostřednictvím entity HARQ a doručí úspěšně dekódovaná data vyšším vrstvám. Role DL-SCH je tedy ústřední pro veškerý přenos dat v downlinku, poskytuje flexibilní, adaptivní a spolehlivý přenosový kanál, který podporuje vysoké datové rychlosti a nízkou latenci slibované technologiemi LTE a NR.

## K čemu slouží

DL-SCH byl zaveden spolu s LTE ve verzi 3GPP Release 8, aby nahradil paradigma vyhrazených kanálů z 3G WCDMA a umožnil plně paketově optimalizovanou rádiovou přístupovou síť. V před-LTE systémech, jako je UMTS, byla uživatelská data často přenášena na vyhrazených kanálech (DCH), které rezervovaly kódové prostředky pro jedno uživatelské zařízení po dobu trvání spojení, což vedlo k neefektivnímu využití prostředků pro trhavý internetový provoz. Koncept sdíleného kanálu představoval revoluční posun, umožňující sdružování síťových prostředků a jejich přidělování na požádání, což je pro IP-based datový provoz, který dominuje moderním sítím, mnohem efektivnější.

Jeho zavedení vyřešilo základní problém efektivní podpory vysokorychlostních služeb paketových dat s nízkou latencí pro velký počet uživatelů. Dynamickým plánováním prostředků umožňuje DL-SCH špičkové datové rychlosti v řádu Gbps, okamžitě se přizpůsobuje měnícím se rádiovým podmínkám prostřednictvím adaptace spojení a poskytuje robustní doručování prostřednictvím HARQ. Motivace byla hnána exponenciálním růstem spotřeby mobilních dat a potřebou rozhraní vzduchu, které by mohlo škálovat výkon při zachování spektrální účinnosti. DL-SCH spolu se svým protějškem pro uplink (UL-SCH) tvoří páteř filozofie 'sdíleného kanálu', která definuje 4G a 5G, což z něj činí jeden z nejkritičtějších a nejtrvalejších konceptů moderní buněčné technologie.

## Klíčové vlastnosti

- Dynamické a adaptivní plánování časově-frekvenčních prostředků mezi více uživatelskými zařízeními (UE) na bázi per-TTI
- Podpora Hybrid ARQ (HARQ) s měkkým kombinováním pro rychlé retransmise a spolehlivé doručení
- Pokročilá adaptace spojení využívající zpětnou vazbu CQI k výběru optimální modulace (od QPSK po 256QAM/1024QAM) a kódovací rychlosti
- Zpracování transportního bloku s kanálovým kódováním (Turbo kód v LTE, LDPC v NR) a fyzickou vrstvou pro PDSCH
- Přenáší multiplexovaná data z více logických kanálů (DTCH, DCCH, CCCH) a systémové informace
- Základní pro provoz MIMO, podporuje přenos přes více vrstev pro prostorové multiplexování

## Související pojmy

- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [MCS – Modulation and Coding Schemes](/mobilnisite/slovnik/mcs/)
- [UL-SCH – Uplink Shared Channel](/mobilnisite/slovnik/ul-sch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [DL-SCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dl-sch/)
