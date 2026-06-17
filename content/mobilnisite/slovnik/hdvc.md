---
slug: "hdvc"
url: "/mobilnisite/slovnik/hdvc/"
type: "slovnik"
title: "HDVC – High Definition Video Conference"
date: 2025-01-01
abbr: "HDVC"
fullName: "High Definition Video Conference"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hdvc/"
summary: "HDVC je služba 3GPP umožňující videokonference s vysokým rozlišením přes mobilní sítě. Specifikuje požadavky na obousměrnou komunikaci s HD videem a zvukem v reálném čase s nízkou latencí a vysokou sp"
---

HDVC je služba 3GPP, která umožňuje obousměrnou videokonferenci s vysokým rozlišením a zvukem v reálném čase přes mobilní sítě s nízkou latencí a vysokou spolehlivostí.

## Popis

High Definition Video Conference (HDVC) v 3GPP označuje standardizovanou službu pro provádění interaktivních videokonferencí v reálném čase s kvalitou videa ve vysokém rozlišení (typicky 720p nebo 1080p) přes IP mobilní sítě. Služba funguje v rámci architektury IP Multimedia Subsystem (IMS) a využívá protokol Session Initiation Protocol (SIP) pro zřizování, modifikaci a ukončení relace. Během hovoru jsou video a audio mediální toky kódovány pomocí účinných kodeků, jako je H.264/[AVC](/mobilnisite/slovnik/avc/) pro video a [AMR-WB](/mobilnisite/slovnik/amr-wb/) nebo [EVS](/mobilnisite/slovnik/evs/) pro audio, a následně paketizovány pro přenos přes Real-time Transport Protocol (RTP). Mezi klíčové architektonické komponenty patří UE (vybavené [HD](/mobilnisite/slovnik/hd/) kamerami a displeji), IMS core ([CSCF](/mobilnisite/slovnik/cscf/) uzly pro řízení) a Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), která může poskytovat služby specifické pro konferenční hovory, jako je mixování více audio/video toků pro hovory více účastníků. Packet Data Network (PDN) zajišťuje IP konektivitu, přičemž Evolved Packet Core (EPC) nebo 5G Core (5GC) zaručují odpovídající QoS prostřednictvím vyhrazených nosičů označených Quality Class Identifiers (QCIs) nebo 5G QoS Identifiers (5QIs) pro garantovanou přenosovou rychlost a prioritu. Úlohou HDVC v síti je poskytnout interoperabilní, operátorské konferenční řešení, které se hladce integruje s dalšími IMS službami (jako je VoLTE) a může využívat síťové funkce jako řízení politik, účtování a podporu tísňových služeb. Technické specifikace jako TS 26.923 podrobně popisují požadavky na zpracování médií a kodeky, aby bylo zajištěno konzistentní vysoce kvalitní uživatelské prostředí napříč zařízeními různých výrobců a síťovými podmínkami.

## K čemu slouží

HDVC byla standardizována, aby uspokojila rostoucí poptávku po vysoce kvalitních profesionálních mobilních videokonferencích, což byla potřeba nedostatečně naplňovaná staršími okruhově přepínanými videohovory nebo best-effort internetovými řešeními. Předchozí přístupy trpěly nízkým rozlišením videa, špatnou kvalitou zvuku, nedostatkem interoperability a neschopností garantovat kvalitu služby v celulárních sítích. Rozšíření podnikových chytrých telefonů a tabletů spolu s nasazením vysokorychlostních LTE sítí vytvořilo příležitost pro operátory nabízet prémiové, zpoplatnitelné konferenční služby. 3GPP HDVC řeší tato omezení definicí služby, která využívá řídicí rovinu IMS pro robustní správu relací a rámec politik pro garantovaný QoS, čímž zajišťuje nízkou latenci a vysokou šířku pásma nezbytnou pro přirozenou interakci v [HD](/mobilnisite/slovnik/hd/) kvalitě v reálném čase. Její vznik byl motivován potřebami podniků a vertikálních trhů po spolehlivých nástrojích pro mobilní spolupráci, teleprezenci a aplikacích jako je vzdálená expertní podpora nebo telemedicína, kde je vizuální jasnost a spolehlivost spojení prvořadá. Standardizace také předchází závislosti na konkrétním dodavateli a podporuje konkurenční ekosystém zařízení a síťového vybavení.

## Klíčové vlastnosti

- Podpora vysokého rozlišení videa (např. 1280x720, 1920x1080) v reálném čase
- Integrace s IMS core pro řízení relací, autentizaci a interoperabilitu s dalšími službami
- Využití účinných, povinně podporovaných video (H.264) a audio (AMR-WB, EVS) kodeků
- Mechanismy QoS prostřednictvím vyhrazených nosičů s odpovídajícími hodnotami QCI/5QI pro konverzační video
- Podpora konferenčních hovorů více účastníků prostřednictvím schopností Media Resource Function (MRF)
- Specifikované postupy zpracování médií pro adaptaci na síťové podmínky a možnosti zařízení

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling

---

📖 **Anglický originál a plná specifikace:** [HDVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/hdvc/)
