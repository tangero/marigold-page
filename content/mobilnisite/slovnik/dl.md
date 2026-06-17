---
slug: "dl"
url: "/mobilnisite/slovnik/dl/"
type: "slovnik"
title: "DL – Downlink"
date: 2025-01-01
abbr: "DL"
fullName: "Downlink"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dl/"
summary: "Downlink (DL) označuje rádiový přenosový směr ze základnové stanice sítě (např. gNB, eNB, NodeB, BTS) k uživatelskému zařízení (UE). Je základní směrovou složkou všech buněčných systémů a přenáší uživ"
---

DL je rádiový přenosový směr ze základnové stanice sítě k uživatelskému zařízení, který přenáší uživatelská data, vysílací informace a řídicí signalizaci pro přístup k síti, mobilitu a správu relací.

## Popis

V 3GPP buněčných systémech je Downlink (DL) jedním ze dvou hlavních směrů rádiového spoje, který zásadně definuje přenosovou cestu ze sítě k uživateli. Zahrnuje všechny fyzické signály a kanály vysílané z přístupového bodu sítě – jako je gNB v 5G NR, [eNB](/mobilnisite/slovnik/enb/) v LTE, NodeB v UMTS nebo [BTS](/mobilnisite/slovnik/bts/) v GSM – k jednomu nebo více uživatelským zařízením (UE). Fyzická vrstva DL je vysoce komplexní a zahrnuje přesné techniky modulace, kódování, multiplexování a formování svazku přizpůsobené každé technologii rádiového přístupu (RAT). Přenáší různorodou směs provozu: uživatelská data (např. internetové pakety, hlasové toky), signalizaci řídicí roviny (např. zprávy [RRC](/mobilnisite/slovnik/rrc/), paging), synchronizační signály (PSS/SSS), vysílané systémové informace ([MIB](/mobilnisite/slovnik/mib/), SIB) a referenční signály pro odhad a měření kanálu (např. [CSI-RS](/mobilnisite/slovnik/csi-rs/), [CRS](/mobilnisite/slovnik/crs/)).

Z architektonického hlediska je DL generován v digitálních a rádiových jednotkách základnové stanice. Datové toky přicházejí ze základní sítě přes přenosové spoje k procesoru základního pásma. Zde procházejí kanálovým kódováním (např. [LDPC](/mobilnisite/slovnik/ldpc/) v 5G, Turbo kódy v LTE), modulací (QPSK, [16QAM](/mobilnisite/slovnik/16qam/), 64QAM, 256QAM atd.) a mapováním vrstev pro MIMO přenosy. Signály jsou následně namapovány na konkrétní časově-frekvenční zdroje (Resource Blocks v LTE/NR, časové sloty/kódy v UMTS/GSM) definované plánovačem. Tento plánovač, klíčová součást vrstvy řízení přístupu k médiu (MAC), dynamicky přiděluje DL zdroje na základě indikátorů kvality kanálu od UE (CQI), požadavků na QoS a algoritmů spravedlivosti. Výsledný RF signál je zesílen a vysílán přes anténní pole základnové stanice, které může využívat formování svazku k nasměrování energie k určitým UE, což je technika klíčová pro výkon 5G NR.

Jeho role je pro provoz sítě naprosto zásadní. DL není jen potrubím pro uživatelská data; je řídicím kanálem sítě. Prostřednictvím DL síť pokyny uděluje UE, jak a kdy vysílat v uplinku (UL), přiděluje zdroje pro předávání hovoru, doručuje klíčové systémové informace pro počáteční výběr buňky a vyvolává UE pro příchozí služby. Výkon DL – jeho datový tok, latence a pokrytí – přímo definuje uživatelský zážitek. Pokroky napříč 3GPP releasy, jako vyšší řády MIMO, agregace nosných a širší šířky pásma, se primárně zaměřovaly na vylepšení schopností DL, aby uspokojily rostoucí poptávku po mobilním širokopásmovém připojení. Specifikace jako TS 38.762 (NR) a TS 36.124 (LTE) definují jeho výkonnostní požadavky, zatímco TS 25.101 (UTRA) a TS 45.005 (GERAN) to činí pro starší technologie.

## K čemu slouží

Downlink existuje jako základní, asymetrická složka buněčné architektury, protože charakter provozu a řídicí paradigma jsou síťově-centrické. Síť má globální přehled o dostupnosti zdrojů, distribuci uživatelů a konektivitě k základní síti, což z ní činí logického řídicího prvku. DL řeší problém efektivního distribuce informací – jak řídicích příkazů, tak uživatelských dat – z centrálního bodu (buňky) k mnoha distribuovaným, mobilním koncovým bodům. Je motivován potřebou vysílat společné informace (jako systémové parametry) a spolehlivě doručovat uživatelsky specifické datové toky s řízenou kvalitou služby.

Historicky měl DL vždy větší kapacitu než Uplink, a to díky většímu dostupnému výkonu na základnové stanici a méně omezujícím faktorům pro antény. Tato asymetrie odpovídá typickému uživatelskému vzorci spotřeby (např. stahování webových stránek, streamování videa). Každá nová generace (3G, 4G, 5G) byla hnací silou exponenciálního zvýšení špičkových datových toků a spektrální účinnosti DL, aby podpořila nové aplikace náročné na šířku pásma. Vývoj DL technologií, od jednoduchého TDMA v GSM po massive MIMO a mmWave v 5G NR, přímo řeší omezení předchozích přístupů ve využití spektra, řízení interference a prostorovém multiplexování, což umožňuje buněčným sítím škálovat se, aby uspokojily moderní požadavky na data.

## Klíčové vlastnosti

- Směr přenosu ze základnové stanice (gNB/eNB/NodeB/BTS) k uživatelskému zařízení (UE)
- Přenáší uživatelská data, vysílací kanály, synchronizační signály a veškeré klíčové downlink řídicí informace (DCI)
- Využívá pokročilé techniky fyzické vrstvy jako OFDMA/DFT-s-OFDM, modulace vysokého řádu a víceanténní MIMO/formování svazku
- Přidělování zdrojů je dynamicky plánováno sítí na základě zpětné vazby od UE a QoS
- Výkonnostní metriky (propustnost, latence, pokrytí) jsou primárními ukazateli schopností sítě
- Definován napříč všemi 3GPP RAT (GSM, UMTS, LTE, NR) s technologicky specifickými implementacemi

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.916** (Rel-16) — Rel-16 Description Summary
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.768** (Rel-12) — Group Communication System Enablers for LTE
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [DL na 3GPP Explorer](https://3gpp-explorer.com/glossary/dl/)
