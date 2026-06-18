---
slug: "pop-core-dm"
url: "/mobilnisite/slovnik/pop-core-dm/"
type: "slovnik"
title: "POP-CORE-DM – Participating Operator Core Network Domain Manager"
date: 2025-01-01
abbr: "POP-CORE-DM"
fullName: "Participating Operator Core Network Domain Manager"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pop-core-dm/"
summary: "Funkce správy sítě odpovědná za správu domény jádrové sítě (CN) účastnického operátora v prostředí více operátorů. Umožňuje delegovanou správu a operační kontrolu nad prostředky CN, usnadňuje spoluprá"
---

POP-CORE-DM je funkce správy sítě, která spravuje doménu jádrové sítě účastnického operátora, umožňující delegovanou správu a řízení v prostředí více operátorů pro roaming, sdílení a služby napříč operátory.

## Popis

Participating Operator Core Network Domain Manager (POP-CORE-DM) je klíčová entita správy definovaná v rámci architektury 3GPP Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)), konkrétně v TS 32.130. Funguje jako Domain Manager ([DM](/mobilnisite/slovnik/dm/)) s rozsahem omezeným na doménu jádrové sítě (CN) účastnického operátora. Účastnický operátor je operátor, který poskytuje prostředky nebo služby v ekosystému více operátorů, jako jsou scénáře sdílení sítě, roamingu nebo multi-operator core network ([MOCN](/mobilnisite/slovnik/mocn/)). POP-CORE-DM je podřízen vyšší manažerské entitě, typicky Network Manageru ([NM](/mobilnisite/slovnik/nm/)) hostitelského nebo primárního operátora, ale zachovává si delegovanou pravomoc nad vlastními prostředky CN.

Z architektonického hlediska POP-CORE-DM komunikuje se spravovanými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) CN ve své doméně pomocí specifických referenčních bodů správy, jako je Itf-N pro severojižní komunikaci s nadřazeným NM a jižní rozhraní (např. založená na NETCONF/YANG, [SNMP](/mobilnisite/slovnik/snmp/) nebo proprietárních protokolech) směrem k prvkům CN, jako jsou [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), UPF a další komponenty 5G Core. Pro svou doménu implementuje model správy FCAPS (Fault, Configuration, Accounting, Performance, Security). Jeho primární rolí je poskytovat vrstvu abstrakce, která překládá direktivy služeb a politik vysoké úrovně od nadřazeného NM do specifických konfiguračních příkazů, úloh monitorování výkonu a akcí správy poruch pro prvky CN pod jeho kontrolou.

Funkčně POP-CORE-DM provádí správu životního cyklu (LCM) softwaru a funkcí CN, spravuje specifické konfigurační parametry CN, sbírá a reportuje měření výkonu (PM) a řeší detekci a lokalizaci poruch ve své doméně. Zajišťuje, že doména CN dodržuje smlouvy o úrovni služeb (SLA) a politiky dohodnuté s nadřazeným NM. Tím, že funguje jako delegovaný manažer, umožňuje účastnickému operátorovi zachovat si operační kontrolu a přehled nad vlastní infrastrukturou CN a zároveň se bezproblémově integrovat do většího prostředí spravovaných služeb více operátorů. Toto oddělení manažerských domén je klíčové pro bezpečnost, odpovědnost a efektivní provoz v komplexních, spolupracujících nasazeních sítí.

## K čemu slouží

POP-CORE-DM byl zaveden, aby řešil složitosti správy vznikající z pokročilých scénářů sdílení sítí a spolupráce více operátorů, které se staly významnými přibližně od 3GPP Release 12. Předchozí přístupy často zahrnovaly monolitické systémy správy nebo vyžadovaly, aby jeden operátor měl plný administrativní přístup k síti druhého, což představovalo významné bezpečnostní, provozní a regulační výzvy. Účelem POP-CORE-DM je umožnit strukturované, bezpečné a škálovatelné delegování manažerské pravomoci.

Řeší problém, jak může účastnický operátor přispět svými prostředky jádrové sítě do sdílené služby (jako je neutrální hostitelská síť nebo roamingový hub), aniž by o tyto prostředky přišel přímou kontrolu. Umožňuje jasné vymezení manažerských odpovědností: nadřazený Network Manager (např. hostitelského operátora) spravuje službu end-to-end, zatímco POP-CORE-DM spravuje technické detaily vlastní domény CN. Tento model podporuje operační nezávislost, usnadňuje řešení problémů v rámci definovaných hranic a umožňuje každému operátorovi používat pod DM své vlastní vendor-specific element management systems (EMS). Vytvoření POP-CORE-DM bylo motivováno posunem průmyslu k virtualizaci sítí, slicing a dynamičtějším formám spolupráce, které vyžadovaly standardizovaný, hierarchický rámec správy schopný pojmout více administrativních domén.

## Klíčové vlastnosti

- Delegovaná správa domény pro prostředky jádrové sítě
- Správa FCAPS (Fault, Configuration, Accounting, Performance, Security) pro doménu CN
- Abstrakce informací specifických pro správu CN pro nadřazené Network Managery
- Podpora standardizovaných severojižních (Itf-N) a vendor-specific jižních rozhraní
- Správa životního cyklu síťových funkcí a softwaru CN
- Monitorování výkonu a správa poruch lokalizovaná na doménu CN účastnického operátora

## Definující specifikace

- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements

---

📖 **Anglický originál a plná specifikace:** [POP-CORE-DM na 3GPP Explorer](https://3gpp-explorer.com/glossary/pop-core-dm/)
