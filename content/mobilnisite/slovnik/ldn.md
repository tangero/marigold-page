---
slug: "ldn"
url: "/mobilnisite/slovnik/ldn/"
type: "slovnik"
title: "LDN – Local Distinguished Name"
date: 2026-01-01
abbr: "LDN"
fullName: "Local Distinguished Name"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ldn/"
summary: "Konvence pojmenování používaná v systému správy sítí 3GPP (Network Management System, NMS) pro jednoznačnou identifikaci spravovaných objektů a jejich instancí. Poskytuje hierarchickou, čitelnou cestu"
---

LDN (Local Distinguished Name) je hierarchická konvence pojmenování používaná v systému správy sítí 3GPP (Network Management System) pro jednoznačnou identifikaci spravovaných objektů a jejich instancí, která poskytuje čitelné cesty pro provádění síťových operací.

## Popis

Local Distinguished Name (LDN) je klíčovým konceptem v architektuře systému správy telekomunikačních sítí 3GPP (Telecommunications Management Network, TMN) a jeho nástupci, systému správy sítí (Network Management System, [NMS](/mobilnisite/slovnik/nms/)), jak je definováno ve specifikacích jako 32.158 a 32.300. Jedná se o strukturovaný pojmenovávací mechanismus používaný k jednoznačné adresaci každé instance spravovaného objektu v rámci systému správy. LDN představuje „umístění“ nebo identitu instance spravovaného objektu ve stromu řídicích informací. Jedná se o posloupnost relativních rozlišujících jmen (Relative Distinguished Names, RDN), která tvoří cestu od kořene pojmenovávacího stromu ke konkrétní instanci objektu.

LDN je konstruován hierarchicky. Například LDN pro konkrétní buňku může být: "ManagedElement=RNC-1, ManagedFunction=NodeB-1, ManagedFunction=Cell-1". Každá část (např. "ManagedElement=RNC-1") je RDN, což je dvojice klíč–hodnota identifikující úroveň v hierarchii. LDN poskytuje kontext; znalost celého LDN umožňuje řídicímu systému přesně lokalizovat a komunikovat s touto buňkou pro operace jako čtení jejího stavu, aktualizace její konfigurace nebo přijímání alarmů z ní. LDN jsou hojně používány na rozhraní Interface-N (Itf-N) a dalších řídicích rozhraních pro odkazování na objekty v příkazech a oznámeních.

Jeho fungování je nedílnou součástí modelu manažer–agent. Agent sídlící na síťovém prvku (Network Element, [NE](/mobilnisite/slovnik/ne/)) udržuje databázi řídicích informací (Management Information Base, [MIB](/mobilnisite/slovnik/mib/)), kde každá instance spravovaného objektu má definovaný LDN. Když manažer (např. Operation Support System, [OSS](/mobilnisite/slovnik/oss/)) potřebuje provést operaci, použije ve své požadavkové zprávě LDN k určení cíle. Agent interpretuje LDN, prochází svým vnitřním objektovým stromem a provede operaci na správné instanci. Podobně, když agent odešle oznámení (např. alarm), zahrne do něj LDN objektu, který událost vyvolal. Tento systém zajišťuje, že řídicí komunikace je přesná a že manažer má konzistentní pohled na strukturu sítě napříč všemi prvky.

## K čemu slouží

LDN existuje k řešení základního problému jednoznačné a konzistentní identifikace mnoha konfigurovatelných a monitorovatelných entit v komplexní telekomunikační síti. Rané systémy správy často používaly proprietární nebo ploché (flat) systémy pojmenování, což vedlo k integračním problémům, nejednoznačnosti a problémům se škálovatelností s růstem sítí. LDN jako součást standardizovaných principů TMN poskytuje jednotný hierarchický pojmenovávací model, který odráží skutečnou strukturu sítě a zařízení.

Jeho vznik byl motivován potřebou vícenedavatelské interoperability v rámci správy. Zařízení od různých dodavatelů mohla být spravována jedním [OSS](/mobilnisite/slovnik/oss/) pouze tehdy, pokud existoval společný způsob adresace spravovaných objektů. LDN, definovaný v manažerských specifikacích 3GPP, poskytuje tento společný jazyk. Odstraňuje omezení nehierarchických nebo nestandardních identifikátorů tím, že nabízí předvídatelný cestový systém pojmenování. To je klíčové pro automatizovanou provizní přípravu, hromadnou konfiguraci a korelovanou analýzu chyb, kde je vztah mezi objekty (implikovaný hierarchií LDN) stejně důležitý jako objekty samotné. Byl zaveden v Release 8 jako součást zrání manažerského rámce 3GPP.

## Klíčové vlastnosti

- Hierarchická struktura: Odráží vztahy obsahování (containment) mezi síťovými prvky, zařízeními a logickými prostředky.
- Jednoznačná identifikace: Zaručuje jedinečné jméno pro každou instanci spravovaného objektu v rámci řídicí domény.
- Čitelný formát: Skládá se z čitelných párů RDN klíč–hodnota (např. ManagedElementId, EquipmentId), což pomáhá při ladění a manuálních operacích.
- Standardizovaná syntaxe: Definována 3GPP, což zajišťuje konzistenci napříč síťovými prvky a systémy správy od různých dodavatelů.
- Základ pro manažerské operace: Používá se jako primární klíč v interakcích CM (Configuration Management), FM (Fault Management) a PM (Performance Management).
- Navigace založená na cestě: Umožňuje řídicím systémům objevovat a procházet strom spravovaných objektů konstrukcí nebo dekompozicí cest LDN.

## Definující specifikace

- **TS 32.158** (Rel-20) — Management and Orchestration REST Solution Sets
- **TS 32.300** (Rel-19) — 3GPP Network Resource Naming Convention

---

📖 **Anglický originál a plná specifikace:** [LDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ldn/)
