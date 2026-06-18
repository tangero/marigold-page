---
slug: "rgw"
url: "/mobilnisite/slovnik/rgw/"
type: "slovnik"
title: "RGW – Residential GateWay"
date: 2025-01-01
abbr: "RGW"
fullName: "Residential GateWay"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rgw/"
summary: "Síťová bránové zařízení instalované v domácnostech, které zajišťuje konektivitu mezi domácí sítí a sítí poskytovatele služeb. Typicky kombinuje funkce modemu, směrovače a často i bezdrátového přístupo"
---

RGW je rezidenční síťová brána (gateway), která propojuje domácí sítě se sítí poskytovatele služeb. Kombinuje funkce modemu, směrovače (routeru) a často i bezdrátového přístupového bodu, čímž umožňuje širokopásmový přístup a služby přes infrastrukturu 3GPP.

## Popis

Rezidenční brána (Residential GateWay, RGW) je zařízení umístěné u zákazníka, které ukončuje síťové připojení poskytovatele služeb v domácnosti předplatitele. Funguje zároveň jako modem (převádí signály pro přístupovou technologii, jako je [DSL](/mobilnisite/slovnik/dsl/) nebo optické vlákno) a jako směrovač (spravuje IP provoz mezi domácí sítí a internetem). RGW typicky obsahuje vestavěný Ethernetový přepínač pro kabelová připojení a Wi-Fi přístupový bod pro bezdrátovou konektivitu. Implementuje klíčové síťové funkce, jako je [DHCP](/mobilnisite/slovnik/dhcp/) pro automatické přidělování IP adres připojeným zařízením, překlad síťových adres ([NAT](/mobilnisite/slovnik/nat/)) pro sdílení jedné veřejné IP adresy více zařízeními a funkce firewallu pro zabezpečení. V kontextech 3GPP se RGW může připojovat přes různé přístupové sítě, včetně pevného širokopásma (jako xDSL nebo [PON](/mobilnisite/slovnik/pon/)) nebo bezdrátově (pomocí 3GPP rádiových technologií). Rozhraní k síťovým prvkům, jako je [BNG](/mobilnisite/slovnik/bng/) v pevných sítích nebo [UPF](/mobilnisite/slovnik/upf/) v 5G jádru sítě, využívá autentizační mechanismy jako 802.1X nebo PPPoE. RGW také podporuje mechanismy kvality služeb (QoS) pro upřednostnění provozu (např. zajištění nízké latence pro VoIP nebo vysoké propustnosti pro streamování videa) a může obsahovat hlasové adaptéry pro analogovou telefonní službu přes IP (VoIP). Pokročilé RGW podporují vzdálenou správu pomocí protokolů jako TR-069, což operátorům umožňuje konfigurovat, monitorovat a řešit problémy se zařízením bez fyzické návštěvy.

## K čemu slouží

Rezidenční brána byla vyvinuta jako jednotný, spravovatelný koncový bod pro poskytování více služeb přes širokopásmová připojení do domácností. Řeší omezení samostatných modemů a směrovačů, které mohly vést k problémům s kompatibilitou, složitému nastavení a obtížné diagnostice. Integrací více funkcí do jednoho zařízení RGW zjednodušuje instalaci pro spotřebitele a snižuje náklady na podporu pro operátory. Její vznik motivoval růst služeb triple-play (internet, [TV](/mobilnisite/slovnik/tv/), telefonie), které vyžadují různé síťové charakteristiky: vysokou propustnost pro video, nízkou latenci pro hlas a spolehlivou konektivitu pro data. RGW umožňuje operátorům řídit kvalitu uživatelského zážitku implementací QoS politik a správou prostředí domácí sítě. Slouží také jako platforma pro nasazení nových služeb, jako je automatizace chytré domácnosti, bezpečnostní monitoring a rodičovské kontroly, což vytváří dodatečné zdroje příjmů pro poskytovatele služeb.

## Klíčové vlastnosti

- Kombinovaná funkce modemu a směrovače pro zjednodušení domácího síťování
- Integrovaný Wi-Fi přístupový bod s podporou více pásem (2,4 GHz a 5 GHz)
- Hlasový adaptér pro analogovou telefonní službu (POTS) přes IP (VoIP)
- Pokročilá QoS pro upřednostnění různých typů provozu (hlas, video, data)
- Možnosti vzdálené správy přes TR-069 pro konfiguraci a diagnostiku
- Podpora více rozhraní WAN včetně DSL, optického vlákna a 3GPP bezdrátového připojení

## Související pojmy

- [RG – Residential Gateway](/mobilnisite/slovnik/rg/)
- [BNG – Broadband Network Gateway](/mobilnisite/slovnik/bng/)
- [VOIP – Voice over IP](/mobilnisite/slovnik/voip/)
- [IPTV – Internet Protocol Television](/mobilnisite/slovnik/iptv/)

## Definující specifikace

- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B

---

📖 **Anglický originál a plná specifikace:** [RGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/rgw/)
