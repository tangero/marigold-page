---
slug: "c-id"
url: "/mobilnisite/slovnik/c-id/"
type: "slovnik"
title: "C-ID – Cell Identifier"
date: 2025-01-01
abbr: "C-ID"
fullName: "Cell Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/c-id/"
summary: "Identifikátor buňky (C-ID) je jedinečný číselný identifikátor přiřazený každé buňce v síti 3GPP, který umožňuje její přesnou identifikaci a lokalizaci rádiových prostředků. Je zásadní pro výběr buňky,"
---

C-ID je jedinečný číselný identifikátor přiřazený každé buňce v síti 3GPP pro její přesnou identifikaci, což umožňuje výběr buňky, předávání hovoru (handover) a připojení zařízení ke konkrétním základnovým stanicím.

## Popis

Identifikátor buňky (C-ID) je kritický identifikátor síťového prvku definovaný ve specifikacích 3GPP, konkrétně podrobně popsaný v TS 25.423 pro rozhraní Iur. Slouží jako primární klíč pro rozlišení jedné rádiové buňky od všech ostatních v rámci veřejné pozemní mobilní sítě (PLMN) nebo konkrétní podsystému rádiové sítě (RNS). C-ID není samostatný globální identifikátor, ale typicky se používá v kombinaci s dalšími identifikátory, jako je identifikátor řadiče rádiové sítě (RNC-ID) nebo kód lokální oblasti ([LAC](/mobilnisite/slovnik/lac/)), aby vytvořil globálně jednoznačnou adresu buňky. Toto složené adresování je nezbytné, protože více buněk spravovaných různými RNC nebo v různých geografických oblastech by teoreticky mohlo mít lokálně přiřazenou stejnou hodnotu C-ID.

Z architektonického hlediska spravuje a přiřazuje C-ID řadič rádiové sítě (RNC) v sítích UMTS nebo odpovídající řídicí uzel v jiných technologiích radiového přístupu 3GPP. Je zabudován do různých zpráv řídicí roviny a uživatelské roviny vyměňovaných přes síťová rozhraní, nejvýznamněji přes rozhraní Iur mezi RNC a rozhraní Iub mezi RNC a jeho Node B. Když uživatelské zařízení (UE) provádí měření, hlásí zjištěný C-ID sousedních buněk, které síť využívá pro rozhodování o předávání hovoru. Samotná síť používá C-ID pro směrování pagingových zpráv, správu rádiových prostředků (jako jsou kanalizační kódy a scrambling kódy) a sběr výkonnostních statistik pro konkrétní buňky.

Role C-ID přesahuje rámec základní identifikace. Je nedílnou součástí operačních parametrů buňky. Například C-ID může být algoritmicky propojeno s primárním scrambling kódem (PSC) používaným v UMTS založeném na WCDMA, což pomáhá UE během procesu hledání buňky a synchronizace. V operačních a údržbových systémech je C-ID primárním údajem pro konfiguraci parametrů specifických pro buňku (např. výkon vysílače, sklon antény), spouštění alarmů a sledování klíčových výkonnostních ukazatelů ([KPI](/mobilnisite/slovnik/kpi/)), jako je míra zrušení hovoru nebo vytížení. Jeho konzistentní používání napříč rozhraními zajišťuje, že na buňku je jednoznačně odkazováno ve všech síťových procedurách, od správy rádiových prostředků až po sledování mobility v jádře sítě.

## K čemu slouží

Identifikátor buňky byl vytvořen k řešení základního problému jednoznačné adresace základní jednotky pokrytí – buňky – v celulární síti. Před standardizovanými celulárními systémy používaly proprietární sítě různé ad-hoc metody pro označování buněk, což bránilo interoperabilitě, zejména u funkcí jako předávání hovoru mezi RNC nebo roaming mezi různými výrobci síťového vybavení. C-ID poskytuje standardizované, jednoduché číselné schéma, které umožňuje každé síťové entitě – UE, RNC, Node B a prvkům jádra sítě – mít společný odkaz na konkrétní rádiový prostředek.

Jeho zavedení bylo motivováno potřebou automatizované a spolehlivé správy mobility. Jak sítě houstly s rostoucím počtem buněk, ruční konfigurace a sledování se staly nemožnými. C-ID umožňuje automatizované procesy, jako je předávání hovoru, při kterém musí UE plynule přenést své spojení ze zdrojové buňky do cílové buňky. Bez jedinečného identifikátoru pro každou buňku, na kterém se síť shodne, by systém nemohl správně nasměrovat UE nebo přenést jeho kontext. Dále pro správu a optimalizaci sítě potřebují inženýři přesně určit, která buňka zažívá zahlcení, interference nebo poruchy. C-ID slouží jako tento přesný lokalizátor ve všech operačních podpůrných systémech a mění surové rádiové signály na spravovatelné síťové objekty.

## Klíčové vlastnosti

- Jednoznačně identifikuje buňku v rámci působnosti jejího řídicího RNC nebo definované oblasti.
- Základní parametr pro procedury předávání hovoru mezi buňkami a mezi RNC.
- Používáno UE v měřicích hlášeních pro síťově řízenou mobilitu.
- Klíčový index pro operační a údržbové systémy (O&M) pro konfiguraci a monitorování výkonu buňky.
- Často propojeno s parametry fyzické vrstvy, jako jsou scrambling kódy, pro hledání buňky.
- Přenášeno v signalizačních zprávách RANAP a RNSAP přes rozhraní Iu a Iur.

## Související pojmy

- [LAC – L2TP Access Concentrator](/mobilnisite/slovnik/lac/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification

---

📖 **Anglický originál a plná specifikace:** [C-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/c-id/)
