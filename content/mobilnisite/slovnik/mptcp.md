---
slug: "mptcp"
url: "/mobilnisite/slovnik/mptcp/"
type: "slovnik"
title: "MPTCP – Multi-Path TCP Protocol"
date: 2026-01-01
abbr: "MPTCP"
fullName: "Multi-Path TCP Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mptcp/"
summary: "Rozšíření protokolu transportní vrstvy, které umožňuje TCP spojení současně využívat více síťových cest, čímž zvyšuje propustnost, odolnost a podporu mobility. Umožňuje zařízením s více rozhraními (na"
---

MPTCP je rozšíření protokolu transportní vrstvy, které umožňuje TCP spojení současně využívat více síťových cest, čímž zvyšuje propustnost a odolnost zařízení s více rozhraními, jako je Wi-Fi a mobilní síť.

## Popis

Multi-Path TCP (MPTCP) je rozšíření standardního Transmission Control Protocol (TCP), které umožňuje současné využití více síťových cest mezi dvěma komunikujícími hostiteli. Na rozdíl od běžného TCP, které navazuje jediné spojení přes jednu dvojici zdrojové a cílové IP adresy, MPTCP vytváří hlavní TCP spojení a následně navazuje další podtoky přes různá dostupná rozhraní nebo IP adresy. Tyto podtoky jsou agregovány do jediného logického spojení, které aplikace vidí, a nadále používá standardní socketové rozhraní. Protokol řídí rozdělování a opětovné slučování dat přes podtoky, zajišťuje doručení dat aplikaci ve správném pořadí a optimalizuje využití dostupné šířky pásma.

Z architektonického hlediska MPTCP funguje na transportní vrstvě s rozšířeními pole TCP option pro přenos informací o správě spojení. Klíčové komponenty zahrnují koncové body s podporou MPTCP a volitelně i mezilehlé prvky, jako jsou proxy, které toto rozšíření podporují. Protokol používá kryptografický token pro bezpečné přiřazení více podtoků ke stejnému spojení. Komponenta správce cest na každém koncovém bodě zjišťuje dostupná rozhraní a IP adresy a plánovač rozhoduje, jak distribuovat data přes podtoky na základě faktorů, jako je latence cesty a zahlcení. Algoritmus řízení zahlcení, typicky vázaný, ale ne zcela synchronní, řídí zahlcení na každém podtoku nezávisle, přičemž usiluje o férovost vůči běžným TCP tokům na sdílených spojích.

V kontextu 3GPP je MPTCP zvláště relevantní pro uživatelské zařízení (UE) s více technologiemi rádiového přístupu, jako je 5G NR, LTE a Wi-Fi. UE může navazovat podtoky přes každou aktivovanou PDU relaci nebo přístupovou síť. Architektura 3GPP podporuje MPTCP prostřednictvím vylepšení v uživatelské rovině, například definicí, jak [UPF](/mobilnisite/slovnik/upf/) zpracovává více tunelů odpovídajících podtokům. Schopnost protokolu přesměrovat provoz z jedné cesty na druhou poskytuje plynulou mobilitu; například když UE opustí dosah Wi-Fi, mobilní podtok může převzít služby bez přerušení aplikační relace. To vyžaduje koordinaci se správou relací v jádru 3GPP pro zvládnutí změn IP adres a kontinuity PDU relací.

## K čemu slouží

MPTCP byl vyvinut, aby překonal omezení tradičního TCP, které je omezeno na jedinou cestu na spojení, a nemůže tak využít více síťových rozhraní běžně dostupných na moderních zařízeních. Toto omezení na jedinou cestu vede k neoptimálnímu využití zdrojů, protože šířka pásma z dalších rozhraní zůstává nevyužita. Zároveň vede k nízké odolnosti; pokud jediná cesta selže, TCP spojení se přeruší a vyžaduje obnovení na aplikační vrstvě. MPTCP tyto problémy řeší tím, že umožňuje souběžné využití více cest, čímž zvyšuje celkovou propustnost, zlepšuje spolehlivost prostřednictvím redundance cest a zvyšuje mobilitu umožněním migrace spojení.

Motivace pro standardizaci MPTCP v rámci 3GPP, počínaje Release 16, vychází z rozšíření zařízení s více RAT a potřeby efektivní agregace provozu a plynulé kontinuity relací v sítích 5G. Předchozí řešení, jako agregace spojení na nižších vrstvách nebo multiplexování na aplikační úrovni, byla buď nestandardní, nebo neefektivní. MPTCP poskytuje standardizované řešení na transportní vrstvě, které je pro většinu aplikací transparentní. Řeší konkrétní případy užití 5G, jako je rozšířené mobilní širokopásmové připojení (eMBB) vyžadující vysokou propustnost, ultra spolehlivá komunikace s nízkou latencí (URLLC) vyžadující odolnost a podpora funkcí směrování, přepínání a rozdělování přístupového provozu ([ATSSS](/mobilnisite/slovnik/atsss/)).

Historicky základní protokol MPTCP vyvinula [IETF](/mobilnisite/slovnik/ietf/). Práce 3GPP integruje a profiluje MPTCP pro mobilní ekosystém, definuje, jak interaguje s funkcemi specifickými pro 3GPP, jako jsou PDU relace, QoS toky a síťově řízené směrování provozu. Tato integrace zajišťuje, že operace MPTCP jsou v souladu s politikami mobilní sítě, účtováním a bezpečnostními modely, což operátorům umožňuje nabízet vylepšené služby, které využívají více přístupů řízeným a efektivním způsobem.

## Klíčové vlastnosti

- Zpětná kompatibilita s aplikacemi používajícími standardní TCP sockety
- Současný přenos dat přes více síťových cest (podtoků)
- Dynamické přidávání a odebírání podtoků během spojení
- Plynulý přechod a migrace cest bez přerušení spojení
- Vázané řízení zahlcení pro férovost vůči standardnímu TCP provozu
- Podpora heterogenních sítí (např. 5G, LTE, Wi-Fi)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity

---

📖 **Anglický originál a plná specifikace:** [MPTCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mptcp/)
