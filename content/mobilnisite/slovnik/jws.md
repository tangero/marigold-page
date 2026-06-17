---
slug: "jws"
url: "/mobilnisite/slovnik/jws/"
type: "slovnik"
title: "JWS – JSON Web Signature"
date: 2026-01-01
abbr: "JWS"
fullName: "JSON Web Signature"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/jws/"
summary: "JSON Web Signature (JWS) je standard pro digitální podepisování JSON dat za účelem zajištění integrity a autenticity. V sítích 3GPP se používá k podepisování zpráv a tokenů, čímž ověřuje, že obsah neb"
---

JWS je standard pro digitální podepisování JSON dat za účelem zajištění integrity a autenticity, používaný v sítích 3GPP k ověření nezměněného obsahu z důvěryhodných zdrojů pro zabezpečenou komunikaci API a autentizaci.

## Popis

[JSON](/mobilnisite/slovnik/json/) Web Signature (JWS) je mechanismus pro zabezpečení JSON dat prostřednictvím digitálních podpisů, který poskytuje integritu, autenticitu a nepopiratelnost. V rámci specifikací 3GPP se JWS používá k podepisování různých datových bloků, jako jsou JSON Web Tokens ([JWT](/mobilnisite/slovnik/jwt/)) nebo zprávy [API](/mobilnisite/slovnik/api/), což zajišťuje jejich ochranu proti neoprávněným změnám a možnost ověření příjemci. Objekt JWS se skládá ze tří částí: hlavičky, datové části a podpisu. Hlavička obsahuje metadata popisující podpisový algoritmus (např. RS256 pro RSA se SHA-256 nebo ES256 pro [ECDSA](/mobilnisite/slovnik/ecdsa/) se SHA-256) a volitelně další parametry, jako identifikátory klíčů. Datová část je skutečná data, která mají být podepsána, a může jít o jakýkoli JSON obsah nebo řetězec kódovaný v base64url. Podpis je generován aplikací kryptografického algoritmu specifikovaného v hlavičce na zřetězenou hlavičku a datovou část zakódované v base64url, a to pomocí soukromého klíče. Při přijetí ověřovatel použije odpovídající veřejný klíč k validaci podpisu, čímž potvrdí, že data nebyla modifikována a byla podepsána držitelem soukromého klíče.

V architekturách 3GPP hraje JWS zásadní roli při zabezpečování rozhraní založených na službách (SBI) a autentizačních rámců. Například v sítích 5G Core se JWT používané pro přístupové tokeny nebo identity assertions často podepisují pomocí JWS, aby se zabránilo padělání. Proces zahrnuje, že podepisovatel sestaví JWS serializací hlavičky a datové části, vypočítá podpis a zakóduje všechny komponenty do kompaktního serializačního formátu (tečkou oddělený řetězec) nebo JSON serializačního formátu. To umožňuje efektivní přenos přes protokoly [HTTP](/mobilnisite/slovnik/http/)/2. Ověření vyžaduje parsování JWS, dekódování hlavičky k identifikaci algoritmu a použití veřejného klíče podepisovatele (získaného z důvěryhodného zdroje, jako je certifikační autorita nebo server klíčů) ke kontrole podpisu vůči poskytnutým datům. Tím se zajišťuje, že zprávy mezi síťovými funkcemi – například mezi Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) – jsou autentické a nebyly během přenosu pozměněny.

Integrace JWS v 3GPP zasahuje do více specifikací, včetně těch pro vystavení zabezpečení, edge computing a automatizaci sítí. Podporuje různé algoritmy, aby vyhověla různým bezpečnostním požadavkům a výkonnostním omezením, jako je HMAC se SHA-256 pro scénáře se symetrickými klíči nebo kryptografie eliptických křivek pro efektivní asymetrické podpisy. JWS se často používá spolu s [JWE](/mobilnisite/slovnik/jwe/) pro komplexní zabezpečení, kde může být datová část podepsána pomocí JWS pro integritu a následně zašifrována pomocí JWE pro důvěrnost. Tato kombinace je zvláště důležitá ve scénářích, jako je vystavení síťového API, kde třetí strany interagují se sítěmi 5G a data musí být důvěryhodná i soukromá. Standardizací na JWS zajišťuje 3GPP interoperabilitu mezi dodavateli a systémy, což umožňuje robustní bezpečnostní mechanismy slučitelné s webovými standardy a usnadňuje nasazení zabezpečených, škálovatelných telekomunikačních služeb.

## K čemu slouží

JWS bylo v 3GPP přijato, aby řešilo potřebu spolehlivé integrity dat a autentizace zdroje v komunikacích založených na JSON, které se rozšířily s přechodem na architektury orientované na služby v 4G a 5G. Před jeho zavedením systémy 3GPP primárně spoléhaly na kódy autentizace zpráv (MAC) nebo tradiční digitální podpisy v binárních formátech, které byly méně flexibilní pro RESTful API a vyžadovaly vlastní parsování. Tyto metody často postrádaly standardizaci pro JSON datové bloky, což vedlo k problémům s interoperabilitou a zvýšené složitosti při implementaci zabezpečených výměn mezi síťovými funkcemi a externími entitami. JWS tyto problémy řeší tím, že poskytuje standardizovaný, na JSON nativní způsob podepisování dat, což zajišťuje, že příjemci mohou ověřit původ a integritu zpráv bez proprietárních rozšíření.

Vznik JWS v 3GPP byl motivován rozšířením vystavení sítě a potřebou zabezpečených autentizačních mechanismů v rozvíjejících se případech užití, jako je IoT a edge computing. Jak se sítě otevíraly třetím stranám prostřednictvím API, zvýšilo se riziko manipulace se zprávami nebo falšování, což mohlo vést k přerušení služeb nebo bezpečnostním incidentům. JWS umožňuje podepisování tokenů a požadavků API, což síťovým funkcím umožňuje důvěřovat datům z autentizovaných zdrojů, například v tocích OAuth 2.0 pro delegování přístupu nebo při zabezpečování rozhraní založených na službách v rámci 5G Core. Začleněním JWS do specifikací jako 33.117 a 33.938 využilo 3GPP průmyslové standardy od IETF (RFC 7515) ke zvýšení zabezpečení a současně snížení vývojových nákladů, což zajišťuje, že telekomunikační sítě mohou bezpečně podporovat inovativní služby a splňovat regulační požadavky na ochranu dat.

## Klíčové vlastnosti

- Digitální podepisování JSON dat pro integritu a autenticitu
- Podpora více podpisových algoritmů (např. RS256, ES256, HS256)
- Kompaktní a JSON serializační formáty pro flexibilitu
- Nepopiratelnost prostřednictvím asymetrické kryptografie klíčů
- Kompatibilita s JWT a JWE pro kombinované zabezpečení
- Standardizované parametry hlavičky pro identifikaci algoritmu

## Související pojmy

- [JWE – JSON Web Encryption](/mobilnisite/slovnik/jwe/)
- [JWT – JSON Web Token](/mobilnisite/slovnik/jwt/)

## Definující specifikace

- **TS 29.573** (Rel-19) — PLMN/SNPN Interconnection Interface Stage 3
- **TS 33.117** (Rel-20) — Catalogue of General Security Assurance Requirements
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.517** (Rel-20) — 5G Security Assurance Specification (SCAS)
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [JWS na 3GPP Explorer](https://3gpp-explorer.com/glossary/jws/)
