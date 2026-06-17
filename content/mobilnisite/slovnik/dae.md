---
slug: "dae"
url: "/mobilnisite/slovnik/dae/"
type: "slovnik"
title: "DAE – Declarative Application Environment"
date: 2025-01-01
abbr: "DAE"
fullName: "Declarative Application Environment"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dae/"
summary: "DAE je rámec 3GPP umožňující vystavení sítě a interakci s aplikacemi prostřednictvím deklarativních API. Umožňuje aplikacím specifikovat požadované síťové chování a výsledky namísto imperativních přík"
---

DAE je rámec 3GPP, který umožňuje vystavení sítě a interakci s aplikacemi tím, že aplikacím umožňuje specifikovat požadované síťové chování prostřednictvím deklarativních API namísto imperativních příkazů.

## Popis

Deklarativní aplikační prostředí (DAE) je standardizovaný rámec v rámci specifikací 3GPP, který poskytuje aplikacím deklarativní rozhraní pro interakci se síťovými funkcemi a službami. Na rozdíl od tradičních imperativních [API](/mobilnisite/slovnik/api/), kde aplikace vydávají konkrétní příkazy pro řízení síťového chování, umožňuje DAE aplikacím deklarovat jejich požadované výsledky, záměry nebo politiky, a síť autonomně určuje, jak tyto deklarace splnit. Tato změna paradigmatu umožňuje vyšší míru abstrakce, zjednodušuje aplikační logiku a snižuje provázanost mezi aplikacemi a podkladovými síťovými implementacemi.

Architektonicky funguje DAE jako mezivrstva mezi aplikacemi a síťovými funkcemi, typicky implementovaná v rámci funkce pro vystavení služebních schopností (SCEF) nebo funkce pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) v systémech 5G. Skládá se z několika klíčových komponent: brány deklarativního API, která přijímá a validuje aplikační deklarace, politického enginu, který tyto deklarace interpretuje do síťově specifických akcí, správce prostředků, který mapuje deklarace na dostupné síťové prostředky, a monitorovací komponenty, která zajišťuje udržení deklarovaných výsledků. Rámec podporuje různé typy deklarací včetně požadavků na kvalitu služby, politik mobility, bezpečnostních omezení a cílů na úrovni služeb.

DAE funguje tak, že přijímá strukturované deklarace od aplikací prostřednictvím RESTful API nebo rozhraní založených na zprávách. Tyto deklarace jsou vyjádřeny ve standardizovaných datových modelech definovaných ve specifikacích 3GPP, typicky pomocí formátů [JSON](/mobilnisite/slovnik/json/) nebo XML. Systém DAE zpracovává tyto deklarace v několika fázích: validace vůči síťovým schopnostem a politikám, překlad do síťově specifických konfiguračních příkazů, vyjednávání se síťovými funkcemi o přidělení prostředků a průběžné monitorování, které zajišťuje udržení deklarovaného stavu. Když se síťové podmínky změní, může DAE automaticky přizpůsobit konfigurace, aby zachoval deklarované výsledky bez nutnosti zásahu aplikace.

Role tohoto rámce v síti je mnohostranná: slouží jako abstraktní vrstva, která před aplikacemi skrývá složitost sítě, umožňuje principy sítí založených na záměrech v mobilních sítích, usnadňuje síťovou automatizaci snížením manuální konfigurace a podporuje dynamické vytváření služeb. DAE je obzvláště cenný ve scénářích vyžadujících síťové řezy, edge computing a služby IoT, kde mají aplikace specifické požadavky, ale neměly by potřebovat detailní znalosti implementace rádiového přístupu nebo jádra sítě. Integruje se s existujícími mechanismy 3GPP, jako je řízení politiky a účtování (PCC), funkce pro výběr síťového řezu ([NSSF](/mobilnisite/slovnik/nssf/)) a funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)), aby prosadil deklarované politiky napříč síťovou infrastrukturou.

## K čemu slouží

DAE byl vytvořen, aby řešil rostoucí složitost integrace aplikací s mobilními sítěmi, zejména jak se sítě vyvíjely směrem k 5G se schopnostmi jako síťové řezy, edge computing a masivní IoT. Tradiční imperativní [API](/mobilnisite/slovnik/api/) vyžadovala, aby aplikace měly detailní znalost vnitřního fungování sítě a spravovaly složité stavové automaty, což zvyšovalo složitost vývoje, vytvářelo těsnou provázanost mezi aplikacemi a konkrétními síťovými implementacemi a ztěžovalo přizpůsobení se změnám nebo výpadkům sítě. Deklarativní přístup zjednodušuje vývoj aplikací tím, že umožňuje vývojářům soustředit se na to, čeho chtějí dosáhnout, spíše než na to, jak toho dosáhnout prostřednictvím konkrétních síťových příkazů.

Historicky se vystavení sítě v systémech 3GPP vyvíjelo od základních webových služeb Parlay X v raných vydáních k sofistikovanější funkci pro vystavení služebních schopností (SCEF) v 4G a funkci pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) v 5G. Tyto přístupy však stále z velké části následovaly imperativní modely, kde aplikace musely vydávat konkrétní příkazy pro síťové akce. DAE představuje změnu paradigmatu inspirovanou podobnými přístupy ve výpočetním cloudu a softwarově definovaných sítích, která uznává, že jak se sítě stávají více programovatelnými a virtualizovanými, je potřeba vyšší abstraktní vrstva pro správu složitosti a umožnění skutečné síťové automatizace.

Tato technologie řeší několik klíčových problémů: snižuje kognitivní zátěž vývojářů aplikací abstrakcí síťové složitosti, umožňuje robustnější a adaptivnější aplikace, které mohou přežít změny sítě bez přeprogramování, usnadňuje síťovou automatizaci tím, že umožňuje síti optimalizovat způsob plnění aplikačních požadavků a podporuje nové obchodní modely, kde mohou být síťové schopnosti vystaveny jako deklarativní služby. Řešením těchto výzev DAE umožňuje rychlejší inovace služeb, snižuje provozní náklady a zpřístupňuje pokročilé síťové funkce vývojářům aplikací bez nutnosti hluboké telekomunikační odbornosti.

## Klíčové vlastnosti

- Deklarativní rozhraní API pro specifikaci požadovaných síťových výsledků
- Politický překlad deklarací do síťových konfigurací
- Integrace se síťovými funkcemi 3GPP včetně NEF a SCEF
- Podpora síťových řezů a deklarací kvality služby
- Průběžné monitorování a adaptace pro udržení deklarovaných stavů
- Standardizované datové modely pro komunikaci aplikace-síť

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [DAE na 3GPP Explorer](https://3gpp-explorer.com/glossary/dae/)
