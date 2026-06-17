---
slug: "mef"
url: "/mobilnisite/slovnik/mef/"
type: "slovnik"
title: "MEF – Maintenance Entity Function"
date: 2026-01-01
abbr: "MEF"
fullName: "Maintenance Entity Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mef/"
summary: "Funkční komponenta v systémech pro provoz, správu a údržbu (OAM), která zahajuje a ukončuje údržbové operace. Vytváří a spravuje údržbové entity (ME) pro monitorování konektivity mezi body v přenosové"
---

MEF je funkční komponenta v systémech OAM, která zahajuje a ukončuje údržbové operace vytvářením a správou údržbových entit (Maintenance Entities) pro monitorování konektivity za účelem detekce poruch a monitorování výkonu v přenosových sítích.

## Popis

Funkce údržbové entity (Maintenance Entity Function, MEF) je klíčový koncept v oblasti provozu, správy a údržby (OAM) sítí, zejména v kontextu přenosových sítí a správy poruch konektivity. Definovaná ve standardech jako [ITU-T](/mobilnisite/slovnik/itu-t/) Y.1731 a [IEEE](/mobilnisite/slovnik/ieee/) 802.1ag a odkazovaná v 3GPP pro aspekty řízení, je MEF funkční entita nacházející se na okraji údržbové domény. Jejím hlavním úkolem je zahajovat a ukončovat OAM protokoly za účelem monitorování a správy údržbové entity (Maintenance Entity, [ME](/mobilnisite/slovnik/me/)). Údržbová entita je logická reprezentace spojení nebo cesty mezi dvěma body zájmu (údržbovými body, Maintenance Points, MPs), která má být monitorována. MEF generuje OAM rámce (jako jsou zprávy kontinuity, zpětné smyčky nebo trasování spojení) a zpracovává odpovědi pro vyhodnocení stavu a výkonu ME.

Architektonicky je MEF asociována s údržbovými body (MPs), což jsou určené body v síti, kde probíhají OAM akce. Existují dva klíčové typy MPs: koncové údržbové body (Maintenance End Points, MEPs) a mezilehlé údržbové body (Maintenance Intermediate Points, MIPs). MEF je umístěna společně s [MEP](/mobilnisite/slovnik/mep/). MEP je aktivní OAM entita, která zahajuje a ukončuje OAM rámce pro konkrétní údržbovou doménu a údržbové sdružení. MEF uvnitř MEP je zodpovědná za logiku protokolu: vytváří OAM paket, vkládá správný identifikátor údržbového sdružení, vysílá jej k partnerskému MEP a analyzuje případné vrácené pakety. Například v Ethernet OAM periodicky vysílá MEF v MEP zprávy kontinuity (CCMs). Pokud přestanou přicházet [CCM](/mobilnisite/slovnik/ccm/) od partnerského MEP, může lokální MEF detekovat ztrátu kontinuity a spustit poplach poruchy.

Činnost MEF je hierarchická a založená na doménách. Sítě jsou rozděleny na údržbové domény (jako operátorská, poskytovatelská nebo zákaznická doména), každá s vlastní úrovní viditelnosti. MEF funguje v rámci konkrétní úrovně domény. Zpracovává pouze OAM rámce označené pro její doménu, ignoruje ty pro vyšší nebo nižší domény. To umožňuje vrstvenou správu poruch. MEF používá různé OAM nástroje: kontrolu kontinuity pro detekci poruch, zpětnou smyčku pro ověření konektivity a trasování spojení pro objevování cesty. V kontextech 3GPP, jako je správa backhaul sítí (např. NG-RAN transport) nebo síťových řezů, jsou principy MEF a MEPs aplikovány pro zajištění spolehlivosti konektivity mezi síťovými funkcemi. MEF je tedy základním stavebním kamenem pro dosažení dostupnosti služeb na úrovni operátora a monitorování výkonu v paketových přenosových sítích, které tvoří základ mobilní telekomunikace.

## K čemu slouží

Funkce údržbové entity (MEF) byla koncipována, aby řešila výzvu proaktivní správy poruch a monitorování výkonu v paketově přepínaných sítích, které nahradily tradiční sítě s přepojováním okruhů s menší inherentní pozorovatelností. V TDM/SDH sítích byla konektivita fyzicky ověřitelná, ale v Ethernet a IP sítích je 'spojení' logické, což ztěžuje izolaci poruch. MEF poskytuje standardizovaný, aktivní monitorovací mechanismus pro vytváření virtuálních 'údržbových entit', které emulují cestu služby, což umožňuje operátorům ověřit její integritu bez spoléhání se pouze na stížnosti zákazníků nebo alarmy nižších vrstev.

Historicky provozovatelé sítí postrádali standardizované nástroje pro zajištění služeb od konce ke konci v nově vznikajících službách Carrier Ethernet a IP/[MPLS](/mobilnisite/slovnik/mpls/). Proprietární nástroje podobné ping byly nedostatečné pro více-dodavatelská, více-doménová prostředí. Vývoj OAM standardů jako [IEEE](/mobilnisite/slovnik/ieee/) 802.1ag (správa poruch konektivity) a [ITU-T](/mobilnisite/slovnik/itu-t/) Y.1731 (OAM funkce pro Ethernet) zavedl architektonický model údržbových entit, koncových údržbových bodů a přidružené funkce údržbové entity. MEF je aktivní inteligence v tomto modelu, umožňující automatizované, kontinuální monitorování cest služeb. Tím byla vyřešena pomalá detekce a izolace poruch v komplexních, vrstvených servisních sítích.

V rámci ekosystému 3GPP, jak se mobilní sítě vyvíjely k použití plně IP transportu (např. pro rozhraní S1, X2, N2, N3), se potřeba robustního transportního OAM stala klíčovou pro plnění smluv o úrovni služeb (SLA) pro hlasové a datové služby. Koncept MEF, prostřednictvím jeho začlenění do specifikací řízení, umožňuje operátorům mobilních sítí monitorovat stav přenosových spojů mezi prvky rádiového přístupu a jádra sítě. To je obzvláště důležité pro síťové řezy v 5G, kde každý řez může mít specifické požadavky na konektivitu. MEF umožňuje vytváření údržbových entit odpovídajících segmentům transportu specifickým pro řez, což umožňuje nezávislé monitorování a správu poruch každého logického řezu, a tím řeší výzvu udržení izolace a výkonnostních záruk ve sdílené fyzické infrastruktuře.

## Klíčové vlastnosti

- Zahajuje a ukončuje rámce OAM protokolu (např. CCM, LBM, LTM)
- Nachází se v koncovém údržbovém bodě (MEP) v rámci údržbové domény
- Vytváří a spravuje životní cyklus údržbových entit (ME)
- Provádí kontrolu kontinuity pro detekci poruch ztráty konektivity
- Podporuje hierarchické údržbové domény pro vrstvenou správu poruch
- Umožňuje metriky monitorování výkonu, jako je zpoždění rámců a měření ztrát

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals

---

📖 **Anglický originál a plná specifikace:** [MEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mef/)
