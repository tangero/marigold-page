---
slug: "cpu"
url: "/mobilnisite/slovnik/cpu/"
type: "slovnik"
title: "CPU – Channel State Information Processing Unit"
date: 2025-01-01
abbr: "CPU"
fullName: "Channel State Information Processing Unit"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cpu/"
summary: "Hardwarová nebo softwarová jednotka v sítích 5G/6G, která zpracovává informace o stavu kanálu (CSI) pro optimalizaci výkonu rádiového spoje. Analyzuje podmínky kanálu, počítá parametry jako prekódovac"
---

CPU je zpracovatelská jednotka v sítích 5G/6G, která analyzuje informace o stavu kanálu (Channel State Information) za účelem výpočtu parametrů, jako jsou prekódovací matice, a tím umožňuje pokročilé MIMO a beamforming pro optimalizaci výkonu rádiového spoje.

## Popis

Channel State Information Processing Unit (CPU) je specializovaná funkční entita v rámci uživatelského zařízení (UE) a/nebo gNodeB (gNB) zodpovědná za získávání, odhad a zpracování informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)). CSI je klíčová datová sada charakterizující aktuální podmínky šíření rádiového kanálu mezi vysílačem a přijímačem, včetně parametrů jako zesílení kanálu, fáze, rozprostření zpoždění a Dopplerův posuv. Primární úlohou CPU je přeměna hrubých měření kanálu na využitelné informace pro fyzickou vrstvu, což síti umožňuje přizpůsobovat přenosové strategie v reálném čase pro potlačení útlumu, interference a útlumu na dráze.

Z architektonického hlediska CPU komunikuje s přijímacím řetězcem zpracování signálu, typicky za modulem odhadu kanálu. Jeho činnost začíná příjmem referenčních signálů, jako jsou [CSI-RS](/mobilnisite/slovnik/csi-rs/) (Channel State Information Reference Signals) v downlinku nebo SRS (Sounding Reference Signals) v uplinku. Jednotka tyto signály zpracovává za účelem odhadu kanálové matice (H). Tento odhad zahrnuje pokročilé algoritmy pro potlačení šumu a interference. Po odhadu CPU provádí složité výpočty pro odvození klíčových přenosových parametrů. Mezi ně patří optimální indikátor prekódovací matice (PMI) pro [MIMO](/mobilnisite/slovnik/mimo/) prostorové multiplexování, indikátor řádu (RI) určující počet použitelných prostorových vrstev a indikátor kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), který doporučuje modulační a kódovací schéma ([MCS](/mobilnisite/slovnik/mcs/)). Pro pokročilé funkce jako beamforming CPU počítá beamformingové váhy.

Klíčové vnitřní komponenty CPU zahrnují odhadovač kanálu, výpočetní engine pro maticové operace lineární algebry (např. rozklad na singulární hodnoty pro eigenbeamforming), kvantizační modul pro redukci zpětné vazby (např. pro PMI) a řídicí logickou jednotku, která spravuje periodické nebo aperiodické reportovací cykly nakonfigurované vrstvou [RRC](/mobilnisite/slovnik/rrc/). V síti implementující massive MIMO je výpočetní zátěž CPU značná a často vyžaduje vyhrazené hardwarové akcelerátory nebo vysoce výkonné [DSP](/mobilnisite/slovnik/dsp/) jádra pro splnění termínů nízkolatenčního zpracování. Jeho výstup přímo vstupuje do scheduleru a prekodéru v gNB, čímž uzavírá adaptivní smyčku pro přizpůsobení spoje.

Úloha CPU je zásadní pro dosažení vysokých přenosových rychlostí a cílů spolehlivosti v 5G a 6G. Poskytováním přesných a včasných CSI umožňuje techniky jako uzavřená smyčka MIMO, kde vysílač prekóduje signály na základě zpětné vazby přijímače za účelem koherentního součtu energie na přijímači, což dramaticky zlepšuje poměr signálu k šumu (SNR). Je také nezbytná pro plánování multi-user MIMO ([MU-MIMO](/mobilnisite/slovnik/mu-mimo/)), kde CPU v gNB zpracovává CSI z více UE za účelem konstrukce ortogonálních paprsků minimalizujících interferenci mezi uživateli. V systémech s duplexem s frekvenčním dělením (FDD) CPU v UE kvantizuje a poskytuje zpětnou vazbu CSI přes PUCCH nebo PUSCH, zatímco v systémech s duplexem s časovým dělením (TDD) může CPU v gNB využít reciprocitu kanálu pomocí uplinkových SRS, což umožňuje efektivnější a přesnější správu paprsků bez explicitní zpětné vazby.

## K čemu slouží

CPU bylo zavedeno k řešení základní výzvy provozování vysokokapacitních bezdrátových systémů v časově proměnných a frekvenčně selektivních útlumových kanálech. Rané buněčné systémy používaly jednoduchá modulační a kódovací schémata s pevnou konfigurací, která byla neefektivní, protože se nemohla přizpůsobit rychlým změnám kanálu, což vedlo buď k nadměrnému plýtvání zdroji (použitím příliš robustních schémat), nebo k vysoké chybovosti paketů (použitím příliš agresivních schémat). Nástup technologie MIMO ve 3GPP Release 4 a dále vytvořil novou dimenzi složitosti; optimalizace prostorového multiplexování a diverzity vyžadovala podrobnou znalost víceanténní kanálové matice, nikoli pouze skalárního měření síly signálu.

Vytvoření CPU jako definované zpracovatelské jednotky formalizuje a optimalizuje tuto kritickou funkci. Řeší problém přizpůsobení kanálu v reálném čase poskytnutím vyhrazeného, standardizovaného modulu pro přeměnu měření kanálu na využitelné řídicí informace. To umožňuje pokročilé techniky fyzické vrstvy, jako je adaptivní modulace a kódování (AMC), uzavřená smyčka prostorového zpracování a beamforming. Bez efektivního zpracování CSI nelze realizovat potenciální zisky MIMO – jako je multiplikativní zvýšení kapacity a vylepšené pokrytí. CPU abstrahuje složité zpracování signálu, což umožňuje protokolům vyšších vrstev činit informovaná rozhodnutí o plánování a alokaci zdrojů na základě stručné sady indikátorů (PMI, RI, CQI).

Historicky, jak se systémy vyvíjely z 2G na 3G (WCDMA) a poté na 4G (LTE), rostla potřeba sofistikovanější zpětné vazby o kanálu. Zavedení konceptu CPU v Release 4 položilo základy pro sofistikované CSI frameworky v pozdějších releasech. Řešilo to omezení předchozích ad-hoc implementací specifikací zpracovatelských požadavků, reportovacích formátů a měřítek přesnosti, čímž zajišťovalo interoperabilitu a konzistenci výkonu mezi zařízeními různých výrobců. Tato standardizace byla pro ekosystém klíčová, protože umožnila vývoj specializovaného křemíku a softwaru, který dokázal držet krok s exponenciálně rostoucími výpočetními nároky massive MIMO a milimetrových vln v 5G NR.

## Klíčové vlastnosti

- Odhad kanálové matice z referenčních signálů (CSI-RS/SRS)
- Výpočet indikátoru prekódovací matice (PMI) pro beamforming a MIMO
- Stanovení indikátoru řádu (RI) pro výběr prostorových vrstev
- Výpočet indikátoru kvality kanálu (CQI) pro přizpůsobení spoje
- Podpora zpětné vazby pro duplex s frekvenčním dělením (FDD) i zpracování založeného na reciprocitě pro duplex s časovým dělením (TDD)
- Konfigurovatelné reportovací režimy (např. wideband, subband, aperiodický, periodický) pro správu režijních nákladů zpětné vazby

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TS 26.847** (Rel-19) — AI/ML Evaluation in 5G Media Services
- **TR 26.927** (Rel-19) — AI/ML in 5G Media Services Study
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 32.859** (Rel-12) — Alarm Management Quality Improvement Study
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz

---

📖 **Anglický originál a plná specifikace:** [CPU na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpu/)
