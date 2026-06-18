---
slug: "pine"
url: "/mobilnisite/slovnik/pine/"
type: "slovnik"
title: "PINE – PIN Element"
date: 2026-01-01
abbr: "PINE"
fullName: "PIN Element"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pine/"
summary: "PINE (PIN Element) je bezpečnostní komponenta zavedená ve specifikaci 3GPP Release 18 pro správu přihlašovacích údajů typu PIN (Personal Identification Number) v systémech 5G. Poskytuje standardizovan"
---

PINE je bezpečnostní komponenta zavedená ve specifikaci 3GPP Release 18, která poskytuje standardizovaný rámec pro správu a ověřování přihlašovacích údajů typu PIN (osobní identifikační číslo) v systémech 5G.

## Popis

[PIN](/mobilnisite/slovnik/pin/) Element (PINE) je funkční entita definovaná v rámci architektury systému 5G pro zpracování operací souvisejících s PIN. Slouží jako zabezpečené úložiště a zpracovatelská jednotka pro přihlašovací údaje PIN spojené s uživatelským zařízením (UE) nebo univerzálním účastnickým identifikačním modulem ([USIM](/mobilnisite/slovnik/usim/)). PINE komunikuje s dalšími síťovými funkcemi, jako je funkce autentizačního serveru ([AUSF](/mobilnisite/slovnik/ausf/)) a jednotná správa dat ([UDM](/mobilnisite/slovnik/udm/)), aby umožnila ověření PIN během autentizačních procedur nebo pro autorizaci konkrétních služeb, které vyžadují dodatečnou vrstvu ověření uživatele nad rámec standardní síťové autentizace.

Z architektonického hlediska je PINE specifikována tak, aby podporovala různé typy PIN, včetně tradičního PIN pro přístup k USIM a potenciálně nových způsobů využití PIN pro zamykání aplikací nebo služeb v rámci ekosystému 5G. Její provoz zahrnuje zabezpečené protokoly pro přenos žádostí a odpovědí pro ověření PIN, což zajišťuje ochranu dat PIN před odposlechem a neoprávněnou manipulací. Specifikace podrobně popisují procedury pro povolení, zakázání, změnu a odblokování PIN, přičemž tyto funkce správy životního cyklu integrují do širšího bezpečnostního rámce 5G.

Úlohou PINE je oddělit logiku správy PIN od základních autentizačních funkcí, což umožňuje flexibilnější a robustnější implementace zabezpečení. Standardizací tohoto prvku zajišťuje 3GPP interoperabilitu mezi různými výrobci síťových zařízení a výrobci UE. Podporuje scénáře, kdy se uživatel musí ověřit pomocí PIN pro přístup k citlivým síťovým službám nebo k provedení kritických operací, čímž přidává uživatelsky orientovanou bezpečnostní vrstvu, která doplňuje síťově orientovanou autentizaci poskytovanou protokoly 5G-AKA nebo EAP-AKA'.

## K čemu slouží

PINE byla vytvořena, aby řešila potřebu standardizovaného síťového rámce pro správu [PIN](/mobilnisite/slovnik/pin/) v 5G. Před Release 18 bylo nakládání s PIN z velké části omezeno na UE a [USIM](/mobilnisite/slovnik/usim/), s minimálním zapojením sítě pro služby vyžadující ověření PIN. Tento nedostatek standardizace ztěžoval implementaci konzistentní a bezpečné autorizace služeb založené na PIN napříč vícevýrobkovými sítěmi a pro nově vznikající služby 5G, jako je zabezpečená správa IoT zařízení nebo rodičovské kontroly.

Motivace vychází z vývoje služeb 5G, které stále více vyžadují detailní souhlas a ověření uživatele. Například rodič může chtít uzamknout určité datové služby na zařízení dítěte pomocí PIN, nebo podnik může vyžadovat ověření PIN předtím, než zařízení získá přístup k podnikovým síťovým řezům. PINE poskytuje architektonické rozhraní v jádrové síti pro zabezpečenou a spolehlivou podporu takových případů užití. Řeší problém fragmentovaných proprietárních implementací definováním jasných rozhraní a procedur v rámci jádra 5G, jak je popsáno ve specifikacích jako 23.501 a 33.127.

Historicky byly PIN primárně funkcí USIM/UICC pro odemykání zařízení. PINE rozšiřuje tento koncept do síťové domény a umožňuje poskytovatelům služeb nabízet rozšířené bezpečnostní funkce. Řeší omezení, kdy síť neměla standardizovaný způsob, jak ověřit uživateli známé tajemství pro autorizaci akcí na úrovni služeb, a tím překlenuje mezeru mezi ověřováním uživatele a autorizací služeb v bezpečnostním modelu 5G.

## Klíčové vlastnosti

- Standardizovaná síťová funkce pro správu a ověřování přihlašovacích údajů typu PIN
- Podpora více typů PIN a scénářů použití nad rámec přístupu k USIM
- Zabezpečená rozhraní k jádrovým síťovým funkcím, jako jsou AUSF a UDM
- Definované procedury pro správu životního cyklu PIN (povolení, změna, odblokování)
- Posiluje autorizaci na úrovni služeb pomocí dodatečného faktoru ověřeného uživatelem
- Podporuje interoperabilitu v vícevýrobkových nasazeních sítí 5G

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.542** (Rel-20) — Application layer support for Personal IoT Network
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.583** (Rel-19) — Application Layer Support for Personal IoT Network
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TR 33.882** (Rel-18) — Technical Report on 5G Security for Personal IoT Networks

---

📖 **Anglický originál a plná specifikace:** [PINE na 3GPP Explorer](https://3gpp-explorer.com/glossary/pine/)
