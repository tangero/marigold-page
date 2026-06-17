---
slug: "mveg"
url: "/mobilnisite/slovnik/mveg/"
type: "slovnik"
title: "MVEG – MCVideo Emergency Group"
date: 2025-01-01
abbr: "MVEG"
fullName: "MCVideo Emergency Group"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mveg/"
summary: "Předdefinovaná nebo dynamicky vytvořená skupina uživatelů MCVideo určená k přijímání nouzových video upozornění a komunikací. Slouží jako cílový subjekt pro MVEA a MVEGC, čímž zajišťuje, že kritické v"
---

MVEG je předdefinovaná nebo dynamicky vytvořená skupina uživatelů MCVideo určená k přijímání nouzových video upozornění a komunikací, která zajišťuje, že kritické informace dorazí k příslušnému personálu, jako jsou hasiči nebo policisté, během incidentu.

## Popis

[MCVideo](/mobilnisite/slovnik/mcvideo/) Emergency Group (MVEG) je funkční entita v rámci architektury 3GPP Mission Critical Video (MCVideo), která představuje soubor uživatelů oprávněných účastnit se nouzových videokomunikací. Jedná se o specializovaný typ skupiny spravovaný systémem správy skupin (Group Management System), který je součástí architektury služby MCVideo. MVEG může být staticky předem nakonfigurována (např. jako seznam všech záchranářů ve městě) nebo dynamicky vytvořena v reakci na probíhající mimořádnou událost na základě kritérií, jako je geografická poloha, role nebo dostupnost. Skupina se používá jako distribuční seznam pro MCVideo Emergency Alerts ([MVEA](/mobilnisite/slovnik/mvea/)) a jako soubor účastníků pro MCVideo Emergency Group Calls ([MVEGC](/mobilnisite/slovnik/mvegc/)), což zajišťuje cílené doručování videokomunikací.

Z architektonického hlediska je MVEG udržována aplikačním serverem MCVideo, který komunikuje se systémem správy skupin. Tento systém ukládá definice skupin, seznamy členů a zásady (např. kdo se může připojit, iniciovat hovory nebo přijímat upozornění). Data skupiny mohou být poskytována síťovými operátory nebo bezpečnostními složkami, často integrovaná s externími databázemi, jako jsou systémy pro správu personálu. Když dojde k mimořádné události, server MCVideo dotazuje systém správy skupin, aby určil členství v MVEG, což může zahrnovat aktualizace polohy v reálném čase od sítě. Identita skupiny je typicky reprezentována jedinečným identifikátorem, jako je Group ID, který se používá v signalizačních protokolech, jako je Session Initiation Protocol (SIP), pro zřizování relací založených na IMS.

Fungování MVEG zahrnuje několik procesů. Během poskytování služby správci skupin definují parametry MVEG, včetně názvu, účelu a seznamu členů. Při provozu, když je iniciována MVEA nebo MVEGC, server MCVideo ověří, že iniciátor je pro danou konkrétní MVEG autorizován, a poté načte aktuální seznam členů. U dynamických skupin může server použít funkce síťové expozice (network exposure functions) k získání poloh nebo stavů uživatelů v reálném čase od 5G jádra sítě. Server následně orchestruje komunikační relaci a zajišťuje, že je upozorněno zařízení každého člena a že se může připojit. Role MVEG v síti spočívá v poskytování škálovatelného a spravovatelného způsobu organizace uživatelů pro nouzové videoslužby, což je nezbytné pro koordinované zásahy, snížení komunikačního šumu a zajištění, že kritické informace obdrží pouze relevantní personál, čímž se zvyšuje provozní efektivita a bezpečnost.

## K čemu slouží

MVEG byla vytvořena za účelem řešení organizačních výzev v nouzových videokomunikacích, kde ad-hoc koordinace může vést ke zpožděním a ztrátě informací. Před její standardizací byly nouzové skupiny často spravovány manuálně prostřednictvím rádiových kanálů nebo jednoduchých seznamů kontaktů, které byly nepružné a náchylné k chybám ve stresových situacích. Mezi omezení patřily potíže s aktualizací členů v reálném čase, nedostatečná integrace se síťovými lokalizačními službami a absence standardizovaného způsobu propojení skupin s multimediálními upozorněními. To bránilo efektivnímu hromadnému oznamování a skupinovému volání v kritických scénářích.

Motivace pro MVEG vzešla z potřeby využít digitální správu skupin v širokopásmových sítích pro veřejnou bezpečnost. Jak se služby Mission Critical Services rozvíjely a zahrnovaly video, bylo zřejmé, že statické skupiny jsou nedostatečné pro dynamické mimořádné události, kdy se polohy a role zasahujících jednotek rychle mění. MVEG umožňuje automatizované vytváření skupin na základě kritérií – například vytvoření skupiny všech policejních důstojníků v okruhu 1 kilometru od incidentu. To zajišťuje, že upozornění a hovory dorazí přesně k těm, kdo je potřebují, čímž se zlepšuje povědomí o situaci a rychlost zásahu.

Historicky byla správa skupin v zastaralých systémech [LMR](/mobilnisite/slovnik/lmr/) omezená a závislá na dodavateli. 3GPP standardizovala MVEG jako součást [MCVideo](/mobilnisite/slovnik/mcvideo/), aby zajistila interoperabilitu napříč různými sítěmi a zařízeními, což je klíčové pro operace více složek. Řeší problém neefektivní komunikace tím, že poskytuje strukturovanou, síťově informovanou skupinovou entitu, která se integruje s dalšími komponentami [MCS](/mobilnisite/slovnik/mcs/). Definováním MVEG umožnila 3GPP škálovatelné nouzové videoslužby, které se mohou přizpůsobit podmínkám v reálném čase, a tím v konečném důsledku podporovat rychlejší a přesnější nouzové zásahy v moderní komunikaci pro veřejnou bezpečnost.

## Klíčové vlastnosti

- Statické nebo dynamické vytváření skupin na základě předdefinovaných kritérií (např. role, poloha)
- Integrace se systémem správy skupin (Group Management System) pro centralizovanou správu
- Aktualizace členství v reálném čase s využitím síťových informací o poloze a stavu
- Autorizační zásady řídící, kdo může iniciovat upozornění nebo hovory pro skupinu
- Jedinečný Group ID pro identifikaci v síťové signalizaci a řízení relací
- Interoperabilita s dalšími typy skupin MCS (např. skupiny MCPTT)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MVEG na 3GPP Explorer](https://3gpp-explorer.com/glossary/mveg/)
