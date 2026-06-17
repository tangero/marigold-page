---
slug: "ei"
url: "/mobilnisite/slovnik/ei/"
type: "slovnik"
title: "EI – Error Indication"
date: 2025-01-01
abbr: "EI"
fullName: "Error Indication"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ei/"
summary: "Primitivní funkce protokolové vrstvy používaná k signalizaci chybového stavu z nižší vrstvy na vyšší vrstvu ve stohu protokolů 3GPP. Jde o základní mechanismus pro procedury hlášení chyb a obnovy, kte"
---

EI je primitivní funkce protokolové vrstvy používaná ve stohu protokolů 3GPP k signalizaci chybového stavu z nižší vrstvy na vyšší vrstvu za účelem hlášení a obnovy.

## Popis

Error Indication (EI) je primitivní funkce definovaná v architektuře protokolů 3GPP, konkrétně v kontextu bodů přístupu ke službám (SAP) mezi protokolovými vrstvami. Jde o řídicí primitivní funkci, nikoli primitivní funkci pro uživatelská data, používanou k oznámení, že nižší vrstva detekovala neodstranitelný chybový stav týkající se konkrétní instance služby nebo spojení. Když nižší vrstva (např. vrstva řízení rádiového spoje – RLC) narazí na závažnou poruchu, jako je překročení maximálního počtu retransmisí nebo selhání rádiového spoje, vygeneruje primitivní funkci EI a předá ji výše do vyšší vrstvy (např. vrstvě PDCP nebo [RRC](/mobilnisite/slovnik/rrc/)). Tato primitivní funkce obsahuje parametry identifikující zasaženou entitu, například identitu rádiového přenosového kanálu (Radio Bearer) nebo signalizačního rádiového přenosového kanálu (Signaling Radio Bearer).

Přijetí Error Indication spouští v vyšší vrstvě specifické akce obnovy. Například v LTE a 5G NR, pokud vrstva RLC odešle EI pro datový rádiový přenosový kanál, může vrstva PDCP zahájit proceduru jeho obnovení. Pro signalizační rádiové přenosové kanály může vrstva RRC interpretovat EI jako selhání rádiového spoje a zahájit procedury obnovení spojení. Mechanismus EI je klíčový pro udržení kontinuity služeb a robustnosti, neboť umožňuje síti a uživatelskému zařízení (UE) rychle reagovat na zhoršující se podmínky spoje.

Specifikace primitivní funkce EI, včetně jejích parametrů a přesných podmínek pro její generování, je podrobně popsána v 3GPP TS 26.110 a dalších specifikacích pro konkrétní vrstvy. Její implementace je nedílnou součástí vrstvového návrhu protokolů a poskytuje standardizovaný způsob komunikace poruchových stavů mezi vrstvami bez těsného propojení. Tato abstrakce je klíčová pro modularitu a udržovatelnost stohu protokolů 3GPP.

## K čemu slouží

Primitivní funkce Error Indication byla zavedena, aby poskytla standardizovanou, jednoznačnou metodu pro nižší protokolové vrstvy k hlášení kritických, neodstranitelných poruch vyšším vrstvám. Před zavedením takových formalizovaných mechanismů mohlo být zpracování chyb ad-hoc nebo závislé na implementaci, což vedlo k problémům s interoperabilitou a nepředvídatelnému chování při síťových poruchách. Primitivní funkce EI vytváří jasnou smlouvu mezi protokolovými vrstvami, definuje podmínky, za kterých je chyba hlášena, a očekávanou reakci přijímající vrstvy.

Její vytvoření bylo motivováno potřebou robustního řízení mobility a relací v paketově přepínaných celulárních sítích, jako jsou LTE a 5G NR. Protože tyto sítě podporují služby reálného času a komunikace s vysokou spolehlivostí, je rychlá detekce a obnova po selhání spoje prvořadá. Mechanismus EI umožňuje rychlou eskalaci problémů, což efektivně spouští procedury vyšších vrstev (jako je předávání spojení, rekonfigurace přenosového kanálu nebo obnovení spojení), minimalizuje přerušení služby a zachovává uživatelský zážitek.

## Klíčové vlastnosti

- Standardizovaná primitivní funkce pro hlášení chyb mezi vrstvami
- Spouští procedury obnovy a rekonstrukce ve vyšších vrstvách
- Nese identifikátory zasažené protokolové entity (např. Radio Bearer ID)
- Signalizuje neodstranitelné poruchy nižších vrstev
- Základní pro detekci a zpracování selhání rádiového spoje
- Definována pro řídicí i uživatelskou část stohu protokolů

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [EI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ei/)
