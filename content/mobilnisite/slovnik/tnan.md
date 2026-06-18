---
slug: "tnan"
url: "/mobilnisite/slovnik/tnan/"
type: "slovnik"
title: "TNAN – Trusted Non-3GPP Access Network"
date: 2026-01-01
abbr: "TNAN"
fullName: "Trusted Non-3GPP Access Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tnan/"
summary: "Přístupová síť mimo 3GPP (např. Wi-Fi, pevný broadband), která má důvěryhodné, zabezpečené spojení k 5G Core síti. 5G Core k ní přistupuje podobně jako k 3GPP RAN, což umožňuje bezproblémové ověřování"
---

TNAN je důvěryhodná přístupová síť mimo 3GPP, například Wi-Fi, která má zabezpečené spojení k 5G Core a je k ní přistupováno podobně jako k 3GPP rádiové přístupové síti.

## Popis

Trusted Non-3GPP Access Network (TNAN) je klíčovou komponentou v 3GPP architektuře 5G pro podporu konvergence přístupových sítí. Jedná se o rádiovou přístupovou síť mimo 3GPP, nejčastěji Wi-Fi síť nebo pevnou broadbandovou síť, která se připojuje k 5G Core (5GC) přes standardizované, zabezpečené rozhraní. Klíčový rozdíl oproti nedůvěryhodnému přístupu mimo 3GPP spočívá v tom, že TNAN má předem navázaný vztah důvěry s operátorem 5G sítě. Tato důvěra je ověřena prostřednictvím autentizace sítě, což umožňuje 5GC poskytovat své služby přímo přes tento přístup bez nutnosti dodatečného [IPsec](/mobilnisite/slovnik/ipsec/) tunelu pro veškerý uživatelský provoz, jak je tomu u nedůvěryhodného přístupu.

Architektonicky se TNAN připojuje k 5GC přes [TNGF](/mobilnisite/slovnik/tngf/) (Trusted Non-3GPP Gateway Function) v případě drátového přístupu, nebo přes [W-AGF](/mobilnisite/slovnik/w-agf/) (Wireline Access Gateway Function) pro určité pevné scénáře. TNGF funguje jako proxy řídicí roviny a kotva uživatelské roviny, která prezentuje přístup mimo 3GPP pro [AMF](/mobilnisite/slovnik/amf/) a [SMF](/mobilnisite/slovnik/smf/) 5GC jako logické rozhraní N3. Spojení mezi uživatelským zařízením (UE) a TNAN využívá nativní zabezpečení specifické pro daný přístup (např. WPA3 pro Wi-Fi). Důvěra je navázána mezi TNAN/TNGF a operátorem 5GC, často na základě přihlašovacích údajů TNAN ověřených 3GPP [AAA](/mobilnisite/slovnik/aaa/) serverem nebo [N3IWF](/mobilnisite/slovnik/n3iwf/) pro řídicí rovinu. Provoz uživatelské roviny může proudit přímo z TNAN do [UPF](/mobilnisite/slovnik/upf/), zabezpečený bezpečnostními mechanismy podkladové transportní sítě.

Fungování zahrnuje několik kroků. Nejprve UE objeví a asociuje se s TNAN pomocí standardních procedur pro Wi-Fi nebo Ethernet. Pro přístup k síti UE iniciuje 5G autentizační a registrační procedury. TNGF přeposílá tyto signalizační zprávy k AMF přes rozhraní N2. 5GC ověří UE pomocí 5G-AKA nebo EAP-AKA' a současně validuje, že TNGF/TNAN je důvěryhodná entita. Po úspěšné autentizaci SMF zřídí PDU Session a uživatelská data proudí mezi UE a UPF přes TNAN a TNGF. Úlohou TNAN je poskytnout důvěryhodnou IP konektivitu, což umožňuje bezproblémovou mobilitu a kontinuitu relací mezi 3GPP a přístupy mimo 3GPP a operátorovi aplikovat konzistentní politiky a účtování napříč všemi typy přístupu.

## K čemu slouží

TNAN byl zaveden v 3GPP Release 16 jako součást širší architektury 5G Systému pro plné naplnění vize konvergentního přístupu. Předtím integrace přístupu mimo 3GPP (např. přes ePDG v 4G) často považovala všechny takové přístupy za 'nedůvěryhodné', což vyžadovalo náročné IPsec tunely pro každé spojení UE, což přidávalo režii a složitost. Účelem TNAN je uznat, že mnoho sítí mimo 3GPP, zejména operátorem spravované Wi-Fi nebo partnerské pevné sítě, je z pohledu operátora inherentně důvěryhodných.

Tento koncept řeší problém neefektivního využití zdrojů a latence pro scénáře s důvěryhodným přístupem. Zřízením kotvy důvěry na síťové úrovni (TNGF) umožňuje 5GC obejít tunelování na úrovni jednotlivých UE pro uživatelskou rovinu, což vede k efektivnějšímu přenosu dat. Motivací byl rostoucí význam Wi-Fi 6 a pevného přístupu ve strategiích nasazení 5G, což umožňuje skutečnou konvergenci drátových a bezdrátových technologií. TNAN umožňuje operátorům nabízet jednotný uživatelský zážitek ze služeb 5G bez ohledu na podkladovou přístupovou technologii, zjednodušuje správu sítě a umožňuje nové servisní modely, jako je 5G Fixed Wireless Access (FWA) s nativní integrací do 5G jádra.

## Klíčové vlastnosti

- Umožňuje integraci důvěryhodných Wi-Fi a pevných sítí do 5G Core bez povinných IPsec tunelů pro každé UE
- Využívá funkci Trusted Non-3GPP Gateway Function (TNGF) jako kotvu síťové důvěry a proxy řídicí roviny
- Podporuje bezproblémovou mobilitu a kontinuitu relací mezi 3GPP a důvěryhodným přístupem mimo 3GPP
- Umožňuje 5GC aplikovat konzistentní ověřování, řízení politik a účtování napříč heterogenními přístupy
- Využívá nativní zabezpečení přístupového spoje (např. WPA3) mezi UE a TNAN
- Poskytuje standardizované rozhraní N2 (řídicí rovina) a N3 (uživatelská rovina) směrem k 5GC

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.807** (Rel-16) — 5G Wireline-Wireless Convergence Security Study

---

📖 **Anglický originál a plná specifikace:** [TNAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/tnan/)
