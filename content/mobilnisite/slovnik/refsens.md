---
slug: "refsens"
url: "/mobilnisite/slovnik/refsens/"
type: "slovnik"
title: "REFSENS – Reference Sensitivity power level"
date: 2025-01-01
abbr: "REFSENS"
fullName: "Reference Sensitivity power level"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/refsens/"
summary: "REFSENS je klíčový parametr výkonu přijímače definující minimální úroveň výkonu vstupního signálu, při které může UE dosáhnout stanovené chybovosti. Je zásadní pro určení pokrytí, výpočet rozpočtu rád"
---

REFSENS je minimální úroveň výkonu vstupního signálu, při které může uživatelské zařízení dosáhnout stanovené chybovosti, což je klíčový parametr pro určení pokrytí a výpočet rozpočtu rádiového spoje v celulárních sítích.

## Popis

Referenční citlivost (REFSENS) je základní metrika výkonu přijímačů uživatelského zařízení (UE) v celulárních sítích, definovaná jako minimální úroveň přijímaného výkonu na anténním konektoru potřebná k dosažení stanovené chybovosti bitu ([BER](/mobilnisite/slovnik/ber/)) nebo bloku ([BLER](/mobilnisite/slovnik/bler/)). Měří se za ideálních podmínek s aditivním bílým Gaussovským šumem ([AWGN](/mobilnisite/slovnik/awgn/)) a na specifických referenčních měřicích kanálech. REFSENS hodnotí schopnost přijímače detekovat a dekódovat slabé signály, což přímo ovlivňuje pokrytí sítě a výpočty rozpočtu rádiového spoje. Parametr je specifikován pro různé provozní pásma, modulační schémata a šířky kanálů napříč technologiemi 3GPP včetně LTE a NR.

Měření REFSENS zahrnuje aplikaci testovacího signálu na anténní port UE a postupné snižování výkonu, dokud není dosaženo cílové chybovosti. Tento proces zajišťuje, že přijímač splňuje minimální požadavky na citlivost, které jsou nezbytné pro spolehlivý provoz na okraji buňky nebo v prostředí se slabým signálem. Mezi klíčové faktory ovlivňující REFSENS patří šumové číslo přijímače, implementační ztráty a účinnost algoritmů základního pásma. Parametr je definován pro různé fyzické kanály, jako je [PSS](/mobilnisite/slovnik/pss/)/[SSS](/mobilnisite/slovnik/sss/) pro synchronizaci a [PDSCH](/mobilnisite/slovnik/pdsch/) pro příjem dat, přičemž každý má své vlastní prahové hodnoty citlivosti.

REFSENS hraje klíčovou roli v plánování a optimalizaci sítě tím, že určuje maximální přípustný útlum na dráze mezi základnovou stanicí a UE. Používá se ve výpočtech rozpočtu rádiového spoje pro odhad poloměru buňky a zajištění konzistentní kvality služby. Standardizací REFSENS zajišťuje 3GPP interoperabilitu a konzistenci výkonu napříč zařízeními od různých výrobců. Zároveň podporuje pokroky v návrhu přijímačů, neboť motivuje ke zlepšování šumových parametrů zesilovačů, filtrů a algoritmů digitálního zpracování signálu za účelem dosažení lepší citlivosti a rozšíření pokrytí.

## K čemu slouží

REFSENS byl zaveden za účelem stanovení standardizovaného etalonu pro citlivost přijímače, aby byla zajištěna splnění minimálních výkonnostních požadavků pro spolehlivý provoz sítě u všech UE. Před standardizací mohly rozdíly v návrhu přijímačů vést k nekonzistentnímu pokrytí a uživatelskému zážitku, zejména v podmínkách slabého signálu. 3GPP definoval REFSENS, aby poskytl společnou metriku pro testování a certifikaci, umožnil spravedlivé srovnání výkonu a garantoval základní kvalitu napříč zařízeními.

Primární problém, který REFSENS řeší, je zajištění, aby UE mohla udržovat komunikační spojení na okraji pokrytí buňky, kde je síla signálu minimální. Řeší problémy související s přerušenými hovory, nízkou přenosovou rychlostí a nespolehlivou službou v náročných rádiových prostředích. Historický kontext zahrnuje vývoj od analogových k digitálním celulárním systémům, kde se citlivost přijímače stala stále kritičtější pro podporu vyšších datových rychlostí a složitých modulačních schémat.

REFSENS také podporuje efektivitu sítě tím, že umožňuje přesné výpočty rozpočtu rádiového spoje, které optimalizují umístění základnových stanic a nastavení jejich vysílacího výkonu. Motivuje k neustálému zlepšování přijímací technologie, což vede k lepší energetické účinnosti a delší výdrži baterie u UE. Vytvoření REFSENS bylo hnací silou potřeby robustního výkonu v různých scénářích nasazení, včetně venkovských oblastí, vnitřních prostředí a situací s vysokým rušením, aby celulární sítě poskytovaly konzistentní kvalitu služby po celém světě.

## Klíčové vlastnosti

- Definuje minimální přijímaný výkon pro stanovené chybovosti (BER/BLER)
- Měří se za podmínek AWGN na referenčních kanálech
- Specifikováno pro každé provozní pásmo, šířku pásma a modulační schéma
- Zásadní pro výpočet rozpočtu rádiového spoje a plánování pokrytí
- Zajišťuje interoperabilitu a konzistenci výkonu napříč UE
- Podporuje pokroky v návrhu přijímačů a zlepšování jejich citlivosti

## Související pojmy

- [AWGN – Additive White Gaussian Noise](/mobilnisite/slovnik/awgn/)

## Definující specifikace

- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 36.714** — 3GPP TR 36.714
- **TS 36.715** — 3GPP TR 36.715
- **TS 36.716** — 3GPP TR 36.716
- **TS 36.744** (Rel-14) — CBRS 3.5GHz Band Specification for US
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 36.761** (Rel-15) — Extended-Band 12 Study Report
- **TR 36.770** (Rel-18) — Technical Report for High Power UE in LTE Band 14
- … a dalších 64 specifikací

---

📖 **Anglický originál a plná specifikace:** [REFSENS na 3GPP Explorer](https://3gpp-explorer.com/glossary/refsens/)
