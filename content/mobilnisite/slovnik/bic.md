---
slug: "bic"
url: "/mobilnisite/slovnik/bic/"
type: "slovnik"
title: "BIC – Baseline Implementation Capabilities"
date: 2025-01-01
abbr: "BIC"
fullName: "Baseline Implementation Capabilities"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bic/"
summary: "Standardizovaný rámec definující minimální povinné a volitelné soubory funkcí, které musí síťové vybavení a uživatelské terminály implementovat pro danou verzi 3GPP. Zajišťuje základní interoperabilit"
---

BIC je standardizovaný rámec definující minimální povinné a volitelné soubory funkcí, které musí síťové vybavení a uživatelské terminály implementovat pro danou verzi 3GPP, aby byla zajištěna základní interoperabilita.

## Popis

Baseline Implementation Capabilities (BIC) je formalizovaný koncept v rámci specifikací 3GPP, který stanovuje společnou, dohodnutou sadu funkcí pro konkrétní verzi. Funguje jako nástroj pro řízení a plánování, nikoli jako běhový protokol. Rámec je architektonicky založen na kategorizaci funkcí z rozsáhlých technických specifikací (TS) a technických zpráv (TR) 3GPP do odlišných tříd. Primární klasifikace rozlišuje mezi povinnými („Mandatory“) a volitelnými („Optional“) schopnostmi. Povinné BIC jsou funkce, které musí podporovat všechny kompatibilní implementace, aby byla zaručena základní úroveň interoperability a služeb v celé síti. Volitelné BIC jsou funkce, které mohou výrobci zvolit k implementaci, což umožňuje diferenciaci produktů a postupný zavádění pokročilých služeb.

Proces definování BIC zahrnuje podrobnou technickou analýzu a vytváření konsenzu v pracovních skupinách 3GPP. Specifikace jako 21.904 a 21.905 slouží jako hlavní katalogy, které pro každou verzi uvádějí a popisují schopnosti. Tyto dokumenty odkazují na podkladové technické specifikace (např. pro rozhraní rádiového přístupu, protokoly jádra sítě nebo služební prostředky), kde jsou definovány podrobné požadavky na implementaci. Rámec BIC tak vytváří abstraktní vrstvu, která mapuje obchodní a služební požadavky na konkrétní technické stavební bloky rozptýlené ve stovkách jednotlivých specifikačních dokumentů.

V praxi seznam BIC funguje jako vzor pro shodu (conformance blueprint). Aby uživatelské zařízení (UE) nebo síťový uzel (jako eNodeB nebo [AMF](/mobilnisite/slovnik/amf/)) mohlo deklarovat shodu s konkrétní verzí 3GPP (např. Release 15 pro 5G), musí prokazatelně implementovat všechny schopnosti označené jako povinné BIC pro danou verzi a kategorii zařízení. Toto ověření je typicky součástí certifikačních procesů prováděných orgány jako Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)). Role BIC v síťovém ekosystému je zásadní: zabraňuje scénáři, kdy by se zařízení od různých výrobců, přestože jsou nominálně kompatibilní se stejnou verzí, nemohla kvůli nekonzistentní podpoře funkcí dorozumět nebo poskytovat základní služby, čímž zajišťuje předvídatelný a spolehlivý uživatelský zážitek.

## K čemu slouží

Rámec BIC byl zaveden, aby vyřešil kritické problémy interoperability a fragmentace trhu, které sužovaly ranou mobilní telekomunikaci. Před jeho formalizací ve verzi Release 99 bylo provádění standardů z velké části ponecháno na interpretaci výrobců, což vedlo k situacím, kdy síťové vybavení a mobilní telefony podporující stejnou generaci (např. GSM) mohly mít stále nekompatibilní soubory funkcí. To bránilo roamingu, zvyšovalo složitost testování a zpomalovalo zavádění nových služeb, protože operátoři si nemohli být jisti jejich všudypřítomnou podporou.

Vytvoření BIC bylo motivováno potřebou poskytnout jasný, standardizovaný plán implementace. Řeší omezení plynoucí z existence tisíců jednotlivých technických specifikací tím, že je destiluje do zvládnutelné sady základních schopností. Pro síťové operátory představují BIC spolehlivý kontrolní seznam pro zadávání zakázek, který zajišťuje, že pořízené vybavení bude spolupracovat a poskytne definovanou sadu služeb. Pro výrobce zařízení a infrastruktury toto objasňuje priority vývoje, snižuje nejistotu ohledně toho, co musí být vybudováno, a zaměřuje výzkumné a vývojové zdroje na standardizované funkce, které mají zaručenou relevanci na trhu.

Historicky byl BIC základním kamenem úspěšného globálního zavedení systémů 3G (UMTS), 4G (LTE) a 5G. Podporuje princip „postavit jednou, nasadit všude“ pro funkce jádra sítě a základní rádiové schopnosti. Definováním stabilního základu umožňuje postupnou inovaci prostřednictvím volitelných funkcí při zachování pevného základu zpětné a dopředné kompatibility, což je nezbytné pro dlouhý životní cyklus telekomunikačních sítí.

## Klíčové vlastnosti

- Definuje povinné soubory funkcí pro zaručenou interoperabilitu
- Katalogizuje volitelné funkce pro diferenciaci výrobců a postupnou implementaci
- Poskytuje výrobcům plán implementace specifický pro danou verzi
- Slouží jako základní referenční dokument pro certifikaci a typové schvalování
- Mapuje vysoké služební požadavky na podrobné technické specifikace
- Snižuje složitost testování stanovením jasných cílů pro shodu (conformance)

## Definující specifikace

- **TR 21.904** (Rel-4) — 3GPP UE Baseline Capability Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.949** (Rel-19) — Privacy Requirements Study for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [BIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bic/)
