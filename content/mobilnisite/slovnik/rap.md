---
slug: "rap"
url: "/mobilnisite/slovnik/rap/"
type: "slovnik"
title: "RAP – Resource Allocation Protocol"
date: 2025-01-01
abbr: "RAP"
fullName: "Resource Allocation Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rap/"
summary: "Protokol pro správu a alokaci síťových zdrojů, primárně definovaný pro služby doručování médií. Zajišťuje efektivní využití přenosové kapacity a síťových prvků koordinací požadavků na zdroje a jejich"
---

RAP (Resource Allocation Protocol) je protokol pro správu a alokaci síťových zdrojů, který zajišťuje efektivní využití přenosové kapacity koordinací požadavků a přiřazení mezi entitami, jako jsou aplikační servery.

## Popis

Resource Allocation Protocol (RAP) je signalizační protokol definovaný v rámci standardů 3GPP, primárně specifikovaný v kontextu služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a dalších služeb doručování médií. Funguje jako mechanismus řídicí roviny pro správu alokace a uvolňování síťových zdrojů potřebných pro mediální relace. Protokol zprostředkovává komunikaci mezi entitami, jako je Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) a funkce pro zpracování médií, což umožňuje vyjednání a rezervaci potřebné přenosové a zpracovatelské kapacity před zřízením mediálního toku. Tím je zajištěno, že síť může po dobu trvání relace garantovat požadovanou kvalitu služby (QoS).

Z architektonického hlediska se RAP týká klíčových síťových prvků včetně alokátoru zdrojů (často součást BM-SC nebo specializované funkce pro správu zdrojů) a konzumentů zdrojů (jako jsou mediální kodéry, paketové brány nebo obsahové servery). Protokol definuje sadu zpráv a procedur pro požadavky na rezervaci zdrojů, potvrzení, změny a uvolnění. Typická RAP transakce začíná zprávou Resource Allocation Request od žádající entity, která obsahuje parametry jako požadovaná šířka pásma, typ mediálního kodeku, doba trvání relace a cílová oblast služby. Alokátor tento požadavek zpracuje, ověří dostupnost zdrojů vůči pravidlům politiky a síťovému vytížení, a odpoví zprávou Resource Allocation Response označující úspěch nebo selhání, spolu s přiřazenými identifikátory zdrojů a parametry.

Fungování RAP je úzce integrováno s dalšími subsystémy 3GPP, zejména s architekturou Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) a přenosovou službou MBMS. Může komunikovat s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) pro vynucení QoS politik a s funkcemi přenosové sítě pro zřizování odpovídajících přenosových kanálů. Protokol podporuje jak okamžitou, tak odloženou alokaci zdrojů, což umožňuje předběžnou rezervaci zdrojů pro plánované vysílání. Obsahuje také mechanismy pro přednostní převzetí zdrojů, kdy relace s vyšší prioritou mohou získat zdroje od těch s nižší prioritou, a pro pozvolnou degradaci ve scénářích soupeření o zdroje. Poskytnutím standardizovaného rozhraní pro správu zdrojů umožňuje RAP interoperabilitu mezi zařízeními různých výrobců a efektivní dynamické využívání zdrojů v celé síti 3GPP.

## K čemu slouží

RAP byl vytvořen pro řešení potřeby standardizovaného a efektivního mechanismu pro správu a alokaci síťových zdrojů pro mediální služby, zejména pro vysílací a skupinové toky. Před jeho zavedením byla správa zdrojů pro služby jako [MBMS](/mobilnisite/slovnik/mbms/) často řešena proprietárními nebo ad-hoc metodami, což vedlo k problémům s interoperabilitou a neoptimálním využitím zdrojů. Protokol poskytuje společný jazyk a proceduru pro vyžádání a rezervaci šířky pásma, výpočetního výkonu a úložné kapacity potřebné pro doručení mediálního obsahu se zaručenou kvalitou.

Motivace vycházela z rostoucí poptávky po multimediálních službách přes mobilní sítě, které vyžadují předvídatelnou alokaci zdrojů pro zajištění uživatelského zážitku. Bez protokolu jako RAP se sítě potýkaly s koordinací zdrojů mezi různými funkčními doménami (např. doručování obsahu, přenos a řízení politik), což vedlo buď k nadměrnému poskytování (plýtvání kapacitou), nebo k nedostatečnému poskytování (způsobující degradaci služby). RAP to řeší zavedením formalizovaného protokolu typu požadavek-odpověď, který je integrován do existujících architektur 3GPP, a umožňuje tak dynamickou správu zdrojů uvědomující si relace.

Historicky se vývoj RAP ve verzi Release 8 časově shodoval s vylepšením MBMS a snahou o služby založené na IP multimédiích. Řešil omezení statické konfigurace zdrojů tím, že umožňoval alokaci na vyžádání v souladu se skutečnými požadavky služby. To bylo klíčové pro škálovatelné doručování živé televize, videa na vyžádání a dalších aplikací náročných na šířku pásma, protože zajišťovalo, že síťové zdroje jsou efektivně alokovány pouze v případě potřeby a po použití jsou okamžitě uvolněny, čímž se zlepšuje celková síťová kapacita a spolehlivost služeb.

## Klíčové vlastnosti

- Standardizovaná sada zpráv pro požadavek na zdroje, jejich alokaci, změnu a uvolnění
- Integrace s Policy and Charging Control (PCC) pro vynucení QoS
- Podpora jak okamžitých, tak odložených (předběžných) rezervací zdrojů
- Mechanismy pro přednostní převzetí zdrojů na základě úrovní priority
- Možnost specifikovat podrobné parametry zdrojů (šířka pásma, kodek, doba trvání, oblast služby)
- Interoperabilita mezi zařízeními různých výrobců prostřednictvím definovaných rozhraní

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines

---

📖 **Anglický originál a plná specifikace:** [RAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rap/)
