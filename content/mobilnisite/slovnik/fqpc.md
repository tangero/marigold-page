---
slug: "fqpc"
url: "/mobilnisite/slovnik/fqpc/"
type: "slovnik"
title: "FQPC – Fully Qualified Partial CDR"
date: 2025-01-01
abbr: "FQPC"
fullName: "Fully Qualified Partial CDR"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fqpc/"
summary: "Specifický typ záznamu o účtování (Charging Data Record - CDR) používaný v offline účtovacích systémech 3GPP. Představuje úplný, samostatný segment účtovacích informací pro sezení služby, obsahující v"
---

FQPC je úplný a samostatný segment záznamu o účtování (Charging Data Record) používaný v offline účtování 3GPP, který obsahuje všechna potřebná pole pro zpracování účtování, i když sezení služby zahrnuje více dílčích záznamů.

## Popis

Fully Qualified Partial [CDR](/mobilnisite/slovnik/cdr/) (FQPC) je základní datová struktura v architektuře offline účtování 3GPP, definovaná v rámci rodiny záznamů o účtování (Charging Data Record - CDR). Offline účtování, známé také jako účtování ex post, generuje CDR pro pozdější zpracování fakturačním systémem. Sezení služby (např. hovor, datové sezení, [SMS](/mobilnisite/slovnik/sms/)) může vygenerovat jeden nebo více CDR. FQPC je specifický typ dílčího CDR, který má klíčovou vlastnost: je 'plně kvalifikovaný' (fully qualified), což znamená, že obsahuje všechna povinná a podmíněná informační pole vyžadovaná fakturačním systémem k jeho samostatnému zpracování, bez nutnosti odkazovat se na jiné dílčí záznamy ze stejného sezení nebo je s nimi slučovat.

Generování FQPC se řídí triggery uvnitř funkce spouštějící účtování (Charging Trigger Function - [CTF](/mobilnisite/slovnik/ctf/)) v síti. Tyto triggery mohou být založené na událostech (např. konec hovoru, změna tarifního času) nebo na objemu/době trvání (např. každých 10 MB přenesených dat, každých 5 minut hovoru). Když je trigger aktivován, CTF v síťovém elementu (jako [SGSN](/mobilnisite/slovnik/sgsn/), GGSN nebo [CSCF](/mobilnisite/slovnik/cscf/)) shromáždí všechny relevantní účtovací informace až do tohoto bodu, naformátuje je podle přísných specifikací v TS 32.298 a vytvoří FQPC. Tento záznam je pak přenesen přes referenční body Rf nebo Ga k funkci pro shromažďování účtovacích dat (Charging Data Function - [CDF](/mobilnisite/slovnik/cdf/)), která jej finalizuje do uzavřeného CDR pro fakturační doménu.

'Plně kvalifikovaná' povaha má architektonický význam. Zajišťuje spolehlivost a robustnost účtování. Pokud dojde k selhání sítě po odeslání FQPC, ale před ukončením sezení, fakturační systém může stále správně účtovat za část služby zachycenou v tomto FQPC. Jiné typy dílčích CDR, jako například neplně kvalifikované dílčí CDR, mohou postrádat určitá pole (např. celkovou dobu trvání sezení nebo objem) a vyžadují sloučení s následným finálním CDR. FQPC tuto závislost odstraňuje, čímž zjednodušuje následnou logiku mediace a zpracování pro účtování. Jeho struktura zahrnuje komplexní sadu polí: pořadové číslo záznamu, identitu obsluhující sítě, identifikátory účastníka ([IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)), podrobnosti služby, množství využití (doba trvání, objem dat), časová razítka a účtovací identifikátory, které spojují všechny dílčí záznamy z jednoho sezení.

## K čemu slouží

FQPC byl vyvinut k řešení kritických problémů škálovatelnosti, spolehlivosti a přesnosti offline účtování v se vyvíjejících sítích 3GPP. Rané účtovací systémy často generovaly jediný, monolitický CDR na konci potenciálně dlouhého sezení (jako například několikahodinové datové připojení). Tento přístup riskoval ztrátu všech účtovacích dat, pokud sezení skončilo abnormálně nebo pokud síťový element selhal před uzavřením a přeposláním záznamu. Také vytvářel velkou paměťovou zátěž na síťových elementech, které musely uchovávat otevřené záznamy po dlouhá časová období.

Zavedení dílčích CDR a konkrétně FQPC řešilo tato omezení tím, že umožnilo přírůstkové, periodické hlášení účtovacích událostí. Atribut 'plně kvalifikovaný' byl klíčovou inovací pro uspokojení potřeby fakturačního systému po úplných, zpracovatelných datech. Umožňuje operátorovi realizovat příjmy přírůstkově a spolehlivě, dokonce i pro probíhající sezení. To bylo motivováno zejména růstem paketových datových služeb v GPRS a UMTS, kde sezení mohla být velmi dlouhodobá a hodnota přenesených dat v jakémkoli daném bodě byla významná. Mechanismus FQPC zajistil, že tato hodnota může být zachycena a účtována bez čekání na konec sezení, čímž se zlepšil cash flow a finanční řízení rizik pro operátory.

## Klíčové vlastnosti

- Samostatný účtovací záznam se všemi povinnými poli pro nezávislé zpracování účtování
- Generován na základě konfigurovatelných triggerů (čas, objem, událost)
- Zabraňuje ztrátě příjmů tím, že periodicky zachycuje zpoplatnitelné události během sezení
- Obsahuje spojovací identifikátory pro asociaci všech dílčích CDR z jednoho sezení služby
- Přenášen z CTF do CDF přes standardizovaná rozhraní Rf/Ga
- Definován podrobnými specifikacemi polí v 3GPP TS 32.298

## Definující specifikace

- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.277** (Rel-19) — Charging Management for Proximity Services (ProSe)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [FQPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fqpc/)
