---
slug: "tp"
url: "/mobilnisite/slovnik/tp/"
type: "slovnik"
title: "TP – TelePresence"
date: 2025-01-01
abbr: "TP"
fullName: "TelePresence"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tp/"
summary: "TelePresence (TP) označuje soubor pokročilých, imerzních komunikačních služeb standardizovaných 3GPP, jejichž cílem je napodobit zážitek z osobního setkání. Kombinuje ultra vysoké rozlišení videa, pro"
---

TP je soubor pokročilých, imerzních komunikačních služeb standardizovaných 3GPP, které napodobují osobní setkání prostřednictvím ultra vysokého rozlišení videa, prostorového zvuku a interaktivních médií.

## Popis

TelePresence (TP) v kontextu 3GPP není jediný protokol, ale komplexní služební koncept a rámec pro imerzní, multimediální komunikaci v reálném čase. Je definován v řadě specifikací pokrývajících služební požadavky, architekturu, účtování a správu. Služby TP přesahují rámec tradiční videokonference tím, že usilují o psychologicky přesvědčivý pocit „být tam“ a „být spolu“ se vzdálenými účastníky. To zahrnuje multisenzorický zážitek integrující video v ultra vysokém rozlišení (např. 4K, 8K nebo 360stupňové), věrný prostorový nebo binaurální zvuk přenášející směr a vzdálenost a potenciálně haptické nebo jiné interaktivní mediální toky.

Architektonicky služby TP využívají IP Multimedia Subsystem (IMS) jako základní řídicí a signalizační rámec pro zřizování, správu a ukončování relací. Mediální toky pro TP však kladou extrémní nároky na přenosovou síť. Tyto toky mohou být směrovány přes entity Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) ke zpracování (např. kompozice videa, mixáž audia) nebo mohou využívat point-to-point nebo multi-point protokoly pro přenos v reálném čase. Mezi klíčové architektonické komponenty patří UE (které musí podporovat špičkové kamery, displeje a kodeky), rámec pro řízení politiky a účtování ([PCC](/mobilnisite/slovnik/pcc/)) pro zajištění odpovídající QoS a podpora síťového segmentování a edge computingu v 5G Core Network.

Z pohledu technického provozu TP relace začíná signalizací založenou na IMS ([SIP](/mobilnisite/slovnik/sip/)) k vyjednání parametrů relace, včetně podporovaných typů médií, kodeků, datových toků a požadavků na QoS. Je aktivován rámec PCC k zřízení vyhrazených QoS toků v systému 5G, které garantují potřebnou šířku pásma, prioritu a rozpočet zpoždění paketů. Mediální toky jsou následně přenášeny pomocí protokolů jako [RTP](/mobilnisite/slovnik/rtp/)/[RTCP](/mobilnisite/slovnik/rtcp/) přes [UDP](/mobilnisite/slovnik/udp/)/IP. Pokročilé kodeky jako [HEVC](/mobilnisite/slovnik/hevc/)/H.265 nebo [VVC](/mobilnisite/slovnik/vvc/)/H.266 jsou nezbytné pro kompresi masivních video dat. Kritickým aspektem je latence end-to-end, která musí být udržována extrémně nízká (ideálně pod několik desítek milisekund), aby byla zachována přirozená interakce a předešlo se pocitu zpoždění. To často vyžaduje využití Mobile Edge Computing (MEC) k hostování aplikačních serverů TP blíže uživatelům, čímž se minimalizuje přenosové zpoždění. Dále může TP využívat síťové segmentování k vytvoření instance virtuální sítě s garantovanými prostředky izolovanými od ostatního provozu, což zajišťuje konzistentní výkon.

## K čemu slouží

TelePresence byl vytvořen, aby řešil omezení stávajících nástrojů pro videokomunikaci, které často trpí nízkým rozlišením, špatnou kvalitou zvuku, znatelnou latencí a plochým, neimerzním zážitkem, který nepodporuje skutečnou spolupráci. Obchodním a společenským motivem bylo umožnit vzdálené interakce, které jsou stejně účinné jako osobní setkání, čímž se snižuje nutnost cestování, zvyšuje produktivita a umožňují se nové formy vzdálené spolupráce, vzdělávání a telemedicíny.

Historicky, s vývojem širokopásmového internetu a mobilních sítí, se stalo možné jednoduché videohovory, ale ty zůstaly slabou náhradou fyzické přítomnosti. Vzestup vysokorozlišovacích displejů a pokročilých kodeků vytvořil technologický základ pro něco více imerzního. 3GPP začalo standardizovat TP, aby zajistilo interoperabilitu mezi sítěmi a zařízeními a definovalo síťové schopnosti potřebné pro jeho podporu. To bylo obzvláště důležité při návrhu 5G, protože se TP stalo klíčovým hybatelem pro služební kategorie 5G: enhanced Mobile Broadband (eMBB) a Ultra-Reliable Low-Latency Communication (URLLC).

Problémy, které TP řeší, jsou mnohostranné: technické (vyžadující od sítí podporu nebývalé propustnosti a latence), zážitkové (vytváření přirozeného pocitu přítomnosti) a komerční (definice modelů účtování a standardů interoperability). Řeší omezení předchozí „videokonference“ tím, že považuje imerzi za prvořadý služební požadavek, což nutí celý systém – od schopností UE po QoS mechanismy v core síti – se vyvíjet. Jeho standardizace zajišťuje, že TP služba od jednoho dodavatele může bezproblémově fungovat s UE a sítěmi od jiných dodavatelů, čímž podporuje konkurenční ekosystém a široké přijetí.

## Klíčové vlastnosti

- Imerzní video v ultra vysokém rozlišení (4K/8K, 360°, s více pohledy)
- Věrný prostorový zvuk s reprodukcí akustické scény
- Integrace s IMS pro řízení relací, autentizaci a interoperabilitu
- Vyžaduje extrémní QoS: velmi vysokou šířku pásma, ultra nízkou latenci a vysokou spolehlivost
- Využívá schopnosti sítě 5G, jako je síťové segmentování a Mobile Edge Computing (MEC)
- Podporuje pokročilé zpracování médií (např. adaptaci výřezu pro VR, mixáž médií)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 24.103** (Rel-19) — Telepresence Protocol for IMS
- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling
- **TS 28.735** (Rel-19) — STN Interface NRM IRP Information Service
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 32.742** (Rel-11) — STN NRM for Configuration Management
- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study
- **TS 32.854** (Rel-11) — FMC Federated Network Information Model
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- **TS 36.579** — 3GPP TR 36.579
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [TP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tp/)
