---
slug: "apdu"
url: "/mobilnisite/slovnik/apdu/"
type: "slovnik"
title: "APDU – Application Protocol Data Unit"
date: 2025-01-01
abbr: "APDU"
fullName: "Application Protocol Data Unit"
category: "Protocol"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/apdu/"
summary: "APDU je strukturovaná datová jednotka používaná pro komunikaci mezi čipovou kartou (např. UICC/USIM) a externí aplikací nebo síťovou entitou. Umožňuje zabezpečené, standardizované příkazy a odpovědi p"
---

APDU je strukturovaná datová jednotka používaná pro zabezpečenou, standardizovanou komunikaci mezi čipovou kartou, jako je UICC nebo USIM, a externí aplikací nebo síťovou entitou.

## Popis

Application Protocol Data Unit (APDU) je základní komunikační paket definovaný standardem [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 7816-4 a přijatý 3GPP pro interakce s čipovými kartami, konkrétně s Universal Integrated Circuit Card (UICC) hostující aplikaci [USIM](/mobilnisite/slovnik/usim/). Slouží jako standardizovaný formát pro výměnu příkazů a odpovědí mezi terminálem (např. mobilním zařízením) a kartou. APDU se skládá z povinného příkazového APDU ([C-APDU](/mobilnisite/slovnik/c-apdu/)) odeslaného terminálem a odpovídajícího odpovědního APDU ([R-APDU](/mobilnisite/slovnik/r-apdu/)) vráceného kartou. Struktura C-APDU zahrnuje hlavičku (CLA, INS, P1, P2) určující třídu, instrukci a parametry, a tělo proměnné délky obsahující příkazová data. R-APDU obsahuje tělo s daty odpovědi a povinnou dvoubajtovou závěrečnou část (SW1, SW2) udávající stav zpracování příkazu (např. úspěch, chybové stavy).

V systémech 3GPP se APDU primárně používají přes rozhraní mezi Mobile Equipment ([ME](/mobilnisite/slovnik/me/)) a UICC, jak je standardizováno v TS 31.101. Umožňují širokou škálu funkcí USIM a Card Application Toolkit ([CAT](/mobilnisite/slovnik/cat/)). Například během síťové autentizace odešle ME APDU příkaz do USIM, aby provedlo algoritmus autentizace a dohody klíče ([AKA](/mobilnisite/slovnik/aka/)), a USIM vrátí APDU odpověď s vypočítaným autentizačním vektorem. APDU také umožňují zabezpečené OTA (Over-The-Air) aktualizace předplatitelských dat, provizionování aplikací (např. pro správu eSIM) a provádění přidaných služeb přes SIM Toolkit.

Mechanismus APDU funguje v rámci modelu master-slave, kde terminál iniciuje všechny příkazy. Protokol na úrovni APDU je bez relace a bezstavový, ačkoli aplikace vyšší vrstvy si stav mohou udržovat. Výměny APDU jsou přenášeny přes fyzické a logické kanály rozhraní UICC. Zabezpečení je nedílnou součástí; citlivé příkazy (např. pro personalizaci nebo správu klíčů) jsou chráněny zabezpečeným zasíláním zpráv, kde jsou data APDU šifrována a chráněna integrita pomocí klíčů uložených na kartě. To zajišťuje důvěrnost a autenticitu operací, jako je stahování profilu pro eSIM.

APDU jsou klíčové pro modularitu a interoperabilitu systémů čipových karet v telekomunikacích. Umožňují různorodým aplikacím (od síťové autentizace po platební aplety) koexistovat na jedné UICC díky poskytnutí jednotné sady příkazů. Přísné formátování a hlášení stavů umožňují robustní zpracování chyb a ladění. V pokročilých případech použití, jako je IoT s vestavěnými SIM (eSIM), APDU usnadňují vzdálenou správu předplatného, jak je definováno ve specifikacích GSMA, které staví na rámci APDU od 3GPP pro instalaci a správu profilů.

## K čemu slouží

APDU bylo zavedeno za účelem standardizace komunikace s čipovými kartami, aby bylo řešeno potřeba univerzální, interoperabilní sady příkazů napříč různými výrobci karet a aplikacemi. Před standardizací proprietární příkazová rozhraní bránila kompatibilitě a zvyšovala složitost pro výrobce zařízení a síťové operátory. Přijetím ISO/IEC 7816-4 zajistilo 3GPP, že UICC a USIM od jakéhokoli dodavatele mohou bezproblémově pracovat s jakýmkoli kompatibilním mobilním zařízením, což podpořilo konkurenční ekosystém a snížilo náklady na integraci.

V kontextu 3GPP řeší APDU problém zabezpečené a efektivní výměny dat pro správu předplatitelské identity a autentizaci. Umožňují USIM provádět kryptografické výpočty lokálně na zabezpečené kartě, takže citlivé klíče nejsou nikdy vystaveny potenciálně kompromitovanému prostředí zařízení. To je zásadní pro síťové zabezpečení v GSM, UMTS a LTE/5G. Dále APDU podporují dynamickou povahu moderních mobilních služeb tím, že umožňují OTA aktualizace, které jsou nezbytné pro provizionování, úpravu předplatitelských dat nebo nasazení nových aplikací bez fyzické výměny karty.

Vytvoření a vývoj použití APDU v 3GPP byly motivovány rozšířením schopností čipových karet za pouhou jednoduchou autentizaci. Jak se UICC vyvinuly v víceaplikační platformy hostující platební, identitní a IoT služby, byl nezbytný robustní, rozšiřitelný protokol. APDU poskytují tento základ, umožňujíce definovat nové instrukce a datové struktury v rámci existujícího rámce. Řeší omezení dřívějších, méně strukturovaných metod tím, že nabízejí přesnou kontrolu, standardizované hlášení chyb a podporu zabezpečeného zasílání zpráv, což je klíčové pro provádění a správu důvěryhodných služeb ve stále více digitálním a propojeném světě.

## Klíčové vlastnosti

- Standardizovaná struktura příkaz-odpověď dle ISO/IEC 7816-4
- Podporuje zabezpečené zasílání zpráv pro šifrovanou a integritu chráněnou výměnu dat
- Umožňuje autentizaci a dohodu klíče (AKA) prostřednictvím příkazů USIM
- Umožňuje OTA (Over-The-Air) provizionování a správu aplikací na kartě
- Poskytuje detailní hlášení stavu prostřednictvím kódů SW1-SW2 pro zpracování chyb
- Rozšiřitelné pro nové instrukce a aplikace na platformě UICC

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [OTA – Over The Air](/mobilnisite/slovnik/ota/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API
- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification
- **TS 51.013** (Rel-19) — SIM API for Java Card Test Specification

---

📖 **Anglický originál a plná specifikace:** [APDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/apdu/)
