---
slug: "acid"
url: "/mobilnisite/slovnik/acid/"
type: "slovnik"
title: "ACID – Atomicity - Consistency - Isolation - Durability"
date: 2026-01-01
abbr: "ACID"
fullName: "Atomicity - Consistency - Isolation - Durability"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/acid/"
summary: "ACID je soubor vlastností zajišťujících spolehlivé zpracování transakcí v databázových systémech. V kontextu 3GPP garantuje integritu dat síťových funkcí, zejména v servisně orientovaných architekturá"
---

ACID je soubor vlastností zajišťujících spolehlivé zpracování transakcí pro garanci integrity dat síťových funkcí v servisně orientovaných architekturách 3GPP.

## Popis

ACID je základní koncept v řízení databázových transakcí, který byl přijat v rámci specifikací 3GPP pro zajištění integrity a spolehlivosti dat síťových funkcí, obzvláště v servisně orientovaných architekturách ([SBA](/mobilnisite/slovnik/sba/)), jako je 5G Core (5GC). Definuje čtyři klíčové vlastnosti, které transakce – logická jednotka práce – musí splňovat, aby byla považována za spolehlivou, zejména v distribuovaných systémech, kde mohou být data replikována nebo přistupována souběžně.

Atomicita (Atomicity) zajišťuje, že transakce je považována za jedinou nedělitelnou jednotku práce. Řídí se principem 'vše nebo nic': buď jsou všechny operace v rámci transakce úspěšně dokončeny a zapsány do databáze, nebo pokud jakákoli část selže, je celá transakce vrácena zpět a stav systému zůstane nezměněn. Tím se zabrání částečným aktualizacím, které by mohly vést k poškození dat. V síti 3GPP je toto klíčové během procedur, jako je registrace nebo zřizování relace, kdy musí více síťových funkcí ([NF](/mobilnisite/slovnik/nf/)) koherentně aktualizovat své stavy.

Konzistence (Consistency) zaručuje, že transakce převádí databázi z jednoho platného stavu do druhého při zachování všech definovaných pravidel, omezení a vztahů. Zajišťuje, že jsou zapsána pouze data, která dodržují předdefinovaná omezení integrity (např. cizí klíče, jedinečnost). Například v jednotném datovém úložišti ([UDR](/mobilnisite/slovnik/udr/)) 3GPP konzistence zajišťuje, že aktualizace profilů účastníků jsou v souladu s pravidly schématu, čímž zabraňuje uložení neplatných konfigurací.

Izolace (Isolation) zajišťuje, že souběžné provádění transakcí ponechá databázi ve stejném stavu, jako kdyby byly prováděny sekvenčně. Řídí, jak a kdy se změny provedené jednou transakcí stanou viditelné pro ostatní, a zabraňuje jevům, jako jsou nepotvrzené čtení (dirty reads), nenavazující se čtení (non-repeatable reads) a fantomové čtení (phantom reads). V síti 3GPP je izolace zásadní, když více funkcí pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) nebo aplikací souběžně přistupuje nebo mění sdílená data, jako jsou pravidla politiky nebo záznamy o účtování.

Trvanlivost (Durability) zaručuje, že jakmile je transakce potvrzena, její změny trvale přetrvají v databázi, a to i v případě selhání systému, výpadku napájení nebo pádu. Toho je typicky dosaženo pomocí protokolování před zápisem (WAL) a replikace dat na nestálé úložiště. Pro systémy 3GPP trvanlivost zajišťuje, že kritická data – jako jsou autentizační vektory účastníka, kontexty relací nebo záznamy o účtovacích údajích ([CDR](/mobilnisite/slovnik/cdr/)) – nebudou ztracena, což podporuje přesnost účtování a kontinuitu služeb.

V servisně orientované architektuře 3GPP jsou principy ACID implicitně nebo explicitně aplikovány v návrhu řešení pro ukládání dat, jako jsou UDR, jednotná správa dat ([UDM](/mobilnisite/slovnik/udm/)) a funkce síťového repozitáře ([NRF](/mobilnisite/slovnik/nrf/)). Tvoří základ spolehlivosti interakcí mezi síťovými funkcemi prostřednictvím služeb založených na [HTTP](/mobilnisite/slovnik/http/) a zajišťují, že složité vícekrokové procedury napříč distribuovanými síťovými funkcemi zachovávají integritu dat a stabilitu systému.

## K čemu slouží

Vlastnosti ACID existují pro řešení základních problémů spolehlivosti a integrity dat v databázových systémech, které jsou klíčové pro jakoukoli složitou softwarovou infrastrukturu, včetně telekomunikačních sítí. Před formalizací ACID byly rané databázové systémy náchylné k poškození dat, nekonzistentnosti a ztrátám při selhání systému nebo souběžném přístupu, což vedlo k nesprávným stavům systému, finančním nesrovnalostem (např. v účtování) a výpadkům služeb. Tento koncept poskytuje rigorózní model pro zajištění, že transakce – operace obchodní logiky, jako je odepsání z účtu nebo aktualizace profilu účastníka – jsou zpracovávány spolehlivě.

V kontextu standardů 3GPP se přijetí principů ACID stalo stále důležitější s vývojem směrem k cloud-nativním, servisně orientovaným architekturám v 4G EPC a zejména v 5G Core. Tyto architektury rozkládají monolitické síťové prvky na distribuované síťové funkce založené na mikroslužbách, které interagují asynchronně a spravují vlastní nebo sdílená datová úložiště. Tato distribuce přináší výzvy v podobě konzistence dat napříč funkcemi během procedur, jako jsou předávání hovoru (handover) nebo aktualizace politik. ACID poskytuje teoretický základ pro návrh datových vrstev (např. v UDM/UDR), které zvládnou tyto složité stavové interakce bez poškození.

Konkrétně specifikace 3GPP odkazují na ACID v kontextu vystavování služeb, správy dat a účtování (jak je vidět ve specifikacích jako 23.558, 29.558). Řeší potřebu, aby síťová API vystavená aplikacím třetích stran (prostřednictvím NEF) garantovala, že úpravy dat jsou atomické a trvalé, a zabránila tak scénářům, kdy požadavek aplikace částečně aktualizuje síťová data, což vede k chybám služby. Principy ACID zajišťují, že síť může poskytovat předvídatelné a důvěryhodné datové služby jak interním síťovým funkcím, tak externím spotřebitelům.

## Klíčové vlastnosti

- Zaručuje, že všechny operace v transakci uspějí, nebo selžou jako celek (Atomicita)
- Zajišťuje, že přechody databáze dodržují všechna definovaná omezení integrity (Konzistence)
- Řídí viditelnost souběžných transakcí, aby se předešlo anomáliím dat (Izolace)
- Trvale uchovává změny potvrzených transakcí navzdory selhání systému (Trvanlivost)
- Poskytuje model pro spolehlivou správu stavu v distribuovaných síťových funkcích
- Tvoří základ integrity dat v servisně orientované architektuře 3GPP a rámcích pro vystavení sítě

## Definující specifikace

- **TS 23.558** (Rel-20) — Architecture for Edge Applications
- **TS 29.558** (Rel-19) — Enabling Edge Applications
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TR 33.739** (Rel-18) — Study on security enhancement of support for

---

📖 **Anglický originál a plná specifikace:** [ACID na 3GPP Explorer](https://3gpp-explorer.com/glossary/acid/)
