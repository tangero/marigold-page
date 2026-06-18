---
slug: "edt"
url: "/mobilnisite/slovnik/edt/"
type: "slovnik"
title: "EDT – Energy Detection Threshold"
date: 2026-01-01
abbr: "EDT"
fullName: "Energy Detection Threshold"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/edt/"
summary: "Prah detekce energie (Energy Detection Threshold, EDT) je klíčový parametr v bezdrátových systémech, zejména pro přístup do neregulovaného (licence-free) spektra, který definuje úroveň výkonu signálu,"
---

EDT je úroveň výkonu signálu, kterou zařízení používá k určení, zda je bezdrátový kanál obsazený, což je zásadní pro mechanismy Poslechu před vysíláním (Listen-Before-Talk) pro sdílení spektra.

## Popis

Prah detekce energie (Energy Detection Threshold, EDT) je konfigurovatelná úroveň výkonu, měřená v dBm, která slouží jako rozhodovací bod pro proceduru vyhodnocení volného kanálu (clear channel assessment, [CCA](/mobilnisite/slovnik/cca/)) bezdrátového zařízení. Když zařízení potřebuje vysílat, nejprve po stanovenou dobu naslouchá zamýšlenému kanálu. Během této naslouchací periody měří celkový přijímaný výkon v kanálu. Základní operace je prosté porovnání: pokud je naměřená energie nad EDT, zařízení prohlásí kanál za 'obsazený' a odloží své vysílání. Pokud je energie pod EDT, je kanál prohlášen za 'volný' a zařízení může přistoupit k vysílání, pokud to dovolují další pravidla.

Z architektonického hlediska je funkce EDT implementována ve fyzické vrstvě (Layer 1) radiového modemu zařízení. Klíčové komponenty zahrnují vysokofrekvenční ([RF](/mobilnisite/slovnik/rf/)) předkoncovou část, která přijímá signál, a obvody pro zpracování základního pásma, které provádějí měření energie a porovnání s uloženou prahovou hodnotou. Konkrétní hodnota EDT může být pevně stanovena regulací (např. [FCC](/mobilnisite/slovnik/fcc/) nebo [ETSI](/mobilnisite/slovnik/etsi/) pro neregulovaná pásma), dynamicky upravována sítí nebo nastavena implementací zařízení na základě zjištěných podmínek. V technologiích 3GPP, jako je Licence Assisted Access ([LAA](/mobilnisite/slovnik/laa/)) a [NR-U](/mobilnisite/slovnik/nr-u/), může gNB (základnová stanice) nebo UE signalizovat nebo konfigurovat parametry EDT jako součást řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)).

Jak EDT funguje v praxi, zahrnuje kompromisy. Nízký EDT činí zařízení velmi citlivým, což způsobuje, že odkládá vysílání i při přítomnosti slabého rušení, což podporuje koexistenci, ale může vést k nadměrně konzervativnímu nevyužití spektra. Vysoký EDT činí zařízení méně citlivým, což mu umožňuje vysílat agresivněji, což může zvýšit jeho vlastní propustnost, ale může způsobit škodlivé rušení jiným blízkým sítím. Nastavení EDT je proto kritickým aspektem řízení rádiových prostředků ([RRM](/mobilnisite/slovnik/rrm/)) pro provoz v neregulovaném spektru. Jeho úlohou je být základním strážcem přístupu ke kanálu, což umožňuje více systémům sdílet stejné médium s určitou mírou spravedlnosti a minimalizovat kolize, což je nezbytné pro předvídatelný výkon ve sdíleném spektru.

## K čemu slouží

EDT existuje, aby umožnil uspořádaný a spravedlivý sdílený přístup k neregulovanému nebo lehce regulovanému rádiovému spektru. Bez takového prahu by zařízení vysílala naslepo, což by vedlo k neustálým kolizím, zhoršenému výkonu pro všechny uživatele a nepoužitelnému sdílenému médiu – scénáři známému jako 'tragédie obecní pastviny'. Problém, který řeší, je zásadní pro jakýkoli distribuovaný bezdrátový systém: jak decentralizovaně určit, kdy je přijatelné vysílat.

Historický kontext jeho významu v 3GPP vychází ze zavedení LTE v neregulovaném spektru (LAA) v Release 13 a NR-U v Release 16. Předtím byla dominantní technologií v pásmech jako 5 GHz Wi-Fi, která používala CSMA/CA s vlastními definicemi EDT. Vstup 3GPP do neregulovaného spektra si vyžádal robustní mechanismus Poslechu před vysíláním (LBT), aby splnil regulatorní požadavky (např. ETSI EN 301 893) a zajistil pokojnou koexistenci s usedlými systémy, jako je Wi-Fi. EDT je centrálním parametrem tohoto mechanismu LBT.

Vytvoření a standardizace parametrů EDT v rámci 3GPP bylo motivováno potřebou, aby buněčné technologie fungovaly jako dobří sousedé ve sdílených pásmech. Řeší omezení předchozích buněčných systémů, které byly navrženy pro exkluzivní, licencované spektrum a takové detekční schopnosti nevyžadovaly. Definováním EDT umožňuje 3GPP síťově řízenou optimalizaci chování koexistence, vyvažující agresivní efektivitu buněčného plánování s ohleduplným přístupem založeným na soutěži, který je potřebný ve sdílených prostředích.

## Klíčové vlastnosti

- Definuje úroveň výkonu pro rozhodnutí o obsazeném/volném kanálu v CCA
- Konfigurovatelný a lze jej přizpůsobit na základě regulací nebo síťové politiky
- Základní pro Poslech před vysíláním (LBT) a detekci nosné (Carrier Sensing)
- Implementuje klíčový požadavek pro provoz v neregulovaném spektru (např. 5 GHz, 6 GHz)
- Může se lišit v závislosti na šířce pásma kanálu (širší pásmo může používat vyšší absolutní práh)
- Používá se jak v počáteční CCA, tak v rozšířené CCA (backoff) proceduře

## Související pojmy

- [LBT – Listen Before Talk](/mobilnisite/slovnik/lbt/)
- [CCA – Critical Communications Application](/mobilnisite/slovnik/cca/)
- [LAA – Licensed-Assisted Access](/mobilnisite/slovnik/laa/)
- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)

## Definující specifikace

- **TS 22.226** (Rel-19) — Global Text Telephony (GTT) Stage 1
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 23.731** (Rel-16) — 5G LCS Architecture Enhancement Study
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [EDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/edt/)
