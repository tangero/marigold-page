---
slug: "nse"
url: "/mobilnisite/slovnik/nse/"
type: "slovnik"
title: "NSE – Network Service Entity"
date: 2025-01-01
abbr: "NSE"
fullName: "Network Service Entity"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nse/"
summary: "Funkční entita v systému základnových stanic (BSS), která poskytuje síťové služby, zejména pro přenos signalizace. Funguje jako koncový bod signalizačních spojení, například těch používaných aplikační"
---

NSE je funkční entita v systému základnových stanic (Base Station System), která poskytuje síťové služby a funguje jako koncový bod signalizačních spojení pro komunikaci s jádrem sítě.

## Popis

Network Service Entity (NSE) je logická funkční komponenta definovaná v architektuře systému základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) v GSM a příbuzných systémech 3GPP. Jejím hlavním úkolem je poskytovat služby síťové vrstvy pro spolehlivý přenos signalizačních zpráv. NSE funguje na vrstvě 3 (Layer 3) protokolového zásobníku a slouží jako ukončovací bod signalizačních spojení, která propojují BSS s prvky jádra sítě, především s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)). Je specifikována v dokumentech jako je TS 48.018, který podrobně popisuje protokol [BSSAP](/mobilnisite/slovnik/bssap/) na rozhraní A.

NSE funguje tak, že spravuje jedno nebo více signalizačních spojení. Využívá služeb podkladové spojové vrstvy (např. z protokolu [LAPD](/mobilnisite/slovnik/lapd/)) k navázání, udržování a uvolnění spolehlivých datových spojení. Pro každé signalizační spojení poskytuje NSE služby nadřazené aplikační části, zejména Base Station System Application Part (BSSAP). Když má BSSAP zprávu k odeslání do MSC, předá ji NSE jako Network Service Data Unit ([NSDU](/mobilnisite/slovnik/nsdu/)). NSE je pak zodpovědná za správné doručení této NSDU přes přiřazené signalizační spojení, řeší funkce jako segmentaci a zpětné sestavení, pokud je to nutné, a informuje vyšší vrstvu o úspěchu či neúspěchu přenosu.

Z architektonického hlediska je NSE identifikována identifikátorem Network Service Entity Identifier ([NSEI](/mobilnisite/slovnik/nsei/)). Jeden BSS může obsahovat více NSE, z nichž každá může být asociována s různými MSC nebo různými signalizačními cestami pro redundanci a rozdělení zátěže. NSE abstrahuje složitost fyzického signalizačního přenosu od aplikačních protokolů vyšších vrstev. Tato abstrakce umožňuje BSSAP soustředit se na aplikačně specifické zprávy (jako jsou žádosti o předání hovoru nebo aktualizace polohy) bez nutnosti spravovat složitosti navazování spojení, opravy chyb nebo řízení toku, které řeší NSE a vrstvy pod ní.

## K čemu slouží

NSE byla zavedena za účelem strukturování a standardizace funkce přenosu signalizace v rámci [BSS](/mobilnisite/slovnik/bss/). Před jejím formálním definováním mohlo být rozdělení odpovědností mezi aplikační signalizaci ([BSSAP](/mobilnisite/slovnik/bssap/)) a podkladovou službu přenosu zpráv nejednoznačné nebo závislé na konkrétní implementaci. NSE vytváří jasné funkční oddělení a definuje vyhrazenou entitu, jejímž jediným účelem je poskytovat spolehlivou, spojově orientovanou síťovou službu pro signalizační zprávy.

Řeší to několik klíčových problémů. Za prvé zvyšuje spolehlivost tím, že zajišťuje pro signalizační zprávy vyhrazenou a řízenou cestu do jádra sítě. Za druhé zlepšuje škálovatelnost a spravovatelnost; lze nakonfigurovat více NSE pro zpracování signalizačního provozu do různých MSC, což podporuje rozšiřování sítě a redundantní schémata jako je MSC pooling. Za třetí standardizuje servisní rozhraní (bod, kde BSSAP předává NSDU NSE), což je klíčové pro interoperabilitu mezi zařízeními BSS od různých výrobců a jádrem sítě.

Vytvoření NSE, zejména jak je podrobně popsáno ve specifikacích rozhraní A od verze Rel-8 dále, bylo motivováno potřebou robustní, flexibilní a standardizované signalizační páteře pro podporu základních mobilních služeb, jako je zpracování hovorů, správa mobility a SMS. Tvoří základní transportní vrstvu, na které je vybudován veškerý dialog mezi BSS a jádrem sítě, a zajišťuje, že kritická komunikace řídicí roviny je doručována přesně a efektivně, což je zásadní pro stabilitu sítě a kvalitu služeb.

## Klíčové vlastnosti

- Poskytuje síťové služby vrstvy 3 (Layer 3) pro přenos signalizačních zpráv
- Ukončuje signalizační spoje na rozhraní A směrem k MSC
- Identifikována jedinečným identifikátorem Network Service Entity Identifier (NSEI)
- Podporuje služby pro aplikační část systému základnových stanic (BSSAP)
- Spravuje spolehlivé doručování jednotek síťových služeb (NSDU)
- Umožňuje více signalizačních spojení pro redundanci a sdílení zátěže

## Související pojmy

- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)
- [BSSAP – Base Station Subsystem Application Part](/mobilnisite/slovnik/bssap/)
- [NSDU – Network Service Data Unit](/mobilnisite/slovnik/nsdu/)
- [NSAPI – Network layer Service Access Point Identifier](/mobilnisite/slovnik/nsapi/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [NSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/nse/)
