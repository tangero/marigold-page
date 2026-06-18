---
slug: "sps"
url: "/mobilnisite/slovnik/sps/"
type: "slovnik"
title: "SPS – Semi-Persistent Scheduling"
date: 2025-01-01
abbr: "SPS"
fullName: "Semi-Persistent Scheduling"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sps/"
summary: "Metoda plánování, při níž jsou rádiové prostředky (čas/frekvence) předem přiděleny uživatelskému zařízení (UE) na určitý časový úsek nebo až do deaktivace, což snižuje režii řídicí signalizace. Je opt"
---

SPS je metoda plánování, při níž jsou rádiové prostředky předem přiděleny uživatelskému zařízení (UE) na určitý časový úsek, což snižuje režii řídicí signalizace tím, že se pro každý přenos nevyžaduje dynamické povolení. Je optimální pro periodický provoz, například VoIP.

## Popis

Semi-Persistent Scheduling (SPS) je mechanismus správy rádiových prostředků definovaný ve specifikacích 3GPP pro LTE a NR, který nastavuje rovnováhu mezi plně dynamickým a plně statickým plánováním. V dynamickém plánování síť vysílá povolení ([DCI](/mobilnisite/slovnik/dci/)) na kanálu [PDCCH](/mobilnisite/slovnik/pdcch/) pro každý jednotlivý uplinkový přenos nebo downlinkový příjem, což poskytuje maximální flexibilitu, ale způsobuje značnou režii řídicího kanálu. SPS naopak konfiguruje UE s opakujícím vzorem rádiových prostředků (specifické subframes/sloty a resource blocks) pro určitý logický kanál, typicky spojený s periodickou službou jako Voice over IP (VoIP). Po aktivaci jedinou DCI zprávou UE automaticky používá předdefinované prostředky na konfigurovaném intervalu bez nutnosti dalších povolení, což dramaticky snižuje zatížení PDCCH.

Provoz SPS zahrnuje fáze konfigurace, aktivace a deaktivace. Síť nejprve konfiguruje UE parametry SPS prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) signalizace. Tyto parametry zahrnují interval SPS (např. 20 ms pro VoIP), specifický časový offset a frekvenční prostředky. Konfigurace je spojena s specifickým Cell Radio Network Temporary Identifier ([C-RNTI](/mobilnisite/slovnik/c-rnti/)) a konfigurovaným indexem konfigurace grantu. Aktivace je provedena dynamicky prostřednictvím speciální DCI (formát 0_0/0_1 pro [UL](/mobilnisite/slovnik/ul/), 1_0/1_1 pro [DL](/mobilnisite/slovnik/dl/) v NR) zakódované s [CS-RNTI](/mobilnisite/slovnik/cs-rnti/) (Configured Scheduling [RNTI](/mobilnisite/slovnik/rnti/), který se vyvinul z konceptu SPS C-RNTI). Tato aktivující DCI odkazuje na předkonfigurovanou SPS konfiguraci a efektivně 'spouští timer'. Po jejím přijetí UE začíná používat periodické prostředky podle konfigurovaného vzoru.

Pro uplinkový SPS UE vysílá na předem přidělených prostředků bez čekání na UL povolení. Pro downlinkový SPS UE monitoruje PDSCH na předem přidělených prostředků. Síť může také vysílat dynamické povolení, které pro určitý okamžik přebíjí SPS prostředky, což poskytuje flexibilitu. SPS je deaktivována buď explicitně DCI zakódovanou s CS-RNTI s specifickým polem nastaveným na indikaci deaktivace, implicitně po konfigurovaném počtu prázdných přenosů (v UL), nebo při RRC rekonfiguraci. Klíčové komponenty zahrnují CS-RNTI (který jednoznačně identifikuje UE s aktivními SPS konfiguracemi), parametry SPS konfigurace v RRC a specifické DCI formáty a zakódování používané pro aktivaci/deaktivaci.

V 5G NR byly koncepty SPS rozšířeny a generalizovány pod označením 'Configured Grants' pro uplink, které zahrnují dva typy. Configured grant typu 1 je podobný tradičnímu SPS, kde všechny parametry jsou poskytnuty RRC. Configured grant typu 2 zahrnuje poskytnutí některých parametrů RRC a DCI (používající CS-RNTI) aktivující periodické prostředky. To poskytuje více dynamickou kontrolu. SPS je stále klíčová pro NR služby vyžadující ultra-reliable low-latency communications (URLLC) a periodický provoz industrial IoT, kde minimalizace řídicí latence a garantování dostupnosti prostředků jsou prioritní. Mechanismus odlehčuje PDCCH, snižuje plánovací latenci pro periodické pakety a šetří životnost baterie UE tím, že snižuje potřebu kontinuálního blind dekódování řídicích kanálů pro každý přenos.

## K čemu slouží

SPS byla primárně vyvinuta pro efektivní podporu služeb s předvídatelnými, periodickými provozními vzory, nejvýznamněji Voice over IP (VoIP). V raných LTE nasazeních bylo pozorováno, že použití plně dynamického plánování pro VoIP – kde je malý paket (např. hlasový frame) generován každých 20 ms – bylo velmi neefektivní. Každý 40-byte hlasový paket vyžadoval samostatné DCI povolení na PDCCH, které mohlo mít velikost 40-50 bitů. To znamenalo, že režie řídicí signalizace mohla přiblížit nebo i překročit samotnou datovou payload, což vážně limitovalo kapacitu VoIP na buňce.

Problém, který SPS řeší, je tento bottleneck režie řídicího kanálu. Předem přidělováním prostředků SPS odstraňuje potřebu povolení pro každý jednotlivý přenos paketu. To dramaticky zvyšuje počet VoIP uživatelů, které jedna buňka může podporovat, protože limitujícím faktorem se stávají dostupné PDSCH/PUSCH prostředky namísto kapacity PDCCH. Také snižuje plánovací latenci, protože UE nemusí čekat na příchod povolení; již ví, kdy a kde vysílat nebo přijímat, což je prospěšné pro udržení konzistentní nízké latence pro real-time služby.

Historicky uvedena v LTE Release 8, SPS řešila klíčový problém pro to, aby LTE byla konkurenční technologie pro hlasové služby. Jak se sítě vyvíjely pro podporu více IoT a M2M aplikací s periodickým reportováním (např. smart meters, senzorová data), využití SPS expandovalo mimo VoIP. V 5G NR byly principy SPS upraveny do více flexibilního frameworku configured grant pro podporu širšího spektra scénářů URLLC a periodického provozu s ještě striktnějšími požadavky na latenci a spolehlivost. SPS reprezentuje fundamentální optimalizaci v designu celulárních systémů: obětování malého množství plánovací flexibility pro masivní zisk v řídicí efektivitě a latenci pro předvídatelné datové toky.

## Klíčové vlastnosti

- Předem přiděluje periodické časově-frekvenční prostředky uživatelskému zařízení (UE), snižuje režii signalizace PDCCH/PUCCH.
- Aktivace a deaktivace jsou provedeny dynamicky prostřednictvím DCI zakódované s CS-RNTI.
- Podporuje uplinkové (UL SPS/Configured Grant) i downlinkové (DL SPS) přenosy.
- Konfigurační parametry (interval, offset, prostředky) jsou poskytnuty prostřednictvím RRC signalizace.
- Umožňuje dynamické povolení přebít předkonfigurované SPS prostředky pro flexibilitu.
- Kritická pro efektivní podporu periodického provozu, jako je VoIP, URLLC a IoT reportování.

## Související pojmy

- [CS-RNTI – Configured Scheduling Radio Network Temporary Identifier](/mobilnisite/slovnik/cs-rnti/)
- [VOIP – Voice over IP](/mobilnisite/slovnik/voip/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.954** (Rel-19) — UE Headset Electrical Interface Testing
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.822** (Rel-11) — LTE RAN Enhancements for Diverse Data Apps
- **TS 38.202** (Rel-19) — 5G NR Physical Layer Services
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [SPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sps/)
