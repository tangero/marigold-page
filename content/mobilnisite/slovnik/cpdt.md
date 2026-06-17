---
slug: "cpdt"
url: "/mobilnisite/slovnik/cpdt/"
type: "slovnik"
title: "CPDT – Control Plane Data Transfer"
date: 2025-01-01
abbr: "CPDT"
fullName: "Control Plane Data Transfer"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cpdt/"
summary: "CPDT je funkce správy podle 3GPP umožňující přenos objemných dat (např. výkonnostních měření, konfiguračních souborů) přes signalizační rozhraní řídicí roviny. Je klíčová pro efektivní správu sítě, ne"
---

CPDT je funkce správy podle 3GPP umožňující přenos objemných dat, jako jsou výkonnostní měření nebo konfigurační soubory, přes signalizační rozhraní řídicí roviny pro efektivní správu sítě.

## Popis

Control Plane Data Transfer (CPDT) je standardizovaný mechanismus v rámci specifikací 3GPP, specifikovaný primárně v TS 32.253, navržený pro spolehlivý a efektivní přenos objemných dat správy mezi síťovými elementy a systémy správy. Na rozdíl od přenosu dat uživatelské roviny, který zpracovává provoz účastníků, CPDT funguje přes řídicí rovinu a využívá signalizační protokoly a rozhraní, která jsou ze své podstaty spolehlivější a pro síťové operace prioritizovaná. Tato architektura je zásadní pro funkce provozu, správy a údržby (OAM), protože umožňuje přenos velkých souborů – jako jsou zprávy o výkonnostních měřeních, aktualizace software, konfigurační data nebo záznamy trasování – bez spotřeby šířky pásma uživatelské roviny a bez podléhání jejím best-effort charakteristikám doručení.

Provoz CPDT zahrnuje klíčové síťové komponenty včetně systému správy (např. Network Manager nebo Element Manager) fungujícího jako klient nebo server přenosu souborů a spravovaných síťových elementů (např. základnových stanic, uzlů jádra sítě) fungujících jako protistrana. Přenos typicky iniciuje systém správy za použití protokolů pro přenos souborů adaptovaných pro prostředí řídicí roviny. CPDT definuje procedury pro navázání relace, segmentaci dat, spolehlivý přenos s mechanismy potvrzení, řízení toku a obnovu po chybě. Zajišťuje integritu a úplnost dat, což je kritické pro data správy, kde by ztráta nebo poškození mohly ovlivnit síťové analýzy a rozhodování.

Role CPDT v síti je nedílnou součástí automatizované a daty řízené správy sítě. Poskytnutím standardizovaného robustního kanálu pro objemná data umožňuje funkce jako hromadný sběr dat výkonnostní správy (PM) pro analýzy, doručování protokolů událostí správy poruch ([FM](/mobilnisite/slovnik/fm/)), distribuci skriptů konfigurační správy ([CM](/mobilnisite/slovnik/cm/)) a podporu minimalizace jízdních testů ([MDT](/mobilnisite/slovnik/mdt/)). Protokol je navržen pro zvládání různých velikostí souborů a síťových podmínek, často zahrnuje funkce jako možnost pokračování přerušených přenosů a bezpečnostní mechanismy pro ochranu citlivých informací správy. Jeho implementace zajišťuje, že provoz správy nezasahuje do uživatelského zážitku, a zároveň garantuje, že nezbytná OAM data dorazí ke svému cíli spolehlivě pro síťovou optimalizaci a zajištění služeb.

## K čemu slouží

CPDT byl vytvořen pro řešení rostoucí potřeby efektivního a spolehlivého přenosu velkých objemů dat správy v mobilních sítích. Před jeho standardizací operátoři často spoléhali na ad-hoc metody nebo kanály uživatelské roviny pro přenos souborů, jako jsou výkonnostní reporty nebo softwarové image. Tyto přístupy měly významná omezení: použití uživatelské roviny mohlo zahltit účastnický provoz, trpět nepředvídatelnou latencí a ztrátou paketů a postrádat mechanismy zaručeného doručení nezbytné pro kritická data správy. Dále nestandardizované metody vedly k problémům s interoperabilitou mezi zařízeními od různých dodavatelů, což zvyšovalo provozní složitost a náklady.

Zavedení CPDT ve 3GPP Release 13 bylo motivováno vývojem směrem k automatizovanější, datově intenzivnější správě sítě a nástupem konceptů jako Self-Organizing Networks (SON) a big data analýzy pro síťovou optimalizaci. Tyto pokročilé OAM funkce vyžadují častý a spolehlivý sběr obrovského množství dat ze síťových elementů. CPDT poskytuje standardizované řešení založené na řídicí rovině, které zajišťuje, že data správy jsou přenášena s vysokou spolehlivostí, prioritním doručením a bez dopadu na uživatelský zážitek. Řeší problém škálovatelného sběru dat pro analýzy, což operátorům umožňuje monitorovat výkon sítě, detekovat anomálie a zavádět optimalizace včas.

Historicky, jak se sítě s příchodem LTE-Advanced a později 5G stávaly komplexnějšími, objem dat správy explodoval kvůli zvýšené hustotě sítě, novým funkcím a podrobnějším měřením. CPDT nabídl budoucím výzvám odolný mechanismus pro zvládnutí tohoto růstu. Využitím inherentní spolehlivosti a bezpečnosti signalizačních protokolů řídicí roviny poskytuje vyhrazený kanál pro OAM data, který je oddělený od best-effort uživatelského provozu. Toto oddělení je klíčové pro udržení stability sítě a zajištění, že provozní operace správy – jako jsou aktualizace software nebo kritické konfigurační změny – mohou být provedeny spolehlivě, dokonce i během období vysokého uživatelského zatížení, čímž podporují kontinuální zlepšování sítě a kvalitu služeb.

## Klíčové vlastnosti

- Využívá signalizaci řídicí roviny pro spolehlivý, prioritizovaný přenos dat
- Podporuje přenos objemných souborů pro výkonnostní měření, konfigurace a aktualizace software
- Implementuje správu relací, segmentaci a mechanismy potvrzení pro integritu dat
- Zahrnuje procedury řízení toku a obnovy po chybě pro zvládání síťových variací
- Navrženo tak, aby se zabránilo zahlcení a rušení provozu uživatelské roviny
- Standardizováno v 3GPP TS 32.253 pro zajištění interoperability mezi více dodavateli

## Definující specifikace

- **TS 32.253** (Rel-19) — Charging for Control Plane Data Transfer

---

📖 **Anglický originál a plná specifikace:** [CPDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpdt/)
