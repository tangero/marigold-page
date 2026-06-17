---
slug: "ecsp"
url: "/mobilnisite/slovnik/ecsp/"
type: "slovnik"
title: "ECSP – Edge Computing Service Provider"
date: 2026-01-01
abbr: "ECSP"
fullName: "Edge Computing Service Provider"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ecsp/"
summary: "Entita, která v rámci architektury 3GPP poskytuje možnosti a služby edge computingu. Umožňuje aplikace s nízkou latencí hostováním aplikací blíže uživateli, což je klíčové pro služby jako AR/VR, průmy"
---

ECSP je entita, která v rámci architektury 3GPP poskytuje možnosti a služby edge computingu, aby umožnila aplikace s nízkou latencí hostováním těchto aplikací blíže uživateli.

## Popis

Edge Computing Service Provider (ECSP) je funkční role definovaná v architektuře 3GPP pro umožnění edge computingu. Provozuje Edge Application Server ([EAS](/mobilnisite/slovnik/eas/)) a Edge Enabler Server ([EES](/mobilnisite/slovnik/ees/)), což jsou klíčové komponenty architektury Edge Computing ([EC](/mobilnisite/slovnik/ec/)). ECSP je zodpovědný za nasazování a správu aplikací na okraji sítě a poskytuje potřebné výpočetní, úložné a síťové prostředky. Rozhraní s 3GPP sítí, konkrétně s 5G Core Network (5GC), za účelem usnadnění objevování služeb, směrování provozu a kontinuity relace pro uživatelské zařízení (UE) s podporou edge computingu. Role ECSP je odlišná od role Mobile Network Operator ([MNO](/mobilnisite/slovnik/mno/)); může se jednat o poskytovatele služeb třetí strany, který využívá konektivitu MNO k nabízení rozšířených služeb s nízkou latencí.

Architektura ECSP je založena na Edge Enabler Client ([EEC](/mobilnisite/slovnik/eec/)) v UE a Edge Enabler Server (EES) v síti. EES, spravovaný ECSP, funguje jako centrální bod pro registraci a objevování edge služeb. Když UE potřebuje edge službu, jeho EEC se dotazuje EES (prostřednictvím 3GPP sítě), aby objevil příslušný Edge Application Server (EAS). EAS, který je také hostován ECSP, je místem, kde se nachází vlastní aplikační logika. 3GPP síť prostřednictvím mechanismů jako Local Area Data Network ([LADN](/mobilnisite/slovnik/ladn/)) a výběr User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) zajišťuje, že datový provoz UE je směrován k optimální instanci EAS, čímž se minimalizuje latence a zatížení backhaulového spoje.

Klíčové protokoly a rozhraní pro ECSP jsou definovány v technických specifikacích jako TS 23.558. Referenční body EC-3 (EEC-EES) a EC-5 (EES-EAS) jsou klíčové pro umožnění služeb. ECSP komunikuje s 5GC prostřednictvím [NEF](/mobilnisite/slovnik/nef/) (Network Exposure Function) pro přístup k síťovým schopnostem a s PCF (Policy Control Function) pro uplatňování politik specifických pro edge computing. Zabezpečení je prvořadé; ECSP musí provádět autentizaci a autorizaci UE a zajistit zabezpečenou komunikaci mezi všemi edge entitami. Model ECSP podporuje principy multi-access edge computingu (MEC), což umožňuje aplikacím využívat jak 3GPP, tak non-3GPP přístupové sítě.

## K čemu slouží

Koncept ECSP byl zaveden, aby formalizoval a standardizoval roli poskytovatelů edge služeb třetích stran v ekosystému 5G. Před jeho definicí byla nasazení edge computingu často proprietární nebo těsně svázaná s jediným mobilním operátorem, což omezovalo inovace a přenositelnost služeb. Vzestup aplikací citlivých na latenci, jako jsou autonomní vozidla, taktilní internet a imerzivní média, vytvořil poptávku po standardizovaném, interoperabilním edge frameworku, který by oddělil poskytování služeb od síťové konektivity.

Model ECSP řeší problém, jak efektivně nasazovat a objevovat aplikace na okraji sítě v prostředí s více dodavateli a více zúčastněnými stranami. Řeší výzvu umožnit UE dynamicky najít a připojit se k nejbližší nebo nejvhodnější instanci aplikačního serveru, což je zásadní pro udržení nízké latence a efektivního využití prostředků. Definováním jasných funkčních rolí a rozhraní umožňuje 3GPP Mobile Network Operatorům (MNO) nabízet svůj síťový okraj jako platformu externím ECSP, čímž podporuje bohatší ekosystém služeb a nové zdroje příjmů mimo tradiční konektivitu.

## Klíčové vlastnosti

- Hostí a spravuje Edge Application Server (EAS) a Edge Enabler Server (EES)
- Poskytuje standardizované mechanismy pro objevování a registraci edge aplikací
- Umožňuje datové cesty s nízkou latencí prostřednictvím rozhraní s možnostmi směrování provozu 3GPP
- Podporuje multi-access edge computing napříč přístupovými typy 3GPP i non-3GPP
- Komunikuje s funkcemi 5G Core Network (NEF, PCF) pro politiky a vystavení funkcí
- Usnadňuje oddělený ekosystém, kde je poskytování služeb odděleno od provozu sítě

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.558** (Rel-19) — Edge Enabler APIs Stage 3
- **TS 28.538** (Rel-19) — Edge Computing Management (ECM)
- **TR 28.815** (Rel-17) — Charging Study for Edge Computing
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TR 28.844** (Rel-18) — Technical Report on Charging Aspects of Satellite in 5GS
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TS 32.257** (Rel-19) — Edge Computing Charging Management
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [ECSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecsp/)
