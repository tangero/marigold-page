---
slug: "nat-t"
url: "/mobilnisite/slovnik/nat-t/"
type: "slovnik"
title: "NAT-T – NAT Traversal"
date: 2025-01-01
abbr: "NAT-T"
fullName: "NAT Traversal"
category: "Core Network"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/nat-t/"
summary: "Soubor technik a protokolů, které umožňují síťovým aplikacím, zejména VPN a komunikaci v reálném čase, správně fungovat přes zařízení s překladem síťových adres (NAT). V rámci 3GPP zajišťuje, aby služ"
---

NAT-T je soubor technik a protokolů, které umožňují aplikacím, jako je IMS-based VoLTE nebo VPN, správně fungovat přes zařízení s překladem síťových adres (NAT) v mobilních sítích a zajišťují bezproblémové end-to-end spojení.

## Popis

[NAT](/mobilnisite/slovnik/nat/) Traversal (NAT-T) označuje mechanismy, které umožňují aplikačním protokolům navazovat a udržovat spojení přes jedno nebo více zařízení s NAT, která normálně narušují předpoklad end-to-end IP konektivity. V sítích 3GPP je NAT-T obzvláště důležitý, protože uživatelské zařízení (UE) je typicky za NAT funkcí v [PGW](/mobilnisite/slovnik/pgw/) (4G) nebo [UPF](/mobilnisite/slovnik/upf/) (5G). Protokoly jako [SIP](/mobilnisite/slovnik/sip/) pro IMS hlas/video, [ESP](/mobilnisite/slovnik/esp/) pro [IPsec](/mobilnisite/slovnik/ipsec/) [VPN](/mobilnisite/slovnik/vpn/) a další, které přenášejí IP adresy a čísla portů ve svém payloadu nebo používají specifická schémata vyjednávání portů, selžou, pokud nejsou použity techniky s podporou NAT.

Architektura zahrnuje jak síťová, tak koncová řešení. Klíčovou síťovou komponentou je Application Layer Gateway (ALG), často integrovaná do zařízení NAT (PGW/UPF) nebo jako samostatná síťová funkce. Pro SIP [IMS-ALG](/mobilnisite/slovnik/ims-alg/) (nebo IMS-AGW) upravuje zprávy SIP/SDP a překládá soukromé informace IP:port v těle zprávy tak, aby odpovídaly veřejným IP:port používaným v mapování NAT. Pro IPsec mechanismus NAT-T definovaný v IETF RFC (jako RFC 3947/3948) zapouzdřuje pakety ESP do UDP, protože NAT zařízení obvykle dokážou stavově pracovat s UDP, a zahrnuje payload pro detekci NAT během vyjednávání IKEv2.

Jak to funguje: Pro IMS služby, když UE iniciuje SIP REGISTER nebo INVITE, SIP ALG zkontroluje paket, vytvoří vazbu NAT pro mediální porty a přepíše řádky SDP 'c=' a 'm=' tak, aby odrážely veřejnou adresu. To umožní vzdálené straně odesílat mediální streamy na správnou veřejnou IP:port, které NAT následně přepošle k UE. Pro IPsec VPN (např. pro podnikový přístup) používají UE a bezpečnostní brána IKEv2 s podporou NAT-T. Během výměny IKE_SA_INIT detekují přítomnost zařízení NAT (pomocí payloadů NAT-D) a následně přepnou na zapouzdření dalšího provozu IKE a ESP do UDP portu 4500, což úspěšně projde přes NAT. Síť 3GPP může také využívat Session Border Controllers (SBC) nebo Interworking Functions, které plní podobné funkce traversal pro hranice mezi operátory nebo přístupovými sítěmi.

## K čemu slouží

NAT-T byl vyvinut k vyřešení základního problému, že NAT narušuje mnoho IP-based aplikací. Když sítě 3GPP všeobecně přijaly NAT pro šetření IPv4 adresami, neúmyslně tím narušily služby, které se stávaly nezbytnými, jako je Voice over IP (VoIP) přes IMS a zabezpečený vzdálený přístup přes IPsec VPN. Tyto protokoly spoléhají na znalost skutečných adres koncových bodů pro přímou komunikaci, což NAT zastírá. Bez NAT-T by IMS hovory selhávaly, protože by se nemohly navázat mediální streamy, a VPN tunely by se nemohly vyjednat, což by vážně omezilo využitelnost mobilních datových sítí pro komunikaci v reálném čase a zabezpečenou komunikaci.

Vznik technik NAT-T v rámci 3GPP (a jejich převzetí z IETF) byl motivován komerčním nasazením all-IP služeb jako VoLTE. Operátoři potřebovali garantovat, že hlasová služba bude spolehlivě fungovat pro každého účastníka bez ohledu na to, že je za NAT. Řešilo to omezení jednoduchého NAT, které bylo navrženo pro klient-server prohlížení webu, ale ne pro peer-to-peer nebo symetrické toky protokolů. NAT-T zajistil, že síťová strategie šetření adresami neprobíhá za cenu narušení pokročilých služeb, což umožnilo naplnit vizi all-IP core sítě podporující bohatou škálu multimediálních a podnikových aplikací.

## Klíčové vlastnosti

- Umožňuje protokolům založeným na SIP/SDP (např. IMS VoLTE/VoNR) fungovat přes NAT.
- Podporuje průchod IPsec VPN (IKEv2/ESP) pomocí UDP zapouzdření (port 4500).
- Využívá Application Layer Gateways (ALG) k úpravám payloadů protokolů při přenosu.
- Zahrnuje mechanismy detekce NAT během navazování spojení (např. NAT-D v IKE).
- Spolupracuje s ICE (Interactive Connectivity Establishment) pro traversal s asistencí koncového bodu.
- Standardizováno v 3GPP pro interoperabilitu mezi zařízeními různých výrobců a operátory.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 29.139** (Rel-19) — H(e)NB - SeGW Interface Specification
- **TS 29.828** (Rel-12) — IMS Media Plane Security H.248 Profiles Study
- **TS 29.839** (Rel-11) — H(e)NB - SeGW Interface Specification

---

📖 **Anglický originál a plná specifikace:** [NAT-T na 3GPP Explorer](https://3gpp-explorer.com/glossary/nat-t/)
