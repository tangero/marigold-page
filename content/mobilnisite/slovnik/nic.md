---
slug: "nic"
url: "/mobilnisite/slovnik/nic/"
type: "slovnik"
title: "NIC – Network Independent Clocking"
date: 2025-01-01
abbr: "NIC"
fullName: "Network Independent Clocking"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nic/"
summary: "NIC je metoda synchronizace, při které síťový prvek nezávisle generuje vlastní časovací signál bez spoléhání se na externí síťový časovací zdroj. Používá se v konkrétních nasazeních, kde není kriticky"
---

NIC je metoda synchronizace, při které síťový prvek nezávisle generuje vlastní časovací signál bez použití externího síťového časovacího zdroje.

## Popis

Network Independent Clocking (NIC) je režim časování a synchronizace definovaný ve specifikacích 3GPP, zvláště relevantní pro rozhraní Iub/Iur v UTRAN (3G) a později zmiňovaný i v širších kontextech. V tomto režimu síťový prvek, například Node B (základnová stanice) nebo Radio Network Controller (RNC), provozuje svůj přenosový hodinový signál nezávisle na jakémkoli externím synchronizačním zdroji z přenosové sítě. To znamená, že prvek neobnovuje své hodiny z příchozího datového toku (jako v Network Synchronized Clocking) ani nepoužívá fyzické synchronizační rozhraní (jako E1/T1 nebo Synchronous Ethernet). Místo toho se spoléhá výhradně na vlastní interní oscilátor, což je typicky relativně levný zdroj hodin s nízkou přesností, například Stratum 3E nebo dokonce volnoběžný oscilátor.

Hlavním technickým důsledkem NIC je, že přenosový spoj pracuje asynchronním nebo plesiochronním způsobem. Vysílací zařízení odesílá data rychlostí určenou svými lokálními hodinami a přijímací zařízení musí mít dostatečnou vyrovnávací paměť (elastic stores nebo [FIFO](/mobilnisite/slovnik/fifo/) buffery), aby absorbovalo nevyhnutelné rozdíly v hodinových rychlostech mezi oběma konci, známé jako hodinový drift. K tomuto driftu dochází, protože žádné dva nezávislé hodiny neběží přesně na stejné frekvenci. Buffer kompenzuje tento rozdíl periodickým slipováním (opakováním nebo vypuštěním rámce), aby zabránil přetečení nebo podtečení. Tento proces je řízen řídicími mechanismy v protokolové vrstvě, například Frame Number ([FN](/mobilnisite/slovnik/fn/)) v Iub Frame Protocol ([FP](/mobilnisite/slovnik/fp/)).

Z architektonického hlediska NIC zjednodušuje fyzické nasazení síťových uzlů. Odstraňuje potřebu vyhrazené distribuční sítě pro synchronizaci, která může být složitá a nákladná na vybudování a údržbu. Neexistuje požadavek na zařízení Synchronous Digital Hierarchy (SDH), zdroje Precision Time Protocol (PTP) nebo přijímače Global Navigation Satellite System ([GNSS](/mobilnisite/slovnik/gnss/)) na každém místě pouze pro synchronizaci přenosu. Rozhraní může fungovat přes asynchronní přenosové sítě jako IP/Ethernet bez jakýchkoli speciálních časovacích funkcí. Klíčovými komponentami umožňujícími NIC jsou lokální oscilátor a související mechanismy pro vyrovnávání a adaptaci rychlosti v rámci hardwaru a softwaru rozhraní.

Úloha NIC v síti je určena pro aplikace, kde vysoká přesnost synchronizace není přísným požadavkem. V raných nasazeních 3G pro nereálné datové služby nebo v určitých scénářích nízkonákladových indoor nebo small cell řešení byl výkonový dopad občasného slipování rámců způsobeného hodinovým driftem přijatelný. Poskytuje nákladově efektivní a jednoduché řešení pro konektivitu. Pro funkce však vyžadující těsnou koordinaci mezi buňkami, jako je makro-diverzita (měkký handover v UMTS), koordinace mezibuněčných interferencí nebo pozdější technologie jako LTE a 5G NR, které vyžadují velmi těsné fázové zarovnání pro funkce jako Coordinated Multipoint (CoMP) a provoz TDD, je NIC nedostatečná. Tyto pokročilé funkce vyžadují vysoce přesnou synchronizaci frekvence, fáze a času, což vede k potřebě režimů Network Synchronized Clocking (NSC) nebo Synchronous Clocking.

## K čemu slouží

NIC byl vytvořen, aby nabídl jednoduchou, nízkonákladovou možnost nasazení pro rozhraní mobilních sítí, primárně v éře 3G UMTS. Základní problém, který řeší, jsou náklady a složitost nasazení synchronizační sítě. Tradiční sítě založené na TDM (jako ty používající linky E1/T1) přenášely synchronizaci inherentně. Když sítě začaly migrovat na paketový přenos (IP, Ethernet), distribuce přesného časování se stala významnou výzvou a nákladem. NIC poskytl bezprostřední, pragmatické řešení pro operátory, kteří upřednostňovali rychlé a ekonomické rozšíření pokrytí základnovými stanicemi, zejména pro služby, kde ultra-přesné časování ještě nebylo kritické, jako například rané datové služby [HSPA](/mobilnisite/slovnik/hspa/).

Řešil omezení vyplývající z požadavku, aby každá lokalita měla vysoce kvalitní zdroj hodin nebo spolehlivý časovací signál ze sítě. V odlehlých, indoorových nebo nákladově citlivých nasazeních byla instalace a údržba [GNSS](/mobilnisite/slovnik/gnss/) antény nebo vyhrazeného synchronního spoje často nepraktická nebo příliš drahá. NIC umožnil připojení zařízení přes standardní, asynchronní Ethernetové linky bez jakékoli dodatečné časovací infrastruktury. To bylo obzvláště užitečné pro spoje Iub (Node B k RNC) v hierarchických 3G sítích.

Historicky NIC představuje přechodnou fázi ve vývoji mobilních sítí. Uznával přechod na paketovou přenosovou síť a zároveň poskytoval provizorní řešení předtím, než se robustní paketové časovací technologie jako [IEEE](/mobilnisite/slovnik/ieee/) 1588v2 (PTP) a Synchronous Ethernet staly zralými a široce nasazenými. Jak se síťové požadavky vyvíjely směrem k vyšší kapacitě, koordinaci mezi buňkami a podpoře TDD a pokročilých anténních systémů, omezení NIC – především jeho nedostatečná přesnost a potenciál pro slipování ovlivňující služby – se stala zřejmými. To motivovalo vývoj a přijetí přesných paketových synchronizačních metod, čímž se NIC stal zastaralým režimem v moderních nasazeních 5G, kde je často vyžadována přesnost na úrovni nanosekund.

## Klíčové vlastnosti

- Funguje s nezávislým lokálním oscilátorem bez externího časovacího referenčního signálu
- Umožňuje asynchronní (plesiochronní) přenos přes paketové sítě
- Odstraňuje potřebu složité infrastruktury pro distribuci synchronizace
- Používá vyrovnávání a mechanismy slipování rámců ke kompenzaci hodinového driftu mezi koncovými body
- Zjednodušuje nasazení a snižuje náklady pro aplikace, kde časování není kritické
- Primárně definován pro rozhraní UTRAN Iub/Iur používající Iub Frame Protocol

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 37.901** (Rel-15) — UE Application Layer Data Throughput Performance

---

📖 **Anglický originál a plná specifikace:** [NIC na 3GPP Explorer](https://3gpp-explorer.com/glossary/nic/)
