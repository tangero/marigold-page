---
slug: "pmu"
url: "/mobilnisite/slovnik/pmu/"
type: "slovnik"
title: "PMU – Phasor Measurement Unit"
date: 2025-01-01
abbr: "PMU"
fullName: "Phasor Measurement Unit"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pmu/"
summary: "Zařízení měřící elektrický fázový úhel a velikost napětí a proudu v elektrizační soustavě, synchronizované vůči společnému časovému zdroji (např. GPS). V kontextu 3GPP jde o klíčový senzor pro aplikac"
---

PMU (fázorová měřicí jednotka) je zařízení, které měří elektrický fázový úhel a velikost napětí v elektrizační soustavě, synchronizované vůči společnému časovému zdroji, a je klíčovým senzorem pro aplikace chytrých sítí v sítích 3GPP.

## Popis

Fázorová měřicí jednotka (PMU) je vysoce přesné měřicí zařízení nasazované v přenosových a distribučních sítích elektrické energie. Jejím hlavním účelem je měření fázoru – velikosti a fázového úhlu – střídavých ([AC](/mobilnisite/slovnik/ac/)) průběhů napětí a proudu v konkrétních uzlech sítě. Tato měření jsou časově synchronizována, typicky pomocí signálů globálního polohového systému ([GPS](/mobilnisite/slovnik/gps/)), vůči společnému referenčnímu času [UTC](/mobilnisite/slovnik/utc/) s mikrosekundovou přesností, čímž vznikají tzv. synchronfázory. Základní činnost zahrnuje vzorkování AC průběhu vysokou rychlostí (často 30–60 vzorků na periodu), aplikaci algoritmu pro odhad fázoru (např. diskrétní Fourierova transformace) a časové označení výsledku. Výstupem je datový proud obsahující hodnoty fázoru, frekvenci, rychlost změny frekvence (ROCOF) a přesný časový štítek.

V rámci ekosystému 3GPP není PMU telekomunikační komponentou jako takovou, nýbrž kritickým koncovým bodem nebo senzorem v širším kontextu aplikací vertikálních odvětví, konkrétně pro chytré sítě a distribuci energie. Standardy 3GPP, zejména od vydání Release 16, definují požadavky na služby a systémovou architekturu pro podporu komunikačních potřeb zařízení, jako jsou PMU. Síť musí poskytovat ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a přesnou časovou synchronizaci nezbytnou pro efektivní fungování PMU v systému monitorování a řízení rozlehlé oblasti. Data z PMU se přenášejí přes síť 3GPP do koncentrátorů fázorových dat ([PDC](/mobilnisite/slovnik/pdc/)) a nakonec do řídicích center.

Úlohou sítě 3GPP je poskytnout komunikační infrastrukturu, která propojuje tyto geograficky rozptýlené PMU. Mezi klíčové síťové schopnosti patří podpora časově citlivé komunikace ([TSC](/mobilnisite/slovnik/tsc/)), vylepšené cíle pro latenci v uplinku a downlinku a síťová distribuce časové synchronizace (např. pomocí profilů protokolu [IEEE](/mobilnisite/slovnik/ieee/) 1588 Precision Time Protocol přes mobilní síť). Architektura zahrnuje PMU jako uživatelské zařízení (UE) nebo IoT zařízení připojené přes 5G rádiovou přístupovou síť (RAN) a core síť (5GC). Síť musí garantovat přísné parametry kvality služby (QoS) pro tyto kritické datové toky, aby se synchronfázorová data dostala do řídicího centra během několika desítek milisekund, což umožní vizualizaci stavu sítě v reálném čase, detekci anomálií a automatizované řídicí akce, jako je vyčlenění ostrova nebo odlehčování sítě.

## K čemu slouží

PMU byla vyvinuta, aby překonala omezení tradičních systémů SCADA v elektrizačních soustavách. SCADA systémy poskytovaly pomalejší, nesynchronizovaná měření, což ztěžovalo získání reálného, koherentního obrazu o stavu celé sítě. Tento nedostatek celoplošné, časově zarovnané přehlednosti přispíval k rozsáhlým výpadkům, protože operátoři nemohli v reálném čase pozorovat vznikající nestabilitu. PMU díky poskytování synchronizovaných měření z celé sítě umožňuje výpočet dynamického stavu sítě, což vede k opravdovému monitorování a řízení rozlehlé oblasti.

Integrace PMU do standardů 3GPP byla motivována potřebou všudypřítomné, spolehlivé a nákladově efektivní komunikace pro nasazení chytrých sítí. Tradiční komunikační metody energetiky, jako jsou vyhrazená optická vlákna nebo mikrovlnné spoje, jsou drahé a nepružné pro nasazení tisíců senzorů. Buněčné sítě, zejména 5G, nabízejí přesvědčivou alternativu díky své rozsáhlé pokrytí, zabudované bezpečnosti a nativní podpoře pro masivní IoT a kritickou komunikaci. Práce 3GPP, počínaje Release 16, formalizovala požadavky (např. na latenci, dostupnost, přesnost časové synchronizace) pro podporu aplikací založených na PMU, čímž zajistila, že 5G sítě mohou sloužit jako životaschopná komunikační páteř pro moderní, odolné elektrizační soustavy. To umožňuje energetickým společnostem flexibilněji nasazovat síťové senzory a využívat pokročilé analytické nástroje pro hodnocení stability, integraci obnovitelných zdrojů a lokalizaci poruch.

## Klíčové vlastnosti

- Vysoce přesné synchronizované měření fázorů napětí/proudu
- Časová synchronizace na úrovni mikrosekund, typicky zajištěná GPS nebo síťovým protokolem PTP
- Výstup datových proudů synchronfázorů obsahujících velikost, fázový úhel, frekvenci a ROCOF
- Podpora standardních datových formátů, jako je IEEE C37.118.2, pro interoperabilitu
- Integrace jako 3GPP uživatelského zařízení (UE) vyžadujícího síťové schopnosti URLLC a TSC
- Umožňuje řídicím centrům elektrizační soustavy reálné celoplošné povědomí o situaci

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 22.104** (Rel-19) — Service requirements for cyber-physical control apps
- **TR 22.867** (Rel-18) — Study on 5G Smart Energy and Infrastructure
- **TR 38.825** (Rel-16) — Study on NR Industrial IoT

---

📖 **Anglický originál a plná specifikace:** [PMU na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmu/)
