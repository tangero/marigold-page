---
slug: "idnns"
url: "/mobilnisite/slovnik/idnns/"
type: "slovnik"
title: "IDNNS – Intra Domain NAS Node Selector"
date: 2025-01-01
abbr: "IDNNS"
fullName: "Intra Domain NAS Node Selector"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/idnns/"
summary: "Funkční entita v základnové síti, která vybírá vhodný uzel NAS (např. MME, AMF) pro UE v rámci jedné síťové domény. Optimalizuje směrování a vyrovnávání zátěže během procedur počáteční registrace a mo"
---

IDNNS je funkční entita v základnové síti, která vybírá vhodný uzel NAS pro uživatelské zařízení v rámci jedné domény, aby optimalizovala směrování a vyrovnávání zátěže během počáteční registrace a mobility.

## Popis

Intra Domain [NAS](/mobilnisite/slovnik/nas/) Node Selector (IDNNS) je síťová funkce zodpovědná za výběr optimálního uzlu Non-Access Stratum (NAS), jako je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G, pro uživatelské zařízení (UE) v rámci jedné administrativní domény. Funguje během počáteční registrace UE, předávání spojení a dalších událostí mobility, kdy je třeba přiřadit nebo změnit přiřazení uzlu NAS. IDNNS se typicky nachází na strategickém místě v základnové síti, například v rámci Diameter směrovacího agenta nebo specializované funkce pro výběr, a pro své rozhodování používá kritéria jako zátěž uzlu, geografickou polohu, data o účastníkovi a síťové politiky.

Z architektonického hlediska IDNNS interaguje s dalšími síťovými prvky, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), pro získání profilů účastníků, a s existujícími uzly NAS pro sběr informací o zátěži. Když UE zahájí proceduru, přístupová síť předá požadavek IDNNS, který vyhodnotí dostupné uzly NAS na základě nakonfigurovaných algoritmů – jako je round-robin, výběr nejméně zatíženého uzlu nebo výběr založený na topologii – a směruje signalizaci na zvolený uzel. Tím je zajištěno vyvážené rozdělení UE mezi uzly NAS, což předchází přetížení a zlepšuje kontinuitu služeb.

V praxi IDNNS zvyšuje škálovatelnost a odolnost sítě dynamickým řízením přiřazení uzlů NAS. Je obzvláště důležitý v rozsáhlých distribuovaných sítích, kde více uzlů NAS obsluhuje překrývající se oblasti. Optimalizací výběru uzlu IDNNS snižuje latenci signalizace, minimalizuje riziko přetížení uzlů a podporuje efektivní správu mobility. Jeho role je klíčová jak v architekturách 4G Evolved Packet Core (EPC), tak 5G Core (5GC), přičemž se přizpůsobuje specifickým protokolům a rozhraním každé generace.

## K čemu slouží

IDNNS byl zaveden, aby řešil výzvy spojené se škálováním základnových sítí s více uzly [NAS](/mobilnisite/slovnik/nas/), kde neefektivní výběr uzlu mohl vést k nevyvážené zátěži, zvýšené latenci a jediným bodům selhání. V dřívějších vydáních byl výběr uzlu NAS často statický nebo založený na jednoduchém hashování, což nezohledňovalo reálné podmínky, jako je kapacita uzlu nebo topologie sítě.

Hlavním problémem, který IDNNS řeší, je optimalizace distribuce UE mezi uzly NAS za účelem zajištění efektivního využití zdrojů a vysoké dostupnosti. Implementací inteligentních výběrových algoritmů zabraňuje scénářům, kdy jsou některé uzly přetížené, zatímco jiné jsou málo využité, což může degradovat výkon během špičkového provozu nebo událostí mobility. To je obzvláště klíčové pro sítě podporující massive IoT nebo nasazení v hustě osídlených městských oblastech.

Motivován potřebou robustní správy mobility v systémech 3GPP, byl IDNNS specifikován pro zvýšení spolehlivosti sítě a kvality služeb. Umožňuje operátorům nasazovat uzly NAS flexibilním a škálovatelným způsobem a podporuje funkce jako sdílení sítě a geografická redundance. Standardizací této funkce pro výběr zajistila 3GPP interoperabilitu a konzistentní chování napříč implementacemi různých dodavatelů, což usnadňuje vývoj směrem k autonomnějším a samooptymalizujícím se sítím.

## Klíčové vlastnosti

- Dynamický výběr uzlů NAS (např. MME, AMF) na základě kritérií v reálném čase
- Vyrovnávání zátěže mezi více uzly NAS za účelem prevence přetížení
- Podpora výběrových algoritmů, jako je round-robin, výběr nejméně zatíženého uzlu a výběr založený na topologii
- Integrace s databázemi účastníků (HSS/UDM) pro výběr zohledňující politiky
- Zvýšení škálovatelnosti a odolnosti sítě při správě mobility
- Snížení latence signalizace a zlepšení kontinuity služeb

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [5GC – 5G Core Network](/mobilnisite/slovnik/5gc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [IDNNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/idnns/)
