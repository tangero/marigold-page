---
slug: "wsid"
url: "/mobilnisite/slovnik/wsid/"
type: "slovnik"
title: "WSID – WLAN Specific Identifier"
date: 2025-01-01
abbr: "WSID"
fullName: "WLAN Specific Identifier"
category: "Identifier"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/wsid/"
summary: "Jedinečný identifikátor používaný v systémech 3GPP pro řízení a autentizaci uživatelského přístupu k bezdrátovým lokálním síťám (WLAN). Je klíčový pro zajištění bezpečného a hladkého spolupráce mezi m"
---

WSID je jedinečný identifikátor používaný v systémech 3GPP pro řízení a autentizaci uživatelského přístupu k bezdrátovým lokálním síťám (WLAN).

## Popis

[WLAN](/mobilnisite/slovnik/wlan/) Specific Identifier (WSID) je identifikátor přístupu definovaný v rámci 3GPP pro usnadnění spolupráce mezi 3GPP mobilními sítěmi a ne-3GPP přístupovými sítěmi, konkrétně WLAN. Je uložen v Universal Subscriber Identity Module ([USIM](/mobilnisite/slovnik/usim/)) a používá se síťovými elementy pro jedinečnou identifikaci uživatelského přístupu pro procedury specifické pro WLAN. Primární architektonická role WSID je v rámci autentizačního a autorizačního frameworku, kde může být použita spolu s nebo jako alternativa jiným identifikátorům jako [IMSI](/mobilnisite/slovnik/imsi/), zejména ve scénářích definovaných specifikacemi Wireless [LAN](/mobilnisite/slovnik/lan/) Interworking ([I-WLAN](/mobilnisite/slovnik/i-wlan/)).

Operačně je WSID využíván během procesu Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)) autentizace, když User Equipment (UE) pokouší připojit k WLAN integrované s 3GPP core síť. Síť, konkrétně Authentication, Authorization, and Accounting ([AAA](/mobilnisite/slovnik/aaa/)) server, může použít WSID pro získání správného profilu přístupu a autentizačních kredencí z Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Tento proces je detailně popsán v specifikacích jako TS 24.234 (3GPP system to Wireless Local Area Network (WLAN) interworking) a TS 31.102 (Characteristics of the Universal Subscriber Identity Module (USIM) application).

Klíčové komponenty zahrnující WSID jsou USIM, kde je uložen, WLAN stack UE, který ho prezentuje během autentizace, a AAA infrastruktura síťových elementů a HSS, které ho zpracovávají. Jeho role je klíčová pro umožnění standardizované, bezpečné metody pro mobilní operátory, aby rozšířili své služby a billingové modely na Wi-Fi hotspoty, zajišťující, že uživatelská zkušenost je konzistentní a řízena pod rámcem operátorových politik. Identifikátor pomáhá oddělit autentizaci přístupu WLAN od hlavní mobilní identity, poskytující flexibilitu v nabídce služeb.

## K čemu slouží

WSID byl zaveden, aby řešil rostoucí potřebu hladkého a bezpečného integrace mezi mobilními sítěmi a WLAN. Před jeho standardizací operátorům chyběl konzistentní, standardizovaný metoda pro identifikaci a autentizaci jejich přístupů na Wi-Fi síťích, vedoucí k fragmentované uživatelské zkušenosti a komplexním, proprietárním autentizačním mechanismům. Vytvoření WSID bylo motivované prací 3GPP na I-WLAN v Release 6, která měla za cíl definovat unified architekturu pro spolupráce.

Technologie řeší problém řízení identity přístupu v heterogenních přístupových prostředích. Poskytnutím WLAN-specific identifikátoru uloženého na USIM umožňuje operátorům využití existující SIM-based bezpečnostní infrastruktury pro WLAN přístup. Tento přístup řešil limity jako potřebu separátních username/password pro Wi-Fi a umožnil tighter integrace s operátorovou core síť pro služby jako autentizace, autorizace a charging. Formoval foundational element pro early network convergence efforts.

## Klíčové vlastnosti

- Uložen bezpečně na USIM aplikaci
- Používán pro identifikaci přístupu v autentizaci pro spolupráce 3GPP-WLAN
- Umožňuje EAP-based autentizační procedury přes AAA infrastrukturu
- Podporuje oddělení identity přístupu WLAN od hlavního IMSI
- Usnadňuje konzistentní aplikaci politik přístupu přes přístupové typy
- Definován v rámci I-WLAN architektonického frameworku

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [I-WLAN – Interworking Wireless Local Area Network](/mobilnisite/slovnik/i-wlan/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification

---

📖 **Anglický originál a plná specifikace:** [WSID na 3GPP Explorer](https://3gpp-explorer.com/glossary/wsid/)
