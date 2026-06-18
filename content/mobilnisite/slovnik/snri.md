---
slug: "snri"
url: "/mobilnisite/slovnik/snri/"
type: "slovnik"
title: "SNRI – SCCP Network Resource Identifier"
date: 2025-01-01
abbr: "SNRI"
fullName: "SCCP Network Resource Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/snri/"
summary: "SNRI je jedinečný identifikátor používaný ve vrstvě SCCP (Signalling Connection Control Part) k rozlišení různých síťových prostředků, jako jsou konkrétní aplikace nebo subsystémy. Je klíčový pro sprá"
---

SNRI je jedinečný identifikátor SCCP používaný k rozlišení síťových prostředků pro správné směrování signalizačních zpráv v legacy okruhově přepínaných a raných paketově přepínaných jádrových sítích.

## Popis

[SCCP](/mobilnisite/slovnik/sccp/) Network Resource Identifier (SNRI) je základní komponentou v rámci Signalling Connection Control Part (SCCP), což je síťová vrstva protokolu v architekturách [SS7](/mobilnisite/slovnik/ss7/) (Signalling System No. 7) a SIGTRAN (Signalling Transport). SCCP poskytuje rozšířené funkce směrování a správy nad rámec Message Transfer Part ([MTP](/mobilnisite/slovnik/mtp/)). SNRI slouží jako lokální identifikátor v rámci signalizačního bodu, používaný k rozlišení mezi více uživateli nebo aplikacemi SCCP umístěnými v tomto uzlu. Funguje ve spojení s číslem subsystému (Subsystem Number, [SSN](/mobilnisite/slovnik/ssn/)), což je globálně standardizovaný kód identifikující konkrétního uživatele SCCP (jako [MAP](/mobilnisite/slovnik/map/), [CAP](/mobilnisite/slovnik/cap/) nebo [INAP](/mobilnisite/slovnik/inap/)). Když signalizační bod přijme zprávu SCCP, použije cílový lokální referenční údaj (Destination Local Reference, DLR) a adresu volané strany, která zahrnuje SSN, k identifikaci cílové aplikace. SNRI poskytuje další úroveň granularity, umožňující jednomu SSN (reprezentujícímu typ aplikace) podporovat interně více instancí nebo prostředků. Například jedna ústředna mobilní sítě (Mobile Switching Centre, [MSC](/mobilnisite/slovnik/msc/)) může hostovat více instancí Mobile Application Part (MAP) pro různé provozní účely, přičemž každá je rozlišena jedinečným SNRI.

Z architektonického hlediska je SNRI spravováno lokálně vrstvou SCCP v uzlu. Není globálně směrovatelné jako číslo bodu (Point Code, PC) nebo SSN. Jeho primární role je interní multiplexování a demultiplexování. Při použití spojově orientované služby SCCP je na dobu trvání transakce přiděleno lokální referenční číslo. SNRI může být součástí kontextu, který váže toto lokální reference na konkrétní prostředek uživatelské aplikace. Tento mechanismus je zásadní pro správu více současných signalizačních dialogů, jako jsou například více současných sestavování hovorů nebo aktualizací polohy, a zajišťuje, že zprávy jsou doručeny ke správné zpracovávající entitě v rámci komplexního síťového prvku.

V praktickém provozu je hodnota SNRI významná během fáze navazování spojení a přenosu dat. Umožňuje signalizačnímu bodu udržovat oddělené stavové informace pro každou probíhající transakci spojenou s různými prostředky. To je klíčové pro spolehlivost a škálovatelnost sítě a zabraňuje vzájemnému ovlivňování různých instancí služeb. Zatímco jeho použití je výraznější v tradičních okruhově přepínaných jádrových sítích (CS Core), porozumění SNRI zůstává důležité pro inženýry pracující na údržbě legacy systémů, mezi-síťových funkcích a vývoji směrem k plně IP sítím, kde SIGTRAN přenáší SS7 přes IP.

## K čemu slouží

SNRI bylo vytvořeno, aby řešilo potřebu přesné identifikace a izolace více prostředků nebo instancí aplikací v rámci jediného síťového uzlu používajícího stejný subsystém SCCP. V raných telekomunikačních sítích, kdy síťové prvky jako MSC nebo domácí lokální registry (Home Location Registers, HLR) začaly být složitější, začaly hostovat více instancí stejného aplikačního protokolu (např. více MAP procesů pro zpracování různého regionálního provozu nebo služeb). Pouze globálně jedinečné číslo subsystému (Subsystem Number, SSN) nestačilo k rozlišení mezi těmito interními instancemi. Bez mechanismu jako SNRI by signalizační zprávy určené pro konkrétní prostředek mohly být špatně směrovány nebo zpracovány nesprávnou instancí, což by vedlo k výpadkům služeb, poškození dat nebo neefektivnímu využití prostředků.

Historicky tato potřeba vznikla s expanzí služeb inteligentních sítí a rostoucí hustotou účastníků. Protokol SCCP, definovaný v ITU-T Q.711-Q.714 a přijatý 3GPP, vyžadoval rozšíření svého adresovacího schématu, aby podpořil toto interní multiplexování. SNRI tuto mezeru zaplnilo poskytnutím lokálně významného identifikátoru. Vyřešilo problém škálovatelného hostování aplikací v rámci jediného signalizačního bodu, což umožnilo telekomunikačním operátorům konsolidovat funkce bez ztráty schopnosti spravovat odlišné signalizační asociace. To bylo obzvláště důležité pro dosažení vysoké dostupnosti a distribuce zátěže, kde více paralelních instancí aplikací mohlo sdílet stejné SSN, ale zpracovávat nezávislé transakce.

Motivace byla zakořeněna v principech robustního návrhu signalizačních systémů: spolehlivost, jednoznačné adresování a efektivní využití síťových prostředků. Začleněním SNRI zajistily standardy 3GPP zpětnou kompatibilitu s existujícím směrováním založeným na SSN a zároveň umožnily sofistikovanější architektury uzlů. Představuje klíčový návrhový vzor v telekomunikační signalizaci – oddělení globálního směrování (pomocí PC+SSN) od interní správy prostředků – vzor, který ovlivňuje i pozdější signalizační architektury založené na IP.

## Klíčové vlastnosti

- Lokálně významný identifikátor pro prostředky SCCP v rámci uzlu
- Funguje ve spojení s globálním číslem subsystému (SSN) pro kompletní adresování
- Umožňuje multiplexování více instancí aplikací pod jedním SSN
- Klíčový pro správu spojově orientované služby SCCP
- Používá se interně pro vázání signalizačních referencí na konkrétní prostředky
- Podporuje škálovatelnost a izolaci ve složitých síťových prvcích

## Související pojmy

- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)

## Definující specifikace

- **TR 23.924** (Rel-19) — Feasibility of SNSF for MSC Pool Enhancement

---

📖 **Anglický originál a plná specifikace:** [SNRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/snri/)
