---
layout: post
title: "Budoucnost frekvenčního multiplexu: Alternativy k OFDMA a jejich role v 6G"
date: 2024-11-25
categories: [LTE, 4G, Mobilní sítě]
---

Budoucnost frekvenčního multiplexu: Alternativy k OFDMA a jejich role v 6G

Orthogonal Frequency Division Multiple Access (OFDMA) se stal základem pro technologie 4G LTE a 5G NR díky své schopnosti efektivně rozdělit dostupné frekvenční spektrum mezi uživatele. Přestože OFDMA nabízí vysokou spektrální efektivitu a robustnost vůči interferenci, vývoj směrem k sítím 6G s sebou přináší potřebu alternativ, které by mohly zlepšit využití spektra, podporovat masivní konektivitu a umožnit přenosy dat s nízkou latencí. 

Mezi nejvýznamnější technologie, které se zvažují jako doplňky nebo náhrady OFDMA, patří Non-Orthogonal Multiple Access (NOMA), Rate-Splitting Multiple Access (RSMA) a Sparse Code Multiple Access (SCMA). Na následujících odkazech si je probereme podrobněji:

- [/mobilnisite/Non-Orthogonal-Multiple-Access-NOMA/](Non-Orthogonal Multiple Access (NOMA))
- [/mobilnisite/Rate-Splitting-Multiple-Access-RSMA/](Rate-Splitting Multiple Access (RSMA))
- [/mobilnisite/Sparse-Code-Multiple-Access-SCMA/](Sparse Code Multiple Access (SCMA))
- další experimentální přístupy na konci tohoto článku
- a pro pořádek povídání o tom, [jak funguje OFDMA](/mobilnisite/ofdma)





## Porovnání technologií: Jak si vedou proti OFDMA?

| Technologie |	Hlavní výhody |	Případné nevýhody |	Podporující společnosti |
| NOMA |	Vyšší spektrální efektivita, podpora IoT |	Vyšší složitost SIC	Huawei, ZTE |
| RSMA |	Robustnost vůči interferenci, univerzálnost	| Náročné řízení přenosu |	Ericsson, Qualcomm |
| SCMA |	Energetická efektivita, podpora IoT |	Vyšší složitost kódování |	NTT DOCOMO |

## Budoucnost a výhled pro 6G

Sítě 6G přinesou zcela nové výzvy v oblasti řízení spektra, včetně podpory extrémně vysokých přenosových rychlostí, masivní konektivity a ultra-nízké latence. Technologie jako NOMA, RSMA a SCMA nabízejí slibné alternativy nebo doplňky k OFDMA, avšak každá z nich má své specifické výhody a omezení. V budoucnosti se pravděpodobně dočkáme kombinace těchto technologií, která zajistí optimální využití spektra pro různé aplikace.

Existují ale i další přístupy, které zatím existují jen v konceptech, kdy se zkoumá několik nových přístupů k multiplexování. Zde jsou hlavní směry výzkumu, které si zmiňujeme pro úplnost:

** Spatial Scattering Modulation (SSM)**:
- Využívá prostorové rozptylové charakteristiky kanálu
- Umožňuje přenos dodatečných informací pomocí výběru vzorců rozptylu
- Vhodné zejména pro systémy s masivním MIMO
- Potenciálně energeticky účinnější než tradiční prostorové multiplexování

**Index Modulation (IM)**:
- Přenáší dodatečné informace pomocí aktivace/deaktivace různých přenosových prvků
- Může být aplikováno na různé domény (frekvence, prostor, čas)
- Nabízí dobrý kompromis mezi spektrální a energetickou účinností
- Nižší implementační složitost ve srovnání s některými jinými pokročilými technikami

**Orbital Angular Momentum (OAM) Multiplexing**:
- Využívá orbitální moment hybnosti elektromagnetických vln
- Umožňuje vytvoření několika ortogonálních kanálů v prostoru
- Potenciálně velmi vysoká spektrální účinnost
- Zatím ve fázi základního výzkumu, čelí výzvám v praktické implementaci

**Reconfigurable Intelligent Surface (RIS) Assisted Multiple Access**:
- Využívá inteligentní odrazné plochy pro optimalizaci přenosových cest
- Umožňuje aktivní tvarování rádiového prostředí
- Může významně zlepšit pokrytí a kapacitu systému
- Kombinovatelné s jinými přístupovými technikami

Tyto techniky jsou zatím ve fázi výzkumu a vývoje. Očekává se, že budoucí sítě 6G budou pravděpodobně využívat kombinaci několika těchto přístupů v závislosti na konkrétních požadavcích aplikací a podmínkách prostředí.

Klíčovou otázkou zůstává standardizace těchto technologií v rámci 3GPP. Zatímco společnosti jako Huawei, Ericsson nebo Qualcomm hrají v tomto procesu hlavní roli, bude důležité, aby se zapojili i další hráči a akademické instituce. Sítě 6G nebudou pouze o rychlejších datech, ale také o efektivnějším a udržitelnějším využití spektra – což je cíl, k němuž tyto technologie směřují.