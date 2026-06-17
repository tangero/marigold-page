---
slug: "mdl"
url: "/mobilnisite/slovnik/mdl/"
type: "slovnik"
title: "MDL – Offset of NB-IoT Downlink channel number to Downlink EARFCN"
date: 2025-01-01
abbr: "MDL"
fullName: "Offset of NB-IoT Downlink channel number to Downlink EARFCN"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mdl/"
summary: "MDL je technický parametr offsetu používaný k mapování indexu úzkopásmového fyzického bloku zdrojů (PRB) nosné NB-IoT na odpovídající downlink E-UTRA Absolute Radio Frequency Channel Number (EARFCN)."
---

MDL je parametr offsetu, který mapuje index úzkopásmového PRB nosné NB-IoT na odpovídající downlink EARFCN pro správné zarovnání frekvence v rámci spektra LTE.

## Popis

MDL (Offset of NB-IoT Downlink channel number to Downlink [EARFCN](/mobilnisite/slovnik/earfcn/)) je základní parametr definovaný v rámci specifikací 3GPP pro technologii Narrowband Internet of Things (NB-IoT). NB-IoT je navrženo jako nízkopříkonová širokoplošná ([LPWA](/mobilnisite/slovnik/lpwa/)) radiová technologie, kterou lze nasadit ve třech režimech: samostatně (standalone), v ochranném pásmu (guard-band) a v pásmu (in-band) stávajícího spektra LTE. Parametr MDL se konkrétně týká scénářů nasazení in-band a guard-band, kde nosná NB-IoT zabírá podmnožinu fyzických bloků zdrojů (PRB) LTE. Jeho primární funkcí je poskytnout přesné mapování mezi indexem úzkopásmového fyzického bloku zdrojů používaného nosnou NB-IoT a downlink EARFCN hostitelské nosné LTE. Toto mapování je nezbytné, protože středová frekvence nosné NB-IoT je odvozena z frekvenční mřížky nosné LTE.

Technicky je downlink EARFCN ([E-UTRA](/mobilnisite/slovnik/e-utra/) Absolute Radio Frequency Channel Number) jedinečné číslo definující konkrétní frekvenci nosné LTE. Pro nasazení NB-IoT in-band zabírá nosná NB-IoT jeden fyzický blok zdrojů (180 kHz) v rámci šířky pásma nosné LTE. Offset MDL, vyjádřený jako celé číslo v jednotkách 100 kHz (odstup podnosných LTE), specifikuje frekvenční odchylku od středové frekvence nosné LTE ke středu přiřazeného PRB nosné NB-IoT. Tento výpočet umožňuje síti a UE určit přesnou rádiovou frekvenci pro synchronizační signály NB-IoT ([NPSS](/mobilnisite/slovnik/npss/) a NSSS) a rozhlasové kanály (NPBCH).

Parametr je definován ve specifikacích pro rádiový přenos a příjem základnové stanice (eNodeB) (např. 36.104, 36.141). Operátoři sítě konfigurují hodnotu MDL jako součást parametrů plánování buňky. UE tento parametr získává implicitně prostřednictvím synchronizace a dekódování systémových informací. Správná konfigurace MDL je klíčová pro zabránění interference mezi signály NB-IoT a hostitelskými signály LTE a zajišťuje, že nosná NB-IoT je správně umístěna v rámci přiřazeného PRB. Hraje nenápadnou, ale zásadní roli na RF vrstvě a umožňuje bezproblémovou integraci NB-IoT jako 'nové' technologie do stávající frekvenční mřížky LTE.

## K čemu slouží

MDL byl zaveden, aby vyřešil specifickou výzvu frekvenčního zarovnání spojenou s nasazením NB-IoT v rámci stávajícího spektra LTE. Před NB-IoT byla další [LPWA](/mobilnisite/slovnik/lpwa/) technologií LTE-M (eMTC), která znovu využívala celou strukturu nosné LTE. NB-IoT však bylo navrženo s novou šířkou pásma nosné 180 kHz, která nebyla zarovnána se středem nosné LTE. Pro nasazení in-band to znamenalo, že nosná NB-IoT bude ležet na PRB LTE s odstupem od středu. Bez standardizovaného parametru offsetu by vznikla nejednoznačnost v definici absolutní frekvence nosné NB-IoT, což by vedlo k potenciálnímu nesouladu a interferenci mezi službami NB-IoT a LTE sdílejícími stejné spektrum.

Vytvoření MDL bylo motivováno potřebou přesného plánování sítě a procedur vyhledávání buňky UE. Poskytuje deterministický vzorec pro odvození frekvence nosné NB-IoT ze známého [EARFCN](/mobilnisite/slovnik/earfcn/) LTE. Tato standardizace zajišťuje, že všechna UE a základnové stanice od různých výrobců interpretují umístění nosné konzistentně, což je předpoklad interoperability. Řeší omezení plynoucí z potřeby flexibilního, ale dobře definovaného frekvenčního vztahu mezi hostitelskou vrstvou LTE a vrstvou NB-IoT, což byl nový koncept zavedený specifikacemi NB-IoT 3GPP Rel-13.

## Klíčové vlastnosti

- Definuje frekvenční odchylku od hostitelského downlink EARFCN LTE ke středu nosné NB-IoT.
- Vyjádřeno v jednotkách 100 kHz, což odpovídá odstupu podnosných LTE.
- Nezbytné pro režimy nasazení NB-IoT in-band a guard-band.
- Používá se sítí pro přesné RF plánování a konfiguraci.
- Používá se UE během počátečního vyhledávání buňky k nalezení signálů NPSS/NSSS.
- Zajišťuje spektrální koexistenci a minimalizuje interferenci se signály LTE.

## Související pojmy

- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)

## Definující specifikace

- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node

---

📖 **Anglický originál a plná specifikace:** [MDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdl/)
