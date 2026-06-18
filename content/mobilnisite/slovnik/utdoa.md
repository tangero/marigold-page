---
slug: "utdoa"
url: "/mobilnisite/slovnik/utdoa/"
type: "slovnik"
title: "UTDOA – Uplink Time Difference of Arrival"
date: 2025-01-01
abbr: "UTDOA"
fullName: "Uplink Time Difference of Arrival"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/utdoa/"
summary: "Síťová metoda určování polohy, při které více základnových stanic měří čas příchodu vzestupných signálů od uživatelského zařízení (UE). Časové rozdíly mezi těmito měřeními se používají k výpočtu poloh"
---

UTDOA je síťová metoda určování polohy, při které více základnových stanic měří časové rozdíly příchodu (TDOA) vzestupných signálů od uživatelského zařízení (UE) k výpočtu jeho polohy pomocí hyperbolické trilaterace.

## Popis

Uplink Time Difference of Arrival (UTDOA) je síťová lokalizační technologie standardizovaná konsorciem 3GPP. Na rozdíl od metod založených na UE, jako je Assisted [GNSS](/mobilnisite/slovnik/gnss/) ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), provádí UTDOA všechna měření v rámci síťové infrastruktury. Základní princip spočívá v hyperbolické trilateraci. Když uživatelské zařízení (UE) vysílá vzestupný signál – například Sounding Reference Signal ([SRS](/mobilnisite/slovnik/srs/)) nebo preambuli kanálu Physical Random Access Channel ([PRACH](/mobilnisite/slovnik/prach/)) – tento signál detekuje více geograficky rozptýlených základnových stanic ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR) nebo specializovaných jednotek Location Measurement Unit ([LMU](/mobilnisite/slovnik/lmu/)). Každý přijímací uzel zaznamená přesný čas příchodu ([TOA](/mobilnisite/slovnik/toa/)) signálu.

Tato nezpracovaná měření TOA jsou následně odeslána do centrálního síťového uzlu zvaného Enhanced Serving Mobile Location Center ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE nebo Location Management Function (LMF) v 5GC. E-SMLC/LMF zná přesné, synchronizované zeměpisné souřadnice a časování každé přijímající základnové stanice. Vypočítá časový rozdíl příchodu (TDOA) mezi dvojicemi přijímačů (např. rozdíl mezi TOA na základnové stanici A a základnové stanici B). Každá hodnota TDOA definuje hyperbolickou čáru (nebo křivku ve 3D), na které se musí UE nacházet, protože konstantní časový rozdíl odpovídá konstantnímu rozdílu vzdálenosti od dvou základnových stanic. Použitím měření TDOA z alespoň tří nebo čtyř základnových stanic vzhledem k referenčnímu přijímači může E-SMLC/LMF vypočítat průsečík těchto hyperbolických křivek, čímž odhadne 2D nebo 3D polohu UE.

Přesnost UTDOA závisí na několika kritických faktorech. Za prvé musí být přijímající základnové stanice těsně synchronizovány, obvykle pomocí GPS nebo síťové synchronizace jako IEEE 1588v2, aby byla zajištěna srovnatelnost měření TOA. Za druhé, geometrie přijímacích míst (jejich vzájemná poloha) výrazně ovlivňuje přesnost; je vyžadována dobrá geometrická ztráta přesnosti (GDOP). Za třetí, systém musí zvládat mnohocestné šíření, kdy signály přicházejí přes více odražených cest, což může zkreslit měření TOA přímé cesty. Pro zvýšení robustnosti se v E-SMLC/LMF používají pokročilé algoritmy, jako je potlačení mnohocestnosti a fúze dat. UTDOA je zvláště účinná v městském a vnitřním prostředí, kde jsou signály GNSS slabé nebo nedostupné, protože spoléhá na vlastní infrastrukturu mobilní sítě.

## K čemu slouží

UTDOA byla vyvinuta za účelem splnění regulatorních požadavků na lokalizaci volajících v nouzi (např. E911 v USA, E112 v Evropě) a pro umožnění komerčních lokalizačních služeb (LBS) ve scénářích, kde metody založené na GNSS selhávají. Jejím primárním účelem je poskytnout spolehlivé, síťově řízené lokalizační řešení, které nezávisí na schopnostech uvnitř UE. To je klíčové pro lokalizaci starších zařízení, levných IoT senzorů bez GNSS přijímače nebo UE pracujících uvnitř budov nebo v městských kaňonech, kde jsou satelitní signály blokovány.

Historicky poskytovaly dřívější síťové metody, jako je Cell-ID, velmi hrubou přesnost (stovky metrů až kilometry). UTDOA tuto limitaci řešila tím, že nabízela mnohem vyšší přesnost, typicky v rozsahu 50 metrů nebo lepší v závislosti na hustotě nasazení a podmínkách signálu. Vyřešila problém lokalizace jakéhokoli zařízení, které dokáže vysílat vzestupný signál, čímž se stala univerzální záložní nebo doplňkovou technologií. Její vznik byl motivován potřebou standardizované, interoperabilní metody, kterou by bylo možné nasadit v sítích více dodavatelů.

UTDOA navíc poskytuje z pohledu UE pasivní metodu určování polohy. UE není pro UTDOA vyžadováno provádět žádná speciální měření nebo výpočty, což šetří její životnost baterie – což je významná výhoda pro IoT aplikace. Pro síťového operátora představuje nástroj pro sledování majetku, optimalizaci sítě a detekci podvodů. V 5G, s jeho podporou pro massive IoT a kritické komunikace, byla role UTDOA posílena, aby podporovala nové případy užití vyžadující střední přesnost určení polohy s nízkou složitostí zařízení.

## Klíčové vlastnosti

- Síťové určování polohy nevyžadující úpravy na straně UE ani GNSS přijímač
- Využívá hyperbolickou trilateraci založenou na měřeních časového rozdílu příchodu (TDOA)
- Závisí na přesné časové synchronizaci mezi více základnovými stanicemi nebo LMU
- Pro měření typicky využívá vzestupné referenční signály jako SRS nebo PRACH
- Centralizovaný výpočet polohy prováděný jednotkou E-SMLC (LTE) nebo LMF (5G)
- Účinná v prostředích bez přístupu k GNSS, jako jsou vnitřní prostory a hustě zastavěné městské oblasti

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 36.111** (Rel-19) — LMU Requirements for UTDOA Positioning
- **TS 36.112** (Rel-19) — E-UTRAN LMU Conformance Requirements
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- **TS 36.456** (Rel-19) — SLm Interface Introduction
- **TS 36.458** (Rel-19) — SLm Interface Signalling Transport
- **TS 36.459** (Rel-19) — SLmAP for E-UTRAN Positioning
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [UTDOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/utdoa/)
