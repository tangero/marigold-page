---
slug: "twag"
url: "/mobilnisite/slovnik/twag/"
type: "slovnik"
title: "TWAG – Trusted WLAN Access Gateway"
date: 2025-01-01
abbr: "TWAG"
fullName: "Trusted WLAN Access Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/twag/"
summary: "Trusted WLAN Access Gateway (TWAG) je funkce brány jádrové sítě v rámci důvěryhodné přístupové sítě WLAN (TWAN). Poskytuje IP konektivitu a správu mobility pro uživatelské zařízení (UE) přistupující k"
---

TWAG je brána jádrové sítě v důvěryhodné přístupové síti WLAN (Trusted WLAN Access Network), která zajišťuje IP konektivitu a správu mobility pro zařízení přistupující k jádru 3GPP prostřednictvím důvěryhodné sítě WLAN a ukončuje rozhraní S2a.

## Popis

Trusted [WLAN](/mobilnisite/slovnik/wlan/) Access Gateway (TWAG) je klíčová funkční entita definovaná v architektuře 3GPP pro důvěryhodný přístup mimo 3GPP. Nachází se v rámci důvěryhodné přístupové sítě WLAN ([TWAN](/mobilnisite/slovnik/twan/)) a slouží jako brána mezi sítí WLAN a jádrem EPC (Evolved Packet Core) 3GPP. Jejím hlavním úkolem je navazovat a spravovat relace IP konektivity pro uživatelská zařízení (UE), která se připojují prostřednictvím důvěryhodné sítě WLAN, jako je například Wi-Fi hotspot spravovaný operátorem. TWAG implementuje síťovou část referenčního bodu S2a, který spojuje TWAN s bránou [PGW](/mobilnisite/slovnik/pgw/) (Packet Data Network Gateway) v EPC. Toto rozhraní může být realizováno pomocí protokolu [GTP](/mobilnisite/slovnik/gtp/) ([GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol) nebo PMIPv6 (Proxy Mobile IPv6), což umožňuje flexibilní scénáře nasazení a spolupráci s existujícími prvky jádrové sítě.

Z architektonického hlediska TWAG spolupracuje s funkcemi [TWAP](/mobilnisite/slovnik/twap/) (Trusted WLAN [AAA](/mobilnisite/slovnik/aaa/) Proxy) a Trusted WLAN Access Point (TWAP) v rámci TWAN. Když se UE připojí k důvěryhodné síti WLAN, autentizace a autorizace jsou zpracovány prostřednictvím TWAP a serveru AAA 3GPP. Po úspěšné autentizaci je TWAG zodpovědná za vytvoření přenosové cesty pro datový provoz UE. Vytváří tunel (GTP nebo [PMIP](/mobilnisite/slovnik/pmip/)) přes rozhraní S2a k bráně PGW, která slouží jako kotvící bod pro IP relaci UE. Tento tunel přenáší veškerý provoz v uživatelské rovině, zajišťuje bezproblémovou kontinuitu služeb a umožňuje UE přístup k paketovým datovým službám (např. IMS, internet), jako by bylo připojeno prostřednictvím 3GPP rádiové přístupové sítě.

TWAG vykonává základní funkce správy mobility a relací. Spravuje vazbu mezi lokální IP adresou UE v síti WLAN a její IP adresou v jádrové síti (přidělenou PGW). Při událostech mobility, jako je předání spojení mezi různými přístupovými body WLAN v rámci stejné TWAN nebo mezi přístupem WLAN a 3GPP, TWAG spolupracuje s jádrovou sítí na aktualizaci přenosové cesty s minimálním narušením. Také komunikuje s funkcí PCRF (Policy and Charging Rules Function) prostřednictvím TWAP nebo přímo (v závislosti na architektuře) za účelem vynucení pravidel kvality služeb (QoS) a tarifikace přijatých z jádrové sítě. To zajišťuje, že datové toky služeb jsou zpracovávány odpovídajícím způsobem podle předplatného uživatele a požadované služby.

Stručně řečeno, TWAG je centrální brána v uživatelské rovině v architektuře pro spolupráci s důvěryhodnou sítí WLAN. Abstrahuje podkladovou technologii WLAN od jádrové sítě a prezentuje ji vůči EPC jako důvěryhodnou přístupovou síť. Poskytnutím standardizovaných rozhraní a protokolů umožňuje bezpečnou, bezproblémovou a politikami řízenou integraci výkonných sítí WLAN do portfolia služeb mobilního operátora, čímž tvoří základní kámen pro strategie včasného přesunu provozu na Wi-Fi (Wi-Fi offloading) a konvergence pevných a mobilních sítí.

## K čemu slouží

TWAG byl zaveden, aby vyřešil problém bezproblémové a bezpečné integrace Wi-Fi sítí řízených operátorem do mobilního paketového jádra 3GPP. Před jeho standardizací byla síť Wi-Fi převážně považována za nedůvěryhodnou externí IP přístupovou síť, což vyžadovalo od uživatelů vytváření samostatných připojení (často prostřednictvím VPN) a vedlo k nespojitému uživatelskému zážitku s přerušenou kontinuitou relace. Hlavní motivací bylo využít rostoucího nasazení kvalitní infrastruktury WLAN jako komplementární rádiové přístupové technologie k buněčným sítím, což umožňuje přesun datového provozu (offloading) a zvýšení kapacity.

Vytvoření TWAG jako součásti širšího konceptu důvěryhodné přístupové sítě WLAN (TWAN) ve verzi 3GPP Release 11 bylo hnací silou potřeby standardizované architektury. Tato architektura by umožnila mobilním operátorům zacházet s jejich vlastními nebo partnerskými Wi-Fi sítěmi jako s důvěryhodným rozšířením jejich rádiové přístupové sítě. Klíčový problém, který řešila, byl nedostatek standardizované bránové funkce, která by mohla ukončovat protokoly jádrové sítě (GTP/PMIP) ze strany WLAN, což by umožnilo těsné propojení s EPC pro autentizaci, vynucování politik a tarifikaci. To byl významný pokrok oproti dříve definovanému modelu nedůvěryhodného přístupu, který spoléhal na tunely IPsec iniciované ze strany UE (eSWAG), což bylo složitější a méně škálovatelné.

Poskytnutím síťové brány TWAG umožnil několik klíčových schopností: bezproblémový přístup ke službám paketových dat 3GPP (jako je IMS) přes WLAN, podporu síťově řízené mobility a předávání spojení mezi přístupem WLAN a 3GPP a uplatňování konzistentních pravidel politik a tarifikace bez ohledu na přístupovou technologii. To usnadnilo vizi operátorů o konvergenci pevných a mobilních sítí (FMC) a položilo základy pro integrovanější přístup v pozdějších systémech 5G. Vyřešil omezení předchozích neintegrovaných přístupů tím, že poskytl standardizovanou, bezpečnou a efektivní cestu pro provoz v uživatelské rovině z důvěryhodné sítě WLAN přímo do mobilního jádra.

## Klíčové vlastnosti

- Ukončuje rozhraní S2a (GTPv2 nebo PMIPv6) směrem k bráně PGW (Packet Data Network Gateway) v EPC
- Poskytuje funkci brány v uživatelské rovině pro důvěryhodný přístup WLAN, směruje datový provoz UE do/z jádrové sítě
- Podporuje správu mobility, včetně předávání spojení mezi sítí WLAN a přístupem 3GPP (např. LTE)
- Vynucuje pravidla QoS a tarifikační pravidla přijatá od PCRF prostřednictvím TWAP
- Spravuje vazbu IP relace na jedno UE mezi lokální adresou ve WLAN a IP adresou v jádrové síti
- Spolupracuje s TWAP na signalizaci v řídicí rovině a autentizaci

## Související pojmy

- [TWAN – Trusted WLAN Access Network](/mobilnisite/slovnik/twan/)
- [TWAP – Trusted WLAN AAA Proxy](/mobilnisite/slovnik/twap/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)

## Definující specifikace

- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [TWAG na 3GPP Explorer](https://3gpp-explorer.com/glossary/twag/)
