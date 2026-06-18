---
slug: "csi-sinr"
url: "/mobilnisite/slovnik/csi-sinr/"
type: "slovnik"
title: "CSI-SINR – CSI Signal-to-Interference-plus-Noise Ratio"
date: 2025-01-01
abbr: "CSI-SINR"
fullName: "CSI Signal-to-Interference-plus-Noise Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/csi-sinr/"
summary: "CSI-SINR je metrika kvality kanálu, kterou UE hlásí gNB v 5G NR. Kvantifikuje poměr výkonu požadovaného signálu k výkonu interference plus šumu na referenčních signálech CSI, což umožňuje přesná rozho"
---

CSI-SINR je metrika kvality kanálu hlášená UE, která kvantifikuje poměr výkonu požadovaného signálu k výkonu interference plus šumu na referenčních signálech CSI, což umožňuje adaptaci spojení a plánování v 5G NR.

## Popis

CSI-SINR (Channel State Information Signal-to-Interference-plus-Noise Ratio) je základní měření fyzické vrstvy definované v 3GPP TS 38.214 pro 5G New Radio (NR). Představuje kvalitu rádiového kanálu, kterou zažívá uživatelské zařízení (UE) na specifických zdrojích referenčního signálu [CSI](/mobilnisite/slovnik/csi/) ([CSI-RS](/mobilnisite/slovnik/csi-rs/)). Na rozdíl od tradičních měření [SINR](/mobilnisite/slovnik/sinr/), která mohou zvažovat všechny přijímané signály, CSI-SINR konkrétně měří kvalitu referenčních signálů pro informace o stavu kanálu, které jsou přesně známy jak vysílači, tak přijímači. Toto cílené měření poskytuje gNodeB (gNB) přesné informace o podmínkách kanálu, které ovlivní přenos dat, což umožňuje přesný výběr schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) a přidělování zdrojů.

Proces měření začíná vysíláním zdrojů CSI-RS nakonfigurovaných pro UE gNB prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/). Tyto referenční signály jsou vloženy na specifické časově-frekvenční pozice v rámci mřížky zdrojů podle nakonfigurovaného vzoru CSI-RS. UE přijímá tyto známé referenční signály spolu s interferencí ze sousedních buněk a šumem z různých zdrojů. Řetězec zpracování fyzické vrstvy UE provede odhad kanálu pomocí přijatého CSI-RS a následně vypočítá poměr výkonu požadovaného signálu (z CSI-RS obslužné buňky) ke kombinovanému výkonu interference (z přenosů jiných buněk ve stejných zdrojích) a tepelného šumu. Tento výpočet následuje specifické algoritmy definované ve standardu, aby bylo zajištěno konzistentní měření napříč různými implementacemi UE.

Výsledná hodnota CSI-SINR je kvantována a hlášena zpět gNB jako součást rámce zpětné vazby CSI. Tato zpětná vazba může být periodická, semi-perzistentní nebo aperiodická v závislosti na nakonfigurovaném režimu hlášení. Plánovač gNB používá tuto informaci CSI-SINR spolu s dalšími metrikami, jako je [CQI](/mobilnisite/slovnik/cqi/) (Channel Quality Indicator) a [RI](/mobilnisite/slovnik/ri/) (Rank Indicator), k přijímání kritických rozhodnutí o parametrech přenosu. Tato rozhodnutí zahrnují výběr vhodného MCS pro maximalizaci propustnosti při zachování přijatelných chybových poměrů bloků, stanovení optimálního přenosového ranku pro [MIMO](/mobilnisite/slovnik/mimo/) operace a přidělování bloků fyzických zdrojů (PRB) různým UE na základě jejich podmínek kanálu.

Z architektonického hlediska měření a hlášení CSI-SINR zahrnuje koordinaci mezi měřicími funkcemi fyzické vrstvy UE a mechanismy hlášení vyšších vrstev. Měření je prováděno v řetězci RF a základního pásma UE, zatímco hlášení je zpracováváno prostřednictvím UCI (Uplink Control Information) na kanálech PUCCH nebo PUSCH. Vrstva MAC gNB tyto hlášení přijímá a zpracovává, aby informovala rozhodnutí plánování. Tento uzavřený smyčkový mechanismus zpětné vazby je nezbytný pro adaptivní přenosová schémata 5G NR, zejména v náročných rádiových prostředích s významnou interferencí nebo ve scénářích mobility, kde se podmínky kanálu rychle mění.

## K čemu slouží

CSI-SINR bylo zavedeno v 5G NR Release 15, aby řešilo omezení jednodušších metrik kvality kanálu používaných v předchozích generacích, jako je LTE. V LTE poskytoval CQI hrubou indikaci kvality kanálu, ale explicitně neodděloval interferenci od šumu a neposkytoval granularitu potřebnou pro pokročilejší přenosová schémata 5G. 5G NR funguje v různých pásmech spektra (včetně mmWave) s komplexními scénáři interference z beamformingu, massive MIMO a zhušťování sítě, což vyžaduje přesnější informace o kvalitě kanálu pro optimální výkon.

Primární problém, který CSI-SINR řeší, je poskytnutí přesných informací o kvalitě kanálu s ohledem na interferenci, aby bylo možné inteligentní adaptaci spojení. Bez přesné znalosti SINR musí gNB buď používat konzervativní výběr MCS (plýtvání spektrální účinností), nebo agresivní výběr MCS (způsobující vysoké chybové poměry a retransmise). CSI-SINR dává plánovači explicitní znalost podmínek interference, což mu umožňuje rozlišit mezi scénáři omezenými šumem a scénáři omezenými interferencí a podle toho přizpůsobit přenosové parametry. To je obzvláště důležité v sítích 5G, kde techniky koordinovaného vícebodového přenosu (CoMP), dynamického sdílení spektra a koordinace interference vyžadují podrobné porozumění vzorcům interference.

Historicky se dřívější systémy spoléhaly na metriky jako RSRP a RSRQ, které poskytovaly indikace síly a kvality signálu, ale nebyly optimalizovány pro pokročilé přenosové techniky v 5G. Vytvoření CSI-SINR bylo motivováno potřebou metriky, která konkrétně měří kvalitu referenčních signálů používaných pro informace o stavu kanálu, což přímo ovlivňuje přesnost předkódování, beamformingu a výběru MIMO vrstev. Poskytnutím poměru interference plus šumu konkrétně na zdrojích CSI-RS umožňuje přesnější predikci výkonu přenosu dat, než by mohly poskytnout obecné metriky kvality signálu.

## Klíčové vlastnosti

- Měří SINR konkrétně na zdrojích referenčního signálu CSI
- Umožňuje přesnou adaptaci spojení a výběr MCS
- Podporuje rozhodování plánování s ohledem na interferenci
- Funguje s periodickými, semi-perzistentními a aperiodickými režimy hlášení
- Integruje se s rámcem zpětné vazby CSI 5G NR
- Nezbytné pro optimalizaci výkonu massive MIMO a beamformingu

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data

---

📖 **Anglický originál a plná specifikace:** [CSI-SINR na 3GPP Explorer](https://3gpp-explorer.com/glossary/csi-sinr/)
