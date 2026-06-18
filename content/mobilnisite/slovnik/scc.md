---
slug: "scc"
url: "/mobilnisite/slovnik/scc/"
type: "slovnik"
title: "SCC – Service Centralization and Continuity Application Server"
date: 2026-01-01
abbr: "SCC"
fullName: "Service Centralization and Continuity Application Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/scc/"
summary: "SCC AS je aplikační server v jádru sítě, který umožňuje kontinuitu a centralizaci služeb pro služby IMS, jako jsou hlasové a videohovory, při předávání spojení mezi přístupovými sítěmi s přepojováním"
---

SCC je aplikační server IMS, který umožňuje kontinuitu a centralizaci služeb pro multimediální hovory při předávání spojení mezi sítěmi s přepojováním okruhů a sítěmi s přepojováním paketů, aby zajistil bezproblémový uživatelský zážitek.

## Popis

Service Centralization and Continuity Application Server (SCC [AS](/mobilnisite/slovnik/as/)) je klíčová funkční entita v architektuře IP Multimedia Subsystem (IMS), definovaná 3GPP pro správu kontinuity a centralizace služeb pro multimediální relace. Funguje jako aplikační server, který ukotvuje relace IMS, zejména ty zahrnující hlasovou nebo video komunikaci, aby usnadnil bezproblémové předávání spojení mezi různými přístupovými technologiemi, například přechod hlasového hovoru z LTE (přepojování paketů) na GSM nebo UMTS (přepojování okruhů). SCC AS toho dosahuje implementací procedur IMS Service Continuity, které zahrnují renegociaci relace a aktualizaci mediální cesty, aby se udržely aktivní relace bez přerušení. Architektonicky komunikuje s dalšími uzly IMS, jako je Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) pro řízení relace a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro data účastníka, čímž zajišťuje, že může uplatnit příslušnou servisní logiku na základě uživatelských profilů a síťových podmínek.

Při provozu SCC AS využívá mechanismy jako Single Radio Voice Call Continuity ([SRVCC](/mobilnisite/slovnik/srvcc/)) a enhanced SRVCC (eSRVCC) pro zvládnutí událostí mobility. Když se UE přesune z oblasti pokrytí LTE s podporou VoLTE do starší sítě 2G/3G, SCC AS koordinuje s Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a [MSC](/mobilnisite/slovnik/msc/) Server přenos ukotvení relace a aktualizaci mediální cesty, čímž minimalizuje narušení služby. Spravuje Access Transfer Control Function ([ATCF](/mobilnisite/slovnik/atcf/)) a Access Transfer Gateway ([ATGW](/mobilnisite/slovnik/atgw/)) ve scénářích eSRVCC, které lokalizují mediální ukotvení za účelem snížení latence při předávání spojení. SCC AS také podporuje funkce během hovoru, jako je přidávání nebo odebírání mediálních komponent během relace, prostřednictvím protokolů pro řízení relace IMS, jako je SIP.

Klíčové komponenty v SCC AS zahrnují logiku pro ukotvení relace, správu kontinuity a spolupráci se sítěmi s přepojováním okruhů prostřednictvím frameworku IMS Centralized Services (ICS). Jeho role přesahuje rámec předávání spojení a zahrnuje centralizaci služeb, kdy slouží jako centralizovaný bod pro uplatňování servisní logiky, což zajišťuje konzistentní uživatelské zážitky napříč více zařízeními a typy přístupu. To je zvláště důležité pro umožnění funkcí jako přesměrování hovoru, současné zvonění a multimediální telefonie. Oddělením provádění služeb od přístupové technologie SCC AS zjednodušuje vývoj sítě a podporuje konvergenci pevných a mobilních služeb.

## K čemu slouží

SCC AS byl představen ve 3GPP Release 8, aby řešil výzvu udržení kontinuity služeb pro služby IMS, jak se sítě vyvíjely směrem k plně IP architekturám, jako je LTE. Před jeho vývojem byly hlasové služby převážně s přepojováním okruhů a předávání spojení mezi doménami s přepojováním paketů a okruhů nebylo standardizováno, což vedlo k přerušeným hovorům při událostech mobility. SCC AS to řeší tím, že poskytuje standardizovaný mechanismus pro ukotvení relací IMS, umožňuje bezproblémové přechody a zajišťuje, že uživatelé nepociťují přerušení při pohybu mezi LTE a staršími sítěmi.

Jeho vytvoření bylo motivováno posunem průmyslu k VoLTE a potřebou podporovat pokročité komunikační služby při využití stávající infrastruktury 2G/3G pro pokrytí. Centralizací servisní logiky SCC AS také snižuje složitost sítě, což operátorům umožňuje nasazovat nové funkce jednotně napříč různými přístupovými technologiemi. Tím řeší omezení dřívějších přístupů, kde byla kontinuita služeb řešena fragmentovaně, často vyžadující proprietární řešení, která bránila interoperabilitě a škálovatelnosti.

## Klíčové vlastnosti

- Ukotvuje relace IMS pro kontinuitu hlasových a video hovorů
- Podporuje SRVCC a eSRVCC pro předávání spojení mezi LTE a sítěmi s přepojováním okruhů
- Integruje se s prvky jádra IMS, jako jsou S-CSCF a HSS
- Spravuje mediální ukotvení prostřednictvím ATCF a ATGW v eSRVCC
- Umožňuje centralizaci služeb pro konzistentní provádění funkcí
- Umožňuje úpravy služeb během hovoru pomocí SIP

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [ATCF – Access Transfer Control Function](/mobilnisite/slovnik/atcf/)

## Definující specifikace

- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.294** (Rel-19) — IMS Centralized Services (ICS) I1 Interface Protocol
- **TS 24.337** (Rel-19) — IMS Inter-UE Transfer Protocol Specification
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [SCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/scc/)
