---
slug: "capc"
url: "/mobilnisite/slovnik/capc/"
type: "slovnik"
title: "CAPC – Channel Access Priority Class"
date: 2025-01-01
abbr: "CAPC"
fullName: "Channel Access Priority Class"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/capc/"
summary: "CAPC je standardizovaný mechanismus priority pro NR-U (New Radio v neregulovaném spektru), který určuje, jak se zařízení ucházejí o přístup na kanál. Definuje čtyři třídy priority s různými parametry"
---

CAPC je standardizovaný mechanismus priority pro NR-U, který definuje čtyři třídy s různými parametry soutěžení o přístup pro určení, jak se zařízení ucházejí o přístup na kanál v neregulovaném spektru.

## Popis

Channel Access Priority Class (CAPC) je základní mechanismus v 5G [NR-U](/mobilnisite/slovnik/nr-u/) (New Radio v neregulovaném spektru), který řídí, jak se User Equipment (UE) a gNB ucházejí o přístup do neregulovaných kmitočtových pásem. Systém funguje v rámci rámce Listen-Before-Talk ([LBT](/mobilnisite/slovnik/lbt/)), který vyžadují regulatorní požadavky pro používání neregulovaného spektra. CAPC definuje čtyři odlišné třídy priority (1-4, kde 1 je nejvyšší priorita), které se mapují na různé parametry soutěžení o přístup, konkrétně velikost Contention Window ([CW](/mobilnisite/slovnik/cw/)) a maximální Channel Occupancy Time ([COT](/mobilnisite/slovnik/cot/)). Každá třída má předdefinované hodnoty pro minimální a maximální velikost CW, které určují náhodnou dobu backoff před pokusy o vysílání.

Architektura integruje CAPC na více protokolových vrstvách. Na fyzické vrstvě (specifikováno v 38.212) CAPC ovlivňuje parametry procedury LBT. Na [MAC](/mobilnisite/slovnik/mac/) vrstvě (37.213) určuje konkrétní chování při soutěžení o přístup během pokusů o přístup na kanál. Vrstva [RRC](/mobilnisite/slovnik/rrc/) (38.331) zpracovává konfiguraci a signalizaci parametrů CAPC mezi gNB a UE. Systém funguje tak, že mapuje různé QoS Flow Identifiers (QFIs) nebo hodnoty [5QI](/mobilnisite/slovnik/5qi/) na konkrétní hodnoty CAPC, čímž zajišťuje, že provoz s vysokou prioritou, jako je URLLC, dostane příznivější parametry soutěžení než best-effort provoz.

Klíčové komponenty zahrnují samotnou proceduru LBT, která se skládá z fází Clear Channel Assessment ([CCA](/mobilnisite/slovnik/cca/)) a Extended CCA (ECCA). Během ECCA zařízení provádí náhodný odpočet backoff na základě velikosti CW spojené s jeho CAPC. Vyšší priority CAPC mají menší minimální a maximální velikosti CW, což vede k kratším průměrným dobám backoff. Maximální COT se také liší podle CAPC, přičemž vyšší priority obvykle získávají delší přenosové příležitosti, jakmile je přístup na kanál získán. Tato hierarchická struktura zajišťuje, že aplikace citlivé na čas mohou získat přístup na kanál rychleji, a přitom zachovávají spravedlnost vůči jiným systémům.

Role CAPC v síti přesahuje jednoduchou priorizaci. Umožňuje dynamické sdílení spektra mezi 5G NR-U a jinými technologiemi, jako je Wi-Fi, implementací standardizovaného schématu priority, které je v souladu s podobnými mechanismy v IEEE 802.11. gNB konfiguruje mapování CAPC na základě síťových politik a charakteristik provozu, což operátorům umožňuje optimalizovat využití spektra při splnění různých požadavků QoS. Tento mechanismus je zvláště klíčový pro podporu síťového řezání (network slicing) v neregulovaném spektru, kde různé řezy mohou vyžadovat různé priority přístupu na kanál k naplnění svých smluv o úrovni služeb.

## K čemu slouží

CAPC byl vytvořen, aby řešil základní výzvu provozování 5G NR v neregulovaných kmitočtových pásmech (především 5 GHz a 6 GHz), kde musí více rádiových technologií spravedlivě koexistovat. Před NR-U buněčné systémy fungovaly výhradně v regulovaném spektru se zaručeným přístupem, ale poptávka po dodatečné šířce pásma vedla 3GPP k vývoji specifikací pro neregulovaný provoz. Hlavní problém, který CAPC řeší, je jak implementovat efektivní diferenciaci QoS v prostředí založeném na soutěžení o přístup při dodržování regulatorních požadavků na spravedlivé sdílení spektra.

Historický kontext ukazuje, že předchozí řešení pro neregulované spektrum založená na LTE (LAA, eLAA) měla jednodušší mechanismy priority, které nebyly optimalizovány pro rozmanité požadavky služeb 5G. Mezi omezení patřila nedostatečná granularita pro současnou podporu URLLC, eMBB a mMTC ve sdíleném spektru. CAPC poskytuje sofistikovanější rámec, který je v souladu se služební architekturou 5G a umožňuje lepší integraci s rámcem 5QI (5G QoS Identifier). To operátorům umožňuje udržovat konzistentní politiky QoS napříč regulovanými i neregulovanými spektrovými komponentami jejich sítí.

Motivace pro vytvoření CAPC pramenila z potřeby podporovat pokročilé služby 5G ve scénářích sdílení spektra bez kompromisů v oblasti výkonu nebo regulatorní shody. Definováním standardizovaných tříd priority s konkrétními parametry soutěžení o přístup CAPC zajišťuje předvídatelné chování napříč různými implementacemi výrobců a umožňuje globální interoperabilitu. To bylo zvláště důležité pro umožnění funkcí jako duální konektivita s NR-U jako sekundární buňkou, kde je konzistentní chování přístupu na kanál klíčové pro udržení bezproblémového uživatelského zážitku a splnění požadavků na latenci pro kritické aplikace.

## Klíčové vlastnosti

- Čtyři standardizované třídy priority (1-4), přičemž třída 1 má nejvyšší prioritu
- Mapování mezi hodnotami 5QI/QFI a CAPC pro konzistentní zpracování QoS
- Třídě specifické parametry Contention Window (CW) pro náhodný backoff
- Různá maximální Channel Occupancy Time (COT) pro každou třídu priority
- Integrace s regulatorními požadavky Listen-Before-Talk (LBT)
- Podpora procedur přístupu na kanál pro downlink i uplink

## Související pojmy

- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 37.213** (Rel-19) — Shared Spectrum Physical Layer Procedures
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz

---

📖 **Anglický originál a plná specifikace:** [CAPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/capc/)
