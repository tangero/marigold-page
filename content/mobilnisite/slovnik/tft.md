---
slug: "tft"
url: "/mobilnisite/slovnik/tft/"
type: "slovnik"
title: "TFT – Traffic Flow Template"
date: 2025-01-01
abbr: "TFT"
fullName: "Traffic Flow Template"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tft/"
summary: "Sada paketových filtrů používaná v kontextu Packet Data Protocol (PDP) v sítích GPRS, UMTS a EPS ke klasifikaci paketů uživatelské roviny ve směru downlink a jejich přiřazení ke konkrétním přenosovým"
---

TFT je sada paketových filtrů v kontextu PDP, která klasifikuje pakety uživatelské roviny ve směru downlink a přiřazuje je konkrétním přenosovým kanálům pro ošetření QoS.

## Popis

Traffic Flow Template (TFT) je klíčový konstrukt pro správu politik a provozu v paketových jádrech sítí 3GPP, včetně [GPRS](/mobilnisite/slovnik/gprs/), UMTS a Evolved Packet System (EPS). Funguje na Gateway GPRS Support Node (GGSN) v UMTS nebo na Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) v EPS. TFT je v podstatě kolekce až osmi paketových filtrů (ve směru downlink), které jsou instalovány jako součást kontextu [PDP](/mobilnisite/slovnik/pdp/) (UMTS) nebo připojení [PDN](/mobilnisite/slovnik/pdn/)/přenosového kanálu EPS (EPS). Každý paketový filtr obsahuje kritéria pro shodu, jako jsou zdrojové/cílové IP adresy a čísla portů, typ protokolu (např. TCP/[UDP](/mobilnisite/slovnik/udp/)), [IPsec](/mobilnisite/slovnik/ipsec/) Security [Parameter](/mobilnisite/slovnik/parameter/) Index ([SPI](/mobilnisite/slovnik/spi/)) a bity pole Type of Service (TOS).

Architektonicky je TFT vytvořen uživatelským zařízením (UE) nebo sítí (prostřednictvím Policy and Charging Rules Function - PCRF) a signalizován do bránového uzlu (GGSN/P-GW) během procedur aktivace nebo modifikace kontextu PDP. Ve směru downlink, když paket dorazí z externí paketové datové sítě (např. internetu), provede GGSN/P-GW klasifikaci paketu vyhodnocením jeho hlavičky vůči všem aktivním filtrům TFT asociovaným s uživatelskými kontexty PDP. Paket je pak nasměrován do konkrétního kontextu PDP (a jeho asociovaného rádiového přenosového kanálu), jehož TFT obsahuje odpovídající filtr. Tím vzniká vazba mezi IP tokem (např. VoIP hovor, video stream) a konkrétním přenosovým kanálem, který má požadované charakteristiky Quality of Service (QoS) (např. garantovaný datový tok, priorita).

Jeho role je klíčová pro umožnění více simultánních služeb s různými požadavky na QoS pod jedinou IP adresou uživatele. Například uživatel může mít výchozí přenosový kanál pro best-effort prohlížení internetu a vyhrazený přenosový kanál s TFT, který odpovídá jeho VoIP provozu, aby bylo zajištěno nízké zpoždění a jitter. Mechanismus TFT umožňuje síti aplikovat odlišné QoS politiky, tarifní pravidla a dokonce i způsoby směrování (jako offload na lokální breakout) na bázi jednotlivých služebních toků. Ve směru uplink používá uživatelské zařízení (UE) paketové filtry TFT k mapování svého vlastního odchozího IP provozu na správný přenosový kanál. TFT je tedy základním nástrojem pro implementaci tokově orientovaného QoS a řízení politik v sítích 3GPP.

## K čemu slouží

TFT byl zaveden k vyřešení problému podpory více IP služeb, z nichž každá má odlišné požadavky na Quality of Service (QoS), v rámci jediného kontextu Packet Data Protocol (PDP), který tradičně měl pouze jednu IP adresu a jednu sadu parametrů QoS. Rané datové služby GPRS/UMTS primárně nabízely jediný 'kanál' pro veškerý provoz, což bylo nedostatečné pro služby v reálném čase, jako je Voice over IP (VoIP) nebo videokonference, které vyžadují garantovanou šířku pásma a nízké zpoždění uprostřed jiného provozu na pozadí.

Vytvoření TFT, standardizovaného od Release 99, bylo motivováno vizí All-IP sítí a multimediálních služeb. Umožňuje síti identifikovat a rozlišovat jednotlivé toky provozu (např. samostatná TCP spojení pro e-mail, web a VoIP stream) pocházející ze stejného uživatelského zařízení. Klasifikací paketů do toků může síť následně mapovat každý tok na vyhrazený přenosový kanál s optimalizovanými charakteristikami QoS, což je proces nezbytný pro standardizovanou QoS architekturu 3GPP. Tím byly odstraněny limity dřívějšího, na službu nehledícího 'best-effort' datového kanálu, což operátorům umožnilo nabízet služby různých úrovní, implementovat sofistikované tarifní modely (např. různá sazba pro video vs. chat) a zajistit konzistentní uživatelský zážitek pro aplikace citlivé na zpoždění.

## Klíčové vlastnosti

- Obsahuje až osm paketových filtrů pro klasifikaci provozu ve směru downlink.
- Kritéria filtrů zahrnují 5-tici (IP adresy, porty, protokol), TOS a IPSec SPI.
- Mapuje IP toky na konkrétní kontexty PDP nebo přenosové kanály EPS s definovaným QoS.
- Může být vytvořen uživatelským zařízením (UE) nebo sítí (prostřednictvím PCRF).
- Základní pro umožnění tokově orientovaného QoS a řízení politik.
- Podporuje současné provozování více služeb pod jedinou IP adresou.

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 34.109** (Rel-19) — UE Conformance Test Functions for UMTS
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [TFT na 3GPP Explorer](https://3gpp-explorer.com/glossary/tft/)
