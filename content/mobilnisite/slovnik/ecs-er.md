---
slug: "ecs-er"
url: "/mobilnisite/slovnik/ecs-er/"
type: "slovnik"
title: "ECS-ER – Edge Configuration Server – Edge Repository"
date: 2026-01-01
abbr: "ECS-ER"
fullName: "Edge Configuration Server – Edge Repository"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ecs-er/"
summary: "Řídicí funkce zavedená ve specifikaci 3GPP Release 18 pro edge computing. Ukládá a poskytuje konfigurační data, popisy aplikací a profily služeb okrajovým aplikačním serverům a klientům, čímž umožňuje"
---

ECS-ER je řídicí funkce zavedená ve specifikaci 3GPP Release 18, která ukládá a poskytuje konfigurační data, popisy aplikací a profily služeb, čímž umožňuje automatizované nasazování a správu životního cyklu okrajových služeb.

## Popis

Edge Configuration Server – Edge Repository (ECS-ER) je klíčovou součástí architektury správy edge computingu 3GPP definované v TS 23.558. Funguje jako centralizovaný repozitář a konfigurační server v rámci okrajové datové sítě. ECS-ER ukládá různé datové objekty potřebné pro provoz okrajových aplikací a služeb, včetně informací pro zjišťování okrajových aplikačních serverů ([EAS](/mobilnisite/slovnik/eas/)), popisů aplikací, profilů služeb a konfiguračních parametrů pro okrajové klienty. Komunikuje s dalšími řídicími entitami, jako je Edge Enabler Client ([EEC](/mobilnisite/slovnik/eec/)) a Edge Enabler Server ([EES](/mobilnisite/slovnik/ees/)), za účelem distribuce těchto informací.

Architektonicky je ECS-ER typicky nasazen v důvěryhodné doméně operátora, často společně nebo v blízkosti Edge Application Server. Pro komunikaci s Edge Enabler Server používá standardizovaná rozhraní, jako je rozhraní Ees-ECSer. EES funguje jako zprostředkovatel, který dotazuje ECS-ER jménem okrajových klientů nebo aplikačních serverů, aby získal potřebná konfigurační data. Toto oddělení odpovědností umožňuje ECS-ER se soustředit výhradně na ukládání a poskytování dat, zatímco EES zajišťuje správu relací a uplatňování politik.

Repozitář obsahuje strukturované datové modely definované 3GPP, což zajišťuje interoperabilitu mezi edge platformami různých výrobců. Při nasazení nové okrajové aplikace je její popis – obsahující požadavky na výpočetní výkon, úložiště, latenci a umístění – zaregistrován v ECS-ER. Podobně když okrajový klient potřebuje zjistit dostupné služby, EES dotazuje ECS-ER na základě umístění a požadavků klienta. ECS-ER odpoví seznamem vhodných instancí EAS a jejich přístupovými informacemi. Tento mechanismus je klíčový pro dynamické zjišťování služeb v distribuovaném edge prostředí, kde mohou být instance aplikací vytvářeny a ukončovány podle poptávky.

Jeho role přesahuje pouhé zjišťování a zahrnuje i podporu správy životního cyklu. ECS-ER může ukládat konfigurační šablony a politiky, které určují, jak se mají okrajové aplikace škálovat, aktualizovat nebo migrovat mezi různými okrajovými uzly. Tím, že poskytuje jediný zdroj pravdy pro konfiguraci okrajových služeb, ECS-ER snižuje potřebu ručního zásahu, minimalizuje konfigurační chyby a umožňuje automatizaci nezbytnou pro provoz rozsáhlých edge sítí s více výrobci. Je to základní prvek pro realizaci vize agilních, softwarově definovaných okrajových služeb v 5G a dalších generacích.

## K čemu slouží

ECS-ER byl vytvořen pro řešení řídicích složitostí, které jsou vlastní distribuovaným architekturám edge computingu zavedeným s 5G. Před jeho specifikací edge computingová nasazení často spoléhala na proprietární nebo nestandardizované metody pro zjišťování služeb a konfiguraci, což vedlo k závislosti na dodavateli a provozní neefektivitě. Rozmístění Edge Application Serverů na mnoha místech sítě představovalo výzvu: jak mohou okrajoví klienti dynamicky a efektivně najít nejvhodnější instanci aplikace na základě latence, schopností a vytížení? ECS-ER poskytuje standardizované řešení.

Jeho vývoj byl motivován potřebou automatizace a škálovatelnosti při nasazování okrajových služeb. Ruční konfigurace tisíců okrajových uzlů a klientů je nepraktická. ECS-ER jako součást širšího rámce Edge Application Enablement umožňuje deklarativní správu služeb. Poskytovatelé aplikací mohou své profily služeb zaregistrovat jednou a systém automaticky zajistí jejich distribuci a zjišťování. Tím je řešen problém mobility služeb a kontinuity při pohybu uživatelů, což zajišťuje jejich plynulé připojení k optimální okrajové instanci.

Dále podporuje paradigma síťových řezů tím, že umožňuje, aby konfigurační data byla specifická pro daný řez. To znamená, že okrajové prostředky a služby mohou být izolovány a přizpůsobeny různým podnikovým zákazníkům nebo typům služeb. Centralizací konfiguračních dat v repozitáři získávají operátoři lepší přehled a kontrolu nad svými okrajovými prostředky, což usnadňuje řešení problémů, auditování a dodržování předpisů. ECS-ER je tedy klíčovým prvkem pro komerční úspěch edge computingu, který jej mění z koncepční technologie na řiditelnou a provozovatelnou realitu.

## Klíčové vlastnosti

- Centralizovaný repozitář pro popisy okrajových aplikací a profily služeb
- Standardizovaný mechanismus pro zjišťování služeb pro okrajové klienty prostřednictvím Edge Enabler Server
- Ukládá konfigurační data pro Edge Application Server (EAS) a Edge Enabler Client (EEC)
- Podporuje dynamické zřizování a správu životního cyklu okrajových služeb
- Umožňuje výběr služeb na základě umístění a schopností
- Poskytuje rozhraní pro registraci, dotazování a odběr oznámení o změnách konfiguračních dat

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications

---

📖 **Anglický originál a plná specifikace:** [ECS-ER na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecs-er/)
