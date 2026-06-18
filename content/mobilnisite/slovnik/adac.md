---
slug: "adac"
url: "/mobilnisite/slovnik/adac/"
type: "slovnik"
title: "ADAC – Automatically Detected and Automatically Cleared"
date: 2025-01-01
abbr: "ADAC"
fullName: "Automatically Detected and Automatically Cleared"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/adac/"
summary: "ADAC je síťový managementový rámec umožňující automatickou detekci a řešení síťových poruch bez lidského zásahu. Snižuje provozní náklady a zvyšuje spolehlivost služeb minimalizací výpadků prostřednic"
---

ADAC je síťový managementový rámec, který umožňuje automatickou detekci a řešení síťových poruch bez lidského zásahu za účelem snížení výpadků a zvýšení spolehlivosti služeb.

## Popis

Automatically Detected and Automatically Cleared (ADAC) je komplexní rámec pro správu sítě definovaný v rámci specifikací Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)) organizace 3GPP. Stanovuje standardizované mechanismy pro autonomní identifikaci, diagnostiku a nápravu síťových poruch napříč infrastrukturou mobilních sítí. Architektura funguje jako uzavřený systém, kde síťové prvky nepřetržitě monitorují svůj provozní stav, detekují anomálie, spouštějí diagnostické procedury a provádějí předdefinované nápravné akce. Tento rámec pokrývá více síťových domén včetně Radio Access Network (RAN), Core Network (CN) a transportních vrstev, čímž poskytuje jednotný přístup ke správě poruch.

Rámec ADAC funguje v několika klíčových fázích: detekce, diagnostika a odstranění. Detekční mechanismy využívají nepřetržité monitorování klíčových výkonnostních ukazatelů ([KPI](/mobilnisite/slovnik/kpi/)), systémy generování alarmů a upozornění na překročení výkonnostních prahových hodnot. Po identifikaci potenciální poruchy jsou automaticky spuštěny diagnostické procedury k izolaci hlavní příčiny, přičemž rozlišují mezi hardwarovými závadami, softwarovými chybami, problémy s konfigurací nebo vnějšími interferencemi. Fáze odstranění pak provede příslušné akce obnovy, které mohou zahrnovat automatickou rekonfiguraci síťových parametrů, přesměrování provozu, procedury obnovy služeb nebo resetování komponent. Tyto akce jsou řízeny systémy řízení založenými na politikách, které definují postupy eskalace a pravidla zásahu.

Mezi klíčové architektonické komponenty patří Network Management System ([NMS](/mobilnisite/slovnik/nms/)) s ADAC schopnostmi, Element Management Systems ([EMS](/mobilnisite/slovnik/ems/)) implementující detekční algoritmy a síťové prvky vybavené funkcemi vlastního monitorování. Rámec se integruje se stávajícími rozhraními správy 3GPP včetně Itf-N (northbound rozhraní) a Itf-S (southbound rozhraní) pro koordinaci akcí napříč různými úrovněmi řízení. ADAC využívá standardizované informační modely definované ve specifikacích 3GPP k zajištění interoperability mezi zařízeními různých výrobců. Systém také zahrnuje učící schopnosti prostřednictvím analýzy historických poruch, což umožňuje rozpoznávání vzorů a prediktivní údržbu v čase.

Role ADAC v síti přesahuje pouhou obnovu po poruše a zahrnuje také optimalizaci výkonu a preventivní údržbu. Automatickým řešením běžných problémů snižuje střední dobu do opravy (MTTR) a zabraňuje eskalaci menších problémů ve vážné výpadky služeb. Rámec podporuje jak reaktivní reakce na okamžité poruchy, tak proaktivní opatření založená na analýze trendů. V moderních sítích jsou funkce ADAC stále častěji implementovány pomocí technik umělé inteligence a strojového učení za účelem zvýšení přesnosti detekce a optimalizace strategií odstranění. Tato automatizace je obzvláště cenná v sítích 5G s jejich zvýšenou komplexitou, požadavky na síťové slicing a přísnými cíli spolehlivosti pro kritické služby.

## K čemu slouží

ADAC byl vyvinut pro řešení rostoucích provozních výzev v mobilních sítích v souvislosti s jejich zvyšující se komplexitou a rozsahem. Tradiční přístupy ruční správy poruch se staly neudržitelnými s rozšířením sítí 4G/LTE, kde samotný objem síťových prvků a vzájemných závislostí činil řešení problémů řízené člověkem pomalým a náchylným k chybám. Rámec řeší problém rostoucích provozních výdajů ([OPEX](/mobilnisite/slovnik/opex/)) spojených s údržbou sítě a zároveň zvyšuje dostupnost a kvalitu služeb. Automatizací rutinních úloh správy poruch umožňuje ADAC síťovým operátorům spravovat větší a složitější sítě s menšími lidskými zdroji.

Historicky vyžadovaly síťové poruchy ruční detekci prostřednictvím monitorovacích systémů následovanou vysláním technika, diagnostikou a opravou – proces, který mohl trvat hodiny i dny. To vedlo k dlouhým výpadkům služeb, nespokojenosti zákazníků a ztrátám příjmů. ADAC řeší tato omezení implementací standardizované automatizace, která omezuje lidský zásah pouze na nejkomplexnější případy. Tato technologie byla motivována potřebou, aby se sítě staly více samoléčícími a odolnými, zejména když se mobilní služby vyvinuly z hlasově orientovaných na datově orientované aplikace s vyššími požadavky na spolehlivost.

Se zavedením 5G a jeho podporou pro aplikace s kritickým nasazením, jako je průmyslová automatizace, autonomní vozidla a vzdálená chirurgie, se požadavek na téměř okamžitou obnovu po poruše stal prvořadým. ADAC poskytuje základní automatizační rámec, který tyto ultra-spolehlivé služby umožňuje zajištěním rychlé detekce a řešení síťových problémů. Rámec také podporuje síťový slicing tím, že umožňuje různé automatizované zásady obnovy pro různé typy slice, což zajišťuje, že kritické slice dostanou při poruchových stavech prioritu. To představuje zásadní posun od reaktivní k proaktivní a prediktivní správě sítě.

## Klíčové vlastnosti

- Automatizovaná detekce poruch prostřednictvím nepřetržitého monitorování KPI a analýzy prahových hodnot
- Standardizované diagnostické procedury pro izolaci hlavní příčiny napříč síťovými doménami
- Automatické akce odstranění založené na politikách včetně rekonfigurace a obnovy
- Integrace se stávajícími rozhraními správy 3GPP (Itf-N, Itf-S) a informačními modely
- Podpora jak reaktivní obnovy po poruše, tak proaktivní preventivní údržby
- Škálovatelná architektura podporující sítě od tisíců po miliony prvků

## Definující specifikace

- **TS 28.111** (Rel-19) — Fault Management Service Specification
- **TS 28.545** (Rel-17) — Fault Supervision for 5G Networks
- **TS 32.111** (Rel-19) — Fault Management Requirements
- **TS 32.541** (Rel-19) — SON Self-Healing Concepts and Requirements
- **TS 32.859** (Rel-12) — Alarm Management Quality Improvement Study

---

📖 **Anglický originál a plná specifikace:** [ADAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/adac/)
