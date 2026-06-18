---
slug: "v-dra"
url: "/mobilnisite/slovnik/v-dra/"
type: "slovnik"
title: "V-DRA – Visited Diameter Routing Agent"
date: 2025-01-01
abbr: "V-DRA"
fullName: "Visited Diameter Routing Agent"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/v-dra/"
summary: "Agent pro směrování protokolu Diameter (DRA) umístěný v navštívené síti. Směruje signalizační zprávy protokolu Diameter mezi síťovými elementy v roamingových scénářích a zajišťuje správné doručování z"
---

V-DRA je agent pro směrování protokolu Diameter (Diameter Routing Agent) nacházející se ve navštívené síti, který směruje signalizační zprávy mezi síťovými elementy, aby zajistil správné doručování zpráv mezi navštívenou a domovskou sítí při roamingu.

## Popis

Visited Diameter Routing Agent (V-DRA) je kritický signalizační uzel v architektuře jádra sítě založené na protokolu Diameter, používaný primárně v 4G (EPS) a raných neautonomních nasazeních 5G. Je nasazen ve Visited Public Land Mobile Network ([VPLMN](/mobilnisite/slovnik/vplmn/)) a funguje jako centralizovaný rozbočovač pro směrování zpráv protokolu Diameter. Primární role V-DRA spočívá v inteligentním směrování signalizačního provozu mezi různými síťovými funkcemi uvnitř navštívené sítě a směrem k domovské síti, zejména pro roamující účastníky. Zkoumá zprávy protokolu Diameter, včetně jejich Application-Id, Destination-Realm a dalších atributů ([AVP](/mobilnisite/slovnik/avp/)), aby určil správného příjemce.

Architektonicky se V-DRA nachází v signalizační cestě mezi elementy, jako jsou Visited Policy and Charging Rules Function ([V-PCRF](/mobilnisite/slovnik/v-pcrf/)), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) ve VPLMN, a jejich protějšky v Home Public Land Mobile Network ([HPLMN](/mobilnisite/slovnik/hplmn/)). Rozhraní s Home [DRA](/mobilnisite/slovnik/dra/) ([H-DRA](/mobilnisite/slovnik/h-dra/)) zajišťuje end-to-end signalizační konektivitu. V-DRA funguje tak, že udržuje vazbu nebo stav relace, který koreluje různé relace protokolu Diameter (např. rozhraní Gx, Rx, S6a, S6d) pro stejného účastníka, což umožňuje koherentní řízení politik a účtování. Toto stavové směrování je klíčové pro kontinuitu relace a konzistentní vynucování politik.

Princip činnosti zahrnuje přijetí požadavku protokolu Diameter od síťového elementu, aplikaci směrovacích pravidel na základě identity účastníka (např. IMSI) a požadované služby a následné přeposlání zprávy na příslušný cíl, kterým může být lokální funkce nebo H-DRA pro další směrování do domovské sítě. V-DRA také poskytuje funkce jako vyrovnávání zátěže mezi více instancemi síťové funkce, redundanci a skrytí topologie, které chrání vnitřní strukturu sítě VPLMN před domovskou sítí. Jeho nasazení je v mnoha roamingových architekturách povinné, aby byla zajištěna škálovatelná a řiditelná signalizace protokolem Diameter.

## K čemu slouží

V-DRA byl zaveden, aby vyřešil problémy se škálovatelností a složitostí přímé signalizace protokolem Diameter v prostředích s více dodavateli a více operátory, zejména při roamingu. Před zavedením DRA musely být síťové funkce staticky konfigurovány s adresami všech možných partnerských uzlů, což vedlo k problému plně propojené sítě (full-mesh), který byl obtížně řiditelný a škálovatelný. To se stalo neudržitelným s růstem LTE a nárůstem roamingových dohod.

Jeho vytvoření ve specifikaci 3GPP Release 8 bylo motivováno potřebou standardizované, centralizované směrovací entity, která by oddělila síťové funkce od sebe navzájem. V-DRA konkrétně řeší roamingový scénář tím, že zajišťuje správné směrování signalizace z navštívené sítě do správné domény domovské sítě. Umožňuje efektivní propojení mezi operátory, podporuje distribuci zátěže a poskytuje bod pro implementaci bezpečnostních a správních politik na signalizačních rovinách. V-DRA je základním prvkem architektury Policy and Charging Control (PCC) při roamingu, zajišťuje, že politiky účastníka jsou správně načteny a aplikovány, i když se uživatel nachází mimo svou domovskou síť.

## Klíčové vlastnosti

- Stavové směrování zpráv protokolu Diameter v navštívené síti
- Podpora klíčových rozhraní protokolu Diameter: Gx, Rx, S6a, S6d, S9 pro roaming
- Poskytuje skrytí topologie pro VPLMN
- Umožňuje vyrovnávání zátěže mezi více instancemi síťových funkcí
- Udržuje vazbu relací pro koherentní řízení politik a účtování
- Nezbytný pro signalizační konektivitu mezi operátory (roaming)

## Související pojmy

- [H-DRA – Home Diameter Routing Agent](/mobilnisite/slovnik/h-dra/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping

---

📖 **Anglický originál a plná specifikace:** [V-DRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/v-dra/)
