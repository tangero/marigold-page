---
slug: "mimo"
url: "/mobilnisite/slovnik/mimo/"
type: "slovnik"
title: "MIMO – Multiple Input Multiple Output"
date: 2025-01-01
abbr: "MIMO"
fullName: "Multiple Input Multiple Output"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mimo/"
summary: "Základní anténní technologie využívající více vysílacích a přijímacích antén ke zlepšení výkonu komunikace. Zvyšuje datovou propustnost a spolehlivost spoje využitím prostorové diverzity a umožněním p"
---

MIMO je základní anténní technologie, která využívá více vysílacích a přijímacích antén ke zvýšení datové propustnosti a spolehlivosti spoje, a tvoří páteř moderních bezdrátových standardů jako 4G a 5G.

## Popis

Multiple Input Multiple Output (MIMO) je rádiová přístupová technologie, která využívá více antén na straně vysílače (např. základnové stanice) i přijímače (např. uživatelského zařízení) ke zlepšení bezdrátových komunikačních systémů. Funguje na fyzické vrstvě využitím prostorového rozměru rádiového kanálu. Základním principem je, že signály vysílané z různých antén urazí k přijímacím anténám mírně odlišné dráhy, čímž vytvářejí nezávislé kanály s útlumem. Systém MIMO je charakterizován svou konfigurací, označovanou jako MxN, kde M je počet vysílacích antén a N je počet přijímacích antén.

MIMO funguje prostřednictvím několika klíčových technik. Prostorové multiplexování vysílá více nezávislých datových proudů současně ve stejném časově-frekvenčním zdroji, čímž lineárně zvyšuje špičkovou datovou rychlost. To vyžaduje, aby přijímač oddělil smíšené proudy pomocí pokročilého zpracování signálu, jako je detekce Zero-Forcing nebo Minimum Mean Square Error ([MMSE](/mobilnisite/slovnik/mmse/)), která se opírá o informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)). Beamforming, další klíčová technika, využívá prekódování k utváření vyzařovacího diagramu vysílacích antén a zaměření energie na zamýšlený přijímač za účelem zlepšení síly signálu a snížení interference. Diverzitní techniky, jako je prostorově-časové kódování, vysílají stejná data přes více antén se specifickým kódováním, aby potlačily útlum a zlepšily spolehlivost spoje. Přijímač tyto signály kombinuje, aby robustněji obnovil data.

Klíčové komponenty v systému MIMO zahrnují anténní pole, RF řetězce (každá anténa má typicky vlastní transceiverový řetězec) a sofistikované jednotky pro zpracování základního pásma pro odhad kanálu, prekódování a detekci. Jeho role v síti, zejména od 3GPP Release 7 dále, byla transformační. V LTE se konfigurace MIMO jako 2x2 a 4x4 staly standardem. V 5G NR je Massive MIMO – využívající pole s desítkami či stovkami antén – klíčovou technologií, která umožňuje přesný beamforming pro kmitočty mmWave a rozsáhlé prostorové multiplexování v pásmech pod 6 GHz. Technologie je úzce integrována s dalšími postupy fyzické vrstvy, jako je návrh referenčních signálů (např. [CSI-RS](/mobilnisite/slovnik/csi-rs/), SRS) pro sondování kanálu a hybridní automatický požadavek na opakování ([HARQ](/mobilnisite/slovnik/harq/)) pro opravu chyb.

## K čemu slouží

Technologie MIMO byla vyvinuta za účelem překonání základních omezení tradičních jednoanténních (SISO) systémů při dosahování vyšších datových rychlostí a spolehlivějších spojů v rámci omezené Shannonovy kapacity daného přenosového pásma. Před MIMO vyžadovalo zvýšení datové rychlosti více spektra nebo modulaci vyššího řádu, což je nákladné a náchylné k šumu. MIMO využívá vícecestné šíření – tradičně považované za škodlivý jev způsobující útlum – a mění jej v prostředek pro zvýšení výkonu. Její vznik byl motivován potřebou uspokojit exponenciálně rostoucí poptávku po mobilních širokopásmových datech.

Historicky se koncepty MIMO objevily z akademického výzkumu v 90. letech 20. století, přičemž 3GPP poprvé standardizovalo základní formy v Release 7 pro [HSPA](/mobilnisite/slovnik/hspa/)+. Řešila omezení předchozích 3G systémů tím, že poskytla zvýšení spektrální účinnosti bez nutnosti dodatečného spektra. Každé následující vydání 3GPP přineslo vylepšení: Release 8 integrovalo MIMO do [OFDMA](/mobilnisite/slovnik/ofdma/) rámce LTE, Release 10 přidalo víceuživatelské MIMO ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)) pro LTE-Advanced a Release 15 zakotvilo Massive MIMO jako klíčovou vlastnost 5G NR. Tato vývojová řešení vyřešila problémy jako pokrytí na okraji buňky, kapacitu sítě v hustých městských oblastech a podporu vysokofrekvenčních pásem se špatnými šířicími charakteristikami pomocí beamformingu k prodloužení dosahu a zaměření energie.

## Klíčové vlastnosti

- Prostorové multiplexování pro vysílání více paralelních datových proudů, čímž se zvyšují špičkové datové rychlosti
- Beamforming prostřednictvím digitálního prekódování za účelem zaměření energie signálu a zlepšení poměru signál-šum (SNR)
- Prostorová diverzita (např. vysílací diverzita, přijímací diverzita) pro zvýšení spolehlivosti spoje a pokrytí
- Podpora víceuživatelského MIMO (MU-MIMO) pro obsluhu více uživatelů současně na stejném časově-frekvenčním zdroji
- Získávání informací o stavu kanálu (CSI) pomocí referenčních signálů (např. CSI-RS, SRS) pro adaptivní prekódování a plánování
- Škálovatelnost na konfigurace Massive MIMO s velkými anténními poli pro masivní prostorové multiplexování a přesný beamforming

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.824** (Rel-8) — HSPA Evolution for 1.28Mcps TDD Study
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [MIMO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mimo/)
