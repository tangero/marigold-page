---
slug: "bat"
url: "/mobilnisite/slovnik/bat/"
type: "slovnik"
title: "BAT – Bearer Association Transport"
date: 2025-01-01
abbr: "BAT"
fullName: "Bearer Association Transport"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bat/"
summary: "BAT je protokolový mechanismus, který v sítích 3GPP umožňuje asociaci více IP toků nebo přenosových kanálů (bearerů) ke konkrétním přenosovým prostředkům. Zajišťuje správné mapování mezi toky služební"
---

BAT je protokolový mechanismus 3GPP, který asociuje více IP toků ke konkrétním přenosovým prostředkům, čímž zajišťuje správné mapování mezi toky služebních dat a přenosovými přenosovými kanály (bearery) za účelem optimalizace využití a podpory QoS.

## Popis

Bearer Association Transport (BAT) je základní protokolový mechanismus v architekturách 3GPP, který vytváří a spravuje asociace mezi přenosovými kanály (bearery) na úrovni služby a prostředky přenosové sítě. V sítích 3GPP představují přenosové kanály (bearery) logické komunikační kanály se specifickými charakteristikami kvality služby (QoS), zatímco přenosové prostředky odkazují na fyzická nebo virtuální spojení, která přenášejí skutečný datový provoz. BAT funguje na rozhraní mezi vrstvou služby a přenosovou vrstvou a zajišťuje, že toky služebních dat jsou správně namapovány na odpovídající přenosové kanály (bearery) se shodnými požadavky na QoS.

Architektura BAT zahrnuje několik klíčových komponent včetně funkce pravidel pro politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/)), funkce vynucování politik a účtování ([PCEF](/mobilnisite/slovnik/pcef/)), funkce vázání přenosových kanálů a hlášení událostí ([BBERF](/mobilnisite/slovnik/bberf/)) a různých prvků přenosové sítě. Když dorazí požadavek na službu, PCRF určí odpovídající QoS politiky a sdělí je PCEF nebo BBERF. Tyto vynucovací funkce pak použijí mechanismy BAT k navázání (vázání) toku služebních dat na konkrétní přenosový kanál (bearer), který dokáže splnit požadované parametry QoS. Tento proces vázání zohledňuje faktory jako požadavky na šířku pásma, omezení latence, toleranci ztráty paketů a charakteristiky účtování.

BAT funguje prostřednictvím série signalizačních procedur, které vytvářejí, modifikují a uvolňují asociace přenosových kanálů. Proces začíná detekcí nového toku služebních dat, typicky spuštěnou aplikačními požadavky nebo síťovými politikami. Vynucovací funkce poté vyhodnotí dostupné přenosové prostředky a vybere vhodný přenosový kanál (bearer) na základě požadavků QoS. Pokud žádný vhodný kanál neexistuje, mechanismy BAT mohou spustit vytvoření nového vyhrazeného přenosového kanálu (dedicated bearer). Během relace BAT průběžně monitoruje asociaci a může dynamicky upravit vázání v reakci na měnící se síťové podmínky, mobilitu uživatele nebo aktualizace politik.

Fungování protokolu je specifikováno v několika technických specifikacích 3GPP s podrobnými postupy pro různé síťové scénáře, včetně prostředí konvergence pevných a mobilních sítí, vícepřístupových edge výpočtů ([MEC](/mobilnisite/slovnik/mec/)) a síťového řezání (network slicing). BAT podporuje přenosové protokoly založené na [GTP](/mobilnisite/slovnik/gtp/) i [PMIP](/mobilnisite/slovnik/pmip/), což poskytuje flexibilitu v scénářích nasazení. Mezi klíčové aspekty patří rozhodování o vázání přenosových kanálů, hlášení událostí pro řízení politik a interakce s účtovacími systémy za účelem zajištění správné korelace mezi využitím služby a spotřebou přenosových prostředků. Mechanismus také řeší chybové stavy a procedury obnovy pro zachování kontinuity služby během síťových přechodů nebo výpadků.

## K čemu slouží

BAT byl vytvořen, aby řešil základní výzvu efektivního mapování požadavků na QoS na úrovni služby na podkladové prostředky přenosové sítě v architekturách 3GPP. Před jeho zavedením se sítě potýkaly s neefektivním využitím prostředků, kdy více služeb se shodnými požadavky na QoS vytvářelo samostatné přenosové kanály (bearery), což vedlo k nadbytečné režii a suboptimálnímu výkonu sítě. Nedostatek standardizovaných mechanismů pro asociaci přenosových kanálů také ztěžoval implementaci konzistentních QoS politik napříč různými síťovými doménami a mezi sítěmi různých operátorů.

Tato technologie řeší několik kritických problémů v mobilních sítích. Za prvé umožňuje optimální využití prostředků tím, že umožňuje více tokům služebních dat se shodnými charakteristikami QoS sdílet stejný přenosový kanál (bearer), čímž snižuje signalizační režii a zlepšuje efektivitu sítě. Za druhé poskytuje standardizovaný mechanismus pro vynucování QoS na celé datové cestě, což zajišťuje konzistentní kvalitu služby od uživatelského zařízení přes rádiovou přístupovou síť a jádro sítě až k externím paketovým datovým sítím. Za třetí BAT podporuje přesné účtování tím, že udržuje správnou korelaci mezi využitím služby a spotřebou přenosových prostředků, což umožňuje sofistikované účtovací modely založené na úrovních QoS a využití síťových prostředků.

Historicky motivace pro BAT vznikla s evolucí směrem k plně IP sítím ve verzi 3GPP Release 8 a zavedením Evolved Packet System (EPS). Jak se sítě přesouvaly z přepojování okruhů na architektury s přepojováním paketů, vznikla potřeba sofistikovanějších mechanismů pro správu vztahu mezi službami a přenosovými prostředky. BAT poskytl potřebný rámec pro podporu pokročilých služeb, jako je VoIP, streamování videa a podnikové aplikace, které vyžadují garantovanou QoS při zachování efektivního provozu sítě. Protokol se vyvíjel, aby řešil nově vznikající požadavky včetně síťového řezání (network slicing), edge výpočtů a architektur založených na službách v 5G.

## Klíčové vlastnosti

- Dynamické vázání přenosových kanálů (bearerů) na základě požadavků QoS
- Podpora více přenosových protokolů včetně GTP a PMIP
- Integrace s funkcemi řízení politik a účtování
- Hlášení událostí pro rozhodování o politikách
- Podpora asociací pro vyhrazené (dedicated) a výchozí (default) přenosové kanály
- Správa přenosových kanálů s ohledem na mobilitu během předávání hovoru (handover)

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)
- [PCEF – Policy and Charging Enforcement Function](/mobilnisite/slovnik/pcef/)

## Definující specifikace

- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.205** (Rel-19) — BICC Protocols for Bearer-Independent CS Core Network
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.565** (Rel-19) — Time Synchronization Function Services

---

📖 **Anglický originál a plná specifikace:** [BAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/bat/)
