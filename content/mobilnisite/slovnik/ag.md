---
slug: "ag"
url: "/mobilnisite/slovnik/ag/"
type: "slovnik"
title: "AG – Absolute Grant"
date: 2025-01-01
abbr: "AG"
fullName: "Absolute Grant"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ag/"
summary: "Absolute Grant (AG) je klíčový řídicí signál ve funkci Enhanced Uplink (EUL) v 3GPP UMTS (HSPA). Je vysílán Node B k uživatelskému zařízení (UE), aby explicitně nastavil maximální povolený výkon pro v"
---

AG (Absolute Grant – absolutní povolení) je řídicí signál vysílaný z Node B k UE v 3GPP HSPA, který přímo nastavuje maximální povolený výkon pro vysílání v uplinku pro jeho E-DCH data.

## Popis

Absolute Grant (AG) je kritickou součástí Enhanced Uplink (EUL), známého také jako High Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)), v rámci 3GPP UMTS. Funguje jako součást rychlého mechanismu plánování řízeného Node B pro Enhanced Dedicated Channel ([E-DCH](/mobilnisite/slovnik/e-dch/)). Primární funkcí AG je poskytnout uživatelskému zařízení (UE) explicitní absolutní hodnotu pro jeho maximální povolený poměr výkonu pro vysílání v uplinku, konkrétně pro přenos dat E-DCH. Tento poměr výkonu je definován vzhledem k výkonu Dedicated Physical Control Channel ([DPCCH](/mobilnisite/slovnik/dpcch/)) UE. AG je přenášen z obsluhující Node B k UE přes E-DCH Absolute Grant Channel ([E-AGCH](/mobilnisite/slovnik/e-agch/)), což je sdílený downlink fyzický kanál. Samotná hodnota povolení je kvantována a reprezentována 5bitovým polem, což Node B umožňuje přímo nastavit konkrétní výkonovou rezervu pro uplink přenosy UE.

Z architektonického hlediska je mechanismus AG ústředním prvkem rychlé smyčky plánování v Node B, na rozdíl od pomalejšího plánování založeného na Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) používaného v dřívějších releasech UMTS. Když se Node B rozhodne upravit přidělení uplinkových zdrojů UE – například pro správu zatížení buňky, upřednostnění provozu nebo reakci na žádost o plánování – odešle příkaz AG. Tento příkaz přímo nastaví Serving Grant UE, který určuje maximální poměr výkonu [E-DPDCH](/mobilnisite/slovnik/e-dpdch/)/DPCCH, který může UE použít pro svůj další přenos. AG může nastavit širokou škálu hodnot, od velmi nízkého povolení (což efektivně umlčí UE) až po maximální povolení povolené pro danou kategorii UE.

AG funguje ve spojení s Relative Grant ([RG](/mobilnisite/slovnik/rg/)). Zatímco AG poskytuje hrubé, absolutní nastavení úrovně výkonu, RG (vysílaný na [E-RGCH](/mobilnisite/slovnik/e-rgch/)) poskytuje jemné přírůstkové úpravy (zvýšení, snížení nebo ponechání) aktuálního povolení. AG se typicky používá pro významné změny v přidělování zdrojů, například když UE zahájí novou datovou relaci nebo když Node B potřebuje drasticky snížit interferenci. UE kontinuálně monitoruje E-AGCH ze své obsluhující buňky a aplikuje novou hodnotu povolení v definovaném aktivačním čase, což umožňuje reakční doby pod 2 ms pro rozhodnutí o plánování. Tato rychlá a přímá kontrola umožňuje Node B těsně řídit uplinkové interference a optimalizovat propustnost buňky a latenci.

Klíčové komponenty zapojené do procesu AG zahrnují plánovač Node B, který generuje hodnotu povolení na základě měření zatížení uplinku a požadavků QoS; fyzický kanál E-AGCH, který přenáší příkaz povolení; a entitu E-DCH medium access control (MAC-e/es) v UE, která interpretuje povolení a aplikuje jej pro výběr vhodné Transport Format Combination (TFC) pro uplink přenos. Role AG je klíčová při transformaci uplinku UMTS z kapacitně omezeného systému řízeného RNC na vysokorychlostní, nízkolatenční a efektivně plánovaný kanál, který tvoří páteř výkonu uplinku v HSPA.

## K čemu slouží

Absolute Grant (AG) byl zaveden, aby vyřešil základní omezení původního uplinku UMTS Release 99. V počáteční architektuře bylo plánování uplinkových zdrojů prováděno výhradně Radio Network Controllerem (RNC), centralizovanou entitou s relativně pomalými reakčními časy (řádově stovky milisekund). Toto pomalé, na celou buňku zaměřené plánování nedokázalo efektivně zvládat trhavý paketový datový provoz, což vedlo k špatné latenci uplinku, nízké propustnosti a neefektivnímu využití zdroje výkonu uplinku – primární komodity omezené interferencí ve WCDMA systémech.

Vytvoření Enhanced Uplink (EUL) v Release 6 bylo motivováno potřebou rychlejší, detailnější a distribuované kontroly uplinku. Mechanismus AG byl vyvinut, aby to umožnil, tím, že přesunul rozhodování o plánování přímo do Node B, síťového prvku nejbližšího rozhraní. To umožňuje Node B reagovat v řádu milisekund na okamžité změny v uplinkové interferenci a stavu bufferu UE. AG poskytuje přímý a jednoznačný příkaz pro řízení vysílacího výkonu UE, což se přímo promítá do její datové rychlosti a generované interference. Tím je vyřešen problém pomalého přerozdělování zdrojů a umožněno efektivní multiplexování trhavého provozu více uživatelů.

Historicky AG řešil klíčovou výzvu řízení uplinkových interferencí v CDMA systému. Tím, že dal Node B rychlý, explicitní nástroj pro nastavení maximálního výkonu UE, mohla síť zabránit tomu, aby jediné UE způsobilo nadměrné interference a zhoršilo službu pro všechny ostatní uživatele v buňce. Také umožnilo rychlé přidělení zdrojů, když data dorazila k neaktivní UE, což výrazně zlepšilo uživatelsky vnímanou latenci pro interaktivní služby. AG jako součást rámce plánování Node B byl klíčovou inovací, která učinila vysokorychlostní, nízkolatenční uplinkový přístup k paketovým datům realitou v sítích 3G.

## Klíčové vlastnosti

- Explicitně nastavuje maximální povolený poměr výkonu E-DPDCH/DPCCH pro uplink přenos UE.
- Přenášen na vyhrazeném kanálu E-DCH Absolute Grant Channel (E-AGCH) z Node B.
- Používá 5bitovou kvantovanou hodnotu k nastavení konkrétní absolutní úrovně povolení.
- Umožňuje velmi rychlé plánování řízené Node B s reakčními časy pod 2 ms.
- Poskytuje hrubé řízení výkonu pro významné změny v přidělování zdrojů UE.
- Funguje v tandemu s Relative Grants (RG) pro doladění povolené úrovně výkonu.

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [E-AGCH – EDCH – Absolute Grant Channel](/mobilnisite/slovnik/e-agch/)

## Definující specifikace

- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [AG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ag/)
