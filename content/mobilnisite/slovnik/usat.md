---
slug: "usat"
url: "/mobilnisite/slovnik/usat/"
type: "slovnik"
title: "USAT – Universal Subscriber Identity Module Application Toolkit"
date: 2025-01-01
abbr: "USAT"
fullName: "Universal Subscriber Identity Module Application Toolkit"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/usat/"
summary: "Standardizované výkonné prostředí a API v rámci UICC/USIM, které umožňuje bezpečné spouštění aplikací (appletů) poskytovaných operátorem. Umožňuje přidané služby jako menu na SIM kartě, OTA konfigurac"
---

USAT je standardizované výkonné prostředí a API v rámci UICC/USIM, které bezpečně spouští aplikace poskytované operátorem, aby umožnilo přidané služby jako SIM menu a bezpečnou autentizaci.

## Popis

Universal Subscriber Identity Module Application Toolkit (USAT) je komplexní rámec standardizovaný organizacemi 3GPP a [ETSI](/mobilnisite/slovnik/etsi/), který mění tradiční [SIM](/mobilnisite/slovnik/sim/) kartu na bezpečnou, programovatelnou platformu schopnou hostovat a provádět aplikace. Je v podstatě aplikační vrstvou běžící na podkladovém hardwaru UICC (Universal Integrated Circuit Card) a logické struktuře [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module). USAT definuje sadu příkazů, procedur a výkonné prostředí, které umožňuje appletům – malým aplikacím napsaným v Java Card nebo nativním kódu – komunikovat s mobilním zařízením (Terminal Equipment nebo [ME](/mobilnisite/slovnik/me/)) a skrze něj s mobilní sítí a externími službami. Architektura je založena na proaktivním modelu: aplikace USAT na UICC může odesílat „Proaktivní příkazy“ do ME. Tyto příkazy instruují ME k provedení akcí, jako je zobrazení textových menu, přehrání tónů, navázání hovoru, odeslání zprávy [SMS](/mobilnisite/slovnik/sms/) (Short Message Service) nebo poskytnutí informace o poloze. ME příkaz vykoná a odešle zpět na UICC „Terminálovou odpověď“ s výsledkem. Tato interakce je řízena přes rozhraní příkazů „AT“ definované ETSI. Mezi klíčové komponenty patří USAT Interpreter pro zpracování příkazů, Souborový systém pro ukládání appletů a dat a Bezpečnostní doména pro správu kryptografických klíčů a protokolů zabezpečeného kanálu, jako je [OTA](/mobilnisite/slovnik/ota/) (Over-The-Air) pro vzdálenou správu aplikací. USAT umožňuje služby jako SIM Toolkit ([STK](/mobilnisite/slovnik/stk/)) menu pro bankovnictví nebo informační služby, OTA provisioning nastavení zařízení (např. přístupových bodů k internetu) a je základem pro pokročilejší bezpečnostní prvky používané v mobilních finančních službách (např. NFC platby přes SIM). Poskytuje důvěryhodné, proti manipulaci odolné prostředí izolované od hlavního operačního systému telefonu, což je klíčové pro operace citlivé na zabezpečení.

## K čemu slouží

USAT byl vyvinut, aby odemkl potenciál [SIM](/mobilnisite/slovnik/sim/) karty nad její původní účel autentizace účastníka a ukládání síťových parametrů. V počátcích GSM byla SIM poměrně statickou součástí. USAT, vyvíjející se z dřívějšího SIM Application Toolkit (SAT), byl vytvořen, aby poskytl standardizovanou platformu nezávislou na výrobci, která umožní mobilním síťovým operátorům nasazovat a spravovat přidané služby přímo ze zabezpečené SIM karty. To řešilo několik problémů: dávalo operátorům kontrolu nad poskytováním služeb nezávisle na výrobcích telefonů, poskytovalo všudypřítomné zabezpečené výkonné prostředí napříč všemi kompatibilními telefony a umožňovalo služby vyžadující vysokou úroveň důvěry, jako je mobilní bankovnictví. Před USAT často zavedení nových funkcí vyžadovalo aktualizace firmwaru telefonu nebo proprietární řešení, což bylo pomalé a fragmentované. USAT vytvořil univerzální ekosystém, kde mohli operátoři napsat aplikaci jednou a nasadit ji OTA na miliony SIM karet účastníků s jistotou, že bude fungovat na jakémkoli kompatibilním zařízení. To motivovalo vytvoření široké škály služeb, od jednoduchých informačních menu po komplexní platební a identifikační aplikace, a ustanovilo SIM kartu jako klíčovou platformu pro mobilní obchod a zabezpečené služby v érách 2G/3G/4G – role, která se dále vyvíjí s embedded SIM (eSIM) a IoT aplikacemi.

## Klíčové vlastnosti

- Definuje proaktivní model příkazů pro interakci UICC–ME
- Poskytuje zabezpečené výkonné prostředí pro Java Card applety
- Umožňuje OTA (Over-The-Air) provisioning a správu aplikací
- Podporuje SIM Toolkit (STK) menu pro uživatelsky interaktivní služby
- Obsahuje API pro telefonní funkce (řízení hovorů, SMS), uživatelské rozhraní a informace o zařízení
- Nabízí proti manipulaci odolný bezpečnostní prvek pro kryptografické a platební operace

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 31.112** (Rel-8) — USAT Interpreter System Architecture
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 31.117** (Rel-19) — USIM Application Toolkit Test for Non-Removable UICC
- **TR 31.901** (Rel-14) — USIM/ISIM/USAT Feature Review Study
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework

---

📖 **Anglický originál a plná specifikace:** [USAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/usat/)
