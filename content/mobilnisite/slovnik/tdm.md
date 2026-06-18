---
slug: "tdm"
url: "/mobilnisite/slovnik/tdm/"
type: "slovnik"
title: "TDM – Time Division Multiplexing"
date: 2025-01-01
abbr: "TDM"
fullName: "Time Division Multiplexing"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tdm/"
summary: "Základní multiplexní technika, při níž více signálů sdílí jediné přenosové médium rozdělením časové domény na oddělené, nepřekrývající se sloty. Každému signálu je přiřazen specifický časový slot, což"
---

TDM (časový multiplex) je základní multiplexní technika, při níž více signálů sdílí jediné přenosové médium rozdělením časové domény na oddělené, nepřekrývající se sloty přiřazené každému signálu.

## Popis

Time Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) (TDM, časový multiplex) je klíčová digitální komunikační technika, která umožňuje více datovým proudům nebo kanálům sdílet společný fyzický přenosový prostředek přidělením jedinečných, periodicky se opakujících časových slotů každému proudu. V systému TDM je čas rozdělen na rámce a každý rámec je dále rozdělen na pevný počet časových slotů. Danému kanálu (např. hovoru uživatele nebo datové relaci) je v každém rámci přiřazen jeden nebo více konkrétních slotů. Vysílač prokládá bity nebo symboly z různých kanálů do těchto sekvenčních slotů, čímž vytváří jediný složený bitový proud s vyšší rychlostí. Na přijímací straně synchronizovaný demultiplexor extrahuje bity z každého časového slotu a rekonstruuje původní jednotlivé kanály.

V systémech 3GPP se TDM používá na více úrovních. V rádiovém přístupu je základní součástí vícekanálových přístupových schémat. Například v GSM využívá rozhraní vzduchu [TDMA](/mobilnisite/slovnik/tdma/) (Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)), kde jsou různým uživatelům přiřazeny různé časové sloty na stejném kmitočtovém nosiči. V LTE a NR, přestože je primární vícekanálovou metodou [OFDMA](/mobilnisite/slovnik/ofdma/), se principy TDM používají v časové struktuře rámců a podrámců. Zdroje jsou přidělovány jak v čase (symboly, sloty), tak v kmitočtu (podnosné). TDM je také klíčový pro multiplexování řídicích a datových kanálů; například řídicí informace ([PDCCH](/mobilnisite/slovnik/pdcch/)) a data ([PDSCH](/mobilnisite/slovnik/pdsch/)) mohou být v rámci podrámce časově multiplexovány.

Mimo rozhraní vzduchu se TDM používá v přenosových sítích spojujících síťové uzly. Tradiční backhaulové spoje často využívají technologie založené na TDM, jako jsou E1/T1 nebo [SDH](/mobilnisite/slovnik/sdh/)/[SONET](/mobilnisite/slovnik/sonet/). Ve specifikacích architektury 3GPP přenášejí rozhraní TDM (např. Iu-CS v UMTS) okruhově přepínaný hlasový provoz pomocí principů TDM. Provoz závisí na přesné synchronizaci mezi multiplexorem a demultiplexorem, kterou obvykle poskytuje síťový hodinový signál. Mezi klíčové parametry patří délka rámce, délka slotu a počet slotů na rámec, které určují přenosovou rychlost a latenci kanálu. TDM poskytuje deterministické záruky latence a šířky pásma, protože slot pro každý kanál je rezervován, což jej činí ideálním pro služby s konstantní přenosovou rychlostí, jako je hlas.

## K čemu slouží

Technologie TDM byla vytvořena k vyřešení základního problému efektivního sdílení nákladné přenosové infrastruktury mezi více uživateli nebo kanály. Před TDM bylo běžné kmitočtové multiplexování (FDM), ale to vyžadovalo ochranná pásma mezi kanály a analogové filtry, což bylo neefektivní. TDM jako digitální technika umožnila konsolidaci více digitalizovaných hlasových kanálů na jedinou digitální linku, což dramaticky snížilo náklady telekomunikačních operátorů. Její deterministická povaha ji učinila dokonalou pro okruhově přepínanou telefonii, protože zajišťovala, že každý hovor obdrží pevný časový slot s nízkou latencí.

Motivace pro její zařazení a pokračující relevanci ve standardech 3GPP vychází z její jednoduchosti, spolehlivosti a vhodnosti pro časově citlivý provoz. V raném 2G GSM bylo zvoleno TDMA jako vícekanálové přístupové schéma, protože poskytovalo dobrou rovnováhu mezi kapacitou, náklady a energetickou účinností pro mobilní zařízení. I když se systémy 3GPP vyvíjely směrem k použití CDMA a poté OFDMA, principy TDM zůstaly zakotveny ve struktuře rámce pro organizaci přenosů v čase. Pro přenos byla backhaulová řešení založená na TDM (jako linky E1) po desetiletí dominantní technologií, poskytující spolehlivé, synchronizované spoje potřebné pro celulární sítě.

TDM řeší omezení čistě soutěživých nebo statistických multiplexních metod, které nemohou garantovat šířku pásma ani latenci. Zatímco paketově přepínané IP sítě z velké části nahradily TDM v páteřních sítích, dědictví TDM přetrvává v požadavcích na synchronizaci (prostřednictvím SyncE nebo IEEE 1588) a ve strukturovaném časování rádiových rámců. Jeho vývoj v rámci 3GPP ukazuje posun od použití TDM jako primárního vícekanálového přístupu rozhraní vzduchu (GSM) k jeho použití jako základního časového rámce pro pokročilejší multiplexní schémata (OFDMA v LTE/NR), což zajišťuje zpětnou kompatibilitu a efektivní rozdělování zdrojů.

## Klíčové vlastnosti

- Dělí přenosový čas na sekvenční, nepřekrývající se sloty přiřazené různým kanálům
- Poskytuje deterministické záruky šířky pásma a latence pro každý kanál
- Tvoří základ pro vícekanálový přístup TDMA v GSM
- Je základem časové struktury rámců v LTE a NR (sloty, symboly)
- Používá se v okruhově přepínaných rozhraních jádra sítě (např. Iu-CS)
- Vyžaduje přesnou synchronizaci mezi vysílačem a přijímačem

## Související pojmy

- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 25.874** (Rel-11) — HSPA Feedback & Signalling Efficiency for LCR TDD
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.412** (Rel-8) — Trunking Gateway Control Procedures
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TR 36.791** (Rel-16) — E-UTRA 2.4 GHz TDD Band for US
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [TDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdm/)
