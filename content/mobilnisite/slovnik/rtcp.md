---
slug: "rtcp"
url: "/mobilnisite/slovnik/rtcp/"
type: "slovnik"
title: "RTCP – Real-time Transport Control Protocol"
date: 2025-01-01
abbr: "RTCP"
fullName: "Real-time Transport Control Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rtcp/"
summary: "RTCP je řídicí protokol doplňující RTP, který poskytuje statistické a řídicí informace mimo přenosový pásmo pro relace přenosu médií v reálném čase. Je nezbytný pro monitorování QoS, synchronizaci med"
---

RTCP je řídicí protokol doplňující RTP, který poskytuje statistické a řídicí informace mimo přenosový pásmo pro monitorování QoS, synchronizaci proudů a umožnění adaptivního streamování v relacích přenosu médií v reálném čase.

## Popis

Protokol [RTCP](/mobilnisite/slovnik/rtpcp/) (Real-time Transport Control Protocol) funguje ve spojení s protokolem [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol) pro správu přenosu dat v reálném čase, jako je audio a video, přes IP sítě. Zatímco RTP zajišťuje vlastní přenos mediální náplně, RTCP využívá samostatné periodické řídicí pakety odesílané všem účastníkům relace. Tyto pakety nesou zprávy odesílatele a příjemce, které obsahují klíčové statistiky, jako je počet paketů, počet oktetů, zpoždění (jitter), doba odezvy (round-trip time) a podíl ztracených paketů. Tato zpětná vazba umožňuje aplikacím monitorovat kvalitu služeb (QoS) a zahlcení sítě, což podporuje adaptivní mechanismy, jako je přepínání kodeků nebo úprava přenosové rychlosti. RTCP také nese položky popisu zdroje (SDES), včetně kanonického jména (CNAME) pro identifikaci účastníka, což je klíčové pro synchronizaci více mediálních proudů (např. audio a video ze stejného zdroje) napříč různými RTP relacemi. Dále může RTCP přenášet pakety BYE pro ukončení relace a aplikačně definované pakety pro rozšířené řízení. Protokol je navržen jako škálovatelný dynamickým přizpůsobováním intervalu hlášení na základě počtu účastníků relace, aby řídicí provoz nezahlcoval síť; typicky je provoz RTCP omezen na 5 % celkové šířky pásma relace. V architekturách 3GPP, zejména pro služby založené na IMS jako VoLTE, používají RTCP hlášení zařízení UE a síťové prvky pro vyhodnocení kvality přenosového kanálu a mohou spouštět úpravy na rádiové vrstvě nebo požadavky na režim kodeku. Protokol je definován [IETF](/mobilnisite/slovnik/ietf/) v [RFC](/mobilnisite/slovnik/rfc/) 3550 a 3GPP specifikuje jeho použití, včetně povinné podpory určitých typů hlášení a rozšíření Secure RTCP ([SRTCP](/mobilnisite/slovnik/srtcp/)) pro důvěrnost a ověřování zpráv v mediální rovině.

## K čemu slouží

[RTCP](/mobilnisite/slovnik/rtpcp/) byl vytvořen, aby řešil nedostatek zpětné vazby a řídicích mechanismů při přenosu dat v reálném čase pomocí [RTP](/mobilnisite/slovnik/rtp/). Čistý RTP neposkytuje žádný vlastní způsob, jak by odesílatelé věděli, zda příjemci proud přijímají, nebo jak by příjemci mohli hlásit síťové podmínky, jako je ztráta a zpoždění. To ztěžovalo implementaci adaptivního streamování, diagnostiku problémů nebo správu relací s více účastníky. RTCP tyto problémy řeší poskytnutím standardizovaného řídicího kanálu s nízkou režií. Jeho hlavními úkoly jsou monitorování QoS, umožňující koncovým bodům přizpůsobit se síťovým podmínkám; synchronizace médií pomocí identifikátoru CNAME; a základní správa relace. V kontextu 3GPP bylo přijetí RTCP motivováno potřebou provozovat telefony přes IP (VoIP) na úrovni operátora, kde je monitorování kvality hovoru klíčové pro zajištění služeb a uživatelský zážitek. Poskytuje technické prostředky pro síť a zařízení k implementaci funkcí hlášení kvality vyžadovaných regulačními nebo smluvními požadavky.

## Klíčové vlastnosti

- Přenáší hlášení odesílatele (SR) a příjemce (RR) s metrikami QoS, jako je ztráta paketů a zpoždění (jitter)
- Nese kanonický identifikátor (CNAME) pro synchronizaci napříč mediálními proudy
- Používá škálovatelný algoritmus pro řízení provozu hlášení (typicky omezen na 5 % šířky pásma relace)
- Podporuje rozšířená hlášení (RTCP XR) pro podrobné metriky VoIP, jako je ztráta v dávkách
- Definuje pakety BYE pro řádné opuštění relace účastníkem
- Může být zabezpečen pomocí SRTCP pro ověřování a šifrování dle bezpečnostních profilů 3GPP

## Související pojmy

- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TR 25.993** (Rel-19) — UTRA RAB Examples and Radio Interface Mapping
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.235** (Rel-12) — Default Codecs for 3GPP IP Multimedia Subsystem
- **TS 26.281** (Rel-19) — MCVideo Codecs and Media Handling
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [RTCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtcp/)
