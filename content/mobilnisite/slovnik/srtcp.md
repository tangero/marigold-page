---
slug: "srtcp"
url: "/mobilnisite/slovnik/srtcp/"
type: "slovnik"
title: "SRTCP – Secure Real-time Transport Control Protocol"
date: 2026-01-01
abbr: "SRTCP"
fullName: "Secure Real-time Transport Control Protocol"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/srtcp/"
summary: "SRTCP je zabezpečená verze protokolu Real-time Transport Control Protocol (RTCP). Poskytuje důvěrnost, autentizaci zpráv a ochranu proti opětovnému přehrání pro řídicí provoz multimediálních relací. T"
---

SRTCP je zabezpečená verze protokolu RTCP, která poskytuje důvěrnost, autentizaci a ochranu proti opětovnému přehrání pro řídicí provoz multimediálních relací v sítích jako IMS a 5G.

## Popis

Secure Real-time Transport Control Protocol (SRTCP) je 3GPP definován jako povinný bezpečnostní mechanismus pro ochranu paketů [RTCP](/mobilnisite/slovnik/rtcp/) v rámci IP Multimedia Subsystem (IMS) a dalších paketově přepínaných služeb 3GPP. SRTCP není samostatný protokol, ale kryptografická transformace aplikovaná na standardní pakety RTCP. Funguje ve spojení se Secure Real-time Transport Protocol ([SRTP](/mobilnisite/slovnik/srtp/)) a poskytuje tak kompletní bezpečnostní řešení pro mediální toky [RTP](/mobilnisite/slovnik/rtp/) a s nimi spojený řídicí provoz. Ochrana je aplikována koncově mezi komunikujícími koncovými body, jako je User Equipment (UE) a aplikační servery.

SRTCP funguje tak, že ke každému paketu [RTCP](/mobilnisite/slovnik/rtpcp/) přidá kryptografickou přívěsku. Tato přívěska obsahuje kód autentizace zprávy ([MAC](/mobilnisite/slovnik/mac/)), který je vypočítán z celého paketu RTCP (hlavičky a datové části) pomocí autentizačního klíče. Tím je zajištěna integrita a autentizace zdroje řídicích dat, což brání manipulaci a falšování. Volitelně může SRTCP poskytnout také důvěrnost šifrováním datové části RTCP, i když to je méně časté, protože pakety RTCP typicky obsahují necitlivé statistické informace. Klíčovou vlastností je použití indexu paketu a seznamu již přijatých paketů pro ochranu proti útokům opětovným přehráním, kdy útočník znovu odešle dříve zachycené pakety.

Architektonicky SRTCP spoléhá na bezpečnostní kontext navázaný pomocí protokolů pro správu klíčů, jako je Multimedia Internet KEYing ([MIKEY](/mobilnisite/slovnik/mikey/)) nebo [DTLS-SRTP](/mobilnisite/slovnik/dtls-srtp/). Tento kontext zahrnuje kryptografické klíče (šifrovací klíč, autentizační klíč, salt klíč) a parametry jako kryptografickou sadu (např. AES-CM, HMAC-SHA1). Vrstva zpracování SRTCP se nachází mezi aplikací RTCP a transportní vrstvou sítě. Při odesílání přijme paket RTCP, vygeneruje autentizační značku a připojí index SRTCP a tuto značku. Při příjmu ověří značku a zkontroluje index proti seznamu již přijatých paketů, než předá paket aplikaci RTCP. Jeho role je v sítích 3GPP klíčová pro zabezpečení hlášení o kvalitě služby, identifikace účastníků a zpráv pro řízení relace, čímž chrání celkové řízení multimediální relace.

## K čemu slouží

SRTCP byl vytvořen, aby řešil bezpečnostní zranitelnosti inherentní původnímu, nechráněnému protokolu [RTCP](/mobilnisite/slovnik/rtcp/). RTCP je protokol doprovázející RTP, který přenáší řídicí informace pro multimediální relace, včetně hlášení účastníků, identifikátorů zdroje synchronizace (SSRC) a statistik o ztrátě paketů. Ve své nešifrované podobě je RTCP náchylný k útokům, jako je padělání zpráv, útoky opětovným přehráním a odmítnutí služby prostřednictvím falešných hlášení. Když sítě 3GPP přijaly IMS pro poskytování hlasu, videa a zpráv přes IP, zabezpečení těchto řídicích kanálů se stalo prvořadým pro integritu služby, přesnost účtování a soukromí uživatelů.

Motivace pro SRTCP vychází z potřeby standardizovaného, odlehčeného bezpečnostního mechanismu, který by mohl být aplikován na často malé a časté pakety RTCP bez zavedení nadměrné režie nebo latence. Předchozí přístupy mohly spoléhat na zabezpečení na síťové úrovni, jako je IPsec, ale to je často ukončeno na hranicích sítě a neposkytuje skutečné koncové zabezpečení mezi aplikačními koncovými body. SRTCP jako součást architektury SRTP poskytuje zabezpečení na vrstvě relace specificky přizpůsobené pro provoz v reálném čase. Řeší problém autentizace řídicího provozu způsobem, který je kryptograficky svázán s bezpečnostním kontextem mediálního toku, čímž zajišťuje jednotný bezpečnostní postoj pro celou relaci RTP v rámci all-IP architektury 3GPP.

## Klíčové vlastnosti

- Poskytuje autentizaci zpráv a ochranu integrity pro pakety RTCP pomocí klíčovaného kódu autentizace zprávy (MAC)
- Volitelné šifrování datové části pro důvěrnost řídicích dat RTCP
- Vestavěná ochrana proti opětovnému přehrání pomocí indexu paketu a seznamu již přijatých paketů
- Nízká režie, přidává pouze kryptografickou přívěsku ke každému paketu
- Používá stejný hlavní klíč a kryptografický kontext jako přidružený proud SRTP pro zjednodušenou správu klíčů
- Povinný pro zabezpečení RTCP v 3GPP IMS a dalších paketově přepínaných multimediálních službách

## Související pojmy

- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)
- [RTCP – Real-time Transport Control Protocol](/mobilnisite/slovnik/rtcp/)
- [RTP – Real-time Transport Protocol](/mobilnisite/slovnik/rtp/)
- [MIKEY – Multimedia Internet KEYing](/mobilnisite/slovnik/mikey/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [DTLS-SRTP – DTLS Extension to Establish Keys for SRTP](/mobilnisite/slovnik/dtls-srtp/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.581** (Rel-19) — MCVideo Media Plane Control Protocol Specification
- **TS 26.281** (Rel-19) — MCVideo Codecs and Media Handling
- **TS 26.880** (Rel-14) — MBMS Enhancements for Mission Critical Video
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.246** (Rel-19) — MBMS Security Specification
- **TS 33.879** (Rel-13) — MCPTT Security Study
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [SRTCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/srtcp/)
