---
slug: "iptv"
url: "/mobilnisite/slovnik/iptv/"
type: "slovnik"
title: "IPTV – Internet Protocol Television"
date: 2025-01-01
abbr: "IPTV"
fullName: "Internet Protocol Television"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iptv/"
summary: "IPTV je systém pro poskytování televizních služeb přes spravovanou IP síť, například 3GPP IMS. Umožňuje vysílání televize, video na vyžádání a interaktivní služby a transformuje mobilní sítě na multim"
---

IPTV je systém pro poskytování vysílání televize, videa na vyžádání a interaktivních televizních služeb přes spravovanou IP síť, jako je 3GPP IMS, který umožňuje poskytování videa na úrovni operátora.

## Popis

Internet Protocol Television (IPTV) v kontextu 3GPP označuje standardizovaný systém pro poskytování televizních a video služeb přes spravovanou síť založenou na IP, který využívá IP Multimedia Subsystem (IMS) pro řízení a správu relací. Na rozdíl od videoobsahu přes internet (over-the-top, [OTT](/mobilnisite/slovnik/ott/)) je 3GPP IPTV spravovanou službou, kde operátor sítě řídí kvalitu služeb, zabezpečení a distribuci obsahu, čímž zajišťuje spolehlivý a kvalitní uživatelský zážitek. Architektura je definována tak, aby podporovala různé modely služeb včetně živého televizního vysílání (Broadcast/Multicast), videa na vyžádání (Video on Demand, VoD) a síťového osobního videozáznamu (network-based Personal Video Recording, nPVR).

Jádrem 3GPP IPTV je IPTV Media Function (IMDF), která zajišťuje distribuci médií, a IPTV Service Control Function (ISCF), která spravuje vyhledávání služeb, jejich výběr a řízení relací a komunikuje s jádrem IMS pro účely autentizace, autorizace a účtování. Obsah je distribuován prostřednictvím IP multicastu pro živá vysílání a unicastu pro obsah na vyžádání. Systém využívá protokoly jako Real-Time Streaming Protocol ([RTSP](/mobilnisite/slovnik/rtsp/)) pro řízení VoD a Internet Group Management Protocol ([IGMP](/mobilnisite/slovnik/igmp/)) pro správu členství ve skupinách multicastu. Klíčová rozhraní, jako je referenční bod Ut, umožňují uživateli spravovat předplatné služeb prostřednictvím webového portálu.

Z pohledu sítě se IPTV hluboce integruje s doménou paketového přenosu (Packet Switched, [PS](/mobilnisite/slovnik/ps/)) a IMS. Využívá Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) k aplikaci specifických pravidel QoS pro video provoz, čímž zajišťuje dostatečnou šířku pásma a nízkou latenci. Tento spravovaný přístup umožňuje operátorům garantovat úrovně služeb, implementovat sofistikované modely účtování (např. předplatné, platba za zhlédnutí) a nabízet bezproblémový zážitek na různých zařízeních. Specifikace podrobně popisují komplexní architekturu od konce ke konci, včetně přípravy obsahu, šifrování pro správu digitálních práv (Digital Rights Management, [DRM](/mobilnisite/slovnik/drm/)) a mechanismů distribuce, což z ní činí ucelený rámec pro televizní služby na úrovni telekomunikačního operátora.

## K čemu slouží

IPTV bylo zavedeno za účelem standardizace poskytování televizních služeb přes sítě 3GPP jako odpověď na rostoucí poptávku spotřebitelů po videu a potřebu operátorů generovat příjmy z pokročilých služeb nad rámec hlasu a základních dat. Před standardizací byla distribuce videa často proprietární nebo založená na nespravovaných modelech [OTT](/mobilnisite/slovnik/ott/), které nenabízely žádné záruky QoS, poskytovaly nekonzistentní uživatelský zážitek a měly omezenou integraci s fakturačními a řídicími systémy operátora. Cílem 3GPP IPTV bylo vytvořit interoperabilní platformu na úrovni operátora.

Vytvoření specifikací 3GPP IPTV bylo motivováno konvergencí telekomunikací a médií, což umožnilo mobilním i pevným síťovým operátorům konkurovat tradičním kabelovým a satelitním televizním poskytovatelům využitím své IP infrastruktury. Řeší problém efektivní distribuce vysokoširokopásmových video streamů v reálném čase řízeným způsobem a umožňuje funkce jako okamžitá změna kanálu, rodičovská kontrola a integrované elektronické programové průvodce ([EPG](/mobilnisite/slovnik/epg/)). Díky využití IMS poskytuje jednotnou řídicí rovinu pro multimediální služby, což zjednodušuje balíčkování služeb (např. triple-play) a umožňuje bezproblémovou mobilitu pro televizní služby.

## Klíčové vlastnosti

- Řízení služeb a autentizace založené na IMS
- Podpora živého vysílání (multicast) a videa na vyžádání (unicast)
- Integrované řízení politik a účtování (PCC) pro garantovanou QoS
- Možnosti síťového osobního videozáznamu (nPVR)
- Standardizovaná rozhraní pro distribuci obsahu a vyhledávání služeb
- Integrace správy digitálních práv (DRM) a ochrany obsahu

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [PCC – Performance-oriented Congestion Control](/mobilnisite/slovnik/pcc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3

---

📖 **Anglický originál a plná specifikace:** [IPTV na 3GPP Explorer](https://3gpp-explorer.com/glossary/iptv/)
