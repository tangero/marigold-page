---
slug: "sch"
url: "/mobilnisite/slovnik/sch/"
type: "slovnik"
title: "SCH – Synchronization Channel"
date: 2025-01-01
abbr: "SCH"
fullName: "Synchronization Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sch/"
summary: "Synchronizační kanál (SCH) je downlinkový fyzický kanál používaný v UMTS a LTE pro vyhledávání buněk a synchronizaci. Skládá se z primárního (P-SCH) a sekundárního (S-SCH) synchronizačního kanálu a um"
---

SCH (Synchronizační kanál) je downlinkový fyzický kanál používaný v UMTS a LTE pro vyhledávání buněk a synchronizaci, který umožňuje UE detekovat buňku, určit její časování a identifikovat skupinu skramblovacích kódů buňky.

## Popis

Synchronizační kanál (SCH) je klíčový downlinkový fyzický kanál v 3GPP UMTS ([UTRA](/mobilnisite/slovnik/utra/)) a jeho evoluci do LTE. Jeho primární funkcí je usnadnit proceduru vyhledávání buněk, kdy uživatelské zařízení (UE) zapne nebo vstoupí do nové oblasti a musí identifikovat a synchronizovat se s vhodnou buňkou. SCH není jediný kanál, ale skládá se ze dvou odlišných komponent: primárního synchronizačního kanálu (P-SCH) a sekundárního synchronizačního kanálu (S-SCH). Ty jsou vysílány v konkrétních časových slotech v rámci struktury rádiového rámce.

V UMTS nese P-SCH primární synchronizační kód ([PSC](/mobilnisite/slovnik/psc/)), který je stejný pro všechny buňky v systému. UE použije přizpůsobený filtr k detekci tohoto kódu, což poskytne synchronizaci hranic slotu. Jakmile je časování slotu získáno, UE čte S-SCH. S-SCH vysílá sekvenci sekundárních synchronizačních kódů ([SSC](/mobilnisite/slovnik/ssc/)) ve vzoru, který se opakuje každý rámec. Tento vzor identifikuje skupinu skramblovacích kódů buňky. Po identifikaci skupiny UE provede vyhledávání v rámci této skupiny, aby našlo přesný primární skramblovací kód používaný primárním společným pilotním kanálem buňky ([P-CPICH](/mobilnisite/slovnik/p-cpich/)), čímž dosáhne synchronizace rámce a dokončí identifikaci buňky.

V LTE se koncept vyvinul, ale zachoval stejný základní účel. P-SCH a S-SCH jsou vysílány v centrálních 72 subnosičích prvního a šestého podrámce každého rádiového rámce ve frekvenční oblasti. LTE P-SCH nese jednu ze tří možných Zadoff-Chu sekvencí, které označují skupinu identit buněk fyzické vrstvy (0, 1 nebo 2). S-SCH nese sekvenci, která identifikuje konkrétní identitu buňky v rámci této skupiny (0-167). Společně poskytují fyzickou identitu buňky ([PCI](/mobilnisite/slovnik/pci/)). Konstrukce v LTE také napomáhá detekci časování rádiového rámce (začátek 10ms rámce) a délky cyklické předpony.

Fungování SCH je těsně integrováno s dalšími fyzickými kanály a signály. Po synchronizaci založené na SCH dekóduje UE fyzický vysílací kanál ([PBCH](/mobilnisite/slovnik/pbch/)), aby získalo základní systémové informace, jako je hlavní informační blok ([MIB](/mobilnisite/slovnik/mib/)). Výkon SCH přímo ovlivňuje dobu počátečního přístupu, spolehlivost předávání spojení a celkovou efektivitu sítě. Jeho robustní konstrukce, využívající dobře definované sekvence s dobrými vlastnostmi autokorelace a vzájemné korelace, zajišťuje spolehlivou detekci i v náročných rádiových podmínkách s vysokým rušením nebo nízkým poměrem signálu k šumu.

## K čemu slouží

SCH byl vytvořen, aby vyřešil základní problém, jak mobilní zařízení objeví a naváže spojení s celulární sítí bez předchozí znalosti. Při absenci společného hodinového signálu musí UE určit přesné časování přenosů buňky (hranice slotů a rámců) a identifikovat konkrétní detekovanou buňku z mnoha možností. Před synchronizací je přijímač UE v podstatě slepý ke struktuře příchozího rádiového signálu.

Konstrukce SCH, zejména rozdělení na primární a sekundární komponentu, řeší efektivitu a složitost. Jediný univerzální kód P-SCH umožňuje rychlé počáteční získání časování pomocí jednoduchého korelačního obvodu. S-SCH pak přenáší konkrétnější identifikační informace ve strukturovaném vzoru. Tento dvoukrokový hierarchický přístup snižuje čas a výpočetní výkon potřebný pro vyhledávání buněk ve srovnání s hrubou silou prohledávání všech možných kódů buněk. Je to základní kámen konstrukce celulárních systémů, který umožňuje plynulou mobilitu a vstup do sítě.

Jeho evoluce z UMTS do LTE odráží přechod na [OFDMA](/mobilnisite/slovnik/ofdma/) a potřebu ještě rychlejšího a efektivnějšího přístupu v vysokorychlostních paketových sítích. Konstrukce SCH v LTE, využívající Zadoff-Chu sekvence ve frekvenční oblasti, je optimalizována pro detekci OFDM symbolů a poskytuje robustní výkon jak v časově, tak frekvenčně selektivních útlumových kanálech, které jsou běžné v mobilním prostředí. SCH zůstává nezbytným prvkem jakéhokoli celulárního rozhraní vzduchu, neboť vytváří samotný základ rádiového spojení.

## Klíčové vlastnosti

- Umožňuje vyhledávání buněk a počáteční synchronizaci pro UE
- Skládá se ze dvou odlišných komponent: Primárního SCH (P-SCH) a Sekundárního SCH (S-SCH)
- Poskytuje časovou synchronizaci slotů a rámců
- Identifikuje skupinu skramblovacích kódů buňky (UMTS) nebo Fyzickou identitu buňky (LTE)
- Používá předdefinované sekvence s dobrými korelačními vlastnostmi pro spolehlivou detekci
- Vysílán na známých pozicích v rámci struktury rádiového rámce

## Související pojmy

- [P-CPICH – Primary Common Pilot Channel](/mobilnisite/slovnik/p-cpich/)
- [PCI – Physical Cell Identity](/mobilnisite/slovnik/pci/)
- [PBCH – Physical Broadcast Channel](/mobilnisite/slovnik/pbch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [SCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sch/)
