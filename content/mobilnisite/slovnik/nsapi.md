---
slug: "nsapi"
url: "/mobilnisite/slovnik/nsapi/"
type: "slovnik"
title: "NSAPI – Network layer Service Access Point Identifier"
date: 2025-01-01
abbr: "NSAPI"
fullName: "Network layer Service Access Point Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nsapi/"
summary: "Číselný identifikátor, který jednoznačně označuje konkrétní síťový přístupový bod služby (NSAP) v mobilní stanici a v síti. Používá se k rozlišení mezi více simultánními kontexty paketového datového p"
---

NSAPI je číselný identifikátor používaný k rozlišení mezi více simultánními PDP kontexty v mobilní síti, což umožňuje nezávislou správu různých datových relací.

## Popis

Identifikátor přístupového bodu služby síťové vrstvy (NSAPI) je klíčový identifikátor v paketově orientovaných systémech 3GPP, jako jsou [GPRS](/mobilnisite/slovnik/gprs/), UMTS a EPS. Jde o hodnotu, typicky v rozsahu 0 až 15, která jednoznačně identifikuje konkrétní instanci síťového přístupového bodu služby ([NSAP](/mobilnisite/slovnik/nsap/)) přidruženou ke kontextu paketového datového protokolu ([PDP](/mobilnisite/slovnik/pdp/)). NSAPI používá jak mobilní stanice (UE), tak síťové uzly, jako jsou [SGSN](/mobilnisite/slovnik/sgsn/) a GGSN, k odkazování na konkrétní datovou relaci. Při aktivaci PDP kontextu je NSAPI přidělen a zůstává s tímto kontextem spojen po celou dobu jeho životnosti, což umožňuje síťové vrstvě směrovat data a spravovat signalizaci pro tuto konkrétní relaci nezávisle na ostatních.

Provozně NSAPI funguje ve spojení s identifikátorem koncového bodu tunelu ([TEID](/mobilnisite/slovnik/teid/)) a PDP adresou (např. IP adresou). Během aktivace PDP kontextu UE navrhne hodnotu NSAPI, kterou síť přijme nebo může přidělit jinou. Tento NSAPI se pak používá ve všech následných zprávách souvisejících s tímto PDP kontextem, jako jsou žádosti o modifikaci nebo deaktivaci. V uživatelské rovině pomáhá NSAPI při multiplexování a demultiplexování datových paketů patřících k různým PDP kontextům přes stejný fyzický rádiový bearer. Například smartphone může mít jeden PDP kontext pro prohlížení internetu (NSAPI=5) a další pro IMS hlas (NSAPI=6), každý s odlišnými parametry QoS; NSAPI zajišťuje, že data pro každou službu jsou správně zpracována.

NSAPI je klíčovou součástí protokolových zásobníků definovaných ve specifikacích jako 23.060. Používá se ve zprávách správy relací ([SM](/mobilnisite/slovnik/sm/)) mezi UE a SGSN a je také mapován na identifikátory v rozhraní Gn/Gp (jako TEID) mezi SGSN a GGSN. Toto mapování umožňuje end-to-end korelaci datové relace napříč více síťovými elementy. Omezený rozsah NSAPI (0-15) omezuje počet simultánních PDP kontextů na jedno UE, ale to je pro většinu případů použití obvykle dostačující. Jeho role je zásadní pro podporu více aktivních datových relací, což umožňuje funkce jako vyhrazené bearery v LTE a síťové segmenty (network slicing) v 5G, kde různé segmenty nebo služby vyžadují samostatné logické kanály.

## K čemu slouží

NSAPI byl zaveden k řešení problému správy více souběžných paketových datových relací na jediném mobilním zařízení. Před jeho standardizací rané datové služby postrádaly robustní mechanismus pro rozlišení různých datových toků, což omezovalo zařízení v podstatě na jeden datový kontext v daný okamžik. NSAPI poskytuje jednoduchý, ale účinný identifikátor, který umožňuje síti a UE současně obsluhovat několik [PDP](/mobilnisite/slovnik/pdp/) kontextů, každý potenciálně s různými požadavky na QoS, například jeden pro best-effort webové prohlížení a další pro nízkolatenční VoIP.

Jeho vytvoření bylo hnací silou evoluce od základního [GPRS](/mobilnisite/slovnik/gprs/) k pokročilejším službám UMTS, kde uživatelé požadovali simultánní přístup k různorodým aplikacím. NSAPI umožňuje síti aplikovat specifické politiky, účtování a QoS na kontext. Například IMS hlasový hovor může být upřednostněn před synchronizací e-mailů na pozadí, protože každý má svůj vlastní PDP kontext označený NSAPI. Tato granularita řeší omezení monolitických datových relací a podporuje složité nabídky služeb moderních mobilních sítí. NSAPI zůstává relevantní v 4G a 5G jako součást konceptů EPS beareru a PDU relace, čímž zajišťuje zpětnou kompatibilitu a konzistentní principy správy relací.

## Klíčové vlastnosti

- Jednoznačně identifikuje instanci PDP kontextu/NSAP v rámci UE a sítě
- Číselný rozsah hodnot 0-15, s konkrétními rezervovanými hodnotami (např. 0 pro signalizaci)
- Používá se v signalizaci správy relací (Session Management) pro aktivaci, modifikaci a deaktivaci kontextu
- Umožňuje multiplexování více datových relací přes sdílené rádiové prostředky
- Mapuje se na další identifikátory, jako je TEID, pro korelaci mezi uzly
- Podporuje nezávislou aplikaci profilu QoS na každý NSAPI

## Související pojmy

- [NSAP – Network Service Access Point](/mobilnisite/slovnik/nsap/)
- [TEID – Tunnel End Point Identifier](/mobilnisite/slovnik/teid/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.065** (Rel-4) — GPRS Subnetwork Dependent Convergence Protocol
- **TS 25.324** (Rel-19) — Broadcast/Multicast Control Protocol
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.065** (Rel-19) — GPRS SNDCP Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [NSAPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/nsapi/)
