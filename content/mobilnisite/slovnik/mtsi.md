---
slug: "mtsi"
url: "/mobilnisite/slovnik/mtsi/"
type: "slovnik"
title: "MTSI – Multimedia Telephony Services for IMS"
date: 2025-01-01
abbr: "MTSI"
fullName: "Multimedia Telephony Services for IMS"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mtsi/"
summary: "MTSI je standardizovaná služba pro poskytování multimediální komunikace v reálném čase přes sítě IP Multimedia Subsystem (IMS). Umožňuje vysokou kvalitu hlasu, videa a doplňkových služeb, jako je čeká"
---

MTSI je služba standardizovaná 3GPP pro poskytování operátorské kvality (carrier-grade) a komunikací v reálném čase, jako je hlas a video, přes sítě IMS, která zajišťuje interoperabilitu, kvalitu služeb a soulad s regulačními požadavky.

## Popis

Multimedia Telephony Services for IMS (MTSI) je komplexní rámec definovaný 3GPP pro poskytování telefonních a multimediálních komunikačních služeb přes IP sítě s využitím architektury IMS. Je navržen tak, aby nahradil a vylepšil tradiční přepojování okruhů využitím flexibility a efektivity sítí s přepojováním paketů. MTSI podporuje širokou škálu typů médií, včetně hlasu ve vysokém rozlišení (např. kodek [EVS](/mobilnisite/slovnik/evs/)), videa, textu v reálném čase a přenosu souborů, vše integrované v rámci jediného servisního rámce. Služba je postavena na základních prvcích IMS, jako je Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)), Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), které spravují řízení relace, data účastníků a zpracování médií. Relace MTSI jsou navazovány pomocí SIP (Session Initiation Protocol) pro signalizaci a RTP (Real-time Transport Protocol) pro přenos médií, přičemž SDP (Session Description Protocol) se používá pro vyjednávání médií. Mezi klíčové architektonické komponenty patří MTSI Application Server ([AS](/mobilnisite/slovnik/as/)), který hostuje servisní logiku a komunikuje s jádrem IMS přes rozhraní [ISC](/mobilnisite/slovnik/isc/) (IMS Service Control) pro implementaci funkcí jako přesměrování hovorů nebo konferenční hovory. Služba také integruje s rámcem Policy and Charging Control (PCC) pro vynucování politik QoS a účtovacích pravidel, což zajišťuje, že toky médií dostávají odpovídající prioritu a způsob fakturace. MTSI definuje podrobné procedury pro navázání, změnu a ukončení relace, včetně podpory nouzových hovorů, zákonného odposlechu a spolupráce se staršími sítěmi, jako je PSTN a [CS](/mobilnisite/slovnik/cs/) fallback. Specifikuje přísné požadavky na výkon, jako je latence, chvění a ztráta paketů, aby byla zaručena uživatelská zkušenost srovnatelná nebo lepší než u tradiční telefonie. Rámec také zahrnuje mechanismy pro kontinuitu služeb, jako je Single Radio Voice Call Continuity (SRVCC) a enhanced SRVCC (eSRVCC), pro udržení aktivních relací během předávání mezi sítěmi LTE a 3G/2G. Role MTSI v síti spočívá v poskytování standardizované, interoperabilní platformy pro operátory, aby mohli nasazovat bohaté komunikační služby při zachování kontroly nad kvalitou, zabezpečením a monetizací.

## K čemu slouží

MTSI bylo vytvořeno, aby řešilo potřebu odvětví po standardizované, operátorské multimediální telefonní službě přes IP sítě, což umožňuje operátorům konkurovat [OTT](/mobilnisite/slovnik/ott/) komunikačním aplikacím. Před MTSI byly telefonní služby převážně založeny na přepojování okruhů, což omezovalo integraci multimediálních funkcí a bylo neefektivní pro datově orientované sítě. Vzestup IMS poskytl základ pro IP služby, ale byl vyžadován komplexní standard pro zajištění konzistentní implementace hlasových, video a doplňkových služeb napříč dodavateli a sítěmi. MTSI to řeší definováním kompletní servisní architektury, protokolů a výkonnostních měřítek, což umožňuje operátorům nabízet funkčně bohatou komunikaci se zaručenou kvalitou služeb a regulačním souladem. Historicky přechod od hlasu s přepojováním okruhů v 2G/3G k plně IP architektuře 4G LTE vytvořil mezeru pro hlasové služby, kterou MTSI zaplnilo jako součást řešení Voice over LTE (VoLTE). Řeší omezení proprietárních nebo fragmentovaných přístupů tím, že poskytuje interoperabilitu, umožňuje bezproblémový roaming a podporuje nouzové služby a požadavky na zákonný odposlech. Motivace sahá i do budoucí přípravy sítí pro 5G, kde se MTSI vyvíjí, aby podporovalo nové kodeky, vylepšené video služby a integraci s network slicing pro přizpůsobené poskytování služeb.

## Klíčové vlastnosti

- Podpora kodeků pro hlas a video ve vysokém rozlišení (např. EVS, HEVC)
- Integrace s jádrem IMS pro řízení relací a správu účastníků
- Komplexní doplňkové služby (čekání na hovor, přidržení, konferenční hovory atd.)
- Vynucování Quality of Service (QoS) prostřednictvím Policy and Charging Control (PCC)
- Mechanismy kontinuity služeb (SRVCC, eSRVCC) pro předávání do starších sítí
- Spolupráce se staršími sítěmi (PSTN, CS) a regulačními službami (nouzové hovory)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 22.813** (Rel-10) — Enhanced Voice Services for EPS Study
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.235** (Rel-12) — Default Codecs for 3GPP IP Multimedia Subsystem
- **TS 26.236** (Rel-12) — Packet Switched Conversational Multimedia Protocols
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- **TS 26.443** (Rel-19) — EVS Codec Floating-Point C Code
- **TS 26.444** (Rel-19) — EVS Codec Conformance Test Sequences
- **TS 26.447** (Rel-19) — EVS Frame Loss Concealment Procedure
- **TS 26.448** (Rel-19) — EVS Jitter Buffer Management Specification
- … a dalších 37 specifikací

---

📖 **Anglický originál a plná specifikace:** [MTSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtsi/)
