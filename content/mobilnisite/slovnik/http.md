---
slug: "http"
url: "/mobilnisite/slovnik/http/"
type: "slovnik"
title: "HTTP – Hypertext Transfer Protocol"
date: 2026-01-01
abbr: "HTTP"
fullName: "Hypertext Transfer Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/http/"
summary: "Protokol aplikační vrstvy pro distribuované, kolaborativní, hypermediální informační systémy. Je základem datové komunikace pro World Wide Web a je primárním protokolem používaným pro přenos webového"
---

HTTP je primární protokol aplikační vrstvy pro přenos webového provozu, včetně HTML, přes mobilní sítě 3GPP a slouží jako základ datové komunikace pro World Wide Web.

## Popis

Hypertext Transfer Protocol (HTTP) je bezestavový protokol aplikační vrstvy v rámci sady internetových protokolů, definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 9110 a následující) a všudypřítomně odkazovaný ve specifikacích 3GPP. Funguje na modelu klient-server, kde klient (typicky webový prohlížeč na uživatelském zařízení, UE) posílá požadavky serveru, který následně vrací odpovědi. V síti 3GPP jsou HTTP zprávy přenášeny jako užitečné zatížení uvnitř IP paketů. Tyto IP pakety jsou transportovány přes datové přenosové kanály sítě, které jsou zřizovány a spravovány procedurami připojení k paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)) jádra sítě – za použití protokolů jako [GTP](/mobilnisite/slovnik/gtp/) mezi bránou ([PGW](/mobilnisite/slovnik/pgw/)/[UPF](/mobilnisite/slovnik/upf/)) a rádiovou přístupovou sítí.

HTTP funguje prostřednictvím řady metod požadavků (GET, POST, PUT, DELETE atd.) a stavových kódů (200 OK, 404 Not Found). GET požadavek na webovou stránku zahájí TCP spojení (nebo použije existující přes perzistentní spojení HTTP/1.1 nebo proudy HTTP/2), které je transportováno přes IP vrstvu mobilní sítě. Odpověď serveru obsahuje hlavičky s metadaty a tělo zprávy, často [HTML](/mobilnisite/slovnik/html/) dokument. Samotný protokol si není vědom podrobností podkladové mobilní sítě; nicméně síť implementuje různé funkce okolo HTTP provozu. Mezi ně patří Řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) pro aplikaci pravidel na základě detekce provozu, Hluboká kontrola paketů (DPI) pro povědomí o službách a Šablony toků provozu (TFT) pro vazbu na přenosové kanály.

Specifikace 3GPP odkazují na HTTP v četných kontextech: jako transport pro konfigurační protokoly jako OMA DM pro správu zařízení, pro zpřístupnění servisních schopností (SCEF/NEF), v rozhraní Ut pro provisioning a jako protokol pro četná northbound API (např. Nnrf, Nudm v 5GC), která jsou založena na HTTP/2. Přechod na architekturu založenou na službách (SBA) v jádru sítě 5G explicitně používá HTTP/2 s užitečným zatížením JSON pro komunikaci mezi síťovými funkcemi (NF). Dále je HTTP klíčový pro techniky optimalizace doručování obsahu diskutované v 3GPP, jako je transparentní cacheování a adaptace video streamování (DASH), které mají za cíl zlepšit efektivitu a uživatelský zážitek přes rádiové rozhraní.

## K čemu slouží

HTTP je nedílnou součástí standardů 3GPP, protože mobilní sítě jsou navrženy tak, aby poskytovaly IP konektivitu, a web (prostřednictvím HTTP) tvoří masivní část IP provozu. Účel protokolu v rámci 3GPP je dvojí: za prvé jako přenašeč aplikačních dat koncového uživatele (webový browsing, video streamování, aktualizace aplikací), a za druhé jako protokol pro interní a managementová rozhraní sítě. Jeho zařazení zajišťuje, že síťová architektura může efektivně zpracovávat vzorce provozu typu požadavek/odpověď, spravovat relace, aplikovat odpovídající kvalitu služeb a účtovat datové využití.

Historický kontext představuje konvergence telekomunikací a internetu. Rané mobilní datové služby používaly specializované protokoly. Přijetí HTTP signalizovalo posun směrem k plně IP síti, která se bezproblémově integruje s internetem. Toto řešilo omezení předchozích dat na principu přepojování okruhů a proprietárních protokolů, které byly neefektivní pro přerušovaný webový provoz. Standardizace kolem HTTP umožnila obrovskému ekosystému internetových aplikací fungovat na mobilních zařízeních bez úprav. V pozdějších vydáních použití HTTP/2 pro rozhraní jádra 5G vyřešilo problémy s efektivitou signalizace a flexibilitou ve srovnání s dřívějšími binárními telekomunikačními protokoly (jako Diameter), což umožnilo agilnější, cloud-nativní síťovou architekturu.

## Klíčové vlastnosti

- Model požadavek/odpověď klient-server s definovanými metodami (GET, POST)
- Bezestavový protokol, přičemž stav je spravován prostřednictvím cookies nebo relací na aplikační vrstvě
- Používá TCP pro spolehlivý transport, přičemž HTTP/3 zavádí QUIC přes UDP
- Podporuje vyjednávání obsahu, direktivy pro cacheování a perzistentní spojení
- Základ pro RESTful API a architekturu 5G založenou na službách (SBA)
- Rozšiřitelný prostřednictvím hlaviček a může přenášet jakýkoli typ digitálního obsahu jako užitečné zatížení

## Související pojmy

- [HTTPS – Hyper Text Transfer Protocol Secure](/mobilnisite/slovnik/https/)
- [IP – IP Packet eXchange](/mobilnisite/slovnik/ip/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 22.242** (Rel-19) — DRM Service Requirements
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.281** (Rel-20) — MCVideo Functional Architecture and Flows
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- … a dalších 72 specifikací

---

📖 **Anglický originál a plná specifikace:** [HTTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/http/)
