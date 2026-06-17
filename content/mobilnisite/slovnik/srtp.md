---
slug: "srtp"
url: "/mobilnisite/slovnik/srtp/"
type: "slovnik"
title: "SRTP – Secure Real-time Transport Protocol"
date: 2026-01-01
abbr: "SRTP"
fullName: "Secure Real-time Transport Protocol"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/srtp/"
summary: "SRTP je profil RTP, který poskytuje důvěrnost, ověřování zpráv a ochranu proti přehrání pro datové toky médií v reálném čase, jako je hlas a video. Je základním bezpečnostním protokolem pro VoIP, vide"
---

SRTP je profil Secure Real-time Transport Protocol (protokol pro zabezpečený přenos v reálném čase), který v sítích 3GPP, jako je IMS a 5G, poskytuje důvěrnost, ověřování a ochranu proti přehrání pro média v reálném čase, například hlas a video.

## Popis

Secure Real-time Transport Protocol (SRTP) je standardizovaný protokol 3GPP, který poskytuje bezpečnostní služby pro provoz protokolu Real-time Transport Protocol (RTP) a jeho řídicího protějšku RTCP (zabezpečeného prostřednictvím SRTCP). SRTP je definován jako kryptografický profil RTP, což znamená, že přidává bezpečnostní funkce ke standardnímu formátu paketu RTP bez změny základní struktury hlavičky RTP. Funguje na bázi zpracování jednotlivých paketů a poskytuje zabezpečení typu end-to-end mezi koncovými body médií, jako je UE a Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)) nebo jiné UE při přímé komunikaci.

SRTP funguje tak, že na užitečná data RTP aplikuje kryptografické transformace. Pro důvěrnost šifruje užitečná data pomocí symetrické šifry, obvykle Advanced Encryption Standard ([AES](/mobilnisite/slovnik/aes/)) v režimu Counter Mode (AES-CM). Tento režim je zvolen proto, že generuje šifrovací proud, který lze aplikovat pomocí bitového XOR, což je efektivní a odolné vůči chybám – jediná chyba v šifrovém textu poškodí pouze odpovídající bit v otevřeném textu. Pro ověřování a integritu připojuje SRTP ke každému paketu kód pro ověření zprávy (Message Authentication Code – [MAC](/mobilnisite/slovnik/mac/)), vypočítaný pomocí klíčované hašovací funkce jako HMAC-SHA1. Tento MAC pokrývá hlavičku RTP, užitečná data a index paketu. Klíčovým mechanismem je použití postupného indexu paketů (odvozeného z pořadového čísla RTP) a hlavního klíče pro generování jedinečných relakových klíčů pro šifrování a ověřování každého paketu, což zabraňuje opakovanému použití klíče.

Z architektonického hlediska se SRTP spoléhá na externí protokol pro správu klíčů (např. [MIKEY](/mobilnisite/slovnik/mikey/), [DTLS-SRTP](/mobilnisite/slovnik/dtls-srtp/) nebo dodání klíče specifické pro 3GPP od jádra sítě) k vytvoření sdíleného bezpečnostního kontextu mezi koncovými body. Tento kontext zahrnuje hlavní klíč, hlavní sůl, kryptografickou sadu a čítače přetečení indexu SRTP/SRTCP. Vrstva zpracování SRTP je typicky implementována v rámci mediálního zásobníku. Při odesílání médií jsou užitečná data RTP zašifrována, vypočítán a připojen ověřovací štítek a výsledný paket SRTP je odeslán přes UDP/IP. Příjemce provádí inverzní operace: ověří ověřovací štítek pomocí seznamu přehrání pro ochranu proti přehrání a poté dešifruje užitečná data. V sítích 3GPP je SRTP povinný pro ochranu mediálních toků ve službách založených na IMS, jako jsou VoLTE, ViLTE a Rich Communication Services (RCS), což zajišťuje soukromí a integritu pro miliony komunikací v reálném čase.

## K čemu slouží

SRTP byl vyvinut za účelem řešení závažných bezpečnostních nedostatků standardního protokolu RTP, který přenáší média v otevřené podobě. Když telekomunikace přešly na plně IP sítě s IMS standardu 3GPP, stal se hlas a video zranitelným vůči odposlechu, manipulaci a útokům přehráním přes nedůvěryhodné IP sítě, jako je veřejný internet. Účelem SRTP je poskytnout standardizovanou, efektivní a povinnou bezpečnostní vrstvu speciálně navrženou pro jedinečná omezení médií v reálném čase: nízkou latenci, toleranci ke ztrátě paketů a vysokou frekvenci paketů.

Vytvoření SRTP v rámci ekosystému 3GPP bylo motivováno potřebou řešení, které by mohlo být všudypřítomně nasazeno napříč zařízeními a sítěmi, aniž by narušilo stávající aplikace založené na RTP. Předchozí zabezpečení na síťové úrovni (např. [IPsec](/mobilnisite/slovnik/ipsec/)) bylo často příliš těžkopádné, složité na správu end-to-end a mohlo zavádět nepřijatelnou latenci nebo nekompatibilitu s překladem síťových adres ([NAT](/mobilnisite/slovnik/nat/)). SRTP tyto problémy řeší tím, že funguje na aplikační vrstvě, přidává minimální režii (typicky 4–10 bajtů pro ověřovací štítek a 4 bajty pro index) a používá šifry vhodné pro streamovaná média. Umožňuje zabezpečené komerční služby VoIP a videa, chrání soukromí uživatelů a umožňuje operátorům splnit regulační požadavky na zabezpečení komunikace, čímž tvoří základ pro důvěryhodné doručování multimédií v 4G a 5G.

## Klíčové vlastnosti

- Poskytuje důvěrnost pro užitečná dat médií RTP pomocí efektivních proudových šifer, jako je AES v režimu Counter Mode (AES-CM)
- Zajišťuje ověřování zpráv a integritu pro celé pakety RTP pomocí klíčovaného kódu pro ověření zprávy (Message Authentication Code – MAC)
- Obsahuje vestavěnou ochranu proti přehrání prostřednictvím mechanismu indexu paketů a seznamu přehrání
- Definován jako profil RTP, zachovává kompatibilitu se stávající infrastrukturou RTP a mezilehlými zařízeními
- Používá mechanismus odvozeného klíče ke generování jedinečných šifrovacích a ověřovacích klíčů pro každý paket z hlavního klíče
- Povinný pro ochranu mediálních toků ve službách IMS standardu 3GPP (např. VoLTE, ViLTE) a dalších paketově přepínaných multimediálních aplikacích

## Související pojmy

- [MIKEY – Multimedia Internet KEYing](/mobilnisite/slovnik/mikey/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [DTLS-SRTP – DTLS Extension to Establish Keys for SRTP](/mobilnisite/slovnik/dtls-srtp/)

## Definující specifikace

- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 26.179** (Rel-19) — Codecs and Media Handling for MCPTT
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.281** (Rel-19) — MCVideo Codecs and Media Handling
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TR 26.812** (Rel-18) — Technical Report
- **TS 26.822** (Rel-19) — 5G RTP Configurations Study Phase 2
- **TS 26.880** (Rel-14) — MBMS Enhancements for Mission Critical Video
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [SRTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/srtp/)
