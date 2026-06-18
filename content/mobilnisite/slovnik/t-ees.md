---
slug: "t-ees"
url: "/mobilnisite/slovnik/t-ees/"
type: "slovnik"
title: "T-EES – Target Edge Enabler Server"
date: 2026-01-01
abbr: "T-EES"
fullName: "Target Edge Enabler Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/t-ees/"
summary: "Target Edge Enabler Server (T-EES) je síťová funkce zavedená ve 3GPP Release 17 pro edge computing. Funguje jako servisní koncový bod pro klientské aplikace (EEC), které chtějí objevit a připojit se k"
---

T-EES (Target Edge Enabler Server) je cílový server pro povolení edge služeb, síťová funkce 3GPP Release 17, která slouží jako koncový bod pro klientské aplikace, aby mohly objevovat a připojovat se k optimálním edge aplikačním serverům pro služby s nízkou latencí.

## Popis

Target Edge Enabler Server (T-EES) je klíčová architektonická komponenta v rámci frameworku 3GPP Edge Application Enablement definovaného od Release 17. Funguje jako serverová protistrana ke klientovi Edge Enabler Client ([EEC](/mobilnisite/slovnik/eec/)), který sídlí v uživatelském zařízení (UE) nebo aplikačním serveru. Primární role T-EES je sloužit jako důvěryhodný zprostředkovatel pro objevování a připojování k edge aplikacím. Když EEC potřebuje využít službu edge computingu, dotazuje se T-EES. T-EES využívá síťové schopnosti a politiky, aby poskytl EEC potřebné informace pro připojení k nejvhodnějšímu Edge Application Serveru ([EAS](/mobilnisite/slovnik/eas/)), který hostuje vlastní aplikační logiku. Tento proces je řízen Edge Configuration Serverem ([ECS](/mobilnisite/slovnik/ecs/)), který EEC zřizuje adresou T-EES.

Operačně T-EES komunikuje s dalšími klíčovými síťovými funkcemi, včetně Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), aby získal přístup k síťovým a uživatelským datům pro činění inteligentních rozhodnutí o výběru edge služeb. Podporuje servisní [API](/mobilnisite/slovnik/api/) definovaná ve 3GPP TS 23.558, což umožňuje přenos aplikačního kontextu a plynulou kontinuitu služeb při pohybu uživatele. T-EES je klíčový pro implementaci referenčního bodu 'EDGE-9', což je rozhraní mezi EEC a T-EES pro registraci služeb, jejich objevování a navazování spojení.

Z pohledu nasazení může být T-EES umístěn v síti operátora, potenciálně v centrální lokalitě nebo distribuován napříč více edge lokalitami. Jeho implementace umožňuje síti dynamicky směrovat aplikační relace k edge zdrojům na základě reálných podmínek, jako je poloha UE, vytížení sítě a požadavky aplikace. Tím odděluje potřebu aplikací na nízkou latenci a vysokou propustnost od tradiční centralizované architektury core sítě a připravuje cestu pro novou generaci imerzivních a responzivních služeb, jako je rozšířená realita, průmyslová automatizace a inteligentní videoanalytika.

## K čemu slouží

T-EES byl vytvořen, aby řešil základní výzvu efektivního zpřístupňování a správy edge výpočetních zdrojů v mobilní síti. Před jeho standardizací bylo nasazování aplikací s nízkou latencí na síťovém okraji často specifické a neinteroperabilní úsilí. Aplikace neměly standardizovaný mechanismus pro dynamické zjišťování, kde jsou edge zdroje dostupné, ani pro navazování optimálních spojení k nim při pohybu uživatelů. To omezovalo škálovatelnost a komerční životaschopnost edge computingu.

Zavedení T-EES v Release 17, jako součást širší pracovní položky Edge Application Enablement, poskytlo standardizovanou, operátorem řízenou vrstvu pro povolování služeb. Řeší problém objevování a přístupu k edge službám a zajišťuje, že klientské aplikace mohou nalézt a připojit se k nejbližší nebo nejvhodnější instanci edge aplikace bezpečným a politikami řízeným způsobem. Tato standardizace je klíčová pro vytvoření více-dodavatelského ekosystému, kde mohou vzájemně spolupracovat poskytovatelé aplikací, síťoví operátoři a cloudoví poskytovatelé.

Navíc T-EES umožňuje nové obchodní modely tím, že operátorům dovoluje zpřístupňovat edge schopnosti jako službu. Poskytuje potřebné řídicí rovinné funkce pro správu životního cyklu relací edge aplikací, včetně aspektů zabezpečení, mobility a kvality služeb, které bylo dříve v distribuovaném edge prostředí obtížné orchestraovat. Jeho vznik byl motivován posunem průmyslu k distribuovaným cloudovým architekturám a potřebou podporovat případy užití ultra-spolehlivé komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a rozšířeného mobilního širokopásmového připojení (eMBB), které jsou s čistě centralizovanou core sítí neproveditelné.

## Klíčové vlastnosti

- Standardizované objevování edge služeb pro klientské aplikace (EEC)
- Dynamický výběr optimálního Edge Application Serveru (EAS) na základě síťových podmínek a politik
- Podpora přenosu aplikačního kontextu pro zajištění kontinuity služeb při mobilitě
- Integrace s funkcemi core sítě (NEF, UDM) pro přístup k politikám a datům
- Zpřístupnění edge schopností prostřednictvím 3GPP definovaných servisních API (TS 23.558)
- Umožňuje zabezpečený a autorizovaný přístup k edge výpočetním zdrojům

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [T-EES na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-ees/)
