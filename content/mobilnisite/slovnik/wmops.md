---
slug: "wmops"
url: "/mobilnisite/slovnik/wmops/"
type: "slovnik"
title: "WMOPS – Weighted Million Operations Per Second"
date: 2025-01-01
abbr: "WMOPS"
fullName: "Weighted Million Operations Per Second"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wmops/"
summary: "WMOPS je metrika výpočetní složitosti definovaná 3GPP pro měření zátěže zpracování řečových a audio kodeků. Poskytuje standardizovaný způsob hodnocení a porovnávání požadavků na zpracování v reálném č"
---

WMOPS je metrika výpočetní složitosti definovaná 3GPP pro měření a porovnávání zátěže reálného času implementací řečových a audio kodeků na hardwaru.

## Popis

Weighted Million Operations Per Second (WMOPS) je standardizovaná měrná jednotka definovaná v 3GPP TS 26.258 a souvisejících specifikacích pro kvantifikaci výpočetní složitosti algoritmů řečových a audio kodeků, jako jsou například v rodinách kodeků [AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/) a [EVS](/mobilnisite/slovnik/evs/). Nejde o měřítko hrubé rychlosti procesoru, ale o vážený počet specifických operací na nízké úrovni (jako jsou sčítání, násobení, přístupy do paměti), které kodek provede za sekundu při zpracování signálu při dané vzorkovací frekvenci a délce rámce. Každému typu operace je přiřazena váha odrážející její relativní výpočetní náročnost na typické [DSP](/mobilnisite/slovnik/dsp/) nebo procesorové architektuře. Celková hodnota WMOPS se vypočítá sečtením vážených počtů všech operací provedených během jedné sekundy kódování nebo dekódování audia.

Metodika výpočtu zahrnuje profilování referenční softwarové implementace kodeku (typicky ve fixed-point C) pomocí definované sady typů operací a jejich přidružených vah. Tyto váhy jsou stanoveny na základě odhadované ceny v cyklech každé operace na generickém modelu procesoru. Specifikace definuje podrobná pravidla pro počítání, včetně způsobu zacházení se smyčkami, podmíněnými operacemi a funkcemi. Testování souladu pro implementaci kodeku často zahrnuje ověření, že jeho spotřeba WMOPS nepřekračuje stanovený maximální limit za nejhorších kanálových podmínek (např. testy Frame Erasure Rate), aby bylo zajištěno, že může běžet v reálném čase na cílovém hardwaru.

WMOPS hraje v ekosystému 3GPP klíčovou roli tím, že poskytuje objektivní, na platformě nezávislou metriku pro porovnávání složitosti kodeků. To umožňuje síťovým operátorům a výrobcům zařízení vybírat vhodný hardware schopný podporovat více současných kanálů kodeků (např. v transkodéru základnové stanice nebo ve smartphonu). Také zajišťuje, že různé softwarové implementace stejného standardu kodeku mají srovnatelnou výpočetní náročnost, což napomáhá interoperabilitě a certifikaci. Metrika je zásadní pro návrh systémů, plánování kapacity a odhad spotřeby energie, protože zatížení zpracováním přímo ovlivňuje výdrž baterie v mobilních zařízeních a náklady na infrastrukturu v sítích.

## K čemu slouží

WMOPS byl vytvořen k řešení problému objektivního porovnávání a specifikace výpočetních požadavků digitálních řečových a audio kodeků způsobem nezávislým na hardwaru. Před jeho standardizací byla složitost kodeků často popisována vágními termíny jako '[DSP](/mobilnisite/slovnik/dsp/) [MIPS](/mobilnisite/slovnik/mips/)', které byly vysoce závislé na konkrétních procesorových architekturách, efektivitě kompilátorů a paměťových systémech, což činilo přesná multiplatformní srovnání a systémový návrh téměř nemožný. Tento nedostatek standardní metriky představoval významné výzvy pro výrobce mobilních telefonů, kteří potřebovali zajistit, že jejich čipsety dokážou podporovat povinné kodeky v reálném čase při dodržení rozpočtů spotřeby energie, a pro výrobce síťové infrastruktury navrhující zařízení pro transkódování s vysokou hustotou.

Motivace vycházela z rozšíření pokročilých kodeků v systémech 3GPP (od GSM [FR](/mobilnisite/slovnik/fr/)/[HR](/mobilnisite/slovnik/hr/) přes UMTS AMR až po LTE EVS), z nichž každý měl rostoucí algoritmickou složitost za účelem dosažení vyšší kvality zvuku a lepší spektrální účinnosti. Standardizovaná míra složitosti byla nezbytná k definování minimálních výkonnostních požadavků v technických specifikacích, což umožnilo spravedlivé benchmarkování a certifikaci implementací. WMOPS poskytl reprodukovatelnou, transparentní metodu pro posouzení, zda lze danou softwarovou implementaci kodeku provádět v reálném čase na konkrétní hardwarové platformě, čímž snížil rizika vývoje produktů a zajistil konzistentní uživatelský zážitek napříč zařízeními a sítěmi. Řešil tak kritickou potřebu společného jazyka mezi návrháři algoritmů kodeků, softwarovými vývojáři a hardwarovými inženýry v rámci ekosystému 3GPP.

## Klíčové vlastnosti

- Na platformě nezávislá metrika složitosti pro řečové/audio kodeky
- Používá vážené počty operací na nízké úrovni (sčítání, násobení, posun, přístup do paměti)
- Definované typy operací a jejich váhy v 3GPP TS 26.258
- Zahrnuje pravidla profilování pro nejhorší kanálové podmínky (např. výpadky rámců)
- Používá se pro testování souladu a stanovení maximálních limitů složitosti
- Umožňuje hodnocení schopnosti zpracování v reálném čase na cílovém hardwaru

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)
- [CODEC – Coder/Decoder](/mobilnisite/slovnik/codec/)

## Definující specifikace

- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- **TS 26.443** (Rel-19) — EVS Codec Floating-Point C Code
- **TS 26.444** (Rel-19) — EVS Codec Conformance Test Sequences
- **TS 26.450** (Rel-19) — EVS Codec DTX System Level Aspects
- **TS 26.451** (Rel-19) — EVS Codec Voice Activity Detector (VAD) Specification
- **TS 26.452** (Rel-19) — EVS Codec Fixed-Point C Code Implementation
- **TR 26.997** (Rel-19) — IVAS Codec Specification
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [WMOPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/wmops/)
