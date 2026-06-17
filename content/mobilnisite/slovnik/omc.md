---
slug: "omc"
url: "/mobilnisite/slovnik/omc/"
type: "slovnik"
title: "OMC – Operations and Maintenance Centre"
date: 2025-01-01
abbr: "OMC"
fullName: "Operations and Maintenance Centre"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/omc/"
summary: "Operations and Maintenance Centre (OMC, česky operační a údržbové centrum) je centralizovaný systém pro správu sítě zodpovědný za provoz, administraci a údržbu síťových prvků, primárně v sítích GSM a"
---

OMC je centralizovaný systém pro správu sítě zodpovědný za provoz, administraci a údržbu síťových prvků, který poskytuje funkce správy FCAPS.

## Popis

Operations and Maintenance Centre (OMC, česky operační a údržbové centrum) je základní součást architektury správy sítě v systémech 2G (GSM) a raných 3G (UMTS) podle definice 3GPP. Slouží jako centralizovaná správní entita pro konkrétní doménu, jako je rádiová přístupová síť (OMC-R) nebo jádro sítě (OMC-S). OMC komunikuje přímo se síťovými prvky ([NE](/mobilnisite/slovnik/ne/)), jako jsou Base Station Controllers ([BSC](/mobilnisite/slovnik/bsc/)), Mobile Switching Centres ([MSC](/mobilnisite/slovnik/msc/)) a Home Location Registers ([HLR](/mobilnisite/slovnik/hlr/)), prostřednictvím standardizovaných rozhraní, často s využitím protokolů jako [CMISE](/mobilnisite/slovnik/cmise/) (Common Management Information Service Element) přes rozhraní Q3. Jejím hlavním úkolem je implementace modelu správy FCAPS (Fault, Configuration, Accounting, Performance, Security).

Architektonicky se OMC skládá ze systému správy, který zahrnuje databázi, uživatelská rozhraní pro operátory a mediační funkce pro komunikaci s NE. Shromažďuje alarmy a měření výkonu ze spravovaných prvků, tato data zpracovává a prezentuje je síťovým operátorům prostřednictvím grafických uživatelských rozhraní. Pro správu konfigurace umožňuje OMC operátorům zřizovat nové služby, aktualizovat software na síťových prvcích a upravovat síťové parametry. Správa výkonu zahrnuje sběr statistik o provozu a kvalitě, které jsou klíčové pro plánování kapacity a optimalizaci.

V širším rámci správy 3GPP představuje OMC systém správy druhé úrovně, který je často řízen vyšší úrovní, jako je Network Management Centre ([NMC](/mobilnisite/slovnik/nmc/)) nebo Operations Support System ([OSS](/mobilnisite/slovnik/oss/)). Jeho zavedení standardizovalo provozní postupy pro telekomunikační sítě a odklonilo se od proprietárních systémů správy prvků. Zatímco termín OMC je silně spojen se sítěmi 2G/3G, jeho funkční principy se vyvinuly do vrstev Element Management ([EM](/mobilnisite/slovnik/em/)) a Network Management (NM) v pozdějších architekturách správy 3GPP, jako je model Telecom Management Network (TMN) a následné rámce.

## K čemu slouží

OMC bylo vytvořeno, aby řešilo kritickou potřebu standardizované, centralizované a efektivní provozní kontroly rychle se rozšiřujících a stále složitějších celulárních sítí, zejména s globálním nasazením GSM. Před jeho standardizací byla správa sítě často řešena proprietárními systémy od každého dodavatele zařízení, což vedlo k vysokým provozním nákladům, složitosti v prostředí s více dodavateli a absenci jednotných postupů pro správu poruch a výkonu.

Jeho zavedení vyřešilo problém fragmentované správy tím, že poskytlo společný rámec pro pět klíčových oblastí FCAPS. To umožnilo síťovým operátorům monitorovat stav sítě z jednoho místa, rychle diagnostikovat a izolovat poruchy, konfigurovat síťové prvky konzistentním způsobem a sbírat standardizovaná data o výkonu pro optimalizaci a plánování sítě. OMC se stalo základním kamenem pro dosažení vysoké dostupnosti sítě a kvality služeb, které jsou nezbytné pro komerční mobilní provoz.

Historicky byl koncept OMC významným krokem v profesionalizaci provozu telekomunikačních sítí, který umožnil rozsah a spolehlivost potřebnou pro mobilní služby masového trhu. Položil základy pro všechny následné architektury správy 3GPP a stanovil principy, které byly později zdokonaleny v kontextu správy sítí UMTS, LTE a 5G, i když pod jinými názvy, jako je Element Manager (EM) a Network Manager (NM).

## Klíčové vlastnosti

- Centralizovaná správa FCAPS (Fault, Configuration, Accounting, Performance, Security) pro síťové prvky
- Standardizované rozhraní Q3 pro komunikaci se spravovanými síťovými prvky (NE)
- Podpora správy domény rádiové přístupové sítě (OMC-R) i jádra sítě (OMC-S)
- Sběr, filtrace, korelace a prezentace alarmů síťovým operátorům
- Správa softwaru a konfigurace pro dálkové zřizování a aktualizace
- Sběr a reportování dat Performance Measurement (PM) pro optimalizaci sítě

## Související pojmy

- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [NMC – Network Management Centre](/mobilnisite/slovnik/nmc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 52.021** (Rel-19) — GSM A-bis Interface Network Management
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [OMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/omc/)
