---
slug: "as-ilcm"
url: "/mobilnisite/slovnik/as-ilcm/"
type: "slovnik"
title: "AS-ILCM – Application Server Incoming Leg Control Model"
date: 2025-01-01
abbr: "AS-ILCM"
fullName: "Application Server Incoming Leg Control Model"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/as-ilcm/"
summary: "AS-ILCM je řídicí model v architektuře CAMEL, ve kterém Application Server (AS) řídí příchozí větev hovoru. Umožňuje servisní logice řídit zpracování příchozích hovorů, což umožňuje inteligentní směro"
---

AS-ILCM je řídicí model architektury CAMEL, ve kterém Application Server spravuje příchozí větev hovoru, aby umožnil inteligentní směrování, kontrolu a spouštění služeb.

## Popis

Application Server Incoming Leg Control Model (AS-ILCM) je základní architektonická komponenta v rámci 3GPP frameworku [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile networks Enhanced Logic), konkrétně definovaná pro řízení služeb v přepojovaných okruzích a v sítích IP Multimedia Subsystem (IMS). Definuje přesné mechanismy a signalizační interakce, pomocí kterých externí Application Server ([AS](/mobilnisite/slovnik/as/)) přebírá kontrolu nad zpracováním příchozí větve hovorové relace. Tento model je vyvolán, když je hovor určen účastníkovi, který má předplacené služby hostované na tomto AS, jako je např. přesměrování hovoru, překlad čísel nebo služby předplaceného účtování, které vyžadují zásah před tím, než je hovor prezentován volanému uživateli.

Architektonicky AS-ILCM funguje v širším kontextu rozhraní CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)) nebo IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)). Když požadavek na sestavení hovoru (např. Initial Address Message v [SS7](/mobilnisite/slovnik/ss7/) nebo [SIP](/mobilnisite/slovnik/sip/) INVITE v IMS) dorazí do přepojovacího uzlu sítě (jako je [MSC](/mobilnisite/slovnik/msc/) nebo [S-CSCF](/mobilnisite/slovnik/s-cscf/)), profil účastníka indikuje vyvolání služeb CAMEL. Přepojovací uzel, který funguje jako gsmSSF nebo IM-SSF, poté zahájí dialog s určeným AS. V AS-ILCM AS přijme informace o příchozí větvi hovoru a provede svou servisní logiku. Tato logika může analyzovat parametry, jako je číslo volajícího, denní doba nebo stav účastníka, a poté dát síti pokyn, jak postupovat – například spojit hovor, přesměrovat jej na jiné číslo, přehrát oznámení nebo aplikovat specifické účtování.

Klíčové komponenty zapojené do AS-ILCM zahrnují Service Switching Function (SSF) v uzlu základní sítě, která detekuje spouštěč služby a spravuje větev, a samotný Application Server, který hostuje servisní logiku. Komunikace mezi nimi využívá standardizované protokoly: CAP přes SS7 pro domény s přepojováním okruhů nebo SIP přes rozhraní ISC pro IMS. Model definuje specifické operace jako Connect, Continue, ReleaseCall a RequestReportBCSMEvent, které AS používá k řízení větve hovoru. Tato přesná kontrola umožňuje komplexní služby v reálném čase, které jsou transparentní pro koncové uživatelské zařízení.

Jeho role v síti je klíčová pro umožnění přidaných služeb hostovaných operátorem bez nutnosti úprav účastnického terminálu. Oddělením servisní logiky od základních funkcí přepojování hovorů AS-ILCM podporuje flexibilitu sítě a rychlé nasazování služeb. Tvoří základ pro služby inteligentní sítě (IN) v mobilních sítích a zajišťuje, že provádění služeb je konzistentní, spolehlivé a integrované s funkcemi základní sítě, jako je správa mobility a účtování.

## K čemu slouží

AS-ILCM byl vytvořen k řešení potřeby standardizovaného, síťového řízení zpracování příchozích hovorů v mobilních sítích. Před zavedením CAMEL a modelů jako je AS-ILCM byly pokročilé hovorové služby často implementovány pomocí proprietárních, na dodavatelích závislých řešení inteligentní sítě (IN), což vedlo k problémům s interoperabilitou a pomalému nasazování služeb napříč vícevýrobkovými sítěmi a různými operátory. Nedostatek jednotného řídicího modelu ztěžoval vytváření přenositelných služeb nebo zajištění konzistentního chování pro roamující účastníky.

Primární problém, který AS-ILCM řeší, je poskytnutí jasného, standardizovaného mechanismu pro externí aplikační server, aby zachytil a řídil, jak je příchozí větev hovoru zpracována, než dorazí k volané straně. To umožňuje širokou škálu účastnických služeb, které závisí na analýze pokusu o hovor v reálném čase. Například umožňuje inteligentní přesměrování hovoru (např. přesměrovat na hlasovou schránku při obsazení nebo na jiné číslo v závislosti na čase), kontrolu příchozích hovorů (přijetí nebo odmítnutí hovorů na základě černých/bílých listin) a služby překladu čísel (jako jsou čísla virtuální privátní sítě).

Historicky bylo jeho zavedení v 3GPP R99 jako součásti CAMEL fáze 3 motivováno rostoucí poptávkou po přizpůsobitelných službách řízených operátorem nad rámec základních hlasových hovorů. Poskytlo architektonický základ pro oddělení servisní logiky od přepojovací infrastruktury, což je klíčový princip inteligentních sítí. Toto oddělení umožnilo operátorům rychle vyvíjet a nasazovat služby na vyhrazených aplikačních serverech bez nutnosti upgradovat každý přepojovací uzel základní sítě, čímž se snížily náklady a zvýšila inovace služeb. AS-ILCM konkrétně řešil scénář příchozího hovoru a doplnil další modely, jako je AS-OLCM (Outgoing Leg Control), aby poskytl komplexní řízení hovoru.

## Klíčové vlastnosti

- Standardizované řízení příchozí větve hovoru externím Application Serverem
- Pro komunikaci mezi síťovým přepojovačem a AS využívá signalizaci CAMEL Application Part (CAP) nebo SIP
- Umožňuje provádění servisní logiky v reálném čase na základě parametrů hovoru a dat účastníka
- Podporuje operace jako Connect, Redirect, Release a Event Reporting pro přesné řízení hovoru
- Umožňuje integraci s profily účastníků a HLR pro spouštění služeb
- Umožňuje služby jako přesměrování hovoru, jeho kontrola, překlad čísel a předplacené účtování

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [CAP – CAMEL Application Part](/mobilnisite/slovnik/cap/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification

---

📖 **Anglický originál a plná specifikace:** [AS-ILCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/as-ilcm/)
