---
slug: "hof"
url: "/mobilnisite/slovnik/hof/"
type: "slovnik"
title: "HOF – HandOver Failure"
date: 2025-01-01
abbr: "HOF"
fullName: "HandOver Failure"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hof/"
summary: "Událost selhání, která nastává, když procedura předání spojení není úspěšná a způsobí selhání rádiového spoje. Je to klíčový ukazatel výkonnosti (KPI) pro optimalizaci sítě, který přímo ovlivňuje uživ"
---

HOF je událost selhání, při níž je procedura předání spojení neúspěšná, což způsobí selhání rádiového spoje a ovlivní uživatelský komfort; jedná se o klíčový KPI pro optimalizaci sítě.

## Popis

HandOver Failure (HOF) je specifický typ selhání rádiového spoje ([RLF](/mobilnisite/slovnik/rlf/)), ke kterému dochází během provádění procedury předání spojení ([HO](/mobilnisite/slovnik/ho/)). Předání spojení je proces převodu probíhajícího hovoru nebo datové relace z jedné buňky (zdrojová buňka) do jiné (cílová buňka). HOF je deklarováno, když se tento převodový proces neúspěšně dokončí, což vede k přerušení nebo ztrátě spojení uživatelského zařízení (UE). Síť a UE provádějí rozsáhlá měření, signalizaci a přípravu prostředků, aby předání spojení provedly; selhání v kterémkoli z těchto kroků může mít za následek HOF. Z hlediska měření je HOF klíčový ukazatel výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)) mobility, který operátoři nepřetržitě sledují, aby vyhodnotili stav a výkon sítě.

Procedura HOF a její detekční mechanismy jsou hluboce integrovány do protokolu řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)). Proces začíná tím, že zdrojová základnová stanice (např. gNB v 5G, [eNB](/mobilnisite/slovnik/enb/) v LTE) rozhodne o předání spojení na základě měřicích reportů od UE. Poté vydá UE příkaz k předání spojení (zpráva RRCConnectionReconfiguration s mobilityControllnfo). K HOF může dojít v několika fázích: selhání příjmu příkazu k předání spojení, selhání přístupu k cílové buňce (selhání na náhodném přístupovém kanále), selhání dokončení rekonfigurace RRC s cílovou buňkou nebo vypršení časového limitu během provádění. Po zjištění podmínek selhání UE zahájí procedury selhání rádiového spoje, které mohou zahrnovat pokusy o výběr buňky a opětovné navázání spojení, a často hlásí příčinu selhání síti k analýze.

V širší síťové architektuře se do řízení HOF zapojuje několik síťových prvků. Uzly rádiové přístupové sítě (RAN) jsou primárně odpovědné za provádění předání spojení a detekci selhání. Systémy pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)) shromažďují od těchto uzlů statistiky HOF a další související měření (jako je míra úspěšnosti předání spojení). Tyto statistiky využívají funkce samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)), konkrétně optimalizace robustnosti mobility ([MRO](/mobilnisite/slovnik/mro/)). Algoritmy MRO analyzují vzorce HOF (např. předčasné předání spojení, pozdní předání spojení, předání spojení do nesprávné buňky) a automaticky upravují řídicí parametry předání spojení, jako je hystereze, čas do spuštění a individuální posuny buněk, aby minimalizovaly budoucí selhání, čímž vytvářejí samoléčící a samooptymalizující síť.

## K čemu slouží

HOF existuje jako definovaný koncept a KPI pro kvantitativní měření a řízení spolehlivosti funkce mobility, která je pro celulární sítě zásadní. Primární problém, který řeší, je kontinuita služby. V mobilní síti se uživatelé pohybují a jejich spojení musí být plynule předávána mezi buňkami, aby byla služba zachována. Selhání v tomto procesu přímo vedou ke špatnému uživatelskému komfortu v podobě přerušených hovorů, zamrzlých video streamů nebo přerušených datových relací. Definováním a měřením HOF mohou operátoři identifikovat problematické oblasti, hranice buněk nebo nastavení parametrů, která způsobují zhoršení služby.

Historicky se selhání předání spojení reaktivně analyzovala pomocí testů v terénu a stížností zákazníků. Standardizace reportování HOF, zejména se zavedením SON ve 3GPP Rel-9 a později, poskytla proaktivní, automatizovaný mechanismus pro detekci selhání a analýzu hlavní příčiny. To bylo motivováno rostoucí složitostí sítí (heterogenní sítě s makrobuňkami a small buňkami), která činila manuální optimalizaci nepraktickou. Funkce MRO využívá data HOF spolu s dalšími měřeními, jako je 'Too Early Handover' a 'Too Late Handover', k automatickému ladění síťových parametrů, čímž řeší problém suboptimálního výkonu předání spojení v dynamicky se měnícím rádiovém prostředí. Tím je zajištěno, že robustní mobilita je zachována, jak se sítě vyvíjejí ze 4G na 5G a dále.

## Klíčové vlastnosti

- Definováno jako podtyp selhání rádiového spoje (RLF) vyskytující se během provádění předání spojení
- Spouští specifické procedury na straně UE, jako je opětovné navázání RRC spojení
- Klíčový vstup pro algoritmy SON pro optimalizaci robustnosti mobility (MRO)
- Reportováno s podrobnými příčinami selhání (např. vypršení T304, selhání náhodného přístupu)
- Sledováno jako klíčový síťový KPI pro kvalitu služby
- Zahrnuje selhání koordinace mezi zdrojovou buňkou, cílovou buňkou a UE

## Definující specifikace

- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study
- **TS 36.839** (Rel-11) — HetNet Mobility Improvements for LTE
- **TS 36.842** (Rel-12) — Small Cell Enhancements for LTE Higher Layers
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 38.744** (Rel-19) — AI/ML for NR Mobility Study

---

📖 **Anglický originál a plná specifikace:** [HOF na 3GPP Explorer](https://3gpp-explorer.com/glossary/hof/)
