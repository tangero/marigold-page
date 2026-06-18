---
slug: "qos"
url: "/mobilnisite/slovnik/qos/"
type: "slovnik"
title: "QoS – Quality of Service"
date: 2026-01-01
abbr: "QoS"
fullName: "Quality of Service"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/qos/"
summary: "Quality of Service (QoS, kvalita služby) je soubor technologií a mechanismů řídících síťový provoz za účelem zaručení výkonnostních úrovní pro konkrétní datové toky. Zajišťuje, aby aplikace dostávaly"
---

QoS je soubor technologií a mechanismů, které řídí síťový provoz, aby zaručily úrovně výkonu, jako je šířka pásma a latence, pro konkrétní datové toky ve sdílených prostředcích.

## Popis

Quality of Service (QoS) v systémech 3GPP je komplexní rámec pro rozlišování a stanovení priorit datového provozu, aby byly splněny specifické výkonnostní požadavky různých služeb. Funguje tak, že třídí pakety do samostatných QoS toků (QoS Flows), z nichž každý je spojen s QoS profilem obsahujícím sadu parametrů QoS. Základními parametry jsou 5G QoS identifikátor ([5QI](/mobilnisite/slovnik/5qi/)), což je skalární hodnota odkazující na standardizované charakteristiky (jako priorita, rozpočet zpoždění paketu, míra chybovosti paketů), a volitelně priorita přidělení a udržení ([ARP](/mobilnisite/slovnik/arp/)), garantovaný bitový tok toku (GFBR), maximální bitový tok toku ([MFBR](/mobilnisite/slovnik/mfbr/)) a vyhodnocovací okno. Tyto parametry definují očekávané zacházení s pakety náležejícími k danému toku.

Z architektonického hlediska je QoS vynucována koncově-koncově napříč systémem 5G a zahrnuje uživatelské zařízení (UE), rádiovou přístupovou síť (RAN) a 5G jádro sítě (5GC). Funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) je odpovědná za zřizování, modifikaci a uvolňování QoS toků na základě požadavků na relaci od aplikační funkce ([AF](/mobilnisite/slovnik/af/)) nebo profilů účastníka od jednotné správy dat ([UDM](/mobilnisite/slovnik/udm/)). SMF odvozuje pravidla QoS a zasílá je do UE a RAN přes funkci správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a gNB. V RAN jsou tato pravidla mapována na datové rádiové přenosy ([DRB](/mobilnisite/slovnik/drb/)) pro přenos vzduchem, kde plánovací algoritmy stanovují prioritu paketů podle jejich 5QI.

Jak to funguje, zahrnuje vícestupňový proces mapování. Na úrovni PDU relace jsou toky služebních dat (SDF) identifikovány pomocí filtrů paketů a mapovány na QoS tok. Každý QoS tok je v rámci PDU relace jednoznačně identifikován identifikátorem QFI (QoS Flow Identifier). RAN mapuje jeden nebo více QoS toků s podobnými charakteristikami na jeden DRB, aby optimalizovala využití rádiových prostředků. Plánovač paketů v gNB používá parametry QoS (zejména prioritu a rozpočet zpoždění) k rozhodování na úrovni milisekund o tom, která data kterého UE se mají přenést na kterých blocích fyzických prostředků, což zajišťuje, že toky citlivé na latenci (jako VoIP) jsou obslouženy dříve než stahování na pozadí. Tato hierarchická a podrobná kontrola je tím, co umožňuje jedné fyzické síti současně podporovat kritický IoT, ultra-HD video a best-effort prohlížení webu.

## K čemu slouží

Technologie QoS byla vytvořena, aby řešila zásadní výzvu podpory více služeb s výrazně odlišnými výkonnostními požadavky přes jedinou sdílenou infrastrukturu paketově přepínané sítě. Rané mobilní sítě byly přepojovány okruhy a vyhrazeny pro hlas, což přirozeně poskytovalo garantovanou kvalitu. S přechodem na plně IP sítě (GPRS, UMTS) se veškerý provoz stal datovými pakety, což hrozilo, že provoz citlivý na latenci, jako je hlas nebo video, bude degradován přenosy hromadných dat. QoS poskytuje potřebné nástroje pro opětovné zavedení diferenciace a záruk v paketovém světě.

Vývoj od 3G přes 4G k 5G přinesl neustálé zdokonalování mechanismů QoS pro podporu stále širšího spektra služeb. V 3G/UMTS (verze 99) QoS zavedla koncept přenosových služeb s třídami provozu (konverzační, streamovací, interaktivní, na pozadí). 4G/LTE to zjednodušila pomocí QCI (QoS Class Identifier). 5G tento rámec významně rozšířilo flexibilnějším, službami řízeným přístupem. Řešilo omezení předchozích systémů tím, že umožnilo podrobnější QoS na úrovni toků (namísto na úrovni přenosů), umožnilo síťové segmenty (network slicing) a poskytlo explicitní podporu pro nové požadavky služeb 5G, jako je ultra-spolehlivá komunikace s nízkou latencí (URLLC) a hromadná komunikace mezi stroji (mMTC).

Bez QoS by sítě fungovaly na jednoduchém best-effort principu, kde jsou všechny pakety zpracovávány stejně. To je nedostatečné pro moderní digitální ekonomiky, které se spoléhají na spolupráci v reálném čase, průmyslovou automatizaci, telemedicínu a imerzivní zábavu. QoS to řeší tím, že umožňuje síťovým operátorům vytvářet úrovně služeb, implementovat správu provozu a plnit smlouvy o úrovni služeb (SLA). Je to technologický základ, který umožňuje komerční příslib 5G – podporu jednotné sítě pro vše od senzorů po autonomní vozidla.

## Klíčové vlastnosti

- Podrobný model QoS toku identifikovaný QFI, oddělený od přenosového spoje (DRB)
- Standardizované hodnoty 5QI pro běžné typy služeb (např. VoIP, streamování videa, zprávy V2X)
- Dynamická kontrola QoS prostřednictvím PCF a SMF na základě požadavků aplikací nebo stavu sítě
- Koncově-koncové vynucování od UE/jádra k RAN s explicitním označováním paketů (DSCP, QFI)
- Podpora reflexivní QoS, kdy si UE může odvodit pravidla QoS pro sestupný směr z pozorovaného provozu
- Integrace se síťovými segmenty (network slicing) pro zajištění izolovaného výkonu QoS na segment

## Definující specifikace

- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TR 37.911** (Rel-19) — 3GPP 5G NTN Self-Evaluation Report

---

📖 **Anglický originál a plná specifikace:** [QoS na 3GPP Explorer](https://3gpp-explorer.com/glossary/qos/)
