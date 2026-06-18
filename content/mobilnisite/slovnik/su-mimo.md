---
slug: "su-mimo"
url: "/mobilnisite/slovnik/su-mimo/"
type: "slovnik"
title: "SU-MIMO – Single User Multiple Input Multiple Output"
date: 2025-01-01
abbr: "SU-MIMO"
fullName: "Single User Multiple Input Multiple Output"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/su-mimo/"
summary: "SU-MIMO je technika MIMO, při níž je jednomu uživatelskému terminálu přiděleno více prostorových vrstev (proudů) z jedné základnové stanice pro zvýšení přenosové rychlosti. Zvyšuje spektrální účinnost"
---

SU-MIMO je technika MIMO, při níž jeden uživatelský terminál přijímá z jedné základnové stanice více paralelních datových proudů na stejných časově-frekvenčních zdrojích za účelem zvýšení přenosové rychlosti a spektrální účinnosti.

## Popis

Single User Multiple Input Multiple Output (SU-MIMO) je klíčová technologie fyzické vrstvy ve standardech 3GPP, primárně definovaná pro LTE a NR. Funguje tak, že jak základnová stanice (eNodeB v LTE, gNB v NR), tak uživatelské zařízení (UE) jsou vybaveny více anténami pro vytvoření více paralelních prostorových kanálů, známých jako vrstvy nebo proudy. Základním principem je prostorové multiplexování, při kterém jsou nezávislé datové proudy vysílány současně z různých anténních portů, čímž se využívá prostorový rozměr rádiového kanálu. Počet vrstev je omezen minimem z počtu vysílacích a přijímacích antén a hodností matice kanálu, kterou UE hlásí prostřednictvím zpětné vazby o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)), včetně indikátoru hodnosti ([RI](/mobilnisite/slovnik/ri/)).

Provoz SU-MIMO zahrnuje několik klíčových procedur. Základnová stanice naplánuje UE a určí předkodovací matici, která mapuje datové vrstvy na fyzické anténní porty, na základě zpětné vazby od UE. Toto předkódování má za cíl směrovat energii k UE a řídit mezistreamové interference. UE využívá pokročilé zpracování signálu, jako je detekce s minimální střední kvadratickou chybou ([MMSE](/mobilnisite/slovnik/mmse/)) nebo maximální věrohodností ([ML](/mobilnisite/slovnik/ml/)), k oddělení a dekódování více překrývajících se proudů přijímaných na svých anténách. Toto oddělení závisí na prostorových charakteristikách (vlastních číslech a vlastních vektorech) přenosového kanálu. U SU-MIMO s uzavřenou smyčkou poskytuje UE zpětnou vazbu ve formě indikátoru předkodovací matice ([PMI](/mobilnisite/slovnik/pmi/)), která základnové stanici pomáhá vybrat optimální předkodovač z předdefinovaného kodebooku.

SU-MIMO je kritickou součástí přenosových schémat pro downlink i uplink. V downlinku je primární metodou pro dosažení vysokých špičkových přenosových rychlostí pro jednoho uživatele, zejména za příznivých podmínek kanálu s vysokým poměrem signálu k šumu a interferencím ([SINR](/mobilnisite/slovnik/sinr/)) a bohatým rozptylem. V uplinku umožňuje Uplink SU-MIMO vysílat z UE více proudů, čímž zvyšuje uplinkovou kapacitu. Výkon této technologie je úzce integrován s dalšími funkcemi správy rádiových zdrojů, jako je adaptivní modulace a kódování (výběr [MCS](/mobilnisite/slovnik/mcs/)), hybridní automatické opakování ([HARQ](/mobilnisite/slovnik/harq/)) a adaptace spojení. Zatímco SU-MIMO se zaměřuje na jednoho uživatele, koexistuje s Multi-User MIMO (MU-MIMO), kde základnová stanice obsluhuje více uživatelů na stejných časově-frekvenčních zdrojích pomocí prostorového oddělení, přičemž SU-MIMO často představuje základní režim před zvažováním plánování MU-MIMO.

## K čemu slouží

SU-MIMO bylo zavedeno, aby řešilo základní výzvu zvyšování přenosových rychlostí a spektrální účinnosti v omezeném a drahém rádiovém spektru. Před technikami MIMO systémy spoléhaly na Single Input Single Output (SISO), které nabízely omezené přenosové rychlosti dané Shannonovou větou pro jeden kanál. Exploze poptávky po mobilních datech, hnaná smartphony a internetovými službami, si vyžádala průlom. SU-MIMO jej poskytuje využitím více antén k vytvoření paralelních prostorových kanálů, čímž efektivně násobí přenosovou rychlost bez potřeby dodatečné šířky spektrálního pásma.

Vznik SU-MIMO byl motivován teoretickými pokroky v teorii informace, zejména prací o kapacitě MIMO od Telatara a Foschiniho, která ukázala, že kapacita může růst lineárně s minimálním počtem antén. 3GPP standardizovalo SU-MIMO v LTE Release 8/9, aby splnilo požadavky IMT-Advanced pro 4G, které stanovily významné zisky v špičkové spektrální účinnosti. Vyřešilo problém, jak poskytovat vysokorychlostní datové služby, jako je mobilní video a broadband, spektrálně účinným způsobem. Zatímco dřívější koncepty existovaly, integrace SU-MIMO do praktického standardu mobilních sítí zahrnovala řešení složitých implementačních výzev, jako je odhad kanálu, režie zpětné vazby a složitost přijímače.

SU-MIMO také položilo základy pro pokročilejší víceanténní techniky. Vytvořilo nezbytný rámec pro zpětnou vazbu o kanálu (CQI, PMI, RI), návrh referenčních signálů (CSI-RS) a řídicí signalizaci, která později umožnila MU-MIMO a massive MIMO. Jeho účel se vyvinul od poskytování vylepšení špičkové rychlosti také ke zlepšení spolehlivosti a pokrytí prostřednictvím režimů vysílací diverzity (podmnožiny MIMO). V podstatě SU-MIMO transformovalo fyzickou vrstvu z jednorozměrného (čas/frekvence) systému na vícerozměrný (čas/frekvence/prostor), čímž odemklo řádově vyšší datové kapacity pro mobilní sítě.

## Klíčové vlastnosti

- Prostorové multiplexování více datových proudů pro jednoho uživatele
- Využití více vysílacích a přijímacích antén
- Provoz s uzavřenou smyčkou se zpětnou vazbou od UE (PMI, RI, CQI)
- Předkódování založené na kodeboocích pro řízení mezistreamových interferencí
- Dynamická adaptace hodnosti na základě podmínek kanálu
- Integrace s adaptivní modulací a kódováním (AMC) a HARQ

## Související pojmy

- [MU-MIMO – Multi-User Multiple Input Multiple Output](/mobilnisite/slovnik/mu-mimo/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements
- **TR 36.912** (Rel-19) — TR on LTE-Advanced (Further E-UTRA)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.838** (Rel-17) — Study on XR Evaluations for NR

---

📖 **Anglický originál a plná specifikace:** [SU-MIMO na 3GPP Explorer](https://3gpp-explorer.com/glossary/su-mimo/)
