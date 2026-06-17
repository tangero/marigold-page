---
slug: "hs-dsch"
url: "/mobilnisite/slovnik/hs-dsch/"
type: "slovnik"
title: "HS-DSCH – High Speed Downlink Shared Channel"
date: 2025-01-01
abbr: "HS-DSCH"
fullName: "High Speed Downlink Shared Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hs-dsch/"
summary: "Transportní kanál v UMTS HSPA, který umožňuje vysokorychlostní přenos paketových dat ve směru downlink dynamickým sdílením rádiových prostředků mezi více uživateli. Je to hlavní kanál pro doručování u"
---

HS-DSCH je hlavní vysokorychlostní transportní kanál v UMTS HSPA, který dynamicky sdílí rádiové prostředky mezi více uživateli pro přenos paketových dat, čímž zvyšuje spektrální účinnost a špičkové přenosové rychlosti.

## Popis

High Speed Downlink Shared Channel (HS-DSCH) je klíčový transportní kanál zavedený jako součást funkce High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) ve specifikaci 3GPP Release 5. Působí v UMTS Terrestrial Radio Access Network (UTRAN) a je v podstatě sdíleným médiem, což znamená, že jeho přenosové časové intervaly (TTI) a kanalizační kódy jsou dynamicky přidělovány Node B (základnovou stanicí) více uživatelským zařízením (UE). Na rozdíl od vyhrazených kanálů si HS-DSCH neudržuje trvalé, exkluzivní přidělení pro jediného uživatele, což umožňuje vysoce efektivní statistické multiplexování paketového datového provozu. Kanál je charakterizován krátkým, pevným TTI 2 ms, adaptivní modulací a kódováním ([AMC](/mobilnisite/slovnik/amc/)), rychlým hybridním [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)) fyzické vrstvy s měkkým kombinováním a rychlým plánováním založeným na Node B. Tyto mechanismy umožňují systému rychle se přizpůsobovat měnícím se rádiovým podmínkám a požadavkům provozu na úrovni každého TTI.

Provoz HS-DSCH je pod přísnou kontrolou Node B. UE sleduje sadu High-Speed Shared Control Channels ([HS-SCCH](/mobilnisite/slovnik/hs-scch/)), aby zjistilo, kdy jsou pro něj naplánována data. HS-SCCH nese kritické řídicí informace pro downlink, včetně sady kanalizačních kódů, modulačního schématu (QPSK nebo [16QAM](/mobilnisite/slovnik/16qam/)), velikosti transportního bloku a informací o procesu HARQ. Po úspěšném dekódování HS-SCCH UE přesně ví, kde a jak má přijímat svá data na [HS-PDSCH](/mobilnisite/slovnik/hs-pdsch/) (fyzickém kanálu přenášejícím HS-DSCH). Související zpětná vazba v uplinku je poskytována prostřednictvím High-Speed Dedicated Physical Control Channel ([HS-DPCCH](/mobilnisite/slovnik/hs-dpcch/)), který nese potvrzení HARQ (ACK/NACK) a indikátor kvality kanálu (CQI). CQI hlášené UE informuje plánovač Node B o podmínkách downlink kanálu, což umožňuje AMC.

Z architektonického hlediska představuje HS-DSCH přesun klíčových funkcí správy rádiových prostředků z Radio Network Controller (RNC) do Node B. To zahrnuje plánování, HARQ a AMC. Toto přemístění snižuje latenci a umožňuje rychlejší reakční časy, což je klíčové pro podporu vysokorychlostních, burstních datových služeb. HS-DSCH je mapován na jeden nebo několik High-Speed Physical Downlink Shared Channels (HS-PDSCH), což jsou kanály se sekundárním skramblovacím kódem. Maximální počet souběžných HS-PDSCH (a tím i špičková datová rychlost) se v následujících verzích zvyšoval se zavedením modulace vyššího řádu (64QAM v Rel-7), MIMO (Multiple-Input Multiple-Output v Rel-7) a vícekanálového HSDPA (DC-HSDPA v Rel-8, 4C-HSDPA a později 8C-HSDPA). HS-DSCH je hlavním nosičem dat uživatelské roviny ve směru downlink v sítích HSPA a tvoří základ pro mobilní širokopásmové služby před rozšířeným nasazením LTE.

## K čemu slouží

HS-DSCH byl vytvořen, aby řešil neefektivnost původních vyhrazených kanálů (DCH) UMTS Release 99 pro paketově spínané datové služby. DCH byl navržen s ohledem na okruhově spínaný hlas, s relativně dlouhými TTI (10, 20, 40 nebo 80 ms) a centralizovaným plánováním v RNC. Tato architektura vedla k vysoké latenci, neefektivnímu využití prostředků pro burstní internetový provoz a omezeným špičkovým datovým rychlostem. Hlavní motivací pro HSDPA a HS-DSCH bylo dramaticky zlepšit výkon downlink paketových dat v sítích UMTS, aby mohly konkurovat novým technologiím a uspokojit rostoucí poptávku uživatelů po mobilním přístupu k internetu.

Zavedení HS-DSCH tyto limity vyřešilo prostřednictvím souboru vylepšení souhrnně označovaných jako HSPA. Přesunutím plánování do Node B a použitím krátkého 2ms TTI byly drasticky zkráceny reakční časy na změny kanálu a uživatelské požadavky. Sdílená povaha kanálu umožnila přidělovat prostředky okamžitě uživateli s nejlepšími podmínkami kanálu nebo nejvyšší prioritou, čímž se maximalizovala propustnost buňky prostřednictvím diverzity více uživatelů. Rychlý HARQ na fyzické vrstvě poskytoval robustní adaptaci spojení s rychlou opravou chyb, což snížilo potřebu opakovaných přenosů na vyšších vrstvách a s nimi spojená zpoždění. Společně tyto funkce přeměnily UMTS na vysoce efektivní paketově spínanou technologii rádiového přístupu schopnou poskytovat cenově výhodný mobilní broadband, čímž prodloužily komerční životnost sítí 3G hluboko do éry 4G.

## Klíčové vlastnosti

- Přidělování prostředků sdíleného kanálu pro statistické multiplexování
- Krátký přenosový časový interval (TTI) 2 ms pro snížení latence
- Rychlé paketové plánování založené na Node B (např. Proportional Fair, Max C/I)
- Rychlý hybridní ARQ (HARQ) fyzické vrstvy s přírůstkovou redundancí
- Adaptivní modulace a kódování (AMC) založené na zpětné vazbě CQI od UE
- Podpora modulace vyššího řádu (QPSK, 16QAM, 64QAM) a MIMO

## Související pojmy

- [HS-PDSCH – High Speed Physical Downlink Shared Channel](/mobilnisite/slovnik/hs-pdsch/)
- [HS-SCCH – High Speed Physical Downlink Shared Control Channel](/mobilnisite/slovnik/hs-scch/)
- [HS-DPCCH – High Speed Dedicated Physical Control Channel (Uplink)](/mobilnisite/slovnik/hs-dpcch/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- … a dalších 19 specifikací

---

📖 **Anglický originál a plná specifikace:** [HS-DSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/hs-dsch/)
