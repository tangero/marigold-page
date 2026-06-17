---
slug: "csa"
url: "/mobilnisite/slovnik/csa/"
type: "slovnik"
title: "CSA – Capability Set supported by the AAS BS"
date: 2025-01-01
abbr: "CSA"
fullName: "Capability Set supported by the AAS BS"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/csa/"
summary: "CSA definuje konkrétní sadu schopností podporovaných základnovou stanicí s aktivní anténní soustavou (AAS BS). Jde o standardizovaný rámec pro popis hardwarových a softwarových vlastností AAS BS, kter"
---

CSA je standardizovaný rámec definující konkrétní sadu hardwarových a softwarových schopností podporovaných základnovou stanicí s aktivní anténní soustavou (AAS BS).

## Popis

Capability Set podporovaný [AAS](/mobilnisite/slovnik/aas/) [BS](/mobilnisite/slovnik/bs/) (CSA) je formalizovaný, strukturovaný informační model definovaný ve specifikacích 3GPP. Slouží jako komplexní deskriptor pro funkční a výkonnostní charakteristiky vlastní základnové stanici s aktivní anténní soustavou (AAS BS). AAS BS integruje rádiový (RF) transceiver, výkonové zesilovače a anténní prvky do jediné integrované jednotky s digitálním řízením jednotlivých anténních prvků nebo sub-pole. CSA poskytuje podrobný rozbor podporovaných schopností napříč několika klíčovými doménami, včetně podporovaných kmitočtových pásem, počtu anténních prvků a transceiverových jednotek (TXRUs), podporovaných architektur beamformingu (např. plně digitální, hybridní), maximálního počtu současných paprsků a podporovaných [MIMO](/mobilnisite/slovnik/mimo/) vrstev a přenosových režimů. Tyto informace jsou typicky hlášeny AAS BS systému správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo RAN Intelligent Controlleru (RIC) při inicializaci nebo na vyžádání.

Architektonicky je CSA klíčovou součástí samo-deskripčního mechanismu AAS BS. Je definován pomocí datových modelů a parametrů, které lze komunikovat přes standardizovaná rozhraní, jako jsou ta mezi základnovou stanicí a její řídicí entitou. Specifikace podrobně popisuje parametry jako počet anténních portů, podporované geometrie anténního pole (např. 2D obdélníkové pole), schopnosti beamformingového kodexu a podporované funkce správy rádiových zdrojů (RRM) související se správou paprsků. To umožňuje síti získat přesné, na dodavateli nezávislé porozumění potenciálu rádiové jednotky, což je nezbytné pro úkoly jako plánování buněk, vyvažování zátěže a dynamické sdílení spektra.

V provozu CSA umožňuje pokročilé síťové funkce. Například když systém správy sítě obdrží CSA od nasazené AAS BS, může určit, zda základnová stanice podporuje funkce vyžadované pro konkrétní scénáře nasazení, jako je ultra-husté pokrytí ve městech s vysokorádovým Massive MIMO nebo pokrytí široké oblasti pomocí beamformingu. CSA informuje algoritmy pro výběr paprsku, koordinaci rušení a precoding pro Massive MIMO. Umožňuje RAN softwaru optimálně využívat schopnosti hardwaru, což zajišťuje, že přenosové strategie odpovídají fyzickým omezením a vlastnostem anténního systému. To je zásadní pro dosažení výkonnostních zisků slibovaných 5G NR, jako je zvýšená spektrální účinnost, vyšší kapacita a lepší pokrytí díky přesnému prostorovému filtrování.

Role CSA přesahuje pouhou správu inventáře. Je základním kamenem pro automatizaci a optimalizaci sítě v moderních architekturách Open RAN (O-RAN). V O-RAN může near-real-time RIC (Near-RT RIC) využívat informace CSA z více AAS BS k provádění inteligentních xApps pro správu rádiových zdrojů. Tyto aplikace mohou například orchestrovat koordinovaný beamforming napříč buňkami nebo dynamicky upravovat MIMO strategie na základě reálných požadavků na provoz a konkrétních schopností každého uzlu. CSA tedy funguje jako klíčový enabler pro softwarově definované, agilní a inteligentní rádiové sítě, poskytuje nezbytná metadata pro síťové funkce vyšších vrstev, aby mohly činit informovaná řídicí rozhodnutí.

## K čemu slouží

Vytvoření konceptu CSA bylo motivováno zavedením a rozšířením aktivních anténních soustav ([AAS](/mobilnisite/slovnik/aas/)) v mobilních sítích, zejména s nástupem 5G. Tradiční základnové stanice používaly pasivní antény s pevným vyzařovacím diagramem a jejich schopnosti bylo relativně jednoduché popsat. Avšak technologie AAS, která integruje aktivní komponenty a umožňuje digitální beamforming, přinesla širokou a komplexní škálu konfigurovatelných parametrů a výkonnostních vlastností. Bez standardizovaného způsobu, jak tyto schopnosti popsat, se správa a optimalizace sítě staly vysoce závislými na dodavateli a provozně náročnými.

Před CSA neexistovala jednotná metoda, jak by systém správy sítě mohl automaticky zjistit a porozumět podrobným možnostem beamformingu, [MIMO](/mobilnisite/slovnik/mimo/) a konfigurace antén AAS [BS](/mobilnisite/slovnik/bs/) od různých dodavatelů zařízení. Tento nedostatek standardizace bránil interoperabilitě mezi více dodavateli, komplikoval plánování a integraci sítě a činil automatizovanou optimalizaci sítě téměř nemožnou. Operátoři nasazující pokročilé funkce jako Massive MIMO potřebovali manuální, dodavatelsky proprietární dokumentaci k pochopení limitů a vlastností každé základnové stanice, což bylo neefektivní a náchylné k chybám.

Rámec CSA byl vyvinut k řešení těchto problémů tím, že poskytuje standardizovaný 'datový list' nebo profil schopností pro AAS BS. Umožňuje plug-and-play integraci zařízení AAS od různých dodavatelů do společného rámce pro správu a orchestraci. Definováním společného jazyka pro schopnosti AAS umožnilo 3GPP operátorům budovat heterogenní sítě, automatizovat úlohy konfigurace a optimalizace a plně využívat pokročilé rádiové funkce, které jsou ústřední pro výkon 5G. Řeší tak základní potřebu abstrakce a interoperability v čím dál více softwarově definovaném a virtualizovaném prostředí rádiového přístupového sítě.

## Klíčové vlastnosti

- Standardizovaný popis hardwarových schopností AAS BS (např. velikost anténního pole, počet TXRU)
- Definice podporovaných architektur beamformingu (digitální, hybridní analogově-digitální)
- Specifikace maximálního počtu souběžných paprsků a beamformingových kodexů
- Výčet podporovaných kmitočtových pásem a kombinací agregace nosných
- Popis MIMO schopností včetně maximálního počtu vrstev a přenosových režimů
- Podpora pro hlášení schopností systémům správy a orchestrace sítě

## Související pojmy

- [AAS – Active Antenna System](/mobilnisite/slovnik/aas/)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 37.114** (Rel-19) — EMC for Active Antenna System Base Stations

---

📖 **Anglický originál a plná specifikace:** [CSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/csa/)
