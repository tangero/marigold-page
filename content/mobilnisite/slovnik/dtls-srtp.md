---
slug: "dtls-srtp"
url: "/mobilnisite/slovnik/dtls-srtp/"
type: "slovnik"
title: "DTLS-SRTP – DTLS Extension to Establish Keys for SRTP"
date: 2025-01-01
abbr: "DTLS-SRTP"
fullName: "DTLS Extension to Establish Keys for SRTP"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/dtls-srtp/"
summary: "Rozšíření pro správu klíčů, které využívá DTLS handshake k vyjednání kryptografických klíčů pro relace Secure Real-time Transport Protocol (SRTP). Poskytuje end-to-end zabezpečení pro real-time mediál"
---

DTLS-SRTP je rozšíření pro správu klíčů, které využívá DTLS handshake k navázání kryptografických klíčů pro SRTP relace, čímž poskytuje end-to-end zabezpečení pro real-time mediální toky, jako je hlas a video.

## Popis

DTLS-SRTP je protokol pro navázání klíčů, který kombinuje Datagram Transport Layer Security ([DTLS](/mobilnisite/slovnik/dtls/)) se Secure Real-time Transport Protocol ([SRTP](/mobilnisite/slovnik/srtp/)). Jeho hlavní funkcí je provedení autentizované výměny klíčů využitím DTLS handshake za účelem vygenerování hlavního klíče a salt materiálu použitých pro klíčování SRTP a SRTCP kryptografických kontextů. Protokol je definován v [IETF](/mobilnisite/slovnik/ietf/) RFC 5764 a je klíčovým prvkem pro zabezpečení médií v IP Multimedia Subsystem (IMS) dle 3GPP a ve frameworku WebRTC. Funguje rozšířením standardního DTLS handshake: během dokončení handshake si komunikující strany vymění data rozšíření "use_srtp", které uvádí podporované SRTP ochranné profily a volitelně i [MIKEY](/mobilnisite/slovnik/mikey/) keying material.

Architektura zahrnuje dva koncové body mediální relace, například dvě uživatelská zařízení (UE) nebo UE a mediální bránu. Nejprve navážou DTLS asociaci přes stejné UDP porty určené pro následný SRTP mediální tok. DTLS handshake autentizuje koncové body (často pomocí certifikátů) a odvodí hlavní tajemství (master secret). Z tohoto DTLS hlavního tajemství je exportován keying material pro SRTP pomocí funkce pro odvozování klíčů definované v RFC 5705. Tím se získá hlavní klíč SRTP, hlavní sůl (master salt) a rychlost odvozování klíčů, které se následně použijí k inicializaci SRTP kryptografického kontextu pro šifrování a autentizaci RTP/RTCP paketů.

Fungování lze shrnout do sekvence: 1) Vyjednání relace přes SIP/SDP indikuje podporu DTLS-SRTP a otisky (fingerprints) DTLS certifikátů. 2) Iniciující koncový bod vystupuje jako DTLS klient a zahájí handshake na IP adresu a port odpovídající strany. 3) Handshake je dokončen, čímž jsou koncové body autentizovány ověřením certifikátů proti otiskům v SDP. 4) Keying material je exportován z navázané DTLS relace. 5) SRTP a SRTCP toky začnou používat odvozené klíče pro šifrování (např. [AES](/mobilnisite/slovnik/aes/)_[CM](/mobilnisite/slovnik/cm/)_128) a autentizaci (např. HMAC_SHA1_80). Tento mechanismus poskytuje plné end-to-end šifrování médií mezi koncovými body, protože klíče nejsou přístupné mezilehlým síťovým prvkům, jako jsou mediální brány, pokud nejsou speciálně navrženy pro legální odposlech.

## K čemu slouží

DTLS-SRTP byl vytvořen k řešení problému navazování bezpečných klíčů pro [SRTP](/mobilnisite/slovnik/srtp/) relace škálovatelným, standardizovaným a firewall-friendly způsobem. Předchozí metody pro klíčování SRTP, jako například Security Descriptions (SDES) v SDP, přenášely klíče v nešifrované podobě v signalizačních zprávách, což vyžadovalo vysokou míru důvěry a zabezpečení signalizační cesty (např. pomocí [IPsec](/mobilnisite/slovnik/ipsec/)). To bylo významným omezením, zejména v architekturách, kde signalizační zprostředkovatelé neměli mít přístup k mediálním klíčům.

Motivace pro DTLS-SRTP vycházela z požadavku projektu WebRTC na povinné šifrování a z potřeby protokolu pro dohodu klíčů fungujícího peer-to-peer. DTLS bylo přirozenou volbou, protože běží nad UDP (stejně jako RTP/RTCP), dokáže procházet NATy a firewally pomocí ICE a poskytuje silnou autentizaci. Využitím DTLS handshake poskytuje DTLS-SRTP jednotné řešení pro autentizaci datového kanálu (pokud je používán) a navázání mediálních klíčů, čímž zjednodušuje bezpečnostní architekturu. V 3GPP bylo jeho přijetí od Release 12 dále motivováno potřebou robustních, end-to-end zabezpečených hlasových a video služeb přes LTE (VoLTE, ViLTE) a pro integraci WebRTC klientů do ekosystému IMS, což zajišťuje konzistentní a vysokou úroveň zabezpečení pro real-time komunikace.

## Klíčové vlastnosti

- Používá DTLS handshake pro autentizovanou výměnu klíčů přes UDP
- Odvozuje SRTP klíče přímo z DTLS hlavního tajemství (master secret)
- Poskytuje skutečné end-to-end šifrování médií nezávislé na zabezpečení signalizační cesty
- Podporuje vzájemnou autentizaci obvykle prostřednictvím X.509 certifikátů
- Integruje se s mechanismy pro průchod NAT, jako jsou ICE a STUN
- Definuje SRTP ochranné profily pro šifrování AES-CM a AES-GCM

## Související pojmy

- [DTLS – Datagram Transport Layer Security](/mobilnisite/slovnik/dtls/)
- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 33.328** (Rel-19) — IMS Media Plane Security Specification
- **TS 33.871** (Rel-12) — Security for WebRTC IMS Client Access

---

📖 **Anglický originál a plná specifikace:** [DTLS-SRTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtls-srtp/)
