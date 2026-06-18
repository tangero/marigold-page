---
slug: "v-udr"
url: "/mobilnisite/slovnik/v-udr/"
type: "slovnik"
title: "V-UDR – Visited Unified Data Repository"
date: 2026-01-01
abbr: "V-UDR"
fullName: "Visited Unified Data Repository"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/v-udr/"
summary: "Funkce Unified Data Repository nasazená v rámci navštívené veřejné pozemní mobilní sítě (VPLMN). Ukládá předplatitelská a politická data relevantní pro roamující uživatele, což umožňuje navštívené sít"
---

V-UDR je funkce Unified Data Repository nasazená v navštívené síti pro ukládání předplatitelských a politických dat roamujících uživatelů, což umožňuje místní rozhodování bez neustálých dotazů na domovskou síť.

## Popis

Visited Unified Data Repository (V-UDR) je funkce pro ukládání dat v architektuře sdílené datové vrstvy jádra 5G sítě, konkrétně nasazená v navštívené veřejné pozemní mobilní síti. Funguje jako lokální mezipaměť nebo instance [UDR](/mobilnisite/slovnik/udr/) pro data týkající se roamujících předplatitelů. Primární role V-UDR spočívá v ukládání podmnožiny uživatelských dat – jako jsou politická data, předplatitelská data a aplikační data – která jsou vyžadována pro to, aby síťové funkce ([NF](/mobilnisite/slovnik/nf/)) [VPLMN](/mobilnisite/slovnik/vplmn/) mohly roamujícího uživatele efektivně obsluhovat. Tato data jsou typicky zřízena nebo synchronizována z domovského UDR ([H-UDR](/mobilnisite/slovnik/h-udr/)) v domovské síti uživatele.

Architektonicky V-UDR implementuje stejné rozhraní založené na službách jako standardní UDR, konkrétně Nudr (např. Nudr_[DM](/mobilnisite/slovnik/dm/), Nudr_[DR](/mobilnisite/slovnik/dr/)). Síťové funkce ve VPLMN, jako je Visited Policy Control Function ([V-PCF](/mobilnisite/slovnik/v-pcf/)) nebo Visited Network Repository Function (V-NRF), mohou dotazovat V-UDR přímo přes tato rozhraní, aby získaly potřebná data pro rozhodování o politikách nebo autorizaci služeb. Tento lokální přístup k datům se vyhýbá potřebě signalizace mezi [PLMN](/mobilnisite/slovnik/plmn/) pro každý datový požadavek, což by znamenalo významnou latenci a zatížení rozhraní mezi operátory. Synchronizace dat mezi H-UDR a V-UDR je klíčovým aspektem, často řízeným dohodami a protokoly pro směrování roamingu, aby byla zajištěna konzistence dat a soukromí.

Během provozu, když se UE přesune do roamingu v síti VPLMN, jsou relevantní data načtena z H-UDR a uložena ve V-UDR. Následné dotazy od síťových funkcí VPLMN jsou obsluhovány lokálně. V-UDR podporuje princip oddělení a nezávislosti dat v jádru 5G. Umožňuje pokročilé roamingové funkce tím, že navštívené síti dovoluje aplikovat politiky na základě profilu předplatitele bez nutnosti reálné interakce s domovskou sítí pro každou transakci. To je zvláště důležité pro řízení politik, účtování a umožnění síťového řezání pro roamující uživatele, kde může být nutné, aby výběr řezu a vynucování politik probíhalo v rámci navštívené sítě.

## K čemu slouží

V-UDR byl zaveden, aby vyřešil výkonnostní a škálovatelnostní výzvy centralizovaného ukládání dat v roamingových scénářích. V dřívějších architekturách vyžadoval každý požadavek na politická nebo předplatitelská data od síťové funkce v navštívené síti dotaz na UDR v domovské síti. To vytvářelo významnou signalizační latenci, zvyšovalo závislost na spolehlivosti propojení mezi PLMN (rozhraní N32) a omezovalo schopnost navštívené sítě rychle reagovat na dynamické požadavky služeb.

Jeho vytvoření bylo motivováno potřebou autonomnějšího provozu v navštívené síti, což je klíčové pro služby 5G s nízkou latencí a efektivní využití síťových zdrojů. Udržováním lokální kopie nezbytných dat umožňuje V-UDR rychlejší rozhodování pro zřizování relací, vynucování politik a autorizaci služeb. To je v souladu s architektonickými cíli 5G, kterými jsou decentralizace a vystavení sítě, což umožňuje VPLMN nabízet roamujícím uživatelům přizpůsobené služby při současném dodržování politik domovského operátora.

## Klíčové vlastnosti

- Ukládá lokální kopie předplatitelských a politických dat roamujících uživatelů v rámci VPLMN
- Poskytuje přístup k datům navštíveným síťovým funkcím (např. V-PCF, V-NRF) přes rozhraní založená na službách Nudr
- Snižuje signalizační latenci a zatížení propojení mezi PLMN tím, že obsluhuje datové požadavky lokálně
- Podporuje mechanismy synchronizace dat s domovským UDR (H-UDR)
- Umožňuje lokální vynucování politik a rozhodování pro roamující uživatele
- Usnadňuje implementaci síťového řezání a pokročilých služeb v roamingových scénářích

## Související pojmy

- [UDR – Unified Data Repository](/mobilnisite/slovnik/udr/)
- [V-PCF – Visited Policy Control Function](/mobilnisite/slovnik/v-pcf/)

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework

---

📖 **Anglický originál a plná specifikace:** [V-UDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-udr/)
