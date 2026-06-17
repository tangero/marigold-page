---
slug: "edp"
url: "/mobilnisite/slovnik/edp/"
type: "slovnik"
title: "EDP – Event Detection Point"
date: 2025-01-01
abbr: "EDP"
fullName: "Event Detection Point"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/edp/"
summary: "Event Detection Point (EDP, bod detekce události) je koncept v rámci servisních architektur CAMEL (Customized Applications for Mobile network Enhanced Logic) a IMS (IP Multimedia Subsystem). Představu"
---

EDP je bod ve stavu hovoru nebo relace v rámci CAMEL nebo IMS, kde může být funkce řízení služeb upozorněna nebo může požádat o instrukce, aby umožnila síťově řízené služby.

## Popis

Event Detection Point (EDP, bod detekce události) je základní stavební prvek v architekturách služeb Intelligent Network ([IN](/mobilnisite/slovnik/in/)) a IP Multimedia Subsystem (IMS) podle 3GPP, konkrétně v rámci paradigmat řízení služeb [CAMEL](/mobilnisite/slovnik/camel/) a SIP. Definuje přesný okamžik nebo stav během zpracování hovoru, relace nebo uživatelské aktivity, kdy se může servisní logika sítě interagovat s řízením hovoru/relace. EDP jsou konfigurovány v síťových přepínacích nebo řídicích uzlech pro relace, jako je [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) pro hovory v okruhově přepínané síti nebo S-CSCF (Serving Call Session Control Function) pro IMS relace. Když zpracování hovoru/relace dosáhne bodu označeného jako EDP, řídicí uzel (Service Switching Function, SSF) může spustit interakci s externí entitou servisní logiky, typicky Service Control Function (SCF) nebo Application Server ([AS](/mobilnisite/slovnik/as/)).

Fungování EDP se řídí předem stanoveným profilem servisní logiky nebo počátečními filtračními kritérii. Řídicí uzel (např. MSC, S-CSCF) monitoruje stav hovoru a při dosažení EDP pozastaví své běžné zpracování. Poté formuluje servisní požadavek, který zapouzdří relevantní data o hovoru/relaci, a odešle jej určenému SCF/AS. Tato interakce umožňuje externí servisní logice rozhodovat a ovlivňovat průběh hovoru, například aplikovat účtování, upravovat směrování, přehrávat hlášení nebo sbírat uživatelský vstup. SCF/AS odpoví instrukcemi (např. Continue, Connect, Release), které řídicí uzel následně provede a odpovídajícím způsobem obnoví zpracování hovoru.

EDP se primárně dělí na dva typy: [EDP-R](/mobilnisite/slovnik/edp-r/) (Request, žádost) a [EDP-N](/mobilnisite/slovnik/edp-n/) (Notification, notifikace), zavedené v pozdějších verzích, ale základní koncept EDP zahrnuje samotný mechanismus detekce a hlášení. Jsou klíčové pro umožnění oddělené servisní architektury, kde servisní logika sídlí ve vyhrazených, znovupoužitelných aplikačních serverech namísto toho, aby byla pevně zakódována do přepínacího zařízení. Tento model umožňuje rychlé vytváření, úpravy a personalizaci služeb bez nutnosti aktualizace každého síťového přepínače. EDP jsou definovány pro různé události hovoru/relace, jako je zahájení hovoru (O-BCSM), ukončení hovoru (T-BCSM) a specifické události během hovoru, jako je zvednutí volaným nebo odpojení.

## K čemu slouží

Koncept Event Detection Point byl vytvořen, aby řešil omezení tradičních telefonních sítí, kde byly služby těsně integrovány a pevně zakódovány do monolitických přepínacích systémů. To zavedení nových služeb zpomalovalo, zvyšovalo náklady a bylo závislé na dodavateli. Koncept Intelligent Network ([IN](/mobilnisite/slovnik/in/)), standardizovaný [ITU-T](/mobilnisite/slovnik/itu-t/) a přijatý 3GPP jako CAMEL, zavedl vrstvenou architekturu oddělující funkci řízení hovoru (Service Switching Function) od servisní logiky (Service Control Function). EDP jsou kritické 'háčky' nebo spouštěče uvnitř přepínače, které toto oddělení umožňují.

Definováním specifických, standardizovaných bodů v modelu hovoru, kde lze předat řízení externí entitě, EDP řeší problém nepružnosti služeb. Umožňují síťovým operátorům nasadit centralizované servisní platformy (SCP), které mohou řídit hovory směrované přes mnoho různých přepínačů od různých dodavatelů. Tato architektura je zásadní pro implementaci komplexních, síťově širokých služeb, jako je účtování předplacených služeb v reálném čase, virtuální privátní sítě (VPN), bezplatná čísla a přenosnost čísel. Vytvoření EDP motivovalo vývoj živého ekosystému služeb s přidanou hodnotou, který přesáhl rámec základní hlasové telefonie. Při vývoji směrem k IMS byl koncept EDP přizpůsoben pro řízení SIP relací, čímž byla zajištěna kontinuita inteligentního řízení služeb ve všech-IP sítích.

## Klíčové vlastnosti

- Definuje přesné body v modelech stavu hovoru/relace (např. O-BCSM, T-BCSM) pro interakci se službou
- Umožňuje oddělení servisní logiky (SCF/AS) od řízení přenosu (MSC, CSCF)
- Podporuje pozastavení zpracování hovoru při čekání na instrukce od servisní logiky
- Přenáší relevantní data o hovoru/relaci (např. volající/volaná čísla, poloha) v servisních požadavcích
- Umožňuje servisní logice vracet řídicí instrukce, jako je Continue, Connect nebo Release
- Základní pro fungování rozhraní CAMEL a IMS Service Control (ISC)

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management

---

📖 **Anglický originál a plná specifikace:** [EDP na 3GPP Explorer](https://3gpp-explorer.com/glossary/edp/)
