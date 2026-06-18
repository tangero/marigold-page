---
slug: "ssrc"
url: "/mobilnisite/slovnik/ssrc/"
type: "slovnik"
title: "SSRC – Synchronization Source Identifier"
date: 2026-01-01
abbr: "SSRC"
fullName: "Synchronization Source Identifier"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ssrc/"
summary: "Jedinečný identifikátor zdroje mediálního proudu v rámci relací protokolu pro přenos v reálném čase (RTP). Rozlišuje mezi více souběžnými mediálními zdroji (např. různí mluvčí v konferenčním hovoru),"
---

SSRC je jedinečný identifikátor zdroje mediálního proudu v rámci RTP relace, který rozlišuje souběžné zdroje pro správnou synchronizaci a přehrávání v IMS a VoLTE/VoNR.

## Popis

Synchronization Source Identifier (SSRC) je 32bitový číselný identifikátor definovaný v protokolu pro přenos v reálném čase ([RTP](/mobilnisite/slovnik/rtp/)), který se používá pro přenos zvuku a videa přes IP sítě. V RTP relaci je každému účastníkovi, který generuje proud RTP paketů (např. mikrofonu, kameře nebo mediálnímu mixéru), přidělen jedinečný SSRC. Tento identifikátor je přenášen v hlavičce každého RTP paketu, což příjemcům umožňuje přiřadit příchozí pakety konkrétnímu zdroji. Hlavní úlohou SSRC je poskytnout rozlišení na úrovni zdroje pro synchronizaci a demultiplexování. Řídicí protokol RTP ([RTCP](/mobilnisite/slovnik/rtcp/)) používá SSRC k asociaci řídicích paketů (obsahujících zprávy o kvalitě, členství účastníků a popis zdroje) s příslušným mediálním zdrojem, což umožňuje funkce jako identifikace účastníka nebo monitorování sítě.

Z architektonického hlediska je SSRC klíčovou součástí mediální roviny služeb založených na IP multimediální podsystému (IMS), jako je Voice over LTE (VoLTE) a Voice over NR (VoNR). Při sestavení hovoru si fáze signalizace [SIP](/mobilnisite/slovnik/sip/) prostřednictvím protokolu pro popis relace ([SDP](/mobilnisite/slovnik/sdp/)) dohodne mediální formáty a porty, ale konkrétní hodnoty SSRC jsou dynamicky zvoleny každým odesílatelem média při zahájení RTP proudu. Mechanismus zajištění jedinečnosti je pravděpodobnostní; každý zdroj náhodně vybere 32bitové číslo, přičemž pravděpodobnost kolize v rámci relace je velmi nízká. Pokud je kolize detekována (dva zdroje si zvolí stejný SSRC), je spuštěn postup řešení konfliktů definovaný v [RFC](/mobilnisite/slovnik/rfc/) 3550, při kterém jeden ze zdrojů může změnit svůj SSRC. Použití v kontextu 3GPP upravují související specifikace jako 3GPP TS 24.229 (IMS) a TS 26.114 (IMS Media).

Jeho fungování je nedílnou součástí scénářů s více stranami. V konferenčním hovoru zařízení každého účastníka funguje jako synchronizační zdroj se svým vlastním SSRC. Funkce mediálních prostředků ([MRF](/mobilnisite/slovnik/mrf/)) nebo konferenční můstek, který mixuje audio proudy, se také může stát synchronizačním zdrojem a generovat nový složený proud s novým SSRC. Příjemci používají SSRC ke správnému vykreslování zvuku od různých mluvčích, aplikaci individuálního nastavení hlasitosti nebo výpočtu samostatných statistik zpoždění a ztráty paketů pro každý zdroj prostřednictvím [RTCP](/mobilnisite/slovnik/rtpcp/) Receiver Reports. Tato identifikace na úrovni zdroje je klíčová pro sledování kvality uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)) a pro pokročilé služby jako indikace aktivního mluvčího. SSRC se také používá v bezpečnostních kontextech; například v Secure RTP (SRTP) jsou kryptografické kontexty často vázány na hodnoty SSRC, aby poskytly autentizaci zdroje a důvěrnost.

## K čemu slouží

SSRC existuje proto, aby řešil základní problém identifikace a správy více souběžných mediálních zdrojů v rámci jedné RTP relace. Před standardizací RTP multimediální relace přes IP postrádaly standardizovaný způsob rozlišení různých přispěvatelů v relaci, což ztěžovalo interoperabilní implementaci funkcí jako audio konference, přepínání videa nebo nezávislé hodnocení kvality jednotlivých proudů. Zavedení SSRC jako součásti RTP (standardizováno v IETF RFC 1889, později RFC 3550) poskytlo jednoduchý, v pásmový mechanismus pro identifikaci zdroje bez nutnosti neustálé signalizace mimo pásmo.

V ekosystému 3GPP bylo přijetí RTP/RTCP, a tedy i SSRC, motivováno přechodem na plně IP sítě pro hlasové a multimediální služby s IMS. U hlasu v přepojování okruhů bylo rozpoznání mluvčích řešeno jinými, méně flexibilními mechanismy. U hlasu přes paketovou síť VoLTE a VoNR SSRC umožňuje síti poskytovat pokročilé komunikační služby (RCS), konferenční hovory a videotelefonii pomocí standardních internetových protokolů. Řeší omezení pouhé identifikace proudu pomocí IP adres a portů, což je nedostatečné, když jeden hostitel (jako konferenční server) generuje více logických proudů nebo když je použita překlad síťových adres (NAT).

Historicky, když 3GPP definovalo IMS ve verzi Rel-5 a později jej integrovalo pro hlas v LTE a 5G, stal se SSRC základním kamenem pro zpracování médií. Jeho účel sahá až k umožnění podrobné mediální analýzy a zákonného odposlechu, jak je specifikováno v 3GPP TS 33.179 a 33.180, kde je klíčové korelovat mediální proudy s konkrétními stranami. SSRC řeší problém škálovatelné, dynamické správy zdrojů v skupinové komunikaci v reálném čase, což je kritický požadavek pro moderní telekomunikační služby přesahující jednoduché bod-bod hovory.

## Klíčové vlastnosti

- 32bitový jedinečný identifikátor přenášený v hlavičce každého RTP paketu
- Dynamicky a náhodně přiřazen každým mediálním zdrojem při zahájení proudu
- Používán jako klíč pro asociaci řídicích paketů RTCP (např. SR, RR, SDES) s mediálními zdroji
- Umožňuje demultiplexování více proudů v rámci jedné RTP relace
- Podporuje procedury detekce a řešení kolizí pro zajištění jedinečnosti
- Základní prvek pro mixování médií, podávání hlášení o kvalitě na zdroj a pro kontexty Secure RTP (SRTP)

## Související pojmy

- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.879** (Rel-13) — MCPTT Security Study
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TS 36.579** — 3GPP TR 36.579
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [SSRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssrc/)
