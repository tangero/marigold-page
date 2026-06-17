---
slug: "duck"
url: "/mobilnisite/slovnik/duck/"
type: "slovnik"
title: "DUCK – Discovery User Confidentiality Key"
date: 2025-01-01
abbr: "DUCK"
fullName: "Discovery User Confidentiality Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/duck/"
summary: "Kryptografický klíč používaný v službách pro komunikaci na krátkou vzdálenost (ProSe) k zajištění důvěrnosti zpráv přenášených při objevování mezi zařízeními. Ochraňuje identitu uživatele a informace"
---

DUCK je kryptografický klíč používaný v ProSe k zajištění důvěrnosti zpráv a ochraně identity uživatele při objevování mezi zařízeními (device-to-device) v LTE a 5G sítích.

## Popis

Klíč důvěrnosti pro objevování uživatele (Discovery User Confidentiality Key, DUCK) je bezpečnostní klíč definovaný v architektuře 3GPP pro služby na krátkou vzdálenost (ProSe). Je odvozen jako část klíčové hierarchie speciálně pro ochranu komunikace související s objevováním mezi uživatelskými zařízeními (UE), které fungují v režimu přímé komunikace mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)) nebo přes síť. Primárním účelem DUCK je poskytnout ochranu důvěrnosti pro zprávy objevování, což jsou signály nebo oznámení vysílána UE, aby její přítomnost nebo služby byly známé ostatním blízkým UE. Bez takové ochrany by tyto zprávy mohly odhalit citlivé informace o identitě, poloze nebo záměru uživatele.

DUCK je generován pomocí funkce odvození klíče ([KDF](/mobilnisite/slovnik/kdf/)) specifikované v 3GPP TS 33.220. Jeho odvození typicky využívá kořenový klíč sdílený mezi UE a síť (například klíč K_ProSe) spolu s dalšími vstupními parametry, jako je ProSe Application Code a identifikátor účelu klíče. Po odvození je DUCK používán v protokolové struktuře ProSe v UE. Když UE chce odeslat zabezpečenou zprávu objevování, použije DUCK k zašifrování obsahu oznámení nebo vyzvání objevování. Odpovídající přijímající UE, které odvodily stejný DUCK (na základě sdílených parametrů poskytnutých síť nebo přímého nastavení), mohou zprávu dešifrovat a zpracovat informace objevování. Tento proces zajišťuje, že pouze autorizované UE účastnící se stejné relace objevování mohou pochopit obsah.

Architektonicky je DUCK řízen funkcí ProSe v síti a zabezpečeně poskytován autorizovaným UE. Funguje spolu s klíčem integrity pro objevování uživatele ([DUIK](/mobilnisite/slovnik/duik/)), který poskytuje ochranu integrity. Kombinace DUCK a DUIK vytváří kompletní bezpečnostní sadu pro signalizaci objevování. Životní cyklus klíče je spojen s relací objevování nebo platností klíče vyšší vrstvy. Jeho použití je detailně popsáno ve specifikacích řídících protokolové vrstvy ProSe (24.334) a bezpečnostní architekturu (33.503). DUCK je klíčovým prvkem pro zabezpečené komerční služby nalezení a připojení a, což je ještě důležitější, pro komunikaci veřejné bezpečnosti, kde objevování mezi prvními respondery musí být spolehlivé a důvěrné.

## K čemu slouží

DUCK byl uveden v 3GPP Release 13 k řešení bezpečnostních požadavků nově standardizovaných služeb na krátkou vzdálenost (ProSe). ProSe umožňuje přímou komunikaci mezi zařízeními, což je změna paradigmatu od tradičních mobilních sítí, kde všechna data prochází přes základnovou stanici. Jednou ze základních operací v ProSe je objevování – proces, při kterém zařízení najdou jedno druhé. Raná práce na ProSe identifikovala, že zprávy objevování, pokud jsou odesílány v nezašifrované formě, by představovala významné riziko pro soukromí a bezpečnost, potenciálně odhalující identitu uživatelů a umožňující sledování nebo podvržení.

Vytvoření DUCK bylo motivováno potřebou poskytnout důvěrnost těchto procedur objevování, obzvláště pro aplikace jako veřejná bezpečnost, kde komunikace musí být zabezpečená proti odposlechu. Před ProSe se bezpečnost mobilních sítí zaměřovala na spojení UE-síť. Objevování [D2D](/mobilnisite/slovnik/d2d/) vyžadoval nový bezpečnostní model pro přímé spojení UE-UE. DUCK, jako část specializované klíčové hierarchie ProSe, řešil problém, jak efektivně a bezpečně zašifrovat obsah objevování bez nutnosti předchozího přímého zabezpečeného spojení mezi objevujícími zařízeními. Umožnil síti delegovat kryptografickou schopnost zařízením pro provoz mimo síť, což je klíčová funkce pro scénáře veřejné bezpečnosti, kde síťová infrastruktura může být nedostupná. DUCK tedy zaplnil kritickou mezeru v bezpečnostní architektuře, umožňující důvěryhodné objevování jako předpoklad zabezpečené D2D komunikace.

## Klíčové vlastnosti

- Poskytuje ochranu důvěrnosti pro zprávy přímého objevování ProSe
- Odvozen z kořenového klíče v klíčové hierarchii ProSe pomocí standardizované KDF
- Používá se k zašifrování obsahu oznámení a vyzvání objevování
- Umožňuje soukromí tím, že ochraňuje identitu uživatele a informace o službách od neautorizovaných zařízení
- Funguje v síťově koordinovaných i samostatných (mimo síť) scénářích ProSe
- Spravován a poskytován síťovou funkcí ProSe

## Definující specifikace

- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.555** (Rel-19) — 5G ProSe UE Policies Specification
- **TS 29.345** (Rel-19) — Diameter-based PC6/PC7 interfaces for ProSe
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TS 33.843** (Rel-15) — Security Study for ProSe UE-to-Network Relay

---

📖 **Anglický originál a plná specifikace:** [DUCK na 3GPP Explorer](https://3gpp-explorer.com/glossary/duck/)
