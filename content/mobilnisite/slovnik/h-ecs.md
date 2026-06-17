---
slug: "h-ecs"
url: "/mobilnisite/slovnik/h-ecs/"
type: "slovnik"
title: "H-ECS – Home Edge Configuration Server"
date: 2026-01-01
abbr: "H-ECS"
fullName: "Home Edge Configuration Server"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/h-ecs/"
summary: "H-ECS je síťová funkce, která spravuje životní cyklus a konfiguraci serverů pro okrajové aplikace (Edge Application Servers, EAS) v domovské síti. Umožňuje efektivní nasazení a provoz služeb edge comp"
---

H-ECS je síťová funkce, která spravuje životní cyklus a konfiguraci serverů pro okrajové aplikace (Edge Application Servers) v domovské síti za účelem zajištění efektivních služeb edge computingu.

## Popis

Home Edge Configuration Server (H-ECS) je řídicí entita zavedená ve specifikaci 3GPP Release 18 jako součást vylepšené architektury Edge Computing ([EDGE](/mobilnisite/slovnik/edge/)). Působí v rámci domovské veřejné pozemní mobilní sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)) a je zodpovědná za inicializaci, konfiguraci a správu životního cyklu serverů pro okrajové aplikace (Edge Application Servers, [EAS](/mobilnisite/slovnik/eas/)). EAS je instance serveru nasazená na okraji sítě (např. v blízkosti základnové stanice) pro hostování aplikací vyžadujících nízkou latenci nebo vysokou přenosovou rychlost, jako je rozšířená realita, průmyslová automatizace nebo videoanalýza. H-ECS poskytuje těmto instancím EAS nezbytná konfigurační data, aby se mohly zaregistrovat v síti a být dohledatelné uživatelským zařízením (UE) a dalšími síťovými funkcemi.

Z architektonického hlediska je H-ECS součástí řídicí roviny. Komunikuje s Edge Enabler Serverem ([EES](/mobilnisite/slovnik/ees/)) a Edge Configuration Serverem ([ECS](/mobilnisite/slovnik/ecs/)) v obsluhující síti. Primárním referenčním bodem je rozhraní EC8 mezi H-ECS a EAS umístěným v domovské síti. Během inicializační procedury nově vytvořená instance EAS kontaktuje H-ECS. H-ECS ověří EAS, obvykle pomocí přihlašovacích údajů zřízených během nasazení EAS. Po úspěšném ověření poskytne H-ECS EAS konfigurační balíček. Tento balíček obsahuje klíčové informace, jako je adresa příslušného Edge Enabler Serveru (EES), u kterého se má EAS zaregistrovat, bezpečnostní přihlašovací údaje pro tuto registraci, podporované profily okrajových služeb a jakékoli operátorské politiky, které musí EAS dodržovat.

Během provozu H-ECS funguje jako důvěryhodná konfigurační autorita. Zajišťuje, že se do ekosystému edge computingu mohou připojit pouze autorizované instance EAS. Poskytnutá konfigurace umožňuje EAS provést registraci u EES prostřednictvím referenčního bodu EDGE-4. EES se tak seznámí s možnostmi a umístěním EAS, což mu umožní reagovat na požadavky UE na okrajové služby. H-ECS může být také zapojen do průběžné správy, například do zasílání aktualizací konfigurace nebo spouštění vyřazení EAS z provozu. Jeho role je klíčová pro udržování zabezpečeného, organizovaného a z politiky vycházejícího souboru okrajových prostředků v celé síti operátora.

## K čemu slouží

H-ECS byl vytvořen, aby řešil provozní výzvy spojené s nasazováním a správou rozsáhlé, distribuované infrastruktury edge computingu. Před jeho standardizací bylo zřizování a konfigurace jednotlivých okrajových serverů ruční, výrobci specifický proces, který nebyl škálovatelný. Rozmístění velkého množství okrajových uzlů pro sítě 5G a novější si vyžádalo automatizované, standardizované řešení pro správu životního cyklu. H-ECS řeší problém, jak bezpečně zprovoznit a nakonfigurovat tisíce instancí [EAS](/mobilnisite/slovnik/eas/) v různých geografických lokalitách bez manuálního zásahu.

Jeho zavedení bylo motivováno potřebou jednotného řídicího bodu v doméně domovského operátora. Umožňuje operátorům udržovat kontrolu a vynucovat konzistentní politiky na všech svých okrajových prostředcích, bez ohledu na jejich fyzické umístění. To je zásadní pro zabezpečení, neboť zajišťuje, že služby mohou nabízet pouze kompatibilní instance EAS. Také zjednodušuje integraci edge computingu se stávajícími systémy pro správu a orchestraci sítě (jako je NFV-MANO). Poskytnutím standardizovaného inicializačního mechanismu H-ECS snižuje bariéru pro poskytovatele aplikací při nasazování služeb na okraji sítě, podporuje bohatší ekosystém a umožňuje využití případů s nízkou latencí, které jsou ústřední pro hodnotový návrh 5G.

## Klíčové vlastnosti

- Inicializace a počáteční konfigurace EAS prostřednictvím rozhraní EC8
- Ověření a autorizace EAS pomocí zřízených přihlašovacích údajů
- Poskytování informací pro vyhledání EES k provedení registrace EAS
- Dodání politik pro operátorské specifická pravidla a profily služeb
- Podpora správy životního cyklu instancí EAS
- Řídicí bod v domovské síti pro správu a zabezpečení okrajových prostředků

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [H-ECS na 3GPP Explorer](https://3gpp-explorer.com/glossary/h-ecs/)
