---
slug: "jwt"
url: "/mobilnisite/slovnik/jwt/"
type: "slovnik"
title: "JWT – JSON Web Token"
date: 2026-01-01
abbr: "JWT"
fullName: "JSON Web Token"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/jwt/"
summary: "JSON Web Token (JWT) je kompaktní, URL bezpečný formát tokenu pro bezpečný přenos nároků mezi stranami. V 3GPP se používá pro autentizaci, autorizaci a výměnu informací, což umožňuje bezstavové (state"
---

JWT je kompaktní, URL bezpečný formát tokenu používaný v systémech 3GPP pro autentizaci, autorizaci a bezpečný přenos nároků (claims) mezi síťovými funkcemi a externími aplikacemi.

## Popis

[JSON](/mobilnisite/slovnik/json/) Web Token (JWT) je standardizovaný formát tokenu, který kóduje nároky jako JSON objekt, jenž je následně digitálně podepsán nebo zašifrován pro zajištění bezpečnosti. V sítích 3GPP slouží JWT jako prostředek pro předávání identity, oprávnění a dalších atributů mezi entitami, například mezi uživatelským zařízením (UE) a síťovými funkcemi nebo mezi různými prvky jádra sítě. JWT se skládá ze tří částí: hlavičky (header), užitečného zatížení (payload) a podpisu (signature) (nebo obálky šifrování, pokud se používá [JWE](/mobilnisite/slovnik/jwe/)). Hlavička typicky specifikuje typ tokenu (JWT) a kryptografický algoritmus použitý pro podpis nebo šifrování (např. HS256 pro HMAC SHA-256). Užitečné zatížení obsahuje nároky (claims), což jsou tvrzení o entitě (např. identita uživatele, údaje o předplatném, čas vypršení platnosti), které jsou kategorizovány jako registrované, veřejné nebo privátní. Podpis je vytvořen podepsáním zakódované hlavičky a užitečného zatížení pomocí tajného nebo privátního klíče, což vede ke kompaktnímu řetězci, který lze snadno přenášet v [HTTP](/mobilnisite/slovnik/http/) hlavičkách nebo [URL](/mobilnisite/slovnik/url/).

V rámci architektury 3GPP je JWT nedílnou součástí mechanismů autentizace a autorizace, zejména v rozhraních založených na službách (service-based interfaces) v 5G. Například v rámci 5G Authentication and Key Agreement (5G [AKA](/mobilnisite/slovnik/aka/)) mohou být JWT použity jako přístupové tokeny pro udělování oprávnění síťovým funkcím na základě principů OAuth 2.0. Token je vydán autorizačním serverem (jako je Network Exposure Function nebo vyhrazený OAuth server) po úspěšné autentizaci a obsahuje nároky jako vydavatel (issuer), subjekt (subject), cílovou skupinu (audience) a čas vypršení platnosti. Když síťová funkce přijme JWT, ověří podpis pomocí veřejného klíče vydavatele, zkontroluje platnost nároků (např. zajistí, že token nevypršel a je určen správné cílové skupině) a následně použije obsažené informace pro rozhodování o autorizaci. Tento proces umožňuje bezstavovou (stateless) autentizaci, protože token sám nese všechny potřebné údaje, což snižuje potřebu ukládání relací na straně serveru a zlepšuje škálovatelnost.

Role JWT se rozšiřuje do různých specifikací 3GPP, včetně těch pro zabezpečení, vystavení sítě (network exposure) a edge computing. Používá se ve scénářích jako je zabezpečený přístup ke službám pro aplikace třetích stran, kde JWT může zapouzdřit souhlas uživatele nebo kvóty [API](/mobilnisite/slovnik/api/), a v roamingových dohodách, kde tokeny usnadňují důvěru mezi operátory. Token může být podepsán pomocí [JWS](/mobilnisite/slovnik/jws/) pro integritu nebo zašifrován pomocí JWE pro důvěrnost, v závislosti na citlivosti nároků. Tato flexibilita umožňuje JWT přizpůsobit se různým bezpečnostním požadavkům, od veřejných nároků, které může číst kdokoli, až po privátní nároky, které musí být chráněny. Přijetím JWT se 3GPP přizpůsobuje webovým standardům ([IETF](/mobilnisite/slovnik/ietf/) RFC 7519), což zajišťuje interoperabilitu se stávajícími systémy identity a zjednodušuje integraci s cloud-nativními aplikacemi. Díky tomu je JWT klíčovým prvkem pro umožnění bezpečné, efektivní a škálovatelné komunikace v moderních telekomunikačních sítích, podporující funkce jako síťové řezy (network slicing), autentizaci zařízení IoT a dynamické vynucování politik.

## K čemu slouží

JWT byl zaveden v 3GPP, aby řešil omezení tradiční autentizace založené na relacích a binárních formátů tokenů v stále více distribuovaných a API řízených síťových prostředích. Před jeho přijetím systémy 3GPP často používaly proprietární nebo složité mechanismy pro výměnu tokenů, jako jsou SAML aserce nebo vlastní binární protokoly, které byly těžkopádné, obtížně analyzovatelné v kontextech webu a vyžadovaly stavové servery pro správu relací. Tyto přístupy představovaly výzvy pro škálovatelnost a interoperabilitu, zejména když se sítě vyvíjely pro podporu architektur mikroslužeb a integrací externích API. JWT tyto problémy řeší tím, že poskytuje lehký, JSON založený token, který je soběstačný (self-contained), nese všechny potřebné informace ve svém užitečném zatížení a lze jej snadno přenášet přes HTTP, což jej činí ideálním pro bezstavovou autentizaci v jádrech založených na službách.

Motivace pro JWT v 3GPP vychází z potřeby efektivního a bezpečného řízení identity v 5G a dalších generacích, kde různé služby a zařízení vyžadují bezproblémovou autentizaci napříč doménami. S nástupem vystavení sítě (network exposure) a edge computingu vzrostla poptávka po standardizovaném formátu tokenu, který by mohly používat jak aplikace třetích stran, tak síťové funkce, aniž by byly závislé na centralizovaných úložištích relací. JWT tuto poptávku naplňuje tím, že umožňuje identitu založenou na nárocích (claims-based identity), kde tokeny mohou být vydány jednou a ověřeny více stranami, což snižuje latenci a zjednodušuje bezpečnostní pracovní postupy. Začleněním JWT do specifikací jako 33.122 a 33.938 využilo 3GPP jeho širokého přijetí v webovém ekosystému ke zvýšení bezpečnosti pro roaming, přístup k API a autentizaci uživatelů, řešíc problémy jako opakované použití tokenu (replay) a vypršení platnosti, a zároveň podporuje dynamickou a škálovatelnou povahu moderních telekomunikačních sítí.

## Klíčové vlastnosti

- Kompaktní, URL bezpečný formát tokenu pro snadný přenos
- Soběstačné (self-contained) užitečné zatížení s nároky pro bezstavovou autentizaci
- Podpora podpisu (JWS) a šifrování (JWE) pro zabezpečení
- Standardizované typy nároků (registrované, veřejné, privátní)
- Validace vypršení platnosti a cílové skupiny pro řízení přístupu
- Interoperabilita s OAuth 2.0 a OpenID Connect

## Související pojmy

- [JWS – JSON Web Signature](/mobilnisite/slovnik/jws/)
- [JWE – JSON Web Encryption](/mobilnisite/slovnik/jwe/)

## Definující specifikace

- **TS 33.122** (Rel-19) — Security Architecture for CAPIF
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [JWT na 3GPP Explorer](https://3gpp-explorer.com/glossary/jwt/)
