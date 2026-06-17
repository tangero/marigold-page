---
slug: "f-teid"
url: "/mobilnisite/slovnik/f-teid/"
type: "slovnik"
title: "F-TEID – Fully Qualified Tunnel Endpoint Identifier"
date: 2025-01-01
abbr: "F-TEID"
fullName: "Fully Qualified Tunnel Endpoint Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/f-teid/"
summary: "Datová struktura používaná v GTP tunelech k jednoznačné identifikaci koncového bodu tunelu kombinací identifikátoru koncového bodu tunelu (TEID) s IP adresou tohoto bodu. Je zásadní pro směrování pake"
---

F-TEID je datová struktura, která jednoznačně identifikuje koncový bod GTP tunelu kombinací TEID s IP adresou, což umožňuje směrování uživatelských dat mezi síťovými uzly v systémech 3GPP.

## Popis

Fully Qualified Tunnel Endpoint Identifier (F-TEID) je klíčová datová struktura v mobilních sítích 3GPP, která umožňuje vytváření a správu tunelů protokolu [GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol ([GTP](/mobilnisite/slovnik/gtp/)). GTP tunel je logická cesta používaná pro přenos provozu v uživatelské rovině (např. IP paketů) mezi síťovými uzly, například mezi eNodeB a Serving Gateway (SGW) nebo mezi SGW a Packet Data Network Gateway (PGW) v síti 4G, nebo v scénářích interoperability se sítěmi 5G. F-TEID jednoznačně identifikuje jeden konec takového tunelu tím, že obsahuje dvě povinné složky: identifikátor koncového bodu tunelu (TEID) a IP adresu uzlu, který tento koncový bod hostuje. TEID je 32bitová lokálně významná hodnota zvolená přijímajícím koncovým bodem, ale ve spojení s IP adresou se F-TEID stává globálně jednoznačným, což umožňuje odesílajícímu koncovému bodu přesně adresovat pakety.

Během provozu, při procedurách jako Připojení (Attach), Předání (Handover) nebo Zřízení přenosového kanálu (Bearer Establishment), si síťové uzly vyměňují F-TEID v řídicích zprávách GTP (např. Create Session Request/Response). Například když SGW zakládá GTP tunel s PGW, PGW přidělí TEID pro svůj koncový bod a odešle svůj F-TEID (TEID + IP adresa PGW) do SGW. SGW pak tento F-TEID používá jako cíl pro všechny pakety uživatelských dat, které v rámci tohoto konkrétního přenosového kanálu odesílá směrem k PGW. Naopak SGW poskytne svůj vlastní F-TEID PGW pro opačný směr. Tato obousměrná výměna zajišťuje, že oba konce přesně vědí, kam provoz odesílat. F-TEID může také obsahovat volitelná pole, jako je IPv6 adresa nebo typ rozhraní (např. S1-U, S5/S8), což poskytuje dodatečný kontext.

Role F-TEID je klíčová na mnoha rozhraních: S1-U mezi eNodeB a SGW, S5/S8 mezi SGW a PGW, a dokonce i v sítích 5G pro N3 (mezi gNB a [UPF](/mobilnisite/slovnik/upf/)) a N9 (mezi UPF), pokud je použit [GTP-U](/mobilnisite/slovnik/gtp-u/). Podporuje mobilitu tím, že umožňuje aktualizovat koncové body tunelu během předání – cílový uzel poskytne nový F-TEID a zdrojový uzel podle toho přesměruje provoz. Také umožňuje více přenosových kanálů na jedno uživatelské zařízení (UE), protože každý přenosový kanál má své vlastní vyhrazené F-TEID. V sítích 5G, zatímco pro řízení rozhraní N4 se používá PFCP a [F-SEID](/mobilnisite/slovnik/f-seid/), GTP-U s F-TEID zůstává převládající pro tunelování v uživatelské rovině, což zajišťuje zpětnou kompatibilitu a bezproblémovou interoperabilitu se sítěmi 4G.

## K čemu slouží

F-TEID byl vytvořen, aby vyřešil problém jednoznačné identifikace koncových bodů tunelů škálovatelným a směrovatelným způsobem v mobilních sítích založených na [GTP](/mobilnisite/slovnik/gtp/). Před jeho formalizací mohlo být řízení tunelů nejednoznačné, pokud byl použit pouze lokálně významný TEID, zejména v sítích s více uzly nebo složitým směrováním. Kombinací TEID s IP adresou F-TEID zajišťuje, že GTP pakety mohou být správně směrovány přes IP sítě do zamýšleného cílového uzlu, a to i v rozsáhlých distribuovaných nasazeních. To bylo nezbytné pro vývoj od 3G k 4G EPC, kde oddělení uživatelské a řídicí roviny a zvýšené nároky na data vyžadovaly robustní tunelovací mechanismy.

Jeho zavedení ve verzi 8 spolu s Evolved Packet System (EPS) řešilo omezení starších, méně strukturovaných tunelovacích identifikátorů. F-TEID standardizoval způsob, jakým jsou koncové body tunelů inzerovány a používány, což usnadňuje interoperabilitu mezi zařízeními od různých výrobců. Podporuje vývoj sítě tím, že je rozšiřitelný (např. přidáním podpory IPv6) a že funguje na různých rozhraních. F-TEID umožňuje klíčové funkce, jako je správa mobility (předání mezi základnovými stanicemi nebo uzly jádra sítě), multi-homing a diferenciace provozu prostřednictvím vyhrazených přenosových kanálů. V sítích 5G zůstává zásadní pro tunelování v uživatelské rovině, zejména ve scénářích zahrnujících interoperabilitu mezi 4G a 5G nebo duální konektivitu, a zajišťuje, že uživatelská data plynule proudí přes heterogenní síťové segmenty.

## Klíčové vlastnosti

- Globálně jednoznačný identifikátor kombinující TEID a IP adresu
- Povinný pro zřízení a správu GTP tunelu
- Používaný na více rozhraních (např. S1-U, S5/S8, N3, N9)
- Podporuje mobilitu prostřednictvím dynamických aktualizací koncových bodů
- Umožňuje více přenosových kanálů na jedno UE s oddělenými F-TEID
- Rozšiřitelný o informace jako IPv6 a typ rozhraní

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)
- [F-SEID – Fully Qualified Session Endpoint Identifier](/mobilnisite/slovnik/f-seid/)

## Definující specifikace

- **TS 23.214** (Rel-19) — Control and User Plane Separation for EPC
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [F-TEID na 3GPP Explorer](https://3gpp-explorer.com/glossary/f-teid/)
