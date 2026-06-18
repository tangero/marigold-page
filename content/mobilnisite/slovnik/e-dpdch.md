---
slug: "e-dpdch"
url: "/mobilnisite/slovnik/e-dpdch/"
type: "slovnik"
title: "E-DPDCH – E-DCH Dedicated Physical Data Channel"
date: 2025-01-01
abbr: "E-DPDCH"
fullName: "E-DCH Dedicated Physical Data Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-dpdch/"
summary: "E-DPDCH je hlavní fyzický datový kanál pro uplink v HSUPA v UMTS. Přináší skutečné paketová data uživatelského rozhraní z UE do Node B vysokou rychlostí. Jeho přenosové parametry, jako rozprostření a"
---

E-DPDCH je hlavní fyzický datový kanál pro uplink v HSUPA v UMTS, který přenáší uživatelská data z UE do Node B vysokou rychlostí s přenosovými parametry, které se mohou dynamicky měnit každých 2 ms.

## Popis

E-DPDCH, nebo [E-DCH](/mobilnisite/slovnik/e-dch/) Dedicated Physical Data Channel, je základní fyzický datový kanál vrstvy pro High-Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)) v UMTS sítích. Je zodpovědný za transport zakódovaných a modulovaných uživatelských dat z User Equipment (UE) do Node B přes rozhraní vzduchu. Funguje pouze v Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)) režimu, E-DPDCH je charakterizován svým krátkým Transmission Time Interval ([TTI](/mobilnisite/slovnik/tti/)) 2 ms (nebo volitelně 10 ms) a jeho schopností podporovat variabilní, vysoké datové rychlosti pomocí adaptivní modulace a kódování. Kanál funguje spolu s [E-DPCCH](/mobilnisite/slovnik/e-dpcch/), který přenáší potřebné kontrolní informace pro jeho demodulaci.

Z technické perspektivy, E-DPDCH může využívat více fyzických kanálů paralelně (multi-code přenos) a variabilní rozprostření pro dosažení různých datových rychlostí. Specifický transportní formát, obsahující množství E-DPDCH a jejich rozprostření, je určen E-DCH Transport Format Combination ([E-TFC](/mobilnisite/slovnik/e-tfc/)) vybraným UE na základě plánovacích povolení (grantů) z Node B. Data na E-DPDCH jsou zpracovány přes kanálové kódování (Turbo kódování), prokládání a mapování fyzického kanálu před kombinováním s kontrolními kanály pro přenos. Klíčový operační aspekt je jeho využití Hybrid [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)) s měkkým kombinováním, kde inkrementální redundance retransmise mohou být vysílány na E-DPDCH pro korekci chyb bez potřebných retransmisí vyšší vrstvy, významně redukující latenci.

Architektura kanálu je hluboce integrována s rychlým plánovačem Node B. UE vysílá plánovací požadavek a ukazatel kvality kanálu, a Node B odpovídá absolutním nebo relativním povolením (grantem), které určuje maximální poměr síly UE může použít pro E-DPDCH relativně vůči DPCCH. Tato povolením řízená kontrola síly umožňuje Node B řídit uplink interference celé buňky. Síla E-DPDCH se může rychle měnit každé TTI, a jeho datová rychlost může škálovat od několika stovek kbps až po teoretický vrchol 5.76 Mbps v Release 6, a následně vylepšený v dalších releasách. Jeho design umožňuje efektivní využití spektra pro bursty provoz, což ho staví jako základní kámen UMTS evoluce k mobilnímu broadbandu.

## K čemu slouží

E-DPDCH byl vytvořen pro řešení vážných limitů pre-HSUPA UMTS uplinku, který používal Dedicated Channel (DCH). DCH byl designován pro kontinuální, circuit-switched-like provoz s plánováním řízeným RNC, výsledkem byly vysoké nastavovací časy a latence řádově 100 ms nebo více. To bylo neefektivní pro bursty, asymetrický charakter internetového datového provozu, kde uplink často potřeboval rychlý přenos malých paketů. Industrie potřebovala řešení, které může poskytnout vyšší vrcholové rychlosti, nižší latenci a lepší spektrální efektivitu pro uplink pro shodu s vylepšeními v downlinku (HSDPA).

3GPP Release 6 představil HSUPA pro splnění těchto požadavků, s E-DPDCH jako jeho hlavní datový kanál. Jeho účel je poskytnout fyzickou vrstvu schopnou podporovat rychlé plánování řízené Node B, adaptivní link adaptaci a HARQ s měkkým kombinováním—techniky již prokázané v HSDPA. Přenesením plánování do Node B a implementací 2 ms TTI, reakční čas pro povolení uplinkových zdrojů byl redukován na milisekundy, drasticky snižující latenci pro interaktivní aplikace. Multi-code a variabilní rozprostření design E-DPDCH řešil problém neefektivní alokace zdrojů pro variabilní velikosti paketů, umožňující síti rychle škálovat uplinkovou datovou rychlost podle aktuální potřebnosti.

Historicky, E-DPDCH umožnil UMTS nabídnout kompetitivní symetrický broadbandový zážitek, podporující aplikace jako video konference, online gaming a upload velkých souborů. Řešil uplink bottleneck, který se stal evidentním jak downlinkové rychlosti rostly s HSDPA, zajišťující UMTS může poskytnout vyvážený servis. Designové principy kanálu rychlé plánování, HARQ a krátké TTI položily základ pro následné uplinkové vylepšení v LTE a 5G NR.

## Klíčové vlastnosti

- Podporuje 2 ms a 10 ms Transmission Time Intervals (TTI) pro nízkou latenci
- Umožňuje multi-code přenos pro vysoké vrcholové datové rychlosti (až 5.76 Mbps v Rel-6)
- Využívá variabilní rozprostření (od 256 až do 2) pro adaptaci rychlosti
- Funguje s rychlým plánováním Node B přes absolutní a relativní povolení (grants)
- Používá Hybrid ARQ (HARQ) s měkkým kombinováním pro rychlou korekci chyb
- Přenosová síla je dynamicky řízena relativně vůči DPCCH pilotu

## Související pojmy

- [E-DPCH – EDCH – Dedicated Physical Channel](/mobilnisite/slovnik/e-dpch/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [TTI – Transmission Timing Interval](/mobilnisite/slovnik/tti/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.706** (Rel-13) — Downlink Enhancements for UMTS Study
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TS 25.823** (Rel-8) — Synchronised E-DCH Study for UTRA FDD
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [E-DPDCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-dpdch/)
