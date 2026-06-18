---
slug: "mort"
url: "/mobilnisite/slovnik/mort/"
type: "slovnik"
title: "MORT – Managed Object Referring to Test"
date: 2025-01-01
abbr: "MORT"
fullName: "Managed Object Referring to Test"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mort/"
summary: "Spravovaný objekt v rámci architektury správy sítí 3GPP, který konkrétně odkazuje na test nebo entitu související s testováním. Jedná se o datovou strukturu používanou k modelování a správě testovacíc"
---

MORT je spravovaný objekt v rámci architektury správy sítí 3GPP, který konkrétně odkazuje na testovací entitu, modelující testovací prostředky a výsledky pro standardizované řízení OAM.

## Popis

Managed Object Referring to Test (MORT) je základní součástí architektury Telecommunications Management Network ([TMN](/mobilnisite/slovnik/tmn/)) a správy sítí ([NM](/mobilnisite/slovnik/nm/)) dle 3GPP, podrobně popsané ve specifikacích řady 32. Jedná se o specifický typ spravovaného objektu ([MO](/mobilnisite/slovnik/mo/)), který slouží jako logická reprezentace testovacího prostředku ve stromu spravovaných informací. Jako MO je definován svými atributy, oznámeními a operacemi, které jsou standardizovány za účelem zajištění interoperability mezi různými síťovými prvky (NEs) a systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)) nebo systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)). MORT poskytuje standardizované rozhraní pro NMS k zahájení, konfiguraci, řízení a získávání výsledků různých testů prováděných v síti, jako jsou kontroly spojení, měření výkonu nebo diagnostika poruch.

Architektonicky se MORTy nacházejí v bázi spravovaných informací ([MIB](/mobilnisite/slovnik/mib/)) spravovaného síťového prvku nebo vyhrazeného testovacího systému. K nim se přistupuje a manipuluje se s nimi prostřednictvím standardizovaných protokolů pro správu, především Common Management Information Service/Protocol ([CMIS](/mobilnisite/slovnik/cmis/)/[CMIP](/mobilnisite/slovnik/cmip/)) nebo jeho nástupců, za použití rozhraní jako je Itf-N. Každá instance MORT je jednoznačně identifikována a obsahuje atributy definující typ testu (např. zpětná smyčka, míra chybovosti), jeho aktuální stav (nečinný, probíhá, dokončen), konfigurační parametry (cílová adresa, testovací vzor, doba trvání) a výsledky (úspěch/neúspěch, naměřené hodnoty, časová razítka). Systém správy může na těchto objektech provádět operace CRUD (vytvořit, přečíst, aktualizovat, smazat) k orchestraci testovacích pracovních postupů.

Jeho role je klíčová pro automatizovanou správu poruch, správu výkonu a zajištění služeb. Díky abstrakci fyzických testovacích postupů do softwarově spravovaných objektů umožňují MORTy operátorům bezproblémově integrovat testování do širších pracovních postupů OAM, jako je automatizovaná analýza hlavní příčiny nebo ověření kvality služby. Například, když je přijat alarm degradace služby, může NMS automaticky vytvořit a aktivovat MORT na podezřelém síťovém prvku za účelem spuštění diagnostického testu, analyzovat výsledky uložené v atributech MORTu a použít tato data k přesné identifikaci poruchy. Tento přístup založený na modelech odděluje logiku správy od implementace testovacího hardwaru nebo softwaru specifické pro daného dodavatele, což podporuje multivendorovou interoperabilitu a zjednodušené provozní postupy.

## K čemu slouží

MORT byl vytvořen, aby řešil problém nestandardizovaných, proprietárních metod pro správu a provádění testů v telekomunikačních sítích. Před jeho standardizací se síťoví operátoři spoléhali na ad-hoc, manuální postupy nebo nástroje specifické pro dodavatele při provádění diagnostiky a testů výkonu. To vedlo k provozní neefektivitě, zvýšené složitosti v prostředí s více dodavateli a neschopnosti automatizovat komplexní testovací pracovní postupy v rámci jednotného systému správy. Rámec TMN si kladl za cíl zavést řád do správy sítí a MORTy byly zavedeny jako konkrétní řešení v rámci funkčních oblastí správy poruch a testování.

Hlavní problém, který MORT řeší, je poskytnutí konzistentního, objektově orientovaného modelu pro reprezentaci jakékoli testovací entity. To umožňuje obecnému NMS zadávat příkazy a přijímat výsledky testů na zařízeních od různých dodavatelů bez nutnosti vlastních integrací pro každý typ testu nebo dodavatele. Formalizuje životní cyklus testu – od vytvoření a konfigurace přes provedení až po získání výsledků – do standardizovaného rozhraní pro správu. Tato schopnost je zásadní pro dosažení cílů TMN v podobě automatizovaných, efektivních a spolehlivých provozních a údržbových (OAM) postupů v síti, což přímo ovlivňuje dostupnost a kvalitu služeb.

## Klíčové vlastnosti

- Standardizovaný objektový model pro reprezentaci testovacích prostředků a konfigurací
- Definované atributy pro typ testu, stav, parametry a výsledky
- Podpora operací správy: Vytvořit, Načíst, Aktualizovat, Smazat a akcí jako Spustit/Zastavit test
- Integrace do širší hierarchické architektury správy TMN (NMS-EMS-NE)
- Umožňuje automatizované vyvolání testu a sběr výsledků jako součást pracovních postupů OAM
- Podporuje multivendorovou interoperabilitu pro síťové testování a diagnostiku

## Související pojmy

- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TS 32.322** (Rel-19) — Test Management IRP Information Service

---

📖 **Anglický originál a plná specifikace:** [MORT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mort/)
