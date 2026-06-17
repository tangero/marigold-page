---
slug: "hfl"
url: "/mobilnisite/slovnik/hfl/"
type: "slovnik"
title: "HFL – Horizontal Federated Learning"
date: 2026-01-01
abbr: "HFL"
fullName: "Horizontal Federated Learning"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hfl/"
summary: "Horizontal Federated Learning (HFL) je distribuovaný framework strojového učení standardizovaný v 3GPP, který umožňuje kolaborativní trénování modelů na více síťových uzlech nebo uživatelských zařízen"
---

HFL je standardizovaný distribuovaný framework strojového učení v 3GPP pro kolaborativní trénování modelů napříč síťovými uzly nebo zařízeními, který chrání soukromí tím, že sdílí pouze aktualizace modelu namísto nezpracovaných dat.

## Popis

Horizontal Federated Learning (HFL) je decentralizovaný paradigma strojového učení standardizovaný 3GPP, který usnadňuje kolaborativní trénování modelů napříč distribuovanými entitami, jako jsou uživatelská zařízení (UE), základnové stanice (gNB) nebo síťové funkce, bez výměny nezpracovaných dat. Architektura typicky zahrnuje centrální server, známý jako agregátor nebo federovaný server, a více účastnících se klientů. Každý klient natrénuje lokální model strojového učení na své vlastní datové sadě a zašle agregátoru pouze aktualizace modelu (např. gradienty, váhy). Agregátor tyto aktualizace následně zkombinuje – běžně za použití algoritmů jako Federated Averaging (FedAvg) – aby vytvořil vylepšený globální model, který je redistribuován klientům pro další kola tréninku. Tento iterativní proces pokračuje, dokud model nedosáhne požadované úrovně výkonu, což umožňuje kolektivní inteligenci sítě při zachování lokalizace citlivých dat.

Technický pracovní postup v kontextu 3GPP zahrnuje specifické procedury pro výběr klientů, zabezpečený přenos aktualizací a koordinaci agregace. Mezi klíčové komponenty patří Federated Learning Management Function (FLMF), která orchestraci procesu tréninku, a zabezpečené komunikační kanály, často využívající existující bezpečnostní mechanismy 3GPP. FLMF řeší úkoly jako autentizace účastníků, alokace prostředků a plánování agregace. Aktualizace modelu se přenášejí přes standardizovaná rozhraní s ohledem na efektivitu šířky pásma a latenci, zejména v bezprostředních prostředích. Soukromí je vynucováno technikami jako diferenciální soukromí nebo secure multi-party computation, které mohou být integrovány, aby zabránily odvození nezpracovaných dat z aktualizací.

Úloha HFL v mobilních sítích spočívá v umožnění pokročilých, daty řízených aplikací, jako je správa rádiových prostředků, predikce mobility a optimalizace síťového řezání, bez narušení soukromí uživatelů nebo vzniku masivních nákladů na přenos dat. Distribucí výpočetního zatížení také ulehčuje zátěž centrálních cloudových prostředků. Specifikace 3GPP definují potřebné protokoly, rozhraní a bezpečnostní frameworky, které zajišťují interoperabilitu a spolehlivý provoz napříč různými dodavateli a síťovými nasazeními, čímž se HFL stává základní technologií pro budoucí AI-nativní sítě.

## K čemu slouží

Horizontal Federated Learning byl zaveden, aby řešil rostoucí potřebu inteligentní automatizace sítě a personalizovaných služeb při současném dodržování přísných předpisů na ochranu dat, jako je GDPR. Tradiční centralizované přístupy strojového učení vyžadují agregaci obrovského množství uživatelských dat na centrálním serveru, což přináší významné obavy o soukromí, problémy s právní shodou a bezpečnostní rizika z úniků dat. HFL odstraňuje potřebu centralizace nezpracovaných dat a umožňuje trénování modelů na decentralizovaných zdrojích dat, což je obzvláště kritické v telekomunikacích, kde jsou uživatelská data vysoce citlivá a geograficky rozptýlená.

Motivace pro standardizaci HFL v 3GPP vychází z posunu průmyslu k AI-řízeným sítím (např. v 5G-Advanced a 6G), které vyžadují rozhodování v reálném čase s ohledem na kontext. Předchozí přístupy postrádaly jednotný framework pro zabezpečené a efektivní federované učení v mobilním prostředí, což vedlo k proprietárním řešením a problémům s interoperabilitou. HFL poskytuje standardizovanou metodu, jak využít kolektivní data z milionů zařízení a síťových uzlů ke zlepšení výkonu sítě, energetické účinnosti a uživatelského zážitku bez kompromisů v soukromí. Umožňuje nové případy užití, jako je kolaborativní detekce narušení nebo predikce kvality zážitku, které byly dříve neproveditelné kvůli datovým silům a omezením soukromí.

## Klíčové vlastnosti

- Decentralizované trénování modelů bez výměny nezpracovaných dat
- Ochrana soukromí sdílením pouze aktualizací modelu
- Podpora iterativních agregačních algoritmů, jako je Federated Averaging
- Integrace s bezpečnostními frameworky 3GPP pro zabezpečenou komunikaci
- Orchestrace funkcí Federated Learning Management Function (FLMF)
- Úsporný provoz vhodný pro prostředí s omezenými bezdrátovými prostředky

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.288** (Rel-20) — 5GS Architecture Enhancements for Data Analytics
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.560** (Rel-19) — AIML Enablement (AIMLE) Services Stage 3 Protocol
- **TS 28.105** (Rel-19) — AI/ML Management for 5GS
- **TS 28.858** (Rel-19) — AI/ML Management Phase 2 Study
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [HFL na 3GPP Explorer](https://3gpp-explorer.com/glossary/hfl/)
