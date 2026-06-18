---
slug: "ibm"
url: "/mobilnisite/slovnik/ibm/"
type: "slovnik"
title: "IBM – Independent Beam Management"
date: 2025-01-01
abbr: "IBM"
fullName: "Independent Beam Management"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ibm/"
summary: "Independent Beam Management (IBM) je technika v 5G NR, kde jsou procedury správy svazků pro uplink a downlink odděleny, což umožňuje jejich nezávislou optimalizaci. To je zvláště výhodné pro systémy s"
---

IBM je technika 5G NR, při které je správa svazků pro uplink a downlink oddělena, aby mohla být optimalizována nezávisle, což přináší výhody pro systémy FDD a asymetrický provoz nebo podmínky na rádiovém kanálu.

## Popis

Independent Beam Management (IBM) je pokročilá technika tvarování svazku standardizovaná ve specifikaci 3GPP Release 16 pro 5G New Radio (NR). V konvenční správě svazků, zejména v systémech s duplexním dělením času ([TDD](/mobilnisite/slovnik/tdd/)), se předpokládá reciprocita směrů svazků pro uplink ([UL](/mobilnisite/slovnik/ul/)) a downlink ([DL](/mobilnisite/slovnik/dl/)) – optimální svazek pro DL se používá i pro UL s využitím reciprocity kanálu. IBM však odděluje procesy správy svazků pro UL a DL, což umožňuje stanici gNB a uživatelskému zařízení (UE) nezávisle vybírat a hlásit nejlepší svazky pro každý směr.

Provoz IBM zahrnuje samostatné procedury a signalizaci pro určení a indikaci svazků pro [UL](/mobilnisite/slovnik/up-link/) a DL. Pro downlink vysílá gNB svazkově formované referenční signály (např. [CSI-RS](/mobilnisite/slovnik/csi-rs/)) a UE provádí měření a hlásí preferovaný DL svazek, podobně jako ve standardních procedurách. Pro uplink je proces nezávislý: UE vysílá svazkově formované referenční signály (např. [SRS](/mobilnisite/slovnik/srs/) – Sounding Reference Signals) pomocí různých svazků a gNB je měří, aby určil optimální UL přijímací svazek na straně gNB. gNB pak může signalizovat preferovaný UL svazek pro UE, nebo si UE může autonomně zvolit svůj UL vysílací svazek na základě samostatných kritérií. Tato nezávislost je umožněna vylepšeními rámce pro hlášení svazků, které dovolují samostatné hlášení stavových informací o svazcích pro UL a DL.

Mezi klíčové komponenty umožňující IBM patří vylepšené SRS zdroje s možnostmi tvarování svazku pro sondování uplinku a vylepšené mechanismy hlášení v MAC-CE nebo [UCI](/mobilnisite/slovnik/uci/) (Uplink Control Information), které mohou nést samostatné informace o indikaci svazků pro UL a DL. IBM je navržena zejména pro systémy [FDD](/mobilnisite/slovnik/fdd/), kde reciprocita kanálu neplatí kvůli různým kmitočtům pro UL a DL, ale přináší výhody i v TDD tím, že umožňuje nezávislou optimalizaci, když je reciprocita nedokonalá kvůli chybám kalibrace hardwaru nebo ve vysoce dynamických mobilních scénářích. Díky nezávislé správě svazků může systém přesněji sledovat rychlé úniky signálu v každém směru, přizpůsobit se asymetrickým podmínkám rušení a lépe podporovat strategie tvarování svazku specifické pro UE, což vede ke zlepšenému rozpočtu spojení, pokrytí a celkové spektrální efektivitě.

## K čemu slouží

IBM byla zavedena, aby řešila omezení předpokladů recipročního tvarování svazků, zejména v nasazeních FDD a v reálných neideálních podmínkách. Raná správa svazků v 5G NR (Rel-15) silně spoléhala na reciprocitu kanálu, která platí primárně pro TDD, kde se stejný kmitočet používá pro oba směry. To znevýhodňovalo systémy FDD, protože nemohly efektivně využít měření DL svazků pro výběr UL svazku, což mohlo vést k suboptimálnímu zacílení svazku a sníženému výkonu v uplinku, který je často kapacitně limitujícím článkem.

Motivace pro IBM vychází z potřeby maximalizovat přínosy tvarování svazků ve všech duplexních režimech a scénářích nasazení. Řeší problém asymetrických podmínek na kanálu mezi UL a DL, které mohou vzniknout z rozdílů v rušení, omezení vysílacího výkonu UE oproti výkonu gNB nebo z charakteristik hardwaru. Díky umožnění nezávislé optimalizace umožňuje IBM sítím dosáhnout vyššího zisku z tvarování svazků v obou spojích, rozšířit pokrytí a zlepšit výkon pro uživatele na okraji buňky. Také usnadňuje efektivnější podporu funkcí, jako je provoz IoT s vysokou zátěží v uplinku, nebo scénářů s vysokou mobilitou UE, kde se optimální svazek může rychle a rozdílně měnit pro každý směr spojení. V podstatě IBM odemyká plný potenciál pokročilého tvarování svazků v širším spektru praktických síťových podmínek a zajišťuje, že výkonnostní výhody 5G nejsou omezeny pouze na ideální nasazení TDD.

## Klíčové vlastnosti

- Odděluje procedury správy svazků pro uplink a downlink
- Umožňuje nezávislý výběr a hlášení svazků pro UL a DL
- Zvláště výhodná pro nasazení NR s FDD, kde neplatí reciprocita
- Využívá vylepšené SRS pro sondování a měření svazků v uplinku
- Podporuje samostatné hlášení stavových informací o svazcích prostřednictvím MAC-CE nebo UCI
- Zlepšuje adaptaci spojení a pokrytí v asymetrických podmínkách na kanálu

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [SRS – Space Radiocommunication Stations](/mobilnisite/slovnik/srs/)
- [FDD – Frequency Division Duplexing](/mobilnisite/slovnik/fdd/)

## Definující specifikace

- **TS 26.264** (Rel-19) — IMS-based AR Real-Time Communication
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TR 38.884** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [IBM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ibm/)
