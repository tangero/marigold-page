---
slug: "ecn"
url: "/mobilnisite/slovnik/ecn/"
type: "slovnik"
title: "ECN – Explicit Congestion Notification"
date: 2026-01-01
abbr: "ECN"
fullName: "Explicit Congestion Notification"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ecn/"
summary: "Explicit Congestion Notification (ECN) je mechanismus pro správu zahlcení sítě, který umožňuje směrovačům signalizovat koncovým bodům hrozící zahlcení označením paketů, nikoli jejich zahazováním. V 3G"
---

ECN je mechanismus pro správu zahlcení sítě přizpůsobený pro mobilní sítě, kde směrovače signalizují hrozící zahlcení označováním paketů namísto jejich zahazování, aby se snížily ztráty a latence a zlepšila se QoS.

## Popis

Explicit Congestion Notification (ECN) je mechanismus pro řízení zahlcení definovaný v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 3168 a přijatý 3GPP pro použití v mobilních paketových jádrových sítích. Umožňuje síťovým uzlům (např. směrovačům, branám) upozornit koncové body na zahlcení nastavením bitů ECN v hlavičce IP paketu, místo aby se spoléhalo pouze na zahazování paketů jako na implicitní signál. V architekturách 3GPP je ECN integrováno do Evolved Packet Core (EPC) a 5G Core (5GC) pro správu toků dat, zejména přes [GTP](/mobilnisite/slovnik/gtp/) tunely a rozhraní SGi/N6. Proces využívá dva bity v IP hlavičce: bit ECN-Capable Transport ([ECT](/mobilnisite/slovnik/ect/)) indikuje podporu koncovým bodem a bit Congestion Experienced ([CE](/mobilnisite/slovnik/ce/)) je nastaven zahlcenými směrovači pro signalizaci zahlcení. Koncové body po přijetí paketů označených CE proaktivně sníží svou přenosovou rychlost, čímž zmírní zahlcení dříve, než dojde ke ztrátě paketů.

Architektonicky ECN funguje napříč více vrstvami v systémech 3GPP. Na vrstvě IP interaguje s transportními protokoly, jako jsou TCP a [QUIC](/mobilnisite/slovnik/quic/), které musí být ECN-aware, aby mohly na oznámení o zahlcení reagovat. V mobilním jádru mohou prvky jako [PGW](/mobilnisite/slovnik/pgw/)/[UPF](/mobilnisite/slovnik/upf/), TDF nebo PCEF implementovat označování ECN na základě řízení politik nebo detekce zahlcení v reálném čase. Klíčové komponenty zahrnují pole ECN v hlavičkách IPv4 nebo IPv6, algoritmy detekce zahlcení v síťových uzlech (např. správa front jako RED nebo CoDel) a mechanismy reakce koncových bodů na zahlcení. Úlohou ECN je zlepšit Quality of Service (QoS) snížením ztrátovosti paketů a jitteru, což je klíčové pro aplikace citlivé na zpoždění, jako je hlas, video a interaktivní hry v mobilních sítích.

Jak ECN funguje v kontextu 3GPP, zahrnuje několik kroků. Nejprve koncové body vyjednají podporu ECN během navazování transportní relace. Když pakety procházejí sítí, směrovače sledují délky front; pokud je zahlcení hrozící, označí pakety CE místo jejich zahazování, za předpokladu, že pakety jsou ECN-capable. V mobilních sítích může k tomuto označení docházet na úzkých místech, jako je rozhraní SGi mezi PGW a internetem, nebo uvnitř jádra během vysokého zatížení provozem. Označené pakety jsou doručeny příjemci, který přenese signál o zahlcení zpět k odesílateli prostřednictvím potvrzení na transportní vrstvě. Odesílatel poté sníží svou přenosovou rychlost, čímž uvolní zahlcení. Specifikace 3GPP rozšiřují ECN pro podporu diferencovaných služeb a integraci s QoS frameworky, jako je PCC (Policy and Charging Control), což operátorům umožňuje aplikovat politiky ECN na základě profilů účastníků nebo typů služeb.

## K čemu slouží

ECN bylo vytvořeno, aby řešilo neefektivnost tradičního řízení zahlcení, které spoléhá na ztrátu paketů jako implicitní signál síťového zahlcení. V mobilních sítích může být ztráta paketů obzvláště škodlivá kvůli variabilitě rádiového rozhraní a omezené šířce pásma, což způsobuje zvýšenou latenci a sníženou propustnost pro aplikace. ECN to řeší poskytováním explicitních, včasných oznámení o zahlcení, což umožňuje koncovým bodům reagovat dříve, než ke ztrátě dojde, a tím zlepšuje celkovou efektivitu sítě a uživatelský zážitek.

Historický kontext sahá do snah IETF z konce 90. let o vylepšení internetového řízení zahlcení, které vedly k RFC 3168. 3GPP přijalo ECN počínaje Release 7 za účelem optimalizace paketových služeb v sítích UMTS a později LTE/5G. Předchozí přístupy, jako je tail-drop nebo RED bez ECN, vedly ke zbytečnému zahazování paketů a timeoutům TCP, což degradovalo výkon pro aplikace v reálném čase. ECN nabídlo proaktivní alternativu v souladu s cíli 3GPP pro vylepšenou QoS a podporu multimediálních služeb.

Motivace pro ECN v 3GPP zahrnují snížení latence pro aplikace s nízkou latencí, šetření rádiových prostředků minimalizací retransmisí a umožnění lepšího řízení provozu v přetížených scénářích. Řeší omezení dřívějších systémů mobilních dat, kterým chyběla sofistikovaná signalizace zahlcení, a podporuje tak vývoj směrem k all-IP sítím a službám rich media. ECN také usnadňuje soulad s regulatorními požadavky na neutralitu sítě a efektivní využití zdrojů.

## Klíčové vlastnosti

- Explicitní signalizace zahlcení prostřednictvím bitů v IP hlavičce (ECT a CE) k zabránění zahazování paketů
- Integrace s QoS frameworky 3GPP, jako je PCC, pro správu zahlcení založenou na politikách
- Podpora transportních protokolů včetně TCP, SCTP a QUIC s vyjednáváním podpory ECN
- Použitelnost napříč rozhraními mobilního jádra (např. SGi, N6) a GTP tunely
- Snížení ztrátovosti paketů a latence pro zlepšení výkonu aplikací
- Kompatibilita se standardy IETF (RFC 3168, RFC 8087) a IPv4/IPv6

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 22.495** (Rel-7) — NGN Requirements for IMS Services
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 23.860** (Rel-10) — Codec Rate Adaptation Enhancements Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [ECN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ecn/)
