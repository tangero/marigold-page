---
slug: "wwsf"
url: "/mobilnisite/slovnik/wwsf/"
type: "slovnik"
title: "WWSF – WebRTC Web Server Function"
date: 2025-01-01
abbr: "WWSF"
fullName: "WebRTC Web Server Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wwsf/"
summary: "Síťová funkce, která umožňuje službám reálného času založeným na WebRTC integraci se sítěmi 3GPP. Funguje jako prostředník, který překládá mezi protokoly WebRTC a systémy založenými na IMS/SIP, což um"
---

WWSF je síťová funkce, která umožňuje službám WebRTC integraci se sítěmi 3GPP tím, že překládá mezi protokoly WebRTC a systémy IMS/SIP pro telekomunikační hovory.

## Popis

WebRTC Web Server Function (WWSF) je základní síťový prvek definovaný ve specifikacích 3GPP, počínaje Release 12, který slouží jako most mezi klienty Web Real-Time Communication (WebRTC) a tradičními sítěmi IP Multimedia Subsystem (IMS) 3GPP. WebRTC je soubor [API](/mobilnisite/slovnik/api/) a protokolů, které umožňují přenos zvuku, videa a dat v reálném čase přímo ve webových prohlížečích bez nutnosti pluginů. WebRTC však používá jiné signalizační a mediální protokoly než IMS, které je založeno na [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) a souvisejících standardech. WWSF tuto nekompatibilitu řeší tím, že funguje jako brána nebo adaptační funkce, která překládá signalizaci WebRTC (často přes WebSocket nebo [HTTP](/mobilnisite/slovnik/http/)) do zpráv SIP a naopak a v případě potřeby zajišťuje i propojení médií.

Architektonicky je WWSF umístěna v servisní vrstvě sítě 3GPP a často komunikuje s komponentami jádra IMS, jako jsou Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a Application Servers ([AS](/mobilnisite/slovnik/as/)). Je specifikována v několika technických specifikacích 3GPP (např. TS 23.334, TS 29.334), které podrobně popisují její rozhraní, procedury a integrační body. WWSF typicky zahrnuje funkční moduly pro převod signalizace, zpracování zabezpečení (např. autentizace a šifrování) a zpracování médií. Může komunikovat s dalšími funkcemi, jako je WebRTC Interworking Function (WIF), pro hlubší adaptaci protokolů. WWSF umožňuje klientům WebRTC – běžícím v prohlížečích nebo nativních aplikacích – registrovat se v síti IMS, zahajovat relace a používat telekomunikační služby, jako by šlo o tradiční koncové body IMS.

Při provozu, když se klient WebRTC pokusí přistoupit ke službě (např. uskutečnit hlasový hovor), připojí se k WWSF přes zabezpečené webové protokoly ([HTTPS](/mobilnisite/slovnik/https/)/WebSocket). WWSF autentizuje uživatele, často využívá přihlašovací údaje 3GPP jako [IMSI](/mobilnisite/slovnik/imsi/) nebo GBA (Generic Bootstrapping Architecture), a převede signalizaci WebRTC (používající např. JavaScript Session Establishment Protocol) do zpráv SIP, které jsou předány do jádra IMS. Pro média může WWSF fungovat jako back-to-back user agent (B2BUA), převádějící mezi protokolem SRTP (Secure Real-time Transport Protocol) WebRTC a mediálními proudy IMS, nebo může po vyjednávání umožnit přímé peer-to-peer mediální cesty. To umožňuje bezproblémovou komunikaci mezi uživateli WebRTC a stávajícími účastníky IMS a podporuje služby jako VoLTE, videohovory a zasílání zpráv.

Klíčové součásti WWSF zahrnují signalizační bránu, řadič mediální brány a bezpečnostní moduly. Její role je klíčová pro rozšíření služeb 3GPP do webového ekosystému, což operátorům umožňuje nabízet pokročilé komunikační služby bez nutnosti instalace speciálních aplikací ze strany uživatelů. Standardizací WWSF zajišťuje 3GPP interoperabilitu mezi webovou komunikací v reálném čase a mobilními sítěmi, čímž podporuje inovace v oblastech jako zákaznický servis využívající WebRTC, kolaborativní aplikace a komunikace IoT. Funkce je navržena jako škálovatelná a bezpečná, v souladu s regulatorními a ochrannými požadavky 3GPP.

## K čemu slouží

WWSF byla představena ve 3GPP Release 12, aby řešila konvergenci webových technologií a telekomunikačních sítí, konkrétně vzestup WebRTC jako standardu pro komunikaci v reálném čase v prohlížeči. Před její definicí aplikace WebRTC fungovaly odděleně od sítí IMS, což omezovalo schopnost operátorů integrovat webové služby se svými základními telekomunikačními nabídkami. Vytvářelo to izolované prostředí, kde weboví uživatelé nemohli snadno využívat funkce jako hlasové služby úrovně operátora, SMS nebo síťovou autentizaci. WWSF to řeší tím, že poskytuje standardizovanou funkci pro vzájemné propojení, což operátorům umožňuje rozšířit služby IMS na jakékoli zařízení podporující WebRTC, a tím zvýšit dosah služeb a snížit závislost na nativních aplikacích.

Historicky komunikace v reálném čase přes web závisela na proprietárních pluginech nebo externím softwaru, což představovalo bezpečnostní rizika a problémy s kompatibilitou. WebRTC se objevilo jako otevřený standard umožňující komunikaci bez pluginů, ale jeho přijetí v telekomunikacích bránil nesoulad protokolů s IMS. WWSF tuto mezeru překlenuje, motivována požadavky operátorů využít stávající investice do IMS a zároveň přijmout webové inovace. Řeší omezení, jako jsou rozdílné signalizační protokoly (WebRTC používá signalizaci založenou na HTTP/WebSocket oproti SIP v IMS) a odlišné bezpečnostní modely (např. DTLS-SRTP ve WebRTC vs. IPSec v IMS).

Definováním WWSF umožňuje 3GPP nové obchodní modely, jako jsou webové hovorové služby, obohacené interakce se zákazníky a bezproblémový přechod mezi webovými a mobilními klienty. Podporuje také dodržování regulatorních požadavků integrací s rámci pro legální odposlech a nouzové služby 3GPP. WWSF v podstatě existuje proto, aby zajistila budoucí připravenost mobilních sítí a jejich schopnost spolupracovat s vyvíjejícím se webovým ekosystémem a poskytovat konzistentní, bezpečné služby komunikace v reálném čase napříč všemi typy přístupu, od 4G přes 5G a dále.

## Klíčové vlastnosti

- Zprostředkovává vzájemné propojení signalizace WebRTC s protokoly IMS/SIP pro bezproblémové navázání relace
- Podporuje autentizaci klientů WebRTC pomocí přihlašovacích údajů 3GPP, jako je IMSI nebo GBA
- Umožňuje vzájemné propojení médií mezi protokolem SRTP WebRTC a mediálními proudy IMS, je-li to vyžadováno
- Poskytuje zabezpečenou komunikaci prostřednictvím TLS/DTLS a integraci s bezpečnostními rámci 3GPP
- Umožňuje vystavení služeb, což dává aplikacím WebRTC přístup k síťovým API a schopnostem
- Standardizována v několika specifikacích 3GPP pro zajištění interoperability a konzistentní implementace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 24.371** (Rel-19) — WebRTC IMS Client Access Specification
- **TS 29.228** (Rel-19) — Cx and Dx Interface Signaling Flows
- **TS 29.229** (Rel-19) — Diameter Protocol for Cx/Dx Interfaces
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.871** (Rel-12) — Security for WebRTC IMS Client Access

---

📖 **Anglický originál a plná specifikace:** [WWSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/wwsf/)
