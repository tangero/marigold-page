---
slug: "nsmf"
url: "/mobilnisite/slovnik/nsmf/"
type: "slovnik"
title: "NSMF – Network Slice Management Function"
date: 2026-01-01
abbr: "NSMF"
fullName: "Network Slice Management Function"
category: "Network Slicing"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nsmf/"
summary: "Funkce správy síťového řezu (NSMF) je hlavní řídicí entita zodpovědná za správu a orchestraci koncového síťového řezu (end-to-end network slice). Převádí požadavky služby na požadavky řezy a koordinuj"
---

NSMF je hlavní řídicí entita zodpovědná za orchestraci koncové síťové řezy (end-to-end network slice), která převádí požadavky služby na požadavky řezy a koordinuje jeho životní cyklus napříč doménami.

## Popis

Funkce správy síťového řezu (NSMF) je klíčový funkční blok v rámci systému správy 3GPP, definovaný v několika specifikacích včetně TS 23.435, TS 28.530 a TS 28.531. Nachází se v řídicí rovině (management plane) a je zodpovědná za správu životního cyklu kompletního, koncového síťového řezu (end-to-end network slice). Koncepčně NSMF funguje jako 'orchestrátor' pro konkrétní instanci síťového řezu a zajišťuje jeho vytvoření, modifikaci, monitorování a ukončení podle jeho služebních požadavků.

Operačně NSMF přijímá požadavek na službu síťového řezu, typicky od funkce správy komunikační služby (CSMF) nebo od operátora. Tento požadavek obsahuje služební požadavky (např. latenci, šířku pásma, hustotu zařízení). Prvním úkolem NSMF je převést tyto služební požadavky na podrobné požadavky síťového řezu. Poté rozloží koncový řez na spravovatelné dílčí síťové části, známé jako podsítě síťového řezu ([NSS](/mobilnisite/slovnik/nss/)), které odpovídají konkrétním technologickým doménám, jako je RAN, Core nebo přenosová síť.

Pro každou NSS NSMF komunikuje s odpovídající funkcí správy podsítě síťového řezu (NSSMF). NSMF deleguje správu zdrojů v rámci konkrétní domény (např. zřizování funkcí Core Network) na příslušnou NSSMF. NSMF agreguje odpovědi a stav od všech NSSMF, aby udržovala holistický pohled na stav a výkon řezy. Je zodpovědná za zajištění, aby řez splňoval celkovou smlouvu o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) prostřednictvím sledování klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)), správy poruch a spouštění nápravných opatření, jako je škálování zdrojů. NSMF zpřístupňuje rozhraní směrem na sever (northbound interfaces) pro integraci s vyššími podnikovými podpůrnými systémy ([BSS](/mobilnisite/slovnik/bss/)) a operačními podpůrnými systémy ([OSS](/mobilnisite/slovnik/oss/)).

## K čemu slouží

NSMF byla vytvořena k řešení problému centralizované, automatizované orchestrace pro komplexní koncové síťové řezy (end-to-end network slices). Před zavedením síťového řezování byly síťové funkce spravovány odděleně (správa RAN, správa core), což znemožňovalo garantovat integrovanou úroveň služby napříč všemi doménami pro konkrétní logickou síť. Ruční koordinace mezi správci domén byla pomalá a náchylná k chybám.

Její zavedení ve verzi 15 (Release 15) bylo zásadní pro realizaci vize síťového řezování v 5G. NSMF poskytuje nezbytnou inteligenci pro abstrakci složitosti podkladové infrastruktury s více doménami a více dodavateli. Umožňuje operátorům nabízet 'řezy jako službu' automatizací převodu obchodního záměru (od zákazníka nebo interního servisního týmu) na technickou realitu v celé síti. Bez NSMF by byla nedosažitelná agilita, izolace a garantovaný výkon slibovaný síťovým řezováním.

## Klíčové vlastnosti

- Orchestrace životního cyklu koncového síťového řezu (vytvoření, modifikace, ukončení)
- Převod požadavků na úrovni služby (od CSMF) na technické požadavky řezy a podsítě
- Rozložení koncového řezy na podsítě síťového řezu (NSS) a koordinace s NSSMF
- Agregace dat o poruchách a výkonu od NSSMF pro holistické zajištění řezy
- Správa a vynucování SLA pro celou instanci řezy
- Vynucování politik a správa konfigurace pro řez napříč doménami

## Související pojmy

- [NSM – Network Slice Management](/mobilnisite/slovnik/nsm/)

## Definující specifikace

- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TS 28.531** (Rel-20) — Management and Orchestration
- **TS 28.801** (Rel-15) — Management and Orchestration of Network Slicing
- **TS 28.805** (Rel-16) — Management of Communication Services in 5G

---

📖 **Anglický originál a plná specifikace:** [NSMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsmf/)
