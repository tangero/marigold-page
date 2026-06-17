---
slug: "cinr"
url: "/mobilnisite/slovnik/cinr/"
type: "slovnik"
title: "CINR – Carrier to Interference-plus-Noise Ratio"
date: 2025-01-01
abbr: "CINR"
fullName: "Carrier to Interference-plus-Noise Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cinr/"
summary: "CINR je klíčová metrika kvality rádiového spoje, která měří poměr výkonu požadovaného signálu ke kombinovanému výkonu rušení a šumu. Poskytuje komplexnější hodnocení stavu kanálu než tradiční SNR (Sig"
---

CINR je poměr výkonu požadovaného signálu ke kombinovanému výkonu rušení a šumu. Slouží jako klíčová metrika pro hodnocení kvality kanálu v mobilních sítích.

## Popis

Carrier to Interference-plus-Noise Ratio (CINR) je základní měření na fyzické vrstvě, které kvantifikuje kvalitu rádiového komunikačního kanálu porovnáním výkonu požadovaného nosného signálu s kombinovaným výkonem všech rušivých signálů a tepelného šumu. Na rozdíl od poměru signál-šum (Signal-to-Noise Ratio, SNR), který uvažuje pouze tepelný šum, CINR zahrnuje jak složku šumu, tak rušení, což je zvláště relevantní pro mobilní sítě, kde je ko-kanálové a sousední-kanálové rušení významným faktorem. Měření se obvykle vyjadřuje v decibelech (dB) a počítá se jako CINR = P_c / (P_i + P_n), kde P_c je výkon nosné, P_i je výkon rušení a P_n je výkon šumu.

V systémech 3GPP se měření CINR provádí jak na straně uživatelského zařízení (UE), tak na straně základnových stanic (eNodeB/gNB) jako součást reportování informace o stavu kanálu (Channel State Information, [CSI](/mobilnisite/slovnik/csi/)). UE měří CINR na referenčních signálech, jako jsou buňkově specifické referenční signály (Cell-Specific Reference Signals, [CRS](/mobilnisite/slovnik/crs/)) v LTE nebo bloky synchronizačních signálů (Synchronization Signal Blocks, SSB) a referenční signály pro informaci o stavu kanálu (Channel State Information Reference Signals, [CSI-RS](/mobilnisite/slovnik/csi-rs/)) v 5G NR. Tato měření jsou hlášena síti prostřednictvím standardizovaných měřicích reportů, které typicky zahrnují jak širokopásmové, tak subpásmové hodnoty CINR. Síť tyto reporty využívá k rozhodování v oblasti správy rádiových zdrojů, včetně výběru adaptivního schématu modulace a kódování (Modulation and Coding Scheme, [MCS](/mobilnisite/slovnik/mcs/)), úprav řízení výkonu a strategií koordinace rušení.

Architektura pro měření CINR zahrnuje více komponent napříč fyzickou vrstvou a vyššími vrstvami. Na fyzické vrstvě přijímač provádí zpracování signálu za účelem oddělení požadovaného signálu od rušení a šumu, přičemž využívá techniky jako odhad kanálu, ekvalizaci a potlačení rušení. Naměřené hodnoty CINR jsou následně zpracovány filtračními algoritmy vrstvy 1 před nahlášením vyšším vrstvám. Ve vrstvě řízení rádiových zdrojů (Radio Resource Control, [RRC](/mobilnisite/slovnik/rrc/)) procedury konfigurace měření a reportování definují, kdy a jak jsou měření CINR spouštěna, filtrována a hlášena síti. Síť může konfigurovat měřicí mezery (measurement gaps), periody reportování a eventově spouštěné reportování na základě prahových hodnot CINR.

CINR hraje klíčovou roli v několika síťových funkcích nad rámec základní adaptace spoje. Pro správu mobility se měření CINR používají jako vstup pro rozhodování o předání hovoru (handover), zejména ve scénářích s výrazným mezibuněčným rušením. Ve scénářích agregace nosných (carrier aggregation) měření CINR pomáhají rozhodovat, které komponentní nosné aktivovat nebo deaktivovat na základě jejich kvality. Pro systémy massive [MIMO](/mobilnisite/slovnik/mimo/) měření CINR informují o rozhodnutích správy svazků (beam management), pomáhajíce vybrat optimální váhy pro formování svazku. Metrika také podporuje pokročilé funkce, jako je koordinovaný vícebodový přenos (Coordinated Multipoint transmission, CoMP), při kterém více buněk koordinuje své přenosy za účelem zlepšení CINR na okraji buňky.

Z implementační perspektivy závisí přesnost měření CINR na několika faktorech, včetně návrhu přijímače, algoritmů odhadu rušení a měřicí šířky pásma. Moderní přijímače využívají pokročilé techniky odhadu rušení, které dokážou rozlišit mezi různými typy rušení (ko-kanálové, sousední-kanálové, mezi-symbolové atd.). Měření se typicky provádí na specifických zdrojových prvcích (resource elements) nesoucích referenční signály, přičemž výsledky jsou průměrovány v časové a frekvenční doméně za účelem snížení rozptylu měření. V 5G NR zavedení flexibilnějších vzorů referenčních signálů a měření založených na svazcích učinilo měření CINR složitějším, ale také přesnějším v zachycení skutečných podmínek kanálu, které zažívá UE.

## K čemu slouží

CINR bylo zavedeno, aby řešilo omezení tradičních měření poměru signál-šum (Signal-to-Noise Ratio, SNR) v rušením limitovaných mobilních prostředích. V raných mobilních systémech byl tepelný šum často dominantní poruchou, což činilo SNR dostatečnou metrikou pro hodnocení kvality spoje. Jak se však mobilní sítě vyvíjely s opakovaným využíváním frekvencí a vyššími hustotami uživatelů, stalo se rušení ze sousedních buněk významným faktorem ovlivňujícím výkon. Měření SNR nedokázala zachytit tuto složku rušení, což vedlo k neoptimálním rozhodnutím v adaptaci spoje, předávání hovoru a přidělování zdrojů. CINR se objevilo jako komplexnější metrika, která přesněji odráží skutečné podmínky kanálu, které uživatelé zažívají ve scénářích dominovaných rušením.

Vytvoření CINR bylo motivováno potřebou přesnější správy rádiových zdrojů v systémech 3GPP, zejména při přechodu sítí na technologie založené na [OFDMA](/mobilnisite/slovnik/ofdma/), jako je LTE. V systémech OFDMA, kde jsou frekvenční zdroje sdíleny mezi více uživateli, se přesné měření rušení stává kritickým pro rozhodování o plánování a koordinaci rušení. CINR poskytuje síťovým operátorům realistické hodnocení kvality spoje, které zohledňuje jak šum, tak rušení, což umožňuje efektivnější využití rádiových zdrojů. To bylo zvláště důležité pro implementaci pokročilých funkcí, jako je částečné frekvenční opakované využití (fractional frequency reuse), mezibuněčná koordinace rušení (Inter-Cell Interference Coordination, [ICIC](/mobilnisite/slovnik/icic/)) a vylepšená mezibuněčná koordinace rušení (enhanced ICIC, eICIC) v heterogenních sítích.

CINR také řeší požadavky moderních mobilních sítí, které fungují v stále složitějších prostředích s rušením. S nasazením malých buněk (small cells), agregací nosných a víceanténních systémů se vzorce rušení staly dynamičtějšími a prostorově variabilnějšími. Tradiční metriky, jako je indikátor síly přijímaného signálu (Received Signal Strength Indicator, RSSI) nebo výkon přijímaného referenčního signálu (Reference Signal Received Power, RSRP), poskytují informace o síle signálu, ale ne o jeho kvalitě. CINR tuto mezeru zaplňuje kvantifikací toho, jak moc signál vystupuje nad šum i rušení, což jej činí nezbytným pro rozhodování založená na kvalitě, nikoli pouze na síle. To se stává stále důležitějším pro udržení kvality služeb v hustých městských nasazeních a pro podporu aplikací citlivých na latenci, které vyžadují spolehlivý odhad kvality spoje.

## Klíčové vlastnosti

- Komplexní hodnocení kvality kanálu kombinující složky rušení i šumu
- Nezbytný vstup pro výběr adaptivního schématu modulace a kódování (MCS)
- Kritická metrika pro rozhodování o předání hovoru (handover) v rušením limitovaných scénářích
- Podporuje techniky koordinace rušení, jako je ICIC a eICIC
- Umožňuje přesnou správu svazků (beam management) v systémech massive MIMO
- Poskytuje přidělování zdrojů založené na kvalitě pro zlepšení spektrální účinnosti

## Související pojmy

- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)

## Definující specifikace

- **TR 45.903** (Rel-19) — SAIC Feasibility Study for GSM Networks

---

📖 **Anglický originál a plná specifikace:** [CINR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cinr/)
