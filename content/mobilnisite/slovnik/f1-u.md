---
slug: "f1-u"
url: "/mobilnisite/slovnik/f1-u/"
type: "slovnik"
title: "F1-U – F1 User Plane Interface"
date: 2025-01-01
abbr: "F1-U"
fullName: "F1 User Plane Interface"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/f1-u/"
summary: "F1-U je uživatelská rovina rozhraní mezi centrální jednotkou gNB (gNB-CU) a distribuovanou jednotkou gNB (gNB-DU) v 5G NR. Přenáší pakety uživatelských dat (IP pakety) přes GTP-U tunely, což umožňuje"
---

F1-U je uživatelská rovina rozhraní mezi centrální jednotkou gNB (gNB-CU) a distribuovanou jednotkou gNB (gNB-DU), která přenáší pakety uživatelských dat přes GTP-U tunely pro flexibilní nasazení 5G RAN.

## Popis

Rozhraní F1-U je uživatelská rovina protějšku k [F1-C](/mobilnisite/slovnik/f1-c/) v rámci disintegrované architektury gNB podle 3GPP. Poskytuje datovou cestu pro uživatelský provoz mezi uživatelskou rovinou [CU](/mobilnisite/slovnik/cu/) (CU-UP) a [DU](/mobilnisite/slovnik/du/). Rozhraní je navrženo pro přenos zapouzdřených paketů uživatelských dat pomocí [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol pro uživatelskou rovinu ([GTP-U](/mobilnisite/slovnik/gtp-u/)) přes transportní vrstvu [UDP](/mobilnisite/slovnik/udp/)/IP. Tento tunelovací mechanismus umožňuje multiplexování datových toků od více uživatelských zařízení (UE) a přenosových kanálů přes jednu asociaci F1-U mezi CU-UP a DU.

Operačně jsou pro každý zřízený datový rádiový přenosový kanál ([DRB](/mobilnisite/slovnik/drb/)) přes rozhraní F1-U zřízeny jeden nebo více GTP-U tunelů. CU-UP, který hostuje vrstvu [PDCP](/mobilnisite/slovnik/pdcp/) pro uživatelskou rovinu, provádí funkce jako komprese hlaviček, šifrování a ochrana integrity. Následně přeposílá zpracované datové jednotky protokolu PDCP (PDU) do DU přes příslušný GTP-U tunel. DU, odpovědný za vrstvy RLC, MAC a PHY, tyto PDCP PDU přijímá, v případě potřeby je segmentuje (na RLC), plánuje jejich přenos (na MAC) a nakonec je vysílá přes rádiové rozhraní k uživatelskému zařízení (UE). Pro uplink data platí obrácená cesta.

Architektura F1-U je definována jako nezávislá na F1-C, což umožňuje směrování uživatelského provozu potenciálně přes různé síťové cesty pro optimalizaci. Toto oddělení je klíčové pro umožnění doručování dat s vysokou propustností a nízkou latencí. Rozhraní podporuje přesměrování dat během procedur předávání spojení pro minimalizaci ztráty dat. Dále je návrh F1-U v souladu s požadavky síťového řezání, protože různé toky QoS mohou být mapovány na různé DRB a následně přenášeny přes F1-U s odpovídající prioritizací v rámci transportní sítě.

## K čemu slouží

Rozhraní F1-U bylo vyvinuto pro usnadnění oddělení uživatelské roviny, které vyžaduje rozdělení CU-DU v 5G. V monolitických 4G eNB byly zpracování uživatelských dat a rádiový přenos těsně svázány v rámci stejného hardwaru, což omezovalo možnosti nasazení. F1-U umožňuje fyzické a logické oddělení funkce zpracování uživatelské roviny (v CU-UP) od funkce rádiového vysílání/příjmu (v DU).

Toto oddělení řeší několik klíčových problémů. Umožňuje síťovým operátorům centralizovat zpracování uživatelské roviny v nákladově efektivních datových centrech (fondy CU), čímž dosahují statistických multiplexních zisků a zjednodušují implementaci pokročilých funkcí, jako je edge computing. DU mohou zůstat jako jednodušší, potenciálně hromadně vyráběné rádiové jednotky nasazené na lokalitách buněk. Tato architektura snižuje požadavky na šířku pásma přístupové části sítě (fronthaul) ve srovnání s přísnějším rozdělením, jako je CPRI, protože F1-U přenáší částečně zpracovaná paketová data namísto nezpracovaných IQ vzorků.

Vytvoření F1-U spolu s F1-C bylo motivováno potřebou virtualizace a cloudifikace RAN. Definováním standardního paketového rozhraní uživatelské roviny umožnila 3GPP implementaci CU-UP jako virtuální síťové funkce (VNF) nebo cloudové nativní síťové funkce (CNF) na komerčních serverech standardní konstrukce. To snižuje náklady, zvyšuje agilitu služeb a připravuje cestu pro optimalizaci RAN založenou na AI/ML. F1-U je tedy nezbytné pro naplnění ekonomických a výkonnostních slibů 5G sítí, včetně podpory služeb rozšířeného mobilního širokopásmového připojení (eMBB) a ultra-spolehlivé komunikace s nízkou latencí (URLLC).

## Klíčové vlastnosti

- Přenáší pakety uživatelských dat pomocí GTP-U přes UDP/IP
- Pro každý datový rádiový přenosový kanál (DRB) zřizuje jeden nebo více GTP-U tunelů
- Podporuje přesměrování dat během předávání spojení uvnitř gNB a mezi gNB
- Umožňuje nezávislé směrování a optimalizaci uživatelského provozu
- Usnadňuje mechanismy řízení toku a hlášení stavu doručení dat
- Navrženo pro vysokou propustnost a nízkou latenci, aby splňovalo požadavky 5G služeb

## Související pojmy

- [F1-C – F1 Control Plane Interface](/mobilnisite/slovnik/f1-c/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)

## Definující specifikace

- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.470** (Rel-19) — F1 Interface Introduction

---

📖 **Anglický originál a plná specifikace:** [F1-U na 3GPP Explorer](https://3gpp-explorer.com/glossary/f1-u/)
