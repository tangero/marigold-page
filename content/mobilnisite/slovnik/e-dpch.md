---
slug: "e-dpch"
url: "/mobilnisite/slovnik/e-dpch/"
type: "slovnik"
title: "E-DPCH – EDCH – Dedicated Physical Channel"
date: 2025-01-01
abbr: "E-DPCH"
fullName: "EDCH – Dedicated Physical Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-dpch/"
summary: "E-DPCH je fyzický kanál v UMTS/HSPA používaný k přenosu řídicích informací pro vylepšený vyhrazený kanál (E-DCH). Přenáší klíčovou signalizaci, jako jsou plánovací povolení a HARQ zpětná vazba, pro um"
---

E-DPCH je vylepšený vyhrazený fyzický kanál v UMTS/HSPA, který přenáší řídicí informace, jako jsou plánovací povolení a HARQ zpětná vazba pro E-DCH, aby umožnil funkci vysokorychlostního uplinku HSUPA.

## Popis

E-DPCH, neboli EDCH – Dedicated Physical Channel, je klíčovou součástí uplink fyzické vrstvy UMTS/[HSPA](/mobilnisite/slovnik/hspa/), konkrétně zavedenou pro podporu vylepšeného vyhrazeného kanálu ([E-DCH](/mobilnisite/slovnik/e-dch/)) pro High-Speed Uplink Packet Access ([HSUPA](/mobilnisite/slovnik/hsupa/)). Jedná se o vyhrazený fyzický řídicí kanál, který pracuje paralelně s datovým kanálem [E-DPDCH](/mobilnisite/slovnik/e-dpdch/). Primární funkcí E-DPCH je přenášet nezbytné řídicí informace, které umožňují Node B efektivně spravovat a dekódovat vysokorychlostní uplink datové přenosy od uživatelského zařízení (UE). Tyto řídicí informace zahrnují indikátor kombinace transportního formátu E-DCH ([E-TFCI](/mobilnisite/slovnik/e-tfci/)), který informuje Node B o transportním formátu (datové rychlosti) používaném na E-DPDCH, číslo sekvence pro retransmise ([RSN](/mobilnisite/slovnik/rsn/)) pro procesy Hybrid [ARQ](/mobilnisite/slovnik/arq/) ([HARQ](/mobilnisite/slovnik/harq/)) a Happy Bit, který indikuje spokojenost UE s aktuálně přidělenou uplink datovou rychlostí.

Architektonicky je E-DPCH namapován na specifické uplink fyzické zdroje kanálu a je vždy vysílán současně s E-DPDCH, když je HSUPA aktivní. Používá pevný šířicí faktor, což zajišťuje spolehlivý příjem řídicích dat i při kolísání výkonu a rychlosti datového kanálu. Kanál podléhá rychlé regulaci výkonu na základě příkazů řízení vysílacího výkonu (TPC) přijímaných na downlinku, podobně jako vyhrazený fyzický řídicí kanál (DPCCH). Node B využívá informace na E-DPCH k provádění koherentní detekce a demodulace přidruženého E-DPDCH, správě HARQ měkkého kombinování a provádění rychlých plánovacích rozhodnutí. Jeho spolehlivý provoz je zásadní pro charakteristiky nízké latence a vysoké účinnosti HSUPA.

Z pohledu sítě E-DPCH umožňuje plánování řízené Node B, které definuje HSUPA. Poskytováním okamžité a v-pásmové signalizace umožňuje Node B mít těsnou kontrolu na úrovni milisekund nad uplink interferencí a využitím zdrojů od více UE. To je klíčový odklon od plánování řízeného RNC v UMTS před HSUPA, což dramaticky snižuje latenci a zvyšuje špičkové datové rychlosti. Návrh kanálu zajišťuje minimalizaci režie řídicí signalizace při zachování robustnosti potřebné pro rychlé zpětnovazební smyčky klíčové pro adaptivní modulaci, kódování a HARQ.

## K čemu slouží

E-DPCH byl zaveden, aby vyřešil požadavky na řídicí signalizaci pro nový vylepšený vyhrazený kanál (E-DCH) v HSUPA, definovaný ve 3GPP Release 6. Před HSUPA byla uplink paketová data v UMTS závislá na vyhrazeném kanálu (DCH), který byl plánován radiovou síťovou kontrolérkou (RNC) s vysokou latencí (desítky až stovky milisekund). Tato architektura byla nevhodná pro praskavý, interaktivní datový provoz. HSUPA přesunulo rychlé plánování do Node B, aby se snížila latence a zlepšila spektrální účinnost, ale to vyžadovalo nový řídicí kanál s nízkou latencí pro přenos potřebné signalizace mezi UE a Node B.

E-DPCH byl vytvořen speciálně pro přenos časově kritických řídicích informací, které umožňují toto plánování Node B. Bez něj by Node B bylo slepé vůči přenosovému formátu a stavu HARQ od UE, což by znemožnilo koherentní demodulaci a efektivní přidělování zdrojů. Řeší omezení stávajícího DPCCH, který byl navržen pro řízení přepojování okruhů a nižších rychlostí paketových dat a nemohl podporovat dynamické změny rychlosti a HARQ zpětnou vazbu vyžadovanou pro HSUPA. E-DPCH je tedy umožňující protějšek řídicí roviny k datové rovině E-DPDCH a tvoří kompletní fyzickou vrstvu pro vysokorychlostní uplink přenosy.

Jeho zavedení bylo motivováno rostoucí poptávkou po symetrických širokopásmových službách, jako je nahrávání videa, přenosy velkých souborů a hraní her v reálném čase, kde se výkon uplinku stával úzkým hrdlem. Poskytnutím vyhrazeného a robustního řídicího kanálu E-DPCH zajistil, že zisky z rychlejšího plánování a pokročilé adaptace spoje v HSUPA mohly být plně realizovány, což učinilo UMTS konkurenceschopným vůči vznikajícím širokopásmovým bezdrátovým technologiím.

## Klíčové vlastnosti

- Přenáší indikátor kombinace transportního formátu E-DCH (E-TFCI) pro signalizaci datové rychlosti
- Přenáší číslo sekvence pro retransmise (RSN) pro správu procesů HARQ
- Obsahuje Happy Bit pro zpětnou vazbu UE k plánovacím povolením
- Používá pevný šířicí faktor pro spolehlivý příjem řídicích dat
- Podléhá rychlé uzavřené smyčce regulace výkonu pro robustnost spoje
- Je vždy vysílán současně s E-DPDCH během aktivity HSUPA

## Související pojmy

- [E-DPDCH – E-DCH Dedicated Physical Data Channel](/mobilnisite/slovnik/e-dpdch/)
- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [DPCH – Dedicated Physical Channel](/mobilnisite/slovnik/dpch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples

---

📖 **Anglický originál a plná specifikace:** [E-DPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-dpch/)
