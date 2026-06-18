---
slug: "psid"
url: "/mobilnisite/slovnik/psid/"
type: "slovnik"
title: "PSID – Provider Service Identifier"
date: 2025-01-01
abbr: "PSID"
fullName: "Provider Service Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/psid/"
summary: "Jedinečný identifikátor poskytovatele služby V2X, který umožňuje zabezpečený a autorizovaný přístup ke službě v komunikaci vozidlo–vše (V2X). Je klíčový pro vyhledávání služeb, autentizaci a zajištění"
---

PSID je jedinečný identifikátor poskytovatele služby V2X, který umožňuje zabezpečený přístup ke službě, její vyhledání a autentizaci v komunikaci vozidlo–vše (V2X).

## Popis

Provider Service Identifier (PSID) je základní identifikátor standardizovaný v rámci 3GPP pro systémy komunikace vozidlo–vše ([V2X](/mobilnisite/slovnik/v2x/)), zavedený ve vydání Release 14. Slouží jako jedinečná, globálně rozpoznatelná značka přiřazená konkrétnímu poskytovateli služby V2X nebo konkrétní aplikaci V2X. PSID je vložen do zpráv V2X, například těch definovaných v rozhraní LTE-V2X PC5 nebo v komunikacích NR-V2X sidelink, což umožňuje přijímajícím entitám identifikovat původ a povahu služby. Tato identifikace je klíčová pro zpracování zpráv, protože různé služby (např. varování před kolizí, zvyšování dopravní účinnosti, ochrana chodců) mají odlišné požadavky na prioritu, zabezpečení a zacházení. PSID funguje v rámci širšího rámce zabezpečení a autorizace služeb a je často uváděn ve spojení s certifikáty a politikami, aby bylo zajištěno, že pouze autorizovaná vozidla nebo zařízení na okraji sítě mohou generovat nebo reagovat na zprávy pro danou službu.

Z architektonického hlediska je PSID klíčovou součástí řídicí roviny a aplikační vrstvy V2X. Je definován na aplikačním serveru V2X a poskytován autorizovaným uživatelským zařízením (UE), jako jsou palubní jednotky ve vozidlech, prostřednictvím systémů správy sítě nebo poskytování přihlašovacích údajů. Když UE vygeneruje zprávu V2X, zahrne příslušný PSID do vyhrazeného pole ve struktuře zprávy, jak je specifikováno v protokolech vrstvy 2 nebo aplikační vrstvy. Přijímající UE nebo síťová entita pak tento PSID použije k vyhledání místních politik – například těch definovaných ve funkci řízení politik V2X v UE – aby rozhodla, jak zprávu zpracovat. To může zahrnovat kontrolu autorizace, aplikaci specifických bezpečnostních procedur nebo směrování zprávy ke správnému aplikačnímu handleru na základě typu služby.

Pokud jde o jeho roli v síti, PSID umožňuje diferenciaci služeb a interoperabilitu mezi více operátory v ekosystémech V2X. Protože služby V2X mohou být nabízeny více poskytovateli (např. výrobci automobilů, provozovatelé silnic, orgány veřejné bezpečnosti), PSID zajišťuje, že zprávy jsou správně přisuzovány a že jsou vynucovány smlouvy o úrovni služeb a bezpečnostní politiky. Je nedílnou součástí bezpečnostního rámce V2X definovaného v specifikacích jako TS 33.836, kde je používán v profilech certifikátů a autorizačních politikách k propojení identity služby s kryptografickými přihlašovacími údaji. Standardizovaný formát PSID umožňuje škálovatelný a organizovaný jmenný prostor, zabraňuje konfliktům mezi poskytovateli služeb a podporuje vývoj nových aplikací V2X v různých vydáních 3GPP bez nutnosti změn základního identifikačního mechanismu.

## K čemu slouží

PSID byl vytvořen, aby řešil potřebu standardizované, zabezpečené a škálovatelné metody pro identifikaci poskytovatelů služeb [V2X](/mobilnisite/slovnik/v2x/) a aplikací v celulárních komunikacích V2X. Před jeho zavedením v 3GPP Release 14 komunikace V2X, zejména v systémech vyhrazené krátkodosahové komunikace (DSRC), často spoléhaly na proprietární nebo méně strukturované identifikátory, což bránilo interoperabilitě, zabezpečení a rozsáhlému nasazení. Rozmach různorodých aplikací V2X – od základních bezpečnostních zpráv po pokročilé služby autonomního řízení – si vyžádal mechanismus pro rozlišení služeb, vynucení řízení přístupu a zajištění, že zprávy jsou zpracovávány podle své kritičnosti a původu.

Primární problém, který PSID řeší, je nejednoznačnost v identifikaci služeb mezi různými vozidly, sítěmi a geografickými regiony. Bez globálně jedinečného identifikátoru by mohla být zpráva V2X od jednoho poskytovatele služby přijímajícím zařízením z jiného ekosystému nesprávně interpretována nebo ignorována, což by ohrozilo bezpečnost a účinnost. PSID poskytuje jasnou, standardizovanou značku, která je rozpoznávána ve všech zařízeních kompatibilních s 3GPP, a umožňuje tak bezproblémové vyhledávání a autorizaci služeb. Zároveň řeší bezpečnostní výzvy propojením identity služby s procesy autentizace a autorizace, čímž zajišťuje, že pouze autorizované entity mohou vysílat nebo reagovat na konkrétní služby V2X, a tím předchází podvržení a neoprávněnému přístupu.

Historicky vycházela motivace pro PSID z tlaku automobilového průmyslu na standardizaci celulárního V2X (C-V2X) jako nástupce systémů založených na [IEEE](/mobilnisite/slovnik/ieee/) 802.11p. Zapojení 3GPP mělo za cíl využít infrastrukturu celulárních sítí pro vylepšené služby V2X, což vyžadovalo robustní identifikátory integrované s bezpečnostními rámci celulárních sítí. PSID to umožňuje tím, že podporuje síťové řízení politik a správu certifikátů, a to jak pro přímou komunikaci PC5, tak pro komunikaci Uu prostřednictvím sítě. Jeho vytvoření bylo hnací silou potřeby podporovat prostředí s více dodavateli a více operátory, kde jsou důvěra a diferenciace služeb klíčové pro bezpečnostně kritické aplikace.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro poskytovatele služeb a aplikace V2X
- Vložen do struktur zpráv V2X pro identifikaci služby
- Umožňuje vynucování služebně specifických politik a zpracování zpráv
- Integruje se s bezpečnostními rámci V2X pro autentizaci a autorizaci
- Podporuje interoperabilitu mezi různými operátory a geografickými regiony
- Usnadňuje škálovatelné nasazení nových služeb V2X bez konfliktů identifikátorů

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 22.186** (Rel-19) — Service requirements for enhanced V2X support
- **TS 23.285** (Rel-19) — V2X Architecture Enhancements for LTE
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TS 33.836** (Rel-16) — Security Study for Advanced V2X Services

---

📖 **Anglický originál a plná specifikace:** [PSID na 3GPP Explorer](https://3gpp-explorer.com/glossary/psid/)
