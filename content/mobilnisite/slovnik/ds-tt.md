---
slug: "ds-tt"
url: "/mobilnisite/slovnik/ds-tt/"
type: "slovnik"
title: "DS-TT – Device-side TSN Translator"
date: 2026-01-01
abbr: "DS-TT"
fullName: "Device-side TSN Translator"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ds-tt/"
summary: "Funkční entita umístěná v zařízení 5G (UE) nebo v zařízení na straně zákazníka (CPE), která překládá mezi protokoly systému 5G a protokoly IEEE Time-Sensitive Networking (TSN). Umožňuje systému 5G fun"
---

DS-TT je funkční entita v zařízení 5G, která překládá mezi protokoly systému 5G a protokoly IEEE Time-Sensitive Networking za účelem integrace průmyslových zařízení do deterministických sítí TSN.

## Popis

Device-side TSN Translator (DS-TT) je klíčová komponenta v architektuře 3GPP pro integraci systému 5G s [IEEE](/mobilnisite/slovnik/ieee/) 802.1 Time-Sensitive Networking (TSN). Jedná se o logickou funkci, která sídlí ve vnitřku uživatelského zařízení (UE) nebo v zařízení na straně zákazníka ([CPE](/mobilnisite/slovnik/cpe/)), které obsahuje 5G modem. Primární úlohou DS-TT je provádět překlad a adaptaci protokolů mezi protokoly uživatelské roviny systému 5G a protokoly IEEE TSN používanými v připojené průmyslové nebo podnikové síti. Funguje jako jeden konec virtuálního TSN mostu, kde systém 5G (skládající se z UE, [5G-AN](/mobilnisite/slovnik/5g-an/) a [UPF](/mobilnisite/slovnik/upf/)) tvoří páteř tohoto virtuálního mostu.

Architektonicky DS-TT komunikuje se dvěma doménami. Na své „síťové straně“ (rozhraní N) se připojuje k funkci uživatelské roviny 5G (UPF) přes PDU sezení za použití standardních protokolů uživatelské roviny 5G (např. [GTP-U](/mobilnisite/slovnik/gtp-u/) přes UDP/IP). Na své „straně zařízení“ (rozhraní D) se připojuje k jedné nebo více TSN koncovým stanicím nebo TSN síti za použití standardních rámců IEEE 802.1 TSN Ethernet. Klíčová operace DS-TT spočívá v překladu mezi těmito dvěma světy. To zahrnuje mapování mezi toky QoS 5G (identifikovanými QFI) a TSN datovými toky (identifikovanými VLAN ID a prioritou), provádění časového značkování pro přesnou časovou synchronizaci (např. využitím služby časové synchronizace systému 5G pro IEEE 802.1AS) a případně zpracování přerušení rámců a tvarování provozu dle standardů TSN. Účastní se také řídicí roviny TSN, přeposílá nebo ukončuje konfigurační protokoly TSN jako IEEE 802.1Qcc (Stream Reservation Protocol) ve spolupráci s Network-side TSN Translator (NW-TT) a systémem 5G.

DS-TT pracuje v tandemu se svým protějškem, NW-TT, který se nachází na straně UPF. Společně vytvářejí iluzi jediného, distribuovaného TSN mostu pro externí TSN síť. Řídicí rovina 5G, konkrétně [PCF](/mobilnisite/slovnik/pcf/) a [SMF](/mobilnisite/slovnik/smf/), konfiguruje DS-TT (a NW-TT) přes [NEF](/mobilnisite/slovnik/nef/) nebo přímo, poskytuje jí potřebná mapovací pravidla, časové informace a parametry QoS odvozené z požadavků TSN Application Function. To umožňuje průmyslovým aplikacím vyžadujícím deterministické zpoždění, ultra-spolehlivost a přesnou synchronizaci (jako je řízení pohybu nebo robotická montáž) bezproblémově fungovat přes síť 5G, jako by byly připojeny přes drátový TSN most.

## K čemu slouží

DS-TT byl vytvořen k řešení zásadní výzvy integrace bezdrátové konektivity 5G do drátových, deterministických průmyslových ethernetových sítí založených na standardech IEEE TSN. Před jeho zavedením průmyslová automatizace téměř výhradně spoléhala na drátová připojení (např. PROFINET, EtherCAT), aby zaručila omezené zpoždění a chvění. Bezdrátová řešení postrádala deterministické záruky vyžadované pro kritické řídicí smyčky. Účelem DS-TT je umožnit, aby se 5G stalo transparentní součástí TSN sítě, což dovolí mobilním robotům, AGV a bezdrátovým senzorům účastnit se časově kritických řídicích systémů bez kompromisů v deterministickém výkonu celé sítě.

Jeho vznik motivovaly trendy Průmyslu 4.0 požadující zvýšenou flexibilitu, mobilitu a bezdrátovou konektivitu v továrnách. Omezení předchozích přístupů byla zřejmá: standardní bezdrátové LAN nebo mobilní datová připojení nemohla poskytnout přísné smlouvy o úrovni služeb (SLA) pro zpoždění a spolehlivost, ani nemohla nativně rozumět řídicím protokolům TSN pro rezervaci zdrojů. DS-TT jako součást rámce integrace TSN do systému 5G definovaného ve 3GPP Release 16 a novějších to řeší tím, že systém 5G se jeví jako standardní komponenta TSN mostu. To umožňuje existujícím systémům správy TSN sítí a koncovým stanicím fungovat beze změn, což dramaticky snižuje bariéru pro adopci 5G v průmyslovém prostředí.

## Klíčové vlastnosti

- Překlad protokolů mezi uživatelskou rovinou 5G (GTP-U/IP) a rámci IEEE TSN Ethernet
- Časové značkování pro přesnou časovou synchronizaci (podpora IEEE 802.1AS)
- Mapování mezi toky QoS 5G (QFI) a TSN datovými toky (VLAN/PCP)
- Ukončení nebo přeposílání řídicích protokolů TSN (např. 802.1Qcc)
- Podpora funkcí tvarování a plánování provozu TSN
- Společné umístění v rámci UE nebo CPE, práce ve dvojici s NW-TT na straně UPF

## Definující specifikace

- **TR 22.878** (Rel-18) — Technical Report on 5G Timing Resiliency
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.519** (Rel-17) — TSN AF to DS-TT/NW-TT Protocol Aspects
- **TS 24.535** (Rel-19) — TS 24535: (g)PTP Message Delivery Protocol
- **TS 24.539** (Rel-19) — NW-TT Protocol Aspects
- **TR 28.839** (Rel-18) — Technical Report
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications
- **TS 29.565** (Rel-19) — Time Synchronization Function Services
- **TS 32.282** (Rel-18) — Charging management; Time Sensitive Networking
- **TR 33.851** (Rel-17) — Security for Industrial IoT in 5G

---

📖 **Anglický originál a plná specifikace:** [DS-TT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ds-tt/)
