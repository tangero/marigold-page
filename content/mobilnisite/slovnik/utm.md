---
slug: "utm"
url: "/mobilnisite/slovnik/utm/"
type: "slovnik"
title: "UTM – Uncrewed Aerial System Traffic Management"
date: 2026-01-01
abbr: "UTM"
fullName: "Uncrewed Aerial System Traffic Management"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/utm/"
summary: "UTM je servisní rámec definovaný 3GPP pro správu provozu dronů (UAS) s využitím mobilních sítí. Poskytuje komunikaci, identifikaci, sledování a koordinaci, aby umožnil bezpečné a efektivní operace dro"
---

UTM je servisní rámec 3GPP, který využívá mobilní sítě ke správě provozu bezpilotních leteckých systémů tím, že poskytuje komunikaci, identifikaci, sledování a koordinaci pro bezpečné operace v nízkých výškách.

## Popis

Uncrewed Aerial System Traffic Management (UTM) je komplexní servisní rámec, který využívá mobilní sítě pro podporu bezpečného a efektivního provozu dronů neboli bezpilotních leteckých systémů ([UAS](/mobilnisite/slovnik/uas/)). Architektura zahrnuje více entit: UAS (dron a jeho ovladač), poskytovatele UTM služeb, síť 3GPP (včetně UE, RAN a core sítě) a regulační orgány. Síť 3GPP poskytuje spolehlivé připojení pro komunikaci příkazů a řízení ([C2](/mobilnisite/slovnik/c2/)) mezi dronem a jeho pilotem nebo automatizovaným systémem, stejně jako pro služební zprávy UTM. Mezi klíčové síťové funkce patří Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) pro zpřístupnění síťových schopností poskytovatelům UTM služeb, Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro autentizaci a lokalizační služby pro sledování.

Systém funguje tak, že přes mobilní síť navazuje zabezpečené datové relace. Dron vybavený modulem 3GPP User Equipment (UE) se připojuje k síti pro C2 spoje a vysílá telemetrická data (poloha, výška, rychlost). Poskytovatel UTM služeb, kterým může být třetí strana nebo operátor sítě, využívá služebních prostředků definovaných 3GPP (jako jsou [API](/mobilnisite/slovnik/api/) související s [UAV](/mobilnisite/slovnik/uav/) zpřístupněná přes NEF) pro přístup k síťovým informacím, jako je poloha v reálném čase, identita a stav letové autorizace. Tato data se používají pro funkce správy provozu, jako je plánování letu, dynamické geofencing, detekce konfliktů a koordinace s řízením letového provozu ([ATC](/mobilnisite/slovnik/atc/)) pro operace ve vyšších výškách. Specifikace jako TS 23.255 (řízení a příkazy UAV přes síť 3GPP) a TS 23.256 (podpora konektivity, identifikace a sledování UAS) definují podrobnosti protokolů a architekturu.

Úlohou UTM je vytvořit řízený vzdušný prostor pro drony, analogicky k řízení letového provozu pro pilotovaná letadla, ale přizpůsobený pro operace v nízkých výškách s vysokou hustotou. Integruje se s regulačními rámci (jako je americká FAA nebo evropská EASA), aby zajistil soulad. Síť 3GPP poskytuje všudypřítomnou, zabezpečenou a nízkolatenční komunikační páteř vyžadovanou pro služby UTM v reálném čase. To umožňuje operace za hranicí přímé viditelnosti ([BVLOS](/mobilnisite/slovnik/bvlos/)), správu flotil více dronů a integraci do ekosystémů městské letecké mobility.

## K čemu slouží

UTM byl vytvořen, aby řešil rostoucí potřebu správy provozu dronů v důsledku nárůstu komerčního a rekreačního využívání dronů, což přináší rizika srážek ve vzduchu, rušení pilotovaného letectva a bezpečnostní obavy. Tradiční systémy řízení letového provozu jsou navrženy pro strukturované trasy ve vysokých výškách a nedokážou zvládnout velký počet dronů v nízkých výškách. Motivací pro zapojení 3GPP, počínaje Release 16, bylo využít stávající mobilní infrastrukturu – s její širokou pokrytím, vysokou spolehlivostí a zabudovanou bezpečností – k poskytnutí komunikační a servisní platformy pro UTM.

Problémy, které UTM řeší, zahrnují absenci standardizovaného systému pro identifikaci, sledování a komunikační spojení příkazů a řízení dronů. Před standardizací 3GPP se používala proprietární řešení a přímé rádiové spoje s omezeným dosahem (jako Wi-Fi), což bylo nedostatečné pro operace na velké ploše za hranicí přímé viditelnosti (BVLOS). UTM od 3GPP poskytuje globálně škálovatelný rámec, který umožňuje poskytovatelům služeb nabízet správu provozu s využitím síťových schopností, jako je přesná lokalizace, diferenciace QoS pro C2 spoje a zabezpečená autentizace. Řeší tak regulační požadavky na dálkovou identifikaci a geofencing.

Historický kontext zahrnuje tlak průmyslu a regulačních orgánů na standardizaci. 3GPP zahájila práci v Rel-16 jako součást širší expanze do vertikál, když rozpoznala potenciál mobilních sítí podporovat nová odvětví. UTM umožňuje ekonomické příležitosti v oblasti doručování pomocí dronů, inspekce infrastruktury a zásahů při mimořádných událostech tím, že činí operace dronů bezpečnějšími a lépe říditelnými. Představuje konvergenci telekomunikací a letectví a vytváří novou servisní doménu pro síťové operátory.

## Klíčové vlastnosti

- Využívá sítě 3GPP pro spolehlivá a zabezpečená komunikační spojení příkazů a řízení (C2)
- Podporuje identifikaci, sledování a dálkovou identifikaci UAV prostřednictvím síťových lokalizačních služeb
- Definuje služební prostředky (např. API přes NEF) pro poskytovatele UTM služeb, aby měli přístup k síťovým schopnostem
- Umožňuje letovou autorizaci, dynamický geofencing a správu omezení vzdušného prostoru
- Umožňuje operace za hranicí přímé viditelnosti (BVLOS) a správu flotil více dronů
- Integruje se s regulačními orgány a systémy řízení letového provozu pro koordinované operace

## Definující specifikace

- **TS 22.125** (Rel-19) — UAS Requirements via 3GPP System
- **TS 22.825** (Rel-16) — UAS Remote Identification and Tracking over 3GPP
- **TR 22.829** (Rel-17) — Enhancement for UAVs; Stage 1
- **TR 22.843** (Rel-19) — Study on Uncrewed Aerial Vehicle (UAV) Phase 3
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.755** (Rel-17) — Study on app layer support for UAS
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 28.853** (Rel-19) — Charging for Uncrewed Aerial Systems
- **TS 29.256** (Rel-19) — UAS-NF Stage 3 Protocol Specification
- **TS 29.257** (Rel-19) — Application layer support for Uncrewed Aerial System (UAS)
- **TS 33.256** (Rel-19) — Security for Uncrewed Aerial Systems (UAS)
- **TS 33.759** (Rel-19) — UAS Security Enhancements Phase 3 Study
- **TR 33.854** (Rel-17) — Security aspects of Uncrewed Aerial Systems

---

📖 **Anglický originál a plná specifikace:** [UTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/utm/)
