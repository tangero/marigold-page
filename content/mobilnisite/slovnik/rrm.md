---
slug: "rrm"
url: "/mobilnisite/slovnik/rrm/"
type: "slovnik"
title: "RRM – Radio Resource Management"
date: 2025-01-01
abbr: "RRM"
fullName: "Radio Resource Management"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rrm/"
summary: "Radio Resource Management (RRM, správa rádiových prostředků) je soubor algoritmů a mechanismů v mobilních sítích, které optimalizují přidělování a využívání rádiových prostředků, jako je šířka pásma,"
---

RRM je soubor algoritmů v mobilních sítích, které optimalizují přidělování rádiových prostředků za účelem zajištění efektivního provozu, udržení kvality služeb a maximalizace kapacity sítě.

## Popis

Radio Resource Management (RRM, správa rádiových prostředků) zahrnuje soubor funkcí a algoritmů v rádiové přístupové síti (RAN), které jsou odpovědné za efektivní využití omezených prostředků rozhraní vzduchového rozhraní. Jeho hlavním cílem je garantovat požadovanou kvalitu služeb (QoS) pro různá spojení při současné maximalizaci celkové kapacity systému a pokrytí. RRM funguje tak, že kontinuálně monitoruje rádiové podmínky, vytížení provozu a schopnosti uživatelského zařízení (UE), aby mohlo činit dynamická rozhodnutí v reálném čase o přidělování prostředků, řízení výkonu a správě mobility.

Z architektonického hlediska jsou RRM funkce rozděleny mezi síťové entity, jako je NodeB/eNodeB/gNB a Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) v 3G, nebo centralizovány v gNB-CU v 5G. Mezi klíčové algoritmické komponenty patří Přijímací kontrola (Admission Control), která rozhoduje, zda lze navázat nové spojení na základě aktuálního zatížení a požadované QoS; Plánovač paketů (Packet Scheduling), který přiděluje bloky fyzických prostředků ([PRB](/mobilnisite/slovnik/prb/)) nebo časové sloty aktivním uživatelům, často s prioritami založenými na kvalitě kanálu a třídě QoS; Adaptace spoje (Link Adaptation), která vybírá optimální modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)) pro aktuální rádiové podmínky kanálu; a Řízení výkonu (Power Control), které upravuje vysílací výkon pro udržení kvality signálu při minimalizaci rušení sousedním buňkám.

Další kritickou funkcí RRM je Správa mobility (Mobility Management), která zajišťuje předávání spojení (handover). To zahrnuje měření kvality signálu z obsluhující a sousedních buněk, rozhodování o vhodném okamžiku pro zahájení předání a výběr nejlepší cílové buňky pro zajištění plynulé kontinuity služby. Vyvažování zatížení (Load Balancing) je také základním úkolem RRM, který rovnoměrně distribuuje provoz mezi buňky, aby se zabránilo přetížení a zlepšilo využití prostředků. V 5G NR se RRM vyvinulo tak, aby podporovalo složitější scénáře, jako je duální konektivita, agregace nosných a síťové segmenty (network slicing), což vyžaduje koordinaci napříč více frekvenčními vrstvami a dokonce mezi 4G a 5G rádiovými rozhraními.

Role RRM je klíčová při převodu požadavků služeb vysoké úrovně na přesné akce na nízké úrovni rádiového rozhraní. Úzce spolupracuje s protokoly vyšších vrstev a s jádrem sítě při prosazování politik. Inteligentní správou rušení, šířky pásma a výkonu RRM přímo ovlivňuje klíčové ukazatele výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)), jako je propustnost, latence, míra ztráty hovorů a spektrální účinnost, což z něj činí základní kámen výkonu a optimalizace RAN.

## K čemu slouží

RRM existuje, aby řešilo základní výzvu efektivního sdílení omezeného, k rušení náchylného rádiového spektra mezi potenciálně velkým počtem uživatelů s různorodými požadavky na služby. Rané mobilní systémy čelily problémům, jako jsou ztráty hovorů, špatná kvalita hlasu a nízká kapacita, kvůli neřízenému rušení a statickému přidělování prostředků. RRM bylo zavedeno, aby přineslo inteligenci a dynamiku na vzdušné rozhraní a umožnilo sítím přizpůsobovat se měnícím se podmínkám.

Motivace pro RRM rostla s každou generací mobilní technologie. V 2G GSM byl důraz kladen na základní přepojování okruhů pro hlas. S příchodem 3G UMTS a zavedením [CDMA](/mobilnisite/slovnik/cdma/) se řízení rušení stalo ještě kritičtějším, což si vyžádalo sofistikované mechanismy řízení výkonu a měkkého předávání hovorů (soft handover). Přechod na přepojování paketů pro data v 4G LTE vyžadoval pokročilé algoritmy plánování paketů pro zvládnutí trhaného provozu a upřednostňování různých datových toků. RRM vyřešilo problém, jak doručit vysoké datové rychlosti a nízkou latenci současně více uživatelům na sdíleném kanálu.

V 5G se účel RRM rozšířil o podporu nebývalého rozsahu případů užití – od rozšířeného mobilního širokopásmového připojení (eMBB) přes ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) až po komunikaci s masivním množstvím strojových zařízení (mMTC). RRM nyní musí spravovat prostředky nejen pro buňky, ale také pro síťové segmenty (slices), z nichž každý má své vlastní výkonnostní cíle. Řeší omezení předchozích přístupů začleněním strojového učení pro prediktivní přidělování prostředků, podporou širších šířek pásma prostřednictvím agregace nosných a správou konektivity v heterogenních sítích (HetNets), čímž zajišťuje, že rádiové prostředky jsou využívány optimálně k naplnění přísných a různorodých požadavků moderních mobilních služeb.

## Klíčové vlastnosti

- Dynamické přidělování prostředků a plánování paketů na základě kvality kanálu a QoS
- Přijímací kontrola (Admission Control) pro regulaci zatížení sítě a prevenci přetížení
- Adaptace spoje (Link Adaptation) pro optimalizaci modulačních a kódovacích schémat (MCS) podle aktuálních rádiových podmínek
- Řízení výkonu (Power Control) pro udržení kvality signálu a minimalizaci mezibuněčného rušení
- Správa mobility (Mobility Management) pro plynulé předávání spojení mezi buňkami
- Vyvažování zatížení (Load Balancing) pro rovnoměrné rozložení provozu po síti

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TS 32.827** (Rel-10) — UE Management over Itf-N for MDT/SON
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 25 specifikací

---

📖 **Anglický originál a plná specifikace:** [RRM na 3GPP Explorer](https://3gpp-explorer.com/glossary/rrm/)
