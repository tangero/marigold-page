---
slug: "sls"
url: "/mobilnisite/slovnik/sls/"
type: "slovnik"
title: "SLS – Service Level Specification"
date: 2026-01-01
abbr: "SLS"
fullName: "Service Level Specification"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/sls/"
summary: "Formální technický popis očekávaného výkonu a charakteristik telekomunikační služby. Definuje měřitelné parametry, jako je latence, propustnost a dostupnost, což umožňuje poskytovatelům služeb garanto"
---

SLS (Service Level Specification) je formální technický popis očekávaného výkonu služby, který definuje měřitelné parametry, jako je latence a propustnost, aby umožnil záruky QoS a jeho monitorování.

## Popis

Service Level Specification (SLS) je základní koncept ve standardech 3GPP pro definování a správu kvality služby. Jedná se o strukturovaný dokument nebo datový model, který kvantitativně specifikuje výkonnostní atributy, které musí síťová služba poskytovat. SLS není jediný parametr, ale soubor cílů úrovně služby (SLO), které pokrývají různé dimenze, jako je propustnost, zpoždění paketů, variaci zpoždění paketů (jitter), míru ztráty paketů a dostupnost služby. Tyto parametry jsou definovány s konkrétními cílovými hodnotami, metodami měření a úrovněmi podrobností pro reportování.

Z architektonického hlediska SLS funguje jako smlouva mezi poskytovatelem služby a jejím spotřebitelem (což může být koncový uživatel, podnik nebo jiný síťový řez). Používají jej systémy pro správu a orchestraci sítě, jako jsou ty definované v rámci Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)) 3GPP, ke konfiguraci síťových prostředků. Když je požadována služba – například řez pro vylepšenou mobilní širokopásmovou síť (eMBB) nebo podnikové [VPN](/mobilnisite/slovnik/vpn/) – je přidružený SLS převeden na konkrétní pravidla řízení politiky a účtování ([PCC](/mobilnisite/slovnik/pcc/)), profily QoS a instrukce pro rezervaci prostředků pro Core Network a Radio Access Network (RAN).

Klíčové součásti SLS zahrnují rozsah (definující geografickou oblast, skupinu uživatelských zařízení nebo datovou síť), výkonnostní metriky s jejich garantovanými a maximálními hodnotami a podmínky pro reportování shody. Funguje v součinnosti se smlouvami o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)), kde SLA představuje komerční nebo právní dohodu a SLS poskytuje technický základ pro její vynucení. Automatizované systémy kontinuálně monitorují klíčové výkonnostní indikátory ([KPI](/mobilnisite/slovnik/kpi/)) vůči prahovým hodnotám SLS a spouštějí alarmy nebo nápravné akce, jako je škálování prostředků, pokud je zjištěno porušení. Jeho role je klíčová pro umožnění diferencovaných služeb, síťového řezání a zajištění toho, aby různé aplikace od komunikací s ultra-spolehlivou nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) až po hromadný IoT dostávaly potřebné výkonnostní záruky.

## K čemu slouží

SLS byl zaveden, aby řešil rostoucí složitost mobilních služeb a potřebu kvantifikovatelné kvality služby přesahující jednoduché doručování typu "best-effort". Před jeho formalizací byly záruky služeb často popisovány vágními, netechnickými termíny v rámci komerčních [SLA](/mobilnisite/slovnik/sla/), což ztěžovalo jejich technické vynucení. Vzestup IP Multimedia Subsystem (IMS) a později síťového řezání v 5G vytvořil naléhavou potřebu standardizovaného, strojově čitelného formátu pro popis očekávání služby.

K jeho vytvoření vedly požadavky podnikových zákazníků a nových vertikálních odvětví (jako je automobilový průmysl, výroba a zdravotnictví), která vyžadují přísné výkonnostní záruky. SLS řeší problém převodu vysokých obchodních požadavků (např. "řízení továrního robota vyžaduje latenci 10 ms") na přesné příkazy pro konfiguraci sítě. Poskytuje společný jazyk pro vyjednávání mezi systémy pro podporu podnikání ([BSS](/mobilnisite/slovnik/bss/)) a systémy pro podporu provozu (OSS), což umožňuje automatizované plnění služeb a jejich zajištění. Historicky jeho vývoj napříč četnými vydáními 3GPP odráží vývoj od jednoduchých hlasových a datových služeb ke komplexním, řezaným 5G sítím, kde je dynamické přidělování prostředků na základě přesných specifikací prvořadé.

## Klíčové vlastnosti

- Definuje kvantifikovatelné výkonnostní metriky (např. latence, propustnost, ztráta paketů)
- Poskytuje strojově čitelný formát pro automatizovanou orchestraci sítě
- Slouží jako technický základ pro komerční smlouvy o úrovni služeb (SLA)
- Umožňuje dynamické vynucování politik a účtování na základě kvality služby
- Klíčový pro vytváření a správu síťových řezů se specifickými charakteristikami
- Podporuje kontinuální monitorování a reportování pro zajištění služby

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TS 28.202** (Rel-19) — 5G Network Slice Management Charging
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 28.535** (Rel-19) — Closed Control Loop Assurance Management
- **TS 28.536** (Rel-19) — Management services for communication service assurance
- **TS 28.735** (Rel-19) — STN Interface NRM IRP Information Service
- **TS 28.805** (Rel-16) — Management of Communication Services in 5G
- **TR 28.907** (Rel-19) — Enhanced Management of Non-Public Networks
- **TS 32.742** (Rel-11) — STN NRM for Configuration Management
- **TS 38.744** (Rel-19) — AI/ML for NR Mobility Study
- **TR 38.830** (Rel-17) — NR Coverage Enhancements Study
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR

---

📖 **Anglický originál a plná specifikace:** [SLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sls/)
