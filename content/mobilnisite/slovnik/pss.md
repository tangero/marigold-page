---
slug: "pss"
url: "/mobilnisite/slovnik/pss/"
type: "slovnik"
title: "PSS – Packet Switched Streaming Service"
date: 2025-01-01
abbr: "PSS"
fullName: "Packet Switched Streaming Service"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pss/"
summary: "Standardizovaná služba 3GPP pro doručování audio a video streamů v reálném čase přes paketově přepínané sítě jako GPRS, UMTS a LTE. Definuje end-to-end protokoly pro doručování médií, řízení relace a"
---

PSS (služba streamování přes paketovou síť) je standardizovaná služba 3GPP pro doručování audio a video streamů v reálném čase přes paketově přepínané mobilní sítě, která definuje protokoly pro doručování médií, řízení relace a správu kvality.

## Popis

Služba streamování přes paketovou síť (Packet Switched Streaming Service, PSS) je komplexní servisní rámec 3GPP navržený pro streamování multimediálního obsahu, jako je audio a video, přes IP-based paketově přepínané mobilní sítě. Byla poprvé představena ve vydání 3GPP Release 99 a vyvíjela se v následujících vydáních pro podporu nových kodeků, transportních protokolů a síťových schopností. PSS specifikuje end-to-end architekturu zahrnující streamovací server a klienta (User Equipment, UE). Služba zahrnuje protokoly pro navázání a řízení relace (např. [RTSP](/mobilnisite/slovnik/rtsp/) - Real Time Streaming Protocol), transport médií (typicky [RTP](/mobilnisite/slovnik/rtp/) přes [UDP](/mobilnisite/slovnik/udp/)) a formáty mediálních kodeků. Zahrnuje také mechanismy pro adaptaci šířky pásma, správu vyrovnávací paměti a signalizaci kvality služeb (QoS) pro zvládnutí proměnných podmínek bezdrátových spojů.

Jádrem PSS je definice profilů a kodeků pro zajištění interoperability mezi servery a klienty od různých výrobců. Klíčové mediální kodeky historicky zahrnují [AMR-NB](/mobilnisite/slovnik/amr-nb/)/[WB](/mobilnisite/slovnik/wb/) pro audio a H.263, MPEG-4 Visual pro video, s pozdějšími doplňky jako H.264/[AVC](/mobilnisite/slovnik/avc/) a [HEVC](/mobilnisite/slovnik/hevc/). Transportní vrstva je postavena na RTP/[RTCP](/mobilnisite/slovnik/rtcp/) od IETF pro doručování a řízení médií, zatímco řízení relace je řešeno pomocí RTSP, SIP nebo HTTP. Architektura také zahrnuje popis prezentace, často poskytovaný přes SDP (Session Description Protocol), který informuje klienta o dostupných mediálních streamech, jejich kodecích a síťových adresách.

PSS hraje klíčovou roli v ekosystému mobilních služeb tím, že poskytuje standardizovaný způsob doručování obsahu v reálném čase, na vyžádání a živého streamování. Integruje se s QoS mechanismy jádrové sítě, což síti umožňuje alokovat vhodné přenašeče pro streamovací provoz. Servisní specifikace pokrývají nejen protokolové zásobníky, ale také chování klienta a serveru, formáty souborů pro streamování (jako 3GPP formát souboru) a metriky pro testování výkonu. Tato standardizace byla zásadní pro rané nasazení mobilní TV, video na vyžádání a dalších streamovacích aplikací, což vytvořilo konzistentní uživatelský zážitek napříč různými operátory a zařízeními.

## K čemu slouží

PSS byla vytvořena, aby umožnila doručování služeb multimediálního streamování v reálném čase přes paketově přepínané mobilní sítě 2.5G a 3G, což byl významný vývoj oproti okruhově přepínaným hlasovým službám. Před PSS neexistovala standardizovaná metoda pro streamování audia a videa přes sítě GPRS nebo UMTS, což vedlo k potenciálním problémům s interoperabilitou mezi poskytovateli obsahu, síťovým vybavením a terminály. Služba si kladla za cíl využít 'vždy připojenou' schopnost a vyšší datové rychlosti paketově přepínaných sítí k nabídnutí nových služeb generujících příjmy, jako je mobilní TV, video klipy a audio streamování.

Vývoj PSS řešil technické výzvy streamování přes bezdrátové spoje, které jsou náchylné k výkyvům šířky pásma, latenci a ztrátě paketů. Definováním kompletní sady protokolů a profilů kodeků zajistila, že streamovací servery a klienti mohou efektivně komunikovat a adaptovat se na síťové podmínky pro udržení přijatelné kvality. Poskytla také rámec pro poskytovatele obsahu k vytváření služeb, které mohou být nasazeny globálně, což podpořilo růst trhu s mobilními médii. Jak se sítě vyvíjely k HSPA a LTE, specifikace PSS byly aktualizovány pro podporu vyšších efektivit a nových schopností, čímž si udržela relevanci jako základní standard pro streamovací služby.

## Klíčové vlastnosti

- Standardizovaná end-to-end sada protokolů pro řízení relace (RTSP/SIP) a transport médií (RTP/RTCP)
- Podpora adaptivního streamování prostřednictvím mechanismů adaptace šířky pásma a správy vyrovnávací paměti
- Definované profily pro povinné a volitelné audio/video kodeky (např. AMR, H.263, MPEG-4, H.264)
- Integrace s mechanismy QoS 3GPP pro zřízení přenašeče a priorizaci provozu
- Specifikace formátu souboru 3GPP pro ukládání a streamování multimediálního obsahu
- Specifikace chování klienta a serveru pro zajištění interoperability a konzistentního uživatelského zážitku

## Související pojmy

- [RTSP – Real-time Streaming Protocol](/mobilnisite/slovnik/rtsp/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 22.233** (Rel-19) — Packet-switched Streaming Service (PSS) Stage 1
- **TS 22.246** (Rel-19) — MBMS User Services Specification
- **TR 22.947** (Rel-19) — Personal Broadcast Service (PBS) Use Cases
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.150** (Rel-19) — Syndicated Feed Reception (SFR) Specification
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.245** (Rel-19) — 3GPP Timed Text Format Specification
- **TS 26.246** (Rel-19) — 3GPP SMIL Language Profile Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- … a dalších 53 specifikací

---

📖 **Anglický originál a plná specifikace:** [PSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pss/)
