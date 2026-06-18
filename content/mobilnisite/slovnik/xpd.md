---
slug: "xpd"
url: "/mobilnisite/slovnik/xpd/"
type: "slovnik"
title: "XPD – Cross-Polar Discrimination"
date: 2025-01-01
abbr: "XPD"
fullName: "Cross-Polar Discrimination"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/xpd/"
summary: "XPD je klíčový parametr výkonu antény měřící izolaci mezi ortogonálně polarizovanými signály, typicky vertikální a horizontální. Kvantifikuje schopnost antény rozlišit nebo oddělit signály na základě"
---

XPD je klíčový parametr výkonu antény, který měří izolaci mezi ortogonálně polarizovanými signály a kvantifikuje schopnost antény je rozlišit. To je zásadní pro polarizační diverzitu a MIMO.

## Popis

Cross-Polar Discrimination (XPD) je základní parametr v anténním inženýrství a rádiovém šíření, definovaný jako poměr výkonu přijatého v zamýšlené (ko-polarizované) polarizaci k výkonu přijatému v ortogonální (křížově polarizované) polarizaci. Zjednodušeně řečeno, pokud je anténa navržena pro vysílání nebo příjem vertikálně polarizované vlny, XPD měří, kolik z tohoto signálu 'unikne' do horizontální polarizace, nebo naopak. Obvykle se vyjadřuje v decibelech (dB), přičemž vyšší hodnota značí lepší čistotu polarizace a izolaci. Matematicky, pro převážně vertikálně polarizovanou anténu, XPD = 10 log10 (Výkon přijatý ve vertikální polarizaci / Výkon přijatý v horizontální polarizaci).

V kontextu systémů 3GPP je XPD klíčovým faktorem při návrhu a nasazení antén pro základnové stanice (eNodeB/gNodeB) a v menší míře i pro uživatelská zařízení (UE). Funguje tak, že charakterizuje vnitřní vlastnost antény udržovat integritu polarizace. V reálném scénáři může mít vyslaný signál s konkrétní polarizací svůj polarizační stav změněn v důsledku odrazů, difrakce a rozptylu v prostředí šíření – jev známý jako depolarizace. XPD přijímací antény v kombinaci s křížovou polarizační vazbou kanálu určuje efektivní izolaci mezi polarizačními kanály.

Z architektonického hlediska XPD ovlivňuje výkon systému několika způsoby. U jednopolarizačních antén vysoké XPD minimalizuje nežádoucí příjem signálů v ortogonální polarizaci, což může být interference. U dvoupolarizačních antén (např. se sklonem ±45°), které jsou všudypřítomné v moderních [MIMO](/mobilnisite/slovnik/mimo/) systémech, XPD přímo ovlivňuje výkon polarizační diverzity a prostorového multiplexování. V konfiguraci 2x2 MIMO využívající dvoupolarizační antény jsou dva datové toky vysílány na ortogonálních polarizacích. Vysoké XPD zajišťuje nízkou vazbu mezi těmito toky, snižuje interferenci mezi vrstvami a umožňuje úspěšné dekódování obou vrstev, čímž zvyšuje propustnost. Mezi klíčové komponenty související s XPD patří návrh anténního prvku, napájecí síť a okolní kryt (radome), které musí být optimalizovány pro maximalizaci XPD v provozním kmitočtovém pásmu a vyzařovacím úhlu.

## K čemu slouží

XPD existuje jako klíčový výkonnostní parametr, který umožňuje a optimalizuje využití polarizace jako zdroje v bezdrátové komunikaci. Rané celulární systémy primárně využívaly prostorové oddělení nebo frekvenční diverzitu. Omezení spočívalo v tom, že tyto metody vyžadují fyzický prostor nebo dodatečnou šířku pásma. Polarizační diverzita, umožněná anténami s dobrým XPD, nabízí způsob, jak vytvořit dva efektivně nezávislé komunikační kanály využívající stejné fyzické umístění a kmitočet, což je vysoce účinné využití zdrojů.

Problém, který řeší, je mnohocestné únikové zanášení (multipath fading) a potřeba zvýšení kapacity bez dodatečného spektra. V mnohocestném prostředí mohou mít signály přicházející různými cestami náhodné polarizace. Anténa se špatným XPD nemůže efektivně rozlišit požadovanou polarizaci od promíchaných, což vede ke zhoršení signálu. Použitím dvou ortogonálně polarizovaných antén s vysokým XPD může přijímač kombinovat signály z obou polarizací, aby zmírnil únikové zanášení, čímž zlepší spolehlivost spoje. To je princip polarizační diverzity.

Jeho význam vzrostl s nástupem [MIMO](/mobilnisite/slovnik/mimo/) a víceanténních technologií v 3GPP LTE a 5G NR. Zde se účel XPD rozšiřuje za diverzitu až k umožnění prostorového multiplexování. Pro vysílání více nezávislých datových toků ze stejného anténního pole je vyžadována ortogonalita mezi kanály. Polarizační ortogonalita, zajištěná vysokým XPD, to poskytuje v kompaktním formátu, což umožňuje hustou integraci anténních prvků v aktivních anténních systémech ([AAS](/mobilnisite/slovnik/aas/)). Proto je specifikace a měření XPD (jak je prováděno ve specifikacích jako 3GPP TR 37.544 a TS 38.903) zásadní pro predikci a zaručení reálného výkonu pokročilých anténních systémů, což přímo ovlivňuje kapacitu sítě a datové rychlosti uživatelů.

## Klíčové vlastnosti

- Měří izolaci mezi ko-polarizovanými a křížově polarizovanými porty antény
- Vyjadřuje se v decibelech (dB), přičemž vyšší hodnoty značí lepší výkon
- Kritický parametr pro dvoupolarizační anténní pole používaná v MIMO
- Ovlivňuje účinnost schémat polarizační diverzity
- Ovlivňuje interferenci mezi vrstvami při prostorovém multiplexování
- Definován a měřen ve specifikacích 3GPP pro shodnost a výkonnostní testy

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [XPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/xpd/)
