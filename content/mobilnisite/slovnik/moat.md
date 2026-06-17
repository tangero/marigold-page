---
slug: "moat"
url: "/mobilnisite/slovnik/moat/"
type: "slovnik"
title: "MOAT – Mobile Originated Application Terminated"
date: 2025-01-01
abbr: "MOAT"
fullName: "Mobile Originated Application Terminated"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/moat/"
summary: "MOAT je schopnost služby 3GPP, kdy mobilní zařízení iniciuje požadavek, který vede k události ukončené na aplikaci, jako je spuštění stahování nebo aktivace vzdálené služby. Umožňuje efektivní interak"
---

MOAT je schopnost služby 3GPP, kdy mobilní zařízení iniciuje požadavek, který vede k události ukončené na aplikaci, což umožňuje efektivní interakce spouštěné zařízením pro scénáře IoT a M2M.

## Popis

Mobile Originated Application Terminated (MOAT) je schopnost služby 3GPP definovaná od vydání Release 16, která usnadňuje scénáře, kdy uživatelské zařízení (UE) iniciuje požadavek, jehož výsledkem je akce na aplikační úrovni ukončená na UE nebo síťové aplikaci. Je zvláště relevantní pro komunikaci IoT a Machine-to-Machine (M2M), kde zařízení může vyslat signál k zahájení následného procesu, jako je spuštění aktualizace firmwaru nebo změny konfigurace. Architektura zahrnuje UE, síť 3GPP (včetně RAN a CN) a aplikační servery, přičemž postupy jsou standardizovány pro zajištění bezproblémové interakce.

Jak to funguje: Ve scénáři MOAT odešle UE uplink zprávu, často servisní požadavek nebo datový paket, do sítě. Tato zpráva je směrována na aplikační server (např. přes [UPF](/mobilnisite/slovnik/upf/) v 5G). Na základě této iniciace pak aplikační server spustí ukončenou akci směrem ke stejnému UE nebo jiné entitě. Například senzor odesílající upozornění na překročení prahové hodnoty (mobilně iniciováno) může způsobit, že server odešle příkaz zpět senzoru (ukončeno na aplikaci) pro úpravu jeho nastavení. Proces využívá stávající mechanismy 3GPP pro přenos dat a správu relací s vylepšeními pro podporu signalizace a interakcí na vrstvě služeb. Klíčové komponenty zahrnují aplikačního klienta v UE, uživatelskou rovinu sítě pro přenos dat a aplikační server, který zpracovává spouštěč MOAT.

Úlohou MOAT je umožnit efektivní, událostmi řízenou komunikaci v automatizovaných systémech, snížením latence a režie spojením mobilně iniciované události s ukončenou akcí. Je specifikována v dokumentech jako 22.262 (požadavky na služby) a 23.554 (architektura), což zajišťuje její integraci s funkcemi 5G core sítě, jako je [NEF](/mobilnisite/slovnik/nef/) (Network Exposure Function) pro spouštěče založené na [API](/mobilnisite/slovnik/api/). Tato schopnost podporuje případy užití v průmyslovém IoT, chytrých městech a vzdálené správě, kde zařízení potřebují iniciovat síťově spouštěné odezvy.

## K čemu slouží

MOAT byla vytvořena pro řešení potřeby zjednodušených interakcí iniciovaných zařízením v ekosystémech IoT a M2M, kde byly tradiční modely klient-server neefektivní. Před její standardizací scénáře vyžadující, aby zařízení spustilo síťovou akci, často zahrnovaly složitá proprietární řešení nebo více kol zpráv, což vedlo ke zvýšené latenci a spotřebě prostředků. Mezi omezení patřil nedostatek jednotných postupů napříč různými službami a sítěmi, což ztěžovalo interoperabilitu.

Motivace pro MOAT vychází z růstu automatizovaných služeb v 5G, jako je vzdálená správa zařízení, prediktivní údržba a systémy řízení v reálném čase. 3GPP Release 16 zavedlo MOAT jako součást rozšířených schopností služeb, čímž vyřešilo problém umožnění, aby mobilně iniciovaná událost bezproblémově způsobila akci ukončenou na aplikaci. Tím se snižuje signalizační režie a zlepšuje se rychlost odezvy, což je klíčové pro časově citlivé aplikace IoT. Historicky dřívější řešení M2M spoléhala na individuální implementace; MOAT poskytuje standardizovaný rámec v rámci 3GPP, který je v souladu s trendy směřujícími k síťovému řezání a edge computingu pro podporu různorodých požadavků vertikálních odvětví.

## Klíčové vlastnosti

- Umožňuje požadavky iniciované UE spouštět akce ukončené na aplikaci
- Podporuje případy užití IoT a M2M, jako jsou vzdálené spouštěče a aktualizace
- Integruje se s funkcemi 5G Core Network (např. NEF, UPF)
- Snižuje latenci spojením iniciační a ukončovací události
- Standardizováno v 3GPP pro interoperabilitu napříč sítěmi
- Usnadňuje událostmi řízenou komunikaci pro automatizaci

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 22.262** (Rel-19) — MSGin5G Service Requirements
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture

---

📖 **Anglický originál a plná specifikace:** [MOAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/moat/)
