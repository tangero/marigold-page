---
slug: "hs-scch"
url: "/mobilnisite/slovnik/hs-scch/"
type: "slovnik"
title: "HS-SCCH – High Speed Physical Downlink Shared Control Channel"
date: 2025-01-01
abbr: "HS-SCCH"
fullName: "High Speed Physical Downlink Shared Control Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hs-scch/"
summary: "Downlinkový fyzický řídicí kanál v UMTS, který přenáší klíčové signalizační informace pro umožnění High-Speed Downlink Packet Access (HSDPA). Informuje UE o parametrech přenosu pro nadcházející data n"
---

HS-SCCH je downlinkový fyzický řídicí kanál v UMTS, který přenáší signalizační informace pro umožnění HSDPA tím, že informuje UE o parametrech přenosu pro nadcházející data na HS-PDSCH.

## Popis

High Speed Physical Downlink Shared Control Channel (HS-SCCH) je základní součástí funkce UMTS High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) zavedené ve 3GPP Release 5. Funguje jako vyhrazený fyzický řídicí kanál vysílaný z Node B k uživatelskému zařízení (UE). Jeho primární funkcí je přenášet nezbytnou řídicí signalizaci vrstvy 1 (Layer 1), kterou UE potřebuje ke správnému příjmu, demodulaci a dekódování dat přenášených na High-Speed Physical Downlink Shared Channel ([HS-PDSCH](/mobilnisite/slovnik/hs-pdsch/)). HS-SCCH je vysílán dva sloty před přidruženým sub-rámcem HS-PDSCH, což poskytuje UE dostatek času na zpracování řídicích informací a konfiguraci svého přijímače.

Informace přenášené na HS-SCCH jsou rozděleny do dvou částí. Část 1 obsahuje klíčové parametry, jako je sada kanalizačních kódů (určující, které rozprostírací kódy jsou použity pro HS-PDSCH) a modulační schéma ([QPSK](/mobilnisite/slovnik/qpsk/) nebo 16-QAM). Část 2 obsahuje parametry jako velikost transportního bloku a informace o procesu Hybrid [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)), včetně verze redundance a indikátoru nových dat. Tato dvoudílná struktura umožňuje efektivní dekódování; UE může dekódovat Část 1, aby zjistila, zda je přenos určen pro ni (na základě UE-specifického maskování kontrolního součtu cyklickou redundancí), a pokud ano, pokračovat v dekódování Části 2.

Z architektonického hlediska je HS-SCCH sdílený kanál, což znamená, že může být použit pro signalizaci více UE v rámci buňky, ale každý sub-rámec je určen pro konkrétní UE. Používá pevný rozprostírací faktor 128. Časování kanálu je těsně provázáno s 2ms Transmission Time Interval ([TTI](/mobilnisite/slovnik/tti/)) HSDPA, což umožňuje rychlá rozhodnutí o plánování v Node B. Plánovač Node B, klíčová součást HSDPA, rozhodne, které UE bude obslouženo v příštím TTI, a poté vysílá odpovídající řídicí informace na HS-SCCH, následované datovou částí na HS-PDSCH. Tento návrh přesouvá plánování a řízení HARQ z Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) do Node B, což drasticky snižuje latenci.

Role HS-SCCH je klíčová pro výkonnostní zisky HSDPA. Poskytnutím rychlé řídicí signalizace v pásmu umožňuje adaptivní modulaci a kódování ([AMC](/mobilnisite/slovnik/amc/)), rychlé plánování paketů a rychlý Hybrid ARQ s měkkým kombinováním. Bez HS-SCCH by UE nevědělo, jak zpracovat dávkovitá vysokorychlostní data přicházející na sdíleném kanálu. Funguje jako nezbytný 'řídicí provoz' pro transportní kanál HS-DSCH, zajišťující, že vysokorychlostní datové potrubí je využíváno efektivně a že UE mohou správně obnovit své určené datové pakety uprostřed sdíleného média.

## K čemu slouží

HS-SCCH byl vytvořen k vyřešení zásadního omezení původní architektury vyhrazeného kanálu (DCH) UMTS Release 99 pro paketová data. V Release 99 byly plánování a řízení retransmisí zpracovávány RNC, umístěným dále od rádiového rozhraní. To zavádělo významnou latenci (kolem 100 ms) pro obousměrnou signalizaci, což výrazně omezovalo schopnost systému rychle se přizpůsobovat rychle se měnícím podmínkám rádiového kanálu a uživatelské poptávce. To ztěžovalo efektivní podporu vysokorychlostního, dávkovitého internetového provozu.

Motivací pro HSDPA, a tedy i pro HS-SCCH, bylo dramaticky zvýšit propustnost downlinkových paketových dat a snížit latenci, aby bylo možné lépe konkurovat vznikajícím širokopásmovým technologiím a podporovat nové multimediální služby. Základní myšlenkou bylo přesunout časově kritické funkce MAC vrstvy (plánování, HARQ) do Node B. To vyžadovalo nový řídicí kanál s nízkou latencí pro předání rozhodnutí plánovače přímo z Node B do UE. HS-SCCH byl navržen speciálně pro tuto roli, což umožnilo provoz s 2ms TTI a rychlou signalizaci, které jsou charakteristickými znaky HSDPA.

Řešil problém, jak dynamicky a rychle informovat UE o komplexních parametrech přenosu (kódy, modulace, HARQ informace) pro sdílený datový kanál. Předchozí řídicí signalizace byla příliš pomalá a nebyla optimalizována pro přidělování po sub-rámcích. Návrh HS-SCCH, s jeho pevným časovým vztahem k HS-PDSCH a UE-specifickou signalizací, poskytl nezbytný mechanismus k odemknutí potenciálu rychlého plánování v Node B a adaptivních technik spojové vrstvy, což vedlo k obrovskému skoku ve výkonu downlinku UMTS.

## Klíčové vlastnosti

- Přenáší řídicí informace vrstvy 1 (Layer 1) pro příjem na HS-PDSCH.
- Používá dvoudílnou strukturu pro efektivní UE-specifické dekódování.
- Vysílán dva sloty před přidruženým sub-rámcem HS-PDSCH.
- Umožňuje rychlé plánování v Node B s 2ms TTI.
- Signalizuje klíčové parametry: kanalizační kódy, modulační schéma (QPSK/16-QAM), velikost transportního bloku a HARQ informace.
- Používá pevný rozprostírací faktor 128.

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [HS-PDSCH – High Speed Physical Downlink Shared Channel](/mobilnisite/slovnik/hs-pdsch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.308** (Rel-19) — HSDPA Overall Description
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [HS-SCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/hs-scch/)
