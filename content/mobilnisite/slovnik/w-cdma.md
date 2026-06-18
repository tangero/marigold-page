---
slug: "w-cdma"
url: "/mobilnisite/slovnik/w-cdma/"
type: "slovnik"
title: "W-CDMA – Wideband Code Division Multiple Access"
date: 2008-01-01
abbr: "W-CDMA"
fullName: "Wideband Code Division Multiple Access"
category: "Radio Access Network"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/w-cdma/"
summary: "W-CDMA je primární technologií rádiového rozhraní pro sítě 3G/UMTS. Využívá přímou sekvenci rozprostřeného spektra s šířkou pásma 5 MHz k poskytnutí vyšších přenosových rychlostí a kapacity než techno"
---

W-CDMA je primární technologií rádiového rozhraní pro 3G/UMTS, která využívá přímou sekvenci rozprostřeného spektra (DSSS) s šířkou pásma 5 MHz k poskytnutí vyšších přenosových rychlostí a kapacity než technologie 2G.

## Popis

Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (W-CDMA) je základní technologií rádiového přístupu definovanou konsorciem 3GPP pro Universal Mobile Telecommunications System (UMTS), standard mobilních sítí třetí generace (3G). Jedná se o technologii přímé sekvence rozprostřeného spektra (DSSS), kde jsou uživatelská data násobena vysokorychlostním pseudonáhodným číselným kódem, čímž je signál rozprostřen přes široký kanál o šířce pásma 5 MHz. Tato velká šířka pásma ve srovnání s 200 kHz kanály GSM je původem označení 'Wideband' (širokopásmový). Všichni uživatelé vysílají současně ve stejném kmitočtovém pásmu, ale jsou odděleni jedinečnými ortogonálními rozprostíracími kódy. Přijímač použije odpovídající kód k 'složení' (de-spread) a obnovení požadovaného uživatelského signálu z celkového přijatého signálu.

Rádiové rozhraní W-CDMA obvykle pracuje v párovém spektru (režim [FDD](/mobilnisite/slovnik/fdd/)) se samostatnými nosnými o šířce 5 MHz pro uplink a downlink, existuje však i varianta s časovým duplexem ([TDD](/mobilnisite/slovnik/tdd/)). Mezi klíčové komponenty fyzické vrstvy patří rozprostírací faktor ([SF](/mobilnisite/slovnik/sf/)), který určuje zisk zpracování a datový tok, a skramblovací kód, který odděluje různé buňky nebo uživatele. Architektura se skládá z uživatelského zařízení (UE) a pozemní rádiové přístupové sítě UMTS ([UTRAN](/mobilnisite/slovnik/utran/)), která zahrnuje Node B (základnovou stanici) a řadiče rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). RNC spravuje rádiové zdroje, předávání hovorů a připojuje se k jádru sítě přes rozhraní Iu. W-CDMA podporuje proměnné datové toky až do 2 Mbps ve své počáteční verzi, čehož je dosaženo pomocí adaptivní modulace, proměnných rozprostíracích faktorů a přenosu s více kódy.

Provoz W-CDMA je charakterizován řízením výkonu, měkkým předáváním hovorů a RAKE přijímači. Rychlé uzavřené řízení výkonu (1500 Hz) je klíčové pro potlačení problému blízký-vzdálený, vlastního systémům [CDMA](/mobilnisite/slovnik/cdma/), a zajišťuje, že všechny signály dorazí k základnové stanici s podobnou úrovní výkonu. Měkké předávání umožňuje, aby bylo UE současně připojeno k více Node B, čímž zlepšuje spolehlivost na okrajích buněk. RAKE přijímač využívá více 'prstů' ke kombinaci energie signálu z různých šířicích drah (víbecestné šíření), čímž mění potenciální zhoršení na výhodu prostřednictvím diverzity drah. Tyto mechanismy společně poskytují robustní mobilní komunikaci s vysokou kapacitou a tvoří základ, na kterém byly vybudovány technologie High-Speed Packet Access ([HSPA](/mobilnisite/slovnik/hspa/)) pro další vylepšení datových schopností.

## K čemu slouží

W-CDMA bylo vyvinuto za účelem splnění požadavků IMT-2000 Mezinárodní telekomunikační unie (ITU) na systémy mobilních sítí 3G, které vyžadovaly výrazně vyšší přenosové rychlosti, spektrální účinnost a podporu multimediálních služeb ve srovnání s technologiemi 2G, jako je GSM (které používalo TDMA/FDMA). Hlavními omezeními 2G byly úzkopásmové kanály (200 kHz), které omezovaly datové toky, a neefektivní využití spektra pro přerušovaná paketová data. CDMA, jehož průkopníkem byla společnost Qualcomm, nabízelo teoretické výhody v kapacitě, frekvenčním využití (faktor opakování kmitočtu 1) a plynulém zhoršování při zatížení.

Vytvoření W-CDMA konkrétně směřovalo k poskytnutí globálního standardu pro 3G, který by podporoval bezproblémový mezinárodní roaming, vysokou kvalitu hlasu a rostoucí poptávku po mobilním přístupu k internetu. Bylo navrženo tak, aby koexistovalo s GSM sítěmi a nakonec je nahradilo, což vyžadovalo dvou režimové terminály. Šířka pásma 5 MHz byla zvolena jako kompromis mezi potenciálem pro vysoké datové toky a dostupnými alokacemi spektra po celém světě. W-CDMA vyřešilo problém umožnění skutečných mobilních širokopásmových služeb, jako je videohovor, mobilní TV a vysokorychlostní přístup k internetu, v komerčním měřítku. Vytvořilo flexibilní rádiovou platformu optimalizovanou pro přenos paketů, která mohla být dále vyvíjena, což vedlo přímo k HSPA a poskytlo technologický základ pro mobilní datovou revoluci.

## Klíčové vlastnosti

- Šířka kanálu 5 MHz využívající přímou sekvenci rozprostřeného spektra (DSSS)
- Vícenásobný přístup s kódovým dělením oddělující uživatele ortogonálními kódy s proměnným rozprostíracím faktorem (OVSF)
- Rychlé řízení výkonu (1500 Hz) pro zvládnutí interference a problému blízký-vzdálený
- Podpora měkkého a měkčího předávání hovorů pro plynulou mobilitu
- RAKE přijímač pro využití diverzity z vícecestného šíření
- Proměnné datové toky až do 2 Mbps (teoreticky) v počátečních verzích, podpora spojově orientovaných i paketově orientovaných služeb

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)
- [CDMA – Code Division Multiple Access](/mobilnisite/slovnik/cdma/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TS 25.821** (Rel-8) — UMTS1500 Work Item Technical Report

---

📖 **Anglický originál a plná specifikace:** [W-CDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/w-cdma/)
