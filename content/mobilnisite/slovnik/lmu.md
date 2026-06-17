---
slug: "lmu"
url: "/mobilnisite/slovnik/lmu/"
type: "slovnik"
title: "LMU – Location Measurement Unit"
date: 2025-01-01
abbr: "LMU"
fullName: "Location Measurement Unit"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lmu/"
summary: "Síťový prvek nebo zařízení, které poskytuje rádiová měření na podporu služeb založených na poloze (LCS). Měří časování, sílu signálu nebo úhel příchodu signálů od mobilních zařízení nebo základnových"
---

LMU je síťový prvek, který poskytuje rádiová měření, jako je časování nebo síla signálu od mobilních zařízení nebo základnových stanic, na podporu lokalizačních technik pro služby založené na poloze.

## Popis

Location Measurement Unit (LMU) je klíčová komponenta v sítích 3GPP, která usnadňuje určení geografické polohy uživatelského zařízení (UE) pro služby založené na poloze ([LCS](/mobilnisite/slovnik/lcs/)). Funguje tak, že provádí přesná rádiová měření na uplinkových signálech od UE (režim s asistencí UE) nebo na downlinkových signálech od základnových stanic (NodeB, [eNB](/mobilnisite/slovnik/enb/), gNB) v závislosti na použité lokalizační metodě. Z architektonického hlediska mohou být LMU samostatné jednotky, integrované do míst základnových stanic nebo implementované jako softwarové funkce v síťových uzlech. Pro metodu Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) v LTE a NR měří LMU rozdíl času referenčního signálu (RSTD) mezi sousedními buňkami a poskytují časová data do Evolved Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)). E-SMLC/LMF následně vypočítá polohu UE pomocí multilateračních algoritmů. V UTRA (UMTS) podporují LMU metodu Uplink Time Difference of Arrival (U-TDOA) měřením času příchodu signálů od UE na více geograficky rozptýlených jednotkách. Mezi klíčové komponenty patří přijímače s vysokou přesností časování (často synchronizované pomocí [GPS](/mobilnisite/slovnik/gps/) nebo síťových časových protokolů), jednotky pro zpracování měření a rozhraní k architektuře jádra LCS (např. rozhraní SLm v LTE). LMU zajišťují přesnost a spolehlivost měření, což je prvořadé pro služby tísňového volání (např. E911), komerční lokalizační služby a optimalizaci sítě. Jejich činnost je koordinována lokalizačním serverem sítě, který jim na základě služebních požadavků udílí pokyny, co a kdy měřit.

## K čemu slouží

LMU byly vytvořeny, aby splnily regulatorní a komerční požadavky na přesné určování polohy mobilních zařízení. Původním impulzem byly požadavky služeb tísňového volání (jako E911 v USA), které vyžadovaly síťové určení polohy i v případě, kdy není v zařízení dostupný [GPS](/mobilnisite/slovnik/gps/). Před metodami vylepšenými o LMU nabízelo základní určení podle Cell ID špatnou přesnost (stovky metrů až kilometry), nedostatečnou pro zásah záchranných služeb. LMU umožnily pokročilé síťové techniky jako [OTDOA](/mobilnisite/slovnik/otdoa/) a U-TDOA, které poskytují mnohem vyšší přesnost (desítky metrů) využitím časových měření z více buněčných lokalit. Tím se vyřešilo omezení spočívající pouze v UE-bázi GPS, která má problémy s pokrytím uvnitř budov a závisí na možnostech zařízení. Historicky zavedené v 3GPP Release 99 poskytly LMU infrastrukturu potřebnou pro standardizované, síťově asistované určování polohy napříč GSM, UMTS, LTE a 5G NR. Řešily potřebu univerzálního lokalizačního řešení, které funguje nezávisle na hardwaru UE, čímž zajišťují soulad s bezpečnostními předpisy a umožňují širokou škálu komerčních aplikací založených na poloze.

## Klíčové vlastnosti

- Poskytuje přesná rádiová měření času, síly signálu nebo úhlu pro určování polohy
- Podporuje více lokalizačních metod: OTDOA, U-TDOA, Enhanced Cell ID
- Může být samostatná jednotka, integrovaná nebo softwarová síťová funkce
- Komunikuje s lokalizačními servery (E-SMLC, LMF) prostřednictvím standardizovaných protokolů
- Vyžaduje vysoce přesnou časovou synchronizaci (např. prostřednictvím GNSS nebo síťové synchronizace)
- Umožňuje síťové určení polohy bez závislosti na GPS schopnosti UE

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 36.111** (Rel-19) — LMU Requirements for UTDOA Positioning
- **TS 36.112** (Rel-19) — E-UTRAN LMU Conformance Requirements
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.456** (Rel-19) — SLm Interface Introduction
- **TS 36.459** (Rel-19) — SLmAP for E-UTRAN Positioning
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [LMU na 3GPP Explorer](https://3gpp-explorer.com/glossary/lmu/)
