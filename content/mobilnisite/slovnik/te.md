---
slug: "te"
url: "/mobilnisite/slovnik/te/"
type: "slovnik"
title: "TE – Terminal Equipment"
date: 2025-01-01
abbr: "TE"
fullName: "Terminal Equipment"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/te/"
summary: "Terminálové zařízení (TE) je koncové zařízení uživatele, například počítač nebo smartphone, které využívá služeb jednotky mobilního zakončení (MT) pro připojení k mobilní síti. Je funkčním ekvivalente"
---

TE je koncové zařízení uživatele, například počítač nebo smartphone, které využívá jednotku mobilního zakončení (Mobile Termination) pro připojení k mobilní síti a je zodpovědné za generování, zpracování a ukončení datového toku uživatele.

## Popis

Terminálové zařízení (TE) je základním konceptem v architekturách 3GPP představujícím koncový bod, který iniciuje nebo ukončuje informační toky. Je to uživatelské zařízení obsahující funkce pro komunikaci s partnerským uzlem. V kontextu mobilních sítí TE neobsahuje specifické funkce rádiového modemu pro přístup k celulární síti; ty jsou umístěny v samostatné funkční entitě zvané mobilní zakončení ([MT](/mobilnisite/slovnik/mt/)). TE se k MT připojuje prostřednictvím standardizovaného rozhraní, jako jsou ta definovaná 3GPP nebo jinými orgány, například [ETSI](/mobilnisite/slovnik/etsi/) nebo [ITU-T](/mobilnisite/slovnik/itu-t/). Toto oddělení umožňuje flexibilitu, díky které se různé typy TE (např. notebooky, IoT senzory, platební terminály) mohou připojit k síti prostřednictvím společného zařízení MT, jako je celulární dongle nebo smartphone fungující jako hotspot.

Architektonicky je TE součástí modelu Terminálové zařízení – Mobilní zakončení (TE-MT). TE je zodpovědné za aplikační vrstvy uživatele (vrstva 7 a výše v modelu [OSI](/mobilnisite/slovnik/osi/)) a zvládá úkoly jako prohlížení webu, e-mailové klienty nebo zpracování dat ze senzorů. S MT komunikuje pomocí funkce adaptace terminálu ([TA](/mobilnisite/slovnik/ta/)), která přizpůsobuje datové toky TE protokolům srozumitelným pro MT pro přenos přes rádiové rozhraní. MT naopak zpracovává všechny protokoly nižších vrstev specifické pro rádiovou přístupovou síť (RAN), včetně řízení rádiových zdrojů, správy mobility a zabezpečení na linkové vrstvě.

Role TE je definována v četných specifikacích 3GPP pokrývajících servisní aspekty, architekturu a protokoly. Specifikace například podrobně popisují, jak TE prostřednictvím MT navazuje datové spojení, jak se vyjednávají parametry kvality služby (QoS) a jak lze pomocí specifických AT příkazů (standardizovaných v 3GPP TS 27.007) ovládat MT z TE. Toto jasné funkční oddělení je klíčové pro certifikaci zařízení, interoperabilitu sítě a vývoj rozsáhlého ekosystému uživatelských zařízení, která mohou využívat vyvíjející se celulární technologie, aniž by každé TE potřebovalo integrovaný rádiový hardware.

## K čemu slouží

Koncept terminálového zařízení byl formalizován, aby vytvořil jasné architektonické oddělení mezi uživatelským aplikačním zařízením a síťově specifickým rádiovým komunikačním hardwarem. Toto oddělení řeší problém rozmanitosti zařízení a technologického vývoje. Bez tohoto modelu by každé koncové uživatelské zařízení muselo integrovat složitou a rychle se měnící technologii rádiového modemu, což by zvyšovalo náklady, velikost a spotřebu energie a ztěžovalo nezávislý upgrade rádiové technologie na aplikačním zařízení.

Historicky tento model vychází z konceptů datového terminálového zařízení ([DTE](/mobilnisite/slovnik/dte/)) a datového koncového zařízení okruhu ([DCE](/mobilnisite/slovnik/dce/)) v pevných datových komunikacích (např. modemy). V mobilním kontextu umožňuje modularitu. Jeden certifikovaný modul [MT](/mobilnisite/slovnik/mt/) (jako USB dongle nebo vestavěný čipset) může poskytovat síťový přístup pro širokou škálu TE. To bylo obzvláště důležité v počátcích mobilních dat (GPRS, UMTS), kdy byla integrace radií do notebooků nepraktická. Model zůstává relevantní pro IoT, kde se jednoduchý senzor (TE) může připojit přes nízkopříkonový celulární modul (MT). Standardizuje rozhraní a zajišťuje, že jakékoli kompatibilní TE může pracovat s jakýmkoli kompatibilním MT, čímž podporuje konkurenční a interoperabilní trh.

## Klíčové vlastnosti

- Představuje koncové aplikační zařízení uživatele (např. PC, senzor, videokamera).
- Odděleno od funkce mobilního zakončení (MT), která zvládá rádiový přístup.
- Komunikuje s MT prostřednictvím standardizovaného rozhraní (např. pomocí AT příkazů).
- Zodpovědné za protokoly vyšších vrstev a aplikační data uživatele.
- Umožňuje modulární návrh zařízení a nezávislý technologický vývoj.
- Základní pro architektonický model TE-MT ve specifikacích 3GPP.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.101** (Rel-19) — UMTS Architecture and Functional Separation
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [TE na 3GPP Explorer](https://3gpp-explorer.com/glossary/te/)
