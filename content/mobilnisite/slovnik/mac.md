---
slug: "mac"
url: "/mobilnisite/slovnik/mac/"
type: "slovnik"
title: "MAC – Message Authentication Code"
date: 2025-01-01
abbr: "MAC"
fullName: "Message Authentication Code"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mac/"
summary: "Kryptografický kontrolní součet používaný v rámci autentizačního a dohodovacího protokolu (AKA) 3GPP k ověření integrity dat a autentizaci sítě vůči uživatelskému zařízení. Je klíčovou součástí autent"
---

MAC je kryptografický kontrolní součet používaný v autentizačním protokolu 3GPP k ověření integrity dat a autentizaci sítě vůči uživatelskému zařízení.

## Popis

V zabezpečení 3GPP je Message Authentication Code (MAC) klíčový prvek generovaný během procedury Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). Konkrétně se jedná o MAC obsažený v autentizačním tokenu ([AUTN](/mobilnisite/slovnik/autn/)), který síť zasílá uživatelskému zařízení (UE) pro vzájemnou autentizaci. MAC je vypočítán autentizačním centrem (AuC) sítě pomocí kryptografického algoritmu f1 (nebo jeho varianty f1* pro 5G AKA) se vstupy tajného klíče K (sdíleného s [USIM](/mobilnisite/slovnik/usim/) v UE), náhodné výzvy [RAND](/mobilnisite/slovnik/rand/), pořadového čísla [SQN](/mobilnisite/slovnik/sqn/) a pole pro správu autentizace ([AMF](/mobilnisite/slovnik/amf/)). Vzorec je MAC = f1_K(SQN || RAND || AMF).

Architektura zahrnuje Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/))/AuC v jádru sítě, který generuje autentizační vektor obsahující RAND, AUTN (který zahrnuje MAC a další pole), [XRES](/mobilnisite/slovnik/xres/) a relací klíče. AUTN je odeslán do obslužné sítě (např. MME v 4G, AMF v 5G), která přepošle RAND a AUTN k UE. Po přijetí USIM v UE nezávisle vypočítá očekávaný MAC (XMAC) pomocí stejného algoritmu f1, svého sdíleného klíče K a přijatých hodnot RAND, SQN a AMF. USIM poté porovná vypočítaný XMAC s hodnotou MAC extrahovanou z přijatého AUTN. Pokud se shodují, dokazuje to UE, že autentizační vektor byl vygenerován entitou disponující správným tajným klíčem K, čímž je síť autentizována. Neshoda indikuje potenciální bezpečnostní hrozbu a autentizace selže.

Fungování je hluboce spojeno s cílem vzájemné autentizace protokolu AKA. Zařazení MAC do AUTN umožňuje UE ověřit legitimitu sítě před pokračováním. Chrání proti útokům padělání; útočník nemůže bez znalosti K sestavit platný AUTN. Výpočet MAC je jednosměrný a kryptograficky silný, což zajišťuje, že i když jsou RAND a AUTN zachyceny, nelze odvodit tajný klíč. Jeho role je zásadní pro navázání důvěryhodné relace, protože úspěšná validace MAC je předpokladem pro to, aby UE vypočítalo relaci klíče (CK, IK) a očekávanou odpověď sítě (RES), čímž dokončí handshake vzájemné autentizace. Tento mechanismus se používá napříč 3G (UMTS), 4G (EPS-AKA) a 5G (5G AKA, EAP-AKA').

## K čemu slouží

Message Authentication Code v rámci AKA byl vytvořen, aby poskytl explicitní autentizaci sítě vůči uživatelskému zařízení a řešil tak bezpečnostní slabinu staršího systému 2G (GSM). V GSM autentizovala síť pouze mobilní stanici (jednosměrná autentizace), což ji činilo zranitelnou vůči útokům falešných základnových stanic ("IMSI catchers"), kdy podvodná síť mohla vydávat za legitimní. Zavedení vzájemné autentizace v 3GPP UMTS bylo zásadním bezpečnostním vylepšením a MAC je mechanismus, který umožňuje UE ověřit síť.

Problém, který řeší, je prokázání autenticity sítě vůči UE v kontextu sdíleného tajného klíče. Bez MAC by UE nedokázalo rozlišit legitimní síť a útočníka vysílajícího zachycený RAND. MAC, odvozený ze sdíleného tajemství K a dalších parametrů čerstvosti (SQN, RAND), tento důkaz poskytuje. Jeho vytvoření bylo motivováno potřebou silnějšího zabezpečení s tím, jak mobilní sítě začaly přenášet citlivá data a transakce. Řeší omezení jednosměrné autentizace tím, že zajišťuje ověření obou stran v komunikaci, čímž vytváří základ pro bezpečnou derivaci klíčů a chrání před útoky typu man-in-the-middle a replay. Tím byl vytvořen důvěryhodný základ pro všechny následující bezpečnostní architektury 3GPP.

## Klíčové vlastnosti

- Generován pomocí kryptografického algoritmu f1 (nebo f1*) se sdíleným tajným klíčem K
- Vložen do autentizačního tokenu (AUTN) odesílaného ze sítě k UE
- Umožňuje ověření autenticity sítě na straně UE během AKA
- Používá vstupy včetně pořadového čísla (SQN), náhodné výzvy (RAND) a AMF pro zajištění čerstvosti
- Kritický pro dosažení vzájemné autentizace v systémech 3G, 4G a 5G
- Selhání porovnání MAC vede k zamítnutí autentizace a případnému spuštění procedury pro selhání synchronizace

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [AUTN – Authentication Token](/mobilnisite/slovnik/autn/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.369** (Rel-19) — AIoT NAS protocol for 5G System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- … a dalších 83 specifikací

---

📖 **Anglický originál a plná specifikace:** [MAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mac/)
