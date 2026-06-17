---
slug: "ftnw"
url: "/mobilnisite/slovnik/ftnw/"
type: "slovnik"
title: "FTNW – Forwarded-To NetWork"
date: 2025-01-01
abbr: "FTNW"
fullName: "Forwarded-To NetWork"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ftnw/"
summary: "Parametr identifikátoru sítě používaný ve službách přesměrování hovorů, zejména pro Optimal Routing (OR) a Camel. Určuje síť (např. PLMN), na kterou je hovor přesměrován, nikoli konkrétní číslo účastn"
---

FTNW je parametr identifikátoru sítě používaný ve službách přesměrování hovorů, který určuje síť, na kterou je hovor přesměrován, což napomáhá efektivnímu směrování mezi sítěmi a spouštění služeb.

## Popis

Forwarded-To NetWork (FTNW) je parametr identifikátoru na úrovni sítě používaný v pokročilých scénářích přesměrování a směrování hovorů v sítích GSM/UMTS. Na rozdíl od [FTN](/mobilnisite/slovnik/ftn/), které určuje cílové telefonní číslo, FTNW určuje veřejnou pozemní mobilní síť (PLMN) nebo jinou síťovou doménu, na kterou má být hovor směrován. Tento parametr je zvláště relevantní v kontextu služeb Camel (Customised Applications for Mobile network Enhanced Logic) a procedur Optimal Routing ([OR](/mobilnisite/slovnik/or/)), kde je vyžadována optimalizace cesty hovoru a řízení služeb přes hranice sítí.

Z architektonického hlediska je FTNW uloženo v [HLR](/mobilnisite/slovnik/hlr/) spolu s daty o přesměrování nebo v souvislosti s nimi. Když je vyvolána podmínka přesměrování hovoru a je určeno, že cílový bod přesměrování je v jiné síti, může být FTNW poskytnuto bránovému [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) nebo jiným směrovacím uzlům. To informuje směrovací logiku, že hovor má být nasměrován na konkrétní identifikátor sítě (např. kombinaci Mobile Country Code a Mobile Network Code – [MCC](/mobilnisite/slovnik/mcc/)/[MNC](/mobilnisite/slovnik/mnc/)) pro další zpracování. GMSC může tuto informaci použít k výběru vhodného výstupního trunku nebo signalizační trasy směrem k této síti.

Ve scénářích Camel hraje FTNW roli v dialogu mezi gsmSCF (řídicí funkcí služeb Camel) a GMSC nebo MSC. Když služba Camel ovlivňuje přesměrování hovoru, může gsmSCF poskytnout FTNW jako součást svých instrukcí, čímž navádí hovor do sítě, kde se nachází další servisní logika (jako předplacená platforma nebo inteligentní periferie). To umožňuje plynulé rozšíření služeb přes více sítí operátorů a podporuje složité, hodnotou přidané toky hovorů, které závisí na rozhodnutích o směrování s ohledem na síť.

## K čemu slouží

FTNW bylo zavedeno za účelem řešení omezení jednoduchého přesměrování založeného na čísle v prostředí více operátorů a inteligentních sítí. Jak se sítě vyvíjely s Camel a zaměřením na optimální směrování, pouhé zadání cílového čísla ([FTN](/mobilnisite/slovnik/ftn/)) již pro efektivní navázání hovoru nestačilo. Síť potřebovala vědět, *do které* sítě má hovor nejprve odeslat, zejména pro obcházení poplatků (toll bypass), nejlevnější směrování nebo spouštění síťově specifických servisních platforem.

Jeho vytvoření ve verzi Release 4 bylo motivováno potřebou jemnější kontroly nad směrováním hovorů mezi PLMN sítěmi. Řešilo problém suboptimálních cest hovoru, kdy mohl být hovor zbytečně směrován zpět přes domovskou síť, což zvyšovalo náklady a latenci. Zadáním FTNW mohla domovská síť instruovat GMSC, aby směroval hovor přímo k síti, kde se aktuálně nacházel přesměrovaný účastník nebo kde existoval servisní uzel, což umožnilo Optimal Routing. To byl klíčový předpoklad pro nákladově efektivní mezinárodní roaming a pokročilé telefonní služby hostované v síti, které vyžadovaly přesnou kontrolu nad cestou hovoru přes administrativní hranice.

## Klíčové vlastnosti

- Identifikuje cílovou síť (PLMN), nikoli číslo účastníka
- Používá se ve spojení s logikou služeb Camel a procedurami Optimal Routing
- Informuje rozhodnutí GMSC o směrování při přesměrování hovorů mezi sítěmi
- Podporuje scénáře efektivního obcházení poplatků a nejlevnějšího směrování
- Parametr se vyměňuje prostřednictvím signalizace MAP mezi HLR a GMSC/MSC
- Umožňuje spouštění služeb s ohledem na síť pro pokročilé telefonní služby

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1

---

📖 **Anglický originál a plná specifikace:** [FTNW na 3GPP Explorer](https://3gpp-explorer.com/glossary/ftnw/)
