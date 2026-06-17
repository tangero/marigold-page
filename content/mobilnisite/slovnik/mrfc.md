---
slug: "mrfc"
url: "/mobilnisite/slovnik/mrfc/"
type: "slovnik"
title: "MRFC – Multimedia Resource Function Controller"
date: 2026-01-01
abbr: "MRFC"
fullName: "Multimedia Resource Function Controller"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mrfc/"
summary: "MRFC je základní prvek sítě v IMS, který řídí MRFP pro zpracování a správu multimediálních prostředků, jako je konferencování, hlášení a transkódování. Funguje jako signalizační mozek, který interpret"
---

MRFC je prvek jádra sítě IMS, který řídí MRFP za účelem zpracování multimediálních prostředků interpretací příkazů SIP pro orchestraci funkcí mediální roviny, jako je konferencování a transkódování.

## Popis

Multimedia Resource Function Controller (MRFC) je klíčová signalizační komponenta v architektuře IP Multimedia Subsystem (IMS). Funguje jako řídicí entita pro Multimedia Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)), se kterou komunikuje pomocí protokolu H.248 (Megaco) nebo jeho profilu 3GPP, rozhraní Mp. MRFC interpretuje servisní logiku a příkazy SIP (Session Initiation Protocol) přijaté od Serving-Call Session Control Function (S-CSCF) přes rozhraní Mr. Na základě těchto příkazů MRFC instruuje MRFP k alokaci, konfiguraci a správě prostředků pro zpracování médií. To zahrnuje zahájení a řízení mediálních proudů, správu konferenčních můstků, přehrávání hlášení, sběr tónů ([DTMF](/mobilnisite/slovnik/dtmf/)) a provádění mediálního transkódování a převodu přenosové rychlosti.

Architektonicky je MRFC součástí Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), která je logicky rozdělena na řadič (MRFC) a procesor (MRFP). Toto oddělení následuje princip rozdělení řídicí a uživatelské roviny, což umožňuje nezávislé škálování a optimalizaci. MRFC obsahuje servisní logiku a stav pro multimediální relace, přičemž překládá požadavky služeb na vysoké úrovni (např. 'přidat účastníka do konference') na konkrétní příkazy nízké úrovně pro MRFP, které se mají provést na mediálních proudech. Spravuje životní cyklus těchto prostředků, zajišťuje jejich alokaci v případě potřeby a jejich včasné uvolnění po použití pro optimalizaci efektivity sítě.

Při provozu, když aplikační server IMS nebo S-CSCF určí potřebu zpracování médií – například při nastavování skupinového videohovoru – odešle SIP INVITE nebo jinou metodu SIP na MRFC. MRFC požadavek ověří, vybere vhodný MRFP na základě zatížení a schopností a naváže řídicí asociaci H.248. Poté odešle příkazy H.248 do MRFP, aby vytvořil kontexty, přidal terminace (logické koncové body pro mediální proudy) a specifikoval požadované funkce zpracování médií (míchání, konverze kodeků). MRFC zůstává ve signalizační cestě, monitoruje relaci a dynamicky upravuje chování MRFP v reakci na akce uživatele nebo servisní logiku, například ztlumení účastníka nebo změnu rozložení videa v konferenci.

## K čemu slouží

MRFC byl vytvořen, aby poskytl standardizovaný, škálovatelný a flexibilní řídicí mechanismus pro zpracování multimediálních prostředků v rámci paketových sítí, konkrétně IMS. Před IMS a konceptem [MRF](/mobilnisite/slovnik/mrf/) byly pokročilé telefonní služby, jako je konferencování nebo interaktivní hlasová odezva ([IVR](/mobilnisite/slovnik/ivr/)), často implementovány pomocí proprietárních, monolitických platforem těsně spojených s přepojováním okruhů. Tyto systémy bylo obtížné integrovat s IP službami a omezovaly inovace. Oddělení MRFC/[MRFP](/mobilnisite/slovnik/mrfp/) tento problém řeší definováním otevřeného, protokolového rozhraní (H.248/Mp) mezi řízením a zpracováním, což umožňuje interoperabilitu více dodavatelů a nezávislý vývoj signalizačních a mediálních zpracovatelských technologií.

Jeho vznik motivovala potřeba podpory široké škály bohatých, multimediálních služeb v reálném čase – nad rámec prostého hlasu – přes IP sítě. Služby jako videokonference, push-to-talk, multimediální hlášení a zákonné odposlechy pro multimediální relace vyžadují sofistikovanou, v síti hostovanou manipulaci s médii. MRFC poskytuje inteligentní řídicí rovinu nezbytnou pro orchestraci těchto komplexních mediálních funkcí jménem více aplikací a uživatelů, čímž abstrahuje složitost jak od servisní vrstvy (aplikační servery), tak od základního řízení relace ([CSCF](/mobilnisite/slovnik/cscf/)). To umožňuje poskytovatelům služeb rychle nasazovat nové multimediální funkce pomocí společného, sdíleného fondu prostředků řízeného MRFC.

## Klíčové vlastnosti

- Řídí prostředky MRFP pomocí standardního protokolu H.248/Megaco (rozhraní Mp)
- Interpretuje a provádí servisní logiku přijatou od S-CSCF přes rozhraní Mr (SIP)
- Spravuje životní cyklus multimediálních relací včetně konferencování, transkódování a hlášení
- Poskytuje řízení přenosu pro mediální proudy, včetně navázání a modifikace spojení
- Podporuje alokaci prostředků, monitorování a bezstavové nebo stavové zpracování podle požadavků služby
- Umožňuje interakci s dalšími entitami IMS, jako je AS a BGCF, pro poskytování komplexních služeb

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRFP – Multimedia Resource Function Processor](/mobilnisite/slovnik/mrfp/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TS 24.103** (Rel-19) — Telepresence Protocol for IMS
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.247** (Rel-19) — IMS Messaging Service Protocol Details
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- … a dalších 26 specifikací

---

📖 **Anglický originál a plná specifikace:** [MRFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrfc/)
