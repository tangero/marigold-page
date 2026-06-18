---
slug: "ribs"
url: "/mobilnisite/slovnik/ribs/"
type: "slovnik"
title: "RIBS – Radio-interface based synchronization"
date: 2025-01-01
abbr: "RIBS"
fullName: "Radio-interface based synchronization"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ribs/"
summary: "Synchronizace založená na rádiovém rozhraní (RIBS) je metoda synchronizace základnových stanic (eNB/gNB) vzduchem pomocí LTE nebo NR signálů, která eliminuje potřebu vyhrazených časovacích propojení v"
---

RIBS je metoda synchronizace základnových stanic vzduchem pomocí LTE nebo NR signálů, která eliminuje potřebu vyhrazených časovacích propojení v přenosové síti (backhaul).

## Popis

Synchronizace založená na rádiovém rozhraní (RIBS) je synchronizační mechanismus definovaný v 3GPP, který umožňuje základnovým stanicím, konkrétně [eNB](/mobilnisite/slovnik/enb/) v LTE a gNB v NR, dosáhnout časové a frekvenční synchronizace využitím signálů rádiového rozhraní vysílaných sousedními základnovými stanicemi nebo určenou referenční buňkou. Namísto spoléhání se na externí synchronizační zdroje, jako je Globální navigační satelitní systém ([GNSS](/mobilnisite/slovnik/gnss/), např. [GPS](/mobilnisite/slovnik/gps/)) nebo přesný časovací protokol ([PTP](/mobilnisite/slovnik/ptp/), např. [IEEE](/mobilnisite/slovnik/ieee/) 1588) přes přenosovou síť (backhaul), umožňuje RIBS základnové stanici synchronizovat se přijímáním a zpracováním downlink referenčních signálů (např. Primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)), Sekundární synchronizační signál ([SSS](/mobilnisite/slovnik/sss/)) nebo Buňkově specifické referenční signály ([CRS](/mobilnisite/slovnik/crs/))) ze synchronizované dárčí buňky. Tento proces zahrnuje měření časových rozdílů a úpravu lokálního oscilátoru pro zarovnání s referencí, čímž zajišťuje, že více buněk pracuje s koordinovaným časováním, což je klíčové pro funkce jako koordinované vícebodové vysílání/příjem (CoMP), vylepšená koordinace mezibuněčné interference (eICIC) a provoz s duplexem s časovým dělením (TDD).

Z architektonického hlediska RIBS funguje v rámci rádiové přístupové sítě (RAN), typicky ve scénářích, kdy základnová stanice (synchronizující uzel) nemá přímý přístup ke spolehlivému externímu časovacímu zdroji. Klíčové komponenty zahrnují dárčí základnovou stanici, která slouží jako synchronizační zdroj, a přijímající základnovou stanici, která provádí měření na downlink rádiových signálech. Proces zahrnuje dekódování synchronizačních signálů přijímající základnovou stanicí a potenciální využití polohových referenčních signálů (PRS) k odhadu zpoždění šíření a korekci časových odchylek. RIBS je specifikováno v 3GPP TS 36.300, která popisuje postupy pro LTE, a podobné principy platí pro nasazení NR. Přesnost synchronizace dosažitelná s RIBS je typicky v řádu mikrosekund, což stačí pro mnoho koordinačních funkcí RAN, ale nemusí dosahovat přesnosti na úrovni nanosekund jako GNSS nebo PTP.

Jak RIBS funguje, zahrnuje několik kroků: nejprve základnová stanice prohledává okolní buňky a identifikuje vhodnou dárčí buňku, která je již synchronizována (např. přes GNSS). Poté kontinuálně monitoruje downlink signály dárčí buňky, přičemž využívá algoritmy k odhadu frekvenčního posunu a časového předstihu. Tyto odhady jsou předávány do synchronizačního modulu základnové stanice, který podle nich upravuje svůj hodinový signál. RIBS může fungovat hierarchickým způsobem, kdy hlavní základnová stanice s externími synchronizačními zdroji synchronizuje sekundární základnové stanice, které se následně mohou stát dárci pro další, čímž vzniká synchronizační řetězec. Tato metoda je obzvláště cenná v hustých městských nasazeních, indoor scénářích nebo odlehlých oblastech, kde jsou GPS signály slabé nebo není dostupná podpora časování v přenosové síti, což umožňuje robustní provoz sítě bez dodatečných nákladů na infrastrukturu.

## K čemu slouží

RIBS bylo zavedeno, aby řešilo výzvy a náklady spojené s nasazením externích synchronizačních zdrojů, jako jsou GPS přijímače nebo přenosové sítě podporující IEEE 1588, u každé základnové stanice, zejména v heterogenních nasazeních a nasazeních small buněk. Před zavedením RIBS synchronizace výrazně závisela na těchto externích metodách, které mohly být nákladné, náchylné k poruchám (např. rušení nebo falšování GPS) nebo nepraktické v prostředích, jako jsou podzemní prostory nebo husté městské zástavby (urban canyons). RIBS poskytuje nákladově efektivní alternativu využitím stávajícího rádiového rozhraní, čímž snižuje závislost na dodatečném hardwaru a zjednodušuje plánování sítě.

Historicky potřeba RIBS rostla s vývojem sítí LTE-Advanced a 5G, kde pokročilé funkce jako CoMP, eICIC a TDD vyžadují těsnou synchronizaci pro omezení interference a zlepšení spektrální účinnosti. Ve vydání 12 3GPP formalizovalo RIBS pro podporu vylepšení small buněk a scénářů duální konektivity. Řeší problémy související se synchronizací v podmínkách neideální přenosové sítě (backhaul), což operátorům umožňuje flexibilně nasazovat základnové stanice bez přísných požadavků na časovací infrastrukturu. To je obzvláště důležité pro zhušťování sítě, kde je třeba efektivně synchronizovat četné small buňky, a pro scénáře obnovy po havárii, kde mohou být externí časovací zdroje narušeny.

## Klíčové vlastnosti

- Umožňuje synchronizaci základnových stanic využitím LTE nebo NR signálů vzduchem od sousedních buněk
- Snižuje závislost na externích časovacích zdrojích, jako je GPS nebo IEEE 1588
- Podporuje hierarchické synchronizační řetězce pro škálovatelné nasazení
- Umožňuje provoz koordinovaného vícebodového vysílání/příjmu (CoMP) a koordinace interference (eICIC)
- Použitelné pro režimy duplexu s frekvenčním dělením (FDD) i duplexu s časovým dělením (TDD)
- Zvyšuje odolnost sítě v prostředích bez dostupného GPS signálu

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [RIBS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ribs/)
