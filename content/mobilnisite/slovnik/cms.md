---
slug: "cms"
url: "/mobilnisite/slovnik/cms/"
type: "slovnik"
title: "CMS – Configuration Management Server"
date: 2026-01-01
abbr: "CMS"
fullName: "Configuration Management Server"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cms/"
summary: "Configuration Management Server (CMS) je síťový prvek odpovědný za správu konfigurace zařízení a služeb v sítích 3GPP. Poskytuje standardizovaný mechanismus pro zabezpečené poskytování, aktualizaci a"
---

CMS je síťový prvek odpovědný za správu konfigurace zařízení a služeb v sítích 3GPP prostřednictvím zabezpečeného poskytování, aktualizace a správy konfiguračních dat.

## Popis

Configuration Management Server (CMS) je klíčová komponenta v rámci architektury správy 3GPP, speciálně navržená pro zabezpečené a efektivní nakládání s konfiguračními daty. Funguje jako centrální úložiště a distribuční bod pro konfigurační parametry vyžadované různými síťovými funkcemi, službami a uživatelskými zařízeními (UE). Architektura CMS je definována tak, aby podporovala jak modely doručování konfigurace založené na dotazování (pull), tak na zasílání (push), což umožňuje zařízením buď vyžádat si aktualizace konfigurace, nebo je proaktivně přijímat ze sítě. Rozhraní CMS komunikuje s dalšími řídicími entitami a funkcemi správy politik, aby zajistila, že konfigurační data jsou v souladu se síťovými politikami, profily služeb a bezpečnostními požadavky.

V jádru CMS spravuje tzv. konfigurační deskriptory, což jsou strukturované datové objekty obsahující specifické sady parametrů pro cílovou entitu, jako je UE nebo síťová funkce. Tyto deskriptory jsou definovány pomocí standardizovaných datových modelů a formátů, aby byla zajištěna interoperabilita. Server provádí autentizaci a autorizaci konfiguračních požadavků, čímž zajišťuje, že konfigurační data mohou získat nebo upravit pouze oprávněné entity. Správa CMS také zahrnuje verzování a informace o závislostech konfigurací, což umožňuje možnosti návratu k předchozí verzi a konzistentní aktualizace v rámci složitých systémů. CMS často integruje s databázemi předplatitelů a funkcemi řízení politik, aby přizpůsobil konfigurace na základě uživatelských předplatných, možností zařízení a stavu sítě.

Technický provoz zahrnuje několik klíčových protokolů a rozhraní. CMS typicky vystavuje rozhraní směrem k vyšším systémům (northbound) pro administraci a integraci s operačními podpůrnými systémy ([OSS](/mobilnisite/slovnik/oss/)). Jeho rozhraní směrem k řízeným prvkům (southbound), často založené na standardizovaných protokolech jako jsou adaptace [OMA](/mobilnisite/slovnik/oma/) [DM](/mobilnisite/slovnik/dm/) (Open Mobile Alliance Device Management) nebo jiné mechanismy specifikované 3GPP, komunikuje se spravovanými zařízeními nebo síťovými prvky. Bezpečnost je prvořadá; všechny výměny jsou chráněny pomocí mechanismů definovaných v bezpečnostních specifikacích 3GPP, včetně vzájemné autentizace, ochrany integrity a důvěrnosti. CMS hraje zásadní roli ve správě životního cyklu, od počátečního zprovoznění zařízení (bootstrap konfigurace) až po průběžné aktualizace pro povolování funkcí, optimalizaci parametrů a nasazování bezpečnostních záplat, čímž snižuje provozní náročnost a minimalizuje narušení služeb.

## K čemu slouží

CMS byl zaveden, aby řešil rostoucí složitost správy konfiguračních dat v stále více heterogenních a dynamických sítích 3GPP. Před jeho standardizací byla správa konfigurace často řešena proprietárními, na dodavateli závislými řešeními nebo integrována do jiných síťových funkcí, což vedlo k problémům s interoperabilitou, bezpečnostním zranitelnostem a vysokým provozním nákladům. Absence jednotného přístupu ztěžovala konzistentní nasazování nových služeb, vynucování bezpečnostních politik nebo aktualizaci parametrů zařízení v prostředích s více dodavateli.

Jeho vznik byl motivován potřebou škálovatelného, bezpečného a standardizovaného rámce pro správu konfigurace, zejména s nástupem různorodých typů zařízení (smartphony, IoT zařízení, směrovače) a sofistikovaných síťových služeb. CMS poskytuje specializovanou, vyhrazenou funkci, která odděluje správu konfigurace od ostatních síťových procesů, což umožňuje efektivnější aktualizace, lepší sledovatelnost změn a vylepšené bezpečnostní kontroly. Řeší problémy spojené s hromadným nasazováním konfigurací, vzdálenou správou zařízení a zajišťováním souladu se síťovými politikami, což je nezbytné pro udržení kvality služeb, bezpečnosti a provozní efektivity v moderních telekomunikačních sítích.

## Klíčové vlastnosti

- Centralizované úložiště pro konfigurační deskriptory a parametry
- Podpora modelů doručování konfigurace založených jak na dotazování (pull), tak na zasílání (push)
- Zabezpečená autentizace, autorizace a chráněný přenos dat
- Verzování konfigurací, správa závislostí a možnosti návratu k předchozí verzi (rollback)
- Integrace s řízením politik a databázemi předplatitelů pro přizpůsobené konfigurace
- Standardizovaná rozhraní a datové modely pro interoperabilitu napříč dodavateli

## Definující specifikace

- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA

---

📖 **Anglický originál a plná specifikace:** [CMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cms/)
