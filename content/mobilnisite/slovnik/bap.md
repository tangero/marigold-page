---
slug: "bap"
url: "/mobilnisite/slovnik/bap/"
type: "slovnik"
title: "BAP – Backhaul Adaptation Protocol"
date: 2026-01-01
abbr: "BAP"
fullName: "Backhaul Adaptation Protocol"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/bap/"
summary: "BAP je protokol vrstvy 2 zavedený v 3GPP Release 16 pro sítě IAB (Integrated Access and Backhaul). Umožňuje dynamické směrování datových a řídicích paketů mezi IAB uzly a dárcovským uzlem přes bezdrát"
---

BAP je protokol vrstvy 2 pro 3GPP sítě IAB (Integrated Access and Backhaul), který dynamicky směruje datové a řídicí pakety mezi IAB uzly a dárcovským uzlem přes bezdrátové páteřní (backhaul) spoje.

## Popis

Backhaul Adaptation Protocol (BAP) je klíčová protokolová vrstva v architektuře IAB, která funguje nad vrstvou RLC (Radio Link Control) a pod vrstvami SDAP (Service Data Adaptation Protocol) a PDCP (Packet Data Convergence Protocol) pro přenos uživatelských dat. Jejím hlavním úkolem je zajišťovat směrování a mapování přenosů (bearer mapping) napříč více skokovou bezdrátovou páteří tvořenou IAB uzly. Každý IAB uzel a IAB donor obsahují BAP entitu. BAP vrstva přidává k paketům BAP hlavičku, která obsahuje BAP Routing ID. Tento identifikátor se používá k směrování paketu správnou cestou přes páteřní topologii k jeho cílovému určení, což může být další IAB uzel, donor nebo UE připojené k IAB uzlu.

BAP pracuje se dvěma typy přenosů (bearers): BAP přenosy a rádiové přenosy. BAP přenos představuje koncový logický spojení mezi centrální jednotkou ([CU](/mobilnisite/slovnik/cu/)) dárcovského uzlu a IAB uzlem nebo UE obsluhovaným IAB uzlem. Je identifikován BAP adresou a BAP path ID. BAP vrstva mapuje tyto BAP přenosy na rádiové přenosy (např. RLC kanály) na každém jednotlivém bezdrátovém skoku. Toto mapování je konfigurovatelné a umožňuje diferenciaci provozu a zpracování QoS v páteři. Směrovací tabulky v každé BAP entitě, které mapují BAP Routing ID na příslušný přenosový odkaz k dalšímu uzlu (next-hop), jsou konfigurovány centrální jednotkou (CU) IAB donoru pomocí signalizace F1-Application Protocol (F1-AP) přes řídicí rovinu.

Pro provoz ve směru downstream (ze sítě k UE) určuje BAP Routing ID donor CU. Jak paket prochází každým IAB uzlem, místní BAP entita prozkoumá BAP Routing ID, nalezne odpovídající záznam ve své směrovací tabulce a přepošle paket správnému podřízenému uzlu (child node) přes příslušný rádiový přenos. Pro upstream provoz IAB uzel, ke kterému je UE připojeno, přidá BAP Routing ID. Tento identifikátor je typicky konfigurován donorem a směruje paket po upstream cestě k donoru. BAP také podporuje adaptaci topologie. Pokud spoj selže nebo je přidán nový uzel, donor CU může překonfigurovat BAP směrovací tabulky v zasažených uzlech a vytvořit nové cesty, což umožňuje vytváření robustních a samoopravných páteřních sítí.

## K čemu slouží

BAP byl vytvořen k řešení výzvy budování škálovatelné a flexibilní bezdrátové páteře pro 5G sítě, konkrétně pro funkci Integrated Access and Backhaul (IAB). Tradiční páteřní spoje (wired nebo point-to-point mikrovlnné) jsou pro hustá nasazení malých buněk (small cells) nákladné a nepružné. IAB umožňuje 5G základnovým stanicím (gNB) použít část svých rádiových zdrojů pro přenos páteřního provozu z jiných, vzdálenějších uzlů, čímž vytváří bezdrátovou síť typu mesh. To však vyžadovalo nový protokol pro správu více skokového směrování uvnitř architektury gNB bez zapojení jádra sítě.

Účelem BAP je poskytnout mechanismus směrování na vrstvě 2, který je těsně integrován s architekturou 3GPP NG-RAN. Před zavedením BAP by více skoková komunikace vyžadovala IP směrování na vrstvě 3, což přináší vyšší složitost, režii a není optimální pro prostředí RAN citlivé na latenci a vyžadující těsnou synchronizaci. BAP tento problém řeší tím, že funguje pod vrstvou PDCP, což umožňuje, aby se IAB síť jevila 5G jádru jako jediný logický gNB. Umožňuje efektivní přeposílání skok po skoku, podporuje diferenciaci QoS v páteři mapováním na různé RLC kanály a usnadňuje rychlou správu topologie pod kontrolou donor [CU](/mobilnisite/slovnik/cu/). To operátorům umožňuje rychle rozšiřovat pokrytí, zejména v oblastech bez dostupného optického vlákna, pomocí bezdrátového řetězení uzlů.

## Klíčové vlastnosti

- Poskytuje směrování na vrstvě 2 pro pakety uživatelské a řídicí roviny v sítích IAB
- Pro rozhodování o přeposílání skok po skoku používá BAP Routing ID v BAP hlavičce
- Mapuje koncové BAP přenosy na rádiové přenosy (RLC kanály) na každém skoku pro podporu QoS
- Směrovací tabulky jsou konfigurovány centrální jednotkou (CU) IAB donoru pomocí řídicí signalizace F1-AP
- Podporuje dynamickou adaptaci topologie a překonfiguraci cest pro odolnost
- Umožňuje, aby byla IAB síť spravována jako jediný logický gNB z pohledu jádra sítě

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TR 33.824** (Rel-17) — Security Study for NR Integrated Access & Backhaul
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification

---

📖 **Anglický originál a plná specifikace:** [BAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bap/)
