---
slug: "ngcor"
url: "/mobilnisite/slovnik/ngcor/"
type: "slovnik"
title: "NGCOR – Next Generation Converged Operations Requirements"
date: 2025-01-01
abbr: "NGCOR"
fullName: "Next Generation Converged Operations Requirements"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ngcor/"
summary: "Rámec 3GPP definující provozní požadavky pro konvergované řízení sítí. Jeho cílem je standardizovat a automatizovat provoz napříč více-dodavatelskými a více-technologickými sítěmi včetně 5G, aby se sn"
---

NGCOR je rámec 3GPP definující provozní požadavky pro konvergované, automatizované řízení sítí napříč více-dodavatelskými a více-technologickými systémy, jako je 5G, za účelem snížení nákladů a složitosti.

## Popis

NGCOR (Next Generation Converged Operations Requirements) je komplexní rámec vyvinutý v rámci 3GPP, který definuje provozní požadavky pro řízení moderních, konvergovaných telekomunikačních sítí. Konkrétně řeší výzvy spojené s provozem sítí, které integrují více technologií rádiového přístupu (RAT), jako jsou 4G LTE a 5G NR, a potenciálně i nepřístup 3GPP, pod jednotným systémem řízení. Rámec je podrobně popsán v několika technických specifikacích (TS), včetně TS 28.390 (požadavky), TS 32.130 (principy telekomunikačního managementu) a TS 32.851 (služby managementu). Jeho hlavním cílem je umožnit bezproblémový, automatizovaný a efektivní provoz a údržbu (O&M) sítě v heterogenním prostředí.

Architektura NGCOR je založena na principech konvergence, automatizace a abstrakce. Definuje sadu služeb managementu a rozhraní směrem k vyšším systémům (northbound interfaces), které umožňují jednotný pohled a řízení síťových zdrojů bez ohledu na podkladovou technologii. To zahrnuje standardizaci datových modelů, správu poruch, správu výkonnosti, správu konfigurace a procedury správy životního cyklu. Mezi klíčové komponenty patří Management Function ([MF](/mobilnisite/slovnik/mf/)) a Network Resource Model (NRM), které poskytují abstraktní reprezentaci fyzických a virtualizovaných síťových funkcí. NGCOR zajišťuje, že operační podpůrné systémy ([OSS](/mobilnisite/slovnik/oss/)) mohou spravovat síťové řezy, virtualizované síťové funkce (VNF) a fyzické síťové funkce (PNF) prostřednictvím společných rozhraní a formátů pro výměnu dat.

V praxi NGCOR funguje tak, že stanovuje společnou sadu požadavků, kterých se musí dodavatelé a operátoři držet pro rozhraní a schopnosti řízení sítě. Umožňuje správu více domén, což operátorovi dovoluje spravovat jak Evolved Packet Core (EPC), tak 5G Core (5GC) z jedné platformy OSS. Rámec podporuje automatizaci s uzavřenou smyčkou, kdy může systém řízení automaticky detekovat anomálie, analyzovat data o výkonnosti a provádět nápravné akce (např. škálování zdrojů, rekonfigurace parametrů) bez lidského zásahu. To je klíčové pro podporu dynamického síťového řezání, kde každý řez může mít jedinečné požadavky na výkon a smlouvu o úrovni služeb (SLA), které musí být průběžně monitorovány a zaručovány.

Role NGCOR v síti je zásadní pro dosažení provozní efektivity a agility v éře 5G. Tím, že poskytuje standardizované požadavky, snižuje integrační náklady a složitost při nasazování zařízení od různých dodavatelů. Usnadňuje přechod na cloud-nativní síťové architektury definováním způsobu správy virtualizovaných a kontejnerizovaných síťových funkcí. Dále podporuje realizaci konceptu Zero-touch network and Service Management (ZSM), což je klíčový cíl pro budoucí sítě, kde jsou ruční operace minimalizovány. NGCOR je v podstatě plán, který zajišťuje, že rovina managementu dokáže držet krok s inovacemi a složitostí zaváděnými v datové a řídicí rovině sítí příští generace.

## K čemu slouží

NGCOR byl vytvořen, aby řešil rostoucí provozní složitost a náklady spojené s řízením více-dodavatelských a více-technologických sítí. Před jeho definicí bylo řízení sítí často izolované, s oddělenými systémy [OSS](/mobilnisite/slovnik/oss/) pro různé síťové domény (např. rádiové, transportní, jádrové) a technologie (2G, 3G, 4G). To vedlo k vysokým integračním nákladům, neefektivním procesům a neschopnosti rychle nasazovat a zajišťovat nové služby. Nástup 5G s jeho sliby síťového řezání, komunikace s ultra-spolehlivým nízkým zpožděním (URLLC) a komunikace s masivními strojovými zařízeními (mMTC) učinil tyto zastaralé provozní modely neudržitelnými.

Historický kontext pro NGCOR představuje posun průmyslu směrem k softwarově definovaným sítím (SDN) a virtualizaci síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)). Zatímco tyto technologie přinesly flexibilitu, vytvořily také nové výzvy pro správu virtualizovaných zdrojů a řetězců služeb. NGCOR poskytuje potřebné provozní požadavky pro využití této flexibility. Řeší problém fragmentovaného managementu definováním konvergovaného rámce, který abstrahuje technologické specifika a umožňuje operátorům spravovat celou svou síť pomocí společných principů a rozhraní.

Konečnou motivací pro NGCOR je umožnit škálovatelný, automatizovaný a nákladově efektivní provoz. Řeší omezení předchozích přístupů, které byly reaktivní, manuální a specifické pro danou technologii. Standardizací provozních požadavků NGCOR pokládá základy pro autonomní sítě, snižuje čas potřebný pro uvedení nových služeb na trh a zajišťuje, že provozní schopnosti se vyvíjejí současně s pokročilými funkcemi nabízenými sítěmi 5G a dalšími generacemi.

## Klíčové vlastnosti

- Definuje požadavky pro konvergovanou správu více-RAT a více-jádrových sítí (EPC a 5GC)
- Podporuje správu jak fyzických, tak virtualizovaných síťových funkcí (PNF a VNF)
- Umožňuje automatizaci s uzavřenou smyčkou pro správu poruch, konfigurace a výkonnosti
- Poskytuje standardizované datové modely a rozhraní směrem k vyšším systémům (northbound interfaces) pro integraci OSS
- Usnadňuje správu životního cyklu síťových řezů a jejich součástí
- Pokládá základy pro architektury Zero-touch network and Service Management (ZSM)

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TS 28.390** (Rel-19) — Solution Profiles for Interface IRPs
- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements
- **TS 32.851** (Rel-12) — Network Sharing OAM Requirements

---

📖 **Anglický originál a plná specifikace:** [NGCOR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngcor/)
