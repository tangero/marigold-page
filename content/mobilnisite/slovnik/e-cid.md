---
slug: "e-cid"
url: "/mobilnisite/slovnik/e-cid/"
type: "slovnik"
title: "E-CID – Enhanced Cell-ID"
date: 2025-01-01
abbr: "E-CID"
fullName: "Enhanced Cell-ID"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-cid/"
summary: "Síťová metoda určování polohy v LTE a 5G NR, která vylepšuje základní Cell-ID začleněním dalších rádiových měření. Odhaduje polohu UE pomocí identity obsluhující buňky kombinované s časovým předstihem"
---

E-CID je síťová metoda určování polohy pro LTE a 5G NR, která zlepšuje přesnost lokalizace kombinací identity obsluhující buňky s dalšími rádiovými měřeními, jako je časový předstih nebo síla signálu.

## Popis

Enhanced Cell-ID (E-CID) je standardizovaná metodika určování polohy od 3GPP pro LTE (od Release 9 dále) pokračující i v 5G NR. Spadá do kategorie síťového určování polohy, kde odhad polohy provádí síť pomocí měření provedených samotnou sítí, UE nebo obojím. Zatímco základní Cell-ID lokalizace prostě vrací zeměpisné souřadnice antény obsluhující buňky, E-CID tento odhad zpřesňuje začleněním dalších měření rádiových prostředků, aby určil přesnější polohu.

Architektura zahrnuje několik klíčových síťových prvků: UE, evolved Node B ([eNB](/mobilnisite/slovnik/enb/)) nebo next-generation Node B (gNB) a Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G Core. Proces určování polohy je typicky zahájen požadavkem služby lokalizace. E-SMLC/LMF funguje jako lokalizační server, který koordinuje proceduru. Vyžádá si konkrétní měření od UE a/nebo eNB/gNB. Mezi běžná měření používaná v E-CID patří Received Signal Strength Indicator (RSSI) a Reference Signal Received Power (RSRP) UE od více detekovaných buněk, vysílací časový předstih (TA) UE pro obsluhující buňku a potenciálně měření úhlu příchodu (AoA) provedená základnovou stanicí.

Jak to funguje: Základním principem je multilaterace nebo porovnávání vzorů signálu. Serving Cell-ID poskytuje hrubou polohu (v rámci pokrytí buňky). Měření časového předstihu (TA), které odpovídá zpoždění obousměrného přenosu mezi UE a základnovou stanicí, definuje radiální vzdálenost, čímž umisťuje UE na kružnici kolem místa buňky. Měření síly signálu (RSRP/RSSI) od obsluhující a sousedních buněk poskytují odhad vzdálenosti založený na modelech útlumu na dráze a relativní úrovně signálu mohou pomoci triangulovat polohu UE. Pokud je k dispozici AoA, poskytuje směrovou přímku od základnové stanice. E-SMLC/LMF spojuje tato nedokonalá a někdy protichůdná měření pomocí algoritmů (např. metoda nejmenších čtverců, porovnávání vzorů s databázemi RF otisků) k výpočtu odhadu zeměpisné šířky/délky a přidružené elipsy nejistoty.

Její role v síti je poskytovat spolehlivé řešení určování polohy se střední přesností, které vyvažuje výkon, náklady a složitost. Na rozdíl od satelitních metod ([GNSS](/mobilnisite/slovnik/gnss/)), které mohou selhat uvnitř budov, E-CID funguje všude, kde je dostupné pokrytí mobilní sítí. Nevyžaduje žádný dodatečný hardware v UE mimo standardní schopnosti celulárního modemu. Slouží kritickým případům užití, jako je lokalizace volajícího při tísňovém volání (E911/E112), služby založené na poloze, optimalizace sítě a sledování IoT aktiv. Ačkoli není tak přesná jako [OTDOA](/mobilnisite/slovnik/otdoa/) nebo GNSS na otevřeném prostranství, její všudypřítomnost a nižší signalizační režie z ní činí klíčovou součást hybridní strategie určování polohy.

## K čemu slouží

E-CID byl vyvinut k řešení nedostatečné přesnosti základního Cell-ID určování polohy, které dokázalo lokalizovat uživatele pouze v rámci celé oblasti pokrytí buňky – často o poloměru několika kilometrů. To bylo nedostačující pro regulatorní požadavky, jako jsou tísňové služby (např. požadavky [FCC](/mobilnisite/slovnik/fcc/) E911), a pro komerční služby založené na poloze, které potřebovaly vyšší podrobnost. Průmysl potřeboval metodu, která by využívala stávající síťovou infrastrukturu a schopnosti UE bez nutnosti zavádět nový hardware, jako jsou přijímače [GPS](/mobilnisite/slovnik/gps/) v každém telefonu.

Jeho vytvoření v LTE Release 9 bylo motivováno potřebou standardizované, vylepšené síťové metody určování polohy při zavádění LTE sítí. Předchozí metody ve 2G/3G, jako časový předstih a síla signálu, byly specifické pro dodavatele nebo nebyly pro lokalizaci plně standardizovány. E-CID sjednotil tato měření do jednotného, interoperabilního rámce. Vyřešil problém poskytnutí „záložní“ nebo doplňkové lokalizační technologie, když nejsou dostupné satelitní signály (uvnitř budov, městské kaňony), a poskytl nákladově efektivní řešení pro lokalizaci zařízení bez [GNSS](/mobilnisite/slovnik/gnss/) schopností, jako jsou mnohé IoT senzory.

Navíc E-CID umožnil sofistikovanější plánování a optimalizaci sítě. Shromažďováním velkého množství měřicích dat od UE mohli operátoři vytvářet podrobné mapy rádiového prostředí, identifikovat díry v pokrytí a optimalizovat parametry přechodu mezi buňkami. Také položil základy pro pokročilejší hybridní techniky, kde by data E-CID mohla být kombinována s jinými metodami (např. senzorová data z UE) pro další zlepšení přesnosti – koncept, který se vyvinul do hybridních lokalizačních funkcí 5G.

## Klíčové vlastnosti

- Vylepšuje základní Cell-ID měřeními časového předstihu a síly signálu
- Síťová metoda, nevyžadující GNSS v UE
- Poskytuje odhady polohy i v prostředí bez GNSS (uvnitř budov)
- Podporuje splnění požadavků pro tísňové služby (E911/E112) jako záložní řešení
- Využívá standardizovaná měření (RSRP, RSRQ, TA, AoA)
- Umožňuje hybridní určování polohy kombinací s jinými metodami

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 33.814** (Rel-16) — Security aspects of enhanced Location Services (eLCS)
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 36.455** (Rel-19) — LTE Positioning Protocol Annex (LPPa)
- **TS 36.809** (Rel-12) — Study on RF Pattern Matching for LTE Positioning
- **TS 37.320** (Rel-19) — Minimization of Drive Tests (MDT) Overview
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [E-CID na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-cid/)
