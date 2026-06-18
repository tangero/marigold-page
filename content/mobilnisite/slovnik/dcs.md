---
slug: "dcs"
url: "/mobilnisite/slovnik/dcs/"
type: "slovnik"
title: "DCS – Distributed Control System"
date: 2026-01-01
abbr: "DCS"
fullName: "Distributed Control System"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dcs/"
summary: "Architektura řídicího systému pro telekomunikační sítě, kde jsou řídicí funkce distribuovány napříč více uzly namísto centralizace. Umožňuje škálovatelný, odolný a efektivní síťový provoz a poskytován"
---

DCS je architektura řídicího systému pro telekomunikační sítě, ve které jsou řídicí funkce distribuovány napříč více uzly, aby umožnila škálovatelný, odolný a efektivní provoz.

## Popis

Distribuovaný řídicí systém (DCS) ve standardech 3GPP označuje architekturu řízení a orchestrace, ve které je řídicí logika a schopnost rozhodování rozptýlena napříč různými síťovými prvky a řídicími doménami. Na rozdíl od tradičních centralizovaných systémů DCS funguje na principech lokalizace, autonomie a koordinace. Skládá se z federace řídicích entit, z nichž každá je zodpovědná za konkrétní doménu (např. instanci síťového řezu, geografickou oblast nebo sadu síťových funkcí). Tyto entity komunikují prostřednictvím standardizovaných rozhraní, aby dosáhly globálních síťových cílů, a zároveň si zachovaly lokální řídicí autonomii.

Architektonicky je DCS postaven kolem klíčových komponent: Distribuovaných řídicích funkcí (DMF), což jsou softwarové entity vestavěné v síťových funkcích nebo vyhrazených řídicích uzlech; koordinační vrstvy, často implementované pomocí služebních rozhraní nebo sběrnic zpráv, která umožňuje komunikaci a synchronizaci stavu mezi DMF; a rámce politik, který definuje pravidla a cíle pro distribuované rozhodování. Systém využívá konsenzuální algoritmy, událostmi řízené spouštěče a distribuované databáze k udržení konzistentního pohledu na stav a prostředky sítě bez spoléhání se na jediný bod řízení.

Při provozu DCS zpracovává úlohy, jako je dynamická alokace prostředků, správa poruch a orchestrace životního cyklu služeb, decentralizovaným způsobem. Například při škálování síťového řezu mohou DMF spojené s dotčenými segmenty RAN a core sítě autonomně vyjednávat a alokovat prostředky na základě lokálních politik a stavu v reálném čase, přičemž vyššímu orchestrátoru hlásí pouze agregované výsledky. Tím se snižuje latence, minimalizuje provoz na řídicí rovině a zvyšuje odolnost systému vůči výpadkům jednotlivých řídicích uzlů.

Jeho role v síti je klíčová pro podporu složitých, rozsáhlých nasazení, jako je 5G a další generace, kde požadavky na ultra-nízkou latenci, vysokou spolehlivost a masivní konektivitu zařízení činí čistě centralizované řízení nepraktickým. DCS umožňuje agilnější a rychleji reagující síťový provoz, usnadňuje implementaci pokročilých případů užití, jako jsou síťové řezy se zaručenou striktní izolací, a tvoří základ pro plně autonomní správu sítě, jak je koncipována v rámci samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)) a provozu bez zásahu člověka (zero-touch) podle 3GPP.

## K čemu slouží

DCS byl vytvořen, aby řešil omezení centralizovaných systémů správy sítě v kontextu rychle rostoucího rozsahu, složitosti a výkonnostních požadavků sítí. Rané mobilní sítě (2G/3G) se spoléhaly na centralizované operační podpůrné systémy ([OSS](/mobilnisite/slovnik/oss/)) a systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)), které se staly úzkými místy s rostoucím počtem síťových prvků a potřebou rychlejšího zřizování služeb a dynamičtější kontroly prostředků. Centralizované systémy trpěly jednotnými body selhání, omezeními škálovatelnosti a zvýšenou latencí pro řídicí operace, což bránilo nasazování služeb citlivých na latenci a vyžadujících vysokou dostupnost.

Motivace pro DCS zesílila s příchodem 5G a souvisejících paradigmat, jako jsou síťové řezy, edge computing a masivní IoT. Ty přinesly požadavky na distribuované zpracování, lokalizované rozhodování a striktní izolaci mezi logickými sítěmi. Centralizovaný řadič nemohl efektivně spravovat tisíce síťových řezů nebo činit rozhodnutí na úrovni milisekund pro edge aplikace. DCS poskytuje architektonickou odpověď distribucí řízení blíže k okraji sítě a zdrojům dat, což umožňuje reakce v reálném čase na lokální události (jako je náhlý nárůst provozu nebo výpadek spoje) bez čekání na příkazy od vzdálené centrální entity.

Dále DCS podporuje vývoj směrem k autonomním sítím vestavěním inteligence do síťové infrastruktury. Řeší problémy provozní efektivity a nákladů tím, že umožňuje automatizovanou, politikami řízenou správu na detailní úrovni, a snižuje tak potřebu neustálého lidského zásahu. Distribucí řízení také zvyšuje bezpečnost a robustnost, protože kompromitace nebo selhání jednoho řídicího uzlu neochromí řídicí schopnosti celé sítě.

## Klíčové vlastnosti

- Decentralizovaná řídicí logika napříč více síťovými doménami a funkcemi
- Autonomní rozhodování lokálních řídicích entit na základě politik
- Koordinační mechanismy pro synchronizaci globálních cílů mezi distribuovanými uzly
- Podpora řídicích akcí v reálném čase, řízených událostmi
- Vylepšená škálovatelnost a odolnost odstraněním úzkých míst centrálního řízení
- Rámec založený na politikách umožňující přizpůsobitelné a izolované řízení pro každý síťový řez nebo službu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.509** (Rel-19) — AUSF Service Based Interface Protocol
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TR 33.857** (Rel-17) — Enhanced Security for Non-Public Networks

---

📖 **Anglický originál a plná specifikace:** [DCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcs/)
