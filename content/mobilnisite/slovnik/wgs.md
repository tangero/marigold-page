---
slug: "wgs"
url: "/mobilnisite/slovnik/wgs/"
type: "slovnik"
title: "WGS – World Geodetic System"
date: 2025-01-01
abbr: "WGS"
fullName: "World Geodetic System"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wgs/"
summary: "World Geodetic System (WGS) je standardní souřadnicový rámec a geodetický datum používaný pro kartografii, navigaci a geografické určování polohy. V 3GPP je WGS-84 referenčním systémem pro definování"
---

WGS je World Geodetic System (světový geodetický systém), konkrétně WGS-84, což je referenční souřadnicový systém 3GPP pro definování geografických oblastí, umístění buněk a poloh uživatelů.

## Popis

World Geodetic System, konkrétně [WGS-84](/mobilnisite/slovnik/wgs-84/), je globální standardní geodetický referenční systém přijatý 3GPP pro všechna geografická data ve svých specifikacích. Poskytuje konzistentní souřadnicový rámec (zeměpisná šířka, délka a nadmořská výška) pro definování tvaru Země a bodů na jejím povrchu. V mobilních sítích se souřadnice WGS-84 používají k určení polohy síťových prvků, jako jsou základnové stanice, hranic oblastí polohy, směrovacích oblastí, sledovacích oblastí a pro geografické ohraničení v službách založených na poloze. Systém je založen na elipsoidním modelu Země s definovanými parametry pro poloosu, zploštění a gravitační model, což zajišťuje interoperabilitu mezi globálními systémy.

Z architektonického hlediska je integrace WGS-84 realizována v síťových funkcích, které zpracovávají služby polohy, jako je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), Location Retrieval Function ([LRF](/mobilnisite/slovnik/lrf/)) a samotné UE při poskytování dat [GPS](/mobilnisite/slovnik/gps/)/[GNSS](/mobilnisite/slovnik/gnss/). Když UE hlásí svou polohu – například během nouzového volání (E911/eCall) nebo pro komerční služby polohy – typicky používá souřadnice WGS-84 odvozené ze satelitních navigačních systémů, jako je GPS, které jsou s WGS-84 inherentně sladěné. Síť tyto souřadnice používá k mapování UE na servisní oblast, spouštění politik založených na poloze nebo směrování nouzových služeb na správné místo příjmu tísňových hovorů ([PSAP](/mobilnisite/slovnik/psap/)).

Systém funguje tak, že převádí surová geografická data do jednotného formátu, který všechny síťové prvky a externí systémy (např. mapové služby, záchranné složky) mohou přesně interpretovat. Mezi klíčové komponenty patří samotný souřadnicový referenční systém, transformační parametry pro převod z lokálních dat (jako NAD83) na WGS-84 a protokoly pro kódování souřadnic v signalizačních zprávách (např. v LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) nebo [SUPL](/mobilnisite/slovnik/supl/)). Role WGS-84 je klíčová pro zajištění přesnosti a konzistence polohových informací po celém světě, což umožňuje aplikace od navigace a sledování majetku až po regulatorní požadavky na lokalizaci nouzových volajících.

## K čemu slouží

WGS-84 byl přijat 3GPP k vyřešení problému nekonzistentního geografického referencování v různých zemích a technologiích. Před jeho zavedením způsobovala různá národní nebo regionální geodetická data (např. evropské ED50, severoamerické NAD27) nesrovnalosti v hlášení polohy, což komplikovalo roaming, nouzové služby a globální nasazení služeb. Pro mobilní sítě, které jsou ze své podstaty globální, byl jediný, přesný a všeobecně přijímaný referenční systém nezbytný pro interoperabilitu, zejména pro nouzové služby, kde přesná poloha může zachránit život.

Vytvoření WGS-84 Ministerstvem obrany USA a jeho přijetí jako mezinárodního standardu poskytlo jednotný rámec, který 3GPP využilo již od svých raných verzí. Jeho integrace řeší potřebu spolehlivých služeb založených na poloze (LBS), regulatorních požadavků na lokalizaci nouzových volajících (např. FCC E911 v USA) a síťových optimalizačních funkcí, jako je geografické směrování nebo plánování pokrytí. Standardizací na WGS-84 3GPP zajišťuje, že poloha hlášená UE v jedné zemi je přesně interpretována síťovými prvky v jiné zemi, což usnadňuje plynulou globální mobilitu a kontinuitu služeb. Toto bylo zvláště motivováno nástupem aplikací využívajících polohu a právními požadavky na přesnost lokalizace pro nouzové služby.

## Klíčové vlastnosti

- Globální standardní geodetický datum (WGS-84) pro souřadnicové referencování
- Poskytuje zeměpisnou šířku, délku a nadmořskou výšku v konzistentním rámci
- Integrace s GPS/GNSS pro určování polohy UE
- Používá se pro definování síťových oblastí (např. sledovací oblasti, identifikátory buněk)
- Podpora lokalizace pro nouzové služby (E911, eCall)
- Umožňuje interoperabilitu služeb založených na poloze přes hranice

## Definující specifikace

- **TS 23.032** (Rel-19) — Universal Geographical Area Description

---

📖 **Anglický originál a plná specifikace:** [WGS na 3GPP Explorer](https://3gpp-explorer.com/glossary/wgs/)
