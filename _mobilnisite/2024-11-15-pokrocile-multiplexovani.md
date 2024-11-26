---
layout: post
title: "Budoucnost frekvenčního multiplexu: Alternativy k OFDMA a jejich role v 6G"
date: 2024-11-25
categories: [LTE, 4G, Mobilní sítě]
---

Budoucnost frekvenčního multiplexu: Alternativy k OFDMA a jejich role v 6G

Orthogonal Frequency Division Multiple Access (OFDMA) se stal základem pro technologie 4G LTE a 5G NR díky své schopnosti efektivně rozdělit dostupné frekvenční spektrum mezi uživatele. Přestože OFDMA nabízí vysokou spektrální efektivitu a robustnost vůči interferenci, vývoj směrem k sítím 6G s sebou přináší potřebu alternativ, které by mohly zlepšit využití spektra, podporovat masivní konektivitu a umožnit přenosy dat s nízkou latencí. 

Zde si podrobněji probereme nejvýznamnější technologie, které se zvažují jako doplňky nebo náhrady OFDMA:

- [Non-Orthogonal Multiple Access (NOMA)](/mobilnisite/Non-Orthogonal-Multiple-Access-NOMA/)
- [Rate-Splitting Multiple Access (RSMA)](/mobilnisite/Rate-Splitting-Multiple-Access-RSMA/)
- [Sparse Code Multiple Access (SCMA)](/mobilnisite/Sparse-Code-Multiple-Access-SCMA/)
- a pro pořádek povídání o tom, [jak funguje OFDMA](/mobilnisite/ofdma)
- další experimentální přístupy na konci tohoto článku





## Porovnání technologií: Jak si vedou proti OFDMA?

| Technologie | Hlavní výhody | Případné nevýhody | Podporující společnosti |
|-------------|---------------|-------------------|-------------------------|
| [NOMA](/mobilnisite/Non-Orthogonal-Multiple-Access-NOMA/) | Vyšší spektrální efektivita, podpora IoT | Vyšší složitost | Huawei, ZTE |
| [RSMA](/mobilnisite/Rate-Splitting-Multiple-Access-RSMA/) | Robustnost vůči interferenci, univerzálnost | Náročné řízení přenosu | Ericsson, Qualcomm |
| [SCMA](/mobilnisite/Sparse-Code-Multiple-Access-SCMA/) | Energetická efektivita, podpora IoT | Vyšší složitost kódování | NTT DOCOMO |
| Spatial Scattering Modulation (SSM) | Vysoká energetická účinnost, využití prostorové diverzity, vhodné pro masivní MIMO | Citlivost na změny prostředí, složitá charakterizace kanálu | Samsung, Nokia |
| Index Modulation (IM) | Nízká implementační složitost, dobrá energetická účinnost, flexibilita nasazení | Omezená spektrální účinnost při vyšších datových tocích, citlivost na synchronizaci | Intel, MediaTek |
| Orbital Angular Momentum (OAM) Multiplexing | Extrémně vysoká spektrální účinnost, teoreticky neomezený počet ortogonálních kanálů | Vysoká citlivost na atmosférické podmínky, omezený dosah, složitá implementace | China Mobile, Huawei |
| RIS Assisted Multiple Access | Aktivní tvarování rádiového prostředí, zlepšení pokrytí, energetická účinnost | Vysoké počáteční náklady na infrastrukturu, složitost optimalizace | NTT DOCOMO, Samsung |

*Poznámka: Technologie bez prolinku na detaily jsou spíše experimentální. Uvedené podporující společnosti jsou orientační a vycházejí z veřejně dostupných informací o výzkumných aktivitách a patentových přihláškách těchto firem. Mnoho těchto technologií je stále ve fázi výzkumu a vývoje, přičemž na jejich vývoji se často podílí více společností současně nebo v rámci výzkumných konsorcií.*

| Technologie |	Hlavní výhody |	Případné nevýhody |	Podporující společnosti |
|-------------|---------------|-------------------|-------------------------|
| [NOMA](/mobilnisite/Non-Orthogonal-Multiple-Access-NOMA/) |	Vyšší spektrální efektivita, podpora IoT |	Vyšší složitost |	Huawei, ZTE |
| [RSMA](/mobilnisite/Rate-Splitting-Multiple-Access-RSMA/) |	Robustnost vůči interferenci, univerzálnost	| Náročné řízení přenosu |	Ericsson, Qualcomm |
| [SCMA](/mobilnisite/Sparse-Code-Multiple-Access-SCMA/) |	Energetická efektivita, podpora IoT |	Vyšší složitost kódování |	NTT DOCOMO |

## Budoucnost a výhled pro 6G

Výše vyjmenovanými technologiemi multiplexování ale nejsme u konce. Sítě 6G přinesou zcela nové výzvy v oblasti řízení spektra, včetně podpory extrémně vysokých přenosových rychlostí, masivní konektivity a ultra-nízké latence. Technologie jako NOMA, RSMA a SCMA nabízejí slibné alternativy nebo doplňky k OFDMA, avšak každá z nich má své specifické výhody a omezení. V budoucnosti se pravděpodobně dočkáme kombinace těchto technologií, která zajistí optimální využití spektra pro různé aplikace.

Existují ale i další přístupy, které zatím existují jen v konceptech, kdy se zkoumá několik nových přístupů k multiplexování. Zde jsou hlavní směry výzkumu, které si zmiňujeme pro úplnost:

**Spatial Scattering Modulation (SSM)**:
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

**👉 Přehled nových přístupů k multiplexování:** \
- [Non-Orthogonal Multiple Access (NOMA)](/mobilnisite/Non-Orthogonal-Multiple-Access-NOMA/)
- [Rate-Splitting Multiple Access (RSMA)](/mobilnisite/Rate-Splitting-Multiple-Access-RSMA/)
- [Sparse Code Multiple Access (SCMA)](/mobilnisite/Sparse-Code-Multiple-Access-SCMA/)
- další [experimentální přístupy k multiplexování](/mobilnisite/pokrocile-multiplexovani/)
- a pro pořádek povídání o tom, [jak funguje OFDMA](/mobilnisite/ofdma)