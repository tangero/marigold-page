---
slug: "p-ue"
url: "/mobilnisite/slovnik/p-ue/"
type: "slovnik"
title: "P-UE – Pedestrian User Equipment"
date: 2025-01-01
abbr: "P-UE"
fullName: "Pedestrian User Equipment"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/p-ue/"
summary: "Klasifikace stavu mobility UE označující uživatele pohybujícího se pěší rychlostí. Umožňuje síti aplikovat optimalizované řízení rádiových zdrojů a mobility, čímž zlepšuje výkon předávání spojení a vý"
---

P-UE je klasifikace stavu mobility UE označující uživatele pohybujícího se pěší rychlostí, která umožňuje optimalizované síťové procedury pro zlepšení předávání spojení a výdrže baterie.

## Popis

Pedestrian UE (P-UE) je klasifikace stavu mobility definovaná ve standardech 3GPP pro identifikaci uživatelského zařízení (UE), které se pohybuje typickou pěší rychlostí, obecně považovanou za rychlost nižší než 30 km/h. Tato klasifikace je součástí širší sady stavů mobility, která zahrnuje také UE se střední mobilitou (M-UE) a UE s vysokou mobilitou (H-UE), které odpovídají rychlostem vozidel. Síť určuje stav mobility UE na základě měření rychlosti změny buňky nebo předávání spojení, nebo pomocí přímých technik odhadu rychlosti. Po klasifikaci může síť přizpůsobit parametry správy mobility konkrétně pro tento stav.

Z architektonické perspektivy je klasifikaci P-UE řízena rádiovou přístupovou sítí (RAN), konkrétně eNodeB v LTE nebo gNB v 5G NR. Uzel RAN sleduje chování UE, jako je rychlost předávání spojení nebo počet změn buňky v rámci specifického časového okna definovaného časovači, jako je T-Criterion v LTE. Algoritmy pro detekci stavu jsou implementačně specifické, ale dodržují směrnice 3GPP pro zajištění interoperability. Klasifikace může ovlivnit procedury jak v řídicí rovině, tak v uživatelské rovině.

Provozně klasifikace UE jako P-UE spouští optimalizované konfigurace. Síť například může snížit frekvenci požadovaných měřicích hlášení od UE, protože pěší pohyb má za následek pomalejší změny stavu kanálu ve srovnání s pohybem vozidel. Tím se snižuje signalizační režie a spotřeba energie UE. Parametry předávání spojení, jako jsou hysterezní okraje a hodnoty času do spuštění ([TTT](/mobilnisite/slovnik/ttt/)), mohou být upraveny tak, aby byly méně agresivní, čímž se zabrání zbytečným předáním spojení (ping-pong efektům) v hustých městských nebo vnitřních prostředích, kde převládají malé buňky. Tato stabilizace zlepšuje uživatelský zážitek udržováním kontinuity spojení.

Role klasifikace P-UE zasahuje do optimalizace výkonu sítě. Aplikací stavově specifického řízení rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) může síť efektivněji alokovat zdroje a plánovat zatížení buněk. Například základnová stanice obsluhující mnoho P-UE může používat jiné plánovací algoritmy ve srovnání se stanicí obsluhující dopravu na dálnici. V 5G tento koncept navazuje na síťové slicing a diferenciaci QoS, což umožňuje, aby slice optimalizovaný pro pěší uživatele (např. ve scénáři chytrého města) měl svůj vlastní profil mobility. Klasifikace je základním prvkem pro umožnění pokročilých funkcí, jako je úspora energie v RAN založená na mobilitě.

## K čemu slouží

Klasifikace P-UE byla zavedena, aby řešila neefektivitu aplikace jednotné strategie správy mobility na všechny uživatele. Rané mobilní sítě používaly pevné parametry pro předávání spojení a změnu buňky, což mohlo vést k neoptimálnímu výkonu. Pro rychle se pohybující uživatele musely být parametry citlivé, aby se zabránilo přerušení hovoru, ale pro pomalu se pohybující chodce stejná nastavení způsobovala nadměrnou signalizaci, zbytečná předání spojení a sníženou výdrž baterie. Rozšíření malých buněk a heterogenních sítí (HetNets) v 4G a 5G tento problém prohloubilo, protože pěší uživatelé v hustých městských oblastech mohli spouštět častá předání spojení mezi mnoha blízkými buňkami.

Vytvořením odlišných stavů mobility umožnila 3GPP síti inteligentně se přizpůsobit. Primárním řešeným problémem je optimalizace procedur mobility pro různé profily rychlosti uživatelů. Pro pěší uživatele je cílem minimalizovat signalizační režii a spotřebu energie při zachování odpovídající kvality služby. To je zvláště důležité pro výdrž baterie IoT zařízení nebo smartphonů. Dále to snižuje síťovou kongesci způsobenou řídicí signalizací a uvolňuje zdroje pro uživatelská data. Historický kontext zahrnuje vylepšení pro LTE v Rel-14 a následnou integraci do 5G NR, kde podpora různých scénářů mobility je klíčová pro případy užití od massive IoT po enhanced mobile broadband.

## Klíčové vlastnosti

- Detekce stavu mobility na základě rychlosti změny buňky nebo odhadu rychlosti
- Spouští optimalizované parametry předávání spojení (např. delší Time-To-Trigger) pro stabilitu
- Snižuje frekvenci hlášení měření kanálu od UE
- Umožňuje úsporu energie UE díky méně častým rádiovým procedurám
- Podporuje diferencované strategie řízení rádiových zdrojů (RRM)
- Integruje se se síťovým slicingem pro služebně specifické profily mobility

## Definující specifikace

- **TR 23.776** (Rel-17) — V2X Architecture Enhancements Phase 2
- **TS 36.885** (Rel-14) — Feasibility Study on LTE-based V2X Services
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR

---

📖 **Anglický originál a plná specifikace:** [P-UE na 3GPP Explorer](https://3gpp-explorer.com/glossary/p-ue/)
