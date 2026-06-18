---
slug: "crrp"
url: "/mobilnisite/slovnik/crrp/"
type: "slovnik"
title: "CRRP – Conformance Requirement Reference Parameter Error"
date: 2025-01-01
abbr: "CRRP"
fullName: "Conformance Requirement Reference Parameter Error"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/crrp/"
summary: "CRRP je chybový kód pro testování shody používaný ve specifikacích 3GPP pro testování UICC a USIM. Označuje selhání, při kterém hodnota parametru v testovacím scénáři neodpovídá očekávané referenční h"
---

CRRP je chybový kód při testování shody (conformance testing) podle 3GPP, který signalizuje, že hodnota parametru v testovacím scénáři pro UICC nebo USIM neodpovídá očekávané referenční hodnotě.

## Popis

Conformance Requirement Reference [Parameter](/mobilnisite/slovnik/parameter/) Error (CRRP) je specifická chybová podmínka definovaná v rámci testovacího rámce pro shodu (conformance testing framework) podle 3GPP, primárně dokumentovaná v technických specifikacích 31.213 (pro UICC) a 51.013 (pro [USIM](/mobilnisite/slovnik/usim/)). Funguje jako diagnostický kód používaný během provádění standardizovaných testovacích sad k ověření, že testované zařízení ([DUT](/mobilnisite/slovnik/dut/)), jako je UICC (Universal Integrated Circuit Card) nebo jeho aplikace USIM (Universal Subscriber Identity Module), správně implementuje požadované protokoly a procedury. Chyba je vyvolána, když se hodnota parametru pozorovaná během testovací sekvence odchyluje od přesné referenční hodnoty stanovené v odpovídajícím požadavku na shodu. Tento mechanismus je zásadní pro automatizované testovací procesy prováděné certifikačními laboratořemi a výrobci.

Z architektonického hlediska je CRRP zabudován do logiky testovacího systému, který se skládá z testovacího prováděče (test executor), knihovny testovacích scénářů odpovídajících struktuře testovacích specifikací ([TSS](/mobilnisite/slovnik/tss/)) a účelům testů ([TP](/mobilnisite/slovnik/tp/)) podle 3GPP a testovaného zařízení (DUT). Testovací systém posílá DUT sérii příkazů (např. [APDU](/mobilnisite/slovnik/apdu/) příkazy pro rozhraní UICC) a sleduje odpovědi. Každý testovací scénář je navržen tak, aby ověřil konkrétní požadavek, s předem definovanými očekávanými hodnotami parametrů (referencemi). Když odpověď DUT obsahuje parametr – například stavové slovo (status word), délku datového pole, hodnotu tagu nebo časový limit procedury – který neodpovídá referenční hodnotě, testovací systém zaznamená selhání typu CRRP. Tím přesně identifikuje povahu nesouladu.

Role CRRP v síťovém ekosystému je nepřímá, ale kritická. Je to nástroj pro zajištění, že základní bezpečnostní a identifikační modul (UICC/USIM) v uživatelském zařízení funguje předvídatelně a podle specifikace. Zachycením chyb parametrů během certifikace testování CRRP předchází selháním v provozu, která by mohla vést k problémům s autentizací, výpadkům služeb nebo bezpečnostním zranitelnostem. Testování pokrývá různé aspekty, včetně správy souborů, autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)) a zpracování aplikačních protokolových datových jednotek (APDU). Chyba CRRP nepoukazuje pouze na obecné selhání; konkrétně identifikuje nesoulad na úrovni parametru, což vývojářům umožňuje efektivně ladit a opravovat své implementace, aby dosáhli plné shody před uvedením na trh.

## K čemu slouží

CRRP existuje k vynucení striktního dodržování technických specifikací 3GPP pro komponenty UICC a [USIM](/mobilnisite/slovnik/usim/), které jsou klíčové pro bezpečnou autentizaci účastníka a přístup ke službám v mobilních sítích. Před zavedením standardizovaného testování shody byla interoperabilita mezi síťovými prvky různých výrobců a moduly identifikace účastníka problematická, což vedlo k nekonzistentnímu poskytování služeb a zvýšeným nákladům pro operátory. Vytvoření podrobných testovacích specifikací pro shodu, včetně chybových kódů jako CRRP, bylo motivováno potřebou garantovat, že jakýkoli certifikovaný UICC/USIM bude bezproblémově fungovat v jakékoli kompatibilní síti, čímž se umožnil vznik globálního vícevýrobcového ekosystému pro GSM, UMTS a LTE.

Řešeným problémem je detekce drobných chyb v implementaci, které nemusí způsobit zjevné funkční selhání, ale mohly by vést k nestandardnímu chování, bezpečnostním slabinám nebo neefektivní interakci se sítí. Bez chybového kódu na úrovni parametru, jako je CRRP, by testovací selhání byla obecnější, což by ztížilo a prodloužilo analýzu příčin. Poskytnutím specifického indikátoru pro neshodu referenčního parametru CRRP urychluje certifikační a vývojový cyklus. Odstraňuje tak omezení dřívějších, méně formalizovaných testovacích přístupů, kde se shoda často posuzovala kvalitativně nebo prostřednictvím bilaterálních dohod, což se nehodilo pro globální hromadnou výrobu.

Historicky, jak se mobilní sítě vyvíjely z GSM přes 3G a dále, významně rostla složitost aplikace USIM a jejích protokolů. Zavedení povinného testování shody pro UICC/USIM ve vydání 3GPP Release 8 formalizovalo proces zajišťování kvality. CRRP jako součást tohoto rámce poskytuje potřebnou úroveň podrobnosti pro ověření složitých sekvencí příkazů a odpovědí definovaných ve specifikacích jako 3GPP TS 31.101 (rozhraní UICC-Terminál) a TS 31.102 (charakteristiky USIM). Jeho konečným účelem je ochrana integrity sítě a uživatelského zážitku tím, že zajišťuje soulad každého parametru vyměňovaného mezi terminálem a UICC se standardem.

## Klíčové vlastnosti

- Ověření shody na úrovni parametru
- Integrace do automatizovaných systémů pro provádění testů
- Specifické zaznamenávání chyb pro ladění nevyhovujících implementací
- Použití napříč testovacími specifikacemi pro UICC a USIM (31.213, 51.013)
- Podpora ověřování sekvencí příkazů/odpovědí APDU
- Nezbytný pro certifikační a interoperability testování

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [APDU – Application Protocol Data Unit](/mobilnisite/slovnik/apdu/)

## Definující specifikace

- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TS 51.013** (Rel-19) — SIM API for Java Card Test Specification

---

📖 **Anglický originál a plná specifikace:** [CRRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/crrp/)
