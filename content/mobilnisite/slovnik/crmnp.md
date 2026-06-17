---
slug: "crmnp"
url: "/mobilnisite/slovnik/crmnp/"
type: "slovnik"
title: "CRMNP – Call Related Mobile Number Portability"
date: 2025-01-01
abbr: "CRMNP"
fullName: "Call Related Mobile Number Portability"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/crmnp/"
summary: "CRMNP je služba 3GPP, která umožňuje účastníkům zachovat si svá mobilní telefonní čísla při přechodu k jinému síťovému operátorovi. Zajišťuje směrování hovorů na správnou síť po přenesení čísla, čímž"
---

CRMNP je služba 3GPP, která umožňuje účastníkům zachovat si svá mobilní telefonní čísla při přechodu k jinému síťovému operátorovi a zajišťuje správné směrování hovorů po přenesení čísla.

## Popis

Call Related Mobile Number Portability (CRMNP) je standardizovaná služba definovaná 3GPP, která usnadňuje směrování hlasových hovorů k mobilnímu účastníkovi, který změnil svého poskytovatele služeb, aniž by změnil své původní telefonní číslo ([MSISDN](/mobilnisite/slovnik/msisdn/)). Hlavní technický problém, který řeší, je oddělení identifikátoru účastníka (MSISDN) od jeho původních síťových směrovacích informací. V případě nepřevedeného čísla MSISDN obsahuje vestavěný kód mobilní sítě ([MNC](/mobilnisite/slovnik/mnc/)) a kód mobilní země ([MCC](/mobilnisite/slovnik/mcc/)), který přímo určuje domovskou veřejnou pozemní mobilní síť účastníka ([HPLMN](/mobilnisite/slovnik/hplmn/)). Po přenesení čísla se tato vestavěná data pro účely směrování stanou nesprávnými.

Architektura CRMNP se spoléhá na centralizovanou nebo distribuovanou databázi přenesených čísel ([NPDB](/mobilnisite/slovnik/npdb/)). Když je uskutečněn hovor na přenesené číslo, spínací uzel sítě volajícího (např. Mobile Switching Center nebo Gateway [MSC](/mobilnisite/slovnik/msc/)) musí provést dotaz na přenesení čísla. Tento dotaz, obvykle využívající signalizační protokoly jako Signaling System No. 7 (SS7) nebo Diameter, je odeslán do NPDB. NPDB, která obsahuje mapování všech přenesených čísel na směrovací číslo jejich současné sítě (např. Mobile Station Roaming Number - [MSRN](/mobilnisite/slovnik/msrn/) nebo specifický směrovací prefix), odpoví správnými směrovacími informacemi. Původní síť pak tyto informace použije k směrování hovoru do nové sítě příjemce.

Klíčové součásti procesu CRMNP zahrnují databázi přenesených čísel (NPDB), signalizační přenosový bod (STP) nebo funkci směrování dotazů a síťové spínače (MSC/[GMSC](/mobilnisite/slovnik/gmsc/)). NPDB je autoritativním zdrojem pro mapování přenesených čísel. Funkce směrování dotazů zajišťuje, že dotaz dorazí na správnou NPDB, která může být organizována na národní nebo regionální úrovni. Výkon tohoto mechanismu dotaz-odpověď je klíčový pro dobu navázání hovoru a standardy definují požadavky na minimalizaci prodlevy po vytáčení. CRMNP je primárně funkcí řízení hovorů a signalizace, integrovanou do vrstvy řízení hovorů jádra sítě.

Úlohou CRMNP je učinit přenesení čísla transparentním pro volajícího a bezproblémovým pro volaného. Zajišťuje správnou funkci veřejné telefonní sítě i přes administrativní změnu síťové příslušnosti účastníka. Služba musí zvládat různé scénáře hovorů, včetně hovorů z pevných sítí, mezinárodních hovorů a hovorů, když je přenesený účastník v roamingu. Implementační detaily, jako je spouštěcí bod dotazu (All Call Query, Query on Release atd.) a konkrétní vrácené směrovací číslo, se mohou lišit podle národní regulace a implementace operátora, ale standard 3GPP poskytuje rámec pro interoperabilitu.

## K čemu slouží

CRMNP bylo vytvořeno za účelem splnění regulatorních požadavků stanovených vládami a telekomunikačními úřady za účelem podpory volby spotřebitele a tržní konkurence. Před možností přenést číslo byli účastníci efektivně 'uzamčeni' u svého stávajícího mobilního operátora, protože změna poskytovatele znamenala ztrátu telefonního čísla, což byla významná nepříjemnost a bariéra pro přechod. Tento nedostatek přenositelnosti potlačoval konkurenci, protože noví hráči na trhu nemohli snadno přilákat zákazníky od zavedených operátorů.

Primární problém, který CRMNP řeší, je technické směrování hovorů v prostředí, kde identifikátor účastníka (MSISDN) již automaticky neodkazuje na jeho skutečnou síť. Tradiční plán směrování telefonie byl hierarchický a založený na číslovacím plánu, který přiděloval bloky čísel konkrétním operátorům. CRMNP tento přímý vazeb přerušuje a vyžaduje dynamický vyhledávací mechanismus. Jeho vytvoření bylo motivováno potřebou standardizovaného, na síti nezávislého řešení, které mohou implementovat všichni operátoři na trhu, a které zajišťuje, že hovor na libovolné číslo bude úspěšně dokončen bez ohledu na současného síťového poskytovatele účastníka.

Před CRMNP pro to neexistoval standardizovaný mechanismus, což by vedlo k chaosu v interoperabilitě nebo by vyžadovalo proprietární bilaterální dohody mezi operátory. Definováním CRMNP poskytlo 3GPP jasnou technickou specifikaci, která umožňuje celostátní nebo regionální schémata přenositelnosti čísel. To vyrovnává konkurenční podmínky a je považováno za základní právo na většině moderních telekomunikačních trhů, což přímo přispívá k nižším cenám, lepší kvalitě služeb a inovacím poháněným mobilitou zákazníků.

## Klíčové vlastnosti

- Umožňuje zachování MSISDN při změně operátora mobilní sítě
- Využívá centralizovanou databázi přenesených čísel (NPDB) pro směrovací informace
- Definuje standardizované signalizační procedury pro dotazování na stav přeneseného čísla
- Podporuje různé implementační modely, jako je All Call Query (ACQ)
- Minimalizuje dopad na dobu navázání hovoru prostřednictvím optimalizovaných dotazovacích mechanismů
- Zajišťuje interoperabilitu mezi jádrovými sítěmi různých síťových operátorů

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization

---

📖 **Anglický originál a plná specifikace:** [CRMNP na 3GPP Explorer](https://3gpp-explorer.com/glossary/crmnp/)
