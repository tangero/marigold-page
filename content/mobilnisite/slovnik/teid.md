---
slug: "teid"
url: "/mobilnisite/slovnik/teid/"
type: "slovnik"
title: "TEID – Tunnel End Point Identifier"
date: 2026-01-01
abbr: "TEID"
fullName: "Tunnel End Point Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/teid/"
summary: "Klíčový identifikátor používaný v sítích GPRS, EPS a 5GS k jednoznačnému označení GTP tunelů mezi síťovými uzly. Umožňuje směrování uživatelských dat a řídicích zpráv jádrovou sítí tím, že identifikuj"
---

TEID je klíčový identifikátor používaný v sítích GPRS, EPS a 5GS k jednoznačnému označení GTP tunelů mezi síťovými uzly za účelem směrování uživatelských dat a řídicích zpráv ke správným koncovým bodům.

## Popis

Tunnel End Point Identifier (TEID) je základním kamenem protokolu [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) používaného napříč 3GPP mobilními sítěmi od 3G po 5G. Jedná se o 32bitové pole přítomné v hlavičce paketů [GTP-U](/mobilnisite/slovnik/gtp-u/) (uživatelská rovina) a [GTP-C](/mobilnisite/slovnik/gtp-c/) (řídicí rovina). Architektonicky je GTP tunel logické point-to-point spojení vytvořené mezi dvěma uzly podporujícími GTP, například mezi Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v 4G, nebo mezi [UPF](/mobilnisite/slovnik/upf/) a [SMF](/mobilnisite/slovnik/smf/)/UPF v 5G. TEID jednoznačně identifikuje konkrétní koncový bod tunelu na přijímacím uzlu. Zásadní je, že oba konce tunelu mají své vlastní lokální hodnoty TEID; odesílatel nastavuje hodnotu TEID, kterou příjemce pro daný konkrétní tunel nebo kontext přenosového kanálu (bearer) přidělil.

Jeho funkce je zásadní pro mobilitu založenou na GTP. Když je v 3G vytvořen Packet Data Protocol (PDP) kontext nebo v 4G připojení PDN/EPS bearer, signalizace v řídicí rovině (GTP-C) přidělí TEID pro tunely v uživatelské rovině (GTP-U). Například během procedury připojení (attach) v LTE MME nařídí SGW vytvořit relaci a SGW přidělí TEID pro svou downlink stranu tunelu S1-U směrem k eNodeB a další TEID pro svou uplink stranu tunelu S5/S8 směrem k PGW. Tyto TEID jsou vyměňovány prostřednictvím zpráv GTP-C. Následně každý paket uživatelských dat nese v hlavičce GTP-U cílový TEID. Přijímací uzel (např. eNodeB nebo UPF) používá tento TEID jako přímý klíč pro vyhledání přidruženého kontextu přenosového kanálu, který obsahuje všechny potřebné informace pro zpracování paketu, jako jsou parametry QoS a další směrovací krok.

Jeho role přesahuje jednoduché adresování. TEID je primárním mechanismem pro multiplexování přenosových kanálů. Jediný síťový uzel (jako SGW) spravuje tisíce současných tunelů, každý pro jiné UE nebo jiný QoS tok. TEID umožňuje uzlu okamžitě demultiplexovat příchozí GTP pakety do správného interního kontextu bez nutnosti prohlížet vnitřní IP pakety. V 5G Core zůstává princip stejný, ačkoli architektura přešla na rozhraní služeb (service-based) v řídicí rovině, zatímco GTP-U zůstává převládající v uživatelské rovině mezi UPF a (R)AN. Konstrukce TEID zajišťuje stavové, spojením orientované přeposílání, které je optimalizované pro mobilitu a vynucování QoS napříč mobilní jádrovou sítí.

## K čemu slouží

TEID byl vytvořen k řešení problému správy více současných paketových datových relací pro miliony uživatelů škálovatelným a efektivním způsobem v rámci mobilních jádrových sítí. Před GPRS byla data primárně přepojována okruhy, což bylo pro trhaný (bursty) IP provoz neefektivní. Zavedení paketového přepojování vyžadovalo tunelovací mechanismus pro přeposílání uživatelských IP paketů mezi síťovými uzly při zachování kontextu relace předplatitele, QoS a účtovacích pravidel během jeho pohybu.

Protokol GTP, s TEID jako svým srdcem, byl navržen, aby tuto tunelovací schopnost poskytl. Řeší klíčová omezení: odděluje uživatelskou IP adresu (která se může měnit) od směrování uvnitř jádrové sítě, umožňuje plynulou mobilitu tím, že umožňuje přeměrování tunelů při pohybu uživatele, a poskytuje jednoduchý, rychlý vyhledávací mechanismus pro přeposílací roviny. TEID konkrétně řeší problém multiplexování – umožňuje, aby jediná dvojice IP adresa/port na síťovém uzlu obsluhovala tisíce odlišných uživatelských relací. Jeho vytvoření bylo motivováno potřebou standardizovaného, robustního tunelovacího protokolu, který by mohl podporovat model "stále připojené" IP konektivity zásadní pro mobilní internetové služby, od raného GPRS až po moderní 5G.

## Klíčové vlastnosti

- 32bitový jednoznačný identifikátor pro koncové body GTP tunelů
- Používán v protokolech řídicí (GTP-C) i uživatelské (GTP-U) roviny GTP
- Umožňuje multiplexování tisíců přenosových kanálů (bearerů) na jediném rozhraní síťového uzlu
- Umožňuje oddělení uživatelského IP adresování od směrování v jádrové síti
- Nezbytný pro správu mobility a procedury předávání hovoru (handover)
- Poskytuje rychlý vyhledávací klíč pro kontext přenosového kanálu při přeposílání v uživatelské rovině

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.119** (Rel-19) — GTP for GLR in 3GPP Networks
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.276** (Rel-19) — EPS S101/S121/S103 Interfaces Stage 3
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- … a dalších 14 specifikací

---

📖 **Anglický originál a plná specifikace:** [TEID na 3GPP Explorer](https://3gpp-explorer.com/glossary/teid/)
