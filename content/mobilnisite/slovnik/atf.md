---
slug: "atf"
url: "/mobilnisite/slovnik/atf/"
type: "slovnik"
title: "ATF – Antenna Test Function"
date: 2022-01-01
abbr: "ATF"
fullName: "Antenna Test Function"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/atf/"
summary: "ATF je síťová funkce definovaná pro testování a ověřování výkonu anténních systémů v sítích 5G NR. Je součástí frameworku OAM (provoz, správa a údržba) a umožňuje automatizované a standardizované test"
---

ATF je síťová funkce pro provoz, správu a údržbu (OAM) určená pro automatizované a standardizované testování a ověřování výkonu anténních systémů, včetně beamforming a MIMO, v sítích 5G NR.

## Popis

Antenna Test Function (ATF) je entita pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)) zavedená organizací 3GPP pro sítě New Radio (NR). Je umístěna v rámci systému správy sítě, typicky jako součást systému správy prvků ([EMS](/mobilnisite/slovnik/ems/)) nebo síťového řídicího systému ([NMS](/mobilnisite/slovnik/nms/)), a je zodpovědná za orchestraci a provádění testů anténních systémů základnových stanic 5G (gNB). Na rozdíl od tradičního ručního ověřování antén při instalaci umožňuje ATF automatizované, vzdálené a periodické testování, což je klíčové pro udržení výkonu pokročilých anténních systémů ([AAS](/mobilnisite/slovnik/aas/)), které využívají massive [MIMO](/mobilnisite/slovnik/mimo/) a beamforming.

Z architektonického hlediska ATF komunikuje s testovaným gNB prostřednictvím rozhraní pro správu, jako jsou například ta definovaná ve specifikacích 3GPP řady 28. Iniciuje testovací postupy zasíláním specifických příkazů pro testovací konfiguraci gNB. Rádiová jednotka a anténní pole gNB následně provedou požadované testy, které mohou zahrnovat vysílání známých testovacích signálů na specifických beamech nebo příjem signálů z testovací sondy. gNB shromažďuje měřená data (např. charakteristiky beam pattern, zisk, směrovost) a výsledky hlásí zpět ATF k analýze. ATF tyto výsledky porovnává s předdefinovanými výkonnostními prahy nebo referenčními hodnotami, aby určil stav vyhověl/nevyhověl.

Jak to funguje, zahrnuje koordinovanou sekvenci. Nejprve ATF může převést gNB nebo konkrétní buňku do testovacího režimu, aby zajistil, že testy nenaruší provozní komunikaci uživatelů. Poté nakonfiguruje anténní systém pro provoz v konkrétním testovacím režimu. Pro vysílací testy může ATF instruovat gNB k vyzařování spojité vlny nebo specifického referenčního signálu na definované sadě beamů. Pro přijímací testy může být zapojen externí zdroj testovacího signálu. Klíčové součásti zahrnují samotný software ATF, spravovaný gNB s možnostmi testovacího režimu a případně externí testovací zařízení. Jeho úlohou je ověřit, že anténní hardware a přidružený beamforming software fungují správně, a zajistit tak, že síť poskytuje slibované pokrytí, kapacitu a uživatelský komfort, které jsou závislé na přesném řízení beamů.

## K čemu slouží

ATF byla vytvořena, aby řešila významné provozní výzvy, které přinášejí pokročilé anténní systémy ([AAS](/mobilnisite/slovnik/aas/)) a beamforming v 5G NR. Tradiční antény byly z velké části pasivní a jejich výkon bylo možné ověřit jednoduchou fyzickou kontrolou a drive testy. Naproti tomu 5G AAS jsou aktivní, integrované systémy se stovkami prvků a jejich výkon je definován komplexními beam pattern řízenými softwarem. Ruční testování těchto systémů je nepraktické, časově náročné a drahé.

Primární problém, který ATF řeší, je potřeba efektivního, automatizovaného ověření výkonu antén v celém životním cyklu sítě – od počátečního nasazení a akceptačních testů až po průběžnou údržbu a detekci poruch. Zajišťuje, že jsou dosaženy zisky z beamforming a že výpadky pokrytí nebo degradace výkonu způsobené poruchami antény (jako je selhání prvku nebo odchylka kalibrace) mohou být detekovány proaktivně. Její vytvoření bylo motivováno snahou snížit provozní výdaje ([OPEX](/mobilnisite/slovnik/opex/)), zlepšit spolehlivost sítě a zajistit, že sofistikované funkce 5G, které jsou vysoce závislé na výkonu antény, fungují v terénu tak, jak bylo zamýšleno.

## Klíčové vlastnosti

- Umožňuje vzdálené, automatizované testování výkonu anténního systému gNB
- Podporuje testování jak vysílacích, tak přijímacích charakteristik beamů
- Integruje se se síťovými systémy OAM pro orchestrované provádění testů
- Definuje standardizované testovací postupy a formáty hlášení měření
- Usnadňuje ověřování výkonu proti předdefinovaným prahům
- Napomáhá detekci poruch a údržbě pokročilých anténních systémů (AAS)

## Související pojmy

- [AAS – Active Antenna System](/mobilnisite/slovnik/aas/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TS 36.509** (Rel-17) — EPC Special UE Conformance Testing Functions
- **TR 36.978** (Rel-13) — Antenna Test Function for MIMO OTA Testing
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures

---

📖 **Anglický originál a plná specifikace:** [ATF na 3GPP Explorer](https://3gpp-explorer.com/glossary/atf/)
