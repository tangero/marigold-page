---
slug: "lbi"
url: "/mobilnisite/slovnik/lbi/"
type: "slovnik"
title: "LBI – Linked Bearer Identity"
date: 2025-01-01
abbr: "LBI"
fullName: "Linked Bearer Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lbi/"
summary: "Identifikátor, který spojuje vyhrazený bearer s jeho přidruženým výchozím bearerem v rámci stejného PDN připojení. Vytváří hierarchický vztah, kde výchozí bearer slouží jako kotva řídicí roviny a k ně"
---

LBI je identifikátor 3GPP, který spojuje vyhrazený bearer s jeho výchozím bearerem v rámci PDN připojení a vytváří jejich hierarchický vztah.

## Popis

Linked Bearer Identity (LBI) je základní identifikátor v architektuře správy bearerů a QoS toků 3GPP Evolved Packet Core (EPC) a 5G Core (5GC). Jedná se o číselnou hodnotu, která jednoznačně identifikuje výchozí bearer v rámci připojení k paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)), ke kterému je vyhrazený bearer propojen. Každé PDN připojení zřízené uživatelským zařízením (UE) musí mít právě jeden výchozí bearer. Tento výchozí bearer zajišťuje IP konektivitu a slouží jako trvalá kotva řídicí roviny pro dané PDN připojení. Všechny další beavery vytvořené v rámci stejného PDN připojení pro specifické služby (jako VoIP nebo video streamování) jsou vyhrazené beavery a každý musí obsahovat LBI odkazující na jeho nadřazený výchozí bearer.

Z architektonického hlediska je LBI přiřazeno sítí během zřizování výchozího beareru a je známo klíčovým funkcím jádra sítě: Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v EPC, Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)), PDN Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a později Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5GC. Když je zřizován vyhrazený bearer – typicky na základě detekovaných datových toků služby vyvoláno funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) – žádost o vytvoření (např. Bearer Resource Command) obsahuje LBI. To síti říká, v jakém kontextu PDN připojení má být nový bearer vytvořen. Vyhrazený bearer přebírá klíčové atributy od výchozího beareru, jako je typ PDN (IPv4, IPv6) a IP adresa PGW/SMF, ale má svůj vlastní odlišný QoS profil definovaný svým QCI (QoS Class Identifier) a případně hodnotami GBR.

Provozně LBI umožňuje efektivní správu bearerů a vynucování politik. Všechny beavery sdílející stejné LBI patří do stejného PDN připojení a tedy sdílejí stejnou IP adresu(y) UE. Toto propojení umožňuje síti aplikovat agregované politiky, jako je Aggregate Maximum Bit Rate (APN-AMBR), napříč všemi beavery daného PDN připojení. APN-AMBR omezuje celkovou přenosovou rychlost, kterou může UE spotřebovat přes svůj výchozí a všechny k němu propojené vyhrazené beavery pro daný APN. Když je výchozí bearer modifikován nebo uvolněn, LBI poskytuje nezbytný kontext pro odpovídající správu všech k němu propojených vyhrazených bearerů. Například uvolnění výchozího beareru (např. při odpojení PDN) spustí uvolnění všech vyhrazených bearerů propojených přes toto LBI.

V systému 5G se koncept vyvíjí, ale zachovává podobné principy. Místo EPS beareru s LBI používá 5G QoS toky v rámci PDU session. Ekvivalentní propojení je dosaženo implicitně, protože všechny QoS toky patří do konkrétní PDU session, která má jedinečné PDU Session ID. Nicméně samotný parametr LBI je stále používán v interworkingových scénářích mezi 4G a 5G (např. během handoverů s rozhraním N26) pro mapování EPS bearerů na 5G QoS toky a naopak, aby byla zachována kontinuita služeb. LBI tedy zůstává kritickým prvkem pro udržení logické hierarchie a kontextu spojení v uživatelské rovině v sítích 3GPP.

## K čemu slouží

Linked Bearer Identity bylo vytvořeno, aby řešilo složitost správy více souběžných datových toků s různými požadavky na QoS pro jediné připojení UE k jednomu APN. Rané paketové datové systémy poskytovaly jediný, monolitický datový kanál na APN připojení. S diverzifikací služeb vznikla potřeba podporovat simultánní aplikace – jako prohlížení webu (best-effort), VoIP (nízká latence) a video streamování (vysoká přenosová rychlost) – z nichž každá vyžaduje odlišné zacházení z hlediska QoS v rámci stejné IP session. Vytváření zcela samostatných PDN připojení pro každou službu by bylo neefektivní, spotřebovávalo by další IP adresy a znamenalo signalizační režii.

LBI umožňuje elegantní a efektivní model 'hierarchie bearerů'. Řeší problém, jak přidružit více specializovaných datových cest (vyhrazených bearerů) ke společné kotvě řízení a konektivity (výchozímu beareru). Bez LBI by síť neměla způsob, jak logicky seskupit beavery, což by znemožnilo vynucování agregovaných politik jako APN-AMBR nebo provádění koordinované správy životního cyklu (např. smazání všech bearerů pro APN, když uživatel přejede mimo pokrytí). LBI poskytuje tento nezbytný mechanismus seskupení.

Dále LBI zjednodušuje řízení politik a účtování. PCRF/PCF může autorizovat více vyhrazených bearerů pro různé datové toky služeb (např. na základě hluboké kontroly paketů nebo žádosti aplikace) a propojit je se stejným kontextem výchozího beareru pomocí LBI. To umožňuje granulární QoS a účtovací pravidla na úrovni jednotlivých toků při zachování jednotného účtovacího a politického kontextu pro uživatelovu session s konkrétním poskytovatelem služeb (APN). Také to usnadňuje mobilitu; během handoverů může síť efektivně přenést stav celého PDN připojení identifikací výchozího beareru a jeho propojených vyhrazených bearerů prostřednictvím LBI. LBI je v podstatě pojivo, které umožňuje sítím 3GPP nabízet sofistikovanou, multislužební IP konektivitu s diferencovanou kvalitou, což je základním kamenem vize All-IP sítě.

## Klíčové vlastnosti

- Jednoznačně identifikuje výchozí bearer v rámci PDN připojení.
- Je zahrnuto v signalizaci pro vytváření, modifikaci a mazání vyhrazených bearerů.
- Umožňuje hierarchické seskupení bearerů pro vynucování agregovaných politik (např. APN-AMBR).
- Nezbytné pro koordinovanou správu životního cyklu všech bearerů v PDN připojení.
- Používá se při interworkingu 4G-5G pro mapování EPS bearerů na 5G QoS toky.
- Známé funkcím jádra sítě (MME, SGW, PGW, SMF) pro správu kontextu session.

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [LBI na 3GPP Explorer](https://3gpp-explorer.com/glossary/lbi/)
