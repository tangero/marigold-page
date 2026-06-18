---
slug: "eess"
url: "/mobilnisite/slovnik/eess/"
type: "slovnik"
title: "EESS – Earth Exploration-Satellite Service"
date: 2025-01-01
abbr: "EESS"
fullName: "Earth Exploration-Satellite Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/eess/"
summary: "Služba družicového průzkumu Země (Earth Exploration-Satellite Service, EESS) je radiokomunikační služba definovaná ITU-R pro satelity, které sbírají data o zemském prostředí, včetně počasí, klimatu, o"
---

EESS je využití pozemního IMT spektra satelity pro pozorování Země k přímému přenosu environmentálních dat na zem, což vyžaduje studie koexistence v rámci předpisů 3GPP.

## Popis

V kontextu 3GPP se termín Služba družicového průzkumu Země (Earth Exploration-Satellite Service, EESS) nevztahuje k síťové funkci 3GPP, nýbrž ke kategorii služby definované Sektorem radiokomunikací Mezinárodní telekomunikační unie ([ITU-R](/mobilnisite/slovnik/itu-r/)). Technické specifikace 3GPP (především v řadách 36, 37 a 38) zkoumají koexistenci a potenciální scénáře interference mezi pozemními systémy Mezinárodní mobilní telekomunikace ([IMT](/mobilnisite/slovnik/imt/)), jako je 5G New Radio (NR), a satelitními systémy provozovanými v pásmech pro EESS a službu vesmírného výzkumu (Space Research Service, [SRS](/mobilnisite/slovnik/srs/)). Satelity EESS jsou typicky pasivní (např. měřící odražené sluneční záření) nebo aktivní (např. využívající radarové výškoměry) senzory, které pozorují Zemi pro vědecké a operační účely, jako je meteorologie, klimatologie a monitoring katastrof.

Technická práce v 3GPP zahrnuje studie sdílení a kompatibility. Tyto studie analyzují přenosové charakteristiky jak základnových stanic IMT/koncového zařízení (UE), tak přijímačů/vysílačů satelitů EESS. Mezi klíčové parametry patří spektrální hustota výkonu, charakteristiky antén, scénáře nasazení a požadovaná ochranná kritéria pro citlivé senzory EESS. Cílem je stanovit technické podmínky, jako jsou maximální přípustné úrovně interference nebo potřebné separační vzdálenosti, za kterých mohou sítě IMT fungovat v přidělených pásmech EESS nebo v jejich sousedství, aniž by způsobily škodlivou interferenci těmto kritickým satelitním službám.

3GPP vypracovává technické zprávy (např. TR 38.807, TR 38.820), které dokumentují metodologii studie, předpoklady, výsledky simulací a závěry. Tyto zprávy slouží jako podklad pro národní regulátory a mezinárodní orgány (jako je Světová radiokomunikační konference [ITU](/mobilnisite/slovnik/itu/)) při rozhodování o přidělování spektra a pravidlech jeho sdílení. Tato práce zajišťuje, že rozvoj pozemních sítí 5G nezhorší výkonnost nezbytných satelitů pro environmentální monitoring, které poskytují data klíčová pro předpověď počasí, klimatologii a veřejnou bezpečnost. Zaměřuje se na definici emisních masek, limitů pro mimopásmový únik a dalších technických opatření pro zařízení IMT.

## K čemu slouží

Zařazení studií EESS do pracovního programu 3GPP je motivováno globální poptávkou po dalším rádiovém spektru pro podporu vysokokapacitních pozemních mobilních širokopásmových služeb (5G a dalších generací). Jelikož regulátoři zvažují přerozdělení nebo sdílení stávajících kmitočtových pásem, dostávají se pod drobnohled i pásma přidělená satelitním službám, jako je EESS, a to kvůli jejich často nevyužitému nebo geograficky řídkému využití. EESS je však pro lidstvo kritickou službou a její ochrana je prvořadá. Proto 3GPP jako přední standardizační orgán pro pozemní mobilní komunikace provádí důkladné technické studie, aby zajistilo, že jakékoli potenciální sdílení spektra je proveditelné a bezpečné.

Tato práce řeší problém potenciální interference od hustě nasazených pozemních vysílačů [IMT](/mobilnisite/slovnik/imt/) do vysoce citlivých satelitních přijímačů na oběžné dráze Země. Předchozí generace mobilních sítí fungovaly v nižších kmitočtových pásmech, ale expanze 5G do vyšších frekvencí (např. okolo 24 GHz, 26 GHz) ji přiblížila k pásmům využívaným pro pasivní snímání v rámci EESS (jako je pásmo 23,6–24 GHz používané pro snímání vodní páry). Bez těchto studií a následných standardizovaných mitigačních technik by nekontrolované emise 5G mohly nenávratně poškodit vědecká data shromažďovaná satelity, což by mělo dopad na globální modely předpovědi počasí a klimatický výzkum.

Účel je tedy dvojí: umožnit růst pozemních mobilních sítí průzkumem všech životaschopných možností spektra a naplnit regulační a společenskou odpovědnost za ochranu životně důležitých vědeckých a operačních satelitních služeb. Představuje klíčovou oblast průniku telekomunikačního inženýrství a spektrální politiky, která zajišťuje, že technologický pokrok neprobíhá na úkor schopností environmentálního monitoringu.

## Klíčové vlastnosti

- Zaměření na koexistenci mezi pozemními systémy IMT (5G NR) a satelitními systémy EESS
- Definice metodologií pro hodnocení interference a simulačních scénářů
- Stanovení ochranných kritérií pro pasivní a aktivní senzory EESS
- Vypracování technických podmínek pro sdílení spektra (např. emisní limity)
- Vytváření technických zpráv pro informování globální spektrální regulace
- Zohlednění obou směrů přenosu: uplink (Země–vesmír) i downlink (vesmír–Země)

## Související pojmy

- [ITU-R – International Telecommunication Union Radiocommunication Sector](/mobilnisite/slovnik/itu-r/)

## Definující specifikace

- **TS 36.745** (Rel-14) — Satellite Protection for LTE Bands 11/21
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.749** (Rel-19) — EESS Protection in 23.6-24 GHz for Rel-19
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TR 38.820** (Rel-16) — NR; 7-24 GHz Frequency Range Study

---

📖 **Anglický originál a plná specifikace:** [EESS na 3GPP Explorer](https://3gpp-explorer.com/glossary/eess/)
