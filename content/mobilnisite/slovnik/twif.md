---
slug: "twif"
url: "/mobilnisite/slovnik/twif/"
type: "slovnik"
title: "TWIF – Trusted WLAN Interworking Function"
date: 2026-01-01
abbr: "TWIF"
fullName: "Trusted WLAN Interworking Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/twif/"
summary: "TWIF je síťová funkce jádra 5G, která umožňuje bezpečnou a bezproblémovou interoperabilitu mezi systémy 3GPP 5G a důvěryhodnými přístupovými sítěmi mimo 3GPP, jako je WLAN. Funguje jako bezpečnostní b"
---

TWIF je síťová funkce jádra 5G, která zajišťuje bezpečnou interoperabilitu a překlad protokolů pro uživatelské zařízení (UE) pro přístup ke službám 5G přes důvěryhodné sítě WLAN, jako je Wi-Fi.

## Popis

Trusted [WLAN](/mobilnisite/slovnik/wlan/) Interworking Function (TWIF) je klíčová komponenta v architektuře jádra 5G (5GC), konkrétně definovaná pro interoperabilitu sítě mimo 3GPP. Funguje jako síťová funkce ([NF](/mobilnisite/slovnik/nf/)), která poskytuje standardizované a bezpečné rozhraní pro připojení uživatelského zařízení (UE) k 5GC prostřednictvím důvěryhodné bezdrátové lokální sítě (WLAN), jako je například Wi-Fi síť spravovaná operátorem nebo podnikem. TWIF ukončuje referenční body N1, [N2](/mobilnisite/slovnik/n2/) a N3 přes přístup mimo 3GPP, čímž efektivně propojuje přístupovou síť WLAN s řídicí a uživatelskou rovinou 5GC. Na straně sítě komunikuje s dalšími funkcemi jádra, jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) přes N2 pro signalizaci řízení, Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) přes rozhraní N4 pro politiky uživatelské roviny a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) pro autentizační údaje.

Architektonicky se TWIF skládá ze dvou hlavních logických entit: Trusted WLAN Access Point ([TWAP](/mobilnisite/slovnik/twap/)) a Trusted WLAN [AAA](/mobilnisite/slovnik/aaa/) Proxy (TWAP). TWAP zajišťuje protokoly specifické pro WLAN na nižší vrstvě a navazuje zabezpečený tunel s UE založený na IPsec/IKEv2 nebo TLS. TWAP funguje jako proxy server pro autentizaci, autorizaci a účtování (AAA), komunikuje s 3GPP AAA Serverem (součást UDM) a provádí autentizaci dle standardů 5G pomocí metody 5G Authentication and Key Agreement (5G-AKA) nebo EAP-AKA'. Tím je zajištěno, že UE je autentizováno se stejnými přihlašovacími údaji a úrovní zabezpečení jako při přístupu přes 3GPP rádiové rozhraní.

Při provozu, když se UE pokusí připojit přes důvěryhodnou síť WLAN, naváže s TWIF zabezpečený tunel (IPsec nebo TLS). TWIF zprostředkovává proces primární autentizace s 5GC, přenáší zprávy Extensible Authentication Protocol (EAP) mezi UE a 3GPP AAA Serverem. Po úspěšné autentizaci TWIF zaregistruje UE u AMF, čímž umožní správu mobility a relací. Pro provoz uživatelské roviny funguje TWIF jako bod pro překlad síťových adres (NAT) nebo jako ukončovací bod N3 pro User Plane Function (UPF), směrující datové pakety mezi WLAN a datovou sítí 5GC. Také vynucuje politiky přijaté od Policy Control Function (PCF), jako jsou pravidla kvality služeb (QoS) a účtování, čímž zajišťuje konzistentní uživatelský zážitek napříč typy přístupu.

Jeho role je klíčová pro konvergovaný přístup, umožňuje operátorům přesměrovávat provoz na Wi-Fi sítě při zachování zabezpečení jádrové sítě, správy účastníků a kontinuity služeb. Integruje WLAN do architektury 5G založené na službách, čímž z ní činí spravovaný a důvěryhodný typ přístupu namísto nedůvěryhodné externí sítě.

## K čemu slouží

TWIF byl vytvořen pro řešení rostoucí potřeby bezproblémové a bezpečné integrace výkonných sítí WLAN do ekosystému 5G. Před vydáním 3GPP Release 16 byl přístup mimo 3GPP (jako Wi-Fi) často považován za nedůvěryhodnou síť, což vyžadovalo, aby UE navázalo tunel podobný VPN (přes Non-3GPP Interworking Function, N3IWF) pro zabezpečený přístup, což přidávalo složitost a režii. Pro Wi-Fi sítě spravované operátorem nebo certifikované, které splňují specifické bezpečnostní požadavky, byl tento model nedůvěryhodného přístupu neefektivní.

Účelem TWIF je definovat „důvěryhodnou“ cestu přístupu mimo 3GPP, kde je samotná přístupová síť považována za bezpečnou, čímž odpadá potřeba zabezpečovacích IPsec tunelů pro každé UE. Tím se snižuje signalizační zátěž, doba navazování spojení a výpočetní režie na straně UE i sítě. Řeší problém poskytnutí zjednodušeného, operátorské úrovně Wi-Fi zážitku, který je plně integrován se službami jádra 5G, včetně autentizace, řízení politik, účtování a podpory mobility. To umožňuje nové případy užití, jako je pevný bezdrátový přístup (FWA) přes Wi-Fi, bezproblémový přechod mezi 5G NR a Wi-Fi a efektivní řízení provozu.

Historicky byla interoperabilita s WLAN definována v dřívějších vydáních (např. důvěryhodný přístup založený na S2a v EPS), ale tyto nebyly nativně integrovány do nové architektury 5GC založené na službách. TWIF ve vydání Release 16 přepracoval tuto interoperabilitu pro éru 5G a sladil ji s principy cloud-nativního přístupu, síťového řezání a jednotného rámce politik. Odstraňuje omezení předchozích přístupů tím, že poskytuje nativní síťovou funkci 5GC se standardními rozhraními založenými na službách (např. Ntwif), což umožňuje automatizaci, škálovatelnost a konzistentní vystavení služeb.

## Klíčové vlastnosti

- Funguje jako ukončovací bod pro rozhraní N1 (NAS), N2 (NGAP) a N3 (uživatelská rovina) přes důvěryhodný přístup mimo 3GPP
- Podporuje autentizaci dle standardů 5G (5G-AKA, EAP-AKA') prostřednictvím integrace s 3GPP AAA Serverem a UDM
- Navazuje zabezpečené spojení s UE pomocí IPsec/IKEv2 nebo TLS v závislosti na modelu důvěry
- Umožňuje bezproblémovou mobilitu a kontinuitu relací mezi přístupem přes 3GPP a důvěryhodnou síť WLAN
- Vynucuje pravidla řízení politik a účtování (PCC) přijatá od PCF pro provoz uživatelské roviny
- Funguje jako User Plane Function (UPF) pro rozhraní N3, zajišťující směrování paketů a označování QoS

## Související pojmy

- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.413** (Rel-19) — NGAP for Non-3GPP Access
- **TS 29.502** (Rel-19) — 5G System; Nsmf Service Based Interface; Stage 3
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)

---

📖 **Anglický originál a plná specifikace:** [TWIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/twif/)
