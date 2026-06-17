---
slug: "jwe"
url: "/mobilnisite/slovnik/jwe/"
type: "slovnik"
title: "JWE – JSON Web Encryption"
date: 2025-01-01
abbr: "JWE"
fullName: "JSON Web Encryption"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/jwe/"
summary: "JSON Web Encryption (JWE) je standard pro šifrování a zabezpečení datových přenosových jednotek pomocí struktur založených na JSON. Poskytuje důvěrnost citlivých informací vyměňovaných v API sítí 3GPP"
---

JWE (JSON Web Encryption) je standard pro šifrování datových přenosových jednotek (payloads) pomocí JSON struktur za účelem zajištění důvěrnosti (confidentiality) a integrity citlivých informací vyměňovaných mezi funkcemi sítě 3GPP.

## Popis

[JSON](/mobilnisite/slovnik/json/) Web Encryption (JWE) je datová struktura reprezentující šifrovanou přenosovou jednotku za použití serializace založené na JSON. Je definována v rámci architektury 3GPP pro zabezpečení citlivých dat v [API](/mobilnisite/slovnik/api/) komunikaci, zejména u rozhraní založených na službách (SBI) v 5G jádru sítě (5G Core). JWE funguje tak, že vezme čistý textový přenos (plaintext payload), což mohou být jakákoli data jako například soubor tvrzení (claim set) JSON Web Token ([JWT](/mobilnisite/slovnik/jwt/)) nebo jiné citlivé informace, a zašifruje je pomocí určeného kryptografického algoritmu. Výsledkem tohoto procesu je JWE objekt, který se skládá z několika částí: chráněné hlavičky (protected header), šifrovaného klíče, inicializačního vektoru, šifrového textu (šifrovaného přenosu) a autentizační značky (authentication tag). Chráněná hlavička obsahuje metadata potřebná pro zpracování, jako je šifrovací algoritmus (např. A256GCM pro AES-GCM s 256bitovým klíčem) a metoda správy klíčů (např. RSA-OAEP pro asymetrické šifrování nebo přímé šifrování se symetrickým klíčem). Šifrovaný klíč je šifrovací klíč obsahu (CEK) zašifrovaný veřejným klíčem příjemce nebo sdíleným tajemstvím v závislosti na režimu správy klíčů. Inicializační vektor zajišťuje náhodnost v procesu šifrování, zatímco autentizační značka poskytuje integritu a autentičnost šifrového textu a brání jeho pozměnění.

V systémech 3GPP se JWE používá v rámci protokolů, jako je API funkce pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)), a v bezpečnostních rámcích pro ochranu dat při přenosu. Například když aplikace třetí strany vyžádá uživatelská data prostřednictvím API, odpověď obsahující soukromé informace může být zapouzdřena v JWE, aby bylo zajištěno, že je mohou dešifrovat pouze autorizované entity. Proces dešifrování zahrnuje rozbor JWE objektu, extrakci chráněné hlavičky k určení algoritmů, dešifrování šifrovaného klíče pro získání CEK a následné použití CEK spolu s inicializačním vektorem k dešifrování šifrového textu a ověření autentizační značky. Tento strukturovaný přístup umožňuje flexibilní správu klíčů s podporou symetrické i asymetrické kryptografie a umožňuje interoperabilitu mezi různými systémy prostřednictvím dodržování standardu [IETF](/mobilnisite/slovnik/ietf/) RFC 7516, který 3GPP profiluje pro své specifické případy použití.

Role JWE v ekosystému 3GPP je klíčová pro udržení důvěrnosti dat v architekturách založených na službách, kde síťové funkce komunikují přes rozhraní [HTTP](/mobilnisite/slovnik/http/)/2. Integruje se s dalšími bezpečnostními standardy založenými na JSON, jako jsou JSON Web Signature ([JWS](/mobilnisite/slovnik/jws/)) a JSON Web Token (JWT), a poskytuje tak komplexní bezpečnostní řešení. Například JWT obsahující uživatelská tvrzení může být zašifrován jako JWE pro ochranu jeho obsahu a poté volně podepsán pomocí JWS pro dodatečnou integritu. Tento vrstvený bezpečnostní model je v 5G sítích zásadní pro ochranu před odposlechem a úniky dat, zejména ve scénářích zahrnujících vystavení sítě externím aplikacím nebo roamingové dohody mezi operátory. Standardizací na JWE zajišťuje 3GPP konzistentní zpracování šifrovaných dat napříč různými implementacemi, čímž zvyšuje bezpečnost a zároveň zachovává flexibilitu a škálovatelnost potřebnou pro moderní telekomunikační služby.

## K čemu slouží

JWE byl do 3GPP zaveden, aby řešil rostoucí potřebu robustního šifrování dat v architekturách sítí řízených [API](/mobilnisite/slovnik/api/), zejména s nástupem 5G a jeho jádra založeného na službách. Před jeho přijetím systémy 3GPP spoléhaly na tradiční bezpečnostní mechanismy, jako je IPsec nebo TLS pro zabezpečení přenosové vrstvy, které poskytovaly šifrování kanálu, ale postrádaly podrobné, na úrovni přenosové jednotky zajištěné utajení (confidentiality) pro konkrétní datové prvky. Toto omezení se ukázalo jako problematické, když se sítě vyvíjely směrem k vystavování schopností aplikacím třetích stran a podpoře dynamičtějších interakcí služeb, kde citlivé informace – jako uživatelské identifikátory, polohové údaje nebo podrobnosti o předplatném – potřebovaly ochranu nad rámec přenosové vrstvy. JWE tento problém řeší tím, že umožňuje end-to-end šifrování jednotlivých JSON přenosových jednotek, zajišťuje důvěrnost dat i v případě jejich zachycení během zpracování nebo uložení a umožňuje selektivní šifrování na základě citlivosti obsahu.

Motivace pro JWE v 3GPP vychází z přechodu k cloud-nativním, na mikroslužbách založeným návrhům, kde síťové funkce komunikují prostřednictvím RESTful API. V takových prostředích data často procházejí více zprostředkujícími články nebo jsou ukládána do vyrovnávacích pamětí, což činí šifrování na úrovni přenosu nedostatečným pro komplexní zabezpečení. JWE poskytuje standardizovanou, interoperabilní metodu pro šifrování JSON dat, která je v souladu s osvědčenými postupy odvětví od IETF a umožňuje hladkou integraci s webovými technologiemi. Řeší specifické požadavky 3GPP, jako je ochrana soukromí uživatelů ve scénářích vystavení sítě a zabezpečení citlivých parametrů v autentizačních protokolech. Zařazením JWE do specifikací jako 29.573 a 33.938 zajišťuje 3GPP, že síťová API mohou bezpečně zpracovávat důvěrná data, zmírňují tak rizika spojená s úniky dat a nedodržováním předpisů, a zároveň podporují flexibilní, otevřené architektury klíčové pro inovace v 5G.

## Klíčové vlastnosti

- Šifrování na úrovni přenosové jednotky (payload) pro JSON datové struktury
- Podpora více kryptografických algoritmů (např. AES-GCM, RSA-OAEP)
- Flexibilní režimy správy klíčů (symetrické a asymetrické)
- Ochrana integrity prostřednictvím autentizačních značek (authentication tags)
- Serializace založená na JSON pro interoperabilitu
- Kompatibilita s JWT a JWS pro vrstvené zabezpečení

## Související pojmy

- [JWS – JSON Web Signature](/mobilnisite/slovnik/jws/)
- [JWT – JSON Web Token](/mobilnisite/slovnik/jwt/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 29.573** (Rel-19) — PLMN/SNPN Interconnection Interface Stage 3
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [JWE na 3GPP Explorer](https://3gpp-explorer.com/glossary/jwe/)
