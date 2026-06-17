---
slug: "dns"
url: "/mobilnisite/slovnik/dns/"
type: "slovnik"
title: "DNS – Directory Name Service"
date: 2026-01-01
abbr: "DNS"
fullName: "Directory Name Service"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dns/"
summary: "DNS je hierarchický distribuovaný systém pojmenování používaný v sítích 3GPP pro překlad čitelných doménových jmen na IP adresy a další záznamy o zdrojích. Je zásadní pro vyhledávání služeb, lokalizac"
---

DNS je hierarchický distribuovaný systém pojmenování používaný v sítích 3GPP pro překlad doménových jmen na IP adresy za účelem vyhledávání služeb, lokalizace síťových prvků a směrování provozu.

## Popis

Služba DNS (Directory Name Service) je v 3GPP kritickou součástí infrastruktury založenou na standardech Internet Engineering Task Force ([IETF](/mobilnisite/slovnik/ietf/)), konkrétně RFC 1034 a RFC 1035. Funguje jako distribuovaná databáze, která překládá plně kvalifikovaná doménová jména ([FQDN](/mobilnisite/slovnik/fqdn/)) na odpovídající IP adresy a další záznamy o zdrojích, jako jsou záznamy [NAPTR](/mobilnisite/slovnik/naptr/) (Naming Authority Pointer) a SRV (Service). V rámci architektury 3GPP je DNS hojně využívána funkcemi jádra sítě pro dynamické vyhledávání a výběr partnerských síťových prvků. Například při navazování připojení k paketové datové síti (PDN) může být brána PGW (Packet Data Network Gateway) nebo funkce [SMF](/mobilnisite/slovnik/smf/) (Session Management Function) vybrána na základě DNS dotazů, které zohledňují název přístupového bodu ([APN](/mobilnisite/slovnik/apn/)), polohu účastníka a síťové politiky. Systém využívá hierarchickou strukturu s kořenovými servery, doménami nejvyšší úrovně a autoritativními jmennými servery specifickými pro síť operátora (např. epc.mnc<[MNC](/mobilnisite/slovnik/mnc/)>.mcc<[MCC](/mobilnisite/slovnik/mcc/)>.3gppnetwork.org). DNS dotazy jsou iniciovány různými síťovými funkcemi, včetně [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity), SGSN (Serving GPRS Support Node), HSS (Home Subscriber Server) a PCRF (Policy and Charging Rules Function), za účelem lokalizace služeb, jako jsou PGW/SMF, HSS/UDM nebo aplikační servery. Proces překladu zahrnuje rekurzivní a iterativní dotazy s mechanismy ukládání do mezipaměti na resolverech pro zvýšení efektivity a snížení latence. DNS je také klíčová pro propojení mezi operátory, umožňuje překlad FQDN pro roamingové scénáře a propojení mezi různými veřejnými pozemními mobilními sítěmi (PLMN). V systémech 5G zůstává DNS nezbytná pro architekturu založenou na službách (SBA), kde instance síťových funkcí (NF) registrují své profily a koncové body v NRF (Network Repository Function) a spotřebitelské NF používají objevování služeb založené na DNS k nalezení vhodných produkčních NF na základě názvů služeb, typů NF a dalších výběrových kritérií.

## K čemu slouží

DNS byla zavedena, aby vyřešila problém statického, pevně zakódovaného adresování síťových prvků, které bylo v rozsáhlých dynamických mobilních sítích nepružné a obtížně spravovatelné. Před jejím zavedením vyžadovaly síťové konfigurace ruční aktualizace IP adres v síťových prvcích, což vedlo k provozní složitosti, problémům se škálovatelností a zvýšenému riziku chyb při rozšiřování sítě nebo výpadcích. Hlavním motivem bylo umožnit automatizované dynamické vyhledávání a výběr síťových funkcí, což je zásadní pro vyrovnávání zátěže, redundanci a efektivní využití zdrojů. DNS poskytuje standardizovaný škálovatelný mechanismus pro objevování služeb a uzlů napříč jádrem sítě, podporuje funkce jako překlad APN, výběr PGW/SMF a roaming mezi operátory. Abstrahuje podkladovou síťovou topologii a umožňuje operátorům nasazovat a přesouvat síťové funkce bez nutnosti rekonfigurace každého závislého prvku. Tato flexibilita je klíčová pro vývoj směrem k cloud-nativním virtualizovaným sítím a architektuře 5G založené na službách, kde mohou být síťové funkce pružně vytvářeny a škálovány. DNS také usnadňuje implementaci pokročilých politik směrování provozu, síťového řezání a interoperability více dodavatelů tím, že poskytuje společný rámec pro překlad.

## Klíčové vlastnosti

- Překlad plně kvalifikovaných doménových jmen (FQDN) na IP adresy pro síťové prvky a služby
- Podpora více typů DNS záznamů včetně A, AAAA, NAPTR a SRV pro pokročilé objevování služeb
- Dynamický výběr bran (např. PGW, SMF) na základě názvu přístupového bodu (APN), polohy účastníka a síťových politik
- Zásadní pro roaming mezi PLMN a propojení operátorů překladem FQDN přes hranice sítí
- Integrace s architekturou 5G založenou na službách (SBA) pro objevování a výběr síťových funkcí (NF)
- Mechanismy ukládání do mezipaměti na DNS resolvers pro snížení latence dotazů a zatížení sítě

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)
- [FQDN – Fully Qualified Domain Name](/mobilnisite/slovnik/fqdn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.327** (Rel-13) — 3GPP-WLAN Mobility Stage 2 Description
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- … a dalších 41 specifikací

---

📖 **Anglický originál a plná specifikace:** [DNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dns/)
