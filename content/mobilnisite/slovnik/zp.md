---
slug: "zp"
url: "/mobilnisite/slovnik/zp/"
type: "slovnik"
title: "ZP – Zero power CSI-RS"
date: 2025-01-01
abbr: "ZP"
fullName: "Zero power CSI-RS"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/zp/"
summary: "Zero power CSI-RS (ZP CSI-RS) je potlačený referenční signálový prostředek v 5G NR. gNB na těchto prostředcích nevysílá nic, což umožňuje UE měřit interferenci ze sousedních buněk. To je klíčové pro p"
---

ZP je potlačený referenční signálový prostředek v 5G NR, kde gNB nevysílá nic, což umožňuje UE měřit interferenci ze sousedních buněk pro přesné podávání zpráv o CSI.

## Popis

Zero power [CSI-RS](/mobilnisite/slovnik/csi-rs/) (ZP CSI-RS) je specifická konfigurace referenčního signálu pro informace o stavu kanálu (Channel State Information Reference Signal, CSI-RS) ve fyzické vrstvě 5G New Radio (NR). Na rozdíl od běžného CSI-RS s nenulovým výkonem (Non-Zero Power, [NZP](/mobilnisite/slovnik/nzp/)), který vysílá známé referenční symboly pro odhad kanálu, je prostředek ZP CSI-RS soubor časově-frekvenčních prostředků, kde gNB záměrně potlačí svůj přenos (vysílá s nulovým výkonem). Primární funkcí těchto potlačených prostředků je vytvořit příležitosti pro měření, aby uživatelské zařízení (User Equipment, UE) mohlo odhadnout interferenci. UE je prostřednictvím signalizace řízení rádiových prostředků (Radio Resource Control, [RRC](/mobilnisite/slovnik/rrc/)) informováno o konfiguraci prostředků ZP CSI-RS, včetně jejich periodicity, šířky pásma a umístění v rámci mřížky prostředků.

Jeho fungování je nedílnou součástí pokročilých rámců pro získávání [CSI](/mobilnisite/slovnik/csi/). gNB plánuje prostředky ZP CSI-RS ve spolupráci se sousedními buňkami, často jako součást schémat koordinovaného vícemístného přenosu (Coordinated Multi-Point, CoMP) nebo vylepšené koordinace mezibuněčné interference (enhanced Inter-Cell Interference Coordination, eICIC). Když obsluhující buňka na těchto konkrétních prvcích prostředků (Resource Elements, REs) potlačí svůj signál, přijímač UE bude primárně zachycovat signály od jiných rušivých vysílačů (např. jiných gNB nebo UE) a šum na těchto prostředcích. Tato změřená výkonnost se používá pro výpočet metriky prostředku pro měření interference (Interference Measurement Resource, [IMR](/mobilnisite/slovnik/imr/)). UE pak tento odhad interference spolu s odhady kanálu získanými z NZP CSI-RS použije k výpočtu zpětné vazby CSI, jako je indikátor kvality kanálu (Channel Quality Indicator, [CQI](/mobilnisite/slovnik/cqi/)), indikátor předkódovací matice (Precoding Matrix Indicator, [PMI](/mobilnisite/slovnik/pmi/)) a indikátor hodnosti (Rank Indicator, [RI](/mobilnisite/slovnik/ri/)).

Mezi klíčové zahrnuté komponenty patří nastavení CSI prostředků, které může obsahovat jak NZP, tak ZP CSI-RS prostředky, a nastavení podávání zpráv o CSI, které propojuje měření s konkrétní zprávou. Konfigurace ZP CSI-RS je součástí informačního elementu CSI-MeasConfig signalizovaného UE. Z architektonického hlediska je tato funkce rozdělena mezi plánovač gNB, který rozhoduje, kdy a kde potlačit přenos, a postupy měření fyzické vrstvy UE. Rozhodnutí gNB nakonfigurovat ZP CSI-RS je úlohou správy sítě zaměřenou na optimalizaci celkového výkonu sítě, zejména v hustých nasazeních, kde je interference limitujícím faktorem.

Jeho role v síti je klíčová pro umožnění přesné adaptace spojení a plánování víceuživatelského MIMO. Tím, že ZP CSI-RS poskytuje čistý pohled na interferenční prostředí, umožňuje UE doporučit schéma modulace a kódování (modulation and coding scheme, MCS), které je odolné vůči skutečné mezibuněčné interferenci, nikoli pouze vůči signálu obsluhující buňky. To vede k vyšší propustnosti a lepší spolehlivosti. Dále, ve scénářích jako je dynamický výběr bodu nebo společný přenos CoMP, se prostředky ZP CSI-RS používají k měření interference z nekooperujících bodů, což síti umožňuje činit inteligentní rozhodnutí o tom, které přenosové body by měly obsluhovat dané UE.

## K čemu slouží

ZP CSI-RS byl představen ve specifikaci 3GPP Release 15 s 5G NR, aby řešil omezení technik měření interference v LTE. V LTE bylo měření interference často založeno na buňkově specifickém referenčním signálu (Cell-specific Reference Signal, CRS), který byl vždy vysílán, což ztěžovalo izolaci interference od konkrétních buněk nebo v konkrétních blocích prostředků. To bylo nedostatečné pro pokročilá víceanténní a koordinační schémata plánovaná pro 5G, která vyžadují přesnou, na prostředky specifickou znalost interference.

Tato technologie existuje, aby vyřešila problém nepřesného podávání zpráv o CSI v prostředích omezených interferencí. Bez ZP CSI-RS by mohla být zpráva CQI od UE založena na interferenci měřené na prostředcích, které zahrnují vlastní data nebo referenční signály obsluhující buňky, což by vedlo k nadhodnocení interference a příliš konzervativnímu výběru MCS. Poskytnutím vyhrazených, potlačených prostředků vytváří ZP CSI-RS „čistý“ snímek interference, což umožňuje agresivnější a přesnější adaptaci spojení. To přímo zlepšuje spektrální účinnost a propustnost uživatele, zejména na okraji buňky.

Historicky bylo jeho vytvoření motivováno potřebou podporovat flexibilní a dynamické TDD, ultra-hustá nasazení sítí a pokročilé techniky CoMP v 5G. Tyto scénáře se vyznačují rychle se měnícími a potenciálně závažnými interferenčními vzory. ZP CSI-RS poskytuje síti potřebný nástroj pro proaktivní řízení této interference. Umožňuje síťově koordinované vzorce potlačení, které lze použít nejen pro měření, ale také jako primitiv pro vyhýbání se interferenci, kde silní rušiče potlačí přenos v určitých prostředcích ve prospěch ohrožených UE v sousedních buňkách.

## Klíčové vlastnosti

- Definuje potlačené časově-frekvenční prostředky, na kterých obsluhující gNB vysílá s nulovým výkonem.
- Konfigurováno prostřednictvím RRC signalizace jako součást rámce pro měření CSI.
- Používáno UE k měření interference ze sousedních buněk a šumu.
- Nezbytné pro přesný výpočet indikátoru kvality kanálu (CQI) a dalších parametrů CSI.
- Umožňuje pokročilé techniky řízení interference, jako jsou CoMP a eICIC.
- Poskytuje měření interference specifické pro prostředky, což je nadřazené metodám založeným na průměrné RSSI.

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [ZP na 3GPP Explorer](https://3gpp-explorer.com/glossary/zp/)
