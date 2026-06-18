---
slug: "mcptt"
url: "/mobilnisite/slovnik/mcptt/"
type: "slovnik"
title: "MCPTT – Mission Critical Push to Talk Identity"
date: 2026-01-01
abbr: "MCPTT"
fullName: "Mission Critical Push to Talk Identity"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mcptt/"
summary: "Jedinečný identifikátor v rámci služebního rámce 3GPP Mission Critical Push to Talk, který slouží k ověřování a autorizaci uživatelů a skupin pro zabezpečenou skupinovou komunikaci s nízkou latencí. J"
---

MCPTT je jedinečný identifikátor v rámci služebního rámce 3GPP Mission Critical Push to Talk, který slouží k ověřování a autorizaci uživatelů a skupin pro zabezpečenou skupinovou komunikaci s nízkou latencí přes sítě LTE/5G.

## Popis

Mission Critical Push to Talk Identity (MCPTT ID) je klíčový prvek v architektuře služeb Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)) dle 3GPP, konkrétně definovaný pro službu MCPTT. Slouží jako jedinečný a trvalý identifikátor přiřazený uživateli služby MCPTT (např. záchranáři) nebo skupině MCPTT. Tato identita se používá napříč servisní vrstvou pro ověřování, autorizaci, poskytování služeb a směrování komunikace typu push-to-talk. MCPTT ID je odlišný od jiných identifikátorů 3GPP (jako [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/)), ale může s nimi být asociován, a je spravován v domovské síti služby MCPTT.

Z architektonického hlediska MCPTT ID využívá několik funkčních entit definovaných ve specifikacích 3GPP. Klient MCPTT, který běží na uživatelském zařízení (UE), je tímto identifikátorem konfigurován. Při registraci klient MCPTT předkládá MCPTT ID platformě služby MCPTT, která zahrnuje komponenty jako MCPTT Server, MCPTT Application Server a entity pro správu klíčů. Identita je ověřována proti předplatitelským datům uloženým v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo v dedikované databázi MCPTT. Pro skupinovou komunikaci se používají MCPTT Group ID k definování hovorových skupin a MCPTT ID určuje členství uživatele a jeho oprávnění v těchto skupinách (např. dispečer, práva pro řízení přístupu ke slovu).

Jak to funguje: identita je vložena do signalizačních zpráv (pomocí protokolů jako [SIP](/mobilnisite/slovnik/sip/) a [HTTP](/mobilnisite/slovnik/http/)) pro všechny procedury MCPTT: registraci, přidružení ke skupině, zahájení hovoru (žádost o slovo) a nouzové hovory. Zabezpečení je prvořadé; MCPTT ID je klíčovým vstupem pro procedury ověřování a dohody o klíči, což zajišťuje, že ke službě mají přístup pouze autorizovaní uživatelé. Umožňuje také funkce jako priorita a přednostní přerušení na základě identity, kdy může MCPTT ID uživatele s vysokou prioritou zajistit okamžitý přístup k síťovým prostředkům při přetížení. Identita zůstává konzistentní napříč relacemi a je klíčová pro zákonné odposlechy a logování pro účely odpovědnosti ve službách veřejné bezpečnosti.

## K čemu slouží

Identita MCPTT byla vytvořena, aby splňovala přísné požadavky profesionální a veřejné bezpečnostní komunikace při přechodu ze starších systémů Land Mobile Radio ([LMR](/mobilnisite/slovnik/lmr/)), jako jsou [TETRA](/mobilnisite/slovnik/tetra/) nebo P25, na širokopásmové sítě založené na 3GPP (LTE, 5G). Starší systémy měly své vlastní proprietární modely identity a zabezpečení. Standardizovaný a bezpečný rámec pro identitu byl nezbytný k umožnění interoperability mezi řešeními MCPTT od různých dodavatelů a k tomu, aby uživatelé veřejné bezpečnosti mohli přecházet na navštívené sítě při zachování svého služebního profilu a autorizace.

Omezení použití obecných mobilních identifikátorů (jako telefonních čísel) pro služby kritické pro plnění mise byla významná. Tyto identifikátory postrádaly dostatečnou podrobnost pro správu skupin, nepodporovaly nativně služebně specifické ověřování a nedaly se snadno použít pro zakódování uživatelských rolí nebo priorit. MCPTT ID tyto problémy řeší tím, že poskytuje identitu na servisní vrstvě přímo uzpůsobenou pro službu push-to-talk. Umožňuje zabezpečený a ověřený přístup ke službě MCPTT, podporuje dynamickou správu skupin a tvoří základ pro pokročilé funkce jako nouzové varování, inherentní uživatelskou prioritu a zabezpečenou skupinovou komunikaci end-to-end. Její vytvoření bylo motivováno potřebou spolehlivého, standardizovaného a bezpečného mechanismu identity, který je nedílnou součástí toho, aby se LTE/5G staly životaschopnou náhradou tradičních sítí PMR.

## Klíčové vlastnosti

- Jedinečný identifikátor pro uživatele a skupiny MCPTT v rámci služebního rámce 3GPP
- Základ pro ověřování a autorizaci ve službách Mission Critical Push to Talk
- Umožňuje dynamické přidružení ke skupině a správu hovorových skupin
- Podporuje mechanismy uživatelské priority a přednostního přerušení na základě identity
- Klíčový pro zabezpečenou signalizaci a odvození šifrovacích klíčů pro média
- Umožňuje roaming a interoperabilitu mezi různými poskytovateli služeb MCPTT

## Definující specifikace

- **TS 22.179** (Rel-20) — MCPTT Service Requirements
- **TS 22.280** (Rel-20) — Mission Critical Services Common Requirements
- **TS 22.281** (Rel-19) — Mission Critical Video (MCVideo) Service Requirements
- **TR 22.879** (Rel-14) — Mission Critical Video over LTE Feasibility Study
- **TS 22.880** (Rel-14) — Mission Critical Data Communications Study
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.741** (Rel-13) — MBMS/GCSE_LTE Architecture Enhancements Study
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TR 23.781** (Rel-15) — Study on MC services migration & interconnection
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- … a dalších 39 specifikací

---

📖 **Anglický originál a plná specifikace:** [MCPTT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcptt/)
