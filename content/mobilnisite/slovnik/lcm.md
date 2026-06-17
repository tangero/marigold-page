---
slug: "lcm"
url: "/mobilnisite/slovnik/lcm/"
type: "slovnik"
title: "LCM – Life Cycle Management"
date: 2026-01-01
abbr: "LCM"
fullName: "Life Cycle Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/lcm/"
summary: "Proces řízení životního cyklu síťových služeb, síťových funkcí a síťových slice v systému 3GPP od začátku do konce. Zahrnuje instanciaci, konfiguraci, škálování, aktualizaci, monitorování a ukončení,"
---

LCM je proces řízení životního cyklu síťových služeb, funkcí a slice od začátku do konce, který zahrnuje jejich instanciaci, konfiguraci, škálování, aktualizaci, monitorování a ukončení.

## Popis

Life Cycle Management (LCM) v 3GPP označuje komplexní soubor řídicích procedur a schopností potřebných pro řízení celého životního cyklu řízených entit v síti 3GPP, zejména v kontextu virtualizace a softwarizace síťových funkcí zaváděných s 5G. Primární řízené entity jsou síťové funkce ([NF](/mobilnisite/slovnik/nf/)), které mohou být virtualizované (VNF) nebo cloud-nativní ([CNF](/mobilnisite/slovnik/cnf/)), síťové služby (NS) tvořené více vzájemně spojenými NF a síťové slice, což jsou logické end-to-end sítě pro specifické businessové případy. LCM proces je základní funkcí frameworku Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)), v souladu s [ETSI](/mobilnisite/slovnik/etsi/) [NFV](/mobilnisite/slovnik/nfv/), a je prováděn entitami jako Network Function Virtualization Orchestrator ([NFVO](/mobilnisite/slovnik/nfvo/)) a 3GPP Network Slice Management Function (NSMF).

Operace LCM následuje fázový model. Pro síťovou službu nebo síťový slice začíná **fází instanciace a konfigurace**. Zahrnuje validaci deploymentového template (např. Network Service Descriptor), alokaci potřebných zdrojů (compute, storage, network), nasazení komponentních balíčků VNF/CNF na vybranou infrastrukturu a konfiguraci počátečních parametrů a konektivity mezi funkcemi. Po instanciaci následuje **fáz provozu**, která zahrnuje kontinuální monitorování výkonu, dohled nad chybami a dynamické akce jako **škálování** (in/out, up/down) pro adaptaci na změny zatížení a **healing** pro obnovu z selhání reinstanciací komponent. **Fáze aktualizace a upgrade** řídí změny, jako aplikace softwarových patchů nebo modifikace service descriptorů, často vyžadující komplexní rollback procedury. Nakonec **fáze ukončení** zahrnuje řádné zastavení služby, uvolnění všech alokovaných zdrojů a aktualizaci inventáře.

Klíčové architektonické komponenty zapojené v LCM zahrnují **Service Management Function ([SMF](/mobilnisite/slovnik/smf/))** pro business-level management, **Network Slice Management Function (NSMF)** a **Network Slice Subnet Management Function (NSSMF)** pro LCM specifické pro slice, **NFVO** pro orchestrace zdrojů a **Virtualized Infrastructure Manager (VIM)** pro řízení infrastruktury. LCM funguje prostřednictvím standardizovaných interfaceů (např. Os-Ma-nfvo, Or-Vnfm) a datových modelů (např. na základě YANG), které přenášejí LCM operace. Jeho role je fundamentální pro dosažení agility, automatizace a efektivity, které přináší 5G, umožňující operátorům rychle nasazovat a elasticky provozovat služby s minimálním manuálním zásahem.

## K čemu slouží

LCM bylo zaváděno pro řešení provozní komplexity a rigidity tradičních telekomunikačních sítí postavených na dedikovaných, proprietárních hardwareových zařízeních. Řízení životního cyklu fyzických síťových elementů bylo manuální, pomalé a náchylné na chyby. Přechod k Network Functions Virtualization ([NFV](/mobilnisite/slovnik/nfv/)), Software-Defined Networking (SDN) a cloud-nativním principům v 3GPP, začínající významně ve Release 14 pro 5G, vytvořil potřebu automatizovaných, standardizovaných řídicích procedur. Bez LCM nemohly být realizovány benefity virtualizace – jako rychlé nasazení služeb, elastické škálování a efektivní využití zdrojů.

Primární problémy, které LCM řeší, jsou dlouhá doba uvedení nových služeb na trh, neefektivní využití hardwareových zdrojů kvůli statické provisioning a vysoké provozní náklady (OPEX) spojené s manuální konfiguraci a troubleshootingem. Poskytuje framework pro přístup k síťovým funkcím a službám jako software, který lze řídit programově. Toto bylo motivované snahou konkurovat web-scale cloudovým providerům v agility a podporovat diverzní a dynamické požadavky 5G use cases, jako massive IoT, enhanced mobile broadband a ultra-reliable low-latency communication, každý potenciálně vyžadující vlastní specificky řízený síťový slice.

Dále LCM umožňuje closed-loop automatizaci, kde monitoring data automaticky spouští LCM operace (např. scale-out při zatížení), směřující k samooptimalizujícím sítím. Řeší omezení tradičních OSS/BSS systémů definováním standardizovaného, intent-based řídicího interface, který odděluje 'co' (service intent) od 'jak' (orchestration details), což je klíčové pro multi-vendor, cloud-nativní prostředí.

## Klíčové vlastnosti

- Automatizovaná instanciace, konfigurace a ukončení NF, NS a Slice
- Elastické škálování (horizontální a vertikální) na základě výkonnostních metrik
- Management softwarových aktualizací a upgrade s možností rollbacku
- Integrované procedury obnovy z chyb a healing
- End-to-end řízení přes více administrativních a technologických domén
- Standardizované interface a datové modely pro interoperabilitu

## Související pojmy

- [NFV – Network Functions Virtualization](/mobilnisite/slovnik/nfv/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 28.500** (Rel-19) — Management of Virtualized Network Functions
- **TS 28.533** (Rel-19) — Management and orchestration; Architecture framework
- **TR 28.834** (Rel-18) — Technical Report
- **TS 28.869** (Rel-20) — Study on cloud aspects of management and orchestration
- **TS 28.890** (Rel-16) — ONAP-3GPP 5G Management Compatibility Study
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface

---

📖 **Anglický originál a plná specifikace:** [LCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcm/)
