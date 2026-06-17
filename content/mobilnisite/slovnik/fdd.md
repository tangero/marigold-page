---
slug: "fdd"
url: "/mobilnisite/slovnik/fdd/"
type: "slovnik"
title: "FDD – Frequency Division Duplexing"
date: 2026-01-01
abbr: "FDD"
fullName: "Frequency Division Duplexing"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fdd/"
summary: "FDD je duplexní metoda, při níž přenosy v uplinku a downlinku probíhají současně na oddělených spárovaných kmitočtových pásmech. Umožňuje plně duplexní komunikaci, což znamená nepřetržitý přenos a pří"
---

FDD je duplexní metoda, při níž přenosy v uplinku a downlinku probíhají současně na oddělených spárovaných kmitočtových pásmech, což umožňuje plně duplexní komunikaci.

## Popis

Frekvenční duplex s dělením kmitočtů (FDD) je základní metoda radiového přístupu používaná v celulárních sítích pro oddělení přenosů v uplinku (od UE k síti) a downlinku (od sítě k UE). Funguje tak, že pro oba směry přiděluje dvě odlišná, spárovaná kmitočtová pásma, což umožňuje současnou obousměrnou komunikaci. Rozestup mezi kmitočty nosných uplinku a downlinku, známý jako duplexní odstup, je pečlivě definován, aby se předešlo interferenci, a je standardizován pro každé kmitočtové pásmo. Tento současný provoz umožňuje plně duplexní komunikaci, která je nezbytná pro služby v reálném čase, jako jsou hlasové hovory a interaktivní datové aplikace vyžadující nízkou latenci.

V systému FDD je uživatelské zařízení (UE) i základnová stanice (např. NodeB, eNodeB, gNB) vybaveno duplexery neboli filtry. Tyto komponenty umožňují, aby vysílač a přijímač mohly pracovat současně na svých příslušných kmitočtech, protože poskytují dostatečnou izolaci mezi vysílací a přijímací cestou. Síť přiřadí buňce konkrétní kmitočty nosných pro uplink a downlink a všechna UE v této buňce používají toto spárované spektrum. Kanály fyzické vrstvy pro řídicí a datové přenosy (např. [PDCCH](/mobilnisite/slovnik/pdcch/), [PDSCH](/mobilnisite/slovnik/pdsch/) v LTE; PDCCH, PDSCH v NR) jsou mapovány na tyto nosné. Klíčové specifikace, jako jsou 3GPP TS 36.101 pro LTE a TS 38.101 pro NR, definují přesná čísla pásem, rozsahy kmitočtů pro uplink/downlink a šířky kanálů pro provoz FDD.

Architektura FDD je nedílnou součástí rádiové přístupové sítě (RAN). Rádiová jednotka (RU) základnové stanice zpracovává RF vysílání a příjem na spárovaných pásmech, zatímco základnová jednotka pro zpracování signálu (baseband) spravuje plánování, modulaci a kódování. Plánování ve FDD je ze své podstaty flexibilní, protože uplink a downlink mají vyhrazené a nepřetržité spektrální zdroje. To umožňuje nezávislou optimalizaci kapacity a kvality každého spoje. FDD je základním kamenem mnoha globálních celulárních pásem (např. Band 1, Band 3, Band 7) a podporuje technologie od UMTS (WCDMA) přes LTE až po 5G NR, často ve spojení s jinými schématy vícečetného přístupu, jako jsou [OFDMA](/mobilnisite/slovnik/ofdma/) a SC-FDMA.

Její role přesahuje rámec pouhého umožnění duplexní komunikace. FDD poskytuje předvídatelnou a konzistentní latenci, protože zdroje jsou vždy dostupné v obou směrech. To ji činí velmi vhodnou pro symetrické typy provozu, jako jsou hlasové a videokonference. Navíc fyzické oddělení kmitočtů zjednodušuje RF návrh ve srovnání s duplexem s dělením času (TDD), protože odpadá potřeba přesné časové synchronizace a ochranných period mezi směry přenosu. Vyžaduje však spárované spektrum, které může být vzácným zdrojem. V 5G NR lze FDD nasadit jak v kmitočtovém rozsahu 1 (sub-6 GHz), tak v kmitočtovém rozsahu 2 (mmWave) a lze jej kombinovat s technikami TDD a doplňkového uplinku (SUL) pro větší flexibilitu.

## K čemu slouží

FDD bylo vytvořeno za účelem řešení základního problému umožnění obousměrné, simultánní (plně duplexní) komunikace v bezdrátových systémech. Raná rádiová komunikace často používala poloduplexní metody (push-to-talk), které byly pro přirozenou konverzaci neefektivní. FDD umožňuje uživateli současně mluvit a naslouchat, což odpovídá zkušenosti s tradičním pevným telefonem a bylo klíčovým požadavkem pro veřejnou mobilní telefonii. Jeho vývoj byl motivován potřebou efektivního využití spektra, které podporuje nepřetržité kvalitní hlasové služby bez přerušení způsobených dělením času, jež jsou vlastní čistě časovým přístupům.

Hlavním problémem, který FDD řeší, je vnitropásmové rušení mezi výkonným vysílačem zařízení a jeho citlivým přijímačem. Použitím oddělených, dostatečně odstupňovaných kmitočtových pásem může duplexní filtr poskytnout potřebnou izolaci (obvykle 40–50 dB), aby zabránil vysílači v desenzibilizaci přijímače. Jedná se na úrovni zařízení o přímočařejší technické řešení ve srovnání s dosažením stejné izolace ve sdíleném kmitočtovém pásmu. Historicky byla FDD dominantní duplexní metodou pro sítě 2G GSM a 3G UMTS, protože poskytovala spolehlivý výkon pro přepojování okruhů v hlasových službách a počátečních datových službách.

Přestože je FDD efektivní, jeho požadavek na spárované, symetrické bloky spektra se stal omezením, protože spektrum se stalo vzácnějším a dražším zbožím. Je méně flexibilní pro asymetrický internetový datový provoz ve srovnání s TDD. Jeho účel však zůstává zásadní: poskytovat robustní, nízkolatenční a vysokokapacitní komunikaci tam, kde je k dispozici spárované spektrum. Tvoří páteř mnoha starších i moderních sítí a zajišťuje zpětnou kompatibilitu a kontinuitu služeb. Pokračující vývoj FDD ve standardech 3GPP se zaměřuje na zvýšení jeho efektivity (např. pomocí agregace nosných, pokročilého [MIMO](/mobilnisite/slovnik/mimo/)) a jeho integraci s flexibilnějšími duplexními schématy v 5G.

## Klíčové vlastnosti

- Současný přenos v uplinku i downlinku na spárovaných kmitočtových pásmech
- Umožňuje plně duplexní komunikaci pro služby s nízkou latencí, jako je hlas
- K izolaci vysílače a přijímače využívá duplexní filtry
- Poskytuje předvídatelnou latenci a symetrickou kapacitu
- Základní metoda pro mnoho globálně standardizovaných celulárních kmitočtových pásem
- Podporuje agregaci nosných mezi FDD nosnými i s TDD

## Související pojmy

- [OFDMA – Orthogonal Frequency Division Multiple Access](/mobilnisite/slovnik/ofdma/)

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
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- … a dalších 151 specifikací

---

📖 **Anglický originál a plná specifikace:** [FDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/fdd/)
