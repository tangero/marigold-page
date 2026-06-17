---
slug: "mnp-srf"
url: "/mobilnisite/slovnik/mnp-srf/"
type: "slovnik"
title: "MNP-SRF – Mobile Number Portability/Signalling Relay Function"
date: 2025-01-01
abbr: "MNP-SRF"
fullName: "Mobile Number Portability/Signalling Relay Function"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mnp-srf/"
summary: "Síťová funkce umožňující přenositelnost mobilních čísel (MNP) zachycením a přeposíláním signalizačních zpráv. Dotazuje se databází přenositelnosti čísel, aby určila správnou cílovou síť pro hovor nebo"
---

MNP-SRF je síťová funkce, která umožňuje přenositelnost mobilních čísel tím, že zachycuje a přeposílá signalizační zprávy za účelem dotazování databází a určení správné cílové sítě pro směrování hovorů nebo relací.

## Popis

Funkce přenositelnosti mobilních čísel a přenosu signalizace (Mobile Number Portability/Signalling Relay Function – MNP-SRF) je klíčový síťový prvek definovaný v rámci architektury 3GPP pro usnadnění implementace přenositelnosti mobilních čísel ([MNP](/mobilnisite/slovnik/mnp/)). Její primární úlohou je fungovat jako zprostředkovatel nebo přenosový bod ve signalizační cestě, konkrétně pro procedury navázání hovoru a relace. Při volání na přenesené číslo jsou signalizační zprávy vycházející sítě (např. [ISUP](/mobilnisite/slovnik/isup/), SIP) směrovány do MNP-SRF. Tato funkce následně provede dotaz v reálném čase na databázi přenositelnosti čísel ([NPDB](/mobilnisite/slovnik/npdb/)) nebo podobné úložiště, aby zjistila aktuální obsluhující síť pro volané číslo mobilního účastníka ([MSISDN](/mobilnisite/slovnik/msisdn/)). Na základě odpovědi na dotaz, která typicky obsahuje směrovací číslo (např. kód mobilní sítě, [MNC](/mobilnisite/slovnik/mnc/), nebo konkrétní směrovací předponu), MNP-SRF odpovídajícím způsobem upraví signalizační zprávu a přepošle ji ke správné cílové síti. Tento proces je pro koncové uživatele transparentní a zajišťuje správné doručení hovorů bez nutnosti, aby volající znal novou síť účastníka.

Z architektonického hlediska je MNP-SRF často implementována jako součást signalizačních přenosových bodů (STP) nebo vyhrazených aplikačních serverů v jádrové síti, zejména v okruhově komutované ([CS](/mobilnisite/slovnik/cs/)) doméně, nebo ve spolupráci s nimi. Rozhraní k NPDB využívá protokoly jako TCAP nad SS7 nebo Diameter, v závislosti na generaci sítě a implementaci. Funkce musí zvládat vysoké objemy signalizačního provozu s nízkou latencí, aby nedocházelo k prodlužování doby navazování hovorů. Její provoz je definován jako interoperabilní napříč různými síťovými operátory a generacemi, podporujícím jak starší 2G/3G CS hovory, tak i (ve vyspělejších implementacích) relace v IP multimediální podsystému (IMS).

Role MNP-SRF přesahuje rámec prostého dotazování a přeposílání. Je zodpovědná za správu chybových stavů, jako je nedostupnost databáze, a může implementovat mechanismy ukládání do mezipaměti pro zvýšení efektivity u často dotazovaných čísel. V širším ekosystému MNP funguje v součinnosti s dalšími funkcemi, jako je brána přenositelnosti čísel (NPG) a domovský registr polohy ([HLR](/mobilnisite/slovnik/hlr/)) nebo server předplatitelů ([HSS](/mobilnisite/slovnik/hss/)) dárce/příjemce, aby zajistila jednotný zážitek účastníka. Její specifikace napříč vydáními 3GPP zajišťují standardizované chování, což je klíčové pro soulad s regulacemi v regionech, kde je přenositelnost čísel nařízena zákonem.

## K čemu slouží

MNP-SRF byla vytvořena k vyřešení základního problému se směrováním, který přinesla přenositelnost mobilních čísel (MNP). Před zavedením MNP obsahovalo mobilní číslo (MSISDN) vestavěné směrovací informace (jako kód síťového operátora), což umožňovalo přepínačům přímo směrovat hovory do správné domovské sítě. Když regulátoři nařídili, že účastníci si mohou při změně operátora ponechat své číslo, tyto vestavěné směrovací informace se staly zastaralými a zavádějícími, protože číslo mohlo být „přeneseno“ na jinou síť, než pro kterou bylo původně přiděleno. Bez mechanismu pro zjištění aktuální sítě by byly hovory chybně směrovány ke starému (dárčímu) operátorovi, což by vedlo k neúspěšným spojením.

Účelem MNP-SRF je poskytnout centralizovaný, standardizovaný bod pro zachycení a vyřešení tohoto problému v rámci signalizační architektury. Řeší omezení dřívějších nestandardizovaných nebo operátorsky specifických řešení MNP, která mohla vést k problémům s interoperabilitou. Definováním jasné funkční entity ve standardech 3GPP zajišťuje, že všichni výrobci síťových zařízení a operátoři implementují směrování MNP konzistentním a spolehlivým způsobem. To bylo zvláště důležité pro umožnění provozu mezihraničních a vícevýrobcových sítí.

K jejímu vzniku vedly regulatorní požadavky v mnoha zemích, které si vyžádaly technické řešení, které je škálovatelné, efektivní a nezhoršuje kvalitu služeb. MNP-SRF umožňuje operátorům plnit požadavky regulace přenositelnosti při zachování výkonu a spolehlivosti jejich jádrových sítí. Abstrahuje složitost přenositelnosti čísel od ostatních síťových prvků, což umožňuje přepínačům a funkcím řízení relací (CSCF) pracovat na základě tradiční směrovací logiky, zatímco MNP-SRF se stará o výjimky u přenesených čísel.

## Klíčové vlastnosti

- Zachycení a analýza signalizačních zpráv pro navázání hovoru/relace
- Dotazování na databáze přenositelnosti čísel (NPDB) v reálném čase
- Úprava signalizačních zpráv (např. vložení směrovacích čísel)
- Přeposílání signalizace ke správné cílové síti
- Podpora jak protokolů dotazů založených na SS7, tak i na IP (např. Diameter)
- Zpracování chyb a záložní procedury pro výpadky databází

## Související pojmy

- [MNPF – Mobile Number Portability Function](/mobilnisite/slovnik/mnpf/)
- [NPDB – Number Portability Data Base](/mobilnisite/slovnik/npdb/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.632** (Rel-11) — Core Network Resources IRP: Network Resource Model
- **TS 32.732** (Rel-11) — IMS Network Resource Model IRP: Information Service

---

📖 **Anglický originál a plná specifikace:** [MNP-SRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnp-srf/)
