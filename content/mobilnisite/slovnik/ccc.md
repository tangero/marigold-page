---
slug: "ccc"
url: "/mobilnisite/slovnik/ccc/"
type: "slovnik"
title: "CCC – CPCH Control Command"
date: 2025-01-01
abbr: "CCC"
fullName: "CPCH Control Command"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ccc/"
summary: "CCC je řídicí příkaz používaný v proceduře společného paketového kanálu (CPCH) v UMTS. Spravuje uplinkové přenosy CPCH poskytováním příkazů pro řízení výkonu a úpravu časování z Node B do UE během pří"
---

CCC (CPCH Control Command) je řídicí příkaz společného paketového kanálu používaný v UMTS ke správě uplinkových přenosů poskytováním pokynů pro řízení výkonu a úpravu časování z Node B do UE.

## Popis

Řídicí příkaz společného paketového kanálu ([CPCH](/mobilnisite/slovnik/cpch/) Control Command – CCC) je klíčový signalizační prvek v rámci přístupové procedury společného paketového kanálu definované ve specifikacích 3GPP UMTS. CPCH byl navržen jako uplinkový transportní kanál pro přenosy paketových dat s nárazovou povahou, nabízející přístup na bázi kolizí s rychlými časy nastavení. CCC funguje v rámci přístupové procedury CPCH, která se skládá z více fází: přístupového preamblu ([AP](/mobilnisite/slovnik/ap/)), preamblu pro detekci kolizí ([CDP](/mobilnisite/slovnik/cdp/)), preamblu pro řízení výkonu CPCH ([PCP](/mobilnisite/slovnik/pcp/)) a vlastní fáze přenosu dat.

Během provozu CPCH, poté co UE úspěšně dokončí fáze AP a CDP, vstoupí do fáze PCP, kde vysílá preambly pro řízení výkonu. Node B tyto preambly monitoruje a reaguje příkazy CCC vysílanými na downlinkovém řídicím kanálu CPCH (C-CPCH). CCC obsahuje dvě hlavní složky: příkazy pro řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)) a příkazy pro úpravu časování ([TA](/mobilnisite/slovnik/ta/)). Příkazy TPC instruují UE, aby upravila svůj vysílací výkon pro udržení optimální kvality signálu na přijímači Node B a zároveň minimalizovala interferenci s ostatními uživateli. Příkazy TA upravují časování vysílání UE pro kompenzaci zpoždění šíření, čímž zajišťují uplinkovou synchronizaci a předcházejí intersymbolové interferenci.

CCC je vysílán pomocí specifických downlinkových fyzických kanálů, primárně sekundárního společného řídicího fyzického kanálu ([S-CCPCH](/mobilnisite/slovnik/s-ccpch/)) nebo vyhrazeného fyzického kanálu ([DPCH](/mobilnisite/slovnik/dpch/)), v závislosti na konfiguraci CPCH. Struktura příkazu je definována ve specifikacích fyzické vrstvy (25.211, 25.214) s přesným bitovým mapováním pro informace TPC a TA. Node B generuje CCC na základě měření přijatých signálů PCP, vypočítává potřebné úpravy pro optimalizaci kvality uplinkového přenosu. Tento mechanismus uzavřené smyčky řízení funguje nepřetržitě během přenosu CPCH, umožňuje dynamickou adaptaci na měnící se rádiové podmínky.

Z perspektivy protokolové architektury CCC funguje na vrstvě 1 (fyzická vrstva), ale je těsně integrován s procedurami vrstvy řízení přístupu k médiu (MAC). Vrstva MAC koordinuje pokusy o přístup k CPCH a spravuje přidělování zdrojů, zatímco fyzická vrstva implementuje vlastní vysílání a příjem CCC. Toto oddělení umožňuje efektivní implementaci při zachování těsné koordinace mezi řízením přístupu a optimalizací přenosu. Mechanismus CCC byl pro CPCH obzvláště důležitý, protože umožňoval rychlé řízení výkonu a časování bez nutnosti nastavení vyhrazeného kanálu, což jej činilo vhodným pro nárazové paketové aplikace s nízkou latencí.

## K čemu slouží

CCC byl vytvořen pro řešení specifických řídicích požadavků společného paketového kanálu v sítích UMTS. CPCH byl navržen jako vylepšení náhodného přístupového kanálu (RACH), poskytující vyšší datové rychlosti a efektivnější využití zdrojů pro nárazové paketové aplikace. Nicméně, povaha CPCH založená na kolizích a rychlejší časy přístupu vytvářely výzvy pro udržení kvality uplinkového přenosu bez rozsáhlých nastavovacích procedur vyhrazených kanálů.

Předchozí přístupy pro uplinkový paketový přenos, zejména RACH, postrádaly sofistikované uzavřené smyčky řízení výkonu a časování během počáteční fáze přenosu. Toto omezení vedlo k suboptimální kvalitě přenosu, vyšším úrovním interference a snížené kapacitě systému. CCC tento problém vyřešil poskytováním okamžité řídicí zpětné vazby během přenosu CPCH, což umožnilo Node B rychle optimalizovat parametry vysílání UE. To bylo obzvláště kritické pro CPCH, který si kladl za cíl podporovat vyšší datové rychlosti než RACH při zachování efektivity přístupu na bázi kolizí.

Historický kontext vývoje CCC byla evoluce UMTS směrem k lepší podpoře paketově orientovaných služeb ve vydání 4 a dále. S růstem mobilních datových aplikací vzrostla potřeba efektivních uplinkových kanálů, které by zvládly nárazový provoz s nízkou latencí. CCC umožnil CPCH poskytnout tuto schopnost při zachování správy interference a kvality přenosu nezbytné pro spolehlivou vysokorychlostní uplinkovou komunikaci. Ačkoli byly CPCH a CCC nakonec opuštěny ve prospěch vylepšených uplinkových technologií jako HSUPA, představovaly důležitý evoluční krok ve vývoji 3GPP efektivních mechanismů přístupu k paketům.

## Klíčové vlastnosti

- Poskytuje uzavřenou smyčku řízení výkonu během přenosu CPCH
- Umožňuje úpravu časování pro uplinkovou synchronizaci
- Vysílán na downlinkových řídicích kanálech (S-CCPCH/DPCH)
- Funguje během fáze preamblu pro řízení výkonu CPCH (PCP)
- Podporuje rychlou adaptaci na měnící se rádiové podmínky
- Integruje se s procedurami přístupu k CPCH na vrstvě MAC

## Definující specifikace

- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [CCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccc/)
