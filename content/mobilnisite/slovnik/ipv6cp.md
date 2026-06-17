---
slug: "ipv6cp"
url: "/mobilnisite/slovnik/ipv6cp/"
type: "slovnik"
title: "IPV6CP – IPv6 Control Protocol"
date: 2025-01-01
abbr: "IPV6CP"
fullName: "IPv6 Control Protocol"
category: "Protocol"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ipv6cp/"
summary: "IPV6CP je řídicí protokol sítě (Network Control Protocol, NCP) v sadě protokolu Point-to-Point Protocol (PPP), který se používá k navázání, konfiguraci, otestování a ukončení protokolu IPv6 přes spoje"
---

IPV6CP je řídicí protokol sítě (Network Control Protocol) v rámci PPP, který slouží k navázání, konfiguraci a správě IPv6 konektivity přes spojení typu point-to-point vyjednáváním parametrů specifických pro IPv6.

## Popis

Řídicí protokol IPv6 (IPv6 Control Protocol, IPV6CP) je podřízený protokol protokolu Point-to-Point Protocol (PPP), definovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý 3GPP pro použití v určitých starších přístupových scénářích. Jako řídicí protokol sítě (Network Control Protocol, [NCP](/mobilnisite/slovnik/ncp/)) má za jediný úkol konfigurovat, povolit a zakázat protokol IPv6 na obou koncích datového spoje PPP. Funguje poté, co základní spojení navázal řídicí protokol spoje PPP (PPP Link Control Protocol, [LCP](/mobilnisite/slovnik/lcp/)). IPV6CP je zodpovědný za vyjednávání parametrů specifických pro IPv6, které jsou nezbytné pro to, aby obě protistrany mohly přes tento spoj komunikovat pomocí IPv6.

Protokol funguje prostřednictvím jednoduché výměny paketů Configure-Request, Configure-Ack, Configure-Nak a Configure-Reject. Nejdůležitějším parametrem, který IPV6CP vyjednává, je identifikátor rozhraní (Interface Identifier). V IPv6 se link-lokální adresa vytvoří spojením známé link-lokální předpony (fe80::/64) s identifikátorem rozhraní. IPV6CP zajišťuje, že dvě připojená rozhraní na spoji PPP zvolí jedinečné 64bitové identifikátory rozhraní, aby se předešlo kolizím adres na místním spoji. Může také vyjednávat protokol pro kompresi IPv6, i když to je u moderního hardwaru méně obvyklé. Jakmile IPV6CP dosáhne stavu Opened, je protokol IPv6 na daném spoji PPP považován za nakonfigurovaný a lze vyměňovat IPv6 pakety.

V architektuře 3GPP je IPV6CP specifikován pro použití při aktivaci kontextu paketového datového protokolu (Packet Data Protocol, PDP) pro IPv6 v sítích 2G ([GPRS](/mobilnisite/slovnik/gprs/)) a 3G (UMTS). Když mobilní stanice požádá o kontext PDP pro IPv6, síť a terminál používají PPP, včetně IPV6CP, přes logický spoj k vyjednání konfigurace IPv6. To je zvláště relevantní pro model referenčního bodu Gi a pro spolupráci s externími sítěmi PDN. Zatímco jeho význam poklesl s přechodem na plně IP architektury 4G/5G, kde se IPv6 konfiguruje pomocí DHCPv6 nebo bezstavové autokonfigurace adres (Stateless Address Autoconfiguration, SLAAC), pochopení IPV6CP zůstává důležité pro údržbu starších systémů a pro pochopení vývoje IP konfigurace v mobilních sítích.

## K čemu slouží

IPV6CP byl vytvořen jako součást sady PPP, aby rozšířil schopnosti PPP za IPv4 a podporoval internetový protokol nové generace, IPv6. PPP byl dominantním protokolem pro navazování přímých spojení přes sériové linky, vytáčené modemy a, což je klíčové, přes rané přenosové kanály mobilních dat. Před IPV6CP mělo PPP pouze řídicí protokol pro IPv4 (IPv4 Control Protocol, [IPCP](/mobilnisite/slovnik/ipcp/)). Nástup IPv6 vyžadoval paralelní řídicí protokol pro správu jedinečných konfiguračních parametrů IPv6 na spoji point-to-point.

Jeho účelem v rámci 3GPP bylo poskytnout standardizovanou metodu pro mobilní zařízení ([MS](/mobilnisite/slovnik/ms/)/UE) a síťové prvky (GGSN v [GPRS](/mobilnisite/slovnik/gprs/)/UMTS), aby mohly vyjednávat a navazovat IPv6 konektivitu během aktivace kontextu PDP. Řešil problém, jak automaticky konfigurovat link-lokální IPv6 adresy a dohodnout parametry bez manuálního zásahu, což je pro škálovatelnost v mobilních sítích zásadní. IPV6CP odstranil omezení stávající konfigurace PPP pouze pro IPv4, což umožnilo rané nasazení a testování IPv6 v sítích 3GPP. Vytvořil most mezi zavedeným rámcem PPP a novou sadou protokolů IPv6, čímž zajistil zpětnou kompatibilitu a hladkou cestu přechodu pro síťové operátory.

## Klíčové vlastnosti

- Řídicí protokol sítě PPP (NCP) pro konfiguraci IPv6
- Vyjednává jedinečný 64bitový identifikátor rozhraní (Interface Identifier) pro každý konec spoje PPP
- Používá stejný mechanismus výměny paketů jako LCP (Request, Ack, Nak, Reject)
- Umožňuje vytváření IPv6 link-lokálních adres (fe80::/64)
- Může volitelně vyjednávat parametry komprese hlaviček IPv6
- Standardizován IETF v RFC 5072 a přijat 3GPP pro starší přístup

## Související pojmy

- [IPCP – IP Control Protocol](/mobilnisite/slovnik/ipcp/)

## Definující specifikace

- **TS 27.060** (Rel-19) — TE-MT Interworking for Packet Domain
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN

---

📖 **Anglický originál a plná specifikace:** [IPV6CP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipv6cp/)
