---
slug: "iq"
url: "/mobilnisite/slovnik/iq/"
type: "slovnik"
title: "IQ – IMS Access Gateway to P-CSCF Reference Point"
date: 2025-01-01
abbr: "IQ"
fullName: "IMS Access Gateway to P-CSCF Reference Point"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iq/"
summary: "Referenční bod IQ je standardizované rozhraní mezi funkcí Proxy-Call Session Control Function (P-CSCF) v jádru IMS a bránou přístupu k IMS (IMS Access Gateway). Umožňuje přenos signalizace SIP a médií"
---

IQ je standardizované rozhraní 3GPP mezi P-CSCF a bránou přístupu k IMS (IMS Access Gateway) pro přenos signalizace SIP a médií přes přístupové sítě mimo 3GPP, jako je Wi-Fi.

## Popis

Referenční bod IQ je klíčové rozhraní v architektuře 3GPP IMS (IP Multimedia Subsystem), které je specificky definováno pro scénáře, kdy uživatelské zařízení (UE) přistupuje ke službám IMS přes IP přístupovou síť mimo 3GPP. Spojuje bránu přístupu k IMS ([AGW](/mobilnisite/slovnik/agw/)), která slouží jako vstupní bod z nedůvěryhodného přístupu mimo 3GPP, s funkcí Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), což je první kontaktní bod v důvěryhodné jádrové síti IMS. Hlavní úlohou rozhraní IQ je poskytovat zabezpečenou a řízenou cestu pro signalizaci SIP (Session Initiation Protocol) a související mediální toky.

Z protokolového hlediska přenáší referenční bod IQ zprávy SIP přes UDP, TCP nebo TLS. Pokud je vyžadována bezpečnost, je pro ochranu signalizace SIP mezi AGW a P-CSCF povinně použito TLS. Rozhraní také zprostředkovává vyjednávání a navazování mediálních toků. Klíčovou funkcí umožněnou přes IQ je překonávání zařízení pro překlad síťových adres ([NAT](/mobilnisite/slovnik/nat/)) a firewallů, která se běžně vyskytují v pevných a veřejných Wi-Fi sítích. Brána přístupu k IMS (IMS Access Gateway) často zahrnuje funkce Session Border Controller (SBC), včetně aplikačních bran SIP (SIP ALG) a podpory Interactive Connectivity Establishment ([ICE](/mobilnisite/slovnik/ice/)), aby toto překonávání NAT usnadnila a zajistila, že média mohou proudit přímo nebo přes přenosové uzly mezi UE a sítí IMS.

Z provozního hlediska, když se UE připojí přes přístupovou síť mimo 3GPP (např. přes domácí Wi-Fi router), zjistí adresu P-CSCF, která je často poskytována prostřednictvím [DHCP](/mobilnisite/slovnik/dhcp/) nebo jiných přístupově specifických metod. UE poté odešle svou zprávu SIP REGISTER a následné zprávy INVITE směrem k této P-CSCF. Tyto zprávy procházejí přes bránu přístupu k IMS (IMS Access Gateway) prostřednictvím rozhraní IQ. AGW může před přeposláním SIP dialogu k P-CSCF provést počáteční filtrování, vynucování politik a bezpečnostní kontroly. Pro média může AGW fungovat jako přenosový uzel pro média nebo jednoduše umožnit, aby jimi média protékala, v závislosti na topologii sítě a konfiguraci NAT/firewallů. Tato architektura umožňuje plynulou kontinuitu služeb, jako je Voice over Wi-Fi (VoWiFi), kdy lze hovor iniciovat nebo přijímat ve Wi-Fi síti se stejnou identitou a servisní logikou jako v LTE rádiové síti.

## K čemu slouží

Rozhraní IQ bylo zavedeno, aby vyřešilo zásadní výzvu: rozšíření služeb založených na IMS, zejména hlasu a zasílání zpráv, na zařízení připojená přes necelaulární IP sítě. Před jeho standardizací byl přístup k IMS většinou omezen na paketovou doménu definovanou 3GPP (např. přes [GPRS](/mobilnisite/slovnik/gprs/), [HSPA](/mobilnisite/slovnik/hspa/) nebo LTE). Operátoři však chtěli využít všudypřítomné sítě Wi-Fi a pevné širokopásmové sítě k odlehčení přenosů, zlepšení vnitřního pokrytí a vytvoření konvergentních služeb. Veřejný internet a privátní pevné sítě přinesly nové výzvy, které se v řízeném přístupu 3GPP nevyskytovaly, konkrétně všudypřítomný [NAT](/mobilnisite/slovnik/nat/), různorodé politiky firewallů a nedostatek inherentní důvěry.

Vytvoření referenčního bodu IQ spolu s funkční entitou brány přístupu k IMS (IMS Access Gateway) poskytlo standardizované řešení. Definovalo jasnou architektonickou hranici a specifikace rozhraní pro bezpečnou integraci těchto nedůvěryhodných přístupových sítí do jádra IMS. Tím byla vyřešena problematika překonávání NAT a firewallů pro toky SIP a RTP/RTCP, což je zásadní pro navazování obousměrných mediálních relací. Také to operátorům umožnilo aplikovat konzistentní ověřování, autorizaci a řízení politik (prostřednictvím rozhraní Rx k PCRF) bez ohledu na přístupovou technologii. Rozhraní IQ se tak stalo klíčovým prvkem pro VoWiFi a další služby IMS přes přístup mimo 3GPP a vytvořilo základní kámen strategie Fixed-Mobile Convergence (FMC) 3GPP.

## Klíčové vlastnosti

- Standardizovaný přenos signalizace SIP mezi přístupovými sítěmi mimo 3GPP a jádrem IMS
- Podpora zabezpečeného přenosu pomocí TLS k ochraně zpráv SIP
- Umožňuje překonávání NAT a firewallů pro signalizaci i mediální toky
- Umožňuje vynucování politik a řízení služeb pro relace IMS pocházející z nedůvěryhodného přístupu
- Klíčová architektonická komponenta pro zajištění Voice over Wi-Fi (VoWiFi) a dalších služeb IMS přes pevnou širokopásmovou síť
- Spolupracuje s funkcemi brány přístupu k IMS (IMS Access Gateway), které často zahrnují schopnosti SBC

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [AGW – Access Gateway](/mobilnisite/slovnik/agw/)

## Definující specifikace

- **TS 29.079** (Rel-19) — Optimal Media Routeing (OMR) Procedures
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [IQ na 3GPP Explorer](https://3gpp-explorer.com/glossary/iq/)
