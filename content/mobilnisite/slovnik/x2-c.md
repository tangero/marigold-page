---
slug: "x2-c"
url: "/mobilnisite/slovnik/x2-c/"
type: "slovnik"
title: "X2-C – X2-Control Plane"
date: 2025-01-01
abbr: "X2-C"
fullName: "X2-Control Plane"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/x2-c/"
summary: "Řídicí rovina rozhraní mezi dvěma eNodeB v LTE a 5G NR. Umožňuje přímou výměnu signalizace pro funkce jako příprava předání spojení, správa zátěže a koordinace rušení, čímž snižuje latenci a zatížení"
---

X2-C je řídicí rovina rozhraní mezi dvěma eNodeB v LTE a 5G NR, která umožňuje přímou signalizaci pro funkce jako předání spojení (handover) a správu zátěže za účelem snížení latence a zatížení páteřní sítě.

## Popis

Rozhraní X2-C je klíčovou součástí architektury rádiové přístupové sítě (RAN) LTE a 5G NR, konkrétně definovanou pro signalizaci řídicí roviny mezi dvěma sousedními eNodeB (v LTE) nebo gNB (v 5G NR). Funguje přes IP transportní síť, typicky využívá [SCTP](/mobilnisite/slovnik/sctp/) (Stream Control Transmission Protocol) jako svůj spolehlivý transportní protokol pro zajištění uspořádaného a spolehlivého doručování signalizačních zpráv. Rozhraní je logický point-to-point spoj, což znamená, že je navázán mezi konkrétními páry základnových stanic, které jsou nakonfigurovány jako sousedé, obvykle na základě geografické blízkosti a očekávaných vzorců mobility uživatelů.

Primární funkcí X2-C je umožnit přímou komunikaci mezi základnovými stanicemi bez nutnosti vždy zapojovat Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) páteřní sítě. To je architektonicky významné, protože decentralizuje některé řídicí funkce RAN. Mezi klíčové procedury prováděné přes X2-C patří Příprava předání spojení (Handover Preparation), kdy zdrojový eNodeB/gNB komunikuje s cílovým za účelem rezervace prostředků a kontextu předtím, než nařídí UE přepnout; Správa zátěže (Load Management), zahrnující výměnu hlášení o stavu prostředků (Resource Status Reports, RSR) o využití rádiových zdrojových bloků; a Koordinace mezibuněčného rušení (Inter-Cell Interference Coordination, [ICIC](/mobilnisite/slovnik/icic/)), kdy si eNodeB vyměňují indikátory přetížení (Overload Indicator, [OI](/mobilnisite/slovnik/oi/)) a indikátory vysokého rušení (High Interference Indicator, HII) za účelem koordinace výkonu a přidělování prostředků na okrajích buněk pro uplink i downlink.

Z pohledu protokolů je nad SCTP provozován [X2](/mobilnisite/slovnik/x2/) Application Protocol (X2AP). X2AP definuje konkrétní elementární procedury a zprávy pro všechny výše uvedené funkce. Nastavení rozhraní zahrnuje proceduru X2 Setup, při které si sousední eNodeB vyměňují své konfigurační údaje, včetně podporovaných funkcí, identifikátorů buněk a kódů sledovacích oblastí. Návrh rozhraní je vysoce škálovatelný; přestože se jedná o logický point-to-point spoj, síť X2 spojení v síti je spravována systémy Operations, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), které konfigurují sousední vztahy. V 5G NR je rozhraní Xn-C přímým vývojem X2-C, zachovávajícím podobné principy, ale s vylepšenými procedurami pro podporu nových schopností 5G, jako je síťové dělení (network slicing) a pokročilejší scénáře duální konektivity.

## K čemu slouží

Rozhraní X2-C bylo vytvořeno k řešení klíčových omezení starší architektury 3G UMTS, kde [RNC](/mobilnisite/slovnik/rnc/) (Radio Network Controller) spravovalo předání spojení a koordinaci mezi NodeB. Ve zploštělé architektuře LTE převzal eNodeB funkce RNC, což si vyžádalo vytvoření přímé komunikační cesty mezi nimi. Primární problém, který X2-C řeší, je snížení latence při předání spojení a signalizační zátěže na páteřní síti. Bez [X2](/mobilnisite/slovnik/x2/) by každé předání spojení mezi eNodeB vyžadovalo, aby signalizace prošla páteřní sítí (zdrojový eNodeB -> MME -> cílový eNodeB), což by znamenalo významné zpoždění a spotřebu prostředků páteřní sítě.

Tím, že umožňuje přímý řídicí spoj, umožňuje X2-C rychlejší a efektivnější předání spojení, což je klíčové pro podporu plynulé mobility vysokorychlostních uživatelů a služeb v reálném čase, jako je VoIP. Dále umožňuje distribuované optimalizační funkce RAN. Například funkce jako Vyvažování zátěže (Load Balancing) a Koordinace rušení vyžadují rychlou výměnu informací o rádiových podmínkách mezi buňkami, což by bylo nepraktické, pokud by byly směrovány přes centrální uzel páteřní sítě. X2-C poskytuje nezbytný signalizační kanál s nízkou latencí a vysokou spolehlivostí pro tyto úkoly koordinace RAN v reálném čase, což zásadně umožňuje koncepty samoorganizujících se sítí (SON), které jsou ústřední pro automatizaci a optimalizaci sítí LTE a 5G.

## Klíčové vlastnosti

- Umožňuje přímou signalizaci mezi základnovými stanicemi pro přípravu a provedení předání spojení
- Podporuje správu zátěže prostřednictvím výměny hlášení o stavu prostředků (Resource Status Reports, RSR)
- Umožňuje koordinaci mezibuněčného rušení (Inter-Cell Interference Coordination, ICIC) pro uplink a downlink
- Používá SCTP pro spolehlivý, spojově orientovaný transport řídicích zpráv
- Definováno X2 Application Protocol (X2AP) pro kódování procedur a zpráv
- Snižuje latenci a signalizační zátěž páteřní sítě pro mobilitu a optimalizaci RAN

## Související pojmy

- [X2-U – X2-User Plane](/mobilnisite/slovnik/x2-u/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.420** (Rel-19) — X2 Interface Introduction for E-UTRAN

---

📖 **Anglický originál a plná specifikace:** [X2-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/x2-c/)
