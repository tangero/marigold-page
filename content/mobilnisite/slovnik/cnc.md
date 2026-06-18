---
slug: "cnc"
url: "/mobilnisite/slovnik/cnc/"
type: "slovnik"
title: "CNC – Centralized Network Configuration"
date: 2026-01-01
abbr: "CNC"
fullName: "Centralized Network Configuration"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cnc/"
summary: "CNC je rámec správy podle 3GPP pro centralizovanou konfiguraci síťových funkcí napříč více doménami. Umožňuje automatizovanou, politikami řízenou správu konfigurace prostřednictvím standardizovaných r"
---

CNC je rámec správy podle 3GPP pro centralizovanou a automatizovanou konfiguraci síťových funkcí napříč více doménami za účelem snížení provozní složitosti.

## Popis

Centralized Network Configuration (CNC) je komplexní rámec správy definovaný 3GPP pro centralizovanou konfiguraci síťových funkcí napříč více administrativními a technologickými doménami. Architektura zavádí hierarchický model, ve kterém centrální CNC funkce koordinuje s doménově specifickými systémy správy, aby zajistila konzistentní uplatňování konfiguračních politik v celé síťové infrastruktuře. Tento rámec funguje prostřednictvím standardizovaných rozhraní, která umožňují automatizované poskytování, ověřování a monitorování konfigurace napříč heterogenními síťovými prostředími včetně segmentů RAN, core sítě a přenosové sítě.

Rámec CNC využívá přístup řízený politikami, kde jsou konfigurační politiky definovány na vysoké úrovni abstrakce a následně převáděny na doménově specifické konfigurační příkazy. Tyto politiky mohou zahrnovat různé aspekty, jako je konfigurace síťového krájení (network slicing), parametry QoS, bezpečnostní nastavení a parametry alokace zdrojů. Funkce CNC udržuje globální přehled o síťových zdrojích a jejich konfiguracích, což jí umožňuje optimalizovat využití zdrojů a zajistit konzistenci konfigurace napříč různými síťovými segmenty. Tato globální perspektiva je zvláště cenná pro poskytování služeb end-to-end, kde musí být konfigurace koordinována napříč více doménami, aby byly splněny smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)).

Mezi klíčové komponenty architektury CNC patří samotná CNC funkce, která slouží jako centrální koordinační bod, a doménově specifické systémy správy, které implementují skutečné konfigurační změny ve svých příslušných doménách. Rámec definuje standardizovaná rozhraní mezi těmito komponentami, přičemž CNC funkce komunikuje s doménovými manažery prostřednictvím rozhraní CNC-DM (Domain Manager). Datové modely konfigurace jsou standardizovány, aby byla zajištěna interoperabilita mezi implementacemi různých dodavatelů. CNC funkce také komunikuje s vyššími systémy správy, jako jsou funkce pro správu síťových řezů a platformy pro orchestraci služeb, aby přijímala konfigurační požadavky a hlásila stav konfigurace.

Při provozu CNC sleduje přístup automatizace s uzavřenou smyčkou, kde jsou konfigurační změny průběžně plánovány, nasazovány, ověřovány a monitorovány. Pokud je vyžadována změna konfigurace, CNC funkce ji nejprve ověří vůči stávajícím konfiguracím a síťovým politikám, aby zajistila kompatibilitu a shodu. Následně koordinuje nasazení změny napříč příslušnými doménami a zajišťuje správné pořadí a načasování, aby se minimalizovalo narušení služeb. Po nasazení CNC funkce monitoruje účinnost konfigurace a může spustit nápravné akce, pokud se skutečné chování sítě odchyluje od očekávaných výsledků. Tento automatizovaný lifecycle management výrazně snižuje potřebu manuálního zásahu a konfigurační chyby v komplexních síťových prostředích.

## K čemu slouží

CNC byl vyvinut, aby řešil rostoucí složitost správy síťové konfigurace v sítích 5G a budoucích sítích, kde musí více technologií, dodavatelů a administrativních domén spolupracovat bezproblémově. Tradiční přístupy ke konfiguraci sítí se silně spoléhaly na manuální, doménově specifickou konfiguraci, která byla časově náročná, náchylná k chybám a obtížně koordinovatelná napříč různými síťovými segmenty. Jak se sítě vyvíjely směrem k softwarově definovaným architekturám a síťové krájení (network slicing) se stalo základní schopností, potřeba automatizované, centralizované správy konfigurace se stala klíčovou pro umožnění rychlého nasazování služeb a efektivního využití zdrojů.

Vytvoření CNC bylo motivováno několika klíčovými výzvami v moderních telekomunikačních sítích. Za prvé, zavedení síťového krájení vyžadovalo koordinovanou konfiguraci napříč doménami RAN, core sítě a přenosové sítě pro vytváření end-to-end síťových řezů se specifickými výkonnostními charakteristikami. Bez centralizované koordinace by konfigurace řezů vyžadovala manuální koordinaci mezi více doménovými manažery, což by vedlo k dlouhým časům nasazení a potenciálním konfiguračním nekonzistencím. Za druhé, rostoucí heterogenita síťových technologií (včetně komponent 4G, 5G a budoucího 6G) vytvořila problémy s interoperabilitou, které mohly být řešeny pouze prostřednictvím standardizovaných rozhraní pro správu konfigurace.

CNC tyto problémy řeší tím, že poskytuje standardizovaný rámec pro centralizovanou správu konfigurace, který abstrahuje složitost podkladových síťových technologií. Umožňuje síťovým operátorům definovat konfigurační politiky na úrovni služby a tyto politiky automaticky převádět na doménově specifické konfigurace. To snižuje provozní náročnost, minimalizuje konfigurační chyby a urychluje nasazování služeb. Rámec také podporuje prostředí s více dodavateli definováním standardizovaných rozhraní a datových modelů, což operátorům umožňuje spravovat heterogenní síťové vybavení prostřednictvím jediného centralizovaného rozhraní namísto práce s proprietárními systémy správy každého dodavatele zvlášť.

## Klíčové vlastnosti

- Řízení konfigurace řízené politikami napříč více doménami
- Standardizovaná rozhraní pro interoperabilitu v prostředí více dodavatelů
- Automatizované nasazení a ověřování konfigurace
- Podpora koordinace konfigurace pro síťové krájení (network slicing)
- Automatizace s uzavřenou smyčkou včetně monitorování a nápravných akcí
- Hierarchická architektura správy s doménově specifickou adaptací

## Definující specifikace

- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 24.519** (Rel-17) — TSN AF to DS-TT/NW-TT Protocol Aspects
- **TS 24.539** (Rel-19) — NW-TT Protocol Aspects
- **TR 28.839** (Rel-18) — Technical Report
- **TS 29.585** (Rel-19) — TSN Interworking Protocol for 5G System
- **TS 32.282** (Rel-18) — Charging management; Time Sensitive Networking
- **TR 33.851** (Rel-17) — Security for Industrial IoT in 5G

---

📖 **Anglický originál a plná specifikace:** [CNC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cnc/)
