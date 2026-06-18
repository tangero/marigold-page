---
slug: "gtp-u"
url: "/mobilnisite/slovnik/gtp-u/"
type: "slovnik"
title: "GTP-U – GPRS Tunnelling Protocol for User Plane"
date: 2025-01-01
abbr: "GTP-U"
fullName: "GPRS Tunnelling Protocol for User Plane"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gtp-u/"
summary: "Uživatelská rovina protokolové rodiny GTP, používaná k tunelování skutečných paketů uživatelských dat mezi síťovými uzly, jako je RAN a brány jádra sítě. Zapouzdřuje IP pakety do GTP hlaviček pro přen"
---

GTP-U je uživatelská rovina protokolové rodiny GTP, která tuneluje pakety uživatelských dat mezi síťovými uzly tím, že zapouzdřuje IP pakety pro přenos přes mobilní páteřní síť.

## Popis

GTP-U je protokol uživatelské roviny v rámci rodiny [GTP](/mobilnisite/slovnik/gtp/), odpovědný za zapouzdřování a přeposílání uživatelského datového provozu mezi síťovými prvky v mobilních sítích 3GPP. Funguje přes [UDP](/mobilnisite/slovnik/udp/) port 2152 a používá se od systémů 3G až po 5G k tunelování IP paketů mezi entitami, jako je Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v UMTS, nebo eNodeB a Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) v LTE, a (R)[AN](/mobilnisite/slovnik/an/) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G. GTP-U přidává ke každému paketu uživatelských dat hlavičku, která obsahuje identifikátor koncového bodu tunelu (TEID), pořadové číslo a volitelné rozšiřující hlavičky. TEID je jedinečný identifikátor přiřazený během signalizace řídicí roviny (přes GTP-C), který určuje koncový bod tunelu, což umožňuje přijímacímu uzlu odstranit zapouzdření paketu a přeposlat jej na správný cíl, například na jiný síťový uzel nebo do externí paketové datové sítě.

Z architektonického hlediska GTP-U vytváří point-to-point tunely, které logicky spojují entity uživatelské roviny a vytvářejí virtuální potrubí pro data účastníka. Tyto tunely jsou zřizovány a spravovány řídicí rovinou (GTP-C nebo jinými protokoly, jako je PFCP v 5G), ale používají se výhradně pro přenos dat. Protokol podporuje jak IPv4, tak IPv6 přenášená data a může transportovat jakýkoli provoz založený na IP, včetně prohlížení webu, streamování videa a IoT dat. Mezi klíčové mechanismy patří číslování sekvencí pro detekci ztráty paketů nebo doručení mimo pořadí, přičemž opakovaný přenos je typicky řešen protokoly vyšších vrstev, jako je TCP. GTP-U také podporuje zprávy správy cesty, jako je Echo Request/Response, pro ověření životaschopnosti tunelu mezi uzly.

Během provozu, když uživatelské zařízení (UE) odešle IP paket, je tento paket prvním GTP-U uzlem (např. eNodeB) zapouzdřen s GTP hlavičkou obsahující TEID odpovídající přenosovému kanálu (bearer) daného UE. Tento zapouzdřený paket je pak směrován přes IP páteřní síť k dalšímu GTP-U uzlu (např. SGW), který použije TEID k identifikaci přidruženého přenosového kanálu, odstraní GTP hlavičku a přepošle původní IP paket směrem k jeho cíli, případně přes další tunelování. Při předávání spojení (handover) jsou GTP-U tunely dynamicky přesměrovány na nové koncové body, aby byla zachována kontinuta relace bez ztráty paketů. V 5G zůstává GTP-U primárním protokolem uživatelské roviny mezi (R)AN a UPF, s vylepšeními pro podporu nových funkcí, jako je síťové dělení (network slicing), kde mohou být tunely asociovány s konkrétními identifikátory řezů, a s integrací Packet Forwarding Control Protocol (PFCP) pro správu relací.

## K čemu slouží

GTP-U byl vytvořen, aby poskytl efektivní a standardizovanou metodu pro tunelování uživatelských dat přes mobilní paketové jádro sítě, což řeší výzvu přenosu IP paketů mezi distribuovanými síťovými uzly při současné podpoře mobility účastníků. Před GTP-U používaly rané systémy GPRS kombinovaný protokol GTP, který nebyl optimalizován pro vysokorychlostní přeposílání dat. Oddělení GTP-U umožnilo vytvoření odlehčeného, specializovaného protokolu uživatelské roviny, který minimalizuje režii a latenci, což je klíčové pro služby v reálném čase a aplikace s vysokou propustností. Řešil potřebu škálovatelného tunelovacího mechanismu, který by zvládl miliony současných datových relací napříč vyvíjejícími se technologiemi radiového přístupu.

Motivace pro GTP-U vycházela z přechodu na plně IP sítě v 3GPP Release 4 a novějších, kde se efektivní datový přenos stal prvořadým. Zapouzdřením uživatelských IP paketů do GTP-U hlaviček může jádro sítě směrovat provoz na základě TEID místo IP adres účastníků, což zjednodušuje správu mobility a umožňuje funkce jako bezproblémové předávání spojení. Tento tunelovací přístup také poskytuje vrstvu abstrakce, která umožňuje, aby vnitřní topologie sítě zůstala skrytá před externími paketovými datovými sítěmi, čímž zvyšuje bezpečnost a flexibilitu. Návrh GTP-U nad UDP/IP zajišťuje nízkou režii zpracování a kompatibilitu s existující IP infrastrukturou, což jej činí vhodným pro datové roviny s vysokým objemem provozu.

Historicky se GTP-U vyvíjel, aby uspokojil rostoucí požadavky na datové rychlosti a nízkou latenci, zejména s nástupem LTE a 5G. Řeší omezení dřívějších tunelovacích metod podporou funkcí, jako jsou rozšíření pro kompresi hlaviček, vylepšené číslování sekvencí pro integritu a integrace s mechanismy kvality služeb (QoS). V 5G zůstává GTP-U nadále nezbytný pro tunelování uživatelské roviny, i když se řídicí rovina přesouvá k novým protokolům, a to díky své prověřené spolehlivosti a efektivitě. Jeho účel sahá až k umožnění pokročilých síťových architektur, jako je edge computing, kde mohou být funkce uživatelské roviny nasazeny blíže k radiovému přístupu a GTP-U tunely usnadňují datové cesty s nízkou latencí.

## Klíčové vlastnosti

- Tunelování uživatelské roviny pro zapouzdřování a přeposílání IP paketů přes mobilní sítě
- Používá pro přenos UDP port 2152, což poskytuje přeposílání dat s nízkou latencí
- Spoléhá se na identifikátory koncových bodů tunelu (TEID) pro dynamické směrování tunelů
- Podporuje pořadová čísla pro detekci ztráty paketů a doručení ve správném pořadí
- Kompatibilní s IPv4 a IPv6 přenášenými daty a síťovými protokoly
- Obsahuje zprávy správy cesty (např. Echo Request) pro monitorování tunelů

## Související pojmy

- [GTP-C – GPRS Tunnelling Protocol for Control Plane](/mobilnisite/slovnik/gtp-c/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)
- [TEID – Tunnel End Point Identifier](/mobilnisite/slovnik/teid/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles
- **TS 37.470** (Rel-19) — W1 Interface Introduction for ng-eNB
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.470** (Rel-19) — F1 Interface Introduction

---

📖 **Anglický originál a plná specifikace:** [GTP-U na 3GPP Explorer](https://3gpp-explorer.com/glossary/gtp-u/)
