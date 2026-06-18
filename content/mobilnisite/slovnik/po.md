---
slug: "po"
url: "/mobilnisite/slovnik/po/"
type: "slovnik"
title: "PO – Participating Operator"
date: 2025-01-01
abbr: "PO"
fullName: "Participating Operator"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/po/"
summary: "Participující operátor (PO) je operátor, který se účastní kooperativního uspořádání sítě, jako je Multi-Operator Core Network (MOCN), dohoda o sdílení Radio Access Network (RAN) nebo síť neutrálního h"
---

PO (Participující operátor) je operátor, který přispívá zdroji nebo službami do kooperativního uspořádání sítě, jako je MOCN nebo sdílení RAN, pro vzájemný prospěch.

## Popis

Participující operátor (PO) je subjekt síťového operátora, který se účastní kooperativní dohody o sdílení síťových zdrojů s jedním nebo více dalšími operátory. Tento koncept je ústřední pro architektury sdílení sítě definované 3GPP, které umožňují více operátorům využívat společnou infrastrukturu – nejčastěji Radio Access Network (RAN) – při zachování nezávislých core sítí a správy účastníků. PO se liší od Primárního síťového operátora ([PNO](/mobilnisite/slovnik/pno/)) pro daného účastníka; jeden operátor může vystupovat jako PNO pro své vlastní účastníky a současně být PO ve sdílecí dohodě pro geografickou oblast, kde nemá vlastní nasazení RAN.

Technická implementace zahrnuje několik klíčových komponent. V modelu sdílení Multi-Operator Core Network ([MOCN](/mobilnisite/slovnik/mocn/)) více PO připojuje své nezávislé core sítě (každá se svým vlastním [MME](/mobilnisite/slovnik/mme/), [S-GW](/mobilnisite/slovnik/s-gw/), [P-GW](/mobilnisite/slovnik/p-gw/) v 4G nebo [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/) v 5G) ke sdílenému RAN uzlu (např. eNodeB nebo gNB). Sdílený RAN vysílá Public Land Mobile Network (PLMN) ID všech participujících operátorů. Když se User Equipment (UE) napojí na tuto buňku, vidí více PLMN jako dostupných. UE na základě své konfigurace a síťových výběrových politik vybere jeden PLMN (svého PNO) a zahájí spojení. RAN uzel pomocí vybraného PLMN ID směruje signalizaci do odpovídajícího prvku core sítě příslušného PO. To vyžaduje vylepšení RAN protokolů (např. S1-AP, NG-AP) pro přenos více PLMN ID a pro správné směrování počátečních zpráv.

V modelu sdílení Gateway Core Network (GWCN) je sdílení hlubší a rozšiřuje se na některé core síťové uzly, jako je MME v LTE. Zde PO sdílejí nejen RAN, ale také společný fond MME. Sdílené MME musí být schopné komunikovat s HSS/UDM každého PO. To vyžaduje, aby MME podporovalo více síťových identit a správně směrovalo požadavky na autentizaci účastníka do příslušné domovské sítě. Specifikace jako TS 23.251 detailně popisují tyto architektury. Role PO je také klíčová ve scénářích sdílení spektra, jako je Licensed Shared Access (LSA) nebo Citizens Broadband Radio Service (CBRS), kde operátor (PO) může získat dočasný přístup ke spektrálním zdrojům vlastněným jiným subjektem.

Koncept se rozšiřuje na 5G network slicing a neveřejné sítě. V instanci síťového řezu zřízené pro podnik může být podnik nebo poskytovatel služeb třetí strany PO, který se účastní provozu a správy řezu. Pro sítě neutrálního hostitele v budovách nebo areálech vybuduje infrastrukturu RAN operátor neutrálního hostitele a více mobilních síťových operátorů se stane PO připojením svých core sítí k ní. Rámec PO umožňuje snížení nákladů (sdílením CapEx a OpEx), rychlejší nasazení (zejména ve venkovských oblastech) a zlepšení pokrytí, a to vše při zachování možnosti operátorů udržet si vlastní značku, nezávislou správu účastníků a kontrolu nad svými core službami a politikami.

## K čemu slouží

Koncept Participujícího operátora byl vyvinut pro usnadnění a standardizaci sdílení sítí, které se ukázalo jako klíčová strategie pro operátory při zvládání rostoucích nákladů a složitosti nasazování a údržby hustých rádiových sítí, zejména při přechodu na 3G, 4G a 5G. Výstavba duplicitní RAN infrastruktury v každém regionu je ekonomicky neefektivní a plýtvavá z hlediska spektra. Model PO poskytuje standardizovaný rámec, který umožňuje operátorům spolupracovat na infrastruktuře, zatímco zůstávají konkurenty na servisní vrstvě, čímž řeší jak ekonomické, tak regulační potřeby.

Historicky, před formálními standardy 3GPP pro sdílení sítí, se operátoři zapojovali do bilaterálního sdílení lokalit nebo roamingových dohod, které byly často omezeného rozsahu a technicky těžkopádné. Zavedení standardizovaných architektur sdílení jako MOCN (od Release 6 dále) a GWCN poskytlo jasný technický plán. To umožnilo operátorovi vystupovat jako PO v oblasti, kde neměl pokrytí, a získat okamžitou servisní přítomnost účastí v RAN jiného operátora. Naopak, operátor s nadbytečnou RAN kapacitou mohl hostovat další PO a přeměnit infrastrukturu na zdroj příjmů. To bylo obzvláště důležité pro nové účastníky trhu a pro pokrytí venkovských nebo řídce obydlených oblastí, kde byl obchodní případ pro samostatnou síť slabý.

Vytvoření role PO bylo motivováno také spektrální politikou a vývojem technologie. S aukcemi vysokofrekvenčního spektra pro 5G (např. mmWave), které má omezenou propagaci, se stává nezbytným, ale pro jednoho operátora prohibitivně drahým, husté nasazení sítě. Sdílení prostřednictvím modelu PO činí taková nasazení proveditelnými. Dále pro technologie jako Network Function Virtualization (NFV) a network slicing umožňuje koncept PO flexibilní služební participaci ve sdílené fyzické infrastruktuře. Řeší problém, jak zachovat provozní a komerční oddělení v technicky konvergovaném prostředí, a umožňuje tak inovacím, jako jsou neutrální hostitelé a operátoři privátních sítí, účastnit se mobilního ekosystému.

## Klíčové vlastnosti

- Operátor, který se zapojuje do standardizované dohody o sdílení sítě (např. MOCN, GWCN).
- Udržuje si vlastní nezávislou core síť a systémy správy účastníků (HSS/UDM).
- Jeho PLMN ID je vysíláno sdíleným RAN uzlem (eNodeB/gNB) společně s ID dalších PO.
- Sdílený RAN směruje uživatelská spojení do příslušné core sítě PO na základě vybraného PLMN ID.
- Umožňuje snížení CapEx a OpEx prostřednictvím sdílení infrastruktury při zachování servisní diferenciace.
- Aplikovatelné pro různé scénáře sdílení: geografické sdílení RAN, sdílení spektra, neutrální hostitel a network slicing.

## Související pojmy

- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)
- [GWCN – GateWay Core Network](/mobilnisite/slovnik/gwcn/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 28.538** (Rel-19) — Edge Computing Management (ECM)
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.470** (Rel-19) — W1 Interface Introduction for ng-eNB
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.470** (Rel-19) — F1 Interface Introduction
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [PO na 3GPP Explorer](https://3gpp-explorer.com/glossary/po/)
