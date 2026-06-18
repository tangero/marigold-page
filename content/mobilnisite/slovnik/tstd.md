---
slug: "tstd"
url: "/mobilnisite/slovnik/tstd/"
type: "slovnik"
title: "TSTD – Time Switched Transmit Diversity"
date: 2025-01-01
abbr: "TSTD"
fullName: "Time Switched Transmit Diversity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tstd/"
summary: "Technika přenosové diverzity používaná v UMTS/WCDMA, kdy v jednom okamžiku vysílá pouze jedna anténa a dochází k přepínání mezi anténami v různých časových slotech. Zvyšuje odolnost signálu ve směrové"
---

TSTD je technika přenosové diverzity v UMTS/WCDMA, která přepíná vysílání mezi anténami v různých časových slotech za účelem zvýšení odolnosti směrového spoje vůči útlumu prostřednictvím prostorové diverzity.

## Popis

Time Switched Transmit Diversity (TSTD) je forma přenosové diverzity s otevřenou smyčkou specifikovaná pro směrový spoj (downlink) systému Universal Mobile Telecommunications System (UMTS) Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) ([WCDMA](/mobilnisite/slovnik/wcdma/)). Funguje tak, že vysílá stejný signál z různých fyzických antén na straně uživatelského zařízení (UE) ve střídajících se časových intervalech. Konkrétně v kontextu směrového spoje UMTS se TSTD aplikuje na synchronizační kanál ([SCH](/mobilnisite/slovnik/sch/)). Synchronizační kanál se skládá ze dvou subkanálů: primárního synchronizačního kanálu (P-SCH) a sekundárního synchronizačního kanálu (S-SCH). Při aktivované TSTD vysílá Node B (základnová stanice) P-SCH z jedné antény v sudých časových slotech a z druhé antény v lichých časových slotech. S-SCH je vysílán v komplementárním vzoru, což zajišťuje, že v každém daném okamžiku jsou oba subkanály vysílány z různých antén.

Základní mechanismus spočívá v časovém přepínání pro využití prostorové diverzity. Střídáním zdroje vysílání prochází signál různými šířicími cestami a podmínkami útlumu. Na straně přijímače (UE) to znamená, že pokud je signál z jedné antény v určitém časovém slotu silně utlumen, existuje vyšší pravděpodobnost, že signál z druhé antény v následujícím slotu bude silnější. UE nepotřebuje explicitně znát přepínací vzor pro P-SCH, protože je inherentně navržena k vyhledávání primárního synchronizačního kódu. Pro S-SCH je vzor známý a napomáhá rámcové synchronizaci a identifikaci skupiny buněk. Přijímač v UE kombinuje signály přijaté v čase, čímž účinně zmírňuje dopad rychlého útlumu a zvyšuje pravděpodobnost úspěšné synchronizace a odhadu kanálu.

Klíčové komponenty zapojené do implementace TSTD zahrnují vícevysílací antény Node B, základnovou procesorovou jednotku, která řídí přepínací logiku podle časování slotů, a samotnou strukturu kanálu SCH. Přepínání je synchronizováno s 10ms rádiovým rámcem a strukturou časových slotů 0,667 ms v UMTS. TSTD je klasifikována jako technika s otevřenou smyčkou, protože nevyžaduje zpětnou vazbu od UE týkající se informací o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)). To zjednodušuje její implementaci a zajišťuje robustnost ve scénářích s vysokou mobilitou, kde může být zpětná vazba zastaralá. Její zisk je však obecně nižší ve srovnání s metodami přenosové diverzity s uzavřenou smyčkou, jako je Closed-Loop Mode 1 (CLM1), které využívají zpětnou vazbu od UE k váhování vysílání z více antén současně.

V celkové architektuře UMTS/[UTRAN](/mobilnisite/slovnik/utran/) hraje TSTD specifickou roli při zlepšování společných kanálů směrového spoje, zejména během počátečního vyhledávání buňky a synchronizace. Zlepšuje oblast pokrytí buňky tím, že činí synchronizační signály odolnějšími vůči útlumu, což je klíčové pro spolehlivý přístup k systému, přechod mezi buňkami a mobilitu. Ačkoli je její použití omezeno na specifické kanály a jde o relativně jednoduchou formu diverzity, TSTD byla důležitou ranou technikou pro zlepšení výkonu směrového spoje bez zvýšení složitosti UE, protože kombinování diverzity je inherentně prováděno v časové doméně algoritmy přijímače UE.

## K čemu slouží

TSTD byla vyvinuta k řešení problému útlumu signálu v mobilním rádiovém prostředí, konkrétně pro kritické synchronizační signály v UMTS. V raných celulárních systémech mohl být výkon směrového spoje vážně degradován vícecestným útlumem, kdy se signály odražené od objektů dostávají k přijímači v různých časech a způsobují konstruktivní a destruktivní interference. To bylo obzvláště problematické pro společné kanály, jako je [SCH](/mobilnisite/slovnik/sch/), které musí být spolehlivě detekovány všemi UE v buňce pro počáteční přístup a převýběr buňky. Bez diverzity mohl hluboký útlum zabránit UE v synchronizaci se sítí, což vedlo k přerušeným hovorům nebo neúspěšným pokusům o přístup, zejména na okrajích buněk.

Motivace pro TSTD vycházela z potřeby jednoduchého, účinného schématu přenosové diverzity, které mohlo být standardizováno pro UMTS již od jeho první verze ([R99](/mobilnisite/slovnik/r99/)). Řešila problém, jak poskytnout výhody prostorové diverzity na straně základnové stanice bez nutnosti složitých zpětnovazebních mechanismů nebo významných změn v konstrukci UE. Před UMTS se diverzitní techniky často zaměřovaly na diverzitu přijímače (více antén na mobilním zařízení), což zvyšovalo náklady a velikost UE. TSTD přesunula složitost na stranu sítě (Node B) a využívala více antén základnové stanice – zdroj, který operátoři stejně stále více nasazovali z důvodů kapacity a pokrytí.

Historicky byla TSTD součástí souboru metod přenosové diverzity zavedených v 3GPP ke zlepšení kapacity a pokrytí směrového spoje. Představovala pragmatický kompromis mezi výkonnostním ziskem a implementační složitostí. Zatímco pokročilejší techniky, jako je Space-Time Transmit Diversity ([STTD](/mobilnisite/slovnik/sttd/)) a režimy s uzavřenou smyčkou, nabízely vyšší zisky, vyžadovaly sofistikovanější zpracování signálu nebo zpětnovazební kanály. TSTD poskytla základní zlepšení pro synchronizační kanály a zajistila robustní provoz systému pro všechna UE. Její přetrvávající přítomnost v pozdějších verzích 3GPP, i když High-Speed Packet Access (HSPA) a LTE zaváděly pokročilejší MIMO schémata, podtrhuje její základní roli při zajišťování spolehlivých procedur fyzické vrstvy pro vyhledávání a zachycení buňky ve systémech založených na WCDMA.

## Klíčové vlastnosti

- Přenosová diverzita s otevřenou smyčkou pro synchronizační kanály směrového spoje UMTS
- Přepíná vysílání mezi dvěma anténami na bázi časového slotu
- Aplikována konkrétně na primární a sekundární synchronizační kanály (P-SCH & S-SCH)
- Zvyšuje odolnost vůči rychlému útlumu a zlepšuje pokrytí buňky
- Nevyžaduje zpětnou vazbu o stavu kanálu od UE
- Zjednodušuje konstrukci přijímače UE pro synchronizaci

## Související pojmy

- [STTD – Space Time Transmit Diversity](/mobilnisite/slovnik/sttd/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [TSTD na 3GPP Explorer](https://3gpp-explorer.com/glossary/tstd/)
