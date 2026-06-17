---
slug: "osf"
url: "/mobilnisite/slovnik/osf/"
type: "slovnik"
title: "OSF – Operations System Functions"
date: 2025-01-01
abbr: "OSF"
fullName: "Operations System Functions"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/osf/"
summary: "Funkční komponenty v rámci telekomunikačního systému podpory provozu (OSS) nebo systému pro správu sítě (NMS). OSF zajišťují úlohy jako správa poruch, konfigurace, účtování, výkon a zabezpečení (FCAPS"
---

OSF je soubor funkčních komponent v rámci systému podpory provozu (Operations Support System), který zajišťuje úlohy jako správa poruch, konfigurace, účtování, výkon a zabezpečení síťových prvků a služeb.

## Popis

Funkce operačního systému (Operations System Functions – OSF) představují základní soubor řídicích funkcí a schopností, které jsou součástí systému podpory provozu ([OSS](/mobilnisite/slovnik/oss/)) nebo systému pro správu sítě ([NMS](/mobilnisite/slovnik/nms/)) v síti 3GPP. Jsou definovány v rámci telekomunikačního managementu (TM, specifikace řady 32) a poskytují logickou architekturu pro správu síťových zdrojů, služeb a obchodních operací telekomunikačního poskytovatele služeb. OSF nejsou jediným softwarovým celkem, ale konceptuálním modelem, který rozkládá komplexní úlohu správy sítě a služeb na řízené, interoperabilní funkční bloky. Tyto funkce vzájemně spolupracují a komunikují s funkcemi síťových prvků ([NEF](/mobilnisite/slovnik/nef/)) nebo spravovanými prvky ([ME](/mobilnisite/slovnik/me/)) v síti prostřednictvím standardizovaných rozhraní, primárně rozhraní Itf-N (severní rozhraní).

Architektura OSF je typicky vrstvená, v souladu s logickou vrstvenou architekturou TMN (Telecommunications Management Network): vrstva obchodního managementu (BML), vrstva správy služeb (SML), vrstva správy sítě ([NML](/mobilnisite/slovnik/nml/)) a vrstva správy prvků ([EML](/mobilnisite/slovnik/eml/)). Každá vrstva obsahuje specifické OSF. Například OSF na EML jsou zodpovědné za přímou správu konkrétních typů síťových prvků (např. všech eNodeB od jednoho dodavatele) a provádějí funkce jako stahování softwaru a sběr alarmů. OSF na NML poskytují pohled na celou síť, spravují zdroje napříč více správci prvků pro úlohy jako zřizování koncových spojení a analýza výkonu. OSF na SML se zabývají instancemi služeb nabízených zákazníkům (např. hlasový nebo datový tarif) a zajišťují objednávání služeb, jejich aktivaci a záruku kvality. OSF na BML podporují činnosti na podnikové úrovni, jako je rozpočtování, plánování a správa vztahů se zákazníky.

OSF fungují tak, že zpracovávají informace přijaté ze sítě prostřednictvím jižních rozhraní (např. pomocí protokolů jako SNMP, NETCONF/YANG nebo protokolů specifických pro 3GPP založených na [CORBA](/mobilnisite/slovnik/corba/)) a prezentují agregované, akceschopné informace severním směrem dalším OSF nebo externím obchodním systémům. Mezi klíčové interní procesy patří mediace dat (převod dat specifických pro dodavatele do standardního formátu), korelace (propojení souvisejících alarmů nebo událostí) a vymáhání politik. Implementace OSF umožňuje automatizaci, snižuje provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) a zajišťuje efektivní provoz sítě, plnění smluvních úrovní služeb (SLA) a schopnost rychle reagovat na nová nasazení služeb nebo poruchové stavy.

## K čemu slouží

Koncept OSF byl vytvořen, aby řešil základní výzvu správy stále složitějších telekomunikačních sítí s více dodavateli a technologiemi. Před standardizovanými rámci pro správu se operátoři spoléhali na proprietární systémy pro správu prvků (EMS), které vytvářely izolované správní celky, což vedlo k vysokým integračním nákladům, manuálním procesům a neschopnosti mít jednotný, komplexní pohled na výkon sítě a stav služeb. Vytvoření modelu OSF v rámci TMN a později rámců 3GPP TM poskytlo plán pro výstavbu interoperabilních, škálovatelných a efektivních systémů správy.

Primární problémy, které OSF řeší, jsou provozní roztříštěnost a nedostatek automatizace. Definováním společné funkční architektury umožňují různým softwarovým komponentám – potenciálně od různých dodavatelů – spolupracovat na provádění komplexní správy FCAPS (poruchy, konfigurace, účtování, výkon, zabezpečení). To operátorům umožňuje automatizovat rutinní úlohy jako zřizování služeb, provádět analýzu hlavní příčiny napříč síťovými vrstvami a implementovat politiky zajištění služeb. Historický kontext je zakořeněn v přechodu od monolitických, hlasově orientovaných sítí k distribuovaným, paketovým sítím (2G na 3G/4G), kde objem spravovaných entit a rychlost změn služeb prudce vzrostly.

OSF navíc poskytují základ pro moderní provozní paradigma, jako je bezobslužná správa sítě a služeb (ZSM) a management založený na záměru (intent-based management). Abstrahují složitost podkladové síťové technologie, což umožňuje funkcím vyšších vrstev spravovat služby na základě obchodního záměru namísto konfigurace na nízké úrovni zařízení. Vývoj OSF v rámci vydání 3GPP byl hnán potřebou spravovat nové síťové funkce (např. LTE, 5G, síťové segmenty), přijímat nové IT technologie (cloud, virtualizace) a podporovat nové obchodní modely, což zajišťuje, že řídicí rovina drží krok s inovacemi v řídicí a uživatelské rovině.

## Klíčové vlastnosti

- Standardizovaný funkční rozklad schopností OSS/NMS
- Vrstvená architektura (BML, SML, NML, EML) pro oddělení zájmů
- Umožňuje interoperabilitu více dodavatelů prostřednictvím definovaných referenčních bodů
- Podporuje správu FCAPS (poruchy, konfigurace, účtování, výkon, zabezpečení)
- Usnadňuje automatizaci životního cyklu síťových a služebních operací
- Poskytuje základ pro zajištění služeb a správu SLA

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.141** (Rel-19) — Subscription Management (SuM) Architecture
- **TS 32.600** (Rel-19) — 3GPP Configuration Management Specification
- **TS 32.611** (Rel-19) — Bulk CM IRP Requirements
- **TS 32.819** (Rel-8) — Element Management Layer OS Functions
- **TS 33.794** (Rel-19) — Study on Zero Trust Security Enablers for 5G

---

📖 **Anglický originál a plná specifikace:** [OSF na 3GPP Explorer](https://3gpp-explorer.com/glossary/osf/)
