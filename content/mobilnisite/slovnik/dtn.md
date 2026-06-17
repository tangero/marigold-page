---
slug: "dtn"
url: "/mobilnisite/slovnik/dtn/"
type: "slovnik"
title: "DTN – Deflected To Number"
date: 2025-01-01
abbr: "DTN"
fullName: "Deflected To Number"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dtn/"
summary: "Služba přesměrování hovoru, která příchozí hovor přesměruje na jiné číslo určené volaným účastníkem. Umožňuje uživatelům dynamicky spravovat směrování hovorů, což zvyšuje flexibilitu a zajišťuje, že s"
---

DTN je služba přesměrování hovoru, která příchozí hovor přesměruje na jiné telefonní číslo určené volaným účastníkem.

## Popis

Deflected To Number (DTN, Přesměrování na číslo) je doplňková služba v telekomunikačních sítích, která umožňuje volanému účastníkovi přesměrovat příchozí hovor na jiné telefonní číslo před tím, než je hovor přijat. K tomuto přesměrování dochází během fáze navazování hovoru, typicky poté, co je hovor doručen volanému účastníkovi, ale ještě před jeho přijetím, což uživateli umožňuje hovor ručně nebo automaticky přesměrovat na jiný cíl. Služba je součástí sady funkcí Call Deflection ([CD](/mobilnisite/slovnik/cd/)), která poskytuje dynamickou kontrolu směrování hovorů pro zvýšení uživatelského komfortu a zlepšení správy hovorů.

Z architektonického hlediska DTN funguje uvnitř jádra sítě systémů 3GPP a zahrnuje síťové entity jako Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro sítě s přepojováním okruhů nebo Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v sítích založených na IMS. Když dorazí hovor, obslužný uzel zkontroluje, zda je DTN pro volaného účastníka aktivní. Pokud je služba povolena, síť hovor zachytí a přesměruje jej na předem definované nebo dynamicky zadané číslo. Mezi klíčové komponenty patří Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), které ukládají nastavení přesměrování, a servisní logika, která přesměrování provádí. Přesměrování může být spuštěno vstupem od uživatele (např. stisknutím klávesy) nebo na základě podmínek, jako je stav obsazeno nebo neodpověď.

Technický proces začíná, když je příchozí hovor směrován na zařízení volaného účastníka. Síť signalizuje navázání hovoru a pokud je vyvolána DTN, UE volaného účastníka nebo síťový uzel odešle žádost o přesměrování obsahující cílové číslo. Tuto žádost zpracuje jádro sítě, které poté hovor přesměruje na nové číslo pomocí standardních procedur navazování hovoru. V doménách s přepojováním paketů může být DTN implementováno pomocí SIP přesměrovacích zpráv v rámci architektury IMS. Služba zajišťuje, že původní volající zůstává v nevědomosti o přesměrování, což zachovává plynulý zážitek.

Úloha DTN v síti spočívá v poskytování flexibilního zpracování hovorů, což snižuje počet zmeškaných hovorů a zlepšuje dostupnost. Běžně se používá ve scénářích, kdy jsou uživatelé dočasně nedostupní na svém primárním čísle, například v kancelářském prostředí nebo při cestování. Služba se integruje s dalšími doplňkovými službami, jako je Přesměrování hovoru (Call Forwarding), ale liší se tím, že přesměrování je typicky iniciováno volaným účastníkem v reálném čase, místo aby bylo předem nakonfigurováno. Specifikace jako TS 23.078 podrobně popisují protokoly a procedury pro DTN, což zajišťuje interoperabilitu napříč různými generacemi sítí a zařízeními různých výrobců.

## K čemu slouží

DTN bylo vytvořeno, aby dalo volaným účastníkům okamžitou kontrolu nad směrováním hovorů a řešilo potřebu dynamické správy hovorů bez předchozího nastavení pravidel přesměrování. Před DTN služby přesměrování hovorů vyžadovaly předkonfiguraci (např. přesměrovat při stavu obsazeno nebo neodpověď), což postrádalo flexibilitu pro ad-hoc situace. DTN tento problém řeší tím, že umožňuje uživatelům přesměrovávat hovory pro každý hovor zvlášť, což jim umožňuje přesměrovat konkrétní hovory na kolegy, do hlasové schránky nebo na jiná čísla podle potřeby, čímž se zvyšuje reaktivita a personalizace.

Historicky se přesměrování hovoru objevilo jako součást doplňkových služeb v GSM a bylo standardizováno v 3GPP Release 4 pro podporu vyvíjejících se telefonních funkcí. Řešilo omezení statického přesměrování tím, že poskytovalo alternativu v reálném čase, zvláště užitečnou v obchodním prostředí, kde zpracování hovorů vyžaduje agilitu. Motivací služby je zlepšení uživatelského zážitku snížením počtu opuštěných hovorů a zajištění, že důležité hovory nejsou zmeškány, zejména když volaný účastník ví, že nemůže odpovědět, ale chce, aby byl hovor zpracován jinde.

V sítích 3GPP začlenění DTN podporuje přechod na IP-based multimedia subsystems, zachovávajíc funkční paritu s legacy službami s přepojováním okruhů. Řeší problémy související s přetížením hovorů a mobilitou uživatelů, což umožňuje plynulé přesměrování přes hranice sítí. Tím, že umožňuje přesměrování na jakékoliv platné číslo, DTN usnadňuje efektivní distribuci hovorů v kontaktních centrech i v osobních případech použití, což přispívá k celkové efektivitě sítě a spokojenosti účastníků v moderních telekomunikacích.

## Klíčové vlastnosti

- Přesměrování hovoru v reálném čase iniciované volaným účastníkem
- Podpora přesměrování na jakékoliv platné telefonní číslo
- Integrace se sítěmi s přepojováním okruhů i sítěmi založenými na IMS
- Dynamické vyvolání bez předchozí konfigurace
- Plynulý zážitek pro volajícího účastníka
- Interoperabilita s dalšími doplňkovými službami, jako je přesměrování hovoru (call forwarding)

## Definující specifikace

- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [DTN na 3GPP Explorer](https://3gpp-explorer.com/glossary/dtn/)
