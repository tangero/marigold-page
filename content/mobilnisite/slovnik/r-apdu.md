---
slug: "r-apdu"
url: "/mobilnisite/slovnik/r-apdu/"
type: "slovnik"
title: "R-APDU – Response Application Protocol Data Unit"
date: 2025-01-01
abbr: "R-APDU"
fullName: "Response Application Protocol Data Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/r-apdu/"
summary: "Odpovědní zpráva ve formátu Application Protocol Data Unit používaná pro zabezpečenou komunikaci mezi kartou UICC/SIM a externí entitou, jako je aplikační server sítě. Je základní součástí SIM Applica"
---

R-APDU je odpovědní zpráva ve formátu Application Protocol Data Unit používaná pro zabezpečenou komunikaci mezi kartou UICC/SIM a externí entitou, klíčová pro SIM Application Toolkit a OTA protokoly.

## Popis

R-APDU (Response Application Protocol Data Unit) je strukturovaný datový paket definovaný standardy 3GPP a [ETSI](/mobilnisite/slovnik/etsi/), konkrétně v rámci protokolů pro aplikace na kartě UICC (Universal Integrated Circuit Card) a [SIM](/mobilnisite/slovnik/sim/) (Subscriber Identity Module). Tvoří odpovědní část transakce příkaz-odpověď iniciované [C-APDU](/mobilnisite/slovnik/c-apdu/) (Command [APDU](/mobilnisite/slovnik/apdu/)). R-APDU je přenášeno z karty UICC do terminálu (např. mobilního zařízení) nebo v [OTA](/mobilnisite/slovnik/ota/) scénářích přes terminál na vzdálený server. Jeho struktura je přesně definována a typicky obsahuje povinné pole pro data odpovědi (které může být prázdné) a povinnou dvoubajtovou závěrečnou část obsahující stavové slovo (SW1, SW2). Toto stavové slovo udává výsledek odpovídajícího příkazu, například úspěch (např. '90 00'), různá varovná stavová hlášení nebo specifické kódy chyb (např. selhání paměti, nesplněný bezpečnostní stav).

Během provozu, když terminál nebo OTA platforma pošle C-APDU na kartu UICC s požadavkem na provedení akce – jako je aktualizace souboru, spuštění apletu nebo provedení kryptografického výpočtu – kartou UICC je příkaz zpracován. Výsledek zpracování, který může zahrnovat požadovaná data (jako kryptografický podpis nebo přečtený soubor) nebo pouze potvrzení, je zabalen do R-APDU. Terminál následně tuto odpověď interpretuje na základě stavového slova a případných přiložených dat. Tento mechanismus je ústřední pro SIM Application Toolkit ([SAT](/mobilnisite/slovnik/sat/)), [USAT](/mobilnisite/slovnik/usat/) (UMTS SAT) a [CAT](/mobilnisite/slovnik/cat/) (CDMA Application Toolkit) a umožňuje síťovým operátorům poskytovat služby, spravovat bezpečnostní prvky a komunikovat s aplikacemi na kartě bez fyzického přístupu.

Role R-APDU v síťovém ekosystému je klíčová pro zabezpečenou správu a aktivaci služeb. Používá se v OTA platformách pro vzdálenou správu SIM (např. správu eSIM), aktualizaci autentizačních klíčů a nasazování služeb s přidanou hodnotou. Protokol zajišťuje integritu a definovaný stavový stroj pro interakce, protože každý příkaz musí být jednoznačně zodpovězen. Jeho návrh umožňuje rozšiřitelnost; datové pole může nést složitá datová zatížení a prostor pro stavová slova je dostatečně velký, aby pokryl mnoho specifických stavů definovaných různými aplikačními specifikacemi, což z něj činí univerzální a trvalou součást architektur zabezpečení a správy v mobilní telekomunikaci.

## K čemu slouží

R-APDU existuje proto, aby poskytlo standardizovanou, zabezpečenou a spolehlivou metodu, kterou může karta UICC/SIM odpovídat na příkazy vydané externí entitou. Před takovou standardizací byly interakce s čipovými kartami specifické pro výrobce a postrádaly interoperabilitu, což bránilo rozsáhlému nasazení OTA služeb a zabezpečené správě aplikací. Protokol páru APDU (C-APDU a R-APDU), převzatý z ISO/IEC 7816-4, byl integrován do telekomunikačních standardů, aby vytvořil jednotný jazyk pro komunikaci mezi kartou a terminálem.

Tím bylo vyřešeno, jak vzdáleně a bezpečně spravovat moduly identifikace účastníka v provozu. Umožnilo to SIM Application Toolkit, který umožnil operátorům nabízet nabídky, služby a aktualizace do telefonů, čímž vznikly nové zdroje příjmů a zlepšil se zákaznický zážitek. Dále, jak se mobilní sítě vyvíjely, aby podporovaly složitější služby, jako je mobilní bankovnictví (prostřednictvím zabezpečení založeného na SIM) a později eSIM pro IoT a spotřebitelská zařízení, se robustní mechanismus příkaz-odpověď APDU stal nepostradatelným. Řeší potřebu atomických transakcí, kde má každý příkaz jednoznačný výsledek úspěchu nebo selhání, což je klíčové pro udržení bezpečnostního stavu a integrity dat na SIM kartě, která je důvěryhodným bodem v síti.

## Klíčové vlastnosti

- Standardizovaný formát odpovědi s povinnou závěrečnou částí obsahující stavové slovo (SW1, SW2)
- Nese datovou část odpovědi ze zpracování aplikace na kartě UICC
- Definuje přesné kódy výsledků pro úspěch, varování a chyby při provádění
- Klíčové pro SIM Application Toolkit (SAT/USAT) a OTA protokoly
- Umožňuje zabezpečenou vzdálenou správu a poskytování služeb aplikací na kartě UICC/SIM
- Zajišťuje interoperabilní komunikaci mezi terminály a čipovými kartami od různých výrobců

## Související pojmy

- [C-APDU – Command Application Protocol Data Unit](/mobilnisite/slovnik/c-apdu/)
- [OTA – Over The Air](/mobilnisite/slovnik/ota/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [R-APDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-apdu/)
