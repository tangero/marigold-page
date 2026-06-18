---
slug: "tdd"
url: "/mobilnisite/slovnik/tdd/"
type: "slovnik"
title: "TDD – Time Division Duplex(ing)"
date: 2026-01-01
abbr: "TDD"
fullName: "Time Division Duplex(ing)"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tdd/"
summary: "TDD je duplexní metoda, při které se přenosy v uplinku a downlinku dělí o stejný kmitočtový kanál, ale jsou odděleny v čase. Umožňuje dynamické přidělování zdrojů na základě poptávky po provozu, což v"
---

TDD je duplexní metoda, při které se přenosy v uplinku a downlinku uskutečňují na stejném kmitočtovém kanálu, ale jsou odděleny v čase, což umožňuje dynamické přidělování zdrojů a efektivní využití nespárovaného spektra.

## Popis

Time Division Duplex (TDD) je základní duplexní schéma v bezdrátových komunikacích, při kterém se stejný nosný kmitočet používá pro přenosy v uplinku ([UL](/mobilnisite/slovnik/ul/)) i downlinku ([DL](/mobilnisite/slovnik/dl/)), přičemž k oddělení dochází časovým dělením. V systémech 3GPP se TDD používá napříč technologiemi včetně [TD-SCDMA](/mobilnisite/slovnik/td-scdma/), LTE-TDD a NR TDD, s podrobnými specifikacemi rozprostřenými v řadě dokumentů, jako jsou série 36. a 38. Provoz zahrnuje rozdělení času na rámce a podrámce, z nichž každý obsahuje sloty určené pro UL nebo DL, spolu se speciálními sloty pro přepínání a ochranné intervaly.

Struktura TDD rámce je vysoce konfigurovatelná a umožňuje různé konfigurace poměru uplink-downlink podle charakteru provozu. Například v LTE existuje sedm konfigurací od převážně DL až po vyvážené poměry, zatímco NR zavádí ještě větší flexibilitu s plánováním na bázi slotů. Mezi klíčové komponenty patří přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/)), ochranný interval ([GP](/mobilnisite/slovnik/gp/)) pro zabránění interference [UL](/mobilnisite/slovnik/up-link/)/DL a přepínací body, kde dochází k přechodům. Synchronizace je klíčová a dosahuje se pomocí synchronizačních signálů a mechanismů časového předstihu pro zarovnání přenosů od UE.

V síťové architektuře TDD ovlivňuje návrh základnové stanice i UE, což vyžaduje rychlé vysokofrekvenční přepínače a přesné řízení časování. Umožňuje dynamické sdílení spektra, kdy lze zdroje přerozdělovat v reálném čase podle poptávky, což zvyšuje efektivitu pro trhavý datový provoz. TDD také umožňuje pokročilé funkce, jako je reciprocita kanálu, kdy lze stav downlink kanálu odvodit z měření v uplinku, což podporuje massive [MIMO](/mobilnisite/slovnik/mimo/) a beamforming. Přináší však také výzvy, jako je řízení interference mezi sousedními buňkami, které se řeší koordinovaným plánováním a zarovnáním časování rámců.

## K čemu slouží

TDD existuje za účelem efektivního využití spektra, zejména nespárovaných pásem, tím, že umožňuje flexibilní přidělování zdrojů pro uplink a downlink. Řeší problém asymetrie provozu v mobilních sítích, kde poptávka po datech často výrazně převažuje na straně downlinku, na rozdíl od symetrického hlasového provozu. Motivace pro TDD sahá do raných digitálních bezdrátových systémů, přičemž jeho přijetí v 3GPP v rámci UMTS a rozšíření v LTE/NR sloužilo k podpoře rostoucích potřeb mobilního širokopásmového připojení.

Historicky dominoval Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)) díky jednodušší implementaci, ale vyžadoval spárované spektrum, které je vzácné. TDD tuto limitaci překonalo tím, že umožnilo provoz v nespárovaných pásmech, často dostupných za nižší cenu. Také umožňuje dynamickou adaptaci na měnící se podmínky provozu, což je klíčové pro služby založené na internetu. Vytvoření a vývoj TDD v 3GPP bylo hnáno potřebou vyšší spektrální účinnosti a podpory různých scénářů nasazení, včetně hustých městských oblastí a privátních sítí.

## Klíčové vlastnosti

- Dynamické přidělování zdrojů pro uplink a downlink na základě provozu
- Provoz v nespárovaných kmitočtových pásmech
- Konfigurovatelné struktury rámců s více UL/DL vzory
- Podpora reciprocity kanálu v pokročilých anténních systémech
- Ochranné intervaly a přepínací body pro zmírnění interference
- Synchronizační mechanismy pro zarovnání síťového časování

## Související pojmy

- [FDD – Frequency Division Duplexing](/mobilnisite/slovnik/fdd/)
- [TD-SCDMA – Time Division Synchronous Code Division Multiple Access](/mobilnisite/slovnik/td-scdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- … a dalších 139 specifikací

---

📖 **Anglický originál a plná specifikace:** [TDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/tdd/)
