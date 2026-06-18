---
slug: "srtp-mk"
url: "/mobilnisite/slovnik/srtp-mk/"
type: "slovnik"
title: "SRTP-MK – Secure Real-time Transport Protocol Master Key"
date: 2025-01-01
abbr: "SRTP-MK"
fullName: "Secure Real-time Transport Protocol Master Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/srtp-mk/"
summary: "SRTP Master Key je kryptografický klíč používaný k odvozování relačních klíčů pro šifrování a autentizaci mediálních streamů v sítích 3GPP. Zajišťuje důvěrnost a integritu komunikace v reálném čase, j"
---

SRTP-MK je kryptografický hlavní klíč používaný v sítích 3GPP k odvozování relačních klíčů pro šifrování a autentizaci mediálních streamů v reálném čase, čímž zajišťuje důvěrnost a integritu služeb, jako jsou VoLTE a VoNR.

## Popis

SRTP-MK (Secure Real-time Transport Protocol Master Key) je základní bezpečnostní parametr v rámci architektury 3GPP pro ochranu provozu v mediální rovině. Jedná se o symetrický kryptografický klíč, typicky o délce 128 nebo 256 bitů, který slouží jako kořenové tajemství pro konkrétní mediální relaci. Tento hlavní klíč není používán přímo pro šifrování nebo autentizaci paketů. Místo toho je spolu s dalšími parametry, jako je [SRTP](/mobilnisite/slovnik/srtp/) Master Salt ([SRTP-MS](/mobilnisite/slovnik/srtp-ms/)), vstupem do funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)) definované v [RFC](/mobilnisite/slovnik/rfc/) 3711 a přijaté standardem 3GPP. KDF generuje sadu relačně specifických klíčů, včetně šifrovacího klíče, autentizačního klíče a solícího klíče pro SRTP a jeho řídicí protokol [SRTCP](/mobilnisite/slovnik/srtcp/). Tento proces zajišťuje, že každá mediální relace používá unikátní kryptografické klíče, čímž se omezuje dopad případného prolomení klíče.

Z architektonického hlediska je SRTP-MK generován a distribuován bezpečnostními funkcemi jádra sítě. V IP Multimedia Subsystem (IMS) je SRTP-MK typicky navázán během signalizace při sestavování relace, například prostřednictvím protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)). Může být přenášen bezpečně pomocí mechanismů jako Key Management Extensions for SDP (SDES) nebo, což je v 3GPP běžnější, prostřednictvím integrace se základní přístupovou bezpečností. Například v EPS a 5GS lze klíče z bezpečnosti přístupové vrstvy (např. Kasme nebo Kamf) použít k odvození SRTP-MK, čímž se vytvoří kryptograficky provázaný řetězec bezpečnosti od rádiového přístupu až k médiím.

Role SRTP-MK je klíčová pro koncové zabezpečení médií mezi uživatelským zařízením (UE) a sítí nebo mezi UE v rámci hovoru. Tvoří základ pro aplikaci standardu [AES](/mobilnisite/slovnik/aes/) (Advanced Encryption Standard) v režimu čítače pro šifrování a HMAC-SHA1 pro autentizaci v rámci SRTP. Správa tohoto klíče – jeho generování, distribuce a životnost – je řízena síťovými prvky, jako je Proxy-Call Session Control Function (P-CSCF) a Media Resource Function (MRF), v koordinaci s řízením politik. Jeho správná implementace je povinná pro kompatibilní nasazení VoLTE a VoNR a zajišťuje, že služby hlasu a videa v reálném čase splňují přísné bezpečnostní a soukromí požadavky moderních telekomunikací.

## K čemu slouží

SRTP-MK byl zaveden, aby poskytl standardizovaný a robustní mechanismus pro zabezpečení mediálních toků v reálném čase v all-IP sítích 3GPP, jako jsou sítě používané pro Voice over LTE (VoLTE) a Voice over NR (VoNR). Před jeho formalizací v 3GPP bylo zabezpečení médií často řešeno ad-hoc nebo vůbec ne, což ponechávalo hlasové a video hovory zranitelné vůči odposlechu a manipulaci na transportní vrstvě IP. Přechod od přepojování okruhů pro hlas, které mělo inherentní fyzickou bezpečnost, k paketově přepínaným IP multimediálním službám vytvořil jasnou potřebu kryptografické ochrany na aplikační vrstvě.

Jeho vytvoření bylo motivováno požadavkem na splnění regulatorních a spotřebitelských požadavků na soukromí komunikace v souladu s širšími průmyslovými standardy, jako je SRTP od IETF. SRTP-MK řeší problém navázání klíče pro mediální relace integrací s existující bezpečnostní architekturou 3GPP. Namísto vytváření zcela samostatného protokolu pro správu klíčů využívá 3GPP klíče a důvěru navázanou během autentizace přístupu k síti (např. prostřednictvím 5G AKA nebo EAP-AKA') k odvození SRTP-MK. Tento přístup poskytuje efektivitu a silné bezpečnostní propojení, které zajišťuje, že pouze autentizovaní uživatelé mohou navázat zabezpečené mediální relace. Řeší tak omezení předchozích přístupů, kdy mohla být média zabezpečena slabými, statickými klíči nebo kde bylo zabezpečení ukončeno na síťovém uzlu, čímž se přerušila ochrana end-to-end.

## Klíčové vlastnosti

- Slouží jako kořenové kryptografické tajemství pro odvozování relačních klíčů SRTP a SRTCP.
- Integrován s přístupovou bezpečností 3GPP pro odvození klíče (např. z výstupu KDF).
- Podporuje délky klíčů 128 a 256 bitů pro šifrování AES.
- Distribuován bezpečně prostřednictvím signalizace IMS (např. v rámci SDP pomocí SDES nebo prostřednictvím kontextu přístupové bezpečnosti).
- Umožňuje unikátní relační klíče pro každý hovor, aby se omezil dopad případného prolomení klíče.
- Základní pro zajištění důvěrnosti a integrity paketů RTP/RTCP.

## Související pojmy

- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)
- [SRTP-MS – Secure Real-time Transport Protocol Master Salt](/mobilnisite/slovnik/srtp-ms/)
- [SRTP-MKI – Secure Real-time Transport Protocol Master Key Identifier](/mobilnisite/slovnik/srtp-mki/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems

---

📖 **Anglický originál a plná specifikace:** [SRTP-MK na 3GPP Explorer](https://3gpp-explorer.com/glossary/srtp-mk/)
