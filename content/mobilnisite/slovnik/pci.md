---
slug: "pci"
url: "/mobilnisite/slovnik/pci/"
type: "slovnik"
title: "PCI – Physical Cell Identity"
date: 2025-01-01
abbr: "PCI"
fullName: "Physical Cell Identity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pci/"
summary: "Základní identifikátor pro buňky LTE a NR, s rozsahem od 0 do 1007 v LTE (504 skupin po 3) a od 0 do 1007 v NR (1008 unikátních hodnot). Používá se pro identifikaci buňky, synchronizaci a demodulační"
---

PCI je základní číselný identifikátor pro buňky LTE a NR, používaný pro identifikaci buňky, synchronizaci a demodulační signály během vyhledávání buňky, předávání spojení (handoveru) a správy rádiových prostředků.

## Popis

Physical Cell Identity (PCI) je kritický identifikátor fyzické vrstvy v systémech LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) i NR (NG-RAN). Není parametrem konfigurovatelným operátorem jako [ECI](/mobilnisite/slovnik/eci/), ale identifikátorem na rádiové úrovni používaným k rozlišení různých buněk na rozhraní vzduchu. V LTE je PCI celočíselná hodnota od 0 do 503, která je odvozena ze dvou složek: skupiny fyzické vrstvy buněčné identity (N_ID^1, rozsah 0-167) a identity fyzické vrstvy v rámci skupiny (N_ID^2, rozsah 0-2), což dává 168 skupin * 3 identity = 504 unikátních PCI. V NR je rozsah PCI rozšířen na 0-1007, což poskytuje 1008 unikátních hodnot. PCI je přímo použit při generování několika downlink referenčních signálů, nejdůležitěji Primary Synchronization Signal ([PSS](/mobilnisite/slovnik/pss/)) a Secondary Synchronization Signal ([SSS](/mobilnisite/slovnik/sss/)), což jsou první signály, které UE detekuje během vyhledávání buňky.

Proces přiřazování PCI a jeho role je ústřední pro provoz sítě. Během počátečního vyhledávání buňky UE skenuje sekvence PSS/SSS. Detekované sekvence přímo odpovídají N_ID^2 (z PSS) a N_ID^1 (z SSS), z nichž se PCI vypočítá. Jakmile je PCI znám, může UE dekódovat buňce-specifické referenční signály ([CRS](/mobilnisite/slovnik/crs/) v LTE, [CSI-RS](/mobilnisite/slovnik/csi-rs/)/SSB v NR), které jsou zakódovány (scramblovány) pomocí PCI. Toto kódování zajišťuje, že referenční signály ze sousedních buněk jsou ortogonální nebo mají nízké rušení, což umožňuje přesný odhad kanálu a měření (jako [RSRP](/mobilnisite/slovnik/rsrp/)/[RSRQ](/mobilnisite/slovnik/rsrq/)). PCI také určuje mapování fyzických bloků prostředků pro řídicí kanály jako PDCCH, což ovlivňuje koordinaci mezibuněčného rušení.

Plánování PCI je klíčový úkol správy sítě. Protože prostor PCI je omezený, je v rozsáhlých sítích nutná jeho opakovaná využitelnost (reuse). Hlavní výzvou je vyhnout se záměně a konfliktu PCI. Ke konfliktu PCI dochází, když dvě sousední buňky používají stejné PCI, což způsobuje vážné rušení pro UE na hranicích buněk. K záměně PCI dochází, když buňka přijímá signál dvou nesousedních buněk používajících stejné PCI, což může narušit procesy předávání spojení. Proto jsou pro dynamickou správu přiřazování PCI specifikovány funkce Self-Organizing Network (SON), jako Automatic Neighbor Relation (ANR) a Automatic PCI Configuration and Conflict Resolution. Role PCI se rozšiřuje i na mobilitu, protože je použit v algoritmech pro hlášení měření a rozhodování o předání spojení, což z něj činí základní prvek pro správu rádiových prostředků a výkon sítě.

## K čemu slouží

PCI byl zaveden s LTE v Release 8, aby poskytl škálovatelnou a efektivní metodu pro unikátní identifikaci rádiových buněk na fyzické vrstvě, nahrazující složitější plánování scramblovacích kódů v UMTS. V UMTS sloužil podobnému účelu Primary Scrambling Code (PSC), ale měl omezení v plánování kódů a správě rušení. Strukturované odvození PCI ze sekvencí PSS/SSS zjednodušuje a urychluje proces vyhledávání buňky pro UE, což umožňuje rychlejší počáteční přístup a předávání spojení. Jeho primárním účelem je jednoznačně identifikovat buňku v místní geografické oblasti za účelem usnadnění synchronizace, odhadu kanálu a správy rušení. Omezený prostor PCI (504/1008) nutí k opakovanému využití, což zavedlo problém konfliktů PCI a motivovalo vývoj automatizačních funkcí SON k řešení této provozní výzvy. Existuje proto, aby oddělil fyzickou rádiovou identifikaci od identifikace buňky na vyšší vrstvě (ECGI/CGI), což umožňuje efektivní rádiové procedury nezávislé na adresování core sítě.

## Klíčové vlastnosti

- Unikátní identifikátor buňky na fyzické vrstvě (0-503 v LTE, 0-1007 v NR).
- Odvozen ze synchronizačních signálů (PSS a SSS) pro rychlé vyhledání a zachycení buňky.
- Použit pro kódování (scrambling) buňce-specifických referenčních signálů (CRS, CSI-RS, DM-RS) pro odhad kanálu.
- Určuje frekvenční posun referenčních signálů, což ovlivňuje mezibuněčné rušení.
- Základní parametr pro správu rádiových prostředků, předávání spojení a algoritmy SON.
- Omezený rozsah hodnot vyžaduje pečlivé plánování sítě nebo automatizované řešení konfliktů.

## Související pojmy

- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [SSS – Secondary Synchronization Signal](/mobilnisite/slovnik/sss/)
- [ECGI – E-UTRAN Cell Global Identification](/mobilnisite/slovnik/ecgi/)
- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [ANR – Automatic Neighbour Relationship](/mobilnisite/slovnik/anr/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study
- **TS 36.863** (Rel-12) — CRS Interference Mitigation for Homogeneous Networks
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 37.816** (Rel-16) — RAN-centric Data Collection & Utilization Study
- **TS 37.822** (Rel-12) — SON Enhancements for UE Types and Active Antennas
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.744** (Rel-19) — AI/ML for NR Mobility Study

---

📖 **Anglický originál a plná specifikace:** [PCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pci/)
