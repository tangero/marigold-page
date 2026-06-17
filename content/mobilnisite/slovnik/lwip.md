---
slug: "lwip"
url: "/mobilnisite/slovnik/lwip/"
type: "slovnik"
title: "LWIP – LTE WLAN Radio Level Integration with IPsec Tunnel"
date: 2025-01-01
abbr: "LWIP"
fullName: "LTE WLAN Radio Level Integration with IPsec Tunnel"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lwip/"
summary: "V kontextu LTE-WLAN Radio Level Integration with IPsec Tunnel (LWIP) se termín LWIP vztahuje k protokolové datové jednotce generované entitou LWIPEP pro zabezpečený přenos přes WLAN. Představuje zapou"
---

LWIP je protokolová datová jednotka generovaná pro zabezpečený přenos přes WLAN, která představuje zapouzdřená uživatelská data směrovaná přes IPsec tunel mezi UE a eNB za účelem umožnění integrace WLAN řízené LTE.

## Popis

Ve specifikaci 3GPP pro LTE WLAN Radio Level Integration with [IPsec](/mobilnisite/slovnik/ipsec/) Tunnel (často zkracováno jako LWIP) termín 'LWIP' konkrétně označuje protokolovou datovou jednotku (PDU). Tuto LWIP PDU generuje entita LWIP Encapsulation Protocol ([LWIPEP](/mobilnisite/slovnik/lwipep/)) v uživatelském zařízení (UE) pro přenos ve směru downlink a v eNodeB ([eNB](/mobilnisite/slovnik/enb/)) pro přenos ve směru uplink, a je určena k přenosu přes WLAN spojení. Jejím hlavním účelem je bezpečně integrovat WLAN jako datový rádiový bearer pro provoz LTE. LWIP PDU je v podstatě IP paket, který zapouzdřuje původní uživatelská data (IP paket nebo Ethernetový rámec) a je chráněn IPsec tunelem Encapsulating Security Payload ([ESP](/mobilnisite/slovnik/esp/)), zřízeným přímo mezi UE a eNB.

Architektura zahrnuje zřízení IPsec ESP tunelu mezi UE a eNB přes nedůvěryhodnou WLAN přístupovou síť. Pro uživatelská data určená k použití LWIP beareru vezme entita LWIPEP v UE původní uplink IP paket (od aplikací), provede případné potřebné zapouzdření (např. do Ethernetového rámce, pokud to WLAN vyžaduje), a tento se stane datovou částí nového IP paketu. Tento nový vnější IP paket je ten, který je zabezpečen IPsec ESP tunelem a směrován přes WLAN spojení k eNB. Výsledný zabezpečený paket, připravený k přenosu přes WLAN, je LWIP PDU. Ve směru downlink provádí entita LWIPEP v eNB reverzní operaci, vytvářejíc zabezpečenou LWIP PDU pro přenos k UE přes WLAN.

Z pohledu sítě má eNB nad touto datovou cestou plnou kontrolu. Rozhoduje, které EPS bearery jsou směrovány přes LWIP tunel (WLAN) a které jsou posílány přes konvenční rozhraní LTE-Uu. eNB ukončuje IPsec tunel, dešifruje LWIP PDU, extrahuje původní uživatelská data a přeposílá je směrem k jádru sítě přes rozhraní S1-U. Díky tomu se WLAN spojení jeví jako zabezpečená, integrovaná transportní vrstva 2 pro LTE bearer, kterou zcela spravuje eNB. Klíčovými komponentami jsou entita LWIPEP, IPsec bezpečnostní asociace a signalizace řídicí roviny, která konfiguruje LWIP bearer. Úlohou LWIP PDU je být standardizovaným, zabezpečeným kontejnerem, který umožňuje eNB používat rádiové prostředky WLAN jako řízené rozšíření LTE rádiové přístupové sítě.

## K čemu slouží

Technologie LWIP byla vyvinuta, aby poskytla alternativní, zabezpečenou metodu pro těsnou integraci WLAN s LTE na rádiové úrovni, která doplňuje přístup [LWA](/mobilnisite/slovnik/lwa/). Řešila potřebu řešení, které by mohlo fungovat s existujícími, neupravenými WLAN přístupovými body (nedůvěryhodné WLAN) bez nutnosti dedikovaného WLAN Termination (WT) uzlu, jak je definováno pro LWA. Před zavedením LWIP vyžadovalo použití nedůvěryhodného WLAN směrování uživatelského provozu přes jádro sítě (např. přes ePDG), což zvyšovalo latenci a složitost pro správu rádiových prostředků v reálném čase.

Hlavním problémem, který LWIP řeší, je umožnit [eNB](/mobilnisite/slovnik/enb/) přímo řídit a bezpečně směrovat provoz uživatelské roviny přes jakoukoli obecnou WLAN síť a zacházet s ní jako s virtuálním rádiovým spojením. Řeší bezpečnostní problém přenosu uživatelských dat LTE přes nedůvěryhodnou IP síť (WLAN) zavedením přímého [IPsec](/mobilnisite/slovnik/ipsec/) tunelu mezi UE a eNB. Tento přístup poskytuje cestu s nižší latencí ve srovnání s tunelováním přes jádro sítě, umožňuje rychlejší přepínání mezi LTE a WLAN a dává eNB schopnost provádět efektivní řízení provozu a agregaci na rádiové úrovni. Motivací bylo nabídnout operátorům flexibilní možnost nasazení integrace WLAN, která nevyžadovala upgrade samotné WLAN infrastruktury, čímž se snížila bariéra pro využití existujících Wi-Fi nasazení k rozšíření kapacity mobilní sítě.

## Klíčové vlastnosti

- Definuje specifický formát PDU pro zabezpečený přenos přes WLAN v kontextu LWIP
- Spoléhá se na IPsec ESP tunel zřízený přímo mezi UE a eNB
- Umožňuje eNB používat nedůvěryhodné, standardní WLAN AP jako datovou cestu
- Podporuje rozhodnutí o směrování specifická pro bearer, která činí eNB
- Poskytuje integritu a důvěrnost uživatelských dat přenášených přes WLAN
- Umožňuje mobilitu UE mezi WLAN a LTE s kontinuitou relace řízenou eNB

## Související pojmy

- [LWIPEP – LWIP Encapsulation Protocol](/mobilnisite/slovnik/lwipep/)
- [LWA – LTE-WLAN Radio Level Aggregation](/mobilnisite/slovnik/lwa/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [ESP – Efficiency Speed Percentage product](/mobilnisite/slovnik/esp/)
- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.729** (Rel-15) — Unlicensed Spectrum Offloading System Enhancements
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 32.868** (Rel-15) — OAM aspects of LTE-WLAN integration (LWA/LWIP)
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.361** (Rel-19) — LWIP Encapsulation Protocol Specification
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.463** (Rel-19) — XwAP Protocol Specification
- **TS 36.464** (Rel-19) — Xw Interface User Plane Protocol
- **TS 36.465** (Rel-19) — Xw User Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [LWIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lwip/)
