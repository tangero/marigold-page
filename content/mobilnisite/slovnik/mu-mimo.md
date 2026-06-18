---
slug: "mu-mimo"
url: "/mobilnisite/slovnik/mu-mimo/"
type: "slovnik"
title: "MU-MIMO – Multi-User Multiple Input Multiple Output"
date: 2025-01-01
abbr: "MU-MIMO"
fullName: "Multi-User Multiple Input Multiple Output"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mu-mimo/"
summary: "MU-MIMO je technika prostorového multiplexu, při níž základnová stanice komunikuje s více uživatelskými zařízeními současně pomocí stejných časově-frekvenčních zdrojů. Dramaticky zvyšuje kapacitu sítě"
---

MU-MIMO je technika prostorového multiplexu, při níž základnová stanice využívá více antén ke komunikaci s několika uživatelskými zařízeními současně na stejných časově-frekvenčních zdrojích, čímž zvyšuje kapacitu sítě.

## Popis

Multi-User Multiple Input Multiple Output (MU-MIMO) je pokročilá anténní technologie, která umožňuje základnové stanici (eNodeB v LTE, gNB v 5G NR) vybavené více vysílacími anténami obsluhovat několik uživatelských zařízení (UE) souběžně na stejných blocích fyzických zdrojů (čas a frekvence). Na rozdíl od jednouživatelského [MIMO](/mobilnisite/slovnik/mimo/) ([SU-MIMO](/mobilnisite/slovnik/su-mimo/)), které směruje více datových proudů k jednomu UE, MU-MIMO prostorově odděluje proudy určené pro různá UE. Toho je dosaženo pomocí sofistikovaného digitálního zpracování signálu na straně vysílače, primárně využitím technik předkódování.

Základním operačním principem je prostorový dělicí multiplex. Základnová stanice využívá informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)), typicky hlášené UEs, k výpočtu matice předkódování. Tato matice manipuluje s fází a amplitudou signálů z každé vysílací antény tak, že při šíření bezdrátovým kanálem dochází ke konstruktivní interferenci na straně zamýšleného UE a destruktivní interferenci u současně plánovaných UEs – proces známý jako beamforming. V downlinku se tomu říká vysílací předkódování. Pro uplink MU-MIMO mohou více UEs vysílat současně na stejných zdrojích a základnová stanice využívá své více přijímací antény a algoritmy, jako je Minimum Mean Square Error ([MMSE](/mobilnisite/slovnik/mmse/)) nebo Successive Interference Cancellation ([SIC](/mobilnisite/slovnik/sic/)), k oddělení překrývajících se datových proudů.

Mezi klíčové komponenty umožňující MU-MIMO patří anténní pole, mechanismy odhadu kanálu a zpětné vazby (jako [CSI-RS](/mobilnisite/slovnik/csi-rs/) a hlášení CSI v NR), plánovací algoritmy, které vybírají kompatibilní UEs s příznivými prostorovými charakteristikami kanálu, a jednotky pro zpracování předkódování/dekódování. Jeho role v síti je transformační z hlediska kapacity. Opětovným využitím časově-frekvenčních zdrojů v prostoru MU-MIMO zvyšuje počet obsluhovaných uživatelů na buňku a celkovou datovou propustnost bez nutnosti získat další spektrum. V 5G je kombinováno s massive MIMO (využívajícím anténní pole s desítkami či stovkami prvků) pro podporu prostředí s vysokou hustotou uživatelů a je nezbytné pro splnění požadavků případu užití enhanced Mobile Broadband (eMBB).

## K čemu slouží

MU-MIMO bylo vyvinuto k řešení kritické výzvy omezené spektrální účinnosti v čím dál přetíženějších mobilních sítích. Jak uživatelská poptávka po datech prudce rostla s příchodem chytrých telefonů a streamování videa, tradiční metody navyšování kapacity – jako získávání dalšího spektra nebo zhušťování buněk – se staly drahé a nepraktické. [SU-MIMO](/mobilnisite/slovnik/su-mimo/) nabízelo zisky, ale bylo limitováno počtem antén, které mohlo jedno UE podporovat. MU-MIMO tento problém překonává využitím anténních zdrojů základnové stanice k současné obsluze více, potenciálně jednodušších, UEs.

Technologie řeší problém nevyužitých prostorových dimenzí. V prostředí s bohatým rozptylem tvoří bezdrátový kanál mezi víceanténní základnovou stanicí a více UEs víceuživatelskou kanálovou matici. MU-MIMO tuto matici využívá k vytvoření paralelních prostorových kanálů, čímž mění interferenci – tradičně škodlivou – na využitelný zdroj pro oddělení uživatelů. To byl posun oproti dřívějším systémům, které se interferenci primárně vyhýbaly prostřednictvím ortogonální alokace zdrojů ([TDMA](/mobilnisite/slovnik/tdma/), FDMA).

Jeho vznik byl motivován potřebou vyšší síťové kapacity v rámci stávajících spektrálních alokací, což byl klíčový cíl pro LTE-Advanced (Rel-10) a novější. Umožňuje operátorům obsloužit více uživatelů s vyššími datovými rychlostmi, zejména v hustě obydlených městských oblastech a přeplněných místech. Navíc tím, že umožňuje UEs s méně anténami (např. chytrým telefonům) těžit z velkého anténního pole základnové stanice, pomáhá vyvážit výkon s cenou, velikostí a spotřebou zařízení, čímž činí vysokorychlostní mobilní broadband dostupným pro širokou škálu zařízení.

## Klíčové vlastnosti

- Prostorový multiplex více uživatelů na stejných časově-frekvenčních zdrojích.
- Pro oddělení signálu spoléhá na vysílací předkódování (downlink) a víceuživatelskou detekci (uplink).
- Vyžaduje zpětnou vazbu informací o stavu kanálu (CSI) od uživatelů pro výpočet předkodéru.
- Integrováno s pokročilým plánováním pro párování uživatelů s semi-ortogonálními kanálovými vektory.
- Škáluje s počtem antén základnové stanice (ústřední pro Massive MIMO).
- Definováno pro směry downlink i uplink v LTE a NR.

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 36.871** (Rel-11) — Downlink MIMO Enhancement for LTE-Advanced
- **TR 36.912** (Rel-19) — TR on LTE-Advanced (Further E-UTRA)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.838** (Rel-17) — Study on XR Evaluations for NR
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology
- **TR 38.922** (Rel-19) — Study on IMT Parameters for NR in Higher Bands

---

📖 **Anglický originál a plná specifikace:** [MU-MIMO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mu-mimo/)
