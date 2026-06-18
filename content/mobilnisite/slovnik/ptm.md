---
slug: "ptm"
url: "/mobilnisite/slovnik/ptm/"
type: "slovnik"
title: "PTM – Point to Multipoint"
date: 2025-01-01
abbr: "PTM"
fullName: "Point to Multipoint"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ptm/"
summary: "PTM je komunikační metoda, při níž jsou data přenášena z jednoho zdroje k více cílům současně. Je zásadní pro efektivní skupinové komunikační služby, jako je multimediální vysílání/multicast, a umožňu"
---

PTM je komunikační metoda, při níž jsou data přenášena z jednoho zdroje k více cílům současně, což umožňuje efektivní skupinové služby, jako je multimediální vysílání/multicast, a optimalizuje síťové zdroje.

## Popis

Point to Multipoint (PTM, bod–více bodů) je základní architektura síťové služby definovaná 3GPP pro doručování obsahu z jednoho zdroje více příjemcům. Funguje napříč více síťovými doménami, včetně jádra sítě (CN) a rádiové přístupové sítě (RAN). Architektura zahrnuje specifické funkční entity a rozhraní pro správu navázání relace, správu přenosových kanálů a distribuci dat. V CN slouží jako vstupní bod Broadcast-Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), které zajišťuje oznámení služby, zabezpečení a účtování. Pro RAN definuje PTM specifické rádiové přenosové kanály a přenosové režimy, jako je Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), který může využívat buď vyhrazený multicastový kanál, nebo sdílený broadcastový kanál v závislosti na počtu uživatelů v buňce.

Provoz začíná oznámením služby a přihlášením uživatele. Když je PTM relace aktivována, síť vytvoří společnou přenosovou cestu pro doručování dat. V RAN to zahrnuje konfiguraci multicastových rádiových přenosových kanálů. Datové pakety jsou replikovány v optimálních bodech sítě – často na rádiové základnové stanici (NodeB/gNB) – aby se minimalizoval provoz v jádru sítě. Mezi klíčové protokoly patří protokoly MBMS ([GTP](/mobilnisite/slovnik/gtp/) pro uživatelskou rovinu a specifická signalizace řídicí roviny) a protokoly RAN pro plánování a přenos přes rozhraní vzduch.

Role PTM je klíčová pro škálovatelnou skupinovou komunikaci. Je základem služeb, jako je mobilní [TV](/mobilnisite/slovnik/tv/), systémy veřejného varování a aktualizace softwaru. Díky využití sdílených síťových zdrojů výrazně zlepšuje spektrální účinnost a snižuje zatížení sítě ve srovnání s vytvářením individuálních Point-to-Point ([PTP](/mobilnisite/slovnik/ptp/)) spojení pro každého uživatele, což z ní činí základní technologii pro broadcastové a multicastové služby v celulárních sítích.

## K čemu slouží

Technologie PTM byla vytvořena, aby řešila neefektivitu používání více unicastových (point-to-point) spojení pro doručování stejného obsahu mnoha uživatelům. Před zavedením PTM by služby, jako je streamování videa pro skupinu, spotřebovávaly nadměrnou šířku pásma sítě a zdroje jádra sítě, protože stejné datové pakety byly odesílány individuálně každému účastníkovi. Tento přístup není škálovatelný a pro služby masového trhu se stává neúnosně nákladným.

Historická motivace vycházela z rostoucí poptávky po multimediální skupinové komunikaci, jako je mobilní [TV](/mobilnisite/slovnik/tv/) a vysílání živých událostí, v sítích 3G UMTS. 3GPP zavedla architekturu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), která je založena na principech PTM, aby umožnila efektivní přenos dat typu jeden–více. PTM řeší problém zahlcení sítě a neefektivního využívání rádiových zdrojů tím, že umožňuje replikaci dat na okraji sítě (v RAN) namísto v jádru.

Dále PTM podporuje nezbytné služby, jako jsou nouzová upozornění a skupinová volání pro veřejnou bezpečnost a komerční aplikace. Poskytuje standardizovaný mechanismus pro poskytovatele služeb k nabízení broadcastových/multicastových služeb, čímž vytváří nové zdroje příjmů a zároveň optimalizuje využití infrastruktury. Vývoj směrem k 5G s dalšími vylepšeními, jako je [MBS](/mobilnisite/slovnik/mbs/) (Multicast and Broadcast Services), pokračuje v tomto účelu pro nové případy užití, jako je V2X a imerzivní média.

## Klíčové vlastnosti

- Efektivní přenos dat typu jeden–více přes sdílené síťové zdroje
- Podpora jak broadcastového režimu (pro všechny uživatele v oblasti), tak multicastového režimu (pro přihlášenou skupinu)
- Integrovaná správa služeb prostřednictvím Broadcast-Multicast Service Center (BM-SC)
- Dynamické přepínání mezi PTM a PTP na základě počtu uživatelů v buňce
- Podpora účtování, zabezpečení (správa klíčů) a oznamování služby
- Optimalizace rádiových přenosových kanálů pro multicastový přenos v RAN

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 37.480** (Rel-19) — E1 Interface General Aspects and Principles
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [PTM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ptm/)
