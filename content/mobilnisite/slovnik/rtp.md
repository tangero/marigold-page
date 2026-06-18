---
slug: "rtp"
url: "/mobilnisite/slovnik/rtp/"
type: "slovnik"
title: "RTP – Real-time Transport Protocol"
date: 2025-01-01
abbr: "RTP"
fullName: "Real-time Transport Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rtp/"
summary: "RTP je standardizovaný formát paketu pro přenos zvuku a videa po IP sítích. Poskytuje koncové síťové transportní funkce vhodné pro aplikace přenášející data v reálném čase, jako je interaktivní zvuk a"
---

RTP je standardizovaný formát paketu pro přenos zvuku a videa po IP sítích, který poskytuje koncové transportní funkce pro data v reálném čase, jako je VoLTE, VoNR a multimediální streamování v sítích 3GPP.

## Popis

Real-time Transport Protocol (RTP) je protokol definovaný [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 3550), který je široce přijímán a profilován v rámci standardů 3GPP pro přenos multimediálního provozu v reálném čase. Není to protokol vynalezený 3GPP, ale klíčový stavební blok používaný ve službách Packet-Switched Streaming ([PSS](/mobilnisite/slovnik/pss/)), Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a službách založených na IP Multimedia Subsystem (IMS), jako je Voice over LTE (VoLTE) a Video over LTE (ViLTE). RTP typicky běží nad [UDP](/mobilnisite/slovnik/udp/), aby zajistil včasné doručování po IP sítích. Jeho hlavní funkcí je poskytovat identifikaci typu přenášených dat, číslování sekvence, časové značky a monitorování doručování.

Paket RTP se skládá z hlavičky a přenášených dat. Hlavička obsahuje kritická pole: číslo sekvence pro detekci ztráty paketů a jejich přeřazení, časovou značku pro umožnění správného časování přehrávání a synchronizaci mezi mediálními proudy (např. zvuk a video), identifikátor synchronizačního zdroje ([SSRC](/mobilnisite/slovnik/ssrc/)) pro rozlišení více zdrojů v relaci a pole typu přenášených dat pro identifikaci formátu kodeku (např. [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/), H.264, VP8). Přenášená data obsahují komprimovaná mediální data vygenerovaná kodekem. Samotný RTP negarantuje QoS ani včasné doručování; spoléhá se na to s protokoly nižších vrstev a síťovými mechanismy QoS (jako jsou QoS Class Identifiers v 5G). Jeho doprovodný protokol, RTP Control Protocol (RTCP), poskytuje statistické a řídicí informace pro relaci mimo přenosový kanál.

V rámci architektury 3GPP jsou relace RTP navazovány a spravovány jádrem IMS, konkrétně funkcemi Call Session Control Functions (CSCFs). Během nastavování hovoru VoLTE například Session Description Protocol (SDP) uvnitř signalizace SIP vyjednává parametry RTP – IP adresy, porty a kodeky. Mediální cesta pro proud RTP pak proudí přímo mezi UEs (nebo přes mediální brány/kotvy jako IMS Media Resource Function) přes datový bearer LTE nebo 5G, který je nakonfigurován s odpovídající QoS pro upřednostnění provozu v reálném čase. Vrstva Packet Data Convergence Protocol (PDCP) v rádiovém zásobníku zajišťuje bezpečné a efektivní doručování těchto IP paketů.

Úlohou RTP je poskytnout standardizovanou, interoperabilní obálku pro média v reálném čase, což umožňuje zařízením od různých výrobců vzájemnou výměnu hlasu a videa. Jeho mechanismus časových značek je zásadní pro správu vyrovnávacích pamětí kolísání zpoždění na straně přijímače, které vyhlazují variace síťového zpoždění. Číslo sekvence umožňuje přijímači detekovat ztracené pakety, které mohou být maskovány pomocí algoritmů pro skrytí chyb nebo nahlášeny pro případné opakované přenosy (při použití RTP s redundancí). Ve vyvinutých systémech se RTP používá spolu s RTP Control Protocol (RTCP) pro zpětnou vazbu a může být zabezpečeno pomocí Secure Real-time Transport Protocol (SRTP), jak je specifikováno v 3GPP pro zabezpečení mediální roviny.

## K čemu slouží

RTP existuje, aby vyřešilo základní problém přenosu časově citlivých zvukových a video dat po best-effort IP sítích, které byly původně navrženy pro nespolehlivý přenos dat mimo reálný čas. Před rozšířeným přijetím RTP a VoIP se komunikace v reálném čase spoléhala na sítě s přepojováním okruhů (jako tradiční telefonní síť), které rezervovaly vyhrazené koncové cesty zaručující konstantní zpoždění a šířku pásma, ale byly neefektivní pro data. Vzestup internetu a IP sítí vytvořil potřebu paketové metody pro zpracování interaktivních médií, což vedlo k vývoji RTP.

RTP řeší omezení použití holého UDP nebo TCP pro média. UDP neposkytuje žádné informace o sekvenci nebo časování, zatímco mechanismy spolehlivosti TCP (opakované přenosy, doručování v pořadí) zavádějí pro přehrávání v reálném čase nepřijatelné a proměnlivé zpoždění. RTP zavádí právě tolik struktury – čísla sekvence a časové značky – aby umožnilo přijímačům rekonstruovat časování a detekovat ztráty, aniž by vnucovalo mechanismus spolehlivosti, který by poškodil latenci. To umožňuje adaptivní vyrovnávací paměti kolísání zpoždění a synchronizaci mezi více mediálními proudy (synchronizace obrazu a zvuku).

V kontextu 3GPP bylo přijetí RTP hnací silou přechodu na plně IP sítě, počínaje 3G a plně realizováno v 4G LTE a 5G NR. Pro služby založené na IMS, jako je VoLTE, byl standardní, široce podporovaný protokol pro přenos médií nezbytný pro interoperabilitu mezi mobilními telefony, síťovými zařízeními a pevnými VoIP systémy. 3GPP profiluje a omezuje použití RTP (a souvisejících kodeků), aby zajistilo konzistentní kvalitu služby, efektivní využití rádiových zdrojů a kompatibilitu s síťovým řízením politik, účtováním a zabezpečením (prostřednictvím SRTP). Je to klíčový prvek, který umožňuje mobilním sítím přejít od hlasu s přepojováním okruhů ke kvalitní, funkčně bohaté multimediální komunikaci založené na IP.

## Klíčové vlastnosti

- Identifikace typu přenášených dat pro dynamické vyjednávání kodeků
- Číslování sekvence pro detekci ztráty paketů a jejich přeřazení
- Časové značky pro synchronizaci a správu vyrovnávací paměti kolísání zpoždění
- Identifikátory synchronizačního zdroje (SSRC) pro relace s více zdroji
- Návrh pro práci s doprovodným protokolem RTCP pro řízení a zpětnou vazbu
- Rozšiřitelný formát hlavičky pro rozšíření specifická pro profil

## Související pojmy

- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TR 22.827** (Rel-17) — Study on Audio-Visual Service Production Stage 1
- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- … a dalších 90 specifikací

---

📖 **Anglický originál a plná specifikace:** [RTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rtp/)
