---
slug: "jose"
url: "/mobilnisite/slovnik/jose/"
type: "slovnik"
title: "JOSE – JavaScript Object Signing and Encryption"
date: 2025-01-01
abbr: "JOSE"
fullName: "JavaScript Object Signing and Encryption"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/jose/"
summary: "Rámec pro zabezpečení dat ve formátu JSON pomocí digitálních podpisů, šifrování a kódů autentizace zpráv (MAC). Ve specifikacích 3GPP se používá v rozhraních založených na službách, například v jádru"
---

JOSE je rámec pro zabezpečení dat ve formátu JSON pomocí digitálních podpisů, šifrování a kódů autentizace zpráv (MAC). Používá se v rozhraních založených na službách (service-based interfaces) 3GPP, jako je jádro 5G sítě, k ochraně API komunikací mezi síťovými funkcemi.

## Popis

JavaScript Object Signing and Encryption (JOSE) je soubor standardů [IETF](/mobilnisite/slovnik/ietf/) (RFC 7515–7519), které definují metody pro bezpečný přenos informací jako objektů [JSON](/mobilnisite/slovnik/json/). Poskytuje kompaktní a v URL bezpečnou reprezentaci dat s podpisem, šifrováním nebo ochranou integrity, což jej činí vhodným pro zabezpečení webových aplikací a [API](/mobilnisite/slovnik/api/). Rámec zahrnuje několik komponent: [JWS](/mobilnisite/slovnik/jws/) (JSON Web Signature) pro digitální podpisy nebo [MAC](/mobilnisite/slovnik/mac/), [JWE](/mobilnisite/slovnik/jwe/) (JSON Web Encryption) pro šifrování, JWK (JSON Web Key) pro reprezentaci klíčů a JWA (JSON Web Algorithms) pro identifikátory algoritmů. V sítích 3GPP je JOSE přijímán především v architekturách založených na službách (SBA), jako je jádro 5G sítě (5GC), k zabezpečení komunikace založené na [HTTP](/mobilnisite/slovnik/http/)/2 mezi síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)).

JOSE funguje tak, že serializuje JSON objekty do kompaktní podoby, často za použití kódování Base64Url, a aplikuje kryptografické operace na základě zadaných algoritmů. Například JWS vytváří podpis nad užitečnými daty (která mohou být libovolná, například JWT nebo prostý JSON) pomocí algoritmů jako HMAC SHA-256 nebo RSA-PSS, čímž vzniká JWS objekt s hlavičkou, užitečnými daty a podpisem. JWE šifruje užitečná data pomocí symetrické nebo asymetrické kryptografie, například AES-GCM nebo RSA-OAEP, což vede k JWE objektu se zašifrovaným obsahem a případně vrstvou pro šifrování klíče. Tyto objekty se přenášejí jako řetězce a lze je snadno vložit do HTTP hlaviček nebo těla.

V kontextu 3GPP je JOSE specifikován v dokumentech jako 29.573 pro bezpečnostní aspekty rozhraní založených na službách. Umožňuje vzájemnou autentizaci, ochranu integrity a důvěrnost pro API volání mezi síťovými funkcemi, například mezi funkcí AMF (Access and Mobility Management Function) a SMF (Session Management Function). Rámec podporuje různé algoritmy, což umožňuje operátorům výběr na základě bezpečnostních požadavků a výkonnostních omezení. JOSE objekty, zejména JWT (JSON Web Tokens), mohou také nést deklarace pro autorizaci, například v tokách OAuth 2.0 používaných pro registraci a zjišťování služeb síťových funkcí.

Klíčové architektonické prvky zahrnují použití JSONu pro flexibilitu a čitelnost pro člověka v kombinaci se silnou kryptografií. JOSE se integruje s TLS pro zabezpečení na transportní vrstvě a přidává ochranu na aplikační vrstvě, která je nezávislá na podkladové síti. To je zásadní v cloudu-nativním prostředí 5G, kde mohou být síťové funkce rozmístěny v různých doménách důvěry. Modularita rámce umožňuje 3GPP specifikovat profily, například povinné algoritmy k implementaci, což zajišťuje interoperabilitu mezi dodavateli při zachování vysokých bezpečnostních standardů pro citlivé síťové signalizační zprávy.

## K čemu slouží

JOSE byl vyvinut, aby řešil absenci standardizované, lehké metody pro zabezpečení dat JSON v webových API a mikroslužbách. Před jeho přijetím systémy často používaly proprietární nebo ad-hoc formáty pro podpisy a šifrování, což vedlo k problémům s interoperabilitou a bezpečnostním zranitelnostem. Vzestup RESTful API a JSONu jako dominantního formátu pro výměnu dat si vyžádal konzistentní rámec, který by mohl poskytovat kryptografické záruky bez složitých binárních kódování.

V sítích 3GPP byl přechod na architekturu založenou na službách (SBA) v jádru 5G sítě hlavní motivací pro zavedení JOSE v Release 15. Předchozí generace spoléhaly na specifické protokolové zabezpečení, jako je IPsec nebo Diameter s TLS, ale rozhraní 5G založená na HTTP/2 vyžadovala flexibilnější mechanismus zabezpečení na aplikační úrovni. JOSE řeší problémy jako zabezpečení servisních zpráv mezi distribuovanými síťovými funkcemi, umožňuje jemně odstupňovanou správu přístupu a podporuje bezstavovou autentizaci s tokeny. Doplněk zabezpečení na transportní vrstvě tím, že poskytuje end-to-end ochranu, která přetrvává přes prostředníky.

Historický kontext zahrnuje rostoucí využití JSON Web Tokens (JWT) v OAuth 2.0 a OpenID Connect, což 3GPP využilo pro autorizaci služeb. Schopnost JOSE zpracovat podepisování i šifrování v kompaktním formátu jej učinila ideálním pro nízkolatenční signalizaci 5G s velkým objemem dat. Řeší omezení předchozích přístupů tím, že nabízí možnost výměny algoritmů, snižuje velikost přenášených dat ve srovnání se standardy založenými na XML, jako je XML Signature a Encryption, a je v souladu s moderními webovými standardy. To zajišťuje, že 5G sítě se mohou bezpečně propojovat s internetovými službami a cloudovými platformami a podporovat inovace jako vystavení síťových funkcí a edge computing.

## Klíčové vlastnosti

- Standardizované formáty založené na JSON pro podpisy (JWS) a šifrování (JWE)
- Podpora více kryptografických algoritmů (např. RSA, ECDSA, AES) prostřednictvím JWA
- Kompaktní a v URL bezpečná reprezentace využívající kódování Base64Url
- Integrace s JWT pro autentizaci a autorizaci založenou na tokenech
- Reprezentace a správa klíčů prostřednictvím JWK (JSON Web Key)
- Možnost výměny algoritmů umožňující budoucí bezpečnostní aktualizace

## Související pojmy

- [JWT – JSON Web Token](/mobilnisite/slovnik/jwt/)

## Definující specifikace

- **TS 29.573** (Rel-19) — PLMN/SNPN Interconnection Interface Stage 3

---

📖 **Anglický originál a plná specifikace:** [JOSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/jose/)
