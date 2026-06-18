---
slug: "ecef"
url: "/mobilnisite/slovnik/ecef/"
type: "slovnik"
title: "ECEF – Earth-Centered, Earth-Fixed"
date: 2025-01-01
abbr: "ECEF"
fullName: "Earth-Centered, Earth-Fixed"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ecef/"
summary: "ECEF je standardní trojrozměrný kartézský souřadnicový systém používaný pro přesné pozemní určování polohy. Jeho počátek je v těžišti Země a osy jsou pevně spojeny s její rotací, což poskytuje stabiln"
---

ECEF je trojrozměrný kartézský souřadnicový systém s počátkem ve středu Země a osami pevně spojenými s planetou, který poskytuje stabilní referenční rámec pro pozemní určování polohy v sítích 3GPP.

## Popis

Earth-Centered, Earth-Fixed (ECEF) je trojrozměrný pravotočivý kartézský souřadnicový systém, který slouží jako základní geodetický referenční rámec v rámci specifikací 3GPP pro určování polohy a polohové služby. Počátek (0,0,0) systému ECEF je definován jako těžiště Země. Osa X vede z počátku průsečíkem rovníku a nultého poledníku (0° zeměpisné délky). Osa Y je v rovníkové rovině kolmá k ose X a vede přes 90° východní délky. Osa Z je zarovnána s osou rotace Země a směřuje k severnímu pólu. Klíčové je, že souřadnicové osy jsou 'pevné' vůči tělesu Země; rotují spolu s ní, na rozdíl od inerciálního rámce pevného v prostoru. To poskytuje stabilní, k Zemi vázaný referenční systém pro popis poloh objektů na povrchu Země nebo v její blízkosti.

V architekturách 3GPP se souřadnice ECEF (typicky vyjádřené v metrech jako trojice X, Y, Z) používají jako společný formát pro výměnu vysoce přesných polohových informací mezi síťovými entitami. Mezi klíčové funkční uzly využívající ECEF patří Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G, Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE a Standalone [SMLC](/mobilnisite/slovnik/smlc/) ([SAS](/mobilnisite/slovnik/sas/)) v UMTS. Tyto entity vypočítávají nebo přijímají odhady polohy UE a často je převádějí z jiných formátů (jako elipsoidní zeměpisná šířka/délka/výška) do ECEF pro interní výpočty nebo signalizaci. Například metody určování polohy jako Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) a Uplink Time Difference of Arrival ([UTDOA](/mobilnisite/slovnik/utdoa/)) zahrnují výpočet hyperboloidů na základě měření časových rozdílů; tyto geometrické výpočty se často provádějí efektivněji v kartézském prostoru ECEF.

Použití ECEF je nedílnou součástí fungování Assisted [GNSS](/mobilnisite/slovnik/gnss/) ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), primární metody vysoce přesného určování polohy. Síť (např. LMF) poskytuje UE asistenční data, která mohou zahrnovat ECEF souřadnice poloh a rychlostí družic GNSS, stejně jako ECEF polohu referenčního místa. To umožňuje přijímači GNSS v UE vypočítat přímo svou vlastní polohu v ECEF. Následně může být tato poloha převedena do uživatelsky přívětivějšího formátu, jako je zeměpisná šířka, délka a výška (LLA), na základě konkrétního referenčního elipsoidu (např. WGS-84). Standardizace ECEF napříč releasy 3GPP zajišťuje jednoznačné a matematicky konzistentní určování polohy napříč různými generacemi sítí (UMTS, LTE, NR) a mezi síťovým vybavením a UE od různých dodavatelů, což tvoří základ spolehlivých a interoperabilních polohových služeb.

## K čemu slouží

Zavedení souřadnicového systému ECEF v rámci 3GPP bylo motivováno potřebou přesného, jednoznačného a výpočetně efektivního referenčního rámce pro výpočty pozemního určování polohy. Rané mobilní polohové služby se často spoléhaly pouze na identitu buňky nebo sílu signálu, což poskytovalo pouze hrubé odhady polohy vázané na síť. Tlak na přesnější určování polohy pro nouzové služby (např. E-911 v USA) a komerční služby založené na poloze (LBS) si vyžádal integraci geometrických metod určování polohy jako GNSS a OTDOA. Tyto metody vyžadují rigorózní matematický rámec.

ECEF byl zvolen před jinými souřadnicovými systémy (jako čistá zeměpisná šířka/délka) z několika klíčových důvodů. Za prvé poskytuje skutečný 3D rámec nezbytný pro určování nadmořské výšky a pro výpočty zahrnující družice, jejichž dráhy jsou přirozeně popisovány v rámci se středem v Zemi. Za druhé jsou kartézské souřadnice (X, Y, Z) mnohem vhodnější pro vektorovou matematiku používanou při výpočtu vzdáleností, časových rozdílů příchodu a průsečíků hyperboloidů nebo koulí – což jsou základní operace v určování polohy metodami OTDOA a GNSS. Provádění těchto operací přímo v elipsoidních souřadnicích je složité a výpočetně náročné. Standardizací ECEF poskytlo 3GPP společný 'jazyk' pro vysoce přesná polohová data, který zjednodušuje implementace, snižuje chyby v transformaci souřadnic a zajišťuje, že výsledky určování polohy jsou konzistentní a interoperabilní v celosvětovém síťovém ekosystému.

## Klíčové vlastnosti

- Kartézský souřadnicový systém s počátkem v těžišti Země
- Osy pevně spojené s rotací Země (X prochází 0° zem. šířky/délky, Z prochází severním pólem)
- Poskytuje stabilní 3D referenční rámec pro pozemní a družicové určování polohy
- Umožňuje efektivní matematické výpočty pro geometrické metody určování polohy
- Standardizovaný formát pro signalizaci vysoce přesné polohy v sítích 3GPP
- Základní pro asistenční data A-GNSS a výpočty OTDOA/UTDOA

## Související pojmy

- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [WGS-84 – World Geodetic System 1984](/mobilnisite/slovnik/wgs-84/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TR 36.763** (Rel-17) — NB-IoT/eMTC Support for Non-Terrestrial Networks
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [ECEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecef/)
