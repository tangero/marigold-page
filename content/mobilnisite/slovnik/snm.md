---
slug: "snm"
url: "/mobilnisite/slovnik/snm/"
type: "slovnik"
title: "SNM – Sub-Network Manager"
date: 2025-01-01
abbr: "SNM"
fullName: "Sub-Network Manager"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/snm/"
summary: "Sub-Network Manager (SNM) je entita systému správy sítě (NMS) zodpovědná za správu specifické podmnožiny nebo domény telekomunikační sítě, jako je RAN nebo segment specifický pro dodavatele. Pro svou"
---

SNM (Správce podsítě) je entita systému správy sítě zodpovědná za správu specifické podmnožiny telekomunikační sítě, která pro tuto doménu zajišťuje správu chyb, konfigurace, výkonu a zabezpečení.

## Popis

Sub-Network Manager (SNM) je funkční entita v rámci architektury 3GPP Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)) a později architektury Management System ([MS](/mobilnisite/slovnik/ms/)). Operuje na vrstvě správy prvků ([EML](/mobilnisite/slovnik/eml/)) nebo potenciálně na vrstvě správy sítě ([NML](/mobilnisite/slovnik/nml/)) v závislosti na hierarchickém modelu. SNM má definovaný rozsah správy, kterým je podsíť – soubor síťových prvků ([NE](/mobilnisite/slovnik/ne/)) seskupených podle geografie, technologie, dodavatele nebo administrativní domény. Příklady zahrnují SNM spravující všechny Node B v regionu, všechny [eNB](/mobilnisite/slovnik/enb/) od konkrétního dodavatele nebo všechny prvky jádra sítě pro doménu paketového přenosu.

SNM provádí plné funkce správy FCAPS (Chyby, Konfigurace, Účtování, Výkon, Zabezpečení) pro síťové prvky ve své doméně. Shromažďuje alarmy a měření výkonu z NE prostřednictvím jižních rozhraní (např. pomocí protokolů jako [SNMP](/mobilnisite/slovnik/snmp/) nebo [CORBA](/mobilnisite/slovnik/corba/)). Může provádět aktualizace konfigurace, stahování softwaru a izolaci a nápravu chyb. SNM často poskytuje specifické rozhraní pro správu od dodavatele nebo pro danou technologii, čímž abstrahuje heterogenitu podkladových NE. Poté prezentuje konsolidovaný, agregovaný pohled na svou doménu severním systémům, jako je Domain Manager (DM) nebo Network Manager (NM), prostřednictvím standardizovaných rozhraní (např. rozhraní Itf-N).

Klíčové součásti SNM zahrnují bázi řídicích informací (MIB) obsahující spravované objekty pro jeho doménu, mediační funkce pro překlad mezi protokoly a informačními modely specifickými pro NE a grafické uživatelské rozhraní (GUI) pro operátory. Jeho role je klíčová pro škálovatelnou správu sítě; namísto jediného monolitického správce obsluhujícího tisíce různorodých NE je síť rozdělena na domény, z nichž každá má vyhrazený SNM. To umožňuje distribuované zpracování, omezení dopadu chyb a specializované znalosti správy pro různé síťové technologie.

## K čemu slouží

Koncept SNM byl vytvořen, aby řešil výzvy škálovatelnosti a složitosti správy velkých, více-dodavatelských a více-technologických telekomunikačních sítí. Rané přístupy ke správě sítě často zahrnovaly proprietární správce prvků, kteří nemohli komunikovat s nadřazenými, vícedoménovými systémy, což vedlo k provozním izolovaným celkům. Problémem byl nedostatek standardizované, hierarchické architektury správy.

Architektura správy 3GPP, definovaná ve specifikacích jako TS 32.102 (Telecom management: Principles and high level requirements) a TS 32.150 (Management and orchestration architecture), zavedla SNM k rozkladu problému správy. Jejím účelem je poskytovat lokalizovanou, efektivní správu pro logickou podmnožinu sítě. Tím se řeší problém zahlcení centrálního správce daty ze všech prvků a umožňuje se optimalizace specifické pro dodavatele na úrovni podsítě. Historicky se vyvinul z konceptu EML v TMN a poskytuje klíčovou vrstvu abstrakce a mediace mezi heterogenními síťovými prvky a jednotnými systémy správy sítě orientovanými na služby.

## Klíčové vlastnosti

- Spravuje definovanou doménu podsítě (např. RAN specifický pro dodavatele)
- Provádí funkce FCAPS pro síťové prvky ve svém rozsahu
- Zajišťuje mediaci mezi rozhraními specifickými pro NE a standardizovanými severními rozhraními (např. Itf-N)
- Agreguje a koreluje alarmy a data o výkonu z více NE
- Umožňuje škálovatelnou a distribuovanou architekturu správy sítě
- Často poskytuje aplikaci pro správu specifickou pro technologii nebo dodavatele

## Definující specifikace

- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.150** (Rel-19) — IRP Concept and Definitions

---

📖 **Anglický originál a plná specifikace:** [SNM na 3GPP Explorer](https://3gpp-explorer.com/glossary/snm/)
