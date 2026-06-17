---
slug: "acir"
url: "/mobilnisite/slovnik/acir/"
type: "slovnik"
title: "ACIR – Adjacent Channel Interference Rejection"
date: 2025-01-01
abbr: "ACIR"
fullName: "Adjacent Channel Interference Rejection"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/acir/"
summary: "Adjacent Channel Interference Rejection (ACIR) je klíčová výkonnostní metrika v 3GPP, která kvantifikuje schopnost přijímače snášet rušení ze signálů v sousedních kmitočtových kanálech. Je zásadní pro"
---

ACIR je výkonnostní metrika 3GPP, která kvantifikuje schopnost přijímače snášet rušení ze signálů v sousedních kmitočtových kanálech. Je klíčová pro kapacitu sítě a efektivní opakované využití spektra.

## Popis

Adjacent Channel Interference Rejection (ACIR) je složený parametr definovaný ve specifikacích 3GPP, který charakterizuje celkovou schopnost přijímače potlačit rušení při vystavení dominantnímu rušivému signálu v sousedním rádiovém kmitočtovém kanálu. Není to samostatná komponenta, ale vypočítaná hodnota (figure of merit), která kombinuje účinky dvou klíčových faktorů: Adjacent Channel Leakage Ratio (ACLR) vysílače rušivého signálu a Adjacent Channel Selectivity (ACS) přijímače oběti. Vztah je definován jako ACIR = 1 / (1/ACLR + 1/ACS). Tento vzorec zachycuje celkový scénář rušení, kde nežádoucí emise z agresivního vysílače (ACLR) a nedokonalé filtrování přijímače oběti (ACS) společně přispívají ke zhoršení užitečného signálu.

V praktickém nasazení sítě a správě rádiových prostředků je ACIR základním vstupem pro simulace na systémové úrovni a plánování sítě. Přímo ovlivňuje výpočty pro minimální kmitočtové odstup (ochranná pásma) vyžadovaný mezi různými nosnými, zejména ve scénářích koexistence. Tyto scénáře zahrnují nasazení sítí více operátorů v sousedních pásmech, nasazení různých technologií radiového přístupu (RAT), jako jsou LTE a NR, v sousedních kanálech, nebo dokonce provoz různých částí šířky pásma (bandwidth parts) v rámci stejné nosné. Vyšší hodnota ACIR znamená lepší potlačení rušení, což umožňuje zmenšit ochranná pásma, což vede k vyšší celkové využitelnosti spektra a kapacitě sítě.

Specifikace a testování požadavků na ACIR jsou podrobně popsány v mnoha technických specifikacích 3GPP (TS) pro přijímače uživatelského zařízení (UE) a základnových stanic (eNB/gNB). Tyto požadavky se liší v závislosti na scénáři nasazení (např. rušení mezi základnovými stanicemi, rušení ze základnové stanice na UE), kmitočtovém pásmu a zúčastněných šířkách kanálu. Konformní testy ověřují, že přijímač dokáže udržet stanovenou propustnost nebo chybovost bloků (BLER), když je přítomen rušič v sousedním kanálu, modulovaný specifickým průběhem a s definovanou úrovní výkonu vůči užitečnému signálu. Tím je zajištěna robustnost provozu v reálných podmínkách.

Role ACIR zasahuje do pokročilých síťových funkcí, jako je agregace nosných (CA) a dynamické sdílení spektra. V CA, kde zařízení současně přijímá na více komponentních nosných, může výkon z jedné nosné pronikat do přijímací cesty jiné. Vysoký výkon ACIR je nezbytný k zabránění vlastního rušení. Podobně pro techniky sdílení spektra, jako je koexistence LTE-NR (EN-DC) nebo sdílení sítě radiového přístupu více operátory (MORAN), ACIR definuje praktické meze izolace potřebné mezi sdílenými entitami, což zajišťuje, že výkon jedné služby nezhorší katastrofálně výkon druhé. ACIR je tedy základní metrikou pro umožnění efektivního a proti rušení odolného řízení spektra ve všech generacích systémů 3GPP od UMTS po 5G NR a dále.

## K čemu slouží

ACIR byl zaveden k řešení základního problému rušení v sousedním kanálu, který se stává akutním, když se bezdrátové spektrum stává více přeplněným a fragmentovaným mezi více operátory a technologiemi. Před jeho formální definicí se plánování sítě spoléhalo na jednodušší, často konzervativnější předpoklady o rušení, což vedlo k neefektivně velkým ochranným pásmům mezi frekvenčními přiděleními. Toto plýtvalo cennými spektrálními zdroji. Vytvoření ACIR poskytlo standardizovanou, kvantifikovatelnou metriku, která přesně modeluje skutečné vazby rušení mezi neideálním vysílačem a neideálním přijímačem pracujícím na blízkých kmitočtech.

Historický kontext důležitosti ACIR rostl s liberalizací telekomunikačních trhů a aukčním přidělováním spektra v diskrétních blocích více operátorům. Ve scénářích, jako byla evropská nasazení 3G (UMTS), získali různí operátoři sousední frekvenční bloky. Bez jasného pochopení potenciálu vzájemného rušení (charakterizovaného ACIR) mohla síť jednoho operátora vážně degradovat kvalitu služby sousedovi, což vedlo ke stížnostem zákazníků a regulačním sporům. ACIR poskytl technický základ pro definování minimálních požadavků na koexistenci, což zajistilo rovné podmínky a spolehlivou službu pro všechny.

ACIR navíc řeší omezení uvažování pouze úniku z vysílače (ACLR) nebo selektivity přijímače (ACS) izolovaně. Síť s vysílači s vynikajícím ACLR by stále mohla zažívat rušení, pokud mají přijímače špatné ACS, a naopak. Kombinací obou do jediného parametru na systémové úrovni poskytuje ACIR plánovačům sítí a výrobcům zařízení úplný obraz scénáře rušení. To umožňuje návrh spektrálně účinnějších sítí, podporuje zavádění nosných s větší šířkou pásma a usnadňuje pokojnou koexistenci starších a nových technologií (např. GSM, UMTS, LTE, NR) v téže geografické oblasti, což je základním kamenem plynulé migrace technologií.

## Klíčové vlastnosti

- Složená metrika kombinující ACLR vysílače a ACS přijímače
- Základní vstup pro simulace na systémové úrovni a RF plánování
- Definuje potřebná ochranná pásma pro koexistenci nosných
- Specifikována pro přijímače UE i základnových stanic napříč všemi technologiemi 3GPP RAT
- Kritická pro scénáře nasazení s více operátory a více technologiemi RAT
- Ověřována konformními testy pro zajištění robustnosti provozu v reálných podmínkách

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.816** (Rel-8) — UMTS 900 MHz RF Requirements Study
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations
- **TR 36.942** (Rel-19) — E-UTRA System Scenarios Specification
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.809** (Rel-11) — E-UTRA & MSR BS Class Requirements
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements
- **TR 38.828** (Rel-16) — CLI and RIM for NR
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [ACIR na 3GPP Explorer](https://3gpp-explorer.com/glossary/acir/)
