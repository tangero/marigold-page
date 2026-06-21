---
slug: "tngf"
url: "/mobilnisite/slovnik/tngf/"
type: "slovnik"
title: "TNGF – Trusted Non-3GPP Gateway Function"
date: 2026-01-01
abbr: "TNGF"
fullName: "Trusted Non-3GPP Gateway Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tngf/"
summary: "Funkce jádra 5G sítě, která zajišťuje zabezpečený a důvěryhodný přístup pro uživatelské zařízení (UE) připojující se přes přístupové sítě mimo 3GPP, jako je Wi-Fi. Funguje jako brána, která autentizuj"
infografika: "/assets/slovnik/tngf.svg"
infografikaAlt: "Schéma architektury 5G sítě se zvýrazněním TNGF"
---

TNGF (Trusted Non-3GPP Gateway Function) je funkce jádra 5G sítě, která zajišťuje zabezpečený a důvěryhodný přístup pro zařízení připojující se přes sítě mimo 3GPP, jako je Wi-Fi, provádí jejich autentizaci a vytváří IPsec tunely do jádra sítě.

## Popis

Funkce Trusted Non-3GPP Gateway Function (TNGF) je klíčovou součástí architektury jádra 5G sítě (5GC), konkrétně definovanou pro Non-3GPP InterWorking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) v kontextu důvěryhodného přístupu mimo 3GPP. Jejím hlavním úkolem je umožnit zabezpečené a řízené připojení pro UE využívající přístupové technologie mimo 3GPP, především důvěryhodné Wi-Fi sítě. Architektonicky se TNGF nachází v uživatelské i řídicí rovině a rozhraní se s dalšími funkcemi jádra sítě. Na referenčním bodě N1 směrem k UE ukončuje rozhraní N1 přes přístup mimo 3GPP a spravuje signalizační spojení. Vytváří s UE [IPsec](/mobilnisite/slovnik/ipsec/) Security Associations ([SA](/mobilnisite/slovnik/sa/)) pro zabezpečené tunely pro provoz řídicí roviny (N1) i uživatelské roviny (N3). TNGF se připojuje k funkci Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) přes rozhraní [N2](/mobilnisite/slovnik/n2/) pro řídicí procedury a k User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) přes rozhraní N3 pro přenos dat.

Operačně, když UE iniciuje přístup přes důvěryhodnou síť mimo 3GPP, vyhledá a vybere TNGF. UE a TNGF provedou vzájemnou autentizaci a vytvoří IPsec tunely. TNGF poté funguje jako proxy, přeposílající registrační a relací management signalizaci UE do jádra 5G sítě přes AMF. Je zodpovědná za zapouzdřování a rozbalování paketů uživatelské roviny mezi IPsec tunelem a [GTP-U](/mobilnisite/slovnik/gtp-u/) tunelem N3 směrem k UPF. TNGF také komunikuje s Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a Unified Data Management (UDM) pro autentizaci na základě přihlašovacích údajů (např. pomocí 5G-AKA nebo EAP-AKA').

Klíčovým aspektem TNGF je její označení 'důvěryhodná', což znamená, že operátor jádra 5G sítě má vztah důvěry s poskytovatelem přístupové sítě mimo 3GPP. Tato důvěra může být založena na roamingu nebo přímém vlastnictví, což jádru sítě umožňuje do určité míry spoléhat na zabezpečení přístupové sítě, přičemž TNGF stále vynucuje vlastní zabezpečení na vrstvě IPsec. TNGF podporuje procedury mobility a kontinuity relací, umožňující předávání mezi přístupem 3GPP (např. NG-RAN) a důvěryhodným přístupem mimo 3GPP bez ztráty PDU Session. Je základním prvkem pro dosažení cíle konvergence v 5G, poskytujícím jednotný zážitek z jádra sítě bez ohledu na podkladovou přístupovou technologii.

## K čemu slouží

TNGF byla zavedena ve 3GPP Release 16, aby formálně definovala a standardizovala bránovou funkci pro důvěryhodný přístup mimo 3GPP v rámci 5G systému (5GS). Před 5G bylo propojení mimo 3GPP (např. přes ePDG v EPS) často považováno za nedůvěryhodný přístup vyžadující robustní ukončení zabezpečení na bráně. Vytvoření TNGF řeší rostoucí význam vysoce kvalitního, operátorského Wi-Fi a dalších pevných bezdrátových přístupů jako nedílných součástí služeb mobilního operátora. Řeší problém poskytování plynulého, zabezpečeného a politicky konzistentního přístupu ke službám jádra 5G sítě přes tyto alternativní sítě.

Motivace vychází z potřeby skutečně přístupově agnostického poskytování služeb. Operátoři chtěli využít svá Wi-Fi nasazení nebo partnerství s poskytovateli Wi-Fi jako důvěryhodné rozšíření pokrytí svého 5G rádiového signálu, zejména pro vnitřní prostředí a scénáře pevného bezdrátového přístupu. TNGF poskytuje standardizovanou architekturu, která zajišťuje zabezpečení (povinným IPsec), podporuje specifické funkce 5G, jako je síťové dělení a QoS přes spoj mimo 3GPP, a umožňuje plynulou mobilitu. Řeší omezení předchozích řešení propojení mimo 3GPP tím, že je nativně integrována do Service-Based Architecture (SBA) 5G, využívá stejné autentizační frameworky a správu politik (přes PCF) jako přístup 3GPP, čímž odstraňuje funkční bariéry.

## Klíčové vlastnosti

- Ukončuje rozhraní N1 (řídicí rovina) a N3 (uživatelská rovina) přes důvěryhodný přístup mimo 3GPP
- Vytváří a udržuje IPsec Security Associations s UE pro důvěrnost a integritu
- Funguje jako signalizační přenoska mezi UE a AMF jádra 5G sítě
- Zapouzdřuje/rozpaketovává uživatelská data mezi IPsec tunely UE a GTP-U tunely N3 směrem k UPF
- Podporuje autentizační procedury 5G (5G-AKA, EAP-AKA') prostřednictvím interakce s AUSF/UDM
- Umožňuje mobilitu a kontinuitu relací mezi přístupem 3GPP a důvěryhodným přístupem mimo 3GPP

## Související pojmy

- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.413** (Rel-19) — NGAP for Non-3GPP Access
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.807** (Rel-16) — 5G Wireline-Wireless Convergence Security Study
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)

---

📖 **Anglický originál a plná specifikace:** [TNGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/tngf/)
