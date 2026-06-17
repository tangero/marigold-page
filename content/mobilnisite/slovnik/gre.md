---
slug: "gre"
url: "/mobilnisite/slovnik/gre/"
type: "slovnik"
title: "GRE – Generic Routing and Encapsulation"
date: 2025-01-01
abbr: "GRE"
fullName: "Generic Routing and Encapsulation"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gre/"
summary: "Generic Routing and Encapsulation (GRE) je tunelovací protokol používaný k zapouzdření široké škály protokolů síťové vrstvy uvnitř virtuálních point-to-point spojení přes IP síť. V 3GPP se používá pro"
---

GRE je tunelovací protokol používaný v sítích 3GPP pro zapouzdření paketů uživatelské a řídicí roviny mezi síťovými funkcemi přes IP spoje pro přenosovou síť (backhaul) a vzájemné propojení.

## Popis

Generic Routing and Encapsulation (GRE) je odlehčený, bezestavový tunelovací protokol definovaný [IETF](/mobilnisite/slovnik/ietf/) (RFC 2784, RFC 2890). V rámci architektur 3GPP je přijat jako transportní mechanismus pro zapouzdření paketů mezi síťovými entitami. GRE funguje tak, že vezme původní paket (přenášený paket, který může být různých protokolů, jako IP, [MPLS](/mobilnisite/slovnik/mpls/) nebo Ethernet) a zapouzdří jej do nového vnějšího IP paketu. Vnější IP hlavička obsahuje zdrojové a cílové IP adresy koncových bodů tunelu. Mezi vnější IP hlavičkou a původním přenášeným paketem je vložena GRE hlavička. Tato minimální hlavička (typicky 4-8 bajtů) obsahuje klíčová pole, jako je pole typu protokolu, které označuje protokol zapouzdřeného přenášeného paketu (např. 0x0800 pro IPv4), a volitelně pole klíče pro identifikaci jednotlivých toků provozu v rámci tunelu.

V systémech 3GPP je role GRE významná v transportu uživatelské roviny. Například v Evolved Packet System (EPS) se GRE používá jako jeden ze zapouzdřovacích protokolů na rozhraní S1-U mezi eNodeB a Serving Gateway (S-GW) a na rozhraních S5/S8 mezi S-GW a Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)). Zapouzdřuje IP pakety (nebo Ethernetové rámce) uživatele pro přenos přes IP páteř operátora. Každý přenosový kanál (bearer, logický kanál se specifickou QoS) je typicky mapován na unikátní GRE klíč, což umožňuje přijímacímu uzlu identifikovat kontext přenosového kanálu, ke kterému paket patří, bez hluboké analýzy paketů. To umožňuje zpracování a směrování na úrovni přenosového kanálu.

Architektura protokolu je jednoduchá a efektivní. Neposkytuje inherentní zabezpečení (jako šifrování) ani spolehlivé doručení (jako číslování a potvrzení); tyto funkce musí být v případě potřeby poskytnuty jinými protokoly (např. [IPsec](/mobilnisite/slovnik/ipsec/) pro zabezpečení). Tato jednoduchost je jeho předností, nabízí nízkou režii a vysoký výkon. V systémech 5G, zatímco novější protokoly jako [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol User Plane ([GTP-U](/mobilnisite/slovnik/gtp-u/)) jsou běžnější, GRE zůstává definovanou volbou a používá se v konkrétních nasazeních a scénářích pro spolupráci. Jeho bezestavová povaha znamená, že koncové body tunelu neudržují složité stavové automaty pro samotný tunel, což jej činí robustním a škálovatelným pro přenos velkého množství provozu uživatelské roviny v přenosových sítích mobilního backhaulu.

## K čemu slouží

GRE byl přijat do specifikací 3GPP, aby poskytl jednoduchou, standardizovanou a efektivní metodu pro tunelování uživatelských dat mezi distribuovanými síťovými uzly přes IP transportní síť. Vývoj směrem k All-IP sítím ve 3GPP Release 8 (EPS) si vyžádal náhradu dřívějších, složitějších tunelovacích metod používaných v [GPRS](/mobilnisite/slovnik/gprs/). GRE tuto potřebu řešil tím, že nabídl odlehčený zapouzdřovací protokol, který je široce podporován v hardwaru směrovačů, což vede k vysokému výkonu při přeposílání.

Klíčové problémy, které řeší, jsou abstrakce přenášeného protokolu a identifikace provozu. Mobilní uživatelské pakety mohou být IPv4, IPv6 nebo PPP. GRE může zapouzdřit kterýkoli z nich, čímž vytvoří jednotnou transportní vrstvu. Dále pole klíče GRE poskytuje přímočarý mechanismus pro demultiplexování více logických spojení (přenosových kanálů EPS) přes jeden fyzický nebo IP tunel mezi dvěma uzly. To je zásadní pro aplikaci správné QoS politiky a směrování každého paketu do příslušného kontextu uživatelské relace na koncovém bodě tunelu. Jeho vytvoření a přijetí bylo motivováno snahou o flexibilní, mezi dodavateli interoperabilní a nákladově efektivní tunelovací řešení, které využívá všudypřítomnou IP infrastrukturu, což je v souladu s posunem průmyslu k plošnějším, IP-centrickým architekturám mobilních sítí.

## Klíčové vlastnosti

- Odlehčené zapouzdření s minimální režií hlavičky
- Umí tunelovat širokou škálu protokolů síťové vrstvy (podpora více protokolů)
- Používá pole Klíč (Key) pro demultiplexování více logických toků (např. přenosových kanálů EPS)
- Bezestavový provoz bez signalizace pro zřízení nebo zrušení tunelu
- Široce podporován v síťovém hardwaru pro vysokovýkonné přeposílání
- Definován jako transportní volba pro rozhraní uživatelské roviny v 3GPP (např. S1-U, S5/S8)

## Související pojmy

- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)

## Definující specifikace

- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3
- **TS 29.276** (Rel-19) — EPS S101/S121/S103 Interfaces Stage 3
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.361** (Rel-19) — LWIP Encapsulation Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [GRE na 3GPP Explorer](https://3gpp-explorer.com/glossary/gre/)
