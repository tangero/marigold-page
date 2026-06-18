---
slug: "recs"
url: "/mobilnisite/slovnik/recs/"
type: "slovnik"
title: "RECS – RECording Session"
date: 2025-01-01
abbr: "RECS"
fullName: "RECording Session"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/recs/"
summary: "RECS je řídicí funkce pro záznam síťových relací, která zachycuje signalizační a uživatelskou rovinu dat pro analýzu. Používá se pro odstraňování problémů, monitorování výkonu a dodržování předpisů a"
---

RECS je řídicí funkce pro záznam síťových relací zachycující signalizační a uživatelskou rovinu dat, používaná pro odstraňování problémů, monitorování výkonu a dodržování předpisů za účelem získání přehledu o chování sítě a kvalitě služeb.

## Popis

RECording Session (RECS) je řídicí entita definovaná ve specifikacích 3GPP, která umožňuje záznam síťových relací pro účely analýzy a monitorování. Funguje v rámci architektury Management Data Analytics ([MDA](/mobilnisite/slovnik/mda/)) a zachycuje data z řídicí i uživatelské roviny během aktivních relací. Architektura zahrnuje RECS klienty, což jsou síťové funkce vyžadující záznam, a RECS servery, které zajišťují ukládání a správu zaznamenaných dat. Mezi klíčové komponenty patří správce záznamu relace, body sběru dat a systémy úložiště, které zajišťují integritu a dostupnost dat.

RECS funguje tak, že na základě spouštěčů, jako jsou specifické události, uživatelské požadavky nebo předdefinované podmínky, zahájí záznam relace. Během relace shromažďuje podrobné informace včetně signalizačních zpráv, paketů uživatelské roviny, časových značek a přidružených metadat. Data jsou typicky ukládána ve strukturovaném formátu, jako jsou soubory [PCAP](/mobilnisite/slovnik/pcap/) nebo databáze, což umožňuje následné zpracování a analýzu. RECS podporuje různé režimy záznamu, včetně úplného záznamu relace, částečného záznamu na základě filtrů a spouštěného záznamu pro konkrétní incidenty.

Úlohou RECS v síti je poskytnout standardizovaný mechanismus pro zachycení dat relace, což je zásadní pro optimalizaci sítě, diagnostiku poruch a dodržování regulatorních požadavků. Umožňuje operátorům rekonstruovat síťové události, analyzovat problémy s výkonem a ověřovat smlouvy o úrovni služeb. Díky integraci s dalšími řídicími funkcemi přispívá RECS k proaktivní údržbě sítě a zvyšuje celkovou kvalitu služeb. Je zvláště cenný ve složitých scénářích, jako jsou VoLTE hovory, IoT relace a komunikace služeb záchranného systému, kde jsou podrobné stopy relací klíčové pro analýzu hlavní příčiny.

## K čemu slouží

RECS byl vytvořen, aby řešil potřebu komplexního záznamu relací v moderních telekomunikačních sítích, kde tradiční mechanismy protokolování byly pro podrobnou analýzu nedostatečné. Rostoucí složitost síťových protokolů a služeb, jako jsou IMS a 5G, vyžadovala strukturovanější přístup k zachycení a analýze dat relací. 3GPP zavedlo RECS ke standardizaci postupů záznamu, což zajišťuje interoperabilitu a konzistenci napříč různými síťovými prvky a dodavateli.

Primární problém, který RECS řeší, je umožnění efektivního odstraňování problémů a monitorování výkonu tím, že poskytuje úplnou viditelnost síťových relací. Umožňuje operátorům diagnostikovat problémy, které je obtížné replikovat, jako jsou přerušované výpadky nebo degradace kvality. Historický kontext zahrnuje vývoj od jednoduchých souborů protokolů k sofistikovaným systémům záznamu, poháněný potřebou analýzy v reálném čase a forenzních schopností v prostředích s více dodavateli.

RECS také podporuje požadavky na dodržování předpisů, jako je zákonné odposlouchávání a auditní stopy, tím, že poskytuje ověřitelné záznamy síťových aktivit. Usnadňuje plánování kapacity a optimalizaci analýzou vzorců provozu a využití prostředků. Motivací pro RECS byl přechod k softwarově definovaným sítím a virtualizaci síťových funkcí, kde se dynamický záznam relací stává nezbytným pro správu virtualizovaných síťových funkcí a zajištění spolehlivosti služeb.

## Klíčové vlastnosti

- Standardizovaný záznam relací pro data řídicí a uživatelské roviny
- Konfigurovatelné spouštěče a filtry pro cílený záznam
- Podpora více režimů záznamu (úplný, částečný, spouštěný)
- Integrace s architekturou Management Data Analytics (MDA)
- Strukturované formáty úložiště dat pro snadnou analýzu
- Interoperabilita napříč různými síťovými funkcemi a dodavateli

## Definující specifikace

- **TS 28.307** (Rel-19) — QoE Measurement Collection IRP Requirements

---

📖 **Anglický originál a plná specifikace:** [RECS na 3GPP Explorer](https://3gpp-explorer.com/glossary/recs/)
