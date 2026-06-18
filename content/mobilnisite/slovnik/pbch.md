---
slug: "pbch"
url: "/mobilnisite/slovnik/pbch/"
type: "slovnik"
title: "PBCH – Physical Broadcast Channel"
date: 2025-01-01
abbr: "PBCH"
fullName: "Physical Broadcast Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pbch/"
summary: "Fyzický kanál na downlinku v LTE a NR, který vysílá základní systémové informace pro počáteční přístup k buňce. Nese Master Information Block (MIB) obsahující klíčové parametry, jako je systémová šířk"
---

PBCH je Physical Broadcast Channel, tedy fyzický vysílací kanál na downlinku, který přenáší základní systémové informace, jako je Master Information Block, a umožňuje tak počáteční přístup k buňce a synchronizaci.

## Popis

Physical Broadcast Channel (PBCH) je základní fyzický kanál na downlinku v technologiích LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) i NR (New Radio). Jeho primární funkcí je vysílat minimální soubor základních systémových informací, známý jako Master Information Block ([MIB](/mobilnisite/slovnik/mib/)), všem uživatelským zařízením (UE) v buňce. PBCH je přenášen s pevným a robustním kódovacím schématem a je vždy umístěn v centrálních 72 subnosných (6 zdrojových bloků) kolem nosné [DC](/mobilnisite/slovnik/dc/), bez ohledu na celkovou systémovou šířku pásma. To zajišťuje, že UE provádějící počáteční vyhledání buňky může PBCH nalézt a dekódovat bez předchozí znalosti systémové šířky pásma.

V LTE je PBCH vysílán v prvních 4 [OFDM](/mobilnisite/slovnik/ofdm/) symbolech slotu 1 v subframu 0 každého rádiového rámce (každých 10 ms). Datová část MIB je malá (24 bitů) a obsahuje nejdůležitější informace: šířku pásma systému na downlinku, konfiguraci Physical Hybrid-ARQ Indicator Channel ([PHICH](/mobilnisite/slovnik/phich/)) a 8 nejvýznamnějších bitů System Frame Number ([SFN](/mobilnisite/slovnik/sfn/)). Celé SFN je zakódováno napříč čtyřmi po sobě jdoucími přenosy PBCH (během 40 ms) pomocí specifického kódovacího schématu. UE musí PBCH úspěšně dekódovat, aby získalo systémovou šířku pásma, což mu následně umožní správně přijímat zbytek nosné a pokračovat v dekódování Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) nesoucího System Information Blocks (SIBs). PBCH využívá schéma diverzity vysílání (např. Space Frequency Block Coding) pro zlepšení spolehlivosti příjmu na okraji buňky.

V NR je koncept PBCH rozvinutý, ale zachovává si svůj základní účel. NR PBCH je součástí [SS](/mobilnisite/slovnik/ss/)/PBCH bloku (Synchronization Signal/PBCH block), což je periodicky vysílaná dávka signálů. MIB v NR obsahuje informace nezbytné pro počáteční přístup, včetně rozestupu subnosných, indexu SSB (pro beamforming), čísla systémového rámce a indikace plánování SIB1. Klíčovým vylepšením v NR je, že datová část PBCH obsahuje další bity, které v kombinaci s Demodulation Reference Signals (DM-RS) uvnitř PBCH pomáhají UE určit časování poloviny rádiového rámce a index SSB v rámci dávky, což je zásadní pro provoz v beamformingových prostředích mmWave. Robustní návrh PBCH v LTE i NR zajišťuje, že UE mohou spolehlivě dosáhnout počáteční synchronizace a získat povinné informace potřebné k přihlášení k buňce, což představuje úplně první krok v procesu přístupu k síti.

## K čemu slouží

PBCH byl vytvořen, aby vyřešil základní bootstrapový problém v celulárních systémech založených na OFDM: zapnuté UE nemá žádnou znalost konfigurace buňky. Před dekódováním jakýchkoli uživatelských dat nebo podrobných systémových informací potřebuje UE minimální soubor parametrů pro konfiguraci svého přijímače. PBCH poskytuje tyto naprosto kritické informace vysoce robustním a předvídatelným způsobem. Řeší tak omezení starších systémů, kde takové informace mohly být rozptýlené nebo vyžadovaly vícekrokové procedury slepé detekce.

V LTE a NR filozofie návrhu klade důraz na jasnou a efektivní sekvenci počátečního přístupu. UE nejprve detekuje Primary a Secondary Synchronization Signals (PSS/SSS), aby dosáhlo časové a frekvenční synchronizace a identifikovalo Physical Cell ID. Následným bezprostředním krokem je dekódování PBCH pro získání MIB. Informace v MIB, zejména systémová šířka pásma, je předpokladem pro to, aby si UE mohlo správně naladit svůj přijímač na celou šířku pásma nosné a lokalizovat řídicí oblast pro příjem PDCCH, který následně plánuje SIB1. Bez PBCH by UE nebylo schopné pokročit za hrubou synchronizaci. Jeho pevná poloha a robustní kódování zajišťují, že jej mohou úspěšně dekódovat i UE na okraji buňky s nízkým poměrem signálu k šumu, což garantuje spolehlivé pokrytí buňky pro počáteční přístup, což je prvořadé pro použitelnost sítě a mobilitu.

## Klíčové vlastnosti

- Nese Master Information Block (MIB) s nezbytnými parametry pro přístup k buňce.
- Přenášen s pevným, robustním kódováním a modulací (QPSK) pro vysokou spolehlivost.
- Zaujímá centrálních 72 subnosných (6 RB), nezávisle na celkové systémové šířce pásma.
- V LTE je vysílán každých 10 ms s kódováním přes 40 ms pro zakódování SFN.
- V NR je součástí SS/PBCH bloku, podporuje beamforming a poskytuje informace o časování/indexu beamu.
- Umožňuje UE určit systémovou šířku pásma, což je předpoklad pro dekódování všech ostatních downlinkových kanálů.

## Související pojmy

- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [SSS – Secondary Synchronization Signal](/mobilnisite/slovnik/sss/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [SIB1 – System Information Block Type 1](/mobilnisite/slovnik/sib1/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.863** (Rel-12) — CRS Interference Mitigation for Homogeneous Networks
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [PBCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbch/)
