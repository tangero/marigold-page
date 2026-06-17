---
slug: "mbsf"
url: "/mobilnisite/slovnik/mbsf/"
type: "slovnik"
title: "MBSF – Multicast/Broadcast Service Function"
date: 2026-01-01
abbr: "MBSF"
fullName: "Multicast/Broadcast Service Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mbsf/"
summary: "Funkce pro multicastové/broadcastové služby (MBSF) je funkce 5G jádra sítě, která spravuje doručování multicastových a broadcastových služeb. Zajišťuje navázání relace, řízení politik a distribuci dat"
---

MBSF je funkce 5G jádra sítě, která spravuje doručování multicastových a broadcastových služeb tím, že zajišťuje navázání relace, řízení politik a distribuci dat pro efektivní skupinovou komunikaci.

## Popis

Funkce pro multicastové/broadcastové služby (MBSF) je klíčová síťová funkce v architektuře 5G Core (5GC), speciálně navržená k orchestraci a správě relací multicastových/broadcastových služeb ([MBS](/mobilnisite/slovnik/mbs/)). Působí jako centrální řídicí bod pro MBS, rozhraním s dalšími funkcemi jádra sítě umožňuje efektivní přenos dat typu point-to-multipoint. MBSF je zodpovědná za celý životní cyklus MBS relace, od zahájení a změny až po ukončení, a zajišťuje spolehlivé doručení obsahu více uživatelským zařízením (UE) současně. Její architektura je založena na servisně orientovaném rámci 5G, což jí umožňuje komunikovat prostřednictvím standardizovaných rozhraní jako Nmbsf pro správu a Nmbst pro přenos dat.

Co se týče provozu, MBSF funguje tak, že přijímá požadavky na službu od aplikací nebo síťových operátorů, často prostřednictvím Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo přímo od Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). Po přijetí požadavku MBSF autentizuje a autorizuje MBS relaci a uplatňuje politiky definované Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)). Následně koordinuje s SMF a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) navázání potřebných datových cest pro multicastový/broadcastový provoz. MBSF také komunikuje s rádiovou přístupovou sítí (RAN), konkrétně s gNB, za účelem alokace rádiových prostředků a konfigurace přenosových parametrů, přičemž využívá identifikátory jako Frequency Selection Area Identity (MBS) pro optimalizaci využití zdrojů.

Klíčové komponenty a rozhraní MBSF zahrnují řídicí rovinu MBSF, která zajišťuje signalizaci a správu relací, a uživatelskou rovinu MBSF, která může být integrována s UPF pro přeposílání dat. Funkce podporuje jak broadcastový režim, kdy je obsah odesílán všem UE v oblasti, tak multicastový režim, kdy data přijímají pouze přihlášená UE. Používá mechanismy pro dynamickou správu skupin, umožňující UE plynule se připojovat k relacím nebo je opouštět. MBSF také hraje roli v účtování a zúčtování, rozhraním s Charging Function ([CHF](/mobilnisite/slovnik/chf/)) sleduje využití MBS služeb.

Úlohou MBSF v síti je umožnit škálovatelnou a efektivní skupinovou komunikaci, která snižuje zahlcení sítě minimalizací duplicitních unicastových proudů. Je nezbytná pro aplikace vyžadující distribuci obsahu v široké oblasti, jako je živé televizní vysílání, nouzové výstrahy, aktualizace softwaru pro IoT zařízení a V2X komunikace. Centralizací správy MBS zajišťuje MBSF konzistentní uplatňování politik, zabezpečení a QoS v rámci celého 5G systému a integruje se s dělením sítě (network slicing) pro poskytování vyhrazených MBS řezů pro různé požadavky služeb.

## K čemu slouží

MBSF byla vytvořena, aby řešila omezení dřívějších multicastových/broadcastových řešení v celulárních sítích, jako je [MBMS](/mobilnisite/slovnik/mbms/) v LTE, kterým chyběla vyhrazená, flexibilní funkce jádra sítě pro správu služeb. V LTE se MBMS spoléhalo na evolved MBMS (eMBMS) s funkcemi jako Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), to však nebylo plně integrováno do servisně orientované architektury 5G. Motivace pro MBSF vychází z potřeby agilnějšího a škálovatelnějšího přístupu ke skupinové komunikaci v 5G, poháněné novými případy užití jako masivní IoT, autonomní řízení a streamování médií v ultra vysokém rozlišení.

Předchozí přístupy trpěly neefektivitou v řízení relací a alokaci zdrojů, což často vedlo k podoptimálnímu výkonu a vysoké provozní složitosti. MBSF tyto problémy řeší tím, že poskytuje standardizovanou, cloud-nativní funkci, která může dynamicky orchestraci MBS relace napříč jádrem a RAN. Umožňuje síťovým operátorům nabízet MBS jako nativní 5G službu s lepší podporou edge computingu a aplikací s nízkou latencí. To je klíčové pro scénáře, kde musí být data v reálném čase distribuována mnoha zařízením, například v chytrých městech nebo průmyslové automatizaci.

Historicky se vývoj MBSF začal v 3GPP Release 17 jako součást širšího rámce 5G MBS, což odráží posun průmyslu směrem ke konvergentním sítím, které efektivně podporují jak unicast, tak multicast. Účelem MBSF je využít architektonické pokroky 5G, jako je dělení sítě (network slicing) a servisně orientovaná rozhraní, k poskytování služeb skupinové komunikace se zvýšenou spolehlivostí, zabezpečením a efektivitou. Řeší rostoucí poptávku po obsahově orientovaných sítích a podporuje regulatorní požadavky na komunikaci pro veřejnou bezpečnost, což z ní činí základní kámen moderních nasazení 5G.

## Klíčové vlastnosti

- Centralizovaná správa životního cyklu MBS relace v 5G jádru
- Integrace se servisně orientovanou architekturou 5G prostřednictvím standardizovaných rozhraní
- Dynamické uplatňování politik a koordinace s PCF a SMF
- Podpora broadcastového i multicastového režimu služeb
- Efektivní alokace zdrojů a koordinace s RAN pro přenos typu point-to-multipoint
- Schopnosti účtování a zúčtování pro MBS služby

## Související pojmy

- [MBS – Frequency Selection Area Identity](/mobilnisite/slovnik/mbs/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 26.502** (Rel-19) — 5G Multicast-Broadcast User Services Architecture
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.521** (Rel-19) — 5G Binding Support Management Service Stage 3
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol
- **TS 29.537** (Rel-19) — 5G Multicast/Broadcast Policy Control Services
- **TS 29.580** (Rel-19) — 5G MBSF Service Interface Stage 3 Specification
- **TS 29.581** (Rel-19) — MBSTF Service Based Interface Protocol Specification
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TR 33.850** (Rel-17) — 5G MBS Security Study

---

📖 **Anglický originál a plná specifikace:** [MBSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbsf/)
