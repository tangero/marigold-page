---
slug: "av"
url: "/mobilnisite/slovnik/av/"
type: "slovnik"
title: "AV – Audio-Visual"
date: 2026-01-01
abbr: "AV"
fullName: "Audio-Visual"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/av/"
summary: "AV označuje multimediální obsah kombinující zvukovou a obrazovou složku v sítích 3GPP. Zahrnuje jak kombinované audio-video proudy, tak samostatná audio nebo video média. Tento základní koncept umožňu"
---

AV je základní koncept pro multimediální obsah kombinující zvukovou a obrazovou složku, který umožňuje služby jako videohovory a streamování v rámci mobilních sítí 3GPP.

## Popis

Audio-Visual (AV) ve standardech 3GPP představuje komplexní rámec pro zpracování multimediálního obsahu, který zahrnuje zvukovou, obrazovou nebo obě synchronizované složky. Architektura pro AV služby pokrývá více síťových domén včetně uživatelského zařízení (UE), rádiové přístupové sítě (RAN) a jádra sítě (CN), přičemž jsou definovány specifické protokoly a kodeky pro efektivní přenos. AV obsah je zpracováván prostřednictvím mediálních kodeků (jako [AMR](/mobilnisite/slovnik/amr/) pro audio a H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/) pro video), zabalen podle protokolů [RTP](/mobilnisite/slovnik/rtp/)/[RTCP](/mobilnisite/slovnik/rtcp/) a transportován přes IP přenosové cesty s odpovídajícím zacházením z hlediska QoS.

Na technické úrovni zahrnují AV služby několik klíčových komponent: funkce kódování/dekódování médií v UE a aplikačních serverech, mediální brány pro konverzi formátů, funkce mediálních zdrojů pro zpracování a řízení politiky pro správu kvality. Specifikace 3GPP definují podrobné procedury pro zřizování, modifikaci a ukončení AV relací prostřednictvím signalizace založené na [SIP](/mobilnisite/slovnik/sip/) nebo [HTTP](/mobilnisite/slovnik/http/). Doručování médií může probíhat prostřednictvím unicastu (bod-bod), multicastu nebo broadcastových mechanismů v závislosti na typu služby, se specifickými adaptacemi pro různé rádiové podmínky a síťové schopnosti.

AV služby se integrují s více podsystémy 3GPP včetně IMS (IP Multimedia Subsystem) pro konverzační služby, [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast Multicast Service) pro vysílání a přenosových cest EPS (Evolved Packet System) pro streamování. Na AV mediální proudy jsou aplikovány bezpečnostní mechanismy včetně šifrování (pomocí SRTP) a ochrany integrity, přičemž správa klíčů je řešena prostřednictvím protokolů jako MIKEY nebo DTLS-SRTP. Systém podporuje dynamickou adaptaci na síťové podmínky prostřednictvím technik jako adaptivní streamování s proměnným datovým tokem, kde se kvalita videa přizpůsobuje na základě dostupné šířky pásma a schopností zařízení.

Kvalita služby pro AV je řízena prostřednictvím vyhrazených přenosových cest s odpovídajícími identifikátory třídy QoS (QCIs), které zajišťují nízkou latenci pro konverzační video a dostatečnou šířku pásma pro streamování. Rozpočet zpoždění paketů (PDB), míra ztráty paketů (PELR) a úrovně priority jsou specificky konfigurovány pro různé typy AV služeb. Síťové funkce včetně PCRF (Policy and Charging Rules Function) a PCEF (Policy and Charging Enforcement Function) spolupracují na vynucení těchto politik a zajištění konzistentní kvality AV napříč mobilní sítí.

## K čemu slouží

Schopnosti AV byly zavedeny za účelem umožnění bohatých multimediálních služeb přes mobilní sítě, čímž reagovaly na rostoucí poptávku po video komunikaci a spotřebě obsahu. Před standardizovaným zpracováním AV primárně podporovaly mobilní sítě hlasové a základní datové služby, přičemž pro multimédia existovala proprietární řešení postrádající interoperabilitu. Formální definice AV v rámci specifikací 3GPP vytvořila jednotný rámec, který umožnil konzistentní implementaci napříč zařízeními a sítěmi, a tím i globální multimediální služby.

Vytvoření standardů AV vyřešilo několik kritických problémů: poskytlo efektivní kompresní techniky vhodné pro mobilní sítě s omezenou šířkou pásma, definovalo mechanismy kvality služby od konce ke konci pro časově citlivá média a stanovilo bezpečnostní protokoly pro ochranu multimediálního obsahu. Tím byly odstraněny limity dřívějších přístupů, kdy byly video služby buď nedostupné, nebo implementovány nestandardizovanými metodami, které trpěly špatnou kvalitou, omezenou kompatibilitou zařízení a bezpečnostními slabinami.

Historicky se zavedení AV ve vydání 6 časově shodovalo s nasazením sítí 3G, které nabídly dostatečnou šířku pásma pro video služby. To umožnilo nové výnosové služby pro operátory včetně videohovorů, mobilní televize a video streamování. Standardizace zajistila, že AV služby mohou škálovat napříč různými generacemi sítí při zachování zpětné kompatibility, což podpořilo vývoj od přepojovaných okruhů pro videotelefonii k paketovým multimediálním službám v pozdějších vydáních.

## Klíčové vlastnosti

- Podpora synchronizovaných audio a video proudů s požadavky na synchronizaci obrazu a zvuku
- Podpora více kodeků včetně schopností adaptivního streamování s proměnným datovým tokem
- Správa kvality služby od konce ke konci s vyhrazenými přenosovými cestami pro mediální provoz
- Integrovaná bezpečnost prostřednictvím šifrování SRTP a protokolů pro správu klíčů
- Podpora více metod doručování: unicast, multicast a broadcast
- Dynamická adaptace na síťové podmínky a schopnosti zařízení

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)

## Definující specifikace

- **TR 22.827** (Rel-17) — Study on Audio-Visual Service Production Stage 1
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study
- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling
- **TS 29.866** (Rel-19) — IMS Disaster Prevention & Restoration Enhancement
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.203** (Rel-19) — IMS Security Specification
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TS 33.514** (Rel-20) — 5G Security Assurance for UDM
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study
- **TR 33.924** (Rel-19) — GBA-OpenID Interworking Specification
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [AV na 3GPP Explorer](https://3gpp-explorer.com/glossary/av/)
