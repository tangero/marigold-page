---
slug: "turn"
url: "/mobilnisite/slovnik/turn/"
type: "slovnik"
title: "TURN – Traversal Using Relays around NAT"
date: 2025-01-01
abbr: "TURN"
fullName: "Traversal Using Relays around NAT"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/turn/"
summary: "TURN je protokol, který umožňuje komunikaci v reálném čase (např. hlas, video) mezi zařízeními za NAT nebo firewally přeposíláním dat přes veřejný server. Slouží jako záložní řešení, když jsou přímá p"
---

TURN je protokol, který přeposílá data prostřednictvím veřejného serveru, aby umožnil komunikaci v reálném čase mezi zařízeními za NAT nebo firewally, když jsou přímé peer-to-peer spojení blokována.

## Popis

Traversal Using Relays around [NAT](/mobilnisite/slovnik/nat/) (TURN) je síťový protokol navržený k usnadnění komunikace s multimédii v reálném čase, jako je VoIP a videokonference, mezi koncovými body, které jsou za zařízeními pro překlad síťových adres (NAT) nebo restriktivními firewally. Funguje jako rozšíření protokolu STUN (Session Traversal Utilities for NAT) a využívá TURN server jako zprostředkující přeposílač ve veřejném internetu. Když je přímá peer-to-peer konektivita nemožná kvůli symetrickým NAT nebo politikám firewallu, TURN umožňuje koncovým bodům navázat spojení odesíláním všech dat přes TURN server, který přeposílá provoz mezi stranami. Protokol je standardizován [IETF](/mobilnisite/slovnik/ietf/) ([RFC](/mobilnisite/slovnik/rfc/) 5766, aktualizováno RFC 8656) a je široce používán ve frameworkech 3GPP IMS (IP Multimedia Subsystem) a WebRTC pro spolehlivé navázání relace.

Z architektonického hlediska nasazení TURN zahrnuje TURN klienty (např. uživatelská zařízení s komunikačními aplikacemi), TURN servery (veřejně přístupné přeposílací uzly) a protistrany (peer endpoints). TURN klient nejprve objeví TURN server pomocí STUN mechanismů, poté na serveru prostřednictvím TURN Allocate požadavku přidělí přeposílanou transportní adresu (IP adresu a port). Tato adresa je sdílena s protistranou pomocí signalizačních protokolů, jako je [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), což umožňuje protistraně odesílat data na přeposílací adresu. TURN server přeposílá příchozí pakety od protistrany klientovi a naopak pomocí zpráv ChannelData nebo indikací Send/Data. Mezi klíčové komponenty patří správa životnosti alokace, oprávnění pro kontrolu toho, které protistrany mohou odesílat data, a ochrana integrity pomocí autentizace zpráv.

Při provozu TURN spolupracuje s [ICE](/mobilnisite/slovnik/ice/) (Interactive Connectivity Establishment) k určení optimální síťové cesty. Během shromažďování kandidátů ICE poskytuje TURN server přeposílací kandidáty, kteří mají nižší prioritu než hostitelské nebo server-reflexivní kandidáty ze STUN. Pokud přímá nebo NATem asistovaná spojení selžou, ICE přejde k použití TURN přeposílače, čímž zajistí konektivitu za cenu zvýšené latence a zatížení serveru. TURN podporuje transporty přes [UDP](/mobilnisite/slovnik/udp/) i TCP (včetně zabezpečených [TLS](/mobilnisite/slovnik/tls/)) s mechanismy pro řízení zahlcení a správu šířky pásma. V sítích 3GPP jsou TURN servery často nasazovány jako součást architektury IMS, specifikované v TS 23.334 pro interoperabilitu s WebRTC, aby byla zaručena kontinuita služeb pro hlasové a video hovory napříč různými síťovými prostředími.

## K čemu slouží

TURN byl vytvořen, aby vyřešil kritický problém průchodu přes [NAT](/mobilnisite/slovnik/nat/) a firewally pro protokoly komunikace v reálném čase, které často selhávají v peer-to-peer režimu kvůli restriktivním síťovým politikám. S růstem používání internetu v 2000. letech se NAT staly všudypřítomnými pro šetření IPv4 adresami, ale narušily end-to-end konektivitu skrýváním privátních IP adres. Zatímco STUN dokázal zvládnout mnoho typů NAT objevením veřejných adres, selhal se symetrickými NAT, kde mapování portů je jedinečné pro každý cíl. Firewally dále blokovaly nevyžádaný příchozí provoz, čímž zabraňovaly přímým mediálním proudům. TURN tyto limity řešil poskytnutím garantované přeposílací cesty, což zajišťovalo, že aplikace jako VoIP a videokonference mohou spolehlivě fungovat ve všech síťových scénářích.

Motivace pro TURN vzešla z práce IETF na ICE a WebRTC s cílem standardizovat záložní mechanismus pro nejhorší případy konektivity. V 3GPP získal TURN na významu s přijetím IMS pro multimediální služby a WebRTC pro komunikaci z prohlížeče, počínaje Release 7. Vyřešil problémy interoperability mezi mobilními sítěmi (často za carrier-grade NAT) a externími internetovými koncovými body, což umožnilo bezproblémové služby jako VoLTE a video hovory. Přeposíláním provozu přes řízený server také TURN nabízí operátorům bod pro správu provozu a vynucování zabezpečení, i když ve srovnání s přímými spojeními zavádí dodatečnou latenci a náklady na zdroje.

## Klíčové vlastnosti

- Přidělení přeposílané transportní adresy na veřejném serveru pro průchod přes NAT/firewall
- Podpora transportů přes UDP, TCP a TLS pro vyhovění různým síťovým politikám
- Integrace s frameworkem ICE jako kandidát s nižší prioritou pro záložní konektivitu
- Mechanismus oprávnění pro omezení přeposílání dat na autorizované koncové body protistran
- Správa životnosti alokací s obnovovacími mechanismy pro šetření zdrojů
- Integrita zpráv a autentizace pomocí zabezpečení založeného na STUN (např. dlouhodobé přihlašovací údaje)

## Související pojmy

- [ICE – Interactivity Connectivity Establishment](/mobilnisite/slovnik/ice/)
- [NAT – Network Address Translation](/mobilnisite/slovnik/nat/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.506** (Rel-19) — Real-Time Media Communication Architecture for 5G
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [TURN na 3GPP Explorer](https://3gpp-explorer.com/glossary/turn/)
