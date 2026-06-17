---
slug: "geo"
url: "/mobilnisite/slovnik/geo/"
type: "slovnik"
title: "GEO – Geostationary satellite Earth Orbit"
date: 2026-01-01
abbr: "GEO"
fullName: "Geostationary satellite Earth Orbit"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/geo/"
summary: "Oběžná dráha družice přibližně 35 786 km nad rovníkem, kde oběžná perioda družice odpovídá rotaci Země, což způsobuje, že se družice jeví jako stacionární vůči bodu na zemském povrchu. V rámci 3GPP se"
---

GEO je oběžná dráha družice přibližně 35 786 km nad rovníkem, kde se družice jeví jako stacionární; používá se v 3GPP Neterestriálních sítích (NTN) pro pokrytí širokých oblastí a komunikaci přímo s koncovým zařízením.

## Popis

V kontextu norem 3GPP se termínem Geostationární oběžná dráha Země (GEO) označuje specifická dráha využívaná družicemi, které jsou integrovány jako přístupové uzly v rámci 3GPP definované Neterestriální sítě (NTN). GEO družice je umístěna ve výšce přibližně 35 786 kilometrů přímo nad zemským rovníkem a pohybuje se stejným směrem jako rotace planety. Tato synchronizace vede k oběžné periodě přesně 24 hodin, což způsobuje, že družice zůstává na obloze pevně umístěna vůči pozorovateli na zemi. Tato stacionární charakteristika je její definující operační vlastností.

Z pohledu síťové architektury funguje GEO družice v 3GPP NTN jako rádiová základnová stanice, často označovaná v 5G terminologii jako gNB, nebo jako transparentní přenosová jednotka, která přeposílá signály. Propojuje koncové zařízení (UE) na zemi s pozemní bránovou stanicí, která je následně připojena k 5G Core síti. Komunikační spojení zahrnuje Servisní spoj (mezi UE a družicí) a Přípojné spojení (mezi družicí a bránou). Kvůli obrovské vzdálenosti zavedou GEO spoje velmi vysoké zpoždění šíření přibližně 250 milisekund pro zpáteční cestu, což je kritické konstrukční omezení ovlivňující protokoly a služby. Velká pokryvná plocha jedné GEO družice (pokrývající až třetinu zemského povrchu) je hlavní výhodou pro poskytování všudypřítomného pokrytí nad oceány, pouštěmi a dalšími neobsluhovanými oblastmi.

Specifikace 3GPP byly upraveny pro podporu NTN založených na GEO. To zahrnuje vylepšení pro zvládnutí dlouhého zpoždění a vysokého Dopplerova posuvu (který je u GEO relativně nízký, ale stále přítomný), procedur časového předstihu, správy mobility (protože přechody mezi buňkami jsou kvůli širokému svazku méně časté) a specifických technik správy rádiových zdrojů. Specifikace fyzické vrstvy (např. v 38.101, 38.108) definují podporovaná kmitočtová pásma a požadavky pro provoz na GEO. Systém musí zvládnout výzvu úrovně přenosu (link budget) kvůli velké vzdálenosti, což vyžaduje UE se zvýšenými schopnostmi nebo specializované terminály pro spolehlivé připojení.

## K čemu slouží

Standardizace provozu GEO družic v rámci 3GPP, počínaje Release 12 a významně rozšířená pro 5G NTN, je hnací silou snahy o poskytnutí plynulého globálního bezdrátového pokrytí. Tradiční terestrické sítě (buňky na stožárech) jsou ekonomicky a fyzicky nepraktické pro pokrytí rozsáhlých venkovských, námořních a leteckých oblastí. GEO družice tento problém řeší tím, že nabízejí jedinou platformu schopnou poskytnout nepřetržité pokrytí celému kontinentu nebo oceánské pánvi, zaplňují kritické mezery v pokrytí a umožňují skutečně všudypřítomnou konektivitu pro 5G.

Historicky existovala satelitní komunikace jako samostatný, neintegrovaný systém. Motivací pro integraci GEO (a dalších oběžných drah, jako jsou [LEO](/mobilnisite/slovnik/leo/) a [MEO](/mobilnisite/slovnik/meo/)) do norem 3GPP je sjednotit terestrické a neterestrické sítě v rámci společného rámce. To umožňuje mobilním zařízením potenciálně se připojit přímo k družicím pomocí upravených 3GPP protokolů, což umožňuje služby jako nouzová komunikace, sledování IoT aktiv ve vzdálených oblastech a přenosové spoje pro venkovské základnové stanice. Řeší to omezení čistě terestrických sítí tím, že zajišťuje všude kontinuitu služeb, což je nezbytné pro komunikaci klíčovou pro činnost, obnovu po katastrofách a propojení nepřipojených, čímž se podporují cíle udržitelného rozvoje OSN pro všeobecný přístup k internetu.

## Klíčové vlastnosti

- Zdánlivě stacionární poloha vůči zemskému povrchu, což zjednodušuje sledování pozemní stanicí
- Extrémně široké pokrytí oblasti (až 34 % zemského povrchu na jednu družici)
- Vysoké zpoždění šíření (~250 ms pro zpáteční cestu) vyžadující úpravy protokolů
- Funguje jako 3GPP definovaný síťový uzel (např. gNB) v Neterestriální síti (NTN)
- Používá Servisní spoje (k UE) a Přípojná spojení (k bráně)
- Podporováno v konkrétních kmitočtových pásmech 5G NR (např. n255, n256) pro satelitní provoz

## Související pojmy

- [LEO – Low-Earth Orbiting satellites](/mobilnisite/slovnik/leo/)
- [MEO – Medium-Earth Orbiting satellites](/mobilnisite/slovnik/meo/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TS 22.887** (Rel-20) — Study on satellite access - Phase 4
- **TS 23.008** (Rel-19) — Organization of Subscriber Data
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 28.874** (Rel-19) — Study on Management Aspects of NTN Phase 2
- … a dalších 22 specifikací

---

📖 **Anglický originál a plná specifikace:** [GEO na 3GPP Explorer](https://3gpp-explorer.com/glossary/geo/)
