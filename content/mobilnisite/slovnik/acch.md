---
slug: "acch"
url: "/mobilnisite/slovnik/acch/"
type: "slovnik"
title: "ACCH – Associated Control Channel"
date: 2025-01-01
abbr: "ACCH"
fullName: "Associated Control Channel"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/acch/"
summary: "ACCH je logický řídicí kanál v GSM/UMTS, který je trvale asociován s vyhrazeným přenosovým kanálem (TCH) nebo samostatným vyhrazeným řídicím kanálem (SDCCH). Přenáší nezbytné signalizační informace pr"
---

ACCH je logický řídicí kanál trvale asociovaný s vyhrazeným přenosovým nebo řídicím kanálem, který přenáší nezbytné signalizační informace s nízkou latencí pro řízení hovoru, mobilitu a správu rádiových prostředků během aktivního spojení.

## Popis

Associated Control Channel (ACCH) je základní koncept logického kanálu v protokolové architektuře rádiového rozhraní GSM a UMTS, konkrétně definovaný ve slovníkových specifikacích 3GPP TS 21.905. Funguje jako sekundární, vyhrazený řídicí kanál, který je vnitřně spárován s primárním kanálem přenášejícím uživatelský provoz nebo signalizaci. V praxi je ACCH vždy asociován buď s přenosovým kanálem (TCH), který přenáší hlas nebo datové přenosy s přepojováním okruhů, nebo se samostatným vyhrazeným řídicím kanálem (SDCCH), jenž se používá pro signalizaci, když není aktivní žádný TCH (např. během aktualizace polohy nebo přenosu SMS). Tato asociace je pevná po dobu přiřazení kanálu.

Z architektonického hlediska není ACCH samostatným fyzickým prostředkem, ale logickou konstrukcí mapovanou na fyzickou vrstvu. V GSM jsou řídicí informace z ACCH typicky multiplexovány s uživatelskými daty z asociovaného TCH ve stejném fyzickém časovém slotu pomocí specifických strukturburstů a příznaků krádeže. Například u plnorychlostního přenosového kanálu (TCH/F) přidružená řídicí signalizace (označovaná jako SACCH/F) zabírá specifické rámce v rámci 26-rámcové multirámcové struktury. Toto těsné propojení zajišťuje, že řídicí signalizace má garantovaný, periodický přístup k rádiovému prostředku bez nutnosti soutěžit o sdílené společné kanály.

Z protokolového pohledu přenáší ACCH signalizační zprávy vrstvy 2 a vrstvy 3 klíčové pro udržování aktivního spojení. Jeho primární rolí je přenos měřicích hlášení, příkazů časového předstihu a informací pro řízení výkonu v uplinku i downlinku. Přenáší také zprávy vyšších vrstev pro řízení hovoru, přípravu předání spojení a řízení šifrovacího režimu. Provoz je obousměrný, s dobře definovanou strukturou a časováním. Pomalý asociovaný řídicí kanál (SACCH) poskytuje pravidelnou signalizační cestu s nízkou přenosovou rychlostí, zatímco rychlý asociovaný řídicí kanál ([FACCH](/mobilnisite/slovnik/facch/)), používaný pro naléhavou signalizaci jako jsou příkazy k předání spojení, funguje na principu 'krádeže' burstů z asociovaného TCH, čímž poskytuje mnohem nižší latenci na úkor okamžitého přerušení uživatelských dat.

Role ACCH je klíčová pro správu rádiových prostředků (RRM) a stabilitu spojení. Poskytnutím vyhrazené signalizační cesty v pásmu umožňuje kontinuální síťový dohled nad kvalitou rádiového spoje (prostřednictvím měřicích hlášení), přesné nastavování časového předstihu mobilní stanice pro udržení synchronizace a efektivní řízení výkonu. Tento uzavřený regulační okruh, umožněný ACCH, je nezbytný pro udržení kvality hovoru, minimalizaci interference, úsporu životnosti baterie a umožnění plynulých předání spojení. Jeho návrh odráží paradigma přepojování okruhů v sítích 2G/3G, kde je pro dobu trvání spojení zřízen vyhrazený, trvalý pár kanálů.

## K čemu slouží

ACCH byl vytvořen, aby řešil kritickou potřebu spolehlivé, nízkolatentní a vyhrazené signalizace souběžně s aktivním uživatelským spojením v sítích GSM. Předchozí buněčné systémy často postrádaly robustní, vždy dostupný řídicí mechanismus pro probíhající hovory, což činilo úkoly jako předání spojení, řízení výkonu a dohled nad spojením náročnými a potenciálně nespolehlivými, pokud byly závislé pouze na sdílených kanálech s náhodným přístupem. Koncept ACCH to vyřešil garantováním deterministické signalizační cesty vnitřně propojené s přenosovým kanálem.

Jeho zavedení s GSM R99 (a jeho základní práce v dřívějších specifikacích GSM) bylo motivováno požadavky služeb hlasu a dat s přepojováním okruhů. Tyto služby vyžadují kontinuální správu rádiového spoje v reálném čase. ACCH poskytuje nezbytnou signalizační schopnost 'mimo pásmo', avšak uvnitř kanálu, k provádění základních funkcí RRM bez narušení vnímání služby uživatelem. Umožňuje síti kontinuálně monitorovat sílu a kvalitu signálu od mobilní stanice, vydávat včasné příkazy k předání spojení prostřednictvím [FACCH](/mobilnisite/slovnik/facch/) a dynamicky upravovat přenosové parametry, což vše je zásadní pro dosažení vysoké kapacity, pokrytí a kvality služeb v buněčné síti.

ACCH představuje základní návrhový princip sítí 2G/3G: asociaci řídicích a přenosových prostředků. Řeší omezení použití společných řídicích kanálů (jako [BCCH](/mobilnisite/slovnik/bcch/), PCH, RACH) pro správu specifickou pro spojení, což by bylo neefektivní a pomalé. Vyčleněním části kapacity přiřazeného kanálu pro řízení zajišťuje rychlou, zabezpečenou a síťově řízenou signalizaci, která je imunní vůči soutěžení a přetížení na společných kanálech, čímž zvyšuje celkovou spolehlivost a výkon systému.

## Klíčové vlastnosti

- Trvalá logická asociace s TCH nebo SDCCH po dobu trvání spojení
- Přenáší nezbytné signalizační zprávy vrstvy 2/vrstvy 3 pro správu rádiových prostředků (RRM) a řízení hovoru
- Přenáší periodická měřicí hlášení, příkazy časového předstihu a příkazy pro řízení výkonu
- Implementován jako Pomalý ACCH (SACCH) pro pravidelnou signalizaci a Rychlý ACCH (FACCH) pro naléhavé příkazy
- Používá signalizaci v pásmu prostřednictvím multiplexování nebo krádeže burstů v rámci přiřazeného fyzického prostředku
- Umožňuje uzavřený regulační okruh pro adaptaci spoje, předání spojení a údržbu spojení

## Související pojmy

- [FACCH – Fast Associated Control CHannel](/mobilnisite/slovnik/facch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [ACCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/acch/)
