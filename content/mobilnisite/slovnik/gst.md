---
slug: "gst"
url: "/mobilnisite/slovnik/gst/"
type: "slovnik"
title: "GST – Generic Network Slice Template"
date: 2026-01-01
abbr: "GST"
fullName: "Generic Network Slice Template"
category: "Network Slicing"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gst/"
summary: "Standardizovaný datový model definující charakteristiky a požadavky síťového řezu. Poskytuje společný jazyk pro popis schopností, výkonu a smluv o úrovni služeb (SLA) řezu a umožňuje tak automatizovan"
---

GST je standardizovaný datový model, který definuje charakteristiky a požadavky síťového řezu (network slice) za účelem umožnění automatizované správy životního cyklu nezávislé na dodavateli.

## Popis

Generic Network Slice Template (GST) je klíčový datový model v rámci standardů 3GPP, speciálně navržený pro správu a orchestraci síťových řezů. Slouží jako standardizovaná, strojově čitelná šablona, která popisuje kompletní sadu atributů, požadavků a omezení instance síťového řezu ([NSI](/mobilnisite/slovnik/nsi/)). GST je definován pomocí datového modelovacího jazyka YANG, což zajišťuje jeho strukturovanost, hierarchičnost a vhodnost pro automatizované zpracování systémy řízení, jako je Communication Service Management Function (CSMF), Network Slice Management Function ([NSMF](/mobilnisite/slovnik/nsmf/)) a Network Slice Subnet Management Function (NSSMF). Jeho primární rolí je fungovat jako informační objekt, který je předáván mezi těmito řídicími funkcemi během procesů zřizování, modifikace a zajištění (assurance) řezu.

Z architektonického hlediska je GST klíčovou součástí rámce správy síťového řezování 3GPP, detailně popsaného v technických specifikacích jako TS 28.531 a TS 28.541. Abstrahuje komplexní, vícedoménovou povahu řezu do podoby spravovatelné šablony. Šablona zahrnuje několik klíčových oblastí: služební profil (definující zamýšlený typ služby řezu, např. eMBB, [URLLC](/mobilnisite/slovnik/urllc/), MIoT), požadavky na podsíť síťového řezu (podrobně specifikující potřebné zdroje a výkon napříč doménami RAN, Transport a Core Network) a požadavky na výkon a politiky řezu (včetně latence, spolehlivosti, propustnosti a úrovní izolace). Tento strukturovaný přístup umožňuje systému řízení rozložit požadavek na službu vysoké úrovně na konkrétní, akční konfigurační příkazy pro podkladové síťové funkce a infrastrukturu.

V provozu GST umožňuje uzavřenou smyčku řízení založeného na záměru (intent-based). Poskytovatel komunikačních služeb ([CSP](/mobilnisite/slovnik/csp/)) nebo podnikový zákazník odešle požadavek na službu, často prostřednictvím portálu nebo northbound [API](/mobilnisite/slovnik/api/), který je převeden na instanci GST. Tuto GST poté spotřebovává NSMF, který interpretuje požadavky a orchestruje potřebné zdroje napříč různými administrativními a technologickými doménami generováním doménově specifických podšablon pro NSSMF. GST zajišťuje konzistenci a předchází nesprávné interpretaci tím, že poskytuje jediný zdroj pravdy o zamýšleném chování řezu. Je nedílnou součástí pro dosažení slibovaných výhod síťového řezování: přizpůsobených logických sítí na sdílené fyzické infrastruktuře, z nichž každá má garantovaný výkon a izolaci.

## K čemu slouží

GST byl zaveden k řešení kritické výzvy v praktickém nasazení síťového řezování: nedostatku standardizované, interoperabilní metody pro popis požadavků na řez. Před jeho definicí mohl každý dodavatel nebo operátor používat proprietární šablony nebo manuální procesy pro definici řezů, což vedlo k fragmentaci, vysokým nákladům na integraci a neschopnosti automatizovat správu životního cyklu v prostředí s více dodavateli. Vytvoření GST bylo motivováno vizí 5G podporovat rozmanité vertikální odvětví (jako automobilový průmysl, výroba a zdravotnictví) s velmi odlišnými požadavky na služby. Tato odvětví potřebovala jasný a jednoznačný způsob, jak komunikovat své síťové potřeby mobilnímu operátorovi.

Historicky byly síťové služby relativně monolitické a vytváření služeb bylo pomalým, manuálním procesem vyžadujícím významný lidský zásah. Posun k softwarizaci a cloud-nativním sítím v 5G vyžadoval agilnější, softwarově řízený přístup. GST jej poskytuje tím, že funguje jako společná 'smlouva' nebo 'recept', který odděluje záměr služby od implementace specifické pro dodavatele. Řeší omezení předchozích ad-hoc přístupů tím, že umožňuje automatizovaný překlad požadavků na službu na obchodní úrovni do technických síťových konfigurací. To je zásadní pro škálování síťového řezování za účelem efektivní a spolehlivé podpory masivního množství různorodých řezů.

## Klíčové vlastnosti

- Standardizovaný YANG datový model pro komunikaci mezi stroji (M2M)
- Komplexní definice služebních profilů řezu (např. eMBB, URLLC, MIoT)
- Specifikace požadavků na výkon (latence, spolehlivost, propustnost)
- Definice politik izolace a sdílení zdrojů
- Podpora pro vícedoménovou dekompozici (RAN, Transport, Core)
- Umožňuje uzavřenou smyčku automatizace pro správu životního cyklu řezu

## Související pojmy

- [NSMF – Network Slice Management Function](/mobilnisite/slovnik/nsmf/)

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.880** (Rel-19) — Study on 5G Energy Efficiency & Saving
- **TR 32.847** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [GST na 3GPP Explorer](https://3gpp-explorer.com/glossary/gst/)
