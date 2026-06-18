---
slug: "eecid"
url: "/mobilnisite/slovnik/eecid/"
type: "slovnik"
title: "EECID – Edge Enabler Client Identification"
date: 2026-01-01
abbr: "EECID"
fullName: "Edge Enabler Client Identification"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eecid/"
summary: "Jedinečný identifikátor klienta edge enableru (EEC) v edge computingu 3GPP. Umožňuje síti jednoznačně identifikovat a spravovat relaci edge aplikace klienta, čímž zajišťuje kontinuitu služby, vynucová"
---

EECID je jedinečný identifikátor klienta edge enableru, který síti umožňuje spravovat jeho relaci edge aplikace za účelem kontinuity služby, vynucování politik a zabezpečeného přístupu k prostředkům.

## Popis

Edge Enabler Client Identification (EECID) je klíčový identifikátor v architektuře edge computingu 3GPP, standardizovaný od Release 17. Slouží jako trvalý a jedinečný ukazatel klienta edge enableru ([EEC](/mobilnisite/slovnik/eec/)), což je funkční entita nacházející se v uživatelském zařízení (UE) nebo aplikačním serveru, která usnadňuje využívání služeb edge computingu. EECID je přiřazen Edge Enabler Serverem ([EES](/mobilnisite/slovnik/ees/)) během počáteční registrace nebo fáze poskytování služby a je používán po celý životní cyklus relace edge aplikace.

Architektonicky je EECID spravován ve vrstvě Edge Computing Enabler definované v TS 23.558. Když klient (EEC) chce přistupovat ke službám edge, iniciuje registrační proceduru u EES. EES po úspěšné autentizaci a autorizaci (dle TS 33.127) vygeneruje a přiřadí jedinečný EECID. Tento identifikátor je pak zahrnut do všech následných servisních požadavků, jako jsou přenosy aplikačního kontextu, procedury kontinuity služby a požadavky na směrování provozu k Edge Application Serveru ([EAS](/mobilnisite/slovnik/eas/)). Funguje jako primární klíč v databázi správy relací klientů na EES.

Role EECID je mnohostranná. Umožňuje EES korelovat servisní požadavky s konkrétní relací klienta, což umožňuje správné vynucování politik, správu kvót a korelaci účtování. Je nezbytný pro scénáře mobility a kontinuity služeb; při pohybu UE umožňuje EECID síti bezproblémově přenést aplikační kontext mezi různými instancemi EES nebo edge lokacemi bez přerušení služby. Dále poskytuje základ pro bezpečnost, protože je používán ve spojení s autentizačními mechanismy k prevenci převzetí relace a k zajištění, že pouze autorizovaný klient může upravit nebo ukončit svou edge relaci.

Z operačního hlediska je EECID typicky přenášen ve zprávách [HTTP](/mobilnisite/slovnik/http/)/2 nebo rozhraní založených na službách definovaných v TS 29.558. Pro klienta je to neprůhledný řetězec (opaque string), což znamená, že EEC jeho hodnotu neinterpretuje, ale pouze ji uvádí v požadavcích. EES a další síťové funkce (jako Edge Configuration Server nebo Policy Control Function) používají EECID k načtení profilu klienta, předplacených služeb a aktuálního stavu relace. Tato centralizovaná identifikace zjednodušuje správu distribuovaných relací edge computingu napříč potenciálně fragmentovanou sítí edge datových center.

## K čemu slouží

EECID byl zaveden ve 3GPP Release 17 k řešení zásadní výzvy v podobě identifikace klienta a správy relací v distribuovaném prostředí edge computingu. Před jeho standardizací se používaly proprietární nebo aplikací-specifické identifikátory, což bránilo interoperabilitě, bezproblémové mobilitě a konzistentnímu vynucování politik napříč různými síťovými operátory a poskytovateli edge služeb. Nedostatek standardizovaného identifikátoru klienta ztěžoval udržení kontinuity služeb při pohybu uživatele mezi rádiovými přístupovými sítěmi nebo různými edge hostujícími lokacemi.

Vytvoření EECID bylo motivováno potřebou škálovatelného a bezpečného mechanismu pro jedinečnou identifikaci spotřebitelů edge služeb v multi-vendorovém, multi-operatorním ekosystému. Řeší problém korelace mnoha souběžných relací edge aplikací (např. z [AR](/mobilnisite/slovnik/ar/)/[VR](/mobilnisite/slovnik/vr/), průmyslového IoT, videoanalytiky) se správným uživatelským zařízením a předplatitelským profilem. Poskytnutím stabilního identifikátoru, který přetrvává navzdory potenciálním změnám IP adresy nebo síťového připojovacího bodu, umožňuje pokročilé funkce edge computingu, jako je migrace stavových aplikací, účtování na základě relace a dynamické směrování provozu k optimálnímu Edge Application Serveru.

EECID navíc podporuje bezpečnostní rámec pro edge computing. Umožňuje Edge Enabler Serveru navázat bezpečnostní přihlašovací údaje a tokeny na konkrétní relaci klienta, čímž zmírňuje rizika, jako jsou replay útoky a neoprávněný přístup k edge prostředkům. Jeho standardizace zajišťuje, že všechny síťové funkce zapojené do poskytování edge služeb mají společnou referenci pro identifikaci klienta, což je klíčové pro automatizaci, izolaci chyb a regulatorní shodu ve složitých sítích 5G a budoucích sítích.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor přiřazený Edge Enabler Serverem
- Trvá po dobu životního cyklu relace edge aplikace
- Používá se pro korelaci a správu relací klienta napříč síťovými funkcemi
- Zásadní pro zajištění kontinuity edge služeb a podpory mobility
- Slouží jako klíč pro vynucování politik, účtování a navázání bezpečnostních tokenů
- Neprůhledný (opaque) pro klienta, čímž je zajištěna síťová kontrola nad formátem a životním cyklem identifikátoru

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [EECID na 3GPP Explorer](https://3gpp-explorer.com/glossary/eecid/)
