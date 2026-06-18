---
slug: "hs-dpcch"
url: "/mobilnisite/slovnik/hs-dpcch/"
type: "slovnik"
title: "HS-DPCCH – High Speed Dedicated Physical Control Channel (Uplink)"
date: 2025-01-01
abbr: "HS-DPCCH"
fullName: "High Speed Dedicated Physical Control Channel (Uplink)"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hs-dpcch/"
summary: "HS-DPCCH je vysílací (uplink) fyzický řídicí kanál v UMTS/HSPA, který přenáší kritickou zpětnou vazbu z UE do Node B pro podporu vysokorychlostního příjmového přístupu k paketovým datům. Přenáší indik"
---

HS-DPCCH je vysílací (uplink) řídicí kanál v UMTS/HSPA, který používá UE k odesílání indikátoru kvality kanálu (CQI) a zpětné vazby HARQ ACK/NACK do Node B pro podporu provozu HS-DSCH.

## Popis

Kanál High Speed Dedicated Physical Control Channel (HS-DPCCH) je základní vysílací (uplink) fyzický kanál v rozhraní UMTS/[WCDMA](/mobilnisite/slovnik/wcdma/), zavedený speciálně pro provoz High-Speed Packet Access ([HSPA](/mobilnisite/slovnik/hspa/)). Je vždy asociován s příjmovým (downlink) přenosem na kanálu [HS-DSCH](/mobilnisite/slovnik/hs-dsch/) (High-Speed Downlink Shared Channel). UE používá tento kanál k odesílání časově kritických řídicích informací zpět k obsluhujícímu Node B, což umožňuje efektivní fungování vysokorychlostního příjmu. HS-DPCCH je kódově multiplexován s ostatními vysílacími vyhrazenými fyzickými kanály ([DPDCH](/mobilnisite/slovnik/dpdch/) a [DPCCH](/mobilnisite/slovnik/dpcch/)).

Kanál přenáší dva hlavní typy informací: potvrzení [HARQ](/mobilnisite/slovnik/harq/) ([ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)) a indikátor kvality kanálu (CQI). HARQ ACK/NACK je signál zpětné vazby pro každý přenesený transportní blok HS-DSCH. Poté, co se UE pokusí dekódovat blok, odešle ACK v případě úspěchu nebo NACK, pokud je vyžadována retransmise. To umožňuje procesu Hybrid ARQ (HARQ) v Node B rychle spravovat retransmise a poskytovat spolehlivost na úrovni spojení. CQI je změřená hodnota hlášená UE, která indikuje podmínky příjmového kanálu, například poměr signálu k šumu. Plánovač v Node B používá hlášení CQI od všech UE k rozhodnutí, kterého uživatele obsloužit příště a jaký modulační a kódovací schéma (např. QPSK, 16QAM) a velikost transportního bloku použít, čímž implementuje adaptaci spojení.

Fyzická struktura HS-DPCCH je rozdělena do dvou odlišných částí v rámci 2ms podrámce (tři časové sloty). První slot je vyhrazen pro přenos informace HARQ ACK/NACK. Zbývající dva sloty nesou CQI (nebo PCI - Pre-coding Control Information v módech MIMO). Kanál používá specifický šířicí faktor (typicky 256) a je vysílán s výkonovým offsetem vůči vysílacímu DPCCH, který nese pilotní bity a další řídicí informace. Výkon HS-DPCCH je pečlivě řízen, aby byla zajištěna spolehlivá recepce této kritické zpětné vazby bez způsobení nadměrného vysílacího rušení.

Z pohledu síťové architektury HS-DPCCH končí v Node B. Informace, které přenáší, jsou zpracovávány entitou MAC-hs (nebo MAC-ehs) a plánovačem v Node B. Rychlá smyčka zpětné vazby (v řádu milisekund) vytvořená pomocí HS-DPCCH je tím, co umožňuje HSPA dosáhnout vysoké spektrální účinnosti a nízké latence ve srovnání s dřívějšími releasy WCDMA. Mění příjem na systém, který je vědomý stavu kanálu a rychle se mu přizpůsobuje.

## K čemu slouží

HS-DPCCH byl zaveden v 3GPP Release 5 spolu s HS-DSCH, aby překonal omezení původního příjmu WCDMA pro paketová data. Před HSPA používal příjmový přístup k paketovým datům vyhrazené kanály (DCH), které byly pro prudce proměnný provoz neefektivní kvůli dlouhým dobám nastavení, pevné alokaci zdrojů a absenci rychlého plánování závislého na stavu kanálu. Vize pro HSDPA byla vytvořit sdílený kanál s velmi krátkými intervaly přenosového času (TTI=2 ms) a rychlými retransmisemi (HARQ) přímo řízenými Node B.

Aby tato vize fungovala, potřeboval Node B od UE dvě klíčové informace s minimálním zpožděním: úspěch/neúspěch každého přenosu (pro HARQ) a měření aktuální kvality kanálu (pro plánování a adaptaci spojení). Stávající vysílací DPCCH nebyl navržen pro přenos těchto nových, častých a časově kritických informací. Proto byl standardizován nový vyhrazený fyzický řídicí kanál, HS-DPCCH, aby poskytoval vyhrazenou cestu zpětné vazby s nízkou latencí.

Toto vyřešilo hlavní problémy starého přístupu. Rychlé ACK/NACK (prostřednictvím HS-DPCCH) umožnilo HARQ řízený Node B, což drasticky snížilo zpoždění retransmise ve srovnání s retransmisemi na úrovni RLC řízenými RNC. Častá hlášení CQI umožnila plánovači využívat diverzitu více uživatelů tím, že vysílal uživatelům, když byly jejich podmínky kanálu nejlepší, a okamžitě přizpůsoboval modulaci a kódování, čímž maximalizoval propustnost. Vytvoření HS-DPCCH tedy bylo zásadním vysílacím prvkem, který umožnil existenci vysoce výkonného příjmu HSDPA, a položilo základy pro všechna následná vylepšení HSPA.

## Klíčové vlastnosti

- Přenáší vysílací (uplink) řídicí informace pro HSDPA: HARQ ACK/NACK a indikátor kvality kanálu (CQI).
- Používá strukturu podrámce 2 ms sladěnou s intervalem přenosového času (TTI) HS-DSCH.
- Je kódově multiplexován ve vysílání s DPDCH a DPCCH, používá specifický šířicí faktor (např. 256).
- Výkon pro vysílání je nastaven vůči vysílacímu DPCCH prostřednictvím síťově konfigurovaného výkonového offsetu.
- Umožňuje rychlé plánování a adaptaci spojení řízené Node B prostřednictvím časté zpětné vazby CQI.
- Podporuje rychlý Hybrid ARQ (HARQ) se zpětnou vazbou ACK/NACK pro každý transportní blok HS-DSCH.

## Související pojmy

- [HS-DSCH – High Speed Downlink Shared Channel](/mobilnisite/slovnik/hs-dsch/)
- [DPCCH – Dedicated Physical Control Channel](/mobilnisite/slovnik/dpcch/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.706** (Rel-13) — Downlink Enhancements for UMTS Study
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 25.823** (Rel-8) — Synchronised E-DCH Study for UTRA FDD
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [HS-DPCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/hs-dpcch/)
