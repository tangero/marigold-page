---
slug: "drc"
url: "/mobilnisite/slovnik/drc/"
type: "slovnik"
title: "DRC – Downlink Rate Command"
date: 2025-01-01
abbr: "DRC"
fullName: "Downlink Rate Command"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/drc/"
summary: "Řídicí signál v sítích HSPA, který UE používá k žádosti o konkrétní přenosovou rychlost ve směru downlink od NodeB. Je součástí vysílacího řídicího kanálu (HS-DPCCH) a je zásadní pro rychlou adaptaci"
---

DRC je řídicí signál v sítích HSPA, pomocí kterého UE (uživatelské zařízení) žádá přes vysílací kanál HS-DPCCH o konkrétní přenosovou rychlost ve směru downlink od NodeB, což umožňuje rychlou adaptaci spojení.

## Popis

Downlink Rate Command (DRC, příkaz pro rychlost ve směru downlink) je základní součástí funkce High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) zavedené ve specifikaci 3GPP Release 5 a dále upravované v následujících vydáních. Funguje v rámci vysílacího kanálu High-Speed Dedicated Physical Control Channel ([HS-DPCCH](/mobilnisite/slovnik/hs-dpcch/)) ve směru od uživatelského zařízení (UE) k NodeB. Primární funkcí DRC je informovat NodeB o okamžitých podmínkách kanálu ve směru downlink tak, jak je vnímá UE, což umožňuje rychlé a adaptivní plánování na vrstvě přístupu k rádiové síti. UE průběžně měří kvalitu vysílacího pilotního kanálu ([CPICH](/mobilnisite/slovnik/cpich/)) a na základě tohoto měření a vlastních schopností přijímače vybere vhodnou kombinaci transportního formátu, o které se domnívá, že ji kanál podporuje. Tato vybraná kombinace je zakódována do indexu DRC, který je vysílán do NodeB. Plánovač NodeB používá tuto informaci DRC spolu s dalšími faktory, jako je dostupný výkon a vytížení buňky, aby rozhodl, kterému UE bude obsluhovat v následujícím přenosovém časovém intervalu ([TTI](/mobilnisite/slovnik/tti/)) a jakou přenosovou rychlostí. Tento proces je znám jako rychlá adaptace spojení.

Mechanismus DRC je úzce propojen s procesy Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)) a hlášením Channel Quality Indicator ([CQI](/mobilnisite/slovnik/cqi/)). Zatímco CQI poskytuje podrobnější doporučení ohledně kvality kanálu, DRC je přímý příkaz udávající preferovanou přenosovou rychlost a modulační schéma (např. [QPSK](/mobilnisite/slovnik/qpsk/) nebo [16QAM](/mobilnisite/slovnik/16qam/)) ze strany UE. Hodnota DRC odpovídá konkrétní kombinaci velikosti transportního bloku, počtu kódů a modulace, jak je definováno ve specifikacích. To umožňuje NodeB rychle upravit parametry přenosu ve směru downlink tak, aby odpovídaly aktuálním rádiovým podmínkám, maximalizovat propustnost při zachování přijatelné míry chybovosti bloků. Přenos DRC je klíčovou součástí rychlé zpětnovazební smyčky, která činí HSDPA efektivním, snižuje latenci a zvyšuje špičkové přenosové rychlosti ve srovnání s WCDMA před zavedením HSDPA.

Z architektonického hlediska je DRC generován fyzickou vrstvou UE a vysílán přes vysílací kanál HS-DPCCH. Entita MAC-hs (Medium Access Control for high speed) v NodeB tuto informaci přijímá a zpracovává. Účinnost DRC závisí na přesném a včasném odhadu kanálu ze strany UE. Pokud je DRC příliš konzervativní, síťové zdroje jsou nevyužity; pokud je příliš agresivní, dochází k nadměrným retransmisím, což plýtvá zdroji. Algoritmy pro výběr DRC v rámci UE jsou tedy závislé na implementaci, ale pro celkový výkon zásadní. Role DRC poklesla se zavedením LTE a 5G NR, které používají pokročilejší zpětnovazební mechanismy, jako jsou hlášení Channel State Information (CSI), ale DRC zůstává klíčovým konceptem ve vývoji paketových datových služeb 3G.

## K čemu slouží

DRC byl vytvořen, aby řešil klíčové omezení raných sítí WCDMA (Release 99): pomalé a centralizované plánování pro paketová data. V počátečních nasazeních 3G se rozhodnutí o plánování prováděla na úrovni Radio Network Controller (RNC), což přinášelo významnou latenci (řádově 100 ms) a neumožňovalo rychle reagovat na rychlé útlumy rádiového kanálu. To vedlo k neefektivnímu využití rádiového spektra a nižší možné datové propustnosti. Zavedení HSDPA v Release 5 přesunulo funkci plánování do NodeB (základnové stanice), což umožnilo rozhodování na základě 2ms TTI.

DRC je zpětnovazební mechanismus, který toto rychlé plánování v NodeB umožňuje. Jeho účelem je poskytovat plánovači téměř okamžitou zpětnou vazbu o podmínkách kanálu od UE. Příjmem přímého příkazu pro podporovanou přenosovou rychlost může NodeB okamžitě přidělit zdroje UE, která je v nejlepší pozici pro jejich přijetí, čímž implementuje formu diverzity více uživatelů. Tím byla vyřešena pomalá adaptace kanálu, což dramaticky zvýšilo spektrální účinnost, špičkovou propustnost pro uživatele (teoreticky až 14,4 Mbps v Release 5) a celkovou kapacitu systému pro paketové datové služby ve směru downlink. Byl to revoluční krok, který učinil mobilní broadband praktickou realitou v sítích 3G.

## Klíčové vlastnosti

- Umožňuje rychlou adaptaci spojení s granularitou 2ms TTI
- Přenášen ve směru uplink na řídicím kanálu HS-DPCCH
- Kóduje preferovaný transportní formát UE (modulace, kódování)
- Podporuje diverzitu více uživatelů prostřednictvím rychlého plánování v NodeB
- Spolupracuje s HARQ pro rychlou opravu chyb
- Zásadní pro dosažení špičkové přenosové rychlosti v HSDPA

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [HS-DPCCH – High Speed Dedicated Physical Control Channel (Uplink)](/mobilnisite/slovnik/hs-dpcch/)

## Definující specifikace

- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.117** (Rel-19) — 5G Media Streaming Speech/Audio Capabilities
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification

---

📖 **Anglický originál a plná specifikace:** [DRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/drc/)
