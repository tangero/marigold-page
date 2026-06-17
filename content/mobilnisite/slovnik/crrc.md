---
slug: "crrc"
url: "/mobilnisite/slovnik/crrc/"
type: "slovnik"
title: "CRRC – Conformance Requirement Reference Context Error"
date: 2025-01-01
abbr: "CRRC"
fullName: "Conformance Requirement Reference Context Error"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/crrc/"
summary: "CRRC je koncept testování shody ve specifikacích 3GPP pro USIM a UICC. Definuje konkrétní chybový stav používaný k ověření, že zařízení správně zpracovává neplatné nebo neočekávané referenční kontexty"
---

CRRC je chybový stav při testování shody ve specifikacích 3GPP, který slouží k ověření, že USIM nebo UICC správně zpracovává neplatné referenční kontexty, a tím zajišťuje robustní interoperabilitu.

## Popis

Conformance Requirement Reference Context Error (CRRC) je podrobný testovací mechanismus specifikovaný v sadách testů shody 3GPP, primárně dokumentovaný v technických specifikacích 31.213 (pro USIM Application Toolkit) a 51.013 (pro testování shody rozhraní UICC-terminál). Funguje tak, že definuje přesný chybový scénář, kdy je terminálu (např. mobilnímu telefonu) nebo USIM předložen neplatný nebo neexistující 'referenční kontext' během standardizované procedury. Referenční kontext je v podstatě ukazatel nebo identifikátor pro konkrétní relaci, soubor nebo datový objekt, který je zpracováván. Hlavní funkcí testování CRRC je stanovit, že testovaná entita musí tuto chybnou podmínku správně detekovat a reagovat na ni určenou chybovou odpovědí, jako je přesný kód SW (Status Word), aniž by došlo k pádu nebo projevila nedefinované chování. Toto ověření je klíčové pro zajištění robustnosti implementací vůči chybně vytvořeným nebo neočekávaným vstupům, které mohou vzniknout z chyb signalizace sítě nebo problémů s interoperabilitou zařízení různých výrobců.

Z architektonického hlediska jsou testy CRRC integrovány do širšího Test Execution Environment (TEE) pro shodu UICC/USIM. Testovací systém funguje jako tester, simuluje buď síťovou stranu, nebo stranu terminálu, aby vložil chybný referenční kontext do protokolového dialogu, jako je PROACTIVE COMMAND z USIM nebo příkaz FETCH z terminálu. Systém poté sleduje odpověď testovaného zařízení (Device Under Test, [DUT](/mobilnisite/slovnik/dut/)) – což může být aplikace USIM nebo rozhraní UICC terminálu. Mezi klíčové součásti patří testovací zařízení (Tester Equipment), DUT a přesná definice testovacího případu, která popisuje počáteční podmínky, podnět (příkaz s neplatným kontextem) a očekávaný výsledek (přesná chybová odpověď). Testovací případy jsou často strukturovány pomocí Tree and Tabular Combined Notation (TTCN-3) pro formální specifikaci chování.

Úloha CRRC v síťovém ekosystému je základní pro spolehlivost a bezpečnost. Důsledným testováním zpracování chyb zabraňuje situacím, kdy by vadná SIM karta nebo chybová implementace terminálu mohla způsobit výpadek služby, bezpečnostní zranitelnost nebo selhání interoperability ve vícevýrobcové síti. Například pokud USIM odešle příkaz k zobrazení textu, ale použije neplatný identifikátor kontextu, terminál jej musí bezpečně odmítnout. Tím je zajištěno, že uživatelský zážitek zůstává stabilní a že síťově iniciované procedury (jako je obnovení nastavení služeb) jsou zpracovány korektně i v okrajových případech. Tento koncept, i když se zdá být nízkourovňový, je základním kamenem filozofie 'defenzivního programování' zabudované ve standardech 3GPP, která zaručuje, že všechna certifikovaná zařízení splňují minimální práh robustnosti.

## K čemu slouží

CRRC bylo vytvořeno k řešení základní potřeby v telekomunikační standardizaci: zajištění předvídatelného a interoperabilního zpracování chyb. Před formalizovaným testováním shody mohli různí výrobci implementovat své vlastní, často nekonzistentní reakce na neplatné protokolové stavy. To vedlo k selhání interoperability, kdy zařízení A mohlo spadnout při přijetí chybně vytvořených dat ze sítě B, zatímco zařízení C je mohlo ignorovat bez reakce, což mohlo vést k bezpečnostním mezerám nebo degradaci služeb. Zavedení CRRC ve verzi Release 8 jako součásti vyvíjejících se testovacích rámců USIM Application Toolkit (USAT) a UICC poskytlo standardizovaný, testovatelný požadavek na správu chyb referenčních kontextů, což znamenalo posun od funkčního testování k zahrnutí negativních testovacích případů.

Primární problém, který CRRC řeší, je nedostatečná robustnost rozhraní UICC-terminál, které představuje kritickou hranici důvěry v mobilních sítích. USIM obsahuje citlivá data účastníka a spouští applety, které mohou ovládat chování terminálu. Nesprávně zpracovaná chyba by mohla být zneužita k vyvolání odmítnutí služby, úniku informací nebo k nepředvídatelnému chování. Definováním přesných chybových stavů a povinných odpovědí CRRC odstraňuje nejednoznačnost pro implementátory a poskytuje testovacím laboratořím jasné kritérium úspěšnosti/neúspěšnosti. To bylo motivováno rostoucí složitostí aplikací na SIM kartách (od základní telefonie po platební a identifikační služby) a nutností odolnějšího mobilního ekosystému s vývojem sítí od 3G přes 4G a dále.

Historicky měly dřívější verze standardů méně přísné testování shody pro chybové scénáře. CRRC tuto oblast formalizovalo a řešilo tak omezení ad-hoc zpracování chyb. Zajišťuje, že všechna certifikovaná zařízení reagují jednotně při konfrontaci se stejným chybným vstupem, což je nezbytné pro rozsáhlé a spolehlivé síťové operace a pro udržení důvěry uživatelů v bezpečnost služeb založených na SIM. Je to klíčový prvek pro prevenci provozních selhání, která je obtížné diagnostikovat a napravit po nasazení.

## Klíčové vlastnosti

- Definuje standardizované chybové stavy pro neplatné referenční kontexty v procedurách USIM/UICC
- Specifikuje povinné chybové kódy odpovědí (např. konkrétní bajty SW) pro kompliantní implementace
- Integrováno do formálních sad testů shody (TS 31.213, TS 51.013) s využitím TTCN-3
- Testuje schopnosti zpracování chyb na straně terminálu i na straně USIM
- Zvyšuje interoperabilitu zajištěním jednotného chování napříč zařízeními různých výrobců
- Zlepšuje robustnost sítě a zařízení vůči chybně vytvořené signalizaci a protokolovým chybám

## Definující specifikace

- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TS 51.013** (Rel-19) — SIM API for Java Card Test Specification

---

📖 **Anglický originál a plná specifikace:** [CRRC na 3GPP Explorer](https://3gpp-explorer.com/glossary/crrc/)
