---
slug: "aim"
url: "/mobilnisite/slovnik/aim/"
type: "slovnik"
title: "AIM – Application Information Model"
date: 2025-01-01
abbr: "AIM"
fullName: "Application Information Model"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/aim/"
summary: "AIM je standardizovaný informační model v rámci 3GPP, který definuje způsob reprezentace a správy dat souvisejících s aplikacemi v telekomunikačních sítích. Poskytuje společný rámec pro popis charakte"
---

AIM je standardizovaný 3GPP informační model pro reprezentaci a správu dat souvisejících s aplikacemi, který umožňuje konzistentní provisioning, vynucování politik a orchestraci napříč síťovými elementy.

## Popis

Application Information Model (AIM) je komplexní datový model definovaný v rámci 3GPP management framework, který specifikuje strukturu, atributy, vztahy a chování informací souvisejících s aplikacemi. Slouží jako abstraktní reprezentace aplikací nasazených v telekomunikační síti nebo s ní interagujících, zachycující jak statické charakteristiky, tak dynamické stavové informace. Model je typicky vyjádřen pomocí standardizovaných modelovacích jazyků, jako je [UML](/mobilnisite/slovnik/uml/) (Unified Modeling Language), a je implementován prostřednictvím management rozhraní, jako jsou ta definovaná v rámci 3GPP Management Object Model (MOM) framework.

Architektonicky AIM funguje v doménách Operations Support System ([OSS](/mobilnisite/slovnik/oss/)) a Business Support System ([BSS](/mobilnisite/slovnik/bss/)) a poskytuje standardizovaný způsob, jakým mohou systémy správy sítě interagovat s entitami souvisejícími s aplikacemi. Model definuje třídy reprezentující různé aspekty aplikací, včetně jejich funkčních schopností, požadavků na zdroje, výkonnostních charakteristik a stavů životního cyklu. Tyto třídy jsou organizovány v hierarchické struktuře s vztahy dědičnosti, což umožňuje specializaci obecných aplikačních konceptů na konkrétní typy aplikací. Model zahrnuje atributy pro identifikaci, verzování, informace o dodavateli, parametry nasazení a operační stav.

Klíčové komponenty AIM zahrnují třídu Application jako centrální entitu, s přidruženými třídami pro Application Requirements (specifikující potřebné výpočetní, úložné a síťové zdroje), Application Dependencies (definující vztahy s jinými aplikacemi nebo službami) a Application Policies (řídící chování za různých podmínek). Model také definuje vztahy mezi aplikacemi a síťovými zdroji, což umožňuje management systémům pochopit, jak aplikace využívají podkladovou infrastrukturu. Management operace, jako je vytváření, konfigurace, aktivace, monitorování a ukončování instancí aplikací, jsou podporovány prostřednictvím standardizovaných rozhraní, která vystavují AIM.

V praxi AIM umožňuje management systémům provádět automatizovaný životní cyklus aplikací tím, že poskytuje konzistentní informační strukturu, kterou mohou zpracovávat různé management funkce. Když je třeba aplikaci nasadit, management systém načte její AIM reprezentaci, ověří požadavky vůči dostupným zdrojům, nakonfiguruje potřebné síťové elementy a monitoruje operační stav aplikace. Model podporuje jak real-time management (prostřednictvím notifikací a alarmů), tak offline management (prostřednictvím konfiguračních databází). Poskytnutím této standardizované abstraktní vrstvy AIM usnadňuje interoperabilitu mezi různými management systémy a snižuje složitost integrace v více-dodavatelských síťových prostředích.

## K čemu slouží

AIM byl vytvořen, aby řešil rostoucí složitost správy různorodých aplikací v telekomunikačních sítích, zejména jak se sítě vyvíjely od poskytování základní konektivity k podpoře sofistikovaných služeb s přidanou hodnotou. Před AIM každý dodavatel aplikací typicky používal proprietární informační modely pro popis svých aplikací, což ztěžovalo síťovým operátorům spravovat aplikace od různých dodavatelů prostřednictvím jednotného management systému. Tato fragmentace vedla k operačním neefektivnostem, zvýšeným nákladům na integraci a omezeným možnostem automatizace pro nasazování a správu aplikací.

Primární motivací pro vývoj AIM bylo vytvořit standardizovaný způsob reprezentace aplikačních informací, kterému by bylo možné konzistentně rozumět a který by bylo možné konzistentně zpracovávat napříč různými management systémy a síťovými doménami. Tato standardizace umožňuje operátorům implementovat automatizované workflow pro onboarding aplikací, provisioning, monitorování a správu životního cyklu bez nutnosti vlastní integrace pro každou aplikaci. Poskytnutím společného jazyka pro popis aplikací AIM snižuje čas a náklady spojené se zaváděním nových služeb a zároveň zlepšuje operační spolehlivost prostřednictvím konzistentních management postupů.

Historicky zavedení AIM v [R99](/mobilnisite/slovnik/r99/) korespondovalo s nástupem sofistikovanějších mobilních služeb přesahujících základní hlasové hovory, včetně raných datových služeb a aplikací s přidanou hodnotou. Jak se sítě vyvíjely směrem k 3G a pozdějším generacím, potřeba standardizované správy aplikací se stávala stále kritičtější pro podporu rostoucího ekosystému aplikací a služeb třetích stran. AIM řešil omezení předchozích ad-hoc přístupů tím, že poskytl framework schopný škálovat s rostoucí diverzitou a složitostí síťových aplikací při zachování zpětné kompatibility s existujícími management systémy.

## Klíčové vlastnosti

- Standardizovaná reprezentace charakteristik a požadavků aplikací
- Podpora operací správy životního cyklu aplikací
- Definice vztahů mezi aplikacemi a síťovými zdroji
- Integrace s 3GPP Management Object Model (MOM) framework
- Podpora interoperability správy aplikací od více dodavatelů
- Schopnost reprezentovat jak statickou konfiguraci, tak dynamický operační stav

## Definující specifikace

- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 32.181** (Rel-19) — User Data Convergence Management Framework
- **TR 32.901** (Rel-19) — UDC Application Data Models Study

---

📖 **Anglický originál a plná specifikace:** [AIM na 3GPP Explorer](https://3gpp-explorer.com/glossary/aim/)
