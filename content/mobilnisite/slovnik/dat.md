---
slug: "dat"
url: "/mobilnisite/slovnik/dat/"
type: "slovnik"
title: "DAT – Digital Audio Tape"
date: 2025-01-01
abbr: "DAT"
fullName: "Digital Audio Tape"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dat/"
summary: "DAT je formát digitálního záznamu zvuku na magnetickou pásku, standardizovaný pro použití v telekomunikačních systémech. Byl specifikován v 3GPP pro vysoce kvalitní záznam, ukládání a přehrávání zvuku"
---

DAT je standardizovaný formát digitální magnetické pásky používaný v telekomunikačních systémech pro vysoce kvalitní záznam, ukládání a přehrávání zvuku v síťových prvcích, jako jsou hlasové schránky.

## Popis

Digital Audio Tape (DAT) je médium pro záznam a přehrávání signálu vyvinuté v 80. letech 20. století, využívající technologii šikmého záznamu s rotujícími hlavami na kazetách s magnetickou páskou. V kontextu specifikací 3GPP je DAT uváděn jako standardizovaný formát digitálního zvukového úložiště pro telekomunikační zařízení, zejména v oblasti hlasových služeb a doplňkových služeb. Tato technologie kóduje zvukové signály pomocí pulzně kódové modulace (PCM), typicky se vzorkovací frekvencí 48 kHz, 44,1 kHz nebo 32 kHz a s 16bitovou lineární kvantizací, což poskytuje vysokou věrnost zvuku vhodnou pro profesionální a telekomunikační aplikace. Mechanismus šikmého záznamu, při kterém se páska omotává kolem rotujícího bubnu obsahujícího záznamové a čtecí hlavy, umožňuje vysokou hustotu dat a robustní opravu chyb, což jej činí spolehlivým pro dlouhodobé ukládání zvukových zpráv, jako jsou ty v systémech hlasových schránek.

V rámci architektury 3GPP jsou rozhraní a schopnosti DAT definovány v technických specifikacích, jako jsou 3GPP TS 26.975 a 3GPP TS 46.008, které detailně popisují zvukové kodeky a akustické charakteristiky terminálů, a 3GPP TS 26.978 a 3GPP TS 46.055, které pokrývají výkon řečových kodeků a síťové zpracování zvuku. Zařízení vybavená DAT, jako jsou síťové záznamové systémy, se integrují s prvky jádra sítě pro zachycení, uložení a načtení zvukových dat. Role tohoto formátu spočívá v zajištění, aby zvukové záznamy – například zprávy v hlasové schránce nebo záznamy hovorů – zachovávaly konzistentní kvalitu a byly přístupné napříč různými síťovými uzly, čímž podporují interoperabilitu mezi zařízeními od různých výrobců.

Technická implementace DAT v systémech 3GPP zahrnuje specifikace pro mechanismy transportu pásky, schémata digitálního kódování a protokoly pro zpracování chyb. Mezi klíčové komponenty patří kazeta DAT (s definovanými rozměry pásky a kapacitou úložiště), buben s rotujícími hlavami pro operace čtení/zápisu a přidružené digitální signálové procesory pro kódování/dekódování zvukových proudů. Integrace DAT do telekomunikačních sítí často zahrnuje rozhraní k přepojovacím centrům nebo mediálním serverům, kde slouží jako médium hromadného úložiště. Jeho případy použití sahají k záznamům pro zákonné odposlechy, službám hlasových oznámení a zvukovému logování, využívaje jeho nevolatilní úložiště a charakteristiky sekvenčního přístupu.

Význam DAT v 3GPP spočívá v poskytnutí standardizovaného řešení pro vysoce kvalitní archivaci zvuku během přechodu od analogových k digitálním telekomunikacím. Ačkoli je dnes již převážně historický, představoval klíčovou technologii pro zajištění věrnosti a spolehlivosti zvuku v raných vydáních 3GPP, zejména pro služby související s hlasem. Specifikace zajišťovaly, že systémy DAT dokážou zvládnout dynamický rozsah a frekvenční odezvu požadovanou pro telefonní zvuk, s podporou více vzorkovacích frekvencí pro vyvážení kvality a efektivity úložiště. Kódy pro opravu chyb, jako jsou ty definované ve formátu DAT, zmírňovaly ztrátu dat způsobenou vadami pásky, což bylo klíčové pro zachování integrity u kritických záznamů.

## K čemu slouží

DAT byl vyvinut, aby řešil omezení analogových formátů zvukové pásky, jako jsou kazety, které trpěly degradací poměru signálu k šumu, wow-and-flutter a omezeným dynamickým rozsahem v průběhu času a používání. V telekomunikacích se potřeba spolehlivého, vysoce věrného digitálního úložného média stala naléhavou s nástupem digitálních hlasových služeb, jako jsou hlasové schránky a systémy interaktivní hlasové odezvy ([IVR](/mobilnisite/slovnik/ivr/)), na konci 20. století. 3GPP standardizovalo DAT, aby zajistilo, že síťoví operátoři mohou nasadit interoperabilní zařízení pro záznam zvuku schopná zachovat kvalitu zvuku při opakovaném přehrávání a dlouhodobém skladování, čímž řešily problémy s konzistencí zvuku a archivní trvanlivostí v rozvíjejících se digitálních sítích.

Historický kontext pro zařazení DAT do specifikací 3GPP pochází z konce 80. a 90. let 20. století, kdy se digitální zvuková technologie rychle rozvíjela a telekomunikační sítě přecházely z analogové na digitální infrastrukturu. Předchozí přístupy spoléhaly na analogovou pásku nebo rané digitální formáty s proprietárními implementacemi, což vedlo k problémům s kompatibilitou a proměnlivým výkonem zvuku. Standardizací DAT poskytlo 3GPP společný referenční bod pro výrobce, což umožnilo bezproblémovou integraci podsystémů pro ukládání zvuku do síťových prvků. To usnadnilo nasazení přidaných služeb závislých na vysoce kvalitním přehrávání zvuku, jako jsou prémiové hlasové schránky nebo informační služby založené na zvuku.

DAT řešil konkrétní telekomunikační výzvy tím, že nabídl robustní úložné médium s lineárním přístupem a osvědčenou spolehlivostí v profesionálním zvukovém prostředí. Jeho digitální povaha eliminovala generační ztráty spojené s analogovým kopírováním, což bylo nezbytné pro právní a regulační záznamy. Kapacita a odolnost formátu jej činily vhodným pro rozsáhlá síťová nasazení, kde bylo potřeba ukládat tisíce zvukových zpráv. Ačkoli byl později nahrazen polovodičovými a diskovými úložišti, role DAT v raných vydáních 3GPP byla klíčová pro stanovení měřítek kvality zvuku a interoperability úložišť v telekomunikacích.

## Klíčové vlastnosti

- Šikmý záznam s rotujícími hlavami pro vysokou hustotu dat
- Kódování zvuku PCM při vzorkovacích frekvencích 48 kHz, 44,1 kHz nebo 32 kHz
- 16bitová lineární kvantizace poskytující široký dynamický rozsah
- Integrovaná oprava chyb pro integritu dat na magnetické pásce
- Standardizovaný faktor kazety pro interoperabilitu
- Podpora sekvenčního přístupu a dlouhodobého archivního úložiště

## Definující specifikace

- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance
- **TS 46.055** (Rel-19) — GSM Enhanced Full Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [DAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/dat/)
