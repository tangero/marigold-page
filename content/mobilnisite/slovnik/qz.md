---
slug: "qz"
url: "/mobilnisite/slovnik/qz/"
type: "slovnik"
title: "QZ – Quiet Zone"
date: 2025-01-01
abbr: "QZ"
fullName: "Quiet Zone"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/qz/"
summary: "Tichá zóna (Quiet Zone) je vyhrazený časově-frekvenční zdroj v rámci rádiového rámce, kde základnová stanice (gNB) dočasně přeruší nebo sníží vysílání. To umožňuje přesná měření rádiového prostředí, j"
---

QZ (tichá zóna) je vyhrazený časově-frekvenční zdroj, kde základnová stanice dočasně přeruší nebo sníží vysílání, aby umožnila přesná měření rádiového prostředí odstraněním vlastního maskujícího signálu.

## Popis

Tichá zóna (Quiet Zone, QZ) je klíčový koncept v sítích 5G New Radio (NR) a LTE-Advanced pro usnadnění pokročilých rádiových měření. Je definována jako nakonfigurovaná sada zdrojových prvků (konkrétní [OFDM](/mobilnisite/slovnik/ofdm/) symboly a subnosné) v rámci downlink rádiového rámce, kde obsluhující základnová stanice (gNB v NR, [eNB](/mobilnisite/slovnik/enb/) v LTE) záměrně utlumí nebo výrazně sníží svůj vysílací výkon. Tím vznikne časová a spektrální 'díra' ve vlastním vysílání buňky, což umožňuje uživatelskému zařízení (UE) provádět čistá měření na jiných signálech, které by za normálních okolností byly přehlušeny silným downlinkem obsluhující buňky.

Konfigurace Tiché zóny je signalizována sítí směrem k UE prostřednictvím zpráv řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)). Konfigurace specifikuje parametry jako periodicita, doba trvání a frekvenční umístění QZ. Například může být nakonfigurována tak, aby se vyskytovala v konkrétních podrámcích a v určitých blocích fyzických zdrojů ([PRB](/mobilnisite/slovnik/prb/)). Během těchto nakonfigurovaných intervalů QZ může gNB vysílat pouze nezbytné signály definující buňku, jako je primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)) a sekundární synchronizační signál ([SSS](/mobilnisite/slovnik/sss/)) se sníženým výkonem, nebo nemusí vysílat vůbec nic, v závislosti na typu QZ.

Primárním technickým využitím Tiché zóny je umožnit přesné měření časového rozdílu referenčního signálu ([RSTD](/mobilnisite/slovnik/rstd/)) pro určování polohy metodou pozorovaného časového rozdílu příchodu ([OTDOA](/mobilnisite/slovnik/otdoa/)). Pro OTDOA měří UE časový rozdíl mezi signály přijatými z obsluhující buňky a z více sousedních buněk. Signál ze vzdálené sousední buňky je ve srovnání se silným signálem místní obsluhující buňky velmi slabý. Utlumením obsluhující buňky v QZ může přijímač UE detekovat a přesně měřit tyto slabé referenční signály pro určování polohy (PRS) od sousedů bez rušení. Podobně se QZ používají pro měření řízení rádiových zdrojů (RRM), jako jsou měření objevovacích signálů ve scénářích s nespojitým vysíláním (DTX), a pro koexistenci v rámci zařízení (IDC), aby mohlo UE snímání jiných rádiových technologií (např. Wi-Fi, GNSS) bez vlastního rušení od LTE/NR.

## K čemu slouží

Mechanismus Tiché zóny byl zaveden, aby vyřešil 'problém slyšitelnosti' v celulárních sítích, zejména pro určování polohy a pokročilou mobilitu. V hustých celulárních nasazeních je UE typicky velmi blízko své obsluhující buňky, jejíž downlink signál je řádově silnější než signály z ostatních buněk, které jsou pro měření klíčové. Tento silný signál působí jako maska, takže přijímač UE nemůže detekovat a přesně měřit slabší referenční signály ze vzdálených základnových stanic. To vážně snižovalo přesnost technik určování polohy, jako je OTDOA, které spoléhají na přesná časová měření z více buněk.

Před standardizovanými QZ bylo síťově asistované určování polohy méně přesné, zejména pro UE ve výhodných podmínkách obsluhující buňky (např. poblíž středu buňky). Vytvoření Tiché zóny tento problém přímo řeší tím, že poskytuje řízené okno bez rušení. Koncept se vyvinul z dřívějších technik LTE, jako jsou téměř prázdné podrámce (ABS) používané pro rozšířené koordinaci mezibuněčného rušení (eICIC), ale QZ jsou přesněji cíleny pro účely měření spíše než pro obecné potlačení rušení pro data.

V 5G NR je potřeba QZ ještě výraznější kvůli použití vyšších frekvenčních pásem (mmWave) s beamformingem a přísným požadavkům na přesnost pro nové případy užití, jako je průmyslový IoT a komunikace vozidlo se vším (V2X). QZ umožňují spolehlivou detekci paprsků sousedních buněk a zlepšují výkon síťových služeb určování polohy, které jsou nezbytné pro aplikace, jako je určování polohy pro tísňová volání, sledování majetku a rozšířená realita. Představují kooperativní chování sítě, kdy buňka dočasně a řízeně obětuje část své kapacity, aby umožnila funkce prospěšné pro celý systém, které přinášejí užitek UE a provozní inteligenci sítě.

## Klíčové vlastnosti

- Konfigurovatelné utlumení vysílání obsluhující buňky ve specifických časově-frekvenčních zdrojích
- Umožňuje přesné měření slabých signálů ze vzdálených buněk pro určování polohy (např. OTDOA)
- Signalizováno směrem k UE prostřednictvím RRC konfigurace specifikující periodicitu, dobu trvání a šířku pásma
- Podporuje různé typy, včetně vzorů utlumení s nulovým výkonem a se sníženým výkonem
- Klíčové pro řešení 'problému slyšitelnosti' v hustých nasazeních sítě
- Používá se pro měření RRM, objevovací signály a scénáře koexistence v rámci zařízení

## Definující specifikace

- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.161** (Rel-19) — NR UE TRP and TRS Requirements for FR1
- **TS 38.561** (Rel-19) — UE Conformance for TRP/TRS FR1
- **TR 38.834** (Rel-17) — NR FR1 TRP/TRS Test Methodology
- **TS 38.870** (Rel-19) — Enhanced OTA Test Methods for NR FR1 TRP/TRS
- **TR 38.884** (Rel-18) — Technical Report
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [QZ na 3GPP Explorer](https://3gpp-explorer.com/glossary/qz/)
