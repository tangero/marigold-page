---
slug: "3g-sgsn"
url: "/mobilnisite/slovnik/3g-sgsn/"
type: "slovnik"
title: "3G-SGSN – 3rd Generation Serving GPRS Support Node"
date: 2025-01-01
abbr: "3G-SGSN"
fullName: "3rd Generation Serving GPRS Support Node"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/3g-sgsn/"
summary: "3G-SGSN je prvek jádra sítě v sítích 3GPP UMTS odpovědný za správu paketových datových relací pro mobilní zařízení. Obsluhuje správu mobility, správu relací a autentizaci uživatele pro 3G paketově pře"
---

3G-SGSN je prvek jádra sítě v sítích 3GPP UMTS odpovědný za správu paketových datových relací, obsluhu mobility, správu relací a autentizaci pro 3G paketově přepínané služby.

## Popis

3G-SGSN (Serving GPRS Support Node třetí generace) je základní komponenta paketově přepínaného jádra sítě UMTS (Universal Mobile Telecommunications System), definovaná od 3GPP Release 99. Slouží jako primární síťový uzel odpovědný za poskytování paketových datových služeb uživatelskému zařízení (UE) v jeho geografické oblasti působnosti. 3G-SGSN vykonává kritické funkce včetně správy mobility, správy relací, autentizace a autorizace uživatele a směrování a přenosu paketů. Rozhraní k němu má UMTS Terrestrial Radio Access Network (UTRAN) přes rozhraní Iu-PS, jiné SGSN přes rozhraní Gn (uvnitř stejné PLMN) nebo Gp (k SGSN v jiných PLMN) a Gateway GPRS Support Node (GGSN) přes rozhraní Gn/Gp pro přístup k externím paketovým datovým sítím (PDN), jako je internet nebo privátní podnikové sítě.

Z architektonického hlediska obsahuje 3G-SGSN několik logických funkčních jednotek. Funkce správy mobility sleduje polohu UE, ať už je ve stavu IDLE, STANDBY nebo READY, a spravuje procedury jako Attach, Detach, aktualizace směrovací oblasti (Routing Area Updates) a předávání spojení mezi SGSN (inter-SGSN handovers). Funkce správy relací je odpovědná za vytváření, udržování a ukončování kontextů Packet Data Protocol (PDP), což jsou logická spojení mezi UE a konkrétním GGSN poskytující datovou relaci s definovaným profilem QoS. 3G-SGSN má také rozhraní k Home Location Register (HLR) nebo Home Subscriber Server (HSS) přes rozhraní Gr pro autentizaci uživatele (pomocí algoritmů jako AKA - Authentication and Key Agreement) a získávání dat z profilu účastníka, a k Equipment Identity Register (EIR) přes rozhraní Gf pro kontrolu IMEI.

Z pohledu datové roviny přijímá 3G-SGSN datové pakety uživatele z UTRAN, zapouzdřuje je pomocí GPRS Tunneling Protocol pro uživatelskou rovinu (GTP-U) a tuneluje je k příslušnému GGSN na základě PDP kontextu. Naopak přijímá downlink GTP-U pakety z GGSN, odstraní z nich zapouzdření a přepošle je správnému Radio Network Controller (RNC), který obsluhuje dané UE. Také vykonává funkce jako sběr účtovacích dat (generování Charging Data Records - CDR), zákonné odposlechy a může vynucovat určitá pravidla politiky sítě. 3G-SGSN byl navržen tak, aby podporoval vyšší datové rychlosti a sofistikovanější mechanismy QoS ve srovnání se svým předchůdcem pro 2G GPRS, v souladu s možnostmi rádiového rozhraní UMTS.

## K čemu slouží

3G-SGSN byl vytvořen jako součást architektury 3GPP UMTS, aby poskytoval robustní a škálovatelné paketově přepínané jádro sítě schopné podporovat pokročilé datové služby plánované pro mobilní sítě třetí generace. Před 3G sítěmi zavedly 2G GPRS sítě koncept SGSN pro základní paketová data, ale tyto systémy byly omezené v datovém propustnosti, podpoře QoS a efektivitě. Přechod na UMTS s jeho rádiovým rozhraním Wideband CDMA (WCDMA) sliboval výrazně vyšší datové rychlosti (až 2 Mbps zpočátku) a složitější služby, jako je videohovor a multimédia. Stávající 2G-SGSN nebyl optimalizován pro nový protokolový zásobník rozhraní Iu-PS (používající RANAP přes ATM/AAL5) ani pro zvýšené požadavky na QoS v UMTS.

3G-SGSN byl vyvinut, aby tyto nedostatky odstranil a sloužil jako kotva pro mobilitu paketových dat a správu relací v novém 3G ekosystému. Řešil problém efektivní správy paketových datových relací pro uživatele pohybující se vysokou rychlostí mezi buňkami a směrovacími oblastmi v rámci UTRAN. Poskytoval potřebná rozhraní pro integraci s novou autentizační infrastrukturou (pomocí USIM karet a silnějších AKA procedur) a pro podporu více současných PDP kontextů na uživatele, což umožňovalo současný běh služeb s různými požadavky na QoS (např. relace Voice-over-IP a relace prohlížení webu). Jeho vznik byl motivován posunem průmyslu od hlasově orientovaných k datově orientovaným mobilním sítím, což vyžadovalo prvek jádra sítě schopný zvládnout očekávaný růst mobilního datového provozu a složitosti služeb při zachování bezproblémové mobility a robustní bezpečnosti.

## Klíčové vlastnosti

- Správa mobility pro 3G uživatele paketových dat (Attach, RAU, předávání spojení)
- Správa relací pro aktivaci, modifikaci a deaktivaci PDP kontextu
- Autentizace a autorizace uživatele přes HLR/HSS pomocí AKA procedur
- Směrování a tunelování paketů mezi UTRAN a GGSN pomocí GTP-U
- Sběr účtovacích dat pro paketové datové relace
- Rozhraní k UTRAN (Iu-PS), GGSN (Gn), HLR (Gr) a jiným SGSN (Gn/Gp)

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN

---

📖 **Anglický originál a plná specifikace:** [3G-SGSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/3g-sgsn/)
