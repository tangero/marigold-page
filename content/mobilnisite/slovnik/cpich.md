---
slug: "cpich"
url: "/mobilnisite/slovnik/cpich/"
type: "slovnik"
title: "CPICH – Common Pilot Channel"
date: 2025-01-01
abbr: "CPICH"
fullName: "Common Pilot Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cpich/"
summary: "Common Pilot Channel (CPICH) je fyzický kanál v sestupné větvi (downlink) sítě UMTS, který vysílá známý nemodulovaný signál. Je nezbytný pro mobilní zařízení (UE) k provádění odhadu kanálu, vyhledáván"
---

CPICH je kanál v sestupné větvi (downlink) sítě UMTS, který vysílá známý nemodulovaný signál používaný mobilními zařízeními pro odhad kanálu, vyhledávání buněk, měření pro předání spojení a řízení výkonu.

## Popis

Common Pilot Channel (CPICH) je základní fyzický kanál v sestupné větvi (downlink) rozhraní UMTS (Universal Mobile Telecommunications System), standardizovaný organizací 3GPP. Jedná se o spojitý nemodulovaný signál vysílaný stanicí Node B (základnovou stanicí) přes celou buňku. CPICH přenáší předdefinovanou bitovou sekvenci, která je rozprostřena pomocí specifického kanalizačního kódu a zakódována primárním scrambling kódem buňky. Tato struktura umožňuje uživatelskému zařízení (UE) snadno identifikovat buňku a synchronizovat se s ní. Primární funkcí CPICH je poskytovat fázový referenční signál pro koherentní demodulaci dalších fyzických kanálů v sestupné větvi, jako je Primary Common Control Physical Channel ([P-CCPCH](/mobilnisite/slovnik/p-ccpch/)) a vyhrazené fyzické kanály. Porovnáním přijímaného pilotního signálu se známou vysílanou sekvencí může UE odhadnout charakteristiky rádiového kanálu, včetně amplitudového a fázového zkreslení způsobeného mnohacestným únikem a dalšími rušivými jevy.

Z architektonického hlediska existují dva typy CPICH: Primary CPICH ([P-CPICH](/mobilnisite/slovnik/p-cpich/)) a Secondary CPICH (S-CPICH). P-CPICH je vysílán pomocí primárního scrambling kódu buňky a pevného kanalizačního kódu (typicky SF=256, kód 0). Je vysílán přes celou buňku a slouží jako primární fázová reference pro většinu kanálů v sestupné větvi. S-CPICH naopak může používat libovolný kanalizační kód s rozprostíracím faktorem 256 a může být zakódován buď primárním, nebo sekundárním scrambling kódem. S-CPICH se typicky používá ve specifických scénářích, jako jsou aplikace beamformingu, kdy je úzký anténní paprsek směrován k určitému uživateli nebo sektoru, nebo v oblastech s vysokou vytížeností pro zlepšení odhadu kanálu.

Nejkritičtější úlohou CPICH je umožnění klíčových měření UE. CPICH Received Signal Code Power (RSCP) je výkon měřený na jednom kódu CPICH, představující sílu signálu z konkrétní buňky po despreadingu. To se liší od RSSI (Received Signal Strength Indicator), které měří celkový širokopásmový výkon. Poměr CPICH RSCP k celkovému přijímanému výkonu (RSSI) je definován jako CPICH [Ec](/mobilnisite/slovnik/ece-c/)/No, což je klíčová metrika pro výběr a převýběr buňky. Běhy procedur mobility UE kontinuálně měří CPICH RSCP a Ec/No sousedních buněk a hlásí je síti, která tato data používá pro rozhodování o předání spojení. CPICH také definuje pokrytí buňky; jeho konstantní vysílací výkon (vzhledem k ostatním kanálům) znamená, že měření jako CPICH RSCP poskytují konzistentní a srovnatelný ukazatel kvality buňky v celé síti.

Z pohledu provozu sítě je úroveň výkonu CPICH kritickým konfiguračním parametrem. Jeho nastavení příliš nízko může vést ke špatnému odhadu kanálu, zvýšené míře přerušení hovorů a zmenšení pokrytí buňky. Nastavení příliš vysoko může vytvářet nadměrné rušení pro ostatní buňky a plýtvat výkonovými zdroji v sestupné větvi, čímž se snižuje celková kapacita. Optimalizace výkonu CPICH je proto klíčovým aspektem plánování a optimalizace rádiové sítě UMTS. Spojitá a předvídatelná povaha tohoto kanálu z něj také činí cíl pro služby založené na poloze, protože na signálu CPICH lze provádět časová měření (jako je Observed Time Difference of Arrival - [OTDOA](/mobilnisite/slovnik/otdoa/)) pro odhad polohy UE.

## K čemu slouží

CPICH byl zaveden ve verzi 3GPP Release 99, aby řešil základní požadavky systému Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (WCDMA). V sítích založených na [CDMA](/mobilnisite/slovnik/cdma/), jako je UMTS, všichni uživatelé sdílejí stejné frekvenční pásmo a jsou odděleni jedinečnými spreading kódy. To vytváří pro přijímač (UE) náročné rádiové prostředí, které musí přesně despreadovat a demodulovat zamýšlený signál za přítomnosti významného víceuživatelského rušení a časově proměnných podmínek kanálu. Primární problém, který CPICH řeší, je poskytnutí stabilního a známého referenčního signálu, který umožňuje UE odhadnout rychle se měnící charakteristiky rádiového kanálu. Bez takové reference by koherentní demodulace – která je energeticky účinnější a robustnější než nekoherentní demodulace – byla extrémně obtížná, což by vedlo k nízké propustnosti dat a vysoké míře chyb.

Před systémy 3GPP používaly sítě druhé generace (2G) GSM odlišnou přístupovou technologii (TDMA/[FDMA](/mobilnisite/slovnik/fdma/)) a nevyžadovaly ekvivalentní spojitý pilotní kanál. Přechod na WCDMA pro 3G si vyžádal nové mechanismy pro synchronizaci a odhad kanálu. CPICH poskytuje společnou fázovou referenci pro všechny uživatele v buňce, což je efektivnější než vkládání pilotních symbolů do vyhrazeného kanálu každého uživatele. Tento návrh zjednodušuje složitost přijímače UE a zlepšuje celkovou kapacitu systému. Navíc tím, že vysílá signál specifický pro buňku (svázaný s primárním scrambling kódem), se CPICH stává kotvou pro procedury vyhledávání a výběru buněk. Když se UE zapne nebo vstoupí do nové oblasti, skenuje signály CPICH, aby identifikovala a seřadila dostupné buňky, což je proces zásadní pro dostupnost sítě a mobilitu.

Vytvoření CPICH bylo motivováno potřebou robustní správy mobility v celulárním CDMA systému. V GSM byla předání spojení (handover) primárně založena na síle signálu (RXLEV). V UMTS, kvůli povaze CDMA omezené rušením, musí rozhodnutí o předání spojení zohledňovat jak sílu signálu, tak jeho kvalitu (poměr signálu k rušení). Měření CPICH [Ec](/mobilnisite/slovnik/ece-c/)/No tuto metriku kvality přímo poskytuje. Standardizací struktury CPICH a měření z něj odvozených (RSCP, Ec/No) zajistilo 3GPP, že UE od různých výrobců mohou spolehlivě měřit a hlásit kvalitu buňky, což umožňuje interoperabilní a efektivní předání spojení, převýběr buněk a řízení výkonu v sítích s více dodavateli. Vytvořilo to univerzální 'měřítko' pro podmínky v sestupné větvi rádiového rozhraní.

## Klíčové vlastnosti

- Poskytuje konstantní, známou fázovou referenci pro koherentní demodulaci kanálů v sestupné větvi
- Umožňuje kritická měření UE: CPICH RSCP (síla signálu) a CPICH Ec/No (kvalita signálu)
- Slouží jako základ pro procedury vyhledávání, výběru a převýběru buněk
- Podporuje dva typy: Primary CPICH (referenční signál pro celou buňku) a Secondary CPICH (pro beamforming / úzké paprsky)
- Základní pro měření a rozhodování o předání spojení (intra-frekvenční, inter-frekvenční, inter-RAT)
- Používá se jako časová reference pro metody určování polohy, jako je Observed Time Difference of Arrival (OTDOA)

## Související pojmy

- [P-CCPCH – Primary Common Control Physical Channel](/mobilnisite/slovnik/p-ccpch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [CPICH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpich/)
