---
slug: "a-mpr"
url: "/mobilnisite/slovnik/a-mpr/"
type: "slovnik"
title: "A-MPR – Additional Maximum Power Reduction"
date: 2025-01-01
abbr: "A-MPR"
fullName: "Additional Maximum Power Reduction"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/a-mpr/"
summary: "A-MPR je mechanismus snížení výkonu UE v 3GPP LTE a NR zajišťující dodržování regulačních emisních limitů, zejména pro nesouvislé alokace spektra a scénáře s agregací nosných. Umožňuje UE snížit svůj"
---

A-MPR je mechanismus dodatečného maximálního snížení výkonu pro UE, který umožňuje splnit regulační emisní limity, zejména v případech nesouvislého spektra nebo scénářů s agregací nosných, a to snížením výkonu nad rámec základní úrovně za účelem prevence interference.

## Popis

Additional Maximum Power Reduction (A-MPR, Dodatečné maximální snížení výkonu) je standardizovaný mechanismus definovaný ve specifikacích 3GPP, který umožňuje uživatelskému zařízení (UE) aplikovat dodatečné snížení výkonu nad rámec základního maximálního snížení výkonu ([MPR](/mobilnisite/slovnik/mpr/)). Základní MPR se uplatňuje kvůli zvýšenému poměru špičkového a průměrného výkonu ([PAPR](/mobilnisite/slovnik/papr/)) při použití modulačních schémat vyššího řádu, jako je [64QAM](/mobilnisite/slovnik/64qam/) nebo 256QAM. A-MPR řeší konkrétnější a přísnější regulační požadavky, zejména ty související s parazitními emisemi a poměrem úniku do přilehlého kanálu ([ACLR](/mobilnisite/slovnik/aclr/)). Tyto požadavky jsou obzvláště náročné, když UE pracuje v nesouvislých alokacích spektra, používá určité alokace zdrojových bloků ([RB](/mobilnisite/slovnik/rb/)) na okraji nosné nebo využívá agregaci nosných ([CA](/mobilnisite/slovnik/ca/)), kde je současně aktivních více komponentních nosných.

Aplikace A-MPR není univerzální, ale je spouštěna specifickou signalizací sítě. Síť nakonfiguruje UE hodnotou 'Allowed A-MPR' prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) signalizace, typicky v rámci informačních prvků RadioResourceConfigDedicated nebo podobných. Tato konfigurace zahrnuje parametry jako hodnota síťové signalizace ([NS](/mobilnisite/slovnik/ns/)_x), která odpovídá konkrétnímu souboru regionálních regulačních požadavků (např. FCC, ETSI). UE na základě svých implementovaných schopností a signalizované hodnoty NS_x určí použitelnou hodnotu A-MPR z předdefinovaných tabulek ve specifikacích (např. 3GPP TS 36.101 pro LTE, TS 38.101 pro NR). UE poté aplikuje tuto hodnotu A-MPR navíc k jakémukoli základnímu MPR, čímž efektivně sníží svůj maximální vysílací výkon (PCMAX), aby zajistila, že její vysílaný signál zůstane v rámci stanovených emisních masek.

Technická implementace zahrnuje složité vyhledávací tabulky, které mapují různé přenosové parametry na požadovanou hodnotu A-MPR. Mezi tyto parametry patří konfigurace přenosové šířky pásma, umístění a souvislost přidělených zdrojových bloků, modulační schéma a konkrétní kombinace pásem pro CA. Například UE vysílající na dvou nesousedících komponentních nosných v Pásmu 1 a Pásmu 3 může vyžadovat vyšší A-MPR než při vysílání na jediném souvislém bloku. Výkonový řídicí algoritmus UE musí dynamicky vypočítat celkové maximální snížení výkonu (MPR + A-MPR), aby určil přípustný maximální výstupní výkon pro každý podrámec nebo slot, a zajistil tak dodržování limitů v reálném čase.

A-MPR hraje zásadní roli ve fyzické vrstvě rádiové přístupové sítě tím, že umožňuje flexibilní využití spektra a zároveň chrání integritu rádiového spektra. Bez něj by agresivní přerozdělování spektra, agregace nosných a používání fragmentovaných bloků spektra mohlo vést k nepřijatelným úrovním mimopásmových emisí a způsobovat interference službám v sousedních pásmech. Definováním jasných, testovatelných požadavků na A-MPR zajišťuje 3GPP, že UE od různých výrobců mohou vzájemně spolupracovat v sítích po celém světě, a to při dodržování různorodých a přísných regionálních regulačních režimů. Jeho správná implementace je ověřována prostřednictvím důkladných testů shody definovaných ve specifikacích jako TS 36.521 a TS 38.521.

## K čemu slouží

A-MPR bylo vytvořeno za účelem řešení praktického problému provozu moderních celulárních systémů s vysokou propustností v rámci přísných regulačních emisních limitů, zejména když se využití spektra stalo složitějším. Raná vydání 3GPP (před Rel-8) se zabývala relativně jednoduchými, souvislými alokacemi spektra. Avšak se zavedením LTE v Rel-8 a následným tlakem na vyšší datové rychlosti se staly nezbytnými techniky jako agregace nosných a používání nesouvislých bloků spektra. Tyto pokročilé přenosové scénáře vytvářejí náročnější signálové průběhy s prudšími přechody a vyšší spektrální regrowth, což ztěžuje výkonovým zesilovačům UE udržovat čisté emise mimo přidělený kanál. Základní MPR, navržený pro výkonové omezení založené na modulaci, byl nedostatečný pro splnění požadavků na parazitní emise a spektrální emisní masku, které pro tyto složité případy ukládají národní regulátoři (např. FCC, ETSI).

Hlavní motivací byla regulační shoda a koexistence spektra. Bez A-MPR by UE pracující s agregací nosných na okraji svého provozního pásma mohla vyzařovat nadměrný výkon do přilehlého pásma, což by potenciálně mohlo interferovat se sítí jiného operátora nebo s úplně jinou službou (např. letectví, satelit). To by porušilo licenční podmínky a zhoršilo celkový výkon sítě. A-MPR poskytuje standardizovanou, síťově řízenou metodu pro vynucení dodatečného výkonového omezení přesně tehdy a tam, kde je to potřeba. To umožňuje operátorům sítí s důvěrou nasazovat pokročilé funkce s vědomím, že UE automaticky upraví svůj výkon, aby zůstala v zákonných limitech, bez ohledu na konkrétní alokaci zdrojů nebo kombinaci pásem.

Dále A-MPR řeší ekonomickou a technickou výzvu návrhu výkonového zesilovače UE. Návrh výkonového zesilovače, který nikdy nepřekročí emisní limity ve všech možných přenosových scénářích, by byl neúměrně drahý a neefektivní. A-MPR nabízí kompromis: zesilovač může být navržen pro typické případy a pro výjimečné, náročnější případy se aplikuje řízené snížení maximálního výstupního výkonu. Tím se vyvažují náklady, energetická účinnost (životnost baterie) a regulační shoda. Představuje klíčový faktor pro globální škálovatelnost zařízení LTE a NR, protože zajišťuje, že jediný návrh UE se může prostřednictvím softwaru a konfigurace přizpůsobit své činnosti tak, aby splňoval specifická emisní pravidla kterékoli země, v níž pracuje.

## Klíčové vlastnosti

- Síťově konfigurované snížení výkonu spouštěné RRC signalizací (hodnoty NS_x)
- Definováno prostřednictvím tabulek ve specifikacích mapujících přenosové parametry na požadované hodnoty A-MPR
- Řeší požadavky na parazitní emise a ACLR pro nesouvislé alokace RB
- Klíčové pro shodu v scénářích s agregací nosných a nesouvislým spektrem
- Aplikováno navíc k základnímu MPR pro modulaci a šířku pásma
- Zajišťuje koexistenci a předchází interferenci s přilehlými kmitočtovými pásmy

## Související pojmy

- [PCMAX – Configured Maximum UE Output Power](/mobilnisite/slovnik/pcmax/)

## Definující specifikace

- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 36.745** (Rel-14) — Satellite Protection for LTE Bands 11/21
- **TR 36.770** (Rel-18) — Technical Report for High Power UE in LTE Band 14
- **TS 36.852** — 3GPP TR 36.852
- **TS 36.860** — 3GPP TR 36.860
- **TS 36.899** — 3GPP TR 36.899
- **TS 37.717** — 3GPP TR 37.717
- **TS 37.718** — 3GPP TR 37.718
- **TS 37.719** (Rel-19) — 3GPP TR 37.719: Dual Connectivity Band Combinations
- **TS 37.825** (Rel-16) — High Power UE (PC2) for EN-DC TDD-TDD
- **TR 37.829** (Rel-18) — Technical Report
- **TS 37.862** (Rel-19) — Adding channel bandwidth in existing NR bands
- **TR 37.880** (Rel-17) — High-power UE for fixed-wireless/vehicle use
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [A-MPR na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-mpr/)
