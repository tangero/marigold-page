---
slug: "5mbs"
url: "/mobilnisite/slovnik/5mbs/"
type: "slovnik"
title: "5MBS – 5G Multicast-Broadcast Services"
date: 2025-01-01
abbr: "5MBS"
fullName: "5G Multicast-Broadcast Services"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5mbs/"
summary: "5MBS je služba 3GPP umožňující efektivní doručení stejného obsahu více uživatelům současně s využitím síťových prostředků 5G. Optimalizuje využití šířky pásma pro aplikace jako živé video, výstrahy pr"
---

5MBS je služba 3GPP, která efektivně doručuje stejný obsah více uživatelům současně přes sítě 5G, optimalizuje šířku pásma pro aplikace jako živé video, výstrahy pro veřejnou bezpečnost a aktualizace softwaru prostřednictvím multicastového a broadcastového přenosu.

## Popis

5G Multicast-Broadcast Services (5MBS) je rámec v rámci systému 5G navržený pro efektivní doručování obsahu ze zdroje do více cílů využitím sdílených síťových prostředků. Na rozdíl od tradičního unicastu, kde jsou k jednotlivým uživatelům vysílány samostatné datové toky, přenáší 5MBS jediný tok přes společné prostředky rádiového přístupu a jádra sítě, který je podle potřeby replikován pro skupiny uživatelů. Tato architektura je definována v několika specifikacích 3GPP, včetně TS 23.527 pro celkovou systémovou architekturu, TS 26.802 pro doručování médií a TS 29.244, 29.532 a 29.581 pro detaily protokolů a rozhraní. Funguje integrací multicast-broadcast funkcionality jak do 5G Core Network (5GC), tak do Radio Access Network (RAN), s klíčovými komponentami jako je [MBSF](/mobilnisite/slovnik/mbsf/) (Multicast/Broadcast Service Function) v jádře a podpora multicastových přenosových bodů v gNB.

Z hlediska provozu podporuje 5MBS dva hlavní režimy: multicast a broadcast. Multicastový režim doručuje obsah konkrétní skupině uživatelů, kteří si službu předplatili (např. živý sportovní přenos nebo firemní videokonference), s využitím IP multicastové adresace. Broadcastový režim naopak distribuuje obsah všem uživatelům ve vymezené geografické oblasti (např. výstrahy nebo veřejná televize) bez nutnosti individuálního předplatného. Systém využívá service-based architekturu 5GC, kde MBSF spravuje navázání relace, přidělování prostředků v uživatelské rovině a autorizaci služby. V RAN zahrnují vylepšení schémata multicastového přenosu přes rozhraní vzduchu, jako je provoz v single-frequency network (SFN), pro zlepšení pokrytí a spektrální účinnosti synchronizací vysílání z více buněk.

Úlohou 5MBS v síti je umožnit škálovatelné a efektivní doručování obsahu, což je zásadní pro aplikace náročné na šířku pásma. Integruje se s existujícími funkcemi 5G, jako je network slicing a mechanismy kvality služeb (QoS), aby poskytovala diferencované úrovně služeb – například zajištění nízké latence pro živá vysílání nebo vysoké spolehlivosti pro kritické komunikace. Mezi klíčová rozhraní patří Nmb9 mezi MBSF a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) pro přeposílání dat a protokoly na rádiové úrovni pro multicastové plánování. Vyložení provozu z unicastových kanálů prostřednictvím 5MBS snižuje zahlcení sítě, provozní náklady a zlepšuje uživatelský zážitek, což z něj činí základní prvek pro pokročilé případy užití 5G v oblasti médií, IoT a veřejných služeb.

## K čemu slouží

5MBS bylo vytvořeno k řešení neefektivnosti unicastového přenosu pro distribuci obsahu typu jeden-více v mobilních sítích. Před jeho zavedením v 3GPP Release 17 se 5G primárně spoléhalo na point-to-point unicast, který spotřebovává nadměrnou šířku pásma a síťové prostředky, když jsou stejná data odesílána více uživatelům – například při živém streamování nebo aktualizacích softwaru. Tento přístup vedl k zahlcení, vyšším nákladům a zhoršenému výkonu, zejména v hustě obydlených městských oblastech nebo během rozsáhlých událostí. Historický kontext zahrnuje dřívější řešení pro multicast-broadcast, jako bylo eMBMS (Evolved Multimedia Broadcast Multicast Service) v 4G LTE, které poskytovalo základní schopnosti, ale postrádalo flexibilitu, integraci a výkon potřebný pro různorodé požadavky služeb 5G.

Omezení předchozích přístupů, včetně eMBMS, zahrnovala rigidní architekturu, omezenou podporu dynamických servisních oblastí a neoptimální sladění s cloud-nativním a service-based jádrem 5G. 5MBS tyto problémy řeší tím, že nabízí nativní, integrovaný multicast-broadcast rámec v systému 5G, navržený od základů tak, aby využíval pokroky 5G, jako je network slicing, edge computing a vylepšený QoS. Umožňuje efektivní využití prostředků sdílením rádiových a jádrových síťových cest, snižuje latenci a zlepšuje škálovatelnost pro aplikace sahající od imerzních médií po masivní nasazení IoT. Motivací pro jeho vytvoření je rostoucí poptávka po skupinové komunikaci, například v oblasti veřejné bezpečnosti, automobilových aktualizací a zábavy, což vyvolává potřebu standardizovaného, vysoce výkonného řešení, které může podporovat budoucí vývoj 5G a nové obchodní modely.

## Klíčové vlastnosti

- Efektivní distribuce obsahu typu jeden-více využitím sdílených síťových prostředků
- Podpora jak multicastového (skupinového), tak broadcastového (oblastního) přenosového režimu
- Integrace s service-based architekturou 5G Core a network slicing
- Vylepšené rádiové techniky jako single-frequency network (SFN) pro lepší pokrytí
- Dynamické řízení relací a diferenciace QoS pro různé servisní požadavky
- Škálovatelnost pro scénáře s vysokou hustotou uživatelů a aplikace náročné na šířku pásma

## Definující specifikace

- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol
- **TS 29.581** (Rel-19) — MBSTF Service Based Interface Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [5MBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/5mbs/)
