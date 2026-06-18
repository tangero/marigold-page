---
slug: "nrid"
url: "/mobilnisite/slovnik/nrid/"
type: "slovnik"
title: "NRID – Networked Remote Identification"
date: 2025-01-01
abbr: "NRID"
fullName: "Networked Remote Identification"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nrid/"
summary: "Služba umožňující identifikaci a sledování bezpilotních letounů (UAV) neboli dronů prostřednictvím sítě 3GPP. Poskytuje standardizovanou, zabezpečenou a síťovou alternativu k metodám přímého vysílání,"
---

NRID je služba 3GPP pro zabezpečenou, síťovou identifikaci a sledování dronů, která umožňuje integraci s řízením letového provozu a splnění regulatorních požadavků.

## Popis

Networked Remote Identification (NRID) je služba definovaná v rámci 3GPP pro podporu identifikace a sledování bezpilotních leteckých systémů ([UAS](/mobilnisite/slovnik/uas/)), běžně známých jako drony, využívající infrastrukturu mobilní sítě. Funguje jako síťová služba, při které dron vybavený uživatelským zařízením (UE) 3GPP vysílá své identifikační a polohové informace síťové entitě známé jako [USS](/mobilnisite/slovnik/uss/) (UAS Service Supplier) nebo systému [UTM](/mobilnisite/slovnik/utm/) (UAS Traffic Management) prostřednictvím 5G core sítě. Tento přenos je autentizován a zabezpečen pomocí standardních bezpečnostních mechanismů 3GPP, což zajišťuje integritu a důvěrnost dat. Architektura zahrnuje UE (dron), 5G RAN a Core Network (včetně [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/)) a externí entity jako USS/UTM a NRID Management Function, která orchestruje identifikační relace.

Služba funguje tak, že pro přenos NRID dat naváže vyhrazenou [PDU](/mobilnisite/slovnik/pdu/) relaci nebo využije existující. UE dronu periodicky nebo na vyžádání odesílá zprávy Remote ID obsahující klíčové informace, jako je jedinečný identifikátor dronu (např. sériové číslo, ID přidělené leteckým úřadem), jeho aktuální geografická poloha, nadmořská výška, rychlost a poloha řídicí stanice. Tato data jsou zabalena podle definovaných protokolů (např. standard ASTM Remote ID) a přenášena přes user plane sítě 3GPP. Síť může aplikovat specifické zásady QoS, aby zajistila včasné doručení těchto bezpečnostně kritických informací. NRID Management Function, potenciálně umístěná společně s Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)), autorizuje žádost dronu o službu a spravuje asociaci mezi předplatným dronu v 3GPP a jeho přihlašovacími údaji pro vzdálenou identifikaci.

Klíčové komponenty zahrnují UE s podporou NRID (dron), funkce 5G Core Network (AMF pro mobilitu, SMF pro správu relací, [UPF](/mobilnisite/slovnik/upf/) pro přeposílání dat) a NRID Management Function. Ta poslední slouží jako rozhraní mezi sítí 3GPP a externími poskytovateli služeb UAS. Jejím úkolem je autentizovat žádosti o službu NRID, vynucovat politiky (např. ověřit, zda je dron oprávněn létat v určité oblasti) a případně iniciovat navázání PDU relace pro NRID data. Služba podporuje jak periodické hlášení, tak režim dotazu na vyžádání, kdy oprávněné entity jako řízení letového provozu mohou požadovat identifikační data pro konkrétní dron.

Úloha NRID v síti spočívá ve využití všudypřítomného pokrytí, spolehlivosti a zabezpečení mobilních sítí k poskytnutí škálovatelného a standardizovaného řešení vzdálené identifikace. Integruje provoz UAS do národního systému vzdušného prostoru tím, že poskytuje digitální identitu a telemetrický přenos, který je přístupný úřadům a dalším uživatelům vzdušného prostoru. Tento síťový přístup kontrastuje s metodami přímého RF vysílání, nabízí delší dosah, lepší zabezpečení proti falšování a možnost integrovat identifikaci s dalšími komunikačními službami pro UAS (jako je řízení a kontrola) přes stejné síťové připojení. Je základním předpokladem pro pokročilé operace UAS, jako jsou lety za vizuální dohled (BVLOS).

## K čemu slouží

NRID bylo vytvořeno, aby řešilo regulatorní a bezpečnostní požadavky vznikající z rychlého rozšíření komerčních a rekreačních dronů. Letecké úřady po celém světě, jako jsou FAA a EASA, nařídily vzdálenou identifikaci dronů, aby zajistily odpovědnost, bezpečnost a zabezpečení ve sdíleném vzdušném prostoru. Před NRID byla řešení často proprietární, založená na přímém rádiovém vysílání (jako Wi-Fi nebo Bluetooth), které mělo omezený dosah, byla náchylná k rušení a falšování a postrádala integraci s širšími systémy řízení letového provozu.

Primární problém, který NRID řeší, je poskytnutí standardizované, zabezpečené a spolehlivé metody, pomocí které mohou drony vysílat svou identitu a polohu úřadům a dalším uživatelům vzdušného prostoru. Motivací pro jeho vývoj v rámci 3GPP bylo využít stávající a budoucí mobilní sítě (4G, 5G) jako důvěryhodnou, všudypřítomnou komunikační platformu. Tento síťový přístup řeší omezení přímého vysílání tím, že nabízí rozšířené pokrytí, využívá síťovou autentizaci a šifrování pro zabezpečení a umožňuje integraci na backendu s platformami UAS Traffic Management (UTM). Umožňuje centralizované monitorování a vynucování letových pravidel.

Historicky byly počáteční metody identifikace dronů roztříštěné. Vytvoření NRID v 3GPP Release 17 poskytlo globálně standardizovaný rámec, který je v souladu s leteckými standardy (jako je Remote ID od ASTM). To zajišťuje interoperabilitu mezi výrobci dronů, mobilními operátory a poskytovateli služeb řízení letového provozu. Řeší omezení předchozích nesíťových přístupů tím, že umožňuje identifikaci i když je dron daleko od pilota nebo pozemního pozorovatele, což je klíčové pro operace BVLOS, které jsou nezbytné pro doručování, inspekce a další komerční aplikace.

## Klíčové vlastnosti

- Síťový přenos identifikace dronu a telemetrie pomocí user plane 3GPP
- Podpora jak periodického autonomního hlášení, tak dotazu na vyžádání od oprávněných entit
- Integrace s funkcemi 5G core sítě (AMF, SMF, NEF) pro autorizaci služby a správu relací
- Soulad s leteckými standardy pro vzdálenou identifikaci (např. ASTM F3411) pro formát a obsah zpráv
- Využití bezpečnostních mechanismů 3GPP (autentizace, šifrování) k ochraně identifikačních dat
- Podpora diferenciace QoS pro priorizaci bezpečnostně kritických zpráv vzdálené identifikace

## Související pojmy

- [UAS – NF Uncrewed Aerial System Network Function](/mobilnisite/slovnik/uas/)
- [UTM – Uncrewed Aerial System Traffic Management](/mobilnisite/slovnik/utm/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TR 23.754** (Rel-17) — Study on UAS Connectivity, ID & Tracking
- **TS 29.256** (Rel-19) — UAS-NF Stage 3 Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [NRID na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrid/)
