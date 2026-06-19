---
slug: "upf"
url: "/mobilnisite/slovnik/upf/"
type: "slovnik"
title: "UPF – User Plane Function"
date: 2026-01-01
abbr: "UPF"
fullName: "User Plane Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/upf/"
summary: "Základní funkce jádra sítě v systému 5G (5GS) zodpovědná za směrování a přeposílání paketů, kontrolu paketů, správu kvality služby (QoS) a hlášení o využití přenosu. Je centrálním kotvícím bodem pro u"
infografika: "/assets/slovnik/upf.svg"
infografikaAlt: "Schéma architektury 5G sítě se zvýrazněním UPF"
---

UPF je základní funkce jádra sítě v systému 5G zodpovědná za směrování a přeposílání paketů, jejich kontrolu, správu kvality služby (QoS) a hlášení o využití, sloužící jako centrální kotvící bod pro přenos dat uživatele.

## Popis

User Plane Function (UPF) je základní síťová funkce v rámci 5G jádra (5GC) postavená na architektuře orientované na služby ([SBA](/mobilnisite/slovnik/sba/)). Je zodpovědná za všechny úlohy spojené se zpracováním a přeposíláním paketů uživatelských dat. UPF funguje jako propojovací bod mezi rádiovou přístupovou sítí (RAN) – ať už NG-RAN nebo ne-3GPP přístupem – a externími datovými sítěmi ([DN](/mobilnisite/slovnik/dn/)), jako je internet nebo služby operátora. Její architektura je navržena jako vysoce flexibilní a distribuovatelná, což umožňuje nasazení více instancí UPF v různých částech sítě (např. centrální, regionální, edge lokality) pro splnění různých požadavků na latenci a šířku pásma.

Fungování UPF řídí pravidla instalovaná funkcí pro správu relací ([SMF](/mobilnisite/slovnik/smf/)). SMF prostřednictvím rozhraní N4 do UPF zavádí pravidla pro detekci paketů ([PDR](/mobilnisite/slovnik/pdr/)), pravidla pro přeposílání ([FAR](/mobilnisite/slovnik/far/)), pravidla pro vynucování kvality služby ([QER](/mobilnisite/slovnik/qer/)) a pravidla pro hlášení o využití ([URR](/mobilnisite/slovnik/urr/)). Po přijetí paketu jej UPF zkontroluje (porovná s PDR) a provede přidružené akce. Tyto akce mohou zahrnovat přeposlání paketu do konkrétního tunelu nebo rozhraní (FAR), aplikaci QoS značek a omezení rychlosti (QER), měření objemu přenosu pro účtování (URR) nebo dokonce duplikaci paketů pro analytiku nebo redundanci. Jedna relace UE může zahrnovat více UPF, například větvící UPF pro připojení s více cestami (multi-homed) nebo mezilehlou UPF pro lokalizované průniky do sítě.

Klíčové součásti role UPF zahrnují funkci kotvícího bodu pro mobilitu – jak uvnitř systému, tak mezi 3GPP a ne-3GPP přístupy. Poskytuje externí rozhraní [PDU](/mobilnisite/slovnik/pdu/) relace, což z ní činí oficiální 'výstupní bod' sítě 5G. Dále je UPF klíčovým prvkem umožňujícím několik pokročilých schopností 5G. Pro síťové dělení (Network Slicing) mohou být různé instance UPF vyhrazeny konkrétním řezům a poskytovat tak izolované datové cesty. Pro edge computing může být UPF nasazena na okraji sítě, aby lokálně směrovala přenos na blízké aplikační servery, což drasticky snižuje latenci. Provádí také hlubokou kontrolu paketů (DPI) pro směrování na základě aplikace a podporuje funkce jako agregace přenosu nebo IPv6 multi-homing.

## K čemu slouží

UPF byla vytvořena jako součást nové koncepce jádra sítě 5G (clean-slate design) k řešení omezení uživatelské roviny 4G EPC, konkrétně rozdělené architektury SGW/PGW. Motivací bylo dosažení větší flexibility, škálovatelnosti a podpory nových servisních paradigmat. Mezi klíčové problémy, které řeší, patří: umožnění služeb s ultra nízkou latencí díky decentralizovanému nasazení na okraji sítě; poskytnutí architektonického základu pro end-to-end síťové dělení díky nabídnutí izolovatelné komponenty datové roviny; a podpora širšího spektra přístupových technologií (5G NR, LTE, Wi-Fi, pevný přístup) s jednotným kotvícím bodem.

Historicky byly brány 4G EPC (SGW, PGW) monolitické entity s těsně propojenou řídicí a uživatelskou rovinou, což ztěžovalo jejich nezávislé škálování a flexibilní nasazení. Koncepční principy 5G – cloudová nativnost, SBA a oddělení řídicí a uživatelské roviny (CUPS) – přímo vedly ke vzniku UPF. UPF je čistý, škálovatelný prvek uživatelské roviny, který může být na vyžádání vytvořen kdekoli v síťovém cloudu. Tím se řeší potřeba dynamické, softwarově řízené architektury schopné podporovat rozmanité případy užití 5G, od rozšířeného mobilního širokopásmového přístupu (eMBB) přes masivní IoT (mIoT) až po kritické komunikace, z nichž každý má odlišné požadavky na šířku pásma, latenci a spolehlivost.

## Klíčové vlastnosti

- Směrování a přeposílání paketů a GTP-U/encapsulation tunelování
- Detekce přenosu a vynucování pravidel prostřednictvím pravidel od SMF (PDR/FAR/QER/URR)
- Kotvící bod pro mobilitu a kontinuitu relace
- Podpora lokalizovaného průniku do sítě a edge computingu (UL CL, IPv6 multi-homing)
- Integrální součást pro izolaci na úrovni jednotlivých řezů při síťovém dělení (Network Slicing)
- Hluboká kontrola paketů (DPI) a směrování přenosu na základě aplikace

## Související pojmy

- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 26.113** (Rel-19) — 5G Real-Time Media Communication Procedures & APIs
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- … a dalších 51 specifikací

---

📖 **Anglický originál a plná specifikace:** [UPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/upf/)
