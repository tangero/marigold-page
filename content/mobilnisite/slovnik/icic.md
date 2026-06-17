---
slug: "icic"
url: "/mobilnisite/slovnik/icic/"
type: "slovnik"
title: "ICIC – Inter-Cell Interference Coordination"
date: 2025-01-01
abbr: "ICIC"
fullName: "Inter-Cell Interference Coordination"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/icic/"
summary: "Soubor technik pro řízení a zmírňování rušení mezi sousedními buňkami v sítích LTE a 5G. Dynamicky koordinuje využívání zdrojů (jako je frekvence a výkon), aby zlepšila propustnost pro uživatele na ok"
---

ICIC je soubor technik pro řízení rušení mezi sousedními buňkami dynamickou koordinací využívání zdrojů s cílem zlepšit propustnost na okraji buňky a celkovou kapacitu sítě.

## Popis

Inter-Cell Interference Coordination (ICIC) je základní funkce správy rádiových zdrojů (RRM) navržená pro řízení a snížení mezibuněčného rušení, zejména pro koncová zařízení (UE) umístěná na okrajích buněk. V celulárních sítích, zejména těch používajících ortogonální multiplex s frekvenčním dělením ([OFDMA](/mobilnisite/slovnik/ofdma/)) jako LTE, může UE na okraji jedné buňky zaznamenat silné rušení na downlinku od přenosů sousední buňky na stejných zdrojových blocích a jeho uplinkové přenosy mohou způsobovat rušení základnové stanici sousední buňky. ICIC tento problém řeší tím, že umožňuje koordinaci mezi eNodeB ([eNB](/mobilnisite/slovnik/enb/)) nebo gNB prostřednictvím rozhraní X2 (nebo Xn v 5G NR). Tato koordinace zahrnuje výměnu signalizačních zpráv přenášejících informace související s rušením, jako jsou indikátory vysokého rušení (HII) a indikátory přetížení ([OI](/mobilnisite/slovnik/oi/)), které informují sousední buňky o zdrojových blocích, které zažívají nebo mají způsobit vysoké rušení.

Jádrový mechanismus ICIC zahrnuje rozdělení a správu rádiových zdrojů ve frekvenční, výkonové a časové oblasti. Běžným přístupem je ICIC ve frekvenční oblasti, kde je dostupné spektrum rozděleno na subpásma. Buňky koordinují přiřazení UE v centru buňky a UE na okraji buňky k různým subpásmům, aby zajistily, že stejné zdroje nejsou současně použity pro okrajové uživatele v sousedních buňkách. Například buňka může omezit svůj vysílací výkon na určitých zdrojových blocích určených pro okrajové uživatele svého souseda. ICIC ve výkonové oblasti zahrnuje úpravu úrovní vysílacího výkonu na zdrojový blok na základě koordinačních zpráv. ICIC v časové oblasti, relevantní pro systémy LTE s duplexem s časovým dělením (TDD), koordinuje konfigurace uplink/downlink, aby se zabránilo křížovému rušení.

ICIC funguje polo-statickým nebo dynamickým způsobem. Polo-statický ICIC zahrnuje předkonfigurované vzory nebo pomalejší koordinaci, zatímco vylepšený ICIC (eICIC) a dále vylepšený ICIC (feICIC), zavedené v pozdějších verzích standardů, podporují dynamičtější a sofistikovanější techniky, jako jsou téměř prázdné podrámce ([ABS](/mobilnisite/slovnik/abs/)). Při použití ABS dominantní makrobuňka ztlumí většinu svých přenosů v konkrétních podrámcích, což umožňuje rušeným malým buňkám nebo okrajovým UE komunikovat se sníženým rušením. Architektura se opírá o RRM funkce v každé základnové stanici, které zpracovávají měřicí hlášení od UE (jako jsou indikátory kvality kanálu) a koordinační zprávy od sousedů, aby přijímaly rozhodnutí o plánování minimalizující rušení, čímž optimalizují spektrální účinnost a uživatelský zážitek.

## K čemu slouží

ICIC byl vytvořen, aby vyřešil kritický problém mezibuněčného rušení, které se stává hlavním limitujícím faktorem výkonu v celulárních sítích, zejména jak se sítě zhušťují a spektrum je agresivně znovu využíváno pro uspokojení rostoucích požadavků na kapacitu. V raných celulárních systémech bylo rušení řízeno převážně statickým frekvenčním plánováním a velkými opakovacími faktory, což bylo neefektivní. S příchodem LTE a jeho cílem dosáhnout univerzálního opakovaného využití frekvence (reuse-1) pro maximální spektrální účinnost se rušení na okrajích buněk stalo závažným, což vedlo k nízké propustnosti a spadlým hovorům pro uživatele, kteří nebyli poblíž středu buňky.

Motivací pro standardizaci ICIC ve verzi 3GPP Release 8 bylo umožnit efektivní provoz s reuse-1 v sítích založených na [OFDMA](/mobilnisite/slovnik/ofdma/) bez obětování výkonu na okraji buňky. Před ICIC se sítě spoléhaly na robustní modulaci a kódování nebo prostě akceptovaly špatný výkon na okraji. ICIC poskytl standardizovaný rámec pro spolupráci základnových stanic, který přeměnil rušení z náhodného, neřízeného jevu na řízený zdroj. To bylo nezbytné pro dosažení vysokých přenosových rychlostí a jednotné kvality služby, kterou LTE slibovalo. Následná vylepšení řešila nové scénáře nasazení, jako jsou heterogenní sítě (HetNets), kde jsou nízkovýkonové uzly (picobuňky, femtobuňky) nasazeny v rámci pokrytí makrobuňky, což vytváří závažné problémy s rušením vyžadující pokročilejší koordinační techniky, jako je eICIC.

## Klíčové vlastnosti

- Rozdělení a koordinace zdrojů ve frekvenční oblasti mezi buňkami
- Výměna indikátorů rušení (HII, OI) prostřednictvím rozhraní X2/Xn
- Koordinace regulace výkonu pro uplinkové a downlinkové zdroje
- Podpora téměř prázdných podrámců (ABS) pro zmírnění rušení v časové oblasti
- Vylepšení pro nasazení heterogenních sítí (HetNet)
- Polo-statické a dynamické režimy koordinace přizpůsobitelné síťovému zatížení

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 32.521** (Rel-11) — SON Policy NRM IRP Requirements
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TR 36.902** (Rel-9) — SON Use Cases and Solutions for LTE

---

📖 **Anglický originál a plná specifikace:** [ICIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/icic/)
