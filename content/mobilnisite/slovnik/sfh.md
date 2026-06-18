---
slug: "sfh"
url: "/mobilnisite/slovnik/sfh/"
type: "slovnik"
title: "SFH – Slow Frequency Hopping"
date: 2025-01-01
abbr: "SFH"
fullName: "Slow Frequency Hopping"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sfh/"
summary: "Technika rozprostřeného spektra, při které se přenosová frekvence uživatelského signálu mění rychlostí nižší než symbolová rychlost. Poskytuje frekvenční diverzitu a průměrování rušení, čímž zlepšuje"
---

SFH je rozprostřené spektrum (spread spectrum) technika, při které se přenosová frekvence uživatele mění pomaleji než symbolová rychlost, čímž poskytuje frekvenční diverzitu a průměrování rušení pro zvýšení odolnosti spoje.

## Popis

Slow Frequency Hopping (SFH) je technika přenosu na fyzické vrstvě definovaná v raných standardech 3GPP, primárně pro GSM (2G) a využívaná v některých módech UMTS (3G). Funguje na principu rozprostřeného spektra s přeskakováním kmitočtů (frequency hopping spread spectrum), kde se nosná frekvence používaná pro daný komunikační kanál nemění, ale je systematicky měněna v čase podle předdefinované přeskakovací sekvence. Přívlastek 'slow' (pomalé) označuje, že ke změně frekvence dochází rychlostí nižší než je rychlost modulačních symbolů; typicky zůstává frekvence konstantní po dobu trvání [TDMA](/mobilnisite/slovnik/tdma/) rámce (nebo více rámců) v GSM, než dojde k přeskoku na další frekvenci v sekvenci. To je v protikladu k Fast Frequency Hopping (FFH), kde se frekvence mění vícekrát za symbol.

Z architektonického hlediska je SFH řízeno Base Station Controllerem ([BSC](/mobilnisite/slovnik/bsc/)) v GSM a Radio Network Controllerem ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS. Tyto síťové elementy přiřazují každému spojení Mobile Allocation ([MA](/mobilnisite/slovnik/ma/)) list – sadu povolených rádiových frekvenčních kanálů – a Hopping Sequence Number ([HSN](/mobilnisite/slovnik/hsn/)). Konkrétní frekvence, která má být použita v daném čase, je určena algoritmem využívajícím MA list, HSN a aktuální číslo rámce. Tento algoritmus zajišťuje, že různí uživatelé ve stejné buňce typicky sledují různé, ortogonální přeskakovací sekvence, aby se minimalizovaly kolize. Fyzický transceiver v základnové stanici i v mobilní stanici musí být schopen rychlého přeladění svého syntetizéru mezi rámci, aby přeskok realizoval.

Jak to funguje, zahrnuje několik klíčových komponent. Za prvé, frekvenční syntetizér musí rychle a přesně přepínat mezi frekvencemi během ochranné periody mezi rámci. Za druhé, přeskakovací sekvence musí být známa jak vysílači, tak přijímači, aby byla zachována synchronizace. Primární přínosy jsou dvojí: frekvenční diverzita a průměrování rušení. Frekvenční diverzita bojuje proti vícecestnému útlumu (multipath fading); protože hluboké útlumy jsou frekvenčně selektivní, přeskok na jinou frekvenci znamená, že signál pravděpodobně nebude na nové frekvenci zažívat hluboký útlum, což vede ke konzistentnější kvalitě signálu. Průměrování rušení snižuje dopad ko-kanálového rušení (od použití stejné frekvence ve vzdálených buňkách) a úzkopásmových rušičů. Protože přenos uživatele přeskakuje přes mnoho frekvencí, vliv silného rušiče na jedné konkrétní frekvenci se v čase vyprůměruje, čímž se zlepší celkový poměr signálu k rušení ([SIR](/mobilnisite/slovnik/sir/)). To umožňuje těsnější vzory opakování frekvencí, což zvyšuje kapacitu sítě. V UMTS mohlo být SFH aplikováno ve spojení s Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)) pro uplink, čímž poskytlo další vrstvu náhodnosti rušení.

## K čemu slouží

Slow Frequency Hopping byl vyvinut pro řešení kritických omezení raných celulárních sítí, zejména GSM, které spoléhaly na pevné přiřazení frekvenčních kanálů a Time Division Multiple Access (TDMA). Hlavními problémy byly frekvenčně selektivní vícecestný útlum (multipath fading) a ko-kanálové rušení. Při statickém přiřazení frekvence by mobilní uživatel zažívající hluboký útlum na své přiřazené frekvenci trpěl trvale špatnou kvalitou hovoru. Podobně by ko-kanálové rušení ze vzdálené buňky používající stejnou frekvenci mohlo trvale degradovat výkon. SFH byl zaveden jako elegantní řešení obou problémů současně.

Historický kontext je zakořeněn v vojenských komunikacích s rozprostřeným spektrem, adaptovaných pro komerční celulární použití. Jeho vznik byl motivován potřebou zlepšit kvalitu a kapacitu sítí GSM bez nutnosti kompletní přestavby infrastruktury. Implementací přeskakování mohli síťoví operátoři dosáhnout 'diverzity rušení', čímž efektivně proměnili systém sužovaný přetrvávajícím rušením na specifických kanálech v systém, kde je rušení rozprostřeno mezi všechny uživatele a stane se zvládnutelnou, zprůměrovanou hladinou šumu. To umožnilo agresivnější faktory opakování frekvencí (např. přechod ze vzoru opakování 12 nebo 9 až na 3 nebo 1 v některých případech), což dramaticky zvýšilo spektrální efektivitu a kapacitu sítě. Také to snížilo potřebu složitých mechanismů řízení výkonu pro boj s útlumem v některých scénářích, protože samotné přeskakování poskytovalo formu časové diverzity. SFH řešil statickou povahu dřívějšího přiřazování kanálů, zavedl dynamiku, která učinila síť robustnější a efektivnější, a stal se jedním ze základních kamenů úspěchu GSM a ovlivnil techniky v pozdějších standardech.

## Klíčové vlastnosti

- Změna frekvence rychlostí nižší než symbolová rychlost (např. na TDMA rámec)
- Poskytuje frekvenční diverzitu pro zmírnění vícecestného útlumu (multipath fading)
- Průměruje ko-kanálové a úzkopásmové rušení napříč sítí
- Umožňuje těsnější opakování frekvencí, čímž zvyšuje kapacitu sítě
- Používá předdefinovaný Mobile Allocation (MA) list a Hopping Sequence Number (HSN)
- Vyžaduje synchronizované frekvenční syntetizéry na vysílači a přijímači

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 51.021** (Rel-19) — RF test methods and conformance requirements for GSM BSS

---

📖 **Anglický originál a plná specifikace:** [SFH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sfh/)
