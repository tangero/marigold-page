---
slug: "laa"
url: "/mobilnisite/slovnik/laa/"
type: "slovnik"
title: "LAA – Licensed-Assisted Access"
date: 2025-01-01
abbr: "LAA"
fullName: "Licensed-Assisted Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/laa/"
summary: "Licensed-Assisted Access (LAA) je technologie 3GPP, která agreguje nelicencované spektrum (např. 5 GHz) s licencovanými nosnými kmitočty pro zvýšení kapacity LTE, přičemž využívá Naslouchání-před-vysí"
---

LAA je technologie 3GPP, která agreguje nelicencované spektrum s licencovanými nosnými kmitočty pro zvýšení kapacity LTE, přičemž využívá mechanismus Naslouchání-před-vysíláním (Listen-Before-Talk) k zajištění spravedlivé koexistence se systémy jako je Wi-Fi.

## Popis

Licensed-Assisted Access (LAA) je funkce zavedená ve specifikaci 3GPP Release 13, která umožňuje Long-Term Evolution (LTE) provoz v nelicencovaných pásmech, především v pásmu 5 GHz, agregací s licencovaným primárním nosným kmitočtem. Je součástí širších iniciativ LTE-Unlicensed (LTE-U) a později 5G [NR-U](/mobilnisite/slovnik/nr-u/). LAA využívá agregaci nosných kmitočtů ([CA](/mobilnisite/slovnik/ca/)), kde primární buňka (PCell) funguje v licencovaném spektru a poskytuje klíčové řídicí funkce a správu mobility, zatímco jedna nebo více sekundárních buněk (SCell) pracuje v nelicencovaném spektru a dodává dodatečnou datovou kapacitu pro downlink (a později i uplink). Základním mechanismem pro koexistenci s jinými nelicencovanými technologiemi, jako je Wi-Fi, je Naslouchání-před-vysíláním ([LBT](/mobilnisite/slovnik/lbt/)), což je forma snímání nosné podobná [CSMA/CA](/mobilnisite/slovnik/csma-ca/), kdy LAA základnová stanice (eNodeB) před vysíláním po určitou dobu snímá kanál, aby se vyhnula kolizím.

Z architektonického hlediska LAA zahrnuje vylepšení eNodeB a UE. eNodeB obsahuje LAA SCell, který provádí procedury LBT: využívá detekci energie nebo snímání preambule k určení, zda je kanál volný. Pokud je volný, vysílá po náhodném odstupu; pokud je obsazený, čeká. Vysílací bloky jsou omezeny maximální dobou obsazení kanálu ([MCOT](/mobilnisite/slovnik/mcot/)), aby byla zajištěna spravedlivost. UE neprovádí LBT pro příjem downlinku, ale podporuje signalizaci specifickou pro LAA, jako jsou referenční signály pro objevování buněk ([DRS](/mobilnisite/slovnik/drs/)) pro detekci buněk a zpětnou vazbu informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)). Uplink LAA, zavedený později, vyžaduje, aby UE před vysíláním na nelicencované SCell provedlo LBT. Protokolový stack rozšiřuje LTE [MAC](/mobilnisite/slovnik/mac/) a PHY pro obsluhu operací v nelicencovaných pásmech, včetně nových fyzických kanálů a signálů přizpůsobených pro koexistenci.

V síti jsou LAA SCell konfigurovány a aktivovány PCell prostřednictvím signalizace RRC a MAC. Mohou být nasazeny jako samostatné small buňky nebo jako součást sady pro agregaci nosných kmitočtů makro buňky. Specifikace definují podrobné procedury pro přístup ke kanálu (např. rámovou strukturu, kategorie LBT), parametry vysílání (např. šířku pásma, limity hustoty výkonového spektra) a požadavky na výkon (např. 36.213, 36.331). LAA výrazně zvyšuje kapacitu LTE a nabízí přenosové rychlosti na úrovni gigabitů při kombinaci s licencovanými nosnými kmitočty, a je předstupněm k 5G NR v nelicencovaných pásmech (NR-U). Umožňuje operátorům využít hojné nelicencované spektrum k uspokojení rostoucí poptávky po datech, zejména v hustě obydlených městských oblastech a vnitřních prostorech, a zároveň zajišťuje harmonický provoz se zavedenými Wi-Fi systémy prostřednictvím standardizovaných mechanismů koexistence.

## K čemu slouží

LAA byl vyvinut k řešení nedostatku spektra, kterému čelili mobilní operátoři v důsledku explozivního růstu datového provozu s rozšířením chytrých telefonů a aplikací náročných na šířku pásma. Licencované spektrum je vzácné a drahé, což omezuje rozšiřování kapacity. Nelicencované spektrum, zejména pásmo 5 GHz, nabízelo velké množství dostupné šířky pásma, ale dominovala mu Wi-Fi. Raná proprietární řešení LTE-U se vyhýbala LBT, což riskovalo nespravedlivou koexistenci s Wi-Fi a regulační problémy v regionech jako Evropa a Japonsko, kde je LBT vyžadováno. 3GPP standardizovalo LAA v Release 13, aby poskytlo globálně harmonizovaný přístup, který zajišťuje spravedlivé sdílení s Wi-Fi a splňuje regulační požadavky, což operátorům umožňuje bezpečně rozšiřovat své sítě.

Motivací pro LAA bylo spojit spolehlivost a kontrolu licencovaného spektra s kapacitním posílením nelicencovaných pásem a vytvořit tak bezproblémový uživatelský zážitek. Na rozdíl od offloadingu na Wi-Fi, který vyžaduje samostatnou autentizaci a často trpí přerušeními mobility, LAA integruje nelicencované spektrum přímo do rámce agregace nosných kmitočtů LTE, čímž si zachovává kontrolu operátora a QoS. Řeší problém neefektivního využití nelicencovaného spektra aplikací pokročilých radiových technik LTE (např. OFDMA, MIMO) a centralizovaného plánování, které v některých scénářích mohou dosáhnout vyšší spektrální účinnosti než Wi-Fi. LAA tedy představuje strategický vývoj směrem k heterogennímu využití spektra a připravuje cestu pro 5G NR-U a budoucí technologie, které kombinují licencované, nelicencované a sdílené spektrum.

## Klíčové vlastnosti

- Využívá agregaci nosných kmitočtů s licencovanou PCell a nelicencovanou/nelicencovanými SCell pro zvýšení kapacity
- Implementuje Naslouchání-před-vysíláním (LBT) pro spravedlivou koexistenci s Wi-Fi a dalšími uživateli nelicencovaného spektra
- Podporuje provoz downlinku (od Rel-13) a uplinku (od Rel-14) v nelicencovaném spektru
- Obsahuje referenční signály pro objevování buněk (DRS) pro detekci a měření buněk v nelicencovaných pásmech
- Omezuje vysílací bloky prostřednictvím maximální doby obsazení kanálu (MCOT) pro zajištění spravedlivosti
- Integruje se s funkcemi LTE-Advanced jako 256-QAM, 4x4 MIMO a agregace nosných kmitočtů až do 32 nosných

## Související pojmy

- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)
- [LBT – Listen Before Talk](/mobilnisite/slovnik/lbt/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.729** (Rel-15) — Unlicensed Spectrum Offloading System Enhancements
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.307** (Rel-19) — Release-Independent Frequency Band Support
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.789** (Rel-13) — LAA Multi-Node Coexistence Test Methodology
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TS 37.213** (Rel-19) — Shared Spectrum Physical Layer Procedures
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [LAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/laa/)
