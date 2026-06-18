---
slug: "vpn"
url: "/mobilnisite/slovnik/vpn/"
type: "slovnik"
title: "VPN – Virtual Private Network"
date: 2026-01-01
abbr: "VPN"
fullName: "Virtual Private Network"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vpn/"
summary: "Virtuální privátní síť (VPN) v rámci 3GPP poskytuje zabezpečené privátní síťové služby přes veřejnou mobilní infrastrukturu. Umožňuje podnikům rozšířit jejich privátní sítě na mobilní uživatele a zaří"
---

VPN je služba v rámci 3GPP, která poskytuje zabezpečené a privátní síťové připojení přes veřejnou mobilní infrastrukturu pro podniky, čímž rozšiřuje jejich sítě na mobilní uživatele a zařízení IoT.

## Popis

V architektuře 3GPP se termín Virtuální privátní síť (VPN) vztahuje k servisní schopnosti, která umožňuje vytváření logicky izolovaných síťových segmentů nad sdílenou veřejnou mobilní síťovou infrastrukturou. Nejde o jeden konkrétní protokol, ale o rámec funkcí a architektur definovaných v mnoha specifikacích (např. TS 22.153, TS 23.501), které umožňují komunikaci pro podniky a vertikální segmenty. VPN v 3GPP poskytuje připojení mezi skupinou účastníků (např. zaměstnanci podniku, senzory IoT) a případně jejich podnikovou sítí, přičemž politiky vynucují, aby komunikace zůstala uvnitř skupiny VPN a byla chráněna před provozem veřejného internetu.

Architektura pro VPN v 3GPP se významně vyvinula. Zpočátku, v dřívějších releasích, byly VPN služby často realizovány prostřednictvím vyhrazených [APN](/mobilnisite/slovnik/apn/) (Access Point Names) a [IPsec](/mobilnisite/slovnik/ipsec/) tunelů ze zařízení do podnikové brány. V systému 5G je podpora VPN hluboce integrovaná a flexibilnější. Mezi klíčové architektonické komponenty patří User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), která může být nasazena jako vyhrazená UPF pro VPN pro ukotvení provozu v uživatelské rovině, a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), která vynucuje politiky relací specifické pro VPN. Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) může vystavovat VPN schopnosti podnikovým aplikacím. Provoz pro VPN je izolován pomocí mechanismů jako [VLAN](/mobilnisite/slovnik/vlan/), VXLAN nebo [MPLS](/mobilnisite/slovnik/mpls/) štítky v transportní síti a specifických QoS toků v rámci [PDU](/mobilnisite/slovnik/pdu/) session.

Fungování VPN v kontextu 5G začíná u předplatného. Profil předplatného UE v Unified Data Management (UDM) obsahuje informace o VPN skupinách, do kterých UE patří. Když UE naváže PDU Session, může požadovat připojení ke konkrétnímu Data Network Name (DNN) asociovanému s VPN. Síť vybere SMF a UPF schopné tuto VPN podporovat. UPF může implementovat směrování provozu, uplink klasifikátory použít k nasměrování provozu určeného pro podnikovou síť na specifické rozhraní N6 (směrem k lokální podnikové síti), zatímco ostatní provoz jde do veřejného internetu. Zabezpečení je prvořadé; autentizace je posílena a důvěrnost a integrita dat mohou být zajištěny end-to-end mezi UE a podnikovou sítí pomocí IPsec nebo TLS, často za podpory bezpečnostních funkcí mobilní sítě. Rámec VPN v 3GPP tedy poskytuje komplexní, operátorem spravované řešení pro zabezpečené připojení mobilní pracovní síly a zařízení IoT.

## K čemu slouží

Standardizace VPN schopností v rámci 3GPP byla motivována rostoucí poptávkou podniků po zabezpečeném, spolehlivém a spravovatelném mobilním připojení pro své zaměstnance a stroje. Před integrovanými funkcemi VPN v 3GPP podniky často spoléhaly na nadstavbová řešení jako klientovské IPsec VPN, která mohla být složitá na správu ve velkém měřítku, nabízela nekonzistentní výkon a postrádala integraci s funkcemi mobilní sítě jako QoS a bezproblémový roaming.

VPN v 3GPP tyto problémy řeší poskytováním nativních síťových VPN služeb. Řeší potřebu izolace provozu, což zajišťuje, že citlivá podniková data neprocházejí nechráněně veřejným internetem. Řeší problém škálovatelného řízení přístupu, což podnikům umožňuje definovat politiky na základě uživatelských skupin a typů zařízení přímo v systémech mobilního operátora. Dále umožňují pokročilé funkce jako network slicing, kde může být VPN mapována na konkrétní síťový řez (slice) pro zaručení výkonnostních parametrů (latence, šířka pásma) šitých na míru podnikovým aplikacím.

Historicky práce na VPN v 3GPP získaly významnou dynamiku se zaměřením na vertikální segmenty a Mission Critical Services v Release 13/14 a staly se základem podnikových nabídek 5G od Release 15 dále. Tento vývoj řeší omezení nadstavbových řešení hlubokou integrací podpory VPN do architektury jádra 5G. To operátorům umožňuje nabízet VPN jako managed službu se zaručenými Service Level Agreements (SLA), bezproblémovým předáváním mezi typy radiového přístupu a inherentní podporou pro masivní množství zařízení IoT, což je klíčové pro Průmysl 4.0 a další iniciativy digitální transformace.

## Klíčové vlastnosti

- Logická izolace uživatelského provozu od veřejného internetu a jiných VPN
- Integrace s 5G Network Slicing pro zajištění výkonnostních SLA
- Podpora jak VPN služeb typu Layer 3 (IP), tak Layer 2 (Ethernet)
- Centralizované řízení politik pro přístup, QoS a směrování v rámci VPN
- Bezproblémová mobilita a kontinuita relace pro uživatele VPN v celé síti
- Vystavení VPN schopností podnikům prostřednictvím API (např. přes NEF) pro samoobslužnou správu

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.153** (Rel-20) — Multimedia Priority Service (MPS) requirements
- **TR 22.854** (Rel-17) — Feasibility Study on Multimedia Priority Service - Phase 2
- **TR 22.953** (Rel-19) — Multimedia Priority Service Feasibility Study
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.310** (Rel-19) — 3GPP Authentication Framework for Network Nodes

---

📖 **Anglický originál a plná specifikace:** [VPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/vpn/)
