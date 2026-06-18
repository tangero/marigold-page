---
slug: "dp"
url: "/mobilnisite/slovnik/dp/"
type: "slovnik"
title: "DP – Decrypted PIN"
date: 2025-01-01
abbr: "DP"
fullName: "Decrypted PIN"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dp/"
summary: "Dešifrovaná data PIN, odkazující na osobní identifikační číslo v dešifrované podobě po bezpečném zpracování. V 3GPP je tento termín spojován s autentizačními a bezpečnostními mechanismy, zejména v kon"
---

DP je dešifrovaný údaj osobního identifikačního čísla (PIN), který je bezpečně zpracován a používán v autentizačních mechanismech 3GPP, zejména pro aplikace USIM a ověřování zabezpečených služeb.

## Popis

DP, z anglického Decrypted [PIN](/mobilnisite/slovnik/pin/), je bezpečnostní termín ve specifikacích 3GPP, který označuje osobní identifikační číslo (PIN) v jeho dešifrovaném stavu po provedení kryptografického zpracování. PIN je tajný číselný kód používaný pro autentizaci uživatele, typicky s [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module) nebo [SIM](/mobilnisite/slovnik/sim/) kartou pro odemčení služeb nebo ověření identity. V bezpečnostní architektuře je PIN uložen v zašifrované podobě, aby se zabránilo neoprávněnému přístupu, a DP představuje výsledek dešifrování této hodnoty pomocí bezpečného klíče, což umožňuje její porovnání se vstupem od uživatele nebo použití v dalších krocích autentizace. Tento proces je součástí širšího rámce autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)) a mechanismů zabezpečeného přístupu ke službám definovaných v 3GPP.

Fungování DP zahrnuje několik vrstev bezpečnostních protokolů. Nejprve je PIN zašifrován pomocí algoritmů, jako jsou ty založené na autentizačním klíči účastníka (Ki) nebo jiných bezpečných klíčech uložených na USIM. Když je vyžadována autentizace – například při startu mobilního zařízení nebo přístupu k omezené službě – systém načte zašifrovaný PIN, dešifruje jej pomocí příslušného klíče (často v rámci zabezpečeného prostředí, jako je odolný hardware USIM), čímž získá DP. Tato dešifrovaná hodnota je pak interně použita pro ověření bez toho, aby byla vystavena externě. Mezi klíčové komponenty patří aplikace USIM, která spravuje šifrování a dešifrování PIN, a bezpečnostní funkce mobilního zařízení, které komunikují s USIM za účelem bezpečného nakládání s DP, a zajišťují, že nikdy neopustí chráněnou doménu v otevřené podobě.

Úloha DP v síti spočívá v usnadnění bezpečné autentizace uživatele při zachování důvěrnosti. Je nedílnou součástí procedur, jako je ověření PIN pro povolení služeb (např. zrušení PIN lock) nebo pro zabezpečené transakce. Ve specifikacích je DP zmiňováno v kontextech, jako jsou management objekty pro správu zařízení (např. v protokolech [OMA](/mobilnisite/slovnik/oma/) [DM](/mobilnisite/slovnik/dm/)) nebo v bezpečnostních protokolech pro přístup ke službám. Tím, že je PIN udržován v zašifrované podobě až do nezbytnosti a dešifrován pouze v rámci zabezpečeného prvku, DP zmírňuje rizika jako odposlech nebo manipulace, což je v souladu s bezpečnostními cíli 3GPP na ochranu identity účastníka a prevenci neoprávněného použití. Tento koncept zdůrazňuje význam komplexní bezpečnosti v mobilních systémech, od USIM až po síťová autentizační centra.

## K čemu slouží

DP existuje, aby řešil bezpečnostní výzvu nakládání s osobními identifikačními čísly ([PIN](/mobilnisite/slovnik/pin/)) v mobilních systémech bez jejich vystavení zranitelnostem. PIN je kritické tajemství pro autentizaci uživatele a jeho ukládání nebo přenos v otevřené podobě by s sebou neslo riziko odposlechu a podvodu. Použitím šifrovaného úložiště PIN a dešifrovaného PIN (DP) pouze v rámci zabezpečeného prostředí specifikace 3GPP zajišťují, že ověření PIN může proběhnout bezpečně, čímž řeší problém bezpečného řízení tajemství v zařízeních a sítích.

Historicky měly rané mobilní systémy jednodušší bezpečnostní mechanismy, které byly náchylné k útokům, jako je klonování nebo odposlech. Zavedení DP v 3GPP od verze [R99](/mobilnisite/slovnik/r99/) odráží vývoj směrem k robustnějším bezpečnostním postupům, které využívají kryptografické techniky k ochraně citlivých dat. To bylo motivováno rostoucí potřebou zabezpečených mobilních služeb, jako je mobilní bankovnictví nebo korporátní přístup, kde se PIN používá pro zajištění identity. Předchozí přístupy, které spoléhaly na méně bezpečné metody ukládání nebo přenosu, byly pro tyto pokročilé případy použití nedostatečné.

Vytvoření DP je hnací silou požadavku na dodržování bezpečnostních standardů a předpisů, jako jsou ty pro finanční transakce nebo ochranu soukromí dat. Umožňuje bezpečné nakládání s PIN napříč různými rozhraními a procedurami definovanými 3GPP, od správy zařízení po síťovou autentizaci. Definováním DP poskytuje 3GPP standardizovaný způsob správy PIN, který vyvažuje použitelnost a bezpečnost, zajišťuje interoperabilitu mezi různými výrobci USIM a mobilními zařízeními a zároveň zmírňuje omezení dřívějších nekryptografických metod, které mohly ohrozit bezpečnost účastníka.

## Klíčové vlastnosti

- Představuje dešifrovanou podobu osobního identifikačního čísla (PIN)
- Používá se v zabezpečených autentizačních procesech v rámci aplikací USIM
- Zahrnuje kryptografické dešifrování pomocí klíčů jako je Ki pro zajištění bezpečnosti
- Zajišťuje důvěrnost PIN tím, že omezuje vystavení otevřené podoby na zabezpečená prostředí
- Nedílná součást procedur pro ověření PIN a řízení přístupu ke službám
- Odkazováno ve specifikacích 3GPP pro správu zařízení a bezpečnostní protokoly

## Související pojmy

- [PIN – Personal Identification Number](/mobilnisite/slovnik/pin/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 26.111** (Rel-19) — 3G-324M Terminal Specification for CS Multimedia
- **TS 29.007** (Rel-19) — PLMN-PSTN/ISDN Interworking Requirements
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.276** (Rel-19) — VCS Online Charging from Proxy Function
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface

---

📖 **Anglický originál a plná specifikace:** [DP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dp/)
