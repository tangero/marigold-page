---
slug: "cd-ssb"
url: "/mobilnisite/slovnik/cd-ssb/"
type: "slovnik"
title: "CD-SSB – Cell-Defining Synchronization Signal Block"
date: 2025-01-01
abbr: "CD-SSB"
fullName: "Cell-Defining Synchronization Signal Block"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cd-ssb/"
summary: "CD-SSB (Cell-Defining SSB) je primární blok synchronizačních signálů (SSB), který uživatelský terminál (UE) používá k počáteční detekci, synchronizaci a identifikaci buňky 5G NR. Jedná se o základní s"
---

CD-SSB je primární blok synchronizačních signálů (Synchronization Signal Block), který definuje buňku 5G NR a umožňuje uživatelskému terminálu (UE) tuto buňku nejprve detekovat, synchronizovat se s ní a identifikovat její časování, frekvenci a základní systémové informace.

## Popis

CD-SSB (Cell-Defining Synchronization Signal Block) je klíčový signál fyzické vrstvy v 5G New Radio (NR). Jedná se o konkrétní instanci obecnějšího bloku synchronizačních signálů a [PBCH](/mobilnisite/slovnik/pbch/) (SSB), který zahrnuje primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)), sekundární synchronizační signál ([SSS](/mobilnisite/slovnik/sss/)) a fyzický vysílací kanál (PBCH). CD-SSB je konkrétní SSB, který uživatelský terminál (UE) používá k provedení počátečního vyhledávání buňky, k dosažení downlinkové synchronizace v čase a frekvenci a k dekódování hlavního informačního bloku ([MIB](/mobilnisite/slovnik/mib/)) přenášeného na PBCH. MIB poskytuje základní parametry, jako je číslo systémového rámce ([SFN](/mobilnisite/slovnik/sfn/)) a informace potřebné pro dekódování zbývajících bloků systémových informací ([SIB](/mobilnisite/slovnik/sib/)), které jsou naplánovány na fyzickém downlinkovém sdíleném kanálu ([PDSCH](/mobilnisite/slovnik/pdsch/)).

Z architektonického hlediska je CD-SSB vysílán v konkrétním vzoru definovaném synchronizačním rastrem. Synchronizační rastr je sada globálních frekvenčních pozic, na kterých musí UE hledat SSB. Střední frekvence CD-SSB a s ní spojený bod A (referenční bod mřížky společných zdrojových bloků) definují absolutní frekvenční umístění mřížky zdrojových bloků buňky. Toto je kritická funkce, protože slouží jako kotva pro celé číslování fyzických zdrojových bloků ([PRB](/mobilnisite/slovnik/prb/)) pro downlink. Časová pozice CD-SSB v rádiovém rámci je také striktně definována, vyskytuje se v konkrétních slotech a symbolech podle rozteče podnosných (SCS) a frekvenčního pásma (FR1 nebo FR2).

Co se týče fungování, UE prohledává synchronizační rastr. Po detekci PSS dosáhne časování na úrovni symbolu a identifikuje jednu ze tří možných hodnot skupiny fyzické identity buňky (PCI). Následný SSS poskytne časování rámce (identifikuje hranici slotu a půlrámce) a identifikuje konkrétní PCI v této skupině, čímž získá kompletní PCI. Pomocí časování odvozeného z PSS/SSS UE demoduluje PBCH uvnitř stejného SSB. Datová část PBCH obsahuje MIB, který zahrnuje 6 nejméně významných bitů SFN, společnou rozteč podnosných pro většinu kanálů a konfiguraci PDCCH pro SIB1 (konkrétně ControlResourceSet Zero a SearchSpace Zero). Referenční signály pro demodulaci (DM-RS) pro PBCH jsou také použity pro zpřesnění frekvenčního odhadu.

Klíčovým aspektem CD-SSB je jeho role v řízení paprsků, zejména pro frekvence nad 6 GHz (FR2). V těchto pásmech může síť vysílat více SSB v různých prostorových směrech (paprscích) jako část sady SS burstů. Avšak pouze jeden z těchto paprsků nese CD-SSB. UE měří referenční výkon přijatého signálu (RSRP) SSB a paprsek odpovídající CD-SSB je použit jako reference pro hlášení kvality buňky a pro počáteční proceduru náhodného přístupu (RACH). Prostředky fyzického kanálu pro náhodný přístup (PRACH) spojené s CD-SSB, definované v SIB1, jsou k němu přímo navázány, čímž se stanoví prostorový vztah pro počáteční uplinkový přenos.

## K čemu slouží

CD-SSB byl vytvořen, aby splnil základní požadavek jakéhokoli buněčného systému: umožnit zařízení najít síť a připojit se k ní. V 5G NR je tento požadavek umocněn použitím mnohem širšího spektra frekvencí (od pásem pod 1 GHz až po milimetrové vlny), různorodými scénáři nasazení (makrobuňky, small cell, indoor) a kritickou potřebou provozu založeného na paprscích na vysokých frekvencích. CD-SSB poskytuje jednotný, efektivní a robustní mechanismus pro počáteční objev buňky ve všech těchto prostředích.

Historicky v LTE plnily primární a sekundární synchronizační signály (PSS/SSS) a fyzický vysílací kanál (PBCH) podobný účel, ale byly to samostatné entity v časově-frekvenční mřížce. Integrace těchto signálů do jediného, samostatného bloku (SSB) v 5G NR zjednodušuje počáteční vyhledávací proceduru a je vhodnější pro beamforming. Označení konkrétního SSB jako 'Cell-Defining' odstraňuje nejednoznačnost v nasazeních s více paprsky. Jasně identifikuje, který paprsek poskytuje autoritativní informace o časování a frekvenci pro definování mřížky zdrojových bloků buňky a struktury systémového rámce. To je nezbytné pro synchronizaci sítě a pro UE provádějící měření a předávání spojení mezi buňkami.

CD-SSB dále řeší omezení pevné struktury synchronizačních signálů. Propojením CD-SSB s flexibilním synchronizačním rastrem a umožněním konfigurovat jeho periodicitu (např. 5 ms, 10 ms, 20 ms, 40 ms, 80 ms, 160 ms) umožňuje významné úspory energie jak pro síť, tak pro UE. Ve scénářích s nízkým provozem nebo rozšířením pokrytí může síť vysílat CD-SSB méně často, čímž sníží spotřebu energie, a přitom zachová viditelnost buňky pro UE v idle módu provádějící diskontinuální příjem (DRX).

## Klíčové vlastnosti

- Definuje absolutní frekvenční umístění (bod A) a mřížku zdrojových bloků buňky 5G NR
- Přenáší hlavní informační blok (MIB) prostřednictvím PBCH, který obsahuje základní systémové parametry
- Poskytuje fyzickou identitu buňky (PCI) prostřednictvím kombinovaných sekvencí PSS a SSS
- Slouží jako časová reference pro číslo systémového rámce (SFN) a strukturu slotů buňky
- Působí jako referenční signál pro měření na úrovni buňky (např. SS-RSRP, SS-SINR) a hlášení paprsků
- Slouží jako prostorová kotva pro počáteční náhodný přístup, s přidruženými prostředky PRACH

## Související pojmy

- [PSS – Packet Switched Streaming Service](/mobilnisite/slovnik/pss/)
- [SSS – Secondary Synchronization Signal](/mobilnisite/slovnik/sss/)
- [PBCH – Physical Broadcast Channel](/mobilnisite/slovnik/pbch/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [CD-SSB na 3GPP Explorer](https://3gpp-explorer.com/glossary/cd-ssb/)
