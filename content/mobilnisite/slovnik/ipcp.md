---
slug: "ipcp"
url: "/mobilnisite/slovnik/ipcp/"
type: "slovnik"
title: "IPCP – IP Control Protocol"
date: 2025-01-01
abbr: "IPCP"
fullName: "IP Control Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ipcp/"
summary: "IP Control Protocol (IPCP) je řídicí protokol sítě (NCP) v rámci sady Point-to-Point Protocol (PPP), který se konkrétně používá ke konfiguraci, povolení a zakázání modulů protokolu IPv4 na obou koncíc"
---

IPCP je řídicí protokol sítě (Network Control Protocol) v rámci PPP, který slouží ke konfiguraci, povolení a zakázání modulů protokolu IPv4 na obou koncích point-to-point spojení za účelem navázání IPv4 konektivity.

## Popis

IP Control Protocol (IPCP) je definován [IETF](/mobilnisite/slovnik/ietf/) v [RFC](/mobilnisite/slovnik/rfc/) 1332 a je klíčovou součástí architektury Point-to-Point Protocol ([PPP](/mobilnisite/slovnik/ppp/)). Samotný PPP poskytuje standardní metodu pro přenos multiprotokolových datagramů přes point-to-point spojení. IPCP funguje jako sourozenecký protokol k dalším [NCP](/mobilnisite/slovnik/ncp/), jako je IPv6CP (pro IPv6), a pracuje ve fázi PPP síťové vrstvy. Jeho jediným účelem je vyjednat parametry specifické pro IPv4 pro PPP spojení, čímž jej převádí z pouhé datové linky na funkční spojení síťové vrstvy schopné přenášet IPv4 pakety.

IPCP funguje prostřednictvím jednoduchého symetrického stavového stroje využívajícího podobný mechanismus výměny paketů jako Link Control Protocol ([LCP](/mobilnisite/slovnik/lcp/)). Po navázání a autentizaci PPP spojení (pomocí LCP a případně [PAP](/mobilnisite/slovnik/pap/)/[CHAP](/mobilnisite/slovnik/chap/)) začíná vyjednávání IPCP. Dva partneři si vyměňují pakety Configure-Request obsahující požadované konfigurační volby. Nejzásadnější volbou je IP-Adresa, kde může partner požadovat konkrétní adresu, navrhnout adresu pro vzdálený konec nebo naznačit, že adresu poskytne později. Mezi další volby patří adresa primárního [DNS](/mobilnisite/slovnik/dns/) serveru, adresa primárního NBNS (NetBIOS Name Server) serveru a IP-Compression-Protocol pro Van Jacobsonovu kompresi hlaviček TCP/IP. Každý partner odpovídá paketem Configure-Ack (přijetí), Configure-Nak (odmítnutí s protinávrhem) nebo Configure-Reject (odmítnutí nerozpoznané volby). Tato výměna pokračuje, dokud obě strany neodešlou a nepřijmou Configure-Ack.

Jakmile IPCP dosáhne stavu Opened, je protokol IPv4 považován za nakonfigurovaný pro toto PPP spojení. Všechny IPv4 pakety jsou poté zapouzdřeny v rámcích PPP (pole Protocol s hodnotou 0x0021) a přenášeny. IPCP také zajišťuje ukončení spojení síťové vrstvy IPv4 prostřednictvím paketů Terminate-Request a Terminate-Ack a může dynamicky převyjednat parametry kdykoli během aktivního spojení pomocí Configure-Request. V kontextech 3GPP hrál IPCP historicky roli v raných PS datových službách (GPRS), kde rozhraní mezi terminálem a sítí (např. přes rozhraní Um/Gb) mohlo používat PPP, a zůstává relevantní pro určité legacy interworking funkce a specifické konfigurace backhaulových spojení.

## K čemu slouží

IPCP byl vytvořen jako součást sady PPP od IETF k řešení problému automatizace konfigurace parametrů síťové vrstvy přes jednoduchá point-to-point spojení. Před PPP a IPCP vyžadovalo navázání IP spojení přes sériovou linku (jako vytáčené modemové připojení) ruční konfiguraci IP adres na obou koncích, což bylo náchylné k chybám a nepraktické pro rozsáhlá nasazení, jako jsou poskytovatelé internetových služeb (ISP). IPCP poskytl odlehčený standardizovaný protokol pro dynamické vyjednávání těchto parametrů, což umožnilo 'plug-and-play' IP konektivitu.

V rámci 3GPP bylo přijetí IPCP hnáno potřebou spolehlivého standardizovaného protokolu datové linky pro rané paketově přepínané služby. V GPRS a raných verzích UMTS mohlo být spojení mezi mobilní stanicí (MS) a sítí přes rádiové rozhraní navázáno pomocí PPP, přičemž IPCP plnil klíčový úkol přiřazení IPv4 adresy MS ze sítě. Tím bylo mobilní zařízení bezproblémově integrováno do IP sítě. Zatímco pozdější systémy 3GPP (EPS, 5GS) přešly na čistě GTP model, kde je přiřazení IP adresy řešeno jádrem sítě (DHCPv4 nebo z PGW/UPF) během zřizování PDN/PDU relace, IPCP zůstává specifikováno pro určité interworking scénáře, podporu legacy zařízení a pro specifické typy přístupu, kde je PPP stále podkladovým linkovým protokolem.

## Klíčové vlastnosti

- Vyjednává přiřazení IPv4 adresy pro oba konce PPP spojení
- Konfiguruje pomocné parametry, jako jsou adresy DNS a NBNS serverů
- Podporuje Van Jacobsonovu kompresi hlaviček TCP/IP prostřednictvím vyhrazené volby
- Používá jednoduchý stavový stroj request/ack/nak/reject pro robustní vyjednávání
- Umožňuje dynamické převyjednání parametrů během aktivní relace
- Funguje v součinnosti s LCP a autentizačními protokoly v rámci zásobníku PPP

## Související pojmy

- [PPP – Priority Precedence Preemption](/mobilnisite/slovnik/ppp/)
- [IPV6CP – IPv6 Control Protocol](/mobilnisite/slovnik/ipv6cp/)
- [LCP – Logical Channel Prioritization](/mobilnisite/slovnik/lcp/)
- [DHCP – Dynamic Host Configuration Protocol](/mobilnisite/slovnik/dhcp/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN

---

📖 **Anglický originál a plná specifikace:** [IPCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipcp/)
