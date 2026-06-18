---
slug: "pics"
url: "/mobilnisite/slovnik/pics/"
type: "slovnik"
title: "PICS – Protocol Implementation Conformance Statement"
date: 2025-01-01
abbr: "PICS"
fullName: "Protocol Implementation Conformance Statement"
category: "Management"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/pics/"
summary: "Standardizovaný dokument, který podrobně popisuje, jaké schopnosti a volby specifikace protokolu 3GPP konkrétní implementace podporuje. Je klíčový pro zajištění interoperability mezi zařízeními různýc"
---

PICS je standardizovaný dokument, který podrobně popisuje, jaké schopnosti a volby specifikace protokolu 3GPP konkrétní implementace podporuje, a poskytuje tak jasné, testovatelné prohlášení pro zajištění interoperability.

## Popis

Protocol Implementation Conformance Statement (PICS, Prohlášení o shodě implementace protokolu) je formální strukturovaný dokument, který doprovází implementaci protokolu 3GPP v produktu. Není to samotná implementace, ale deklarace toho, které konkrétní funkce, volby a hodnoty parametrů z příslušných specifikací protokolu produkt podporuje. PICS je organizován podle článků a tabulek v základním standardu a souvisejících testovacích specifikacích. Pro každou schopnost protokolu definovanou ve standardu PICS uvádí, zda ji implementace podporuje (Ano/Ne), a pokud je to možné, i konkrétní hodnoty nebo rozsahy, které podporuje. Tento strukturovaný formát umožňuje testovacím laboratořím a síťovým operátorům systematicky ověřit, že implementace splňuje deklarované schopnosti.

Z architektonického hlediska je PICS klíčovým vstupem pro proces testování shody. Testovací sady, jako jsou ty definované v sérii 3GPP TS 51.010 pro GSM nebo TS 38.523 pro NR, jsou navrženy k ověření chování popsaného v PICS. Testovací systém používá PICS k určení, které testovací případy jsou použitelné a jaké by měly být očekávané výsledky. To zajišťuje, že testování je jak komplexní, tak efektivní, a zaměřuje se pouze na schopnosti, které výrobce tvrdí, že implementoval. Samotný PICS je typicky generován vývojářem produktu na základě podrobné analýzy standardů protokolu a návrhu jejich produktu.

Jeho role v síťovém ekosystému je zásadní pro interoperabilitu více výrobců. Před nasazením síťového zařízení nebo uživatelských zařízení podstupují důkladné testování shody založené na jejich PICS. Tento proces, často prováděný akreditovanými testovacími domy, ověřuje, že zařízení se chová správně podle standardu pro všechny deklarované funkce. Kompletní a přesný PICS je proto smluvním a technickým pilířem, který snižuje integrační rizika, urychluje uvedení na trh a zajišťuje, že koncoví uživatelé zažívají spolehlivé a konzistentní služby bez ohledu na výrobce zařízení. Překlenuje propast mezi abstraktní specifikací protokolu a konkrétním, nasaditelným produktem.

## K čemu slouží

PICS byl vytvořen, aby řešil kritickou výzvu interoperability v komplexních telekomunikačních sítích více výrobců. Rané digitální mobilní systémy čelily významným integračním problémům, protože různí výrobci interpretovali standardy protokolů odlišně nebo implementovali pouze částečné podmnožiny. To vedlo k nákladným a časově náročným bilaterálním testovacím a integračním snahám pro každou novou kombinaci síťových prvků. PICS poskytuje standardizovaný, jednoznačný způsob, jak může výrobce deklarovat, co jeho produkt přesně dělá, čímž proměňuje interoperabilitu z ad-hoc hádanky na systematický, ověřitelný inženýrský proces.

Historicky byl jeho vývoj motivován globálním úspěchem GSM a následnou potřebou formalizovanějšího přístupu k shodě, jak se systémy vyvíjely k [GPRS](/mobilnisite/slovnik/gprs/), UMTS a LTE. 3GPP přijalo a formalizovalo koncept PICS z širších metodik testování protokolů [ITU-T](/mobilnisite/slovnik/itu-t/) a [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/). Řeší problém 'nejednoznačnosti standardu' tím, že nutí implementátory učinit explicitní volby pro každou volitelnou nebo podmíněnou funkci ve specifikaci. Tato transparentnost umožňuje síťovým operátorům činit informovaná rozhodnutí o nákupu a nezávislým testovacím laboratořím provádět reprodukovatelné, standardizované testovací kampaně.

V konečném důsledku PICS existuje k budování důvěry v ekosystém. Snižuje komerční a technické riziko pro operátory nasazující zařízení z více zdrojů. Poskytnutím jasné základny pro testování zajišťuje, že zařízení, které tvrdí, že podporuje funkci, ji skutečně implementuje správně, čímž předchází selhání sítě a špatným uživatelským zkušenostem. Je klíčovým enablerem pro konkurenční, inovativní a spolehlivý trh, který charakterizuje moderní mobilní komunikace.

## Klíčové vlastnosti

- Strukturovaná deklarace podporovaných schopností protokolu
- Povinný referenční dokument pro testování shody a interoperability
- Organizován podle článků základního standardu
- Specifikuje podporu volitelných funkcí a rozsahů parametrů
- Umožňuje generování seznamů použitelných testovacích případů
- Základ pro procesy certifikace a schvalování typu

## Související pojmy

- [IXIT – Implementation eXtra Information for Testing](/mobilnisite/slovnik/ixit/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 36.523** (Rel-19) — UE Conformance Test Spec for Idle Mode
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.508** (Rel-19) — 5G NR UE Radio Transmission & Reception
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TS 51.010** (Rel-19) — SIM Application Toolkit Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [PICS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pics/)
