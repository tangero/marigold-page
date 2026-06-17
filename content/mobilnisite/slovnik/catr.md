---
slug: "catr"
url: "/mobilnisite/slovnik/catr/"
type: "slovnik"
title: "CATR – Compact Antenna Test Range"
date: 2025-01-01
abbr: "CATR"
fullName: "Compact Antenna Test Range"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/catr/"
summary: "Specializovaná měřicí technika pro testování velkých antén a zařízení v kompaktním, řízeném prostředí. Vytváří rovinnou čelní vlnu pomocí reflektorů k simulaci podmínek dalekého pole, což umožňuje pře"
---

CATR (kompaktní anténní měřicí polygon) je kompaktní anténní měřicí polygon, který využívá reflektory k vytvoření rovinné čelní vlny, simulující podmínky dalekého pole pro přesná měření antén v řízeném vnitřním prostředí.

## Popis

Kompaktní anténní měřicí polygon (CATR) je sofistikovaný měřicí systém určený k hodnocení výkonu antén, zejména těch používaných v moderních bezdrátových komunikačních systémech, jako je 5G NR. Na rozdíl od tradičních polygonů dalekého pole, které vyžadují značnou fyzickou vzdálenost mezi testovanou anténou (AUT) a měřicí sondou k dosažení rovinných čelných vln, CATR využívá jeden nebo více speciálně tvarovaných reflektorů (typicky parabolických, válcových nebo systémů s dvojitým reflektorem) ke kolimaci sférických vln z napájecí antény do rovinné čelní vlny v omezené, anechoické komoře. Tato kolimovaná 'klidová zóna' je objem prostoru, kde elektromagnetické pole přibližně odpovídá rovinné vlně, což umožňuje přesná měření dalekého pole vyzařovacího diagramu, zisku, směrovosti a účinnosti AUT. Architektura systému je navržena tak, aby minimalizovala amplitudové a fázové vlnění v klidové zóně, což zajišťuje věrnost měření srovnatelnou s tradičními metodami dalekého pole.

Klíčové komponenty CATR zahrnují systém napájecí antény, který generuje počáteční sférickou vlnu; hlavní kolimační reflektory, které jsou přesně obrobeny do specifických profilů (jako jsou výseče offsetové paraboly) pro transformaci čelní vlny; anechoickou komoru, která pohlcuje odrazy a vytváří prostředí podobné volnému prostoru; a systém polohovače, který otáčí AUT pro zachycení plných sférických vyzařovacích diagramů. Napáječ je typicky umístěn v ohnisku reflektoru. Pokročilé CATR systémy mohou zahrnovat konstrukce s dvojitým reflektorem (např. Gregoriánské nebo Cassegrainovy konfigurace) pro zlepšení výkonu, snížení křížové polarizace a řízení celkové velikosti polygonu. Velikost klidové zóny je kritický parametr, určený rozměry reflektoru a provozní frekvencí, a musí být dostatečně velká, aby plně osvětlila AUT.

V kontextu 3GPP je metodologie CATR specifikována pro testování shody antén základnových stanic ([BS](/mobilnisite/slovnik/bs/)) a uživatelských zařízení (UE), zejména pro 5G New Radio (NR). Technické specifikace 3GPP (např. TS 37.141, TS 38.141) definují požadované výkonnostní metriky CATR, jako je uniformita pole v klidové zóně, amplitudový pokles a fázová odchylka, aby zajistily reprodukovatelné a přesné testování Over-the-Air ([OTA](/mobilnisite/slovnik/ota/)). Pro antény massive [MIMO](/mobilnisite/slovnik/mimo/) a beamforming, které jsou nedílnou součástí 5G, CATR umožňuje hodnocení aktivních anténních systémů ([AAS](/mobilnisite/slovnik/aas/)) v jejich provozních stavech, měření diagramů svazků, přesnosti natočení svazku a celkového vyzářeného výkonu. Technika podporuje frekvenční rozsahy od pásem pod 6 GHz až po milimetrové vlny (mmWave), ačkoli konstrukce reflektoru se na vyšších frekvencích stává náročnější kvůli přísnějším požadavkům na toleranci povrchu.

Role CATR v síťovém ekosystému je primárně ve fázích výzkumu a vývoje, certifikace a validace síťového zařízení. Umožňuje výrobcům ověřit, že anténní návrhy splňují požadavky 3GPP na radiační výkon před nasazením. Tím, že poskytuje řízené, opakovatelné testovací prostředí nezávislé na počasí a vnějších rušeních, CATR urychluje vývojové cykly a zajišťuje, že základnové stanice a zařízení fungují optimálně v reálných scénářích. Je obzvláště cenný pro testování velkých antén, jako jsou ty pro makrobuňkové základnové stanice, kde by venkovní polygony dalekého pole byly neprakticky velké. Dále CATR podporuje testování integrovaných systémů, kde nelze anténu snadno oddělit od rádiové jednotky, což umožňuje skutečnou OTA charakterizaci.

## K čemu slouží

Technologie CATR byla vyvinuta, aby řešila základní výzvu přesného měření radiačních charakteristik dalekého pole velkých antén a vysokofrekvenčních zařízení bez nutnosti nepřiměřeně velkých testovacích vzdáleností. Tradiční testování dalekého pole vyžaduje vzdálenost alespoň 2D²/λ (kde D je apertura antény a λ je vlnová délka) mezi AUT a sondou k dosažení rovinných čelných vln. Pro velké apertury nebo vysoké frekvence (např. mmWave) může tato vzdálenost dosahovat stovek metrů nebo i kilometrů, což činí venkovní polygony nákladnými, logisticky obtížnými a náchylnými k rušení prostředím, mnohocestnému šíření a bezpečnostním obavám. Vnitřní anechoické komory tradičně nemohly tyto vzdálenosti dosáhnout. CATR to řeší použitím reflektoru jako optiky ke 'stlačení' podmínky dalekého pole do kompaktního prostoru, což umožňuje přesná měření v laboratorním prostředí.

Vytvoření a standardizace CATR v rámci 3GPP bylo motivováno vývojem mobilních síťových technologií směrem k 5G a dále, který přinesl nové anténní složitosti. Zavedení massive [MIMO](/mobilnisite/slovnik/mimo/), beamformingu a provozu v mmWave spektru (FR2) učinilo validaci anténního výkonu kritičtější než kdy dříve. Tyto pokročilé antény mají elektricky velké apertury a vyžadují charakterizaci aktivních, adaptivních diagramů svazků – úkoly nevhodné pro konvenční testovací metody s kabelovým připojením nebo malé komory. CATR poskytuje potřebnou schopnost provádět plné [OTA](/mobilnisite/slovnik/ota/) testování těchto systémů, což zajišťuje, že přesnost natočení svazku, úrovně postranních laloků a celkový vyzářený výkon splňují specifikace pro účinnost sítě a koexistenci.

Historicky, před rozšířeným přijetím CATR, existovaly alternativy jako techniky transformace blízkého pole na vzdálené, ale ty zahrnují komplexní skenování a výpočetní zpracování, které může být pro velmi velká pole časově náročné a náchylné k chybám. CATR nabízí přímý přístup měření dalekého pole, čímž snižuje testovací čas a výpočetní režii. Jeho zařazení do specifikací 3GPP (počínaje Release 13 pro LTE-Advanced Pro a vyvíjející se přes 5G release) poskytlo standardizovanou, spolehlivou metodologii pro celoprůmyslové testování shody, což zajišťuje interoperabilitu a konzistenci výkonu napříč zařízeními různých výrobců při nasazování těchto pokročilých anténních technologií.

## Klíčové vlastnosti

- Generuje rovinné čelní vlny v kompaktní klidové zóně pomocí tvarovaných reflektorů
- Umožňuje měření antén v dalekém poli pro velké apertury bez nutnosti rozsáhlé vzdálenosti
- Podporuje testování aktivních anténních systémů (AAS) a beamformingových diagramů Over-the-Air
- Funguje v širokých frekvenčních pásmech včetně pásem pod 6 GHz a milimetrových vln
- Poskytuje řízené, opakovatelné prostředí bez venkovního rušení
- Standardizován v 3GPP pro testování shody základnových stanic a zařízení

## Definující specifikace

- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TS 38.817** — 3GPP TR 38.817
- **TR 38.871** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [CATR na 3GPP Explorer](https://3gpp-explorer.com/glossary/catr/)
