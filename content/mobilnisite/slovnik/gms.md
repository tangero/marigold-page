---
slug: "gms"
url: "/mobilnisite/slovnik/gms/"
type: "slovnik"
title: "GMS – Group Management Server"
date: 2026-01-01
abbr: "GMS"
fullName: "Group Management Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gms/"
summary: "Funkce jádra sítě pro správu služeb skupinové komunikace, jako je Mission Critical Push-to-Talk (MCPTT). Zajišťuje správu členství ve skupinách, jejich konfiguraci a autorizaci služeb, což umožňuje ef"
---

GMS je funkce jádra sítě, která spravuje služby skupinové komunikace tím, že zajišťuje správu členství ve skupinách, jejich konfiguraci a autorizaci služeb.

## Popis

Group Management Server (GMS) je klíčová funkční entita v architektuře 3GPP pro služby pro zásahové řízení (Mission Critical Services – [MCS](/mobilnisite/slovnik/mcs/)), standardizovaná jako součást frameworku Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)). Funguje ve vrstvě služeb, odděleně od podkladové IP Multimedia Subsystem (IMS) nebo Evolved Packet Core (EPC)/5G Core (5GC), a je zodpovědná za centralizovanou správu skupin. Skupina je základní konstrukcí v MCPTT, která definuje sadu uživatelů oprávněných vzájemně komunikovat. GMS udržuje trvalou databázi všech skupin, jejich členů a přidružených atributů, jako je identita skupiny, úrovně priority, politiky řízení přístupu k vysílání (floor control) a geografické rozsahy.

Z architektonického hlediska GMS komunikuje s několika dalšími funkcemi MCPTT. Komunikuje s MCPTT Application Server ([AS](/mobilnisite/slovnik/as/)), aby poskytl konfigurační data skupin potřebná pro zřizování a řízení skupinových relací. Také komunikuje s Key Management Server ([KMS](/mobilnisite/slovnik/kms/)) pro distribuci bezpečnostních klíčů specifických pro skupiny a s Configuration Server pro provizionování. GMS zpřístupňuje rozhraní směrem k vyšším vrstvám (např. rozhraní Mcx) pro externí správu autorizovanými administrátory nebo systémy, což umožňuje vytváření, modifikaci a mazání skupin a členství. Jeho provoz je definován jako vysoce spolehlivý a dostupný, neboť je klíčový pro nouzové a zásahové operace.

Z procesního hlediska je GMS zapojen vždy, když uživatel zahájí nebo se připojí ke skupinovému hovoru. MCPTT klient nebo AS dotazuje GMS za účelem ověření členství uživatele a získání operačních parametrů skupiny. GMS také spravuje dynamické přidružení ke skupinám, kdy se uživatelé mohou v reálném čase připojovat ke skupinám nebo je opouštět na základě své role nebo situace. Podporuje složité hierarchie skupin, včetně podskupin a hovorových skupin, a může vynucovat politiky založené na prioritě uživatele, právech na přednostní přístup a stavu nouze. GMS v podstatě funguje jako autoritativní zdroj pravdy pro definice skupin, což zajišťuje, že komunikace je organizovaná, zabezpečená a dodržuje předem definovaná operační pravidla služby pro zásahové řízení.

## K čemu slouží

GMS byl vytvořen, aby řešil specifické a přísné požadavky profesionální komunikace a komunikace složek integrovaného záchranného systému, které jsou z velké části závislé na okamžité, spolehlivé a organizované skupinové komunikaci. Tradiční mobilní služby, jako jsou hlasové hovory nebo SMS, byly navrženy pro komunikaci jeden na jednoho a postrádají strukturovanou správu skupin, zpracování priorit a zabezpečení potřebné pro koordinovaný týmový zásah v nouzových situacích. Před jeho standardizací proprietární systémy, jako je Terrestrial Trunked Radio (TETRA), nabízely skupinové funkce, ale byly izolované, drahé a neintegrované se širokopásmovými mobilními sítěmi.

Zavedení GMS v rámci frameworku služeb pro zásahové řízení (Mission Critical Services) 3GPP umožňuje složkám integrovaného záchranného systému využívat komerční sítě 3GPP (4G LTE a 5G) pro kritickou komunikaci. Řeší problém škálovatelné, bezpečné a spravovatelné skupinové komunikace přes IP sítě. Centralizací správy skupin odstraňuje potřebu, aby si každý aplikační server nebo klient udržoval vlastní nekonzistentní seznamy skupin, a zajišťuje tak jednotnost a bezpečnost v celé oblasti pokrytí služby. Jeho vznik byl motivován globálními iniciativami, jako jsou ty vedené First Responder Network Authority (FirstNet) a European Telecommunications Standards Institute ([ETSI](/mobilnisite/slovnik/etsi/)), za účelem vývoje standardizovaných, interoperabilních a budoucím potřebám odpovídajících řešení pro kritickou komunikaci.

## Klíčové vlastnosti

- Centralizovaná správa definic skupin, členství a atributů
- Integrace s MCPTT Application Server pro řízení relací a vynucování politik
- Podpora dynamického přidružení a odpojení od skupin v reálném čase
- Vynucování bezpečnostních politik založených na skupinách a koordinace správy klíčů
- Poskytování geografického rozsahu a politik skupin založených na poloze
- Správa hierarchií skupin, podskupin a hovorových skupin

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.781** (Rel-15) — Study on MC services migration & interconnection
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 23.784** (Rel-16) — Discreet Listening for Mission Critical Services
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.879** (Rel-13) — MCPTT Security Study
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [GMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/gms/)
