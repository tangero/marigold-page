---
slug: "hal"
url: "/mobilnisite/slovnik/hal/"
type: "slovnik"
title: "HAL – Hypertext Application Language"
date: 2025-01-01
abbr: "HAL"
fullName: "Hypertext Application Language"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/hal/"
summary: "Hypertext Application Language (HAL) je typ média a formát pro reprezentaci prostředků a jejich vztahů v RESTful API, který pro navigaci používá hypertextové odkazy. Standardizuje odpovědi API s vlože"
---

HAL je typ média a formát používaný v rozhraních 3GPP založených na službách pro reprezentaci prostředků síťových funkcí a jejich vztahů pomocí vložených hypertextových odkazů pro komunikaci přes RESTful API.

## Popis

Hypertext Application Language (HAL) je jednoduchý, lehký typ média (application/hal+json nebo application/hal+xml) navržený pro reprezentaci prostředků a jejich vztahů v hypermédii řízených RESTful [API](/mobilnisite/slovnik/api/). Strukturováním odpovědí API zajišťuje, že obsahují nejen data, ale také hypertextové odkazy ukazující možné akce a vztahy k dalším prostředkům, čímž dodržuje omezení [HATEOAS](/mobilnisite/slovnik/hateoas/) (Hypermedia as the Engine of Application State). To umožňuje klientům dynamicky objevovat a navigovat API bez předchozí znalosti struktury URI, což podporuje volné spojení mezi klienty a servery. V 3GPP je HAL přijat v architekturách založených na službách, zejména pro rozhraní mezi síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) v 5G jádru, aby usnadnil flexibilní a škálovatelnou komunikaci.

Formát HAL organizuje prostředky do dvou hlavních komponent: stav prostředku (datové vlastnosti) a vložené prostředky (podprostředky obsažené v odpovědi). Každý prostředek obsahuje objekt '_links' s hypertextovými odkazy klíčovanými podle typů vztahů (např. 'self', 'next', 'related'), které definují navigační cesty. Například prostředek instance síťové funkce může obsahovat odkazy na přidružené služby nebo koncové body správy. Tento přístup zaměřený na odkazy umožňuje klientům procházet API sledováním vztahů, což snižuje závislosti na pevně zakódovaných cestách a umožňuje vývoj API bez narušení klientů. HAL také podporuje curies (kompaktní URI) pro definování vlastních vztahů odkazů, což zvyšuje čitelnost a standardizaci.

Ve specifikacích 3GPP se HAL používá v [HTTP](/mobilnisite/slovnik/http/) rozhraních založených na službách (SBI) definovaných pro 5G základní síť, jako jsou rozhraní mezi funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)). Funguje tak, že serializuje reprezentace prostředků ve formátu [JSON](/mobilnisite/slovnik/json/) nebo XML, s předdefinovanými schématy pro objevování síťových funkcí, registraci a spotřebu služeb. Protokol využívá standardní HTTP metody (GET, POST, PUT, DELETE) a stavové kódy, přičemž HAL poskytuje strukturní konzistenci pro odpovědi. To umožňuje automatizovanou interakci služeb, dynamické vyvažování zátěže a odolnost proti chybám, protože klienti mohou prostřednictvím odkazů objevovat alternativní instance. Použití HAL je v souladu s principy cloud-nativních aplikací a podporuje mikroslužební architektury a průběžné nasazování v telekomunikačních sítích.

## K čemu slouží

HAL byl v 3GPP zaveden, aby řešil potřebu standardizované, hypermédii řízené komunikace v architekturách založených na službách, zejména při přechodu na 5G. Předchozí přístupy, jako proprietární [API](/mobilnisite/slovnik/api/) nebo REST bez hypermédií, vedly k těsnému spojení mezi síťovými funkcemi, což činilo systémy křehkými a obtížně vyvíjetelnými. HAL to řeší vložením možnosti objevování přímo do odpovědí API, což umožňuje klientům se dynamicky přizpůsobovat změnám a snižuje složitost integrace.

Motivace pro přijetí HAL vychází z přechodu na cloud-nativní a mikroslužebami založené základní sítě, kde jsou síťové funkce oddělené a nasazované nezávisle. Tradiční telekomunikační rozhraní byla často statická a typu point-to-point, což bránilo škálovatelnosti a agilitě. HAL umožňuje flexibilnější model interakce, kde lze služby objevovat a spotřebovávat na vyžádání, což podporuje automatizaci, orchestraci a síťové slicing. To je klíčové pro požadavky 5G na nízkou latenci, vysokou spolehlivost a rozmanitost služeb.

Historicky návrh API v telekomunikacích spoléhal na specifické metody protokolů (např. Diameter) s pevnými toky zpráv. HAL poskytuje webově přívětivou, RESTful alternativu, která je v souladu s postupy IT průmyslu a usnadňuje integraci s cloudovými platformami a službami třetích stran. Řeší omezení, jako jsou problémy s verzováním a aktualizacemi klientů, použitím hypertextových odkazů jako primárního prostředku navigace, čímž zajišťuje zpětnou kompatibilitu a budoucí odolnost síťových rozhraní. To zvyšuje interoperabilitu a urychluje inovace v nasazování síťových služeb.

## Klíčové vlastnosti

- Standardizovaný typ média (application/hal+json/xml) pro reprezentaci prostředků
- Vložené hypertextové odkazy v objektu '_links' pro možnost objevování API a dodržování HATEOAS
- Podpora vložených prostředků pro zahrnutí souvisejících podprostředků v odpovědích
- Použití typů vztahů (např. self, next, curies) pro definování navigační sémantiky
- Integrace s HTTP rozhraními založenými na službách v 3GPP 5G základních sítích
- Umožňuje volné spojení mezi klienty a servery, což usnadňuje dynamický vývoj API

## Související pojmy

- [HATEOAS – Hypermedia As The Engine Of Application State](/mobilnisite/slovnik/hateoas/)

## Definující specifikace

- **TS 29.501** (Rel-19) — 5GC SBI API Design Principles & Guidelines
- **TS 32.866** (Rel-15) — REST, HTTP, JSON for Management Interfaces
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [HAL na 3GPP Explorer](https://3gpp-explorer.com/glossary/hal/)
