---
slug: "teid-u"
url: "/mobilnisite/slovnik/teid-u/"
type: "slovnik"
title: "TEID-U – Tunnel Endpoint Identifier, user plane"
date: 2025-01-01
abbr: "TEID-U"
fullName: "Tunnel Endpoint Identifier, user plane"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/teid-u/"
summary: "Jedinečný identifikátor pro GTP tunely uživatelské roviny mezi síťovými uzly (např. SGW a eNB/PGW). Umožňuje multiplexování více toků uživatelských dat v rámci jediného spojení transportní vrstvy, čím"
---

TEID-U je jedinečný identifikátor pro GTP tunely uživatelské roviny mezi síťovými uzly, který umožňuje multiplexování více datových toků v rámci jednoho transportního spojení pro správné směrování paketů a správu relací.

## Popis

Identifikátor koncového bodu tunelu pro uživatelskou rovinu (TEID-U) je základní součástí architektury protokolu [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)), konkrétně definovaný pro uživatelskou rovinu ([GTP-U](/mobilnisite/slovnik/gtp-u/)). Jedná se o 32bitové pole, které jednoznačně identifikuje koncový bod GTP tunelu na síťovém uzlu pro datový provoz konkrétního uživatele. Když uživatelské zařízení (UE) naváže datovou relaci, síť vytvoří GTP tunely pro přenos IP paketů uživatele. Například v LTE EPC existuje GTP-U tunel mezi Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a další mezi SGW a eNodeB. Každému koncovému bodu těchto tunelů je přijímajícím uzlem přidělen TEID-U. Tento TEID-U je následně signalizací řídicí roviny ([GTP-C](/mobilnisite/slovnik/gtp-c/)) sdělen vysílajícímu uzlu, takže když odesílatel zapouzdří uživatelské IP pakety do hlavičky GTP-U, vyplní pole [TEID](/mobilnisite/slovnik/teid/) hodnotou TEID-U přiřazenou přijímačem. To umožňuje přijímajícímu uzlu správně demultiplexovat příchozí pakety a předat je příslušnému kontextu přenosového kanálu pro cílové UE.

TEID-U funguje ve spojení s IP adresou uživatele a číslem [UDP](/mobilnisite/slovnik/udp/) portu pro GTP-U (obvykle 2152). Tato kombinace vytváří jedinečný soket pro tunelovaný provoz. Hlavní úlohou TEID-U je rozlišit mezi více simultánními GTP tunely, které mohou mezi dvěma uzly sdílet stejnou síťovou transportní vrstvu (IP adresu a UDP port). Například jediný SGW může obsluhovat tisíce UE, každé s potenciálně více přenosovými kanály (např. výchozí a vyhrazené kanály). Každý kanál vyžaduje vlastní GTP-U tunel, a tedy vlastní pár TEID-U (jeden pro uplink, jeden pro downlink). Hodnota lokálního TEID-U je volena přijímající entitou a musí být v kontextu tohoto přijímajícího uzlu pro danou IP adresu a UDP port jedinečná.

Z architektonického hlediska je TEID-U spravován řídicí rovinou. Během procedur, jako je zřízení nebo modifikace kanálu, přenášejí zprávy GTP-C (např. Create Session Request/Response) informační prvky TEID-U. Uzel iniciující tunel (např. SGW pro rozhraní S5-U směrem k PGW) zahrne do požadavku svůj vlastní TEID-U pro směr uplink. Protějškový uzel (např. PGW) tento TEID-U uloží pro odesílání downlink paketů a vygeneruje svůj vlastní TEID-U pro směr uplink, který odešle zpět v odpovědi. Tato obousměrná výměna stanoví identifikátory tunelu pro oba směry. TEID-U je klíčový pro události mobility, jako je předávání spojení. Běli předání spojení založeného na X2 v LTE odešle zdrojový eNB TEID-U(y) datových rádiových kanálů cílovému eNB ve zprávě HANDOVER REQUEST, což umožní cílovému eNB začít okamžitě po předání přijímat downlink data od SGW a minimalizovat tak ztrátu dat.

## K čemu slouží

TEID-U byl vytvořen k řešení základního problému multiplexování a směrování paketů uživatelských dat v rámci tunelové páteřní sítě, konkrétně v rámci 3GPP GPRS a později Evolved Packet System (EPS). Před standardizovanými tunelovacími protokoly by alternativní mechanismy směrování paketů mohly spoléhat pouze na IP směrovací tabulky nebo složité okruhy vrstvy 2, které jsou neefektivní pro správu milionů simultánních, mobilních uživatelských relací se specifickými požadavky na kvalitu služeb (QoS). Protokol GTP a v něm obsažený TEID-U poskytuje odlehčenou, na relaci orientovanou nadstavbu, která abstrahuje IP tok uživatele od podkladové transportní IP sítě.

Jeho vytvoření bylo motivováno potřebou škálovatelné a efektivní správy uživatelské roviny. Použitím jednoduchého 32bitového identifikátoru s lokálním rozsahem pro koncový bod tunelu se síť může vyhnout prohlížení vnitřních IP hlaviček uživatelských paketů pro rozhodování o přeposílání na každém skoku, čímž zlepšuje výkon. Umožňuje také plynulou mobilitu a kontinuitu relace; když se uživatel pohybuje, síť může jednoduše aktualizovat mapování TEID-U na kotvící bráně (např. PGW), aby ukazovalo na nový SGW nebo přístupový uzel, aniž by došlo k přerušení uživatelské IP relace. Tento design je ústřední pro koncept 'tunelové' mobility v 3GPP sítích, který odděluje stabilní IP kotvící bod uživatele od měnících se bodů rádiového přístupu.

## Klíčové vlastnosti

- 32bitový identifikátor pro koncové body GTP-U tunelu
- Jednoznačně identifikuje přenosový kanál uživatelské roviny v rámci GTP-U asociace
- Lokálně přidělován přijímající GTP-U entitou
- Vyměňován mezi uzly prostřednictvím signalizace řídicí roviny GTP-C
- Umožňuje multiplexování více tunelů přes jediné UDP/IP spojení
- Nezbytný pro směrování downlink paketů a přeposílání specifické pro kanál

## Související pojmy

- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)
- [GTP-C – GPRS Tunnelling Protocol for Control Plane](/mobilnisite/slovnik/gtp-c/)

## Definující specifikace

- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [TEID-U na 3GPP Explorer](https://3gpp-explorer.com/glossary/teid-u/)
