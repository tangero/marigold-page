---
slug: "fnim"
url: "/mobilnisite/slovnik/fnim/"
type: "slovnik"
title: "FNIM – Federated Network Information Model"
date: 2025-01-01
abbr: "FNIM"
fullName: "Federated Network Information Model"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/fnim/"
summary: "Federated Network Information Model (FNIM) je standardizovaný informační rámec v rámci architektury Management and Orchestration (MANO) konsorcia 3GPP. Definuje společný datový model pro reprezentaci"
---

FNIM je standardizovaný 3GPP informační rámec, který definuje společný datový model pro síťové prostředky a služby za účelem umožnění interoperability správy mezi více dodavateli a doménami a automatizované orchestraci.

## Popis

Federated Network Information Model (FNIM) je klíčovou součástí rámce Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)) konsorcia 3GPP, konkrétně v rámci rodiny specifikací Network Resource Model (NRM). Nejde o jedinou databázi, ale o standardizovaný objektově orientovaný informační model, který definuje, jak jsou síťové elementy, jejich schopnosti, konfigurace a vztahy reprezentovány jako spravované objekty. Tento model poskytuje společný jazyk a strukturu pro řídicí data vyměňovaná mezi různými systémy správy, jako jsou Element Managers (EMs), Network Management Systems ([NMS](/mobilnisite/slovnik/nms/)) a systémy vyšší úrovně orchestrace, například Network Function Virtualization Orchestrator ([NFVO](/mobilnisite/slovnik/nfvo/)).

FNIM funguje tak, že specifikuje hierarchii tříd spravovaných objektů, z nichž každá má definované atributy, operace a notifikace. Tyto třídy modelují vše od fyzického hardwaru (např. stojany, karty, porty) přes virtualizované síťové funkce (VNFs), logická propojení až po měření výkonu. Klíčovým architektonickým principem je federace: FNIM umožňuje integraci informací z více, potenciálně heterogenních řídicích domén (např. doména RAN a doména core sítě, nebo sítě různých operátorů) do koherentního jednotného pohledu pro nadřazený systém správy. Toho je dosaženo pomocí standardizovaných referenčních bodů a rozhraní informačních služeb, které umožňují systémům objevovat, získávat a manipulovat s instancemi spravovaných objektů na základě schématu FNIM.

Mezi klíčové komponenty FNIM patří Generic Network Resource Model (GRNM), který poskytuje základní třídy objektů, a technologie-specifické deriváty, které tyto třídy rozšiřují pro konkrétní síťové domény, jako jsou 5G NR, LTE nebo síťové funkce 5GC. Model podporuje operace plného životního cyklu správy – vytvoření, konfiguraci, monitorování a ukončení – síťových prostředků. Jeho úlohou je fungovat jako schéma 'jediného zdroje pravdy', které umožňuje automatizované poskytování, korelaci chyb napříč doménami, zajištění služeb a optimalizaci v uzavřené smyčce. Dodržováním FNIM mohou systémy správy vzájemně spolupracovat bez nutnosti vlastních, bod-od-bodu integrací, což je zásadní pro správu rozsáhlých, více-dodavatelských 5G a cloud-nativních sítí.

## K čemu slouží

FNIM byl vytvořen, aby řešil kritickou výzvu složitosti a fragmentovanosti správy moderních telekomunikačních sítí. Před jeho standardizací se správa sítí výrazně opírala o proprietární Management Information Bases (MIBs) a rozhraní specifická pro zařízení každého dodavatele. To činilo poskytování služeb od konce ke konci, správu chyb a optimalizaci výkonu v síti s více dodavateli nesmírně pracným, náchylným k chybám a pomalým. Posun směrem k Network Functions Virtualization ([NFV](/mobilnisite/slovnik/nfv/)) a Software-Defined Networking (SDN) v letech 2010 tento problém ještě prohloubil, protože sítě se staly více softwarovými, dynamickými a skládaly se z elementů od mnoha dodavatelů.

Motivací pro FNIM bylo poskytnout jednotný, standardizovaný informační rámec, který by mohl sloužit jako základ pro vizi 3GPP automatizované, zero-touch správy sítě a služeb. Definováním společného modelu umožňuje systémům správy od různých dodavatelů nebo zodpovědným za různé domény, aby si informace bezproblémově rozuměly a vyměňovaly. Tím řeší problém sémantické interoperability – zajišťuje, že 'virtuální jádro procesoru' nebo 'instance síťového řezu' znamená totéž pro všechny systémy zapojené do jeho životního cyklu.

Historicky se vyvinul z jiných modelovacích snah, jako je model SID (Shared Information/Data) fóra TM Forum a informační modely [ETSI](/mobilnisite/slovnik/etsi/) NFV, a integruje je. Jeho vývoj v rámci 3GPP, začínající ve verzi 11, byl hnán potřebou telekomunikačně specifického modelu, který by dokázal zvládnout jedinečné požadavky síťových technologií 3GPP a zároveň umožňoval federaci s širšími ekosystémy [IT](/mobilnisite/slovnik/it/) správy. FNIM je tedy klíčovým enablerem pro dosažení cílů automatizace 5G, síťového řezání (kde každý řez vyžaduje vlastní spravovaný životní cyklus) a efektivní více-doménové orchestrace služeb.

## Klíčové vlastnosti

- Standardizované, objektově orientované schéma pro modelování fyzických a virtuálních síťových prostředků
- Podporuje federaci řídicích informací napříč více technologickými a administrativními doménami
- Umožňuje operace správy životního cyklu (vytvořit, získat, aktualizovat, smazat, notifikovat) na spravovaných objektech
- Poskytuje základ pro technologie-specifické modely prostředků (např. pro 5G NR, síťové funkce 5GC)
- Usnadňuje automatizované poskytování služeb a správu konfigurace
- Umožňuje korelaci chyb a výkonnostních dat napříč sítí s více dodavateli pro analýzu hlavní příčiny

## Související pojmy

- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)
- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)

## Definující specifikace

- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 28.820** (Rel-12) — Umbrella Operation Model for Fixed Mobile Convergence
- **TS 28.821** (Rel-13) — UML Model Repertoire for FMC Management
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.103** (Rel-19) — 3GPP Management IRP Overview
- **TS 32.107** (Rel-19) — Federated Network Information Model (FNIM)
- **TS 32.863** (Rel-13) — PM Measurement Metadata Definition

---

📖 **Anglický originál a plná specifikace:** [FNIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/fnim/)
