---
slug: "pvt"
url: "/mobilnisite/slovnik/pvt/"
type: "slovnik"
title: "PVT – Public Validation Token"
date: 2025-01-01
abbr: "PVT"
fullName: "Public Validation Token"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pvt/"
summary: "Bezpečnostní token používaný v sítích 3GPP k ověření autenticity a integrity veřejných dat nebo služeb, jako jsou ty poskytované aplikačními servery (AS) nebo pro autorizaci uživatelského zařízení (UE"
---

PVT je kryptografický bezpečnostní token používaný v sítích 3GPP k ověření autenticity a integrity veřejných dat nebo služeb, který pomáhá předcházet podvržení a zajišťuje, že pouze legitimní entity mají přístup k síťovým službám.

## Popis

Public Validation Token (PVT) je bezpečnostní konstrukce definovaná ve specifikacích 3GPP, primárně v kontextu zabezpečení aplikační vrstvy a autentizačních rámců. Funguje jako ověřitelný doklad, často generovaný důvěryhodnou entitou, jako je síťová funkce nebo autentizační server, a je předkládán klientem (např. UE nebo [AS](/mobilnisite/slovnik/as/)) k prokázání jeho práva přístupu ke konkrétní službě nebo prostředku. Token je typicky digitálně podepsán nebo chráněn kódem pro ověření zprávy ([MAC](/mobilnisite/slovnik/mac/)), což zajišťuje jeho integritu a autenticitu. Proces ověření zahrnuje ověření podpisu nebo MAC tokenu přijímající entitou pomocí předem sdílených nebo zřízených veřejných klíčů nebo symetrických klíčů, čímž se potvrdí, že byl vydán legitimní autoritou a nebyl pozměněn.

Architektonicky jsou mechanismy PVT integrovány do protokolů autorizace služeb. Například ve scénářích zahrnujících přístup aplikačního serveru (AS) k síťovým schopnostem nebo přístup UE ke službám třetích stran může být PVT součástí tokenu OAuth 2.0 nebo podobného přenosového dokladu. Token obsahuje nároky o subjektu (např. identita, oprávnění, doba platnosti) a je vázán na konkrétní kontext, aby se zabránilo opakovaným útokům. Mezi klíčové komponenty patří vydavatel tokenu (Token Issuer), což je důvěryhodná bezpečnostní funkce (jako Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo specializovaný autentizační server), spotřebitel tokenu (Token Consumer, entita, která token přijímá a ověřuje) a držitel tokenu (Token Holder, entita předkládající token). Formát tokenu a pravidla ověření jsou standardizovány, aby byla zajištěna interoperabilita mezi různými dodavateli a síťovými nasazeními.

Během provozu zahrnuje životní cyklus PVT vydání, předložení a ověření. Vydavatel vygeneruje token po úspěšném ověření a autorizaci žádající entity a vloží do něj potřebné atributy a kryptografický důkaz. Držitel pak tento token zahrne do žádostí o službu směrem ke spotřebiteli. Spotřebitel, který má potřebný ověřovací klíč (často získaný od vydavatele nebo služby distribuce klíčů), dešifruje nebo ověří podpis, zkontroluje nároky (jako expirace a rozsah) a podle toho přístup povolí nebo zamítne. Tím se oddělí událost ověření od přístupu ke službě, což umožňuje bezstavové a škálovatelné bezpečnostní kontroly. Jeho role je klíčová v moderních architekturách založených na službách ([SBA](/mobilnisite/slovnik/sba/)) jádra 5G, kde spolu komunikují četné síťové funkce a externí aplikace a je vyžadována odlehčená, ale bezpečná metoda pro vytváření důvěry mezi doménami bez nutnosti průběžného opětovného ověřování.

## K čemu slouží

PVT byl zaveden, aby řešil rostoucí potřebu bezpečných, škálovatelných a standardizovaných autorizačních mechanismů v sítích 3GPP, zejména když se služby více otevíraly aplikacím třetích stran a cloudovým prostředím. Před jeho formalizací se autorizace často spoléhala na jednodušší, méně flexibilní metody, jako jsou statické [API](/mobilnisite/slovnik/api/) klíče nebo integrované ověřování v rámci proprietárních protokolů, které přinášely rizika jako únik klíčů, nedostatek podrobné kontroly a obtížné řízení důvěry mezi administrativními doménami. PVT poskytuje kryptograficky zabezpečený, tokenový přístup, který podporuje delegovanou autorizaci a přístup s nejnižšími oprávněními, čímž se přizpůsobuje moderním paradigmatům správy identit a přístupu ([IAM](/mobilnisite/slovnik/iam/)), jako je OAuth.

Historicky, jak se sítě 3GPP vyvíjely směrem k 5G a rozhraním založeným na službách, vystavení síťových schopností (např. přes [NEF](/mobilnisite/slovnik/nef/)) externím aplikačním serverům vyžadovalo robustní bezpečnostní model, který by zabránil neoprávněnému přístupu a zneužití služeb. PVT to řeší tím, že umožňuje síti vydávat krátkodobě platné, kontextově specifické tokeny, které externí entity mohou používat k prokázání své autorizace, čímž se ve srovnání s dlouhodobými přihlašovacími údaji snižuje prostor pro útok. Řeší také omezení dřívějších bezpečnostních mechanismů 3GPP, které byly často těsně provázány s ověřováním v jádru sítě (jako [AKA](/mobilnisite/slovnik/aka/)) a nebyly vhodné pro zabezpečení na aplikační vrstvě nebo severních API. Poskytnutím standardizovaného formátu tokenu a postupu ověření PVT usnadňuje bezpečné otevření sítě a API ekonomiku, které jsou ústřední pro vizi 5G umožňující služby vertikálních odvětví.

## Klíčové vlastnosti

- Kryptografická integrita a autenticita prostřednictvím digitálních podpisů nebo MAC
- Podpora delegované autorizace a rámců OAuth 2.0
- Obsahuje nároky na identitu, oprávnění a dobu platnosti
- Odlehčené a bezstavové ověření pro škálovatelný přístup ke službám
- Zabraňuje opakovaným útokům prostřednictvím kontextové vazby a časového omezení platnosti
- Interoperabilní mezi různými implementacemi dodavatelů a síťovými funkcemi

## Definující specifikace

- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 33.885** (Rel-14) — Security Study for V2X Services

---

📖 **Anglický originál a plná specifikace:** [PVT na 3GPP Explorer](https://3gpp-explorer.com/glossary/pvt/)
