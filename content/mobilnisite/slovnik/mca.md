---
slug: "mca"
url: "/mobilnisite/slovnik/mca/"
type: "slovnik"
title: "MCA – MSE Configuration API"
date: 2025-01-01
abbr: "MCA"
fullName: "MSE Configuration API"
category: "Management"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/mca/"
summary: "MSE Configuration API (MCA) je standardizované rozhraní zavedené ve verzi 3GPP Release 16 pro správu konfigurací Media Streaming Engine (MSE). Umožňuje dynamické řízení a optimalizaci parametrů doručo"
---

MCA je standardizované rozhraní zavedené ve verzi 3GPP Release 16 pro správu konfigurací Media Streaming Engine, umožňující dynamické řízení parametrů doručování médií pro zlepšení kvality streamování a efektivity sítě.

## Popis

[MSE](/mobilnisite/slovnik/mse/) Configuration [API](/mobilnisite/slovnik/api/) (MCA) je standardizované aplikační programové rozhraní definované v architektuře 3GPP, určené speciálně pro správu a konfiguraci Media Streaming Engines (MSE). MSE je síťová funkce zodpovědná za zpracování a doručování mediálního obsahu, jako jsou video a audio streamy, do koncových uživatelských zařízení. MCA poskytuje programové prostředky pro externí aplikace nebo systémy správy sítě k interakci s MSE, což umožňuje dynamické přizpůsobení jeho provozních parametrů. Tato interakce je klíčová pro optimalizaci doručování médií v reálném čase na základě stavu sítě, preferencí uživatele a požadavků služby.

Architektonicky je MCA typicky implementováno jako sada RESTful nebo podobných webových služeb API, jak je specifikováno v 3GPP TS 23.479 a TS 26.857. Definuje strukturovaný datový model a řadu operací (např. GET, POST, PUT, DELETE), které lze vyvolat pro čtení nebo úpravu konfiguračního stavu MSE. Klíčové aspekty konfigurace spravované prostřednictvím MCA zahrnují profily adaptivního streamování s proměnným datovým tokem ([ABR](/mobilnisite/slovnik/abr/)), strategie ukládání obsahu do mezipaměti, nastavení šifrování, parametry kvality služeb (QoS) a konfigurace logování a analýzy. API funguje jako severní rozhraní (northbound interface), které abstrahuje vnitřní složitosti MSE a představuje konzistentní správovou fasádu.

MCA funguje v širším ekosystému doručování médií. Typický pracovní postup zahrnuje síťový analytický modul nebo orchestrační systém, který monitoruje síťové vytížení, možnosti uživatelského zařízení a oblíbenost obsahu. Na základě těchto informací systém pomocí MCA zasílá konfigurační aktualizace do MSE. Například během špičkového vytížení lze MCA použít k pokynu pro MSE, aby upřednostňovalo video profily s nižším datovým tokem nebo aby předběžně načítalo oblíbený obsah do okrajových (edge) mezipamětí. Tato dynamická konfigurace umožňuje síti udržovat vysokou kvalitu streamování při efektivním využívání přenosové kapacity a výpočetních zdrojů.

Jeho role v síti je klíčová pro umožnění inteligentního, softwarově definovaného doručování médií. Oddělením řídicí roviny (správa konfigurace pomocí MCA) od datové roviny (skutečné zpracování a přenos médií v MSE) usnadňuje automatizaci, agilitu a inovace služeb. Provozovatelé sítí a poskytovatelé obsahu mohou prostřednictvím standardizovaných API volání nasazovat nové funkce pro streamování, optimalizovat výkon pro různé scénáře a rychleji řešit problémy, čímž opouštějí manuální, na zařízení specifické způsoby konfigurace.

## K čemu slouží

MCA bylo vytvořeno pro řešení rostoucí složitosti a dynamické povahy streamování médií v mobilních sítích. Před jeho standardizací konfigurace a správa Media Streaming Engines často zahrnovala proprietární rozhraní specifická pro dodavatele nebo manuální zásahy prostřednictvím příkazového řádku. Tento nedostatek jednotnosti ztěžoval operátorům automatizaci pracovních postupů doručování médií, integraci [MSE](/mobilnisite/slovnik/mse/) s širšími systémy správy sítě a rychlé nasazování nových optimalizací streamování napříč nasazeními s více dodavateli.

Motivace vycházela z explozivního růstu video provozu, který vyžaduje inteligentní, na síť citlivou adaptaci pro zajištění kvality uživatelského prožitku ([QoE](/mobilnisite/slovnik/qoe/)). Statické konfigurace nedostačovaly pro zvládání proměnlivých síťových podmínek a různých možností uživatelských zařízení. MCA poskytuje standardizovaný 'regulační prvek' pro externí inteligenci (jako je síťová analýza nebo [AI](/mobilnisite/slovnik/ai/)), aby dynamicky ladila chování MSE. To řeší problém rigidního, univerzálního doručování médií a umožňuje optimalizaci v reálném čase pro efektivitu šířky pásma, snížení latence a zlepšení kvality videa.

Historicky, jak se 3GPP vyvíjelo pro podporu rozšířených multimediálních služeb ve verzích 15 a 16, vznikla jasná potřeba formalizovat správu mediálních funkcí v rámci služební architektury 5G. MCA je v souladu s tímto trendem, neboť nabízí cloud-nativní, API-řízený přístup ke konfiguraci, podporuje síťové řezy (network slicing) pro mediální služby a umožňuje agilnější nasazování služeb a správu životního cyklu pro streamovací aplikace.

## Klíčové vlastnosti

- Standardizované RESTful API rozhraní pro správu MSE
- Dynamická konfigurace profilů adaptivního streamování s proměnným datovým tokem (ABR)
- Řízení zásad ukládání obsahu do mezipaměti a předběžného načítání
- Konfigurace šifrování médií a bezpečnostních parametrů
- Nastavení pravidel kvality služeb (QoS) a tvarování provozu
- Umožnění konfigurace analýz v reálném čase a logování

## Související pojmy

- [MSE – Mobility Speed Estimation](/mobilnisite/slovnik/mse/)
- [ABR – Adaptive Bit Rate](/mobilnisite/slovnik/abr/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers

---

📖 **Anglický originál a plná specifikace:** [MCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mca/)
