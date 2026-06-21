---
slug: "ran"
url: "/mobilnisite/slovnik/ran/"
type: "slovnik"
title: "RAN – Radio Access Network"
date: 2026-01-01
abbr: "RAN"
fullName: "Radio Access Network"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ran/"
summary: "Rádiová přístupová síť (Radio Access Network, RAN) je část mobilní sítě, která spojuje jednotlivá uživatelská zařízení (UE) s jádrem sítě prostřednictvím rádiových vln. Skládá se ze základnových stani"
infografika: "/assets/slovnik/ran.svg"
infografikaAlt: "Schéma architektury 5G sítě se zvýrazněním RAN"
---

RAN je část mobilní sítě, která spojuje uživatelská zařízení s jádrem sítě prostřednictvím rádiových vln; zahrnuje základnové stanice a řadiče, které spravují rádiové prostředky a spojení.

## Popis

Rádiová přístupová síť (Radio Access Network, RAN) představuje kritickou infrastrukturu, která zprostředkovává bezdrátovou komunikaci mezi uživatelským zařízením (UE), jako jsou chytré telefony a IoT zařízení, a operátorským jádrem sítě. Je zodpovědná za všechny funkce související s rádiovým přenosem, včetně vysílání a příjmu rádiových signálů, modulace/demodulace dat, správy rádiového spektra a zajištění mobility uživatelů při jejich pohybu. Fyzicky se RAN skládá z buněk vybavených anténami a rádiovým zařízením (často nazývanými základnové stanice), které jsou propojeny pomocí přenosových tras (backhaul, mikrovlnné nebo optické spoje) s centralizovanými nebo distribuovanými zpracovatelskými jednotkami.

Z architektonického hlediska se RAN vyvíjela napříč generacemi. Ve 2G/3G (GSM/UMTS) šlo o hierarchickou síť se základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)/NodeB) a centralizovaným řadičem rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)). RAN pro 4G LTE zavedla zploštělou architekturu s eNodeB, který integroval funkce řadiče přímo do základnové stanice, čímž snížil latenci. RAN pro 5G NR se dále vyvinula s gNodeB (gNB) a zavedla koncepty jako rozdělení na centralizovanou jednotku ([CU](/mobilnisite/slovnik/cu/)) a distribuovanou jednotku ([DU](/mobilnisite/slovnik/du/)), což umožňuje flexibilnější a cloudově nativní nasazení. Bez ohledu na generaci RAN plní klíčové funkce: správu rádiových prostředků (plánování, řízení výkonu), řízení mobility spojení (předávání), rádiové řízení přístupu a hlášení měření.

Na úrovni protokolové vrstvy RAN implementuje zásobník napříč fyzickou vrstvou ([PHY](/mobilnisite/slovnik/phy/)), řízením přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), řízením rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)), protokolem pro konverzi paketových dat ([PDCP](/mobilnisite/slovnik/pdcp/)) a řízením rádiových prostředků (RRC). Tyto vrstvy zajišťují úkoly od přenosu surových bitů vzduchem až po vytváření a udržování rádiových přenosových kanálů pro uživatelská data a signalizaci. RAN rozhraní s jádrem sítě prostřednictvím standardizovaných rozhraní: rozhraní Iu ve 3G, rozhraní S1 ve 4G a rozhraní NG v 5G. Právě výkon RAN – její spektrální účinnost, latence a spolehlivost – přímo určuje uživatelský zážitek ze všech mobilních služeb, od hlasových hovorů až po ultra-spolehlivou komunikaci s nízkou latencí (URLLC).

## K čemu slouží

Rádiová přístupová síť existuje proto, aby překlenula propast mezi pevným jádrem sítě a množstvím bezdrátových koncových zařízení. Jejím základním účelem je poskytnout všudypřítomné rádiové pokrytí a kapacitu, což umožňuje mobilní komunikaci. Bez RAN by služby jádra sítě byly pro mobilní uživatele nedostupné. Řeší problém poskytování spolehlivého a kvalitního bezdrátového připojení uživatelům, kteří se pohybují a jejichž charakteristiky spojení se neustále mění vlivem faktorů, jako je vzdálenost, interference a překážky.

Historicky byl vývoj RAN hnán potřebou vyšších přenosových rychlostí, nižší latence, větší kapacity a efektivnějšího využití spektra. Rané RAN (1G, 2G) byly navrženy především pro přepojování okruhů pro hlas. RAN pro 3G zavedla schopnosti přepojování paketů pro data. Přechod na plochou architekturu v 4G LTE byl motivován potřebou snížit latenci pro služby založené na IP. Probíhající vývoj směrem k 5G a Open RAN je poháněn požadavky na extrémně vysokou mobilní šířku pásma, masivní připojení IoT a služby pro klíčové aplikace, což vyžaduje nebývalou flexibilitu, účinnost a inovace na rádiové vrstvě.

RAN řeší základní technické výzvy bezdrátové komunikace: správu sdíleného, na interferenci náchylného média (rádiového spektra), podporu mobility uživatelů s plynulým předáváním spojení a přizpůsobování se velmi proměnným podmínkám přenosového kanálu. Tyto složitosti abstrahuje a poskytuje jádru sítě stabilní datový kanál. Kontinuální inovace v technologii RAN prostřednictvím technik, jako je MIMO, agregace nosných a dělení sítě (network slicing), umožňují každé nové generaci mobilní technologie přinášet převratné nové služby a zážitky.

## Klíčové vlastnosti

- Správa rádiových prostředků a dynamické plánování
- Řízení mobility a provádění předávání spojení (handover)
- Zpracování signálu pro modulaci/demodulaci (fyzická vrstva PHY)
- Vytváření, udržování a uvolňování spojení (RRC)
- Zpracování datových paketů, šifrování a komprese hlaviček (PDCP/RLC)
- Rozhraní k jádru sítě (např. prostřednictvím rozhraní S1, NG)

## Definující specifikace

- **TR 21.866** (Rel-15) — Study on Energy Efficiency in 3GPP Standards
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.468** (Rel-19) — Group Communication System Enabler Requirements
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TS 22.822** (Rel-16) — Satellite Access in 5G Study
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- … a dalších 76 specifikací

---

📖 **Anglický originál a plná specifikace:** [RAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ran/)
