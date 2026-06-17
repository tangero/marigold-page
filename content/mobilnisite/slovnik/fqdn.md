---
slug: "fqdn"
url: "/mobilnisite/slovnik/fqdn/"
type: "slovnik"
title: "FQDN – Fully Qualified Domain Name"
date: 2026-01-01
abbr: "FQDN"
fullName: "Fully Qualified Domain Name"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fqdn/"
summary: "Fully Qualified Domain Name (FQDN) je úplný, jednoznačný název domény pro hostitele nebo síťový uzel, který specifikuje jeho přesnou polohu v hierarchii Domain Name System (DNS). V 3GPP se FQDNs hojně"
---

FQDN je úplný a jednoznačný název domény určující přesnou polohu hostitele v hierarchii DNS, který je v rámci 3GPP široce používán k identifikaci síťových funkcí, koncových bodů a pro zjišťování služeb.

## Popis

V architektuře 3GPP je Fully Qualified Domain Name (FQDN) základním identifikátorem používaným v rámci Uniform Resource Identifiers (URI) k jednoznačné lokalizaci prostředků v IP síti. FQDN se skládá z názvu hostitele a jeho nadřazené domény (domén), až po doménu nejvyšší úrovně (TLD), a zapisuje se jako sekvence oddělená tečkami (např. `nrf.epc.mnc001.mcc505.3gppnetwork.org`). Je 'plně kvalifikovaný', protože nevyvolává žádnou nejednoznačnost ohledně polohy hostitele ve stromu [DNS](/mobilnisite/slovnik/dns/); jedná se o absolutní cestu. V rámci specifikací 3GPP se FQDNs nepoužívají pouze pro webové servery, ale jsou kriticky integrovány do architektury založené na službách (SBA) 5G Core (5GC) a IP Multimedia Subsystem (IMS).

Z mechanického hlediska FQDNs fungují ve spojení s Domain Name System (DNS). Když síťová funkce ([NF](/mobilnisite/slovnik/nf/)), jako je Session Management Function ([SMF](/mobilnisite/slovnik/smf/)), potřebuje komunikovat s jinou NF, například Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), často vytvoří nebo je nakonfigurována s cílovým FQDN. Tento FQDN následuje standardizovanou konvenci pojmenování definovanou 3GPP (např. v TS 23.003). Dotazující se NF provede DNS dotaz (obvykle pro záznamy [NAPTR](/mobilnisite/slovnik/naptr/), SRV nebo A/AAAA), aby tento FQDN přeložil na jednu nebo více IP adres a čísel portů, kde je služba dostupná. Tento proces, známý jako DNS-based Service Discovery, je klíčový pro dynamickou a škálovatelnou povahu cloud-nativních 5G core, což umožňuje vyrovnávání zatížení, redundanci a bezproblémové škálování NF.

Struktura FQDN v 3GPP je velmi organizovaná. Například FQDN pro Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)) v 5G síti může být: `nrf.5gc.mnc<MNC>.mcc<MCC>.3gppnetwork.org`. Tato struktura zakóduje typ NF (`nrf`), síťový řez/instanci (`5gc`), Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)), Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)) a vyhrazenou 3GPP doménu nejvyšší úrovně. Toto hierarchické pojmenování umožňuje logickou organizaci a efektivní DNS překlad. FQDNs se používají v nesčetných 3GPP procedurách: pro HTTP/2 koncové body služeb mezi NF, pro SIP směrování v IMS (např. doména domovské sítě v SIP URI jako `sip:user@home.net`), pro připojení k účtovacím systémům, policy serverům a pro přístup k aplikačním serverům. Poskytují nezbytnou vrstvu abstrakce, která odděluje logickou identitu služby od její fyzické IP lokace, což umožňuje síťovou agilitu a automatizaci.

## K čemu slouží

Zavedení FQDNs v rámci 3GPP bylo motivováno přechodem průmyslu na plně IP sítě a architektury založené na webu. Rané mobilní systémy spoléhaly na statické, předem nakonfigurované point codes nebo IP adresy pro adresování uzlů, které byly nepružné a obtížně spravovatelné ve velkém měřítku. Jak se sítě vyvíjely směrem k IMS (3GPP Release 5/6) a později k cloud-nativnímu 5G Core, objevila se kritická potřeba dynamického, škálovatelného a standardizovaného způsobu zjišťování a komunikace s distribuovanými síťovými službami. FQDNs spolu s DNS tento problém řeší tím, že poskytují globálně unikátní, hierarchický systém pojmenování, který podporuje zjišťování služeb, vyrovnávání zatížení a převzetí služeb při selhání.

Historická motivace spočívá v překonání omezení pevně zakódované síťové topologie. V monolitické síti vyžadovalo přidání nového serveru aktualizaci konfigurace na všech partnerských uzlech. V moderním, na mikroslužbách založeném 5G core s automatickým škálováním a geografickou redundancí mohou být NF dynamicky vytvářeny a ukončovány. FQDNs umožňují konzumentovi NF najít producenta NF bez předchozí znalosti jeho přesné IP adresy. Vrstva DNS překladu může vrátit různé IP adresy na základě zatížení, lokality (pro edge computing) nebo dostupnosti služby. Tím jsou řešeny klíčové požadavky na automatizaci sítě, škálovatelnost a odolnost, což činí z FQDNs základní technologii pro implementaci Service-Based Architecture (SBA) a umožňuje efektivní síťové řezy, kde různé řezy mohou překládat stejný typ NF (např. `smf`) na různé instance na základě řezy specifického FQDN.

## Klíčové vlastnosti

- Poskytuje absolutní, jednoznačný název domény pro hostitele nebo síťovou funkci
- Řídí se hierarchickými konvencemi pojmenování 3GPP, které kódují typ NF, síť a PLMN
- Používá se v rámci URI pro HTTP/2 rozhraní služeb v 5G SBA
- Nezbytný pro DNS-based service discovery a vyrovnávání zatížení NF
- Umožňuje dynamickou síťovou topologii a cloud-nativní škálovatelnost
- Základní pro SIP směrování v IMS a pro identifikaci aplikačních serverů

## Související pojmy

- [DNS – Directory Name Service](/mobilnisite/slovnik/dns/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.167** (Rel-19) — 3GPP IMS Management Object Specification
- **TS 24.228** (Rel-5) — IP Multimedia Call Control Signaling Flows
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- … a dalších 64 specifikací

---

📖 **Anglický originál a plná specifikace:** [FQDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/fqdn/)
