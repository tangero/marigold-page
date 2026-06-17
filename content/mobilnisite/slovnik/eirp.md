---
slug: "eirp"
url: "/mobilnisite/slovnik/eirp/"
type: "slovnik"
title: "EIRP – Effective Isotropic Radiated Power"
date: 2025-01-01
abbr: "EIRP"
fullName: "Effective Isotropic Radiated Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eirp/"
summary: "EIRP (Effective Isotropic Radiated Power) je klíčová metrika rádiových kmitočtů představující výkon vyzářený anténou ve směru jejího maximálního zesílení, vztažený k izotropnímu zářiči. Kombinuje výko"
---

EIRP je výkon vyzářený anténou ve směru jejího maximálního zesílení, který kombinuje výkon vysílače a zisk antény mínus ztráty a slouží k definování síly signálu pro splnění předpisů a plánování sítě.

## Popis

EIRP (Effective Isotropic Radiated Power) je základní parametr v bezdrátové komunikaci, který kvantifikuje vyzářený výkon kombinace vysílače a antény v určitém směru. Je definován jako výkon, který by musel být přiveden na bezeztrátovou izotropní anténu (teoretický bodový zdroj vyzařující stejně ve všech směrech), aby vytvořil stejnou hustotu výkonu jako skutečná anténa ve směru svého maximálního zesílení. EIRP se vypočítává jako EIRP = Výstupní výkon vysílače (TPO) + Zisk antény (dBi) - Ztráty ve vedení (dB) a obvykle se vyjadřuje v dBm nebo dBW. Tato metrika je klíčová pro pochopení efektivní síly signálu vyzařovaného z základnové stanice, uživatelského zařízení (UE) nebo jakéhokoli rádiového zařízení.

V praxi se EIRP hojně používá při analýze rádiového rozpočtu pro stanovení dosažitelného poměru signál-šum (SNR) a dosahu pokrytí. Například v 5G NR mají základnové stanice (gNB) specifikované limity EIRP pro každé kmitočtové pásmo, aby byla zajištěna shoda s regulatorními požadavky a zabránilo se rušení jiných systémů. Výpočet zahrnuje detailní komponenty: výstup výkonového zesilovače, ztráty v kombinátorech, ztráty v propojovacích kabelech a vyzařovací diagram antény. Zisk antény, měřený v dBi, zesiluje signál v určitých směrech a vytváří svazky v systémech Massive [MIMO](/mobilnisite/slovnik/mimo/), což přímo ovlivňuje EIRP. Specifikace jako 38.101 a 38.104 poskytují tabulky maximálních hodnot EIRP pro různé třídy zařízení a scénáře nasazení.

EIRP hraje zásadní roli v plánování a optimalizaci sítí. Inženýři jej používají k modelování šíření signálu, aby zajistili dostatečné pokrytí při dodržení emisních limitů stanovených orgány jako [FCC](/mobilnisite/slovnik/fcc/) nebo [ETSI](/mobilnisite/slovnik/etsi/). U technologií beamformingu se EIRP liší podle směru svazku, což vyžaduje dynamické výpočty pro efektivní správu výkonu. Souvisí také s pojmem Equivalent Isotropically Radiated Power (EIRP), který se někdy používá zaměnitelně, ačkoli EIRP striktně odkazuje na efektivní výkon zohledňující účinnost antény. Měření zahrnuje specializované vybavení jako spektrální analyzátory a kalibrované antény, jak je popsáno v testovacích specifikacích jako 38.141. Řízením EIRP operátoři vyvažují výkon, rušení a regulatorní shodu v různých prostředích od hustých městských buněk po venkovské makro buňky.

## K čemu slouží

EIRP byl vyvinut, aby poskytl standardizovanou míru pro porovnání vyzařovacích schopností různých anténních systémů, která zohledňuje jak výkon vysílače, tak směrovost antény. Před jeho přijetím specifikace často spoléhaly pouze na výstupní výkon vysílače, což nezachycovalo skutečnou sílu signálu v zamýšleném směru kvůli charakteristikám antény. To vedlo k nekonzistencím v předpovědích pokrytí a vynucování regulatorních požadavků, zejména s nástupem směrových antén v celulárních sítích. EIRP tento problém řeší tím, že nabízí komplexní metriku odrážející reálný výkon, což umožňuje přesné výpočty rádiového rozpočtu a správu rušení.

Historicky, jak se mobilní sítě vyvíjely od všesměrových antén ve 2G k sofistikovanému beamformingu v 5G, rostla potřeba přesné metriky výkonu. EIRP řeší omezení předchozích přístupů tím, že zahrnuje zisk antény, což je klíčové pro vysokofrekvenční pásma jako mmWave, kde je beamforming pro pokrytí nezbytný. Podporuje regulatorní shodu stanovením maximálních limitů výkonu, aby se zabránilo škodlivému rušení a zajistilo sdílení spektra, například v nelicencovaných pásmech. Jeho vytvoření bylo motivováno požadavkem telekomunikačního průmyslu na univerzální parametr usnadňující certifikaci zařízení, nasazení sítí a mezinárodní roaming, což zajišťuje interoperabilitu napříč různým hardwarem a geografickými oblastmi.

## Klíčové vlastnosti

- Kombinuje výkon vysílače, zisk antény a ztráty ve vedení do jediné směrové metriky výkonu
- Nezbytný pro výpočet rádiového rozpočtu a plánování pokrytí při návrhu bezdrátových sítí
- Podléhá regulatorním limitům definovaným organizacemi jako FCC, ETSI a 3GPP pro každé kmitočtové pásmo
- Podporuje beamforming a systémy Massive MIMO, kde se EIRP liší podle směru svazku
- Používá se při testování shody zařízení a typovém schvalování dle 3GPP TS 38.141 a 38.521
- Umožňuje správu rušení a koexistenci mezi různými rádiovými službami a operátory

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 28.302** (Rel-19) — LSA Controller IRP Management Operations
- **TS 32.855** (Rel-14) — Study on OAM Support for Licensed Shared Access
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- … a dalších 76 specifikací

---

📖 **Anglický originál a plná specifikace:** [EIRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/eirp/)
