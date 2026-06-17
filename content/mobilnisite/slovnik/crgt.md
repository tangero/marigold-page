---
slug: "crgt"
url: "/mobilnisite/slovnik/crgt/"
type: "slovnik"
title: "CRGT – Charging Tariff Information"
date: 2025-01-01
abbr: "CRGT"
fullName: "Charging Tariff Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/crgt/"
summary: "CRGT je standardizovaná datová struktura v sítích 3GPP, která přenáší podrobné tarifní informace pro účtovací události. Používá ji systém online účtování (Online Charging System, OCS) k určení ceny sl"
---

CRGT je standardizovaná datová struktura v sítích 3GPP, která přenáší podrobné tarifní informace, což umožňuje systému online účtování (Online Charging System) určovat náklady na služby v reálném čase pro přesné vyúčtování.

## Popis

Informace o účtovacím tarifu (Charging Tariff Information, CRGT) je klíčový datový prvek definovaný ve specifikacích 3GPP pro online účtování. Funguje jako kontejner nebo informační prvek, který sděluje konkrétní cenová pravidla a podmínky použitelné pro událost využití síťového prostředku, jako je hlasové volání, datová relace nebo SMS zpráva. CRGT je přenášeno v rámci protokolů pro účtování založených na Diameter, primárně mezi síťovými funkcemi, jako je funkce pravidel řízení a účtování (Policy and Charging Rules Function, PCRF) nebo aplikační funkce (Application Function, [AF](/mobilnisite/slovnik/af/)) a systémem online účtování (Online Charging System, [OCS](/mobilnisite/slovnik/ocs/)). Jeho struktura je navržena jako rozšiřitelná a nese atributy jako tarifní časy (např. sazby ve špičce/mimo špičku), tarifní měny, cenové prvky (náklady na jednotku) a podmínky pro přepnutí tarifu.

Architektonicky CRGT funguje v rámci frameworku 3GPP pro řízení politik a účtování (Policy and Charging Control, PCC). Když uživatel zahájí službu, síť spustí žádost o účtování. Příslušná síťová funkce (např. PCRF přes rozhraní Gx nebo AF přes rozhraní Rx) může zahrnout nebo odkazovat na CRGT v rámci zprávy Diameter Credit-Control-Request ([CCR](/mobilnisite/slovnik/ccr/)) odeslané do OCS. OCS, který spravuje zůstatky účtů předplatitelů a ratingové funkce, analyzuje CRGT, aby aplikoval správný tarif. To umožňuje OCS vypočítat peněžní náklady nebo počet servisních jednotek, které mají být odečteny z účtu uživatele před přidělením kvóty pro službu. OCS poté odpoví zprávou Credit-Control-Answer ([CCA](/mobilnisite/slovnik/cca/)) obsahující přidělenou kvótu, na kterou má vliv vyhodnocení tarifu.

Klíčovými komponentami CRGT jsou páry atribut-hodnota (attribute-value pairs, [AVP](/mobilnisite/slovnik/avp/)) definované v základním protokolu Diameter a rozšířeních 3GPP. Tyto AVP mohou podrobně specifikovat tarifní informace, včetně AVP Tariff-Time-Change (udává, kdy dojde ke změně tarifu), AVP Tariff-Change-Usage (definuje prahovou hodnotu využití pro změnu tarifu) a kódů měn. Tato granularita podporuje složité fakturační modely, jako je vrstvené cení (tiered pricing), slevy podle denní doby a sazby založené na objemu. Jeho role spočívá v oddělení tarifní logiky od jádrové účtovací transakce, což operátorům umožňuje aktualizovat cenové schémata v OCS nebo PCRF bez změny protokolu mezi síťovými prvky, čímž se zvyšuje provozní flexibilita.

V praxi CRGT umožňuje online účtování v reálném čase s ohledem na relaci. Například během datové relace může PCRF informovat OCS, že prvních 100 MB se účtuje jednou sazbou (tarif 1) a jakékoli následné využití jinou sazbou (tarif 2), přičemž CRGT nese tyto podmínky. OCS to používá ke sledování využití vůči prahovým hodnotám a k dynamickému přepínání tarifů. Tento mechanismus je zásadní pro implementaci politik spravedlivého využití (fair usage), propagačních nabídek a sofistikovaných služebních plánů. Zajišťuje, že účtování je přesné, transparentní a přizpůsobivé konkurenčním požadavkům trhu, a tvoří tak páteř zpoplatnění v mobilních sítích.

## K čemu slouží

CRGT bylo zavedeno, aby řešilo omezení dřívějších, jednodušších účtovacích mechanismů, které nedokázaly podporovat dynamické a složité tarifní struktury vyžadované moderními mobilními službami. Před jeho standardizací se účtování často spoléhalo na statické, předem nakonfigurované sazby v síťových prvcích, což ztěžovalo implementaci cenotvorby v reálném čase s ohledem na kontext. To bylo nedostatečné pro vzestup předplacených služeb, kde jsou okamžité kontroly zůstatku a flexibilní rating klíčové. Vytvoření CRGT v rámci architektury systému online účtování 3GPP (Online Charging System, [OCS](/mobilnisite/slovnik/ocs/)), počínaje Release 8, poskytlo standardizovaný, interoperabilní způsob komunikace podrobných tarifních informací napříč síťovými rozhraními, čímž vyřešilo problém rigidních, monolitních fakturačních systémů.

Historicky, jak se sítě vyvíjely od přepojování okruhů pro hlas k přepojování paketů pro data a služeb multimédií založených na IMS, rostla potřeba granulárního, relací založeného účtování. Operátoři chtěli nabízet různé plány – jako jsou časové slevy, objemové úrovně a služebně specifické sazby – bez nutnosti přestavby celé své účtovací infrastruktury pro každou novou nabídku. CRGT jako součást referenčních bodů Gy a Sy založených na Diameter (specifikovaných v 29.458 a 29.658) to umožnilo oddělením definice tarifu od toku účtovací transakce. To umožnilo, aby se OCS stal centralizovaným, inteligentním ratingovým engine, zatímco síťové prvky mohly jednoduše předávat identifikátory tarifů nebo parametry prostřednictvím CRGT, což snížilo složitost a umožnilo rychlé nasazení služeb.

Tato technologie řeší klíčové provozní výzvy: zajišťuje přesnost fakturace poskytováním explicitních tarifních detailů v reálném čase, podporuje regulatorní požadavky na transparentní účtování a usnadňuje inovace v zpoplatnění služeb. Standardizací CRGT zajistilo 3GPP, že komponenty OCS, PCRF a [AF](/mobilnisite/slovnik/af/) od různých dodavatelů mohou bezproblémově spolupracovat, čímž podpořilo konkurenční ekosystém. To bylo motivováno posunem odvětví k plně IP sítím a poptávkou po personalizovaných, flexibilních fakturačních modelech pro spotřebitele i podniky, které starší systémy nedokázaly efektivně zvládnout.

## Klíčové vlastnosti

- Standardizované AVP protokolu Diameter pro kódování tarifních parametrů
- Podpora časového přepínání tarifů (např. sazby ve špičce/mimo špičku)
- Umožnění objemových nebo vrstvených cenových modelů založených na využití
- Oddělení tarifní logiky od jádrových účtovacích protokolů pro flexibilitu
- Aplikace tarifů v reálném čase v rámci rozhodování systému online účtování (OCS)
- Interoperabilita napříč síťovými funkcemi prostřednictvím rozhraní definovaných 3GPP

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)

## Definující specifikace

- **TS 29.458** (Rel-8) — SIP Transfer of Tariff Info for Charging
- **TS 29.658** (Rel-19) — SIP Transfer of Tariff Information

---

📖 **Anglický originál a plná specifikace:** [CRGT na 3GPP Explorer](https://3gpp-explorer.com/glossary/crgt/)
