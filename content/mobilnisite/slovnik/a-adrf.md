---
slug: "a-adrf"
url: "/mobilnisite/slovnik/a-adrf/"
type: "slovnik"
title: "A-ADRF – Application layer - Analytical Data Repository Function"
date: 2026-01-01
abbr: "A-ADRF"
fullName: "Application layer - Analytical Data Repository Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/a-adrf/"
summary: "A-ADRF je funkce aplikační vrstvy v rámci 3GPP, která poskytuje standardizované úložiště pro ukládání a správu analytických dat. Umožňuje sdílení a spotřebu dat pro síťové analýzy, trénování AI/ML mod"
---

A-ADRF je funkce aplikační vrstvy, která poskytuje standardizované úložiště pro ukládání, správu a sdílení analytických dat za účelem podpory síťových analýz, AI/ML a optimalizace služeb v systémech 5G.

## Popis

Application layer - Analytical Data Repository Function (A-ADRF) je logická funkce definovaná v rámci architektury založené na službách (SBA) 3GPP pro analýzu síťových dat. Působí na aplikační vrstvě, odděleně od uživatelské a řídicí roviny, a je navržena jako centralizované nebo distribuované úložiště, které uchovává strukturovaná analytická data. Tato data mohou zahrnovat metriky výkonnosti sítě, vzorce chování uživatelského zařízení (UE), statistiky využití služeb a další informace generované různými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) a externími aplikačními funkcemi ([AF](/mobilnisite/slovnik/af/)). A-ADRF zpřístupňuje rozhraní [API](/mobilnisite/slovnik/api/) směrem na sever (northbound), specifikovaná primárně v 3GPP TS 29.549, což umožňuje autorizovaným konzumentům, jako je Network Data Analytics Function (NWDAF), jiným A-ADRF nebo aplikacím třetích stran pro analýzu, ukládat, načítat, dotazovat se a přihlašovat k odběru aktualizací dat standardizovaným způsobem.

Z architektonického hlediska A-ADRF komunikuje s producenty a konzumenty dat prostřednictvím rozhraní založených na službách (SBI) v rámci 5G jádra sítě. Je součástí širšího rámce pro analýzu dat, který zahrnuje funkce jako NWDAF pro generování analytiky a [ADRF](/mobilnisite/slovnik/adrf/) (funkce jádra sítě) pro ukládání nezpracovaných nebo zpracovaných dat. A-ADRF se odlišuje tím, že se zaměřuje na data aplikační vrstvy, která mohou být abstraktnější nebo více orientovaná na služby ve srovnání s daty síťové vrstvy. Mezi klíčové komponenty patří moduly pro příjem dat, které zpracovávají příchozí datové toky přes API, úložný backend, který může využívat databáze nebo datová jezera, možnosti správy dat pro řízení životního cyklu (např. politiky uchovávání, anonymizace) a stroje pro zpracování dotazů na podporu složitých analytických požadavků. Podporuje různé datové formáty a schémata definované ve specifikacích 3GPP, čímž zajišťuje interoperabilitu.

Při provozu A-ADRF funguje tak, že přijímá data od producentů – například od NWDAF, která vygenerovala analytické poznatky, nebo od AF poskytující metriky specifické pro aplikaci – prostřednictvím standardizovaných RESTful API založených na [HTTP](/mobilnisite/slovnik/http/). Tato data trvale ukládá a aplikuje případné požadované zpracování dat, jako je agregace, filtrování nebo formátování. Konzumenti pak mohou k datům přistupovat na vyžádání prostřednictvím dotazovacích rozhraní nebo si nastavit odběry pro oznámení v reálném čase, když jsou k dispozici nová data odpovídající určitým kritériím. To umožňuje případy užití, jako je trénování modelů strojového učení pro optimalizaci sítě, kdy jsou historická data z A-ADRF vkládána do [AI](/mobilnisite/slovnik/ai/) pracovních postupů. A-ADRF také podporuje federaci dat, což umožňuje více instancím A-ADRF si data vyměňovat, což je klíčové pro scénáře analýz ve velkém měřítku nebo napříč doménami. Jejím úkolem je oddělit úložiště dat od analytického zpracování, čímž podporuje opakované použití, škálovatelnost a efektivní správu dat v sítích 5G a budoucích sítích.

## K čemu slouží

A-ADRF byla vytvořena, aby řešila rostoucí složitost a náročnost na data moderních mobilních sítí, zejména s nasazením 5G a vizí pro 6G. Před jejím zavedením byla analytická data v systémech 3GPP často zpracovávána ad hoc, přičemž analytické funkce jako NWDAF data interně ukládaly nebo spoléhaly na nestandardizovaná úložiště. To vedlo k problémům se sdílením dat, interoperabilitou a škálovatelností, protože různé síťové funkce a externí aplikace nemohly snadno přistupovat k společnému datovému fondu ani do něj přispívat. Nedostatek standardizovaného úložiště bránil rozvoji pokročilých analýz, aplikací [AI/ML](/mobilnisite/slovnik/ai-ml/) a automatizované správy sítě, které vyžadují rozsáhlé a různorodé datové sady pro trénink a inferenci.

Historicky začal 3GPP vylepšovat analytické schopnosti zavedením NWDAF ve verzi 15, která se zaměřovala na generování analytiky. Jak se však sítě vyvíjely směrem k větší inteligenci a automatizaci, stala se zřejmou potřeba specializované, škálovatelné funkce pro ukládání dat. A-ADRF, zavedená ve verzi 18, to řeší poskytnutím jednotného úložiště na aplikační vrstvě, které odděluje ukládání dat od analytické logiky. To je v souladu s průmyslovými trendy směřujícími k daty řízeným operacím a podporuje případy užití, jako je optimalizace síťového řezání, prediktivní údržba a zlepšení kvality uživatelského prožitku (QoE). Standardizací rozhraní a datových modelů umožňuje inovace v ekosystému, což dodavatelům a operátorům dovoluje vytvářet kompatibilní analytická řešení bez proprietárního uzamčení.

Motivace pro A-ADRF také vychází z omezení předchozích přístupů, kdy datová úložiště (silosy) a nestandardní rozhraní ztěžovala provádění analýz napříč doménami nebo integraci nástrojů [AI](/mobilnisite/slovnik/ai/) třetích stran. Například bez A-ADRF by operátor mohl mít potíže s korelací dat aplikační vrstvy od OTT služeb s daty o výkonnosti sítě pro komplexní zajištění služeb. A-ADRF to řeší tím, že nabízí flexibilní úložiště, které dokáže uchovávat různé typy dat, podporovat federaci napříč doménami a poskytovat zabezpečený, řízený přístup. To usnadňuje naplnění vize 3GPP pro automatizovanou, inteligentní síť, která využívá data ke zlepšení efektivity, uživatelského prožitku a inovací služeb.

## Klíčové vlastnosti

- Standardizovaná RESTful API pro příjem a spotřebu dat (založená na 3GPP TS 29.549)
- Podpora trvalého ukládání strukturovaných analytických dat ze síťových a aplikačních zdrojů
- Správa životního cyklu dat včetně politik uchovávání a možností anonymizace
- Mechanismy odběru a oznamování pro aktualizace dat v reálném čase
- Dotazovací rozhraní umožňující složité získávání dat pro analytické a AI/ML pracovní postupy
- Federativní schopnosti umožňující výměnu dat mezi více instancemi A-ADRF napříč doménami

## Související pojmy

- [ADRF – Analytical Data Repository Function](/mobilnisite/slovnik/adrf/)

## Definující specifikace

- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications

---

📖 **Anglický originál a plná specifikace:** [A-ADRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-adrf/)
