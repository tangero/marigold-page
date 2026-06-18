---
slug: "pkce"
url: "/mobilnisite/slovnik/pkce/"
type: "slovnik"
title: "PKCE – Proof Key for Code Exchange"
date: 2026-01-01
abbr: "PKCE"
fullName: "Proof Key for Code Exchange"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/pkce/"
summary: "PKCE je bezpečnostní rozšíření toku autorizačního kódu OAuth 2.0, navržené k ochraně proti útokům na zachycení autorizačního kódu, zejména u veřejných klientů, jako jsou mobilní aplikace. Zvyšuje bezp"
---

PKCE je bezpečnostní rozšíření toku autorizačního kódu OAuth 2.0, které chrání veřejné klienty, jako jsou mobilní aplikace, tím, že je nutí vytvořit a prokázat držení tajného klíče během autorizačního procesu.

## Popis

Proof Key for Code Exchange (PKCE, vyslovováno 'pixie') je definováno v 3GPP TS 33.180 jako bezpečnostní vylepšení pro framework OAuth 2.0, konkrétně pro typ grantu autorizačního kódu. Je primárně určeno k zabezpečení veřejných klientů – aplikací, které nemohou bezpečně uložit tajemství klienta, jako jsou nativní mobilní aplikace nebo jednostránkové webové aplikace. Základní mechanismus spočívá v tom, že klient vytvoří kryptograficky náhodný řetězec zvaný 'code verifier' (ověřovací kód) a jeho transformovanou hodnotu, 'code challenge' (výzva kódu), které se používají k propojení autorizační žádosti s následnou žádostí o token.

Z architektonického hlediska PKCE zavádí do toku OAuth dva nové parametry. Na začátku autorizačního procesu klient vygeneruje kryptograficky náhodný řetězec s vysokou entropií, code verifier. Poté vytvoří code challenge aplikací transformace (jako SHA-256) na verifier. Tato code challenge je odeslána autorizačnímu serveru spolu se standardní autorizační žádostí. Autorizační server tuto výzvu asociuje s vydaným autorizačním kódem a uloží ji.

Když klient později vymění přijatý autorizační kód za přístupový token, musí v žádosti o token předložit původní code verifier. Autorizační server přepočítá code challenge z předloženého verifieru a porovná ji s uloženou výzvou asociovanou s autorizačním kódem. Shoda dokazuje, že subjekt žádající o token je tentýž, který inicioval autorizační žádost, čímž se zmírňuje riziko, že zachycený autorizační kód použije útočník. Tento proces nevyžaduje tajemství klienta, což je ideální pro aplikace prováděné v nezabezpečeném prostředí. Jeho role v ekosystému 3GPP je klíčová pro zabezpečení přístupu k síťovým [API](/mobilnisite/slovnik/api/) pro aplikace třetích stran, zajišťující, že ověřování a autorizace pro služby jako API pro lokalizaci nebo platby jsou odolné proti útoku.

## K čemu slouží

PKCE bylo vytvořeno, aby řešilo kritickou zranitelnost ve standardním toku autorizačního kódu OAuth 2.0 při použití veřejnými klienty. Tradiční tok předpokládá, že se klient může ověřit pomocí tajemství, ale to je nepraktické a nejisté pro aplikace běžící na uživatelském zařízení, kde lze tajemství snadno extrahovat. Bez PKCE by útočník mohl zachytit autorizační kód (např. prostřednictvím škodlivé aplikace na stejném zařízení nebo manipulací s přesměrovacími [URI](/mobilnisite/slovnik/uri/)) a použít jej k získání přístupového tokenu a vydávání se za legitimního klienta.

Historický kontext spočívá ve stále větší závislosti na OAuth pro ověřování v mobilních a webových aplikacích. 3GPP přijalo PKCE (původně rozšíření [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 7636) pro zabezpečení síťových [API](/mobilnisite/slovnik/api/) vystavených poskytovateli služeb. Řeší problém útoků na vložení a zachycení autorizačního kódu zavedením mechanismu proof-of-possession (důkaz držení). Klient prokáže, že inicioval původní žádost, čímž uzavírá významnou bezpečnostní mezeru. To bylo motivováno potřebou standardizovaného, robustního bezpečnostního protokolu pro aplikace třetích stran přistupující k telekomunikačním síťovým funkcím, který zajišťuje ochranu uživatelských dat a síťových zdrojů, i když samotné klientské aplikaci nelze plně důvěřovat s dlouhodobým tajemstvím.

## Klíčové vlastnosti

- Ochrana proti útokům na zachycení autorizačního kódu
- Navrženo pro veřejné klienty OAuth (např. mobilní a jednostránkové aplikace)
- Používá kryptograficky náhodný code verifier generovaný klientem
- Využívá code challenge (transformovaný verifier) odesílanou během autorizace
- Propojuje autorizační žádost s žádostí o token prostřednictvím proof-of-possession
- Nevyžaduje statické tajemství klienta, čímž zvyšuje bezpečnost pro distribuované aplikace

## Definující specifikace

- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service

---

📖 **Anglický originál a plná specifikace:** [PKCE na 3GPP Explorer](https://3gpp-explorer.com/glossary/pkce/)
