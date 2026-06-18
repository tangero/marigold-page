---
slug: "tnl"
url: "/mobilnisite/slovnik/tnl/"
type: "slovnik"
title: "TNL – Transport Network Layer"
date: 2026-01-01
abbr: "TNL"
fullName: "Transport Network Layer"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tnl/"
summary: "Podpůrná síťová infrastruktura, která poskytuje konektivitu a přenosové služby pro uživatelská data a signalizaci mezi síťovými uzly v systému 3GPP. Je nezávislá na rádiové technologii a poskytuje spo"
---

TNL je podpůrná síťová infrastruktura založená na IP, která poskytuje konektivitu a přenosové služby pro uživatelská data a signalizaci mezi uzly v systému 3GPP.

## Popis

Transportní síťová vrstva (Transport Network Layer, TNL) v systémech 3GPP označuje základní síťovou infrastrukturu zodpovědnou za přenos veškeré signalizace řídicí roviny a datového provozu uživatelské roviny mezi různými síťovými funkcemi a uzly. Jedná se o logickou vrstvu, která abstrahuje fyzické přenosové spoje (např. optické vlákno, mikrovlnný spoj) a přepínací/směrovací zařízení. TNL poskytuje přenosovou službu, která propojuje prvky rádiové přístupové sítě (RAN), jádra sítě (CN) a mezi RAN a CN. Jejím hlavním úkolem je poskytovat spolehlivou, škálovatelnou a často na kvalitu služeb (QoS) citlivou službu doručování paketů.

Z architektonického hlediska není TNL jediným celkem, ale souborem technologií a protokolů. V moderních sítích 3GPP (od 3G výše) je převážně založena na internetovém protokolu (IP). Pro provoz uživatelské roviny v RAN využívá TNL protokol [GTP](/mobilnisite/slovnik/gtp/) pro uživatelskou rovinu ([GTP-U](/mobilnisite/slovnik/gtp-u/)) nad [UDP](/mobilnisite/slovnik/udp/)/IP k vytváření tunelů mezi uzly, jako je gNB a [UPF](/mobilnisite/slovnik/upf/), což zajišťuje izolaci provozu a přeposílání na základě identifikátorů koncových bodů tunelů ([TEID](/mobilnisite/slovnik/teid/)). Pro signalizaci řídicí roviny se běžně používají protokoly jako [SCTP](/mobilnisite/slovnik/sctp/) nad IP pro spolehlivý přenos signalizace, například na rozhraní [NGAP](/mobilnisite/slovnik/ngap/) mezi gNB a [AMF](/mobilnisite/slovnik/amf/). TNL také zahrnuje technologie nižších vrstev, jako je Ethernet, MPLS nebo optický přenos (OTN), pro fyzickou a spojovou vrstvu.

Funguje tak, že vyšší protokolové vrstvy 3GPP (např. RRC, NGAP, F1-AP) využívají služby TNL. Předávají jí datové jednotky protokolu (PDU) a TNL je zodpovědná za jejich doručení partnerské entitě. TNL zajišťuje funkce jako směrování, řízení zahlcení, fragmentaci a v některých případech i zabezpečení (např. IPsec). V kontextu RAN jsou mezi uzly vytvářeny specifické TNL asociace (TNLA) pro zajištění redundance a rozdělení zátěže. Výkonnost TNL – její latence, zpoždění, ztráta paketů a šířka pásma – přímo ovlivňuje výkonnost mobilních služeb, které podporuje, což činí její návrh a správu kritickými pro síťové operátory.

## K čemu slouží

Koncept samostatné transportní síťové vrstvy je základním prvkem od počátků digitálních mobilních sítí. Jejím účelem je oddělit problematiku rádiově specifických a služebně specifických protokolových vrstev od obecného problému přenosu dat. Tato abstrakce umožňuje, aby se architektury rádiového přístupu a jádra sítě 3GPP vyvíjely nezávisle na podkladové transportní technologii. Zpočátku, v 2G a raném 3G, byl přenos často založen na TDM okruzích. Přechod na paketovou TNL (IP) od 3GPP Release 5 byl hnán potřebou vyšší efektivity, flexibility a nákladové efektivity pro zvládání rostoucího datového provozu.

TNL řeší několik kritických problémů. Poskytuje jednotnou, škálovatelnou páteřní síť pro agregaci provozu z tisíců základnových stanic. Umožňuje sdílení sítí a virtualizaci tím, že poskytuje společnou transportní strukturu. Definováním standardních transportních protokolů (jako GTP, SCTP) zajišťuje interoperabilitu mezi zařízeními různých výrobců. Vývoj směrem k plně IP TNL řešil omezení přepojování okruhů, které bylo neefektivní pro trhaný datový provoz a obtížně škálovatelné. Pokračujícím účelem TNL je podpora stále rostoucích požadavků na kapacitu, nižší latenci (pro URLLC), synchronizaci a síťové řezy prostřednictvím začleňování pokroků v transportních technologiích, jako je Segment Routing, Time-Sensitive Networking (TSN) a vylepšené mechanismy QoS.

## Klíčové vlastnosti

- Poskytuje abstrakci pro fyzické přenosové spoje (optické vlákno, mikrovlnný spoj, metalický kabel)
- Primárně je založena na IP síťování pro směrování a přeposílání paketů
- Využívá specifické protokoly pro tunelování (GTP-U) a spolehlivou signalizaci (SCTP)
- Podporuje rozlišení kvality služeb (QoS) pro různé typy provozu
- Umožňuje síťovou redundanci a rozdělení zátěže prostřednictvím více TNL asociací
- Tvoří základ pro síťové řezy tím, že poskytuje izolované transportní zdroje pro každý řez

## Související pojmy

- [TNLA – Transport Network Layer Association](/mobilnisite/slovnik/tnla/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)
- [SCTP – Stream Control Transmission Protocol](/mobilnisite/slovnik/sctp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- **TS 25.442** (Rel-19) — Node B Implementation Specific O&M Transport via RNC
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 28.874** (Rel-19) — Study on Management Aspects of NTN Phase 2
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 32.860** (Rel-14) — D-SON MLB OAM Enhancement Study
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [TNL na 3GPP Explorer](https://3gpp-explorer.com/glossary/tnl/)
