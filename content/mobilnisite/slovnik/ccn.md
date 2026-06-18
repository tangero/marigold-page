---
slug: "ccn"
url: "/mobilnisite/slovnik/ccn/"
type: "slovnik"
title: "CCN – Composition Capable Network"
date: 2025-01-01
abbr: "CCN"
fullName: "Composition Capable Network"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ccn/"
summary: "Síťová architektura umožňující dynamické skládání síťových funkcí a služeb od více poskytovatelů. Umožňuje operátorům vytvářet přizpůsobené síťové řezy kombinací zdrojů a schopností napříč administrat"
---

CCN je síťová architektura umožňující dynamické skládání síťových funkcí a služeb od více poskytovatelů za účelem vytváření přizpůsobených síťových řezů napříč administrativními doménami.

## Popis

Composition Capable Network (CCN) je architektonický rámec 3GPP, který umožňuje dynamické skládání síťových funkcí a služeb napříč více administrativními doménami. Jádrem CCN jsou mechanismy pro vyhledávání, výběr a kombinaci síťových schopností od různých poskytovatelů za účelem vytváření služeb typu end-to-end. Tato architektura zavádí kompoziční funkce, které fungují jako zprostředkovatelé mezi spotřebiteli služeb a poskytovateli síťových zdrojů a spravují životní cyklus složených síťových služeb prostřednictvím standardizovaných rozhraní a protokolů.

Architektura CCN se skládá z několika klíčových komponent: Composition Function ([CF](/mobilnisite/slovnik/cf/)), která orchestruje proces skládání; Service Registry, která uchovává informace o dostupných síťových schopnostech; Resource Manager, který zprostředkovává přidělování a rezervaci zdrojů; a Composition Manager, který dohlíží na celý životní cyklus skládání. Tyto komponenty spolupracují prostřednictvím standardizovaných referenčních bodů definovaných ve specifikacích 3GPP, což umožňuje interoperabilitu mezi různými síťovými doménami a administrativními subjekty. CF komunikuje s poskytovateli síťových funkcí prostřednictvím kompozičních rozhraní, vyjednává smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) a zajišťuje soulad s technickými a obchodními požadavky.

Z technického hlediska CCN funguje prostřednictvím vícefázového procesu: zjišťování schopností (capability discovery), při kterém jsou identifikovány dostupné síťové funkce a zdroje; plánování skládání (composition planning), při kterém jsou na základě požadavků služby určeny optimální kombinace schopností; vytvoření instance skládání (composition instantiation), při kterém jsou vybrané síťové funkce nakonfigurovány a propojeny; a správa skládání (composition management), při které je složená služba monitorována a udržována po celý svůj životní cyklus. Architektura podporuje jak statické skládání (předem nakonfigurované řetězce služeb), tak dynamické skládání (vytváření služeb na požádání), a to včetně mechanismů pro odolnost proti chybám, vyrovnávání zátěže a zajištění kvality služeb (QoS).

CCN hraje klíčovou roli při umožnění síťového řezání (network slicing) a přizpůsobení služeb v sítích 5G a budoucích generací. Tím, že umožňuje operátorům kombinovat schopnosti od více poskytovatelů, usnadňuje vytváření specializovaných síťových řezů pro různé případy užití (např. rozšířené mobilní širokopásmové připojení, hromadný IoT, ultra-spolehlivá komunikace s nízkou latencí) bez nutnosti řešení od jediného dodavatele. Architektura také podporuje obchodní modely, jako je síť jako služba (NaaS), a usnadňuje integraci síťových funkcí třetích stran, čímž podporuje inovace a konkurenci v telekomunikačním ekosystému.

## K čemu slouží

CCN byl vyvinut pro řešení rostoucí složitosti síťových prostředí s více dodavateli a více doménami v moderní telekomunikaci. Tradiční síťové architektury často spoléhaly na monolitická, vertikálně integrovaná řešení od jediného dodavatele, což ztěžovalo kombinaci schopností od různých poskytovatelů a omezovalo flexibilitu operátorů. Jak se sítě vyvíjely směrem k otevřenějším, disagregovaným architekturám s virtualizací síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a softwarově definovaným sítím ([SDN](/mobilnisite/slovnik/sdn/)), objevila se potřeba standardizovaných mechanismů pro skládání služeb typu end-to-end z heterogenních síťových komponent.

Primární motivací pro CCN bylo umožnit operátorům vytvářet přizpůsobené síťové služby dynamickým kombinováním schopností z více administrativních domén a technologických poskytovatelů. Tím se řeší několik omezení předchozích přístupů: odstraňuje závislost na jediném dodavateli (vendor lock-in) tím, že umožňuje interoperabilitu mezi různými implementacemi síťových funkcí; umožňuje efektivnější využití zdrojů tím, že operátorům umožňuje vybírat nejvhodnější schopnosti pro konkrétní požadavky služeb; a podporuje nové obchodní modely, kde mohou být síťové schopnosti nabízeny jako služby napříč organizačními hranicemi. CCN také usnadňuje realizaci síťového řezání v systémech 5G, kde různé řezy mohou vyžadovat různé kombinace síťových funkcí a zdrojů.

Historicky CCN vznikl z práce 3GPP na vývoji síťové architektury, zejména v kontextu zpřístupnění služebních schopností (service capability exposure) a virtualizace síťových funkcí (NFV). Navazuje na koncepty z dřívějších standardizačních snah v oblastech, jako je servisně orientovaná architektura ([SOA](/mobilnisite/slovnik/soa/)) a řetězení síťových služeb (network service chaining), ale aplikuje je specificky na telekomunikační doménu s požadavky na provozní spolehlivost, zabezpečení a výkon na úrovni telekomunikačních operátorů. Vývoj CCN byl hnán požadavky operátorů na větší flexibilitu při vytváření a nasazování služeb, stejně jako průmyslovým trendem směrem k disagregaci sítí a otevřeným rozhraním.

## Klíčové vlastnosti

- Dynamické skládání síťových funkcí napříč administrativními doménami
- Standardizovaná rozhraní pro zjišťování a vyjednávání schopností
- Podpora statického i dynamického skládání služeb
- Správa životního cyklu složených síťových služeb
- Zajištění kvality služeb (QoS) napříč složenými řetězci služeb
- Vynucování obchodních a technických politik během procesu skládání

## Definující specifikace

- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 44.901** (Rel-19) — Extended NACC for External Cell Change
- **TS 48.018** (Rel-19) — BSS-SGSN Interface for GPRS Control

---

📖 **Anglický originál a plná specifikace:** [CCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccn/)
