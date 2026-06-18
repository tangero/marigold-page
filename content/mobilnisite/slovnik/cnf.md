---
slug: "cnf"
url: "/mobilnisite/slovnik/cnf/"
type: "slovnik"
title: "CNF – Conjunctive Normal Form"
date: 2025-01-01
abbr: "CNF"
fullName: "Conjunctive Normal Form"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cnf/"
summary: "Standardizovaný formát logického výrazu používaný ve specifikacích 3GPP, zejména v pravidlech pro řízení politik a účtování (PCC). Reprezentuje složité podmínky jako konjunkci (AND) disjunkcí (OR), co"
---

CNF je standardizovaný formát logického výrazu používaný ve specifikacích 3GPP k jednoznačné definici složitých podmínek politik jako konjunkce disjunkcí.

## Popis

Konjunktivní normální forma (CNF) v 3GPP je formální logická reprezentace používaná k vyjádření složitých podmínek, primárně v rámci architektur Řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) definovaných ve specifikacích jako TS 29.501. Strukturuje logické výrazy do standardizovaného formátu sestávajícího z konjunkce (logického [AND](/mobilnisite/slovnik/and/)) jedné či více klauzulí, kde každá klauzule je disjunkcí (logickým [OR](/mobilnisite/slovnik/or/)) literálů. Literál představuje základní atomickou podmínku, která může být buď kladným tvrzením (např. 'uživatel je v roamingu'), nebo negovaným tvrzením (např. 'uživatel NENÍ v domácí síti'). Tato hierarchická struktura umožňuje síťovým politikám kódovat mnohostranná pravidla, která musí vyhodnocovat více kritérií současně.

Architektonicky je CNF používána uvnitř Funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) k definici pravidel politik, která jsou následně vynucována Funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) a Funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)). Když PCF generuje PCC pravidla pro relaci protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)), může použít CNF k určení spouštěcích podmínek těchto pravidel. Například pravidlo může platit pouze, pokud ((podmínka A NEBO podmínka B) A (podmínka C NEBO [NE](/mobilnisite/slovnik/ne/) podmínka D)). Formát CNF zajišťuje, že tyto složené podmínky jsou parsovány a vyhodnocovány konzistentně napříč různými síťovými funkcemi, čímž zabraňuje chybným interpretacím, které by mohly vzniknout z nejednoznačného přirozeného jazyka nebo ad-hoc logických reprezentací.

Z provozní perspektivy, když dojde k síťové události (jako změna lokace uživatele, denní doba nebo předplacená služba), příslušná síťová funkce vyhodnotí CNF výraz vůči aktuálním parametrům relace. Každý literál je zkontrolován na pravdivostní hodnotu, poté jsou vyhodnoceny disjunkce uvnitř klauzulí a nakonec konjunkce všech klauzulí určí, zda je celková podmínka splněna. Toto vyhodnocení spustí odpovídající akce, jako je změna parametrů kvality služby (QoS), aplikace tarifních sazeb nebo přesměrování provozu. Použití standardu formální logiky jako CNF je klíčové v servisně orientované architektuře 5G, kde musí být politiky dynamicky aplikovány napříč distribuovanými, cloud-nativními funkcemi.

Klíčové komponenty v CNF výrazu zahrnují literály (atomické podmínky odkazující na standardizované parametry), klauzule (disjunkce literálů) a celkovou konjunkci spojující klauzule. Parametry odkazované v literálech jsou definovány ve specifikacích 3GPP a mohou zahrnovat lokaci uživatelského zařízení (UE), identifikátor síťového řezu, název datové sítě (DNN), identifikátor aplikace, časová okna a stav roamingu. Strukturováním politik do CNF umožňuje 3GPP složitá, vícerozměrná rozhodnutí politik, která se přizpůsobují podmínkám sítě v reálném čase a kontextu uživatele, čímž podporují pokročilé schopnosti 5G, jako je síťové řezání a diferencovaná QoS.

## K čemu slouží

CNF byla zavedena k řešení problému nejednoznačné a nekonzistentní interpretace složitých podmínek politik v telekomunikačních sítích. Před standardizací často používala pravidla politik proprietární nebo neformální logické výrazy, což vedlo k problémům s interoperabilitou mezi síťovými funkcemi od různých dodavatelů. Jak se sítě 5G vyvíjely s sofistikovanějšími službami, jako je síťové řezání, edge computing a IoT, potřeba přesných, strojově čitelných definic politik se stala kritickou. CNF poskytuje matematicky rigorózní formát, který eliminuje nejednoznačnost, a zajišťuje, že pravidla politik jsou prováděna přesně podle záměru napříč celým síťovým ekosystémem.

Vznik CNF byl motivován posunem k deklarativní správě politik v architektuře 5G 3GPP. Na rozdíl od procedurálních přístupů, kde je logika politik pevně zakódována, deklarativní politiky specifikují 'co' se má stát za určitých podmínek, nikoliv 'jak' to implementovat. CNF slouží jako formální jazyk pro tyto podmínky, což umožňuje PCF generovat přenositelná pravidla politik, která mohou být distribuována různým vynucovacím bodům. Tím se řeší omezení dřívějších architektur politik (jako ty v 4G), které byly méně flexibilní a obtížně zvládaly složité, víceatributové podmínky vyžadované pro případy užití 5G.

Historicky se řízení politik v mobilních sítích vyvinulo od jednoduchých pravidel založených na úrovni předplatitele k dynamickým politikám zohledňujícím kontext v reálném čase. CNF tuto evoluci podporuje tím, že poskytuje škálovatelný způsob kódování složité obchodní logiky a technických omezení. Například poskytovatel služeb může vytvořit politiku, která nabízí vylepšenou QoS pouze tehdy, když je uživatel v konkrétní geografické oblasti, během pracovní doby a používá konkrétní aplikaci, a zároveň nerouminguje. Spolehlivá reprezentace takové mnohostranné podmínky vyžaduje formální logický systém jako CNF, který zajišťuje, že všechny síťové komponenty vyhodnotí pravidlo stejně, čímž se udržuje integrita služby a soulad se smlouvami o úrovni služeb (SLA).

## Klíčové vlastnosti

- Standardizovaný logický formát pro jednoznačné vyhodnocení podmínek politik
- Podporuje konjunkci (AND) disjunkčních (OR) klauzulí pro definici složitých pravidel
- Umožňuje dynamickou adaptaci politik na základě více parametrů v reálném čase
- Usnadňuje interoperabilitu mezi síťovými funkcemi od více dodavatelů
- Integruje se s Funkcí řízení politik (PCF) 5G pro deklarativní správu politik
- Odkazuje na standardizované parametry jako lokace, ID řezu, DNN a ID aplikace

## Definující specifikace

- **TS 29.501** (Rel-19) — 5GC SBI API Design Principles & Guidelines

---

📖 **Anglický originál a plná specifikace:** [CNF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cnf/)
