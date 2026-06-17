---
slug: "atu-sti"
url: "/mobilnisite/slovnik/atu-sti/"
type: "slovnik"
title: "ATU-STI – Access Transfer Update - Session Transfer Identifier"
date: 2025-01-01
abbr: "ATU-STI"
fullName: "Access Transfer Update - Session Transfer Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/atu-sti/"
summary: "ATU-STI je jedinečný identifikátor používaný během procedur kontinuity služeb IMS ke sledování a správě přenosu multimediálních relací mezi různými přístupovými sítěmi. Zajišťuje, že žádosti o přenos"
---

ATU-STI je jedinečný identifikátor používaný ke sledování a správě přenosů multimediálních relací mezi různými přístupovými sítěmi během procedur kontinuity služeb IMS.

## Popis

Access Transfer Update - Session Transfer Identifier (ATU-STI) je klíčová komponenta v architektuře IP Multimedia Subsystem (IMS), která usnadňuje kontinuitu služby během přenosů mezi přístupovými sítěmi. Funguje jako korelační identifikátor, který spojuje různé signalizační zprávy týkající se stejného postupu přenosu relace. Když se User Equipment (UE) přesouvá mezi různými přístupovými technologiemi (například z LTE na Wi-Fi nebo naopak), ATU-STI zajišťuje, že všechny síťové prvky zapojené do přenosu mohou správně identifikovat a zpracovat kontext probíhající relace.

Z architektonického hlediska ATU-STI funguje v rámci frameworku IMS Service Continuity definovaného ve specifikacích 3GPP. Během procedury přenosu přístupu vygeneruje Serving-Call Session Control Function (S-CSCF) nebo Service Centralization and Continuity Application Server (SCC [AS](/mobilnisite/slovnik/as/)) ATU-STI a zahrne jej do žádosti Access Transfer Update. Tento identifikátor je následně propagován signalizační cestou ke všem relevantním síťovým funkcím, včetně Target Access Transfer Control Function ([ATCF](/mobilnisite/slovnik/atcf/)) a Access Transfer Gateway ([ATGW](/mobilnisite/slovnik/atgw/)). ATU-STI umožňuje těmto prvkům korelovat žádost o přenos s konkrétní přesouvanou relací, čímž zajišťuje správné směrování médií a signalizačních cest.

Z pohledu protokolu je ATU-STI přenášen v rámci zpráv SIP jako součást procedur kontinuity služeb IMS. Typicky se objevuje v hlavičkách SIP nebo tělech zpráv během toku Access Transfer Update. Identifikátor dodržuje specifický formát definovaný 3GPP, což zajišťuje interoperabilitu mezi implementacemi různých dodavatelů. Když cílová síť přijme žádost o přenos s ATU-STI, použije tento identifikátor k načtení odpovídajícího kontextu relace a provedení nezbytných úprav k udržení multimediální relace bez přerušení.

ATU-STI hraje klíčovou roli v předcházení selháním a chybným asociacím při přenosu relací. Bez tohoto identifikátoru by mohlo dojít k záměně u více současných přenosů relací, což by vedlo k nesprávnému směrování relací nebo úplnému selhání přenosu. Poskytnutím jedinečného korelačního mechanismu ATU-STI umožňuje spolehlivé předávání služeb založených na IMS, jako je voice over LTE (VoLTE), videohovory a další služby komunikace v reálném čase, napříč heterogenními přístupovými sítěmi. Tato schopnost je zásadní pro poskytování bezproblémového uživatelského zážitku v moderních mobilních sítích, kde zařízení často přepínají mezi buněčnou a Wi-Fi konektivitou.

## K čemu slouží

ATU-STI byl zaveden k řešení výzev spojených s udržováním kontinuity služeb IMS během přenosů mezi přístupovými sítěmi v heterogenních síťových prostředích. Před jeho zavedením měly sítě IMS potíže se spolehlivou korelací žádostí o přenos relace s konkrétními probíhajícími relacemi, když se uživatelé přesouvali mezi různými přístupovými technologiemi. Toto omezení se stalo obzvláště problematickým s rozšířením vícepřístupových zařízení, která mohla současně udržovat připojení k sítím 3GPP (jako LTE) i non-3GPP (jako Wi-Fi).

Primární problém, který ATU-STI řeší, je spolehlivá identifikace a korelace postupů přenosu relace. V dřívějších implementacích bez standardizovaných korelačních mechanismů mohly síťové prvky chybně asociovat žádosti o přenos, což vedlo k ukončení relací, narušení mediálních cest nebo nesprávnému směrování relací. To bylo obzvláště kritické pro služby v reálném čase, jako jsou hlasové a videohovory, kde i krátké přerušení významně zhoršuje uživatelský zážitek. ATU-STI poskytuje standardizovaný způsob, jak jedinečně identifikovat každý postup přenosu, což zajišťuje, že všechny síťové prvky zapojené do procesu předávání mohou správně asociovat signalizační zprávy s příslušným kontextem relace.

Historicky potřeba ATU-STI vznikla s vývojem IMS Service Continuity v 3GPP Release 10, jehož cílem bylo poskytnout bezproblémový zážitek ze služeb napříč různými přístupovými sítěmi. Když operátoři začali nasazovat Voice over LTE (VoLTE) a další služby založené na IMS, potřebovali mechanismy k udržení těchto služeb, když se uživatelé přesouvali mezi buněčnými a Wi-Fi sítěmi. ATU-STI se stal nezbytnou součástí této architektury, umožňující spolehlivé předávání multimediálních relací při zachování parametrů kvality služby a zabezpečení. Jeho vytvoření bylo motivováno posunem průmyslu k plně IP sítím a požadavkem na konzistentní uživatelský zážitek napříč heterogenními přístupovými technologiemi.

## Klíčové vlastnosti

- Jedinečný korelační identifikátor pro postupy přenosu relace
- Umožňuje spolehlivou asociaci mezi žádostmi o přenos a probíhajícími relacemi
- Podporuje předávání mezi přístupovými sítěmi 3GPP a non-3GPP
- Předchází chybnému směrování a selhání přenosu relace
- Standardizovaný formát zajišťující interoperabilitu mezi síťovými prvky
- Základní komponenta architektury IMS Service Continuity

## Definující specifikace

- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures

---

📖 **Anglický originál a plná specifikace:** [ATU-STI na 3GPP Explorer](https://3gpp-explorer.com/glossary/atu-sti/)
