---
slug: "tod"
url: "/mobilnisite/slovnik/tod/"
type: "slovnik"
title: "TOD – Tele-Operated Driving"
date: 2025-01-01
abbr: "TOD"
fullName: "Tele-Operated Driving"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tod/"
summary: "Tele-Operated Driving (TOD) je služba 3GPP umožňující dálkové ovládání vozidel přes mobilní sítě. Vyžaduje ultra-spolehlivou komunikaci s nízkou latencí (URLLC) pro výměnu senzorových dat a příkazů v"
---

TOD je služba 3GPP pro dálkové ovládání vozidel přes mobilní sítě, vyžadující ultra-spolehlivou komunikaci s nízkou latencí pro výměnu senzorových dat a příkazů v reálném čase.

## Popis

Tele-Operated Driving (TOD) je služba definovaná ve standardech 3GPP, která umožňuje dálkové ovládání vozidel přes mobilní sítě. Je klíčovým případem užití pro 5G a další generace a vyžaduje přísné výkonnostní parametry, zejména ultra-nízkou latenci a vysokou spolehlivost, aby bylo zajištěno bezpečné a citlivé dálkové ovládání. Služba spočívá v tom, že vzdálený lidský operátor nebo automatizovaný systém přijímá od vozidla senzorová data v reálném čase (video, LiDAR, radar) a zpět odesílá odpovídající řídicí příkazy (řízení, akcelerace, brzdění). Systém 3GPP poskytuje komunikační rámec, přičemž specifikace detailně popisují potřebné toky kvality služby (QoS), požadavky na polohování pro vzdáleného operátora a vozidlo a metodiky hodnocení výkonu.

Z architektonického hlediska TOD využívá podporu [URLLC](/mobilnisite/slovnik/urllc/) a síťového řezání v systému 5G. Pro zajištění garantované přenosové rychlosti, rozpočtu zpoždění paketů a míry chybovosti paketů vyžadovaných pro službu teleoperace může být vytvořen vyhrazený síťový řez. Vozidlo funguje jako uživatelské zařízení (UE) s rozšířenými schopnostmi pro sběr senzorových dat, jejich kompresi a uplinkový přenos. Vzdálené řídicí centrum, hostující Tele-Operation Center (TOC), se k mobilní síti připojuje jako aplikační funkce ([AF](/mobilnisite/slovnik/af/)) nebo přes datovou síť. Jádrová síť 5G za použití funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) vytváří a spravuje [PDU](/mobilnisite/slovnik/pdu/) relace s odpovídajícími charakteristikami QoS pro obousměrné datové toky.

Mezi klíčové technické komponenty patří přesné polohování, které je zásadní pro situační povědomí vzdáleného operátora. Specifikace jako 3GPP TS 38.845 definují výkonnostní požadavky a jejich hodnocení pro polohování ve scénářích TOD. Služba dále závisí na end-to-end synchronizaci a časování, které jsou často podporovány síťovými časovými protokoly. Datové toky jsou typicky zpracovávány jako samostatné QoS toky – jeden pro vysokokapacitní uplinková senzorová data s nízkou latencí a druhý pro downlinkové řídicí příkazy s nízkou kapacitou a ultra-spolehlivostí. Specifikace pro testování a zajištění (např. TS 37.571) definují testy shody pro UE podporující funkce TOD, což zajišťuje splnění přísných výkonnostních kritérií nezbytných pro bezpečný provoz.

## K čemu slouží

Tele-Operated Driving byl zaveden, aby řešil omezení plně autonomních vozidel, zejména ve složitých, nepředvídatelných nebo legislativně omezených situacích. Zatímco [AI](/mobilnisite/slovnik/ai/) pro autonomní řízení pokročila, existují okrajové případy – jako jsou staveniště, místa nehod nebo selhání systému – kde je lidský úsudek a zásah lepší nebo zákonem vyžadovaný. TOD poskytuje záložní řešení, které umožňuje vzdálenému operátorovi bezpečně navigovat nebo přímo ovládat vozidlo. To umožňuje nasazení služeb autonomních vozidel, jako jsou robotaxi nebo autonomní kamiony, s pojistkou, čímž se zvyšuje důvěra veřejnosti a přijetí regulátory.

Vytvoření standardů TOD v rámci 3GPP bylo motivováno potřebou standardizovaného, spolehlivého a globálně interoperabilního komunikačního rámce. Předchozí ad-hoc řešení využívající proprietární rádiové spoje postrádala škálovatelnost, zabezpečení a garantovaný výkon buněčného systému. Práce 3GPP, začínající v pozdních vydáních 4G a dozrávající v 5G, si kladla za cíl definovat přesné síťové požadavky – latenci pod 10–50 ms, spolehlivost až 99,999 % a přesné polohování – které musí mobilní operátoři splnit, aby podpořili takové bezpečnostně kritické služby. Řeší problém, jak rozšířit lidskou schopnost řízení na velké vzdálenosti s téměř okamžitou zpětnou vazbou, což bylo s před-5G mobilními technologiemi kvůli jejich vyšší latenci a méně deterministickému výkonu nemožné.

## Klíčové vlastnosti

- Vyžaduje ultra-spolehlivou komunikaci s nízkou latencí (URLLC) s přísnými parametry QoS (např. latence <50 ms, spolehlivost >99,999 %)
- Podporuje obousměrné datové toky: uplink pro senzorová/video data a downlink pro řídicí příkazy
- Často je implementována pomocí vyhrazených 5G síťových řezů pro zaručení izolace výkonu
- Spoléhá se na služby vysoce přesného polohování (např. A-GNSS, RTK) pro povědomí o poloze vozidla a kontextu
- Definuje specifické výkonnostní požadavky a metodiky hodnocení v testovacích specifikacích 3GPP
- Umožňuje dálkové ovládání pro scénáře jako parkování, doručování, nákladní doprava a přeprava osob

## Související pojmy

- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TR 38.845** (Rel-17) — NR Positioning Use Cases Study
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS

---

📖 **Anglický originál a plná specifikace:** [TOD na 3GPP Explorer](https://3gpp-explorer.com/glossary/tod/)
