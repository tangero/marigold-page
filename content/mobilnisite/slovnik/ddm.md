---
slug: "ddm"
url: "/mobilnisite/slovnik/ddm/"
type: "slovnik"
title: "DDM – Data Description Method"
date: 2025-01-01
abbr: "DDM"
fullName: "Data Description Method"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ddm/"
summary: "DDM je standardizovaná metoda pro popis a strukturování dat výkonnostních měření v sítích 3GPP. Definuje formální jazyk a rámec pro vytváření datových popisů (DD), které specifikují formát, sémantiku"
---

DDM je standardizovaná metoda pro popis a strukturování dat výkonnostních měření v sítích 3GPP, která umožňuje konzistentní sběr, reportování a analýzu.

## Popis

Metoda popisu dat (Data Description Method, DDM) je klíčovou součástí architektury správy výkonnosti (Performance Management, [PM](/mobilnisite/slovnik/pm/)) 3GPP, specifikovanou primárně v technických specifikacích řady 32. Poskytuje standardizovaný, na technologii nezávislý jazyk pro definování struktury a významu dat výkonnostních měření. Datový popis (Data Description, [DD](/mobilnisite/slovnik/dd/)) je formální, strojově čitelný dokument, který přesně specifikuje výkonnostní metriky včetně jejich názvů, datových typů, jednotek, povolených hodnot a sémantických definic. DD se používají ke konfiguraci sběru dat výkonnostních měření (PM) v síťových prvcích (Network Elements, NEs) a k interpretaci souborů se sebranými daty (PM data files) generovanými těmito prvky.

Architektonicky DDM funguje v rámci definovaném referenčním bodem integrace (Integration Reference Point, [IRP](/mobilnisite/slovnik/irp/)) pro správu výkonnosti. IRP definuje informační model a rozhraní směrem nahoru (jako Itf-N), která používají systémy operační podpory (Operations Support Systems, [OSS](/mobilnisite/slovnik/oss/)) ke správě síťových prvků. DDM poskytuje konkrétní syntaxi a sémantiku pro vytvoření instance tohoto informačního modelu pro konkrétní typy měření. Klíčovou součástí je jazyk popisu dat (Data Description Language, DDL), který se používá k vytváření DD. Tyto DD jsou následně nasazeny jak do síťových prvků (které je používají k formátování výstupních dat), tak do OSS (které je používají k parsování a porozumění příchozím datovým proudům). Tím je zajištěno, že producent ([NE](/mobilnisite/slovnik/ne/)) a konzument (OSS) výkonnostních dat mají sdílené, jednoznačné porozumění obsahu dat.

Metoda funguje na principu oddělení definice *co* se měří od implementace *jak* se to měří. Dodavatelé síťových zařízení implementují sběr měření podle pravidel v DD. Výstupem jsou strukturované datové soubory (např. kódované v [XML](/mobilnisite/slovnik/xml/) nebo ASN.1), jejichž schéma je přímo odvozeno z DD. Toto oddělení je klíčové pro interoperabilitu. Aby OSS mohlo zpracovávat PM soubory z nového síťového prvku nebo nové verze, potřebuje pouze odpovídající DD soubor, nikoli nový parsovací kód pro každého dodavatele nebo verzi. DDM pokrývá široké spektrum výkonnostních dat včetně měření čítačů, měření stavových veličin, kontrol stavu a složitých odvozených měření, čímž podporuje komplexní monitorování potřebné pro sítě 2G, 3G, 4G a 5G.

Role DDM je zásadní pro automatizovanou správu výkonnosti sítě. Umožňuje sítím s více dodavateli a technologiemi reportovat výkonnostní data konzistentním způsobem. Tato konzistence je předpokladem pro efektivní správu poruch, zajištění služeb, plánování kapacity a úlohy optimalizace sítě prováděné OSS. Poskytnutím rigorózního, standardizovaného popisného jazyka DDM snižuje integrační náklady, minimalizuje chyby v interpretaci dat a usnadňuje vývoj obecných OSS aplikací, které mohou pracovat s výkonnostními daty od jakéhokoli kompatibilního síťového prvku.

## K čemu slouží

DDM byla vytvořena k řešení základního problému v řízení telekomunikačních sítí: absence standardizovaného, na dodavateli nezávislého způsobu definice a výměny dat výkonnostních měření. Před jejím zavedením v 3GPP Release 6 používali dodavatelé síťových zařízení často proprietární formáty a definice pro výkonnostní čítače a metriky. To vytvářelo významné integrační výzvy pro síťové operátory, kteří nasazovali sítě s více dodavateli. [OSS](/mobilnisite/slovnik/oss/) operátora vyžadovalo vlastní parsery a adaptéry pro zařízení každého dodavatele, což vedlo k vysokým integračním nákladům, prodlouženým cyklům nasazení a vysokému riziku chybné interpretace dat kvůli nejednoznačným definicím.

Primární motivací bylo umožnit skutečnou interoperabilitu v oblasti správy výkonnosti. Definováním formální popisné metody chtěl 3GPP oddělit definici dat od přenosu dat a OSS aplikací. To umožňuje dodavatelům inovovat v implementacích sběru měření, přičemž zaručuje, že výstupní data mohou být univerzálně pochopena. Historickým kontextem byla rostoucí složitost sítí 3G a snaha průmyslu o standardizovaná, otevřená rozhraní managementu jako součást rámců Telecom Management Network ([TMN](/mobilnisite/slovnik/tmn/)) a později NGOSS (Next Generation Operations Systems and Software). DDM přímo řeší omezení ad-hoc, bilaterálních dohod o datových formátech tím, že poskytuje jediný, autoritativní zdroj pravdy pro sémantiku výkonnostních metrik.

DDM navíc podporuje vývoj síťových technologií. Když 3GPP zavádělo nové technologie rádiového přístupu (HSPA, LTE, NR) a architektury jádra sítě (EPC, 5GC), bylo třeba rámec správy výkonnosti rozšířit, aniž by došlo k narušení stávajících systémů. DDM poskytuje rozšiřitelnost pro definování nových měření pro nové síťové funkce a služby při zachování zpětné kompatibility. Řeší problém škálování síťového managementu pro stále více heterogenní a softwarově definované sítě a zajišťuje, že výkonnostní data zůstávají spolehlivým zdrojem pro autonomní optimalizaci sítě a operace řízené AI/ML.

## Klíčové vlastnosti

- Standardizovaný jazyk popisu dat (Data Description Language, DDL) pro definování výkonnostních metrik
- Na technologii nezávislý rámec použitelný pro síťové prvky 2G, 3G, 4G a 5G
- Umožňuje jednoznačnou sémantickou definici čítačů, stavových veličin a kontrol stavu
- Odděluje produkci dat v síťových prvcích (Network Elements) od spotřeby dat v OSS
- Podporuje generování interoperabilních PM datových souborů (např. ve formátu XML)
- Usnadňuje automatizovanou konfiguraci sběru výkonnostních dat prostřednictvím IRP rozhraní

## Související pojmy

- [IRP – Integration Reference Point](/mobilnisite/slovnik/irp/)
- [NE – Network Element](/mobilnisite/slovnik/ne/)

## Definující specifikace

- **TS 23.241** (Rel-6) — Data Description Method for Generic User Profile
- **TR 23.941** (Rel-6) — 3GPP Generic User Profile Data Description
- **TS 32.140** (Rel-19) — Subscription Management (SuM) requirements

---

📖 **Anglický originál a plná specifikace:** [DDM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ddm/)
