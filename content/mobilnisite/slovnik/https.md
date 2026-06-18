---
slug: "https"
url: "/mobilnisite/slovnik/https/"
type: "slovnik"
title: "HTTPS – Hyper Text Transfer Protocol Secure"
date: 2025-01-01
abbr: "HTTPS"
fullName: "Hyper Text Transfer Protocol Secure"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/https/"
summary: "HTTPS je protokol HTTP/1.1 zabezpečený pomocí SSL/TLS, který pracuje na portu 443. Poskytuje šifrovanou a autentizovanou komunikaci pro webové služby v sítích 3GPP a chrání uživatelská data a integrit"
---

HTTPS je zabezpečená verze protokolu HTTP, která využívá SSL/TLS k poskytnutí šifrované a autentizované komunikace pro webové služby v sítích 3GPP, čímž chrání data mezi uživatelským zařízením (UE) a síťovými funkcemi.

## Popis

Hyper Text Transfer Protocol Secure (HTTPS) je základním protokolem aplikační vrstvy v architekturách 3GPP, konkrétně definovaným jako [HTTP](/mobilnisite/slovnik/http/)/1.1 fungující nad vrstvou Secure Sockets Layer ([SSL](/mobilnisite/slovnik/ssl/)) nebo jejím nástupcem Transport Layer Security ([TLS](/mobilnisite/slovnik/tls/)). V kontextu 3GPP není HTTPS pouze webovým protokolem, ale klíčovým zabezpečeným transportním mechanismem pro mnoho síťových služeb a aplikačních programových rozhraní ([API](/mobilnisite/slovnik/api/)), zejména těch vystavených funkcemi pro vystavení síťových schopností ([NEF](/mobilnisite/slovnik/nef/)) a funkcemi pro vystavení schopností služeb ([SCEF](/mobilnisite/slovnik/scef/)). Vytváří zabezpečený kanál mezi klientem, jako je uživatelské zařízení (UE) nebo externí aplikační server, a síťovým serverem, což zajišťuje, že všechna vyměňovaná data jsou šifrována a autentizována.

Protokol pracuje na dobře definovaném portu, obvykle 443. Zabezpečení je poskytováno podkladovou vrstvou SSL/TLS, která zajišťuje kryptografický handshake, navázání symetrického klíče a průběžné šifrování HTTP dat. Tento handshake zahrnuje autentizaci serveru (a volitelně i autentizaci klienta) pomocí digitálních certifikátů X.509, dohodu kryptografické sady (cipher suite) a generování relakových klíčů. Jakmile je tunel TLS navázán, jsou v tomto šifrovaném kanálu použity standardní metody HTTP (GET, POST, PUT, DELETE) pro přenos dat, provádění procedur nebo získávání informací ze síťových funkcí.

Z architektonického hlediska je HTTPS nedílnou součástí architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) jádra 5G (5GC), kde síťové funkce komunikují prostřednictvím protokolu HTTP/2 s datovými částmi ve formátu [JSON](/mobilnisite/slovnik/json/) nebo Protobuf, vše zabezpečené TLS – což je přímá evoluce principů HTTPS. Pro externí vystavení specifikuje 3GPP HTTPS jako primární metodu pro zabezpečený přístup třetích stran k síťovým schopnostem. Klíčové komponenty v tomto ekosystému zahrnují zásobník TLS implementující protokoly jako TLS 1.2 nebo 1.3, software HTTP klienta a serveru a infrastrukturu veřejných klíčů (PKI) spravující potřebné digitální certifikáty. Jeho úlohou je zaručit důvěrnost, integritu a autentizaci pro transakce webových služeb, což je zásadní pro ochranu soukromí účastníka, zabezpečené provozování, rozhraní pro zákonné odposlechy a integritu síťové signalizace směrem k aplikacím.

## K čemu slouží

HTTPS byl do standardů 3GPP zaveden, aby řešil kritickou potřebu zabezpečení webových rozhraní, která se stávala běžnými pro poskytování služeb a správu sítě. Před jeho formálním přijetím mohly být pro výměnu dat používány proprietární nebo méně bezpečné metody, což otevíralo zranitelnosti vůči odposlechu, manipulaci a útokům typu impersonation. Motivací bylo využít široce přijímaný, robustní a standardizovaný internetový bezpečnostní protokol k ochraně citlivých dat účastníků, příkazů pro konfiguraci sítě a transakcí spojených s poskytováním služeb.

Vytvoření podpory pro HTTPS v rámci 3GPP bylo hnací silou evoluce směrem k IP službám a otevřeným API. Jak se sítě vzdalovaly uzavřeným, okruhově přepínaným paradigmatům ve prospěch architektur plně založených na IP, stala se potřeba univerzálního bezpečnostního mechanismu na aplikační vrstvě zřejmou. HTTPS řeší problém přenosu přihlašovacích údajů, osobních dat a kritických síťových instrukcí přes potenciálně nedůvěryhodné IP sítě. Poskytuje dobře srozumitelný bezpečnostní model, který se bezproblémově integruje s ekosystémem World Wide Web, a umožňuje tak zabezpečené interakce pro služby jako správa zařízení, multimediální zprávy nebo služby založené na poloze. Jeho přijetí standardizuje bezpečnostní postupy napříč různými výrobci a poskytovateli služeb, čímž zajišťuje interoperabilitu a konzistentní bezpečnostní základ.

## Klíčové vlastnosti

- Poskytuje end-to-end šifrování pro datové části HTTP pomocí SSL/TLS
- Pracuje na standardním portu 443 přiděleném IANA
- Podporuje autentizaci serveru prostřednictvím certifikátů X.509
- Umožňuje volitelnou autentizaci klienta pomocí certifikátu pro vzájemný TLS
- Zajišťuje integritu dat a chrání před útoky typu man-in-the-middle
- Základ pro zabezpečená RESTful API v architekturách založených na službách

## Související pojmy

- [TLS – Transport Layer Security](/mobilnisite/slovnik/tls/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [SCEF – Service Capability Exposure Function](/mobilnisite/slovnik/scef/)
- [API – Application Programming Interface](/mobilnisite/slovnik/api/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TS 29.201** (Rel-19) — RESTful Rx Interface for AF-PC Communication
- **TS 29.817** (Rel-12) — Study on XML-based Rx interface for PCC
- **TS 32.583** (Rel-19) — HNB OAM&P Procedure Flows for Type 1 Interface
- **TS 32.593** (Rel-19) — HeNB OAM&P Procedure Flows for Type 1 Interface
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [HTTPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/https/)
