---
slug: "gzip"
url: "/mobilnisite/slovnik/gzip/"
type: "slovnik"
title: "GZIP – GNU ZIP"
date: 2025-01-01
abbr: "GZIP"
fullName: "GNU ZIP"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/gzip/"
summary: "Formát a algoritmus komprese dat standardizovaný pro použití v rozhraních sítí 3GPP, primárně pro API založená na HTTP, jako je Nnrf_NFManagement. Snižuje velikost přenášených datových zátěží, čímž zl"
---

GZIP je standardizovaný formát a algoritmus komprese dat používaný v rozhraních sítí 3GPP ke snížení velikosti přenášených datových zátěží (payload), čímž zvyšuje efektivitu využití přenosové kapacity a snižuje latenci u API založených na protokolu HTTP.

## Popis

GZIP, zkratka pro GNU ZIP, je široce používaný formát souboru a softwarová aplikace pro bezztrátovou kompresi dat. V rámci architektury 3GPP je od verze Release 16 formálně specifikováno použití GZIP komprese přes rozhraní typu service-based ([SBI](/mobilnisite/slovnik/sbi/)) založená na [HTTP](/mobilnisite/slovnik/http/), jako jsou například ta definovaná pro Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)). Hlavní technickou specifikací upravující její použití je 3GPP TS 29.500, která podrobně popisuje obecné principy a požadavky pro rozhraní typu service-based v systému 5G, včetně podpory kódování obsahu. Doprovodná specifikace TS 29.573 poskytuje podrobnější aspekty protokolu pro specifické služby NRF.

Integrace GZIP funguje na vrstvě protokolu HTTP. Když klient síťové funkce ([NF](/mobilnisite/slovnik/nf/)), jako je [AMF](/mobilnisite/slovnik/amf/) nebo [SMF](/mobilnisite/slovnik/smf/), odešle HTTP požadavek (např. POST nebo PUT požadavek obsahující velkou datovou zátěž [JSON](/mobilnisite/slovnik/json/) pro registraci nebo vyhledání NF) na serverovou NF, jako je NRF, může do svého požadavku zahrnout hlavičku 'Accept-Encoding: gzip'. Tím signalizuje serveru, že klient dokáže zpracovat odpovědi komprimované pomocí GZIP. Server následně při generování odpovědi může před přenosem komprimovat tělo odpovědi (data JSON) pomocí algoritmu GZIP a tuto skutečnost indikuje zahrnutím hlavičky 'Content-Encoding: gzip' v HTTP odpovědi. Klient následně přijatá data dekomprimuje.

Samotný algoritmus GZIP je založen na algoritmu DEFLATE, který kombinuje LZ77 (kompresní schéma založené na slovníku, které nahrazuje opakující se řetězce ukazateli) a Huffmanovo kódování (forma entropického kódování používající proměnně dlouhé kódy pro symboly). Tato kombinace je vysoce účinná pro textová data, jako jsou struktury JSON běžné v SBI rozhraních 3GPP. Proces komprese výrazně snižuje počet bajtů, které je nutné přenést po síti. To je zvláště významné pro signalizační zprávy, které mohou být rozsáhlé, jako jsou ty obsahující komplexní data politik, informace o předplatném nebo seznamy objevených síťových funkcí.

Její role v síti spočívá v tom, že jde o technologii umožňující zvýšení efektivity přenosu. Nemění sémantický obsah zpráv 3GPP, ale optimalizuje jejich fyzický přenos. Snížením velikosti přenášených datových zátěží komprese GZIP snižuje zatížení přenosových síťových spojů, může snížit režii zpracování paketů v mezilehlých uzlech a snižuje celkovou latenci při výměně zpráv, zejména ve scénářích s omezenou přenosovou kapacitou nebo vysokou signalizační zátěží. Tím přispívá k celkové škálovatelnosti a výkonu architektury typu service-based v jádru sítě 5G.

## K čemu slouží

Účelem standardizace komprese GZIP v rámci specifikací 3GPP bylo řešit rostoucí signalizační režii a spotřebu přenosové kapacity, které jsou vlastní nové architektuře typu service-based ([SBA](/mobilnisite/slovnik/sba/)) zavedené s jádrem sítě 5G. Před 5G často používala starší rozhraní binární protokoly (jako Diameter), které byly relativně kompaktní. Přechod na HTTP/2 a zprávy založené na JSON pro všechna interní rozhraní jádra sítě 5G, ačkoli přinesl flexibilitu a interoperabilitu na úrovni webových technologií, způsobil významné zvětšení velikosti zpráv kvůli rozvláčnosti textového kódování JSON.

Tato rozvláčnost představovala pro operátory sítí hmatatelný problém: větší zprávy spotřebovávají více přenosové kapacity na spojích mezi datovými centry, zvyšují zatížení síťových funkcí spojené se serializací/deserializací a mohou vést k vyšší latenci. Ve velkých nasazeních s miliony zařízení by kumulativní efekt neefektivního přenosu signalizace mohl ovlivnit výkon sítě a provozní náklady. Motivací pro přijetí GZIP bylo využít osvědčenou, průmyslově standardní kompresní techniku ke zmírnění těchto nevýhod bez nutnosti přepracování aplikačních protokolů.

Proto 3GPP zavedlo podporu GZIP jako povinnou funkci (mandatory-to-support) pro určité NF (jako je NRF), aby zajistilo, že výhody flexibilní SBA nebudou podkopány neefektivitou přenosu. Řeší problém nafouknutí přenášených datových zátěží tím, že poskytuje standardizovanou, efektivní metodu pro NF, jak vyjednat a aplikovat kompresi, čímž zajišťuje interoperabilitu mezi implementacemi různých dodavatelů a zároveň optimalizuje využití síťových zdrojů.

## Klíčové vlastnosti

- Standardizované kódování obsahu HTTP pro rozhraní typu Service-Based v 3GPP
- Bezztrátová komprese zajišťující integritu dat signalizačních zpráv
- Založeno na algoritmu DEFLATE (LZ77 a Huffmanovo kódování)
- Vyjednáváno prostřednictvím HTTP hlaviček (Accept-Encoding a Content-Encoding)
- Primárně aplikováno na datové zátěže JSON ve zprávách správy a vyhledávání NF
- Snižuje spotřebu přenosové kapacity a latenci u rozsáhlých signalizačních transakcí

## Související pojmy

- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)
- [JSON – JavaScript Object Notation](/mobilnisite/slovnik/json/)

## Definující specifikace

- **TS 29.500** (Rel-19) — 5GC Service Based Architecture Specification
- **TS 29.573** (Rel-19) — PLMN/SNPN Interconnection Interface Stage 3

---

📖 **Anglický originál a plná specifikace:** [GZIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/gzip/)
