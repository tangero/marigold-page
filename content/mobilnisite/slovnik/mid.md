---
slug: "mid"
url: "/mobilnisite/slovnik/mid/"
type: "slovnik"
title: "MID – Media Identification"
date: 2025-01-01
abbr: "MID"
fullName: "Media Identification"
category: "Services"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mid/"
summary: "Mechanismus pro identifikaci a popis mediálních komponent (např. audio- či videoproudů) v rámci multimediální relace, jako je IMS hovor nebo služba zasílání zpráv. Umožňuje řízení relace a vyjednávání"
---

MID je mechanismus pro identifikaci a popis mediálních komponent, jako jsou audio- nebo videoproudy, v rámci multimediální relace, který umožňuje řízení relace a vyjednávání médií mezi koncovými body.

## Popis

Media Identification (MID, identifikace médií) je rámec používaný v rámci 3GPP k jednoznačné identifikaci a popisu jednotlivých mediálních komponent v multimediální relaci zřízené pomocí protokolů jako Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)). Je klíčovou součástí vyjednávání médií a řízení relace, zejména ve službách IP Multimedia Subsystem (IMS). Multimediální relace, například videohovor nebo konferenční služba s více proudy, se skládá z více mediálních proudů (např. primární audio, sekundární video pro sdílení obsahu, text). Každé z těchto logických mediálních komponent je při výměně SDP nabídky/odpovědi přiřazen jedinečný atribut MID. Atribut MID, definovaný v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 5888, je zahrnut v řádku 'm=' (media) popisu SDP. Umožňuje koncovým bodům a síťovým uzlům (jako je Media Resource Function Controller, [MRFC](/mobilnisite/slovnik/mrfc/)) korelovat mediální řádky napříč SDP nabídkami a odpověďmi a odkazovat se na konkrétní mediální proudy pro manipulaci. Například při modifikaci relace může koncový bod použít hodnotu MID k označení, který konkrétní mediální proud si přeje pozastavit, změnit pro něj kodek nebo jej zcela odebrat. Tento přístup je robustnější než použití pořadí mediálních řádků, které se může změnit. V rámci 3GPP se MID používá ve spojení s dalšími mechanismy SDP a SIP pro funkce jako Early Media, Interactive Connectivity Establishment ([ICE](/mobilnisite/slovnik/ice/)) pro průchod [NAT](/mobilnisite/slovnik/nat/) a autorizaci médií. Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Application Function (AF) mohou také použít identifikaci médií k uplatnění konkrétních zásad Quality of Service (QoS) a účtování na jednotlivé mediální toky v rámci relace, což umožňuje sofistikovanou diferenciaci služeb.

## K čemu slouží

MID byl zaveden, aby vyřešil omezení správy složitých multimediálních relací, ve kterých je zapojeno více simultánních mediálních proudů. Rané multimediální relace typicky popisovaly média na základě pořadí řádků 'm=' v SDP, což bylo křehké – pokud se pořadí během vyjednávání změnilo, mohlo to vést k nesprávnému přiřazení proudů a selhání relací. Potřeba stabilního, jedinečného identifikátoru se stala naléhavou s příchodem pokročilých IMS služeb, jako je Video Telephony, Collaborative Workspaces a Rich Communication Services (RCS), kde mohou relace dynamicky přidávat nebo odebírat mediální komponenty (např. přidání přenosu souboru nebo druhého videoproudu). MID poskytuje explicitní, na úrovni protokolu umístěnou referenci pro každou mediální komponentu, což umožňuje robustní modifikaci relace, operace pozastavení/obnovení a adaptaci obsahu. Umožňuje síťovým prvkům přesně identifikovat, na který mediální tok se má vztahovat pravidlo zásad, což je zásadní pro implementaci pokročilých modelů účtování (např. samostatné účtování videa a hlasu) a zaručené QoS s přidělenou přenosovou rychlostí. Jeho vznik byl hnán prací IETF na SDP a byl přijat 3GPP, aby zajistil interoperabilitu a spolehlivé řízení služeb v all-IP servisní architektuře IMS.

## Klíčové vlastnosti

- Poskytuje jedinečný textový identifikátor pro každý mediální popis SDP (řádek 'm=')
- Definován v IETF RFC 5888 a přijat 3GPP
- Umožňuje stabilní odkazování na mediální proudy během výměn SDP nabídky/odpovědi
- Umožňuje nezávislou manipulaci (pozastavení, změnu, odebrání) s jednotlivými mediálními komponentami
- Používán síťovými funkcemi zásad (PCRF, AF) pro detailní řízení zásad s ohledem na média
- Nezbytný pro složité IMS služby, jako jsou videohovory a multimediální konference

## Související pojmy

- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security

---

📖 **Anglický originál a plná specifikace:** [MID na 3GPP Explorer](https://3gpp-explorer.com/glossary/mid/)
