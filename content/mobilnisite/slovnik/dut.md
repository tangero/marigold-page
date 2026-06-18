---
slug: "dut"
url: "/mobilnisite/slovnik/dut/"
type: "slovnik"
title: "DUT – Device Under Test"
date: 2025-01-01
abbr: "DUT"
fullName: "Device Under Test"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dut/"
summary: "Obecný termín pro jakékoli fyzické nebo logické telekomunikační zařízení (UE, základnová stanice, síťový uzel) podstupující testování shody, výkonu nebo interoperability. Je to centrální předmět testo"
---

DUT je obecný termín pro jakékoli telekomunikační zařízení podstupující testování shody, výkonu nebo interoperability v rámci specifikací 3GPP.

## Popis

V kontextu specifikací 3GPP není Zařízení pod testem (Device Under Test, DUT) konkrétní technologií, ale základním konceptem testovacího a validačního rámce. Odkazuje na entitu, jejíž chování, výkon nebo charakteristiky jsou měřeny a vyhodnocovány vůči normativním požadavkům stanoveným v technických specifikacích 3GPP. DUT může zahrnovat širokou škálu zařízení: uživatelská zařízení (UE), jako jsou smartphony a IoT moduly, uzly rádiového přístupové sítě (RAN), jako jsou gNB a [eNB](/mobilnisite/slovnik/enb/), funkce jádra sítě nebo i celé systémy. Konkrétní identita DUT je definována rozsahem příslušné testovací specifikace (např. TS 36.521-1 pro rádiový přenos a příjem u UE).

Testovací architektura zahrnuje DUT, testovací systém (často zahrnující testovací zařízení, jako jsou emulátory kanálů, generátory signálů a testery protokolů) a přesně definované testovací prostředí specifikované normou. Testovací systém stimuluje DUT řízenými vstupy (signály, zprávami, rádiovými podmínkami) a měří jeho výstupy (vysílaný výkon, míra chyb, protokolové zprávy, časování). Odpovědi DUT jsou pak porovnány s kritérii vyhoví/nevyhoví specifikovanými ve standardu. Testy jsou kategorizovány do oblastí, jako je shoda v rádiových kmitočtech ([RF](/mobilnisite/slovnik/rf/)) (např. výstupní výkon, spektrální maska emisí), správa rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) (např. předávání hovoru, výběr buňky), shoda protokolů (např. signalizace [RRC](/mobilnisite/slovnik/rrc/), [NAS](/mobilnisite/slovnik/nas/)) a testování výkonu (např. propustnost, zpoždění).

Role DUT je pasivní v tom smyslu, že je předmětem testování, ale jeho konfigurace je klíčová. Musí být uvedeno do definovaného referenčního stavu, často za použití specifických testovacích režimů nebo firmwaru, které umožňují reprodukovatelná měření. Při testování UE má DUT typicky Testovací aplikaci nebo používá definovanou signalizaci pro vstup do testovacích smyček. Při testování základnových stanic je DUT konfigurováno se specifickými parametry a připojeno k testovacím UE. Komplexní sada testů DUT zajišťuje, že zařízení od různých výrobců v živých sítích bezproblémově spolupracují, poskytují slibovaný výkon a nezpůsobují škodlivé rušení.

## K čemu slouží

Koncept DUT je základní pro standardizační proces 3GPP, protože umožňuje objektivní ověření shody implementace. Bez standardizovaných testovacích postupů soustředěných na jasně definované DUT by byla interoperabilita mezi sítěmi a zařízeními od více dodavatelů nespolehlivá, což by vedlo k přerušeným hovorům, neúspěšným předáním hovoru a zhoršené kvalitě služeb. Rozmach specifikací souvisejících s DUT ve všech vydáních podtrhuje jeho roli při zajišťování spolehlivosti sítě a uživatelského zážitku.

Historicky, jak se buněčná technologie vyvíjela od GSM přes UMTS a LTE až k současnému 5G NR, složitost rozhraní a protokolů vzrostla exponenciálně. To učinilo ad-hoc testování nedostatečným. Formalizace testování shody založeného na DUT, která robustně začala ve vydání 6 3GPP a dále se rozšiřovala, byla motivována potřebou vytvořit globální certifikační ekosystém (např. prostřednictvím [GCF](/mobilnisite/slovnik/gcf/) a PTCRB). Odstraňuje omezení proprietárního testování tím, že poskytuje společný, jednoznačný standard, kterého musí všichni výrobci dosáhnout, což podporuje zdravou konkurenci, urychluje nasazení technologie a zároveň zachovává integritu sítě.

## Klíčové vlastnosti

- Obecný zástupný symbol reprezentující jakoukoli testovanou entitu, od UE přes gNB až po funkci jádra sítě.
- Předmět široké škály testovacích případů pokrývajících RF, RRM, protokolové a výkonnostní charakteristiky.
- Funguje v řízeném testovacím prostředí definovaném testovacími specifikacemi 3GPP (např. 38.141, 36.521).
- Často vyžaduje specifický provozní režim (např. testovací režim) pro provedení reprodukovatelných testovacích smyček.
- Klíčový pro certifikační programy (GCF, PTCRB) pro vstup na trh.
- Výsledky testů DUT poskytují objektivní důkaz o shodě se standardy a interoperabilitě.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 26.130** (Rel-19) — RTP Payload Format Testing for 3GPP Codecs
- **TR 26.921** (Rel-19) — UE Performance in Ambient Noise
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 36.789** (Rel-13) — LAA Multi-Node Coexistence Test Methodology
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [DUT na 3GPP Explorer](https://3gpp-explorer.com/glossary/dut/)
