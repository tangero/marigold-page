---
slug: "mue"
url: "/mobilnisite/slovnik/mue/"
type: "slovnik"
title: "MUE – Macro UE"
date: 2025-01-01
abbr: "MUE"
fullName: "Macro UE"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mue/"
summary: "Uživatelské zařízení (UE), které je přihlášeno k makro buňce a přijímá od ní služby. Toto je standardní provozní režim pro většinu UE v rozlehlé síti, na rozdíl od těch připojených k small cells nebo"
---

MUE je uživatelské zařízení (UE), které je přihlášeno k makro buňce a přijímá od ní služby, což definuje základní scénář konektivity pro plánování sítě.

## Popis

Macro UE (MUE) je uživatelské zařízení, které je aktivně přihlášeno k základnové stanici makro buňky (eNodeB v LTE, gNB v NR). Tato klasifikace je zásadní pro studie síťové architektury a řízení rádiových zdrojů, zejména ty zahrnující heterogenní sítě (HetNety). V takových studiích je síť modelována jako mix vysokovýkonných makro buněk poskytujících pokrytí v široké oblasti a nízkovýkonných small cells (piko, femto) pro zvýšení kapacity. MUE představuje uživatelskou populaci obsluhovanou touto tradiční, vysokovýkonnou vrstvou.

Provozní stav MUE je definován jeho stavem řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) a jeho připojením k fyzickým kanálům makro buňky. Synchronizuje se se synchronizačními signály makro buňky (PSS/SSS), dekóduje vysílané systémové informace ([MIB](/mobilnisite/slovnik/mib/), SIBs) a provádí měření na referenčních signálech makro buňky (např. [CRS](/mobilnisite/slovnik/crs/) v LTE, SSB v NR). Obsluhující makro buňka spravuje veškeré řízení rádiových zdrojů pro MUE, včetně přidělování zdrojů na [PDCCH](/mobilnisite/slovnik/pdcch/), alokace [PDSCH](/mobilnisite/slovnik/pdsch/) pro downlinková data a PUSCH pro uplinková data, a rozhodování o předávání spojení.

Z pohledu síťového modelování, zejména ve specifikacích jako 36.825 (LTE), které studují pokročilou koordinaci interference mezi buňkami (eICIC) a její další vylepšení (FeICIC), je MUE klíčovou entitou. Jeho výkonnostní metriky, jako je propustnost a poměr signálu k interferenci a šumu (SINR), jsou analyzovány v přítomnosti interference ze sousedních makro buněk a, což je klíčové, z blízkých small cells. Techniky jako Almost Blank Subframes ([ABS](/mobilnisite/slovnik/abs/)) v LTE byly navrženy k ochraně zranitelných UE (často těch na okraji buňky) před dominantními interferery; chování a plánování MUE je během těchto chráněných podrámců upravováno za účelem řízení interference mezi vrstvami v HetNetu.

Koncept se méně týká konkrétní protokolové zprávy a více definované role nebo stavu pro simulaci, analýzu a specifikaci síťových algoritmů. Poskytuje jasné odlišení od jiných typů UE, jako je Pico UE (PUE) nebo Relay UE, a umožňuje tak přesné modelování různých interferenčních prostředí, vzorců mobility a strategií dělení zdrojů napříč vrstvenou topologií sítě.

## K čemu slouží

Termín MUE byl formálně definován, aby umožnil přesné technické studie a specifikace pro heterogenní sítě (HetNety). Když se mobilní sítě vyvinuly za hranice homogenních nasazení makro buněk, zavedení nízkovýkonných uzlů (LPN), jako jsou pikobuňky a femtobuňky, vytvořilo složité interferenční scénáře. Plánovači sítí a normalizační orgány potřebovali jasný a standardizovaný způsob, jak odkazovat na uživatelská zařízení připojená k tradiční, vysokovýkonné vrstvě buněk, aby odlišili její chování a požadavky od zařízení připojených k nové, nízkovýkonné vrstvě.

Toto rozlišení je klíčové pro vývoj a vyhodnocování technik pro zmírnění interference. V HetNetu může UE na okraji makro buňky zažívat silnou interferenci z blízké small cell pracující na stejné frekvenci, a naopak. Kategorizací UE jako MUE (obsluhovaných makro buňkou) nebo PUE (obsluhovaných piko buňkou) mohly specifikace jako 3GPP TR 36.825 definovat konkrétní testovací scénáře, vyhodnocovat výkonnost nových algoritmů, jako je eICIC, a specifikovat, jak mají být zdroje (jako časové podrámce) rozděleny mezi vrstvami, aby se tato interference mezi vrstvami minimalizovala.

Bez této jasné terminologie by popis síťových algoritmů, simulačních předpokladů a výkonnostních požadavků pro různé uživatelské populace byl nejednoznačný. MUE slouží jako základní modelová entita, umožňující konzistentní analýzu pokrytí, kapacity a kvality služeb ve stále složitějších vícevrstvých rádiových přístupových sítích definovaných od LTE Release 8 výše.

## Klíčové vlastnosti

- Definováno jako UE přihlášené k makro buňce eNodeB/gNB.
- Slouží jako základní typ uživatele ve studiích heterogenních sítí (HetNet).
- Je vystaveno interferenci od jiných makro buněk a od small cells.
- Jeho výkonnost je klíčovou metrikou pro vyhodnocování technik koordinace interference mezi buňkami (ICIC).
- Jeho plánování a přidělování zdrojů je řízeno výhradně makro buňkou.
- Je protikladem k Pico UE (PUE), Home UE (HUE) nebo Relay UE v systémových simulacích.

## Definující specifikace

- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations

---

📖 **Anglický originál a plná specifikace:** [MUE na 3GPP Explorer](https://3gpp-explorer.com/glossary/mue/)
