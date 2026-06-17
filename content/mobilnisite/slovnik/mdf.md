---
slug: "mdf"
url: "/mobilnisite/slovnik/mdf/"
type: "slovnik"
title: "MDF – MBMS (Download & Streaming) Delivery Function"
date: 2025-01-01
abbr: "MDF"
fullName: "MBMS (Download & Streaming) Delivery Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mdf/"
summary: "MDF je základní síťová funkce v architektuře rozšířené služby Multimedia Broadcast Multicast Service (eMBMS). Je odpovědná za doručování, správu relací a synchronizaci vysílaného/skupinově vysílaného"
---

MDF je základní síťová funkce v eMBMS odpovědná za doručování, správu relací a synchronizaci vysílaného či skupinově vysílaného obsahu od poskytovatelů k rádiové přístupové síti.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) Delivery Function (MDF) je klíčová logická entita v rámci 3GPP Evolved Packet Core (EPC) a 5G Core sítě, konkrétně pro rozšířenou službu Multimedia Broadcast Multicast Service (eMBMS). Funguje jako centrální koordinační bod mezi zdrojem vysílaného/skupinově vysílaného obsahu (např. Broadcast-Multicast Service Center - [BM-SC](/mobilnisite/slovnik/bm-sc/)) a rádiovou přístupovou sítí ([E-UTRAN](/mobilnisite/slovnik/e-utran/) nebo NG-RAN). Primární role MDF spočívá ve správě doručování MBMS uživatelských dat, což může být buď doručování souborů (stahování) prostřednictvím File Delivery over Unidirectional Transport ([FLUTE](/mobilnisite/slovnik/flute/)), nebo přenos v reálném čase (streamování) prostřednictvím RTP, k více uživatelským zařízením (UE) současně.

Z architektonického hlediska je MDF často umístěna společně s BM-SC nebo je její funkční součástí, jak je definováno ve specifikacích jako TS 26.956 a TS 33.126. Pro MBMS stahování přijímá MDF soubory nebo souborové karusely od poskytovatelů obsahu. Poté řídí relaci doručování, která zahrnuje plánování přenosu, aplikaci kódování pro opravu chyb ([FEC](/mobilnisite/slovnik/fec/)) dle TS 26.346 a zapouzdření dat do IP multicast paketů. Rozhraní k MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) využívá protokoly jako Diameter pro řízení relace a IP multicast pro distribuci dat v uživatelské rovině. Kritickou technickou funkcí MDF ve scénářích streamování je generování a distribuce synchronizačních informací, jako jsou časové reference M1 a pakety Synchronization Protocol (SYNC), aby byla zajištěna přesně současná přenosová činnost stejného obsahu ze všech eNodeB/gNBs v oblasti Multimedia Broadcast Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)), což umožňuje koherentní makro-diverzitní kombinaci na straně UE.

V oblasti zabezpečení, jak je popsáno v TS 33.126-128, hraje MDF klíčovou roli v systému MBMS Service Protection. Může komunikovat s funkcí Key Management Function (KMF) za účelem získání šifrovacích klíčů pro provoz (TEK) a následně bezpečně distribuovat přidružený klíčový materiál (jako [MIKEY](/mobilnisite/slovnik/mikey/) nebo MSK) autorizovaným UE prostřednictvím procedur oznámení služby a distribuce klíčů BM-SC. To zajišťuje, že vysílaný obsah může dešifrovat pouze předplatitel. Schopnosti správy MDF také zahrnují monitorování stavu relace, zpracování hlášení chyb a podporu kontinuity služeb pro mobilní uživatele pohybující se mezi oblastmi vysílání/skupinového vysílání a doručování typu unicast.

## K čemu slouží

MDF byla zavedena za účelem centralizace a standardizace složitých mechanismů doručování potřebných pro efektivní distribuci obsahu typu point-to-multipoint v mobilních sítích. Před vylepšeními eMBMS se vysílací služby často spoléhaly na oddělené, neintegrované systémy. Vytvoření MDF, zvláště zdůrazněné od Release 14 s vylepšeními pro LTE-based 5G broadcast, bylo motivováno rostoucí poptávkou po škálovatelných multimediálních službách, jako je živé TV, aktualizace softwaru a veřejná varování, které by mohly zatížit unicastové sítě.

Řeší základní problém efektivního doručování identického obsahu obrovskému počtu uživatelů bez zahlcení jádrové a rádiové sítě redundantními unicastovými proudy. Správou doručování obsahu jako vysílací/skupinově vysílací relace umožňuje MDF sdílení síťových zdrojů, což dramaticky zvyšuje spektrální účinnost. Její synchronizační schopnosti jsou speciálně navrženy k umožnění provozu MBSFN, který mění interferenci z přenosů z více buněk v konstruktivní signál, čímž zlepšuje pokrytí a spolehlivost na okrajích buněk – což je kritický požadavek pro vysílací služby.

Dále MDF řeší potřebu jednotného rámce, který podporuje jak stahování (pro služby založené na karuselech, jako jsou aktualizace firmwaru), tak streamování (pro živé události). Její integrace s MBMS bezpečnostní architekturou poskytuje standardizovanou metodu pro ochranu obsahu a monetizaci služeb prostřednictvím předplatného. Vývoj MDF napříč releasy odráží snahu podporovat nové případy užití, jako je konvergence ATSC 3.0, vylepšené TV služby a skupinová komunikace V2X, což z ní činí základní kámen pro síťové vysílání a skupinové vysílání v éře 5G.

## Klíčové vlastnosti

- Řídí doručování MBMS v uživatelské rovině pro služby stahování souborů (FLUTE) i přenosu v reálném čase (RTP)
- Generuje a distribuuje synchronizační informace (SYNC protokol, časování M1) pro provoz MBSFN
- Komunikuje s MBMS Gateway pro řízení relace a distribuci IP multicast dat
- Integruje se s MBMS Service Protection pro bezpečnou distribuci klíčů a šifrování obsahu
- Spravuje relace doručování včetně plánování, aplikace FEC a hlášení chyb
- Podporuje mechanismy kontinuity služeb mezi režimy doručování vysílání/skupinového vysílání a unicast

## Související pojmy

- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.981** (Rel-19) — MBMS Provisioning & Content Ingestion Interface Study
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [MDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdf/)
