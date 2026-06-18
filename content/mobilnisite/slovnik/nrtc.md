---
slug: "nrtc"
url: "/mobilnisite/slovnik/nrtc/"
type: "slovnik"
title: "NRTC – NR Test Configuration"
date: 2025-01-01
abbr: "NRTC"
fullName: "NR Test Configuration"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nrtc/"
summary: "NRTC je standardizovaná sada parametrů a podmínek používaná pro testování a validaci zařízení a výkonu sítě NR (New Radio). Zajišťuje konzistentní a opakovatelné testování napříč dodavateli a laborato"
---

NRTC je standardizovaná sada parametrů a podmínek používaná pro testování a validaci zařízení a výkonu sítě New Radio (NR) za účelem zajištění konzistentních a opakovatelných výsledků.

## Popis

NR Test Configuration (NRTC) je základní koncept v rámci specifikací 3GPP, podrobně popsaný především v dokumentech jako 38.113 a 38.175. Definuje komplexní rámec pro testování shody uživatelských zařízení (UE) a základnových stanic (gNB) provozovaných v 5G New Radio (NR). NRTC specifikuje přesnou sadu rádiových podmínek, kanálových modelů, parametrů signálu a metrik výkonu, vůči kterým musí být zařízení nebo síťový prvek vyhodnocen. To zahrnuje definici konkrétních referenčních měřicích kanálů ([RMC](/mobilnisite/slovnik/rmc/)), podmínek šíření (např. profily útlumu), úrovní výkonu a šířek pásma za účelem vytvoření řízeného a reprodukovatelného testovacího prostředí.

Architektura testování s NRTC zahrnuje testovací zařízení, jako jsou systémy pro testování shody, které jsou naprogramovány s parametry NRTC tak, aby emulovaly standardizovanou NR buňku. Testované zařízení ([DUT](/mobilnisite/slovnik/dut/)) komunikuje s touto emulovanou buňkou a jeho výkon – metriky jako propustnost, latence, podíl chybných bloků ([BLER](/mobilnisite/slovnik/bler/)) a chování správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) – je měřen vůči prahovým hodnotám definovaným v konfiguraci. Mezi klíčové komponenty NRTC patří testovací kmitočty (např. FR1 nebo FR2), numerologie (rozestup subnosných), konfigurace fyzické vrstvy (např. modulační a kódovací schéma, počet anténních portů) a konkrétní testovací scénáře (např. mobilita, beamforming).

NRTC jsou kategorizovány pro různé účely testování, jako je rádiový přenos a příjem (Tx/Rx), výkon ([PER](/mobilnisite/slovnik/per/)) a správa rádiových zdrojů (RRM). Každá kategorie obsahuje sadu testovacích konfigurací přizpůsobených pro zatížení specifických funkcí protokolového zásobníku NR. Například výkonová NRTC může definovat scénář s vysokým rušením pro testování odolnosti kanálového kódování, zatímco RRM NRTC může definovat podmínky pro předání spojení. Role NRTC v síťovém ekosystému spočívá v tom, že slouží jako technický základ pro certifikační programy (jako [GCF](/mobilnisite/slovnik/gcf/) a PTCRB), čímž zajišťuje, že jakékoli UE nebo gNB deklarující shodu se standardy 3GPP se v reálných nasazeních s více dodavateli chová předvídatelně a interoperabilně.

## K čemu slouží

Účelem NRTC je řešit kritický problém nekonzistentního a neopakovatelného testování zařízení 5G NR. Před zavedením standardizovaných testovacích konfigurací mohla každá firma nebo zkušebna používat vlastní sadu podmínek, což znemožňovalo objektivní porovnání výkonu zařízení nebo záruku interoperability. Tento nedostatek jednotnosti byl významnou překážkou rychlého a spolehlivého zavádění nových generací bezdrátových technologií.

Historicky existovaly podobné koncepty pro předchozí technologie, jako je LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/) Test Configuration), ale zavedení NR v Rel-15 přineslo nové složitosti, jako jsou milimetrové vlny (mmWave), massive [MIMO](/mobilnisite/slovnik/mimo/) a flexibilní numerologie. Tato pokročilá řešení si vyžádala novou, sofistikovanější sadu testovacích konfigurací. Vytvoření NRTC bylo motivováno potřebou stanovit společný 'jazyk' pro testování, který mohou používat všichni hráči v ekosystému – výrobci čipových sad, výrobci zařízení, síťoví operátoři a dodavatelé testovacího vybavení. Odstraňuje omezení ad-hoc testování tím, že poskytuje řízený referenční bod, který je nezbytný pro validaci, že zařízení splňují náročné požadavky na výkon, spolehlivost a spektrální účinnost slibované technologií 5G.

## Klíčové vlastnosti

- Definuje standardizované modely rádiových kanálů pro reprodukovatelné podmínky útlumu
- Specifikuje referenční měřicí kanály (RMC) pro konzistentní generování signálu
- Pokrývá jak kmitočtové pásmo 1 (Sub-6 GHz), tak kmitočtové pásmo 2 (mmWave)
- Zahrnuje konfigurace pro testování výkonu (PER), správy rádiových zdrojů (RRM) a RF testování
- Podporuje více typů numerologie (např. SCS 15, 30, 60 kHz) a šířky pásma
- Poskytuje základ pro certifikaci shody organizacemi jako GCF a PTCRB

## Související pojmy

- [NR – New Radio](/mobilnisite/slovnik/nr/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.175** (Rel-19) — EMC for NR IAB Nodes

---

📖 **Anglický originál a plná specifikace:** [NRTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrtc/)
