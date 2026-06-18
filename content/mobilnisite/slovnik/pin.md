---
slug: "pin"
url: "/mobilnisite/slovnik/pin/"
type: "slovnik"
title: "PIN – Personal Identification Number"
date: 2026-01-01
abbr: "PIN"
fullName: "Personal Identification Number"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pin/"
summary: "Personal Identification Number (PIN) je číselné heslo používané k autentizaci uživatele vůči mobilnímu zařízení nebo síťové službě. Ve specifikacích 3GPP PIN zabezpečuje SIM/USIM karty, přístup k zaří"
---

PIN je číselné heslo používané ve specifikacích 3GPP pro autentizaci uživatele a zabezpečení SIM/USIM karet, přístupu k zařízení a síťovým službám, čímž brání neoprávněnému použití.

## Popis

Personal Identification Number (PIN) je klíčový bezpečnostní koncept v systémech 3GPP, který slouží jako tajný číselný kód používaný pro autentizaci a řízení přístupu. Primárně je spojován s modulem účastnické identity ([SIM](/mobilnisite/slovnik/sim/)) nebo univerzálním SIM ([USIM](/mobilnisite/slovnik/usim/)) vloženým do mobilního zařízení. PIN uzamýká samotnou SIM/USIM kartu; pokud je funkce aktivována, uživatel musí zadat správný PIN k odemknutí karty a umožnit mobilnímu zařízení přístup k síťovým službám na ní uloženým. Tím se zabrání neoprávněnému použití SIM při ztrátě nebo odcizení zařízení. Typicky existují dva PINy: PIN1 (standardní PIN) a PIN2 (používaný pro určité pokročilé funkce, jako jsou pevně volaná čísla). PIN je bezpečně uložen na SIM/USIM a je ověřován lokálně kartou; nepřenáší se přes síť, což zvyšuje bezpečnost. Kromě uzamčení SIM se koncept PINu rozšiřuje i na přístup ke službám, například autentizaci PINem pro přidané služby nebo jako součást schémat dvoufaktorové autentizace. Správa PINů zahrnuje možnosti povolení/zákazu kontroly PINu, změnu PINu a řešení jeho odblokování pomocí [PUK](/mobilnisite/slovnik/puk/) (PIN Unblocking Key), pokud je PIN zadán nesprávně příliš mnohokrát. Z architektonického hlediska se ověření PINu provádí mezi mobilním zařízením ([ME](/mobilnisite/slovnik/me/)) a SIM/USIM prostřednictvím standardizovaných příkazů (např. ENTER PIN). Síťový operátor může nastavit počáteční hodnoty PIN a PUK. PINy jsou kritickým prvkem bezpečnostního rámce 3GPP, který chrání identitu účastníka a údaje o předplatném na fyzické úrovni karty.

## K čemu slouží

PIN byl zaveden od nejstarších vydání GSM (Rel-2) k řešení základního bezpečnostního problému ochrany fyzické [SIM](/mobilnisite/slovnik/sim/) karty a identity účastníka. Bez PINu by mohla být SIM karta volně použita v jakémkoli zařízení, což by vedlo k podvodům a neoprávněnému přístupu k síťovým službám. PIN poskytuje jednoduchou, uživatelem spravovanou vrstvu ochrany předplatného. Řeší problém krádeže nebo ztráty zařízení tím, že zajišťuje uzamčení samotné SIM. S jednotlivými vydáními se koncept PINu vyvinul, aby podporoval složitější služby a možnosti správy, což odráží jeho úlohu základního, ale zásadního autentizačního prvku. Jeho přetrvávání ve všech vydáních zdůrazňuje jeho trvalý význam v mobilní bezpečnosti, a to i s nástupem pokročilejších metod autentizace, jako je biometrie. Rozsáhlý seznam specifikací odkazujících na PIN poukazuje na jeho integraci do správy předplatného, přístupu ke službám, správy zařízení a bezpečnostních procedur.

## Klíčové vlastnosti

- Autentizace pro odemknutí SIM/USIM karty
- Lokální ověření na SIM bez přenosu přes síť
- Dva typy: PIN1 pro obecný přístup, PIN2 pro specifické funkce
- Přidružený klíč pro odblokování PINu (PUK) pro obnovu po uzamčení
- Uživatelsky konfigurovatelné postupy povolení/zákazu a změny
- Integrace do širších bezpečnostních rámců pro předplatné a služby

## Související pojmy

- [SIM – Subscriber Identity Module / Universal Subscriber Identity Module](/mobilnisite/slovnik/sim/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [PUK – PIN Unblocking Key](/mobilnisite/slovnik/puk/)

## Definující specifikace

- **TS 21.111** (Rel-19) — USIM and UICC Requirements for 3G
- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.153** (Rel-20) — Multimedia Priority Service (MPS) requirements
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.854** (Rel-17) — Feasibility Study on Multimedia Priority Service - Phase 2
- **TR 22.859** (Rel-18) — Technical Report
- **TR 22.950** (Rel-19) — Feasibility Study on Priority Service
- **TR 22.953** (Rel-19) — Multimedia Priority Service Feasibility Study
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.542** (Rel-20) — Application layer support for Personal IoT Network
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [PIN na 3GPP Explorer](https://3gpp-explorer.com/glossary/pin/)
