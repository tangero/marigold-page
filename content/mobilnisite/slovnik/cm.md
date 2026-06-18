---
slug: "cm"
url: "/mobilnisite/slovnik/cm/"
type: "slovnik"
title: "CM – Configuration Management"
date: 2026-01-01
abbr: "CM"
fullName: "Configuration Management"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/cm/"
summary: "Configuration Management (CM, správa konfigurace) je základní funkce správy sítě, která řídí, identifikuje, shromažďuje data z a poskytuje data síťovým prvkům. Je nezbytná pro zřizování, inicializaci"
---

CM (Configuration Management, správa konfigurace) je základní funkce správy sítě, která řídí, identifikuje, shromažďuje data z a poskytuje data síťovým prvkům za účelem zřizování, inicializace a udržování provozních parametrů celého systému 3GPP.

## Popis

Configuration Management (CM, správa konfigurace) je klíčovou součástí frameworku Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)) v sítích 3GPP. Zahrnuje soubor funkcí odpovědných za plánování, instalaci, uvedení do provozu, provoz a průběžnou správu všech konfigurovatelných parametrů v síťových prvcích ([NE](/mobilnisite/slovnik/ne/)) a v síti jako celku. To zahrnuje správu hardwarových, softwarových a logických konfigurací. Funkce CM provádějí systémy správy, jako je Element Management System ([EMS](/mobilnisite/slovnik/ems/)) nebo Network Management System ([NMS](/mobilnisite/slovnik/nms/)), které komunikují se spravovanými NE prostřednictvím standardizovaných rozhraní, jako je Itf-N.

Architektura CM je hierarchická a distribuovaná. Na nejnižší úrovni obsahuje každý NE Management Information Base ([MIB](/mobilnisite/slovnik/mib/)), což je virtuální databáze reprezentující všechny spravovatelné objekty v daném prvku, jako jsou verze softwaru, konfigurace desek, přenosové parametry a seznamy sousedních buněk. Systém správy používá protokoly jako Common Object Request Broker Architecture ([CORBA](/mobilnisite/slovnik/corba/)) nebo Simple Network Management Protocol ([SNMP](/mobilnisite/slovnik/snmp/)) k provádění CM operací nad těmito objekty. Mezi klíčové operace patří GET (pro získání aktuálních konfiguračních dat), [SET](/mobilnisite/slovnik/set/) (pro změnu konfigurace), CREATE a DELETE. Tyto operace umožňují zřizování nových služeb, aktualizace softwaru, rekonfigurace pro zotavení z poruch a rozšiřování kapacity.

Role CM pokrývá celý životní cyklus sítě. Během zavádění sítě se CM používá pro počáteční instalaci a uvedení NE do provozu nastavením jejich základních provozních parametrů. V denním provozu podporuje aktivaci/deaktivaci funkcí, softwarové aktualizace a dynamickou rekonfiguraci pro optimalizaci nebo vyrovnávání zatížení. Například v Radio Access Network (RAN) CM spravuje kritické parametry, jako jsou identity buněk, kmitočtové nosné, scrambling kódy, prahové hodnoty pro předávání spojení a nastavení náklonu antén. V jádru sítě spravuje kapacity Mobile Switching Centre (MSC), kapacity předplatitelů v Home Location Register (HLR) a access point names (APN) v Gateway GPRS Support Node (GGSN).

Kritickým aspektem CM je udržování konzistence a integrity. Systémy správy často používají funkce konfiguračních auditů a synchronizace k detekci a opravě nesrovnalostí mezi zamýšlenou konfigurací (uloženou v databázi systému správy) a skutečnou konfigurací běžící na NE. Dále CM podporuje funkce zálohování a obnovení, což umožňuje operátorům ukládat známé správné konfigurace a rychle se zotavovat z poruch. Tato komplexní kontrola nad 'plánem' sítě je zásadní pro zajištění dostupnosti služeb, výkonu a zavádění nových technologií bez přerušení služby.

## K čemu slouží

Configuration Management existuje proto, aby řešila obrovskou složitost a rozsah moderních telekomunikačních sítí. Jak se sítě vyvíjely z jednoduchých hlasových systémů na komplexní ekosystémy s více dodavateli a technologiemi podporující hlas, data a IoT, ruční konfigurace tisíců síťových prvků se stala nemožnou. Účelem CM je automatizovat, standardizovat a centralizovat řízení síťových parametrů, což umožňuje efektivní nasazení, spolehlivý provoz a rychlé zavádění služeb.

Historicky, bez automatizované CM, bylo zřizování sítě náchylné k chybám, pomalé a nekonzistentní, což vedlo k dlouhodobým výpadkům služeb a obtížnému odstraňování problémů. Standardizace CM v rámci 3GPP tyto problémy řeší definováním společné sady spravovaných objektů a operací. To umožňuje operátorům používat jednotné systémy správy pro řízení zařízení od různých dodavatelů, čímž zajišťuje interoperabilitu a snižuje provozní náklady. Řeší kritickou potřebu reprodukovatelnosti, možnosti auditu a kontroly nad stavem sítě, což je zásadní pro plnění smluv o úrovni služeb (SLA) a regulatorních požadavků.

Navíc je CM hybatelem pokročilé automatizace sítí a Self-Organizing Networks (SON). Tím, že poskytuje programové rozhraní pro čtení a úpravu síťových konfigurací, tvoří CM základní vrstvu, na které jsou vybudovány funkce SON, jako je správa Automatic Neighbor Relation (ANR), Mobility Load Balancing (MLB) a Capacity and Coverage Optimization (CCO). Řeší problém agility sítě, což operátorům umožňuje dynamicky reagovat na vzorce provozu, poruchy a zavádění nových síťových řezů v systémech 5G.

## Klíčové vlastnosti

- Zřizování a uvedení do provozu síťových prvků a softwaru
- Správa hardwarových, softwarových a logických konfigurací prostředků
- Podpora zálohování, obnovení a auditu/synchronizace konfigurace
- Standardizovaná rozhraní (např. Itf-N) pro správu více dodavatelů
- Integrace se správou poruch a výkonu pro operace s uzavřenou smyčkou
- Základ pro automatizovanou optimalizaci sítě a funkce Self-Organizing Network (SON)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 28.533** (Rel-19) — Management and orchestration; Architecture framework
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 28.606** (Rel-12) — CN and non-3GPP interworking NRM IRP Solution Sets
- **TS 28.616** (Rel-19) — EPC and non-3GPP access NRM IRP SS definitions
- **TS 28.621** (Rel-19) — Generic Network Resource Model (NRM) IRP Requirements
- … a dalších 120 specifikací

---

📖 **Anglický originál a plná specifikace:** [CM na 3GPP Explorer](https://3gpp-explorer.com/glossary/cm/)
