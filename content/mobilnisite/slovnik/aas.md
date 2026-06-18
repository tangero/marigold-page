---
slug: "aas"
url: "/mobilnisite/slovnik/aas/"
type: "slovnik"
title: "AAS – Active Antenna System"
date: 2025-01-01
abbr: "AAS"
fullName: "Active Antenna System"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aas/"
summary: "AAS je architektura základnové stanice, kde jsou anténní prvky integrovány s aktivními rádiovými komponenty, jako jsou výkonové zesilovače a šumově nízké zesilovače. Umožňuje pokročilé beamforming a M"
---

AAS je architektura základnové stanice, ve které integrované anténní prvky a aktivní rádiové komponenty umožňují individuální řízení pro pokročilé beamforming a MIMO, což je zásadní pro sítě 4G LTE-Advanced a 5G NR.

## Popis

Aktivní anténní systém (AAS) představuje zásadní architektonický posun v návrhu základnových stanic, přecházející od tradičních pasivních anténních polí připojených k dálkovým rádiovým jednotkám přes koaxiální kabely k plně integrovanému systému, kde jsou zářiče, transceivery a komponenty pro zpracování signálu umístěny společně v jednom anténním krytu. Na rozdíl od konvenčních základnových stanic, kde jsou anténní prvky pasivní a beamforming se provádí v základnové jednotce, AAS provádí beamforming v oblasti vysokofrekvenčního ([RF](/mobilnisite/slovnik/rf/)) pásma prostřednictvím přesného řízení fáze a amplitudy u každého anténního prvku. Tato integrace eliminuje ztráty ve výživních vedeních, snižuje prostorové nároky na lokalitu a umožňuje dynamické trojrozměrné beamformingové schopnosti, které se přizpůsobují distribuci uživatelů a rádiovým podmínkám v reálném čase.

Jádrová architektura AAS se skládá z více anténních prvků uspořádaných do dvourozměrného pole (typicky konfigurace 8x8, 16x16 nebo větší), z nichž každý je připojen k vlastnímu transceiverovému řetězci. Každý transceiverový řetězec obsahuje výkonový zesilovač ([PA](/mobilnisite/slovnik/pa/)) pro vysílání, šumově nízký zesilovač ([LNA](/mobilnisite/slovnik/lna/)) pro příjem, analogově-digitální/digitálně-analogové převodníky ([ADC](/mobilnisite/slovnik/adc/)/[DAC](/mobilnisite/slovnik/dac/)) a digitální front-endové zpracování. Jednotka digitálního beamformingu vypočítává komplexní váhové vektory pro každý anténní prvek na základě informací o stavu kanálu, polohy uživatele a charakteru provozu. Tyto váhy upravují fázi a amplitudu signálů vysílaných nebo přijímaných každým prvkem, čímž vytvářejí konstruktivní interferenci v požadovaných směrech a destruktivní interferenci jinde, a tak vytvářejí vysoce směrové paprsky.

AAS funguje prostřednictvím sofistikovaných algoritmů pro zpracování signálu, které průběžně optimalizují tvary paprsků. Při vysílání základnová stanice aplikuje předkodovací matice na datové toky uživatele, mapuje je na konkrétní anténní porty s vypočtenými fázovými posuny. Pro příjem aplikuje kombinační váhy na signály z více anténních prvků, aby maximalizovala poměr signálu k šumu a rušení ([SINR](/mobilnisite/slovnik/sinr/)). Systém podporuje jak analogový beamforming (kde fázové posouvače pracují s RF signály), tak hybridní beamforming (kombinující analogový beamforming s digitálním předkódováním), přičemž implementace 5G upřednostňují hybridní přístupy pro vyvážení výkonu a složitosti. Mezi klíčové provozní režimy patří beamforming specifický pro buňku pro vysílací kanály, beamforming specifický pro uživatele pro vyhrazený provoz a víceuživatelské [MIMO](/mobilnisite/slovnik/mimo/), kde více paprsků obsluhuje různé uživatele současně na stejných časově-frekvenčních zdrojích.

Role AAS v moderních sítích přesahuje základní beamforming a umožňuje nasazení masivního MIMO (mMIMO) s desítkami až stovkami anténních prvků. Vytvářením úzkých, adaptivních paprsků AAS dramaticky zvyšuje kapacitu sítě prostřednictvím prostorového multiplexování, zlepšuje pokrytí soustředěním energie směrem k uživatelům a snižuje rušení prostorovým filtrováním. V 5G NR AAS podporuje jak pásma pod 6 GHz, tak milimetrová vlnová pásma, s různými implementacemi optimalizovanými pro každé z nich: AAS pro pásma pod 6 GHz typicky používá střední počet prvků (32-64) pro sektorové pokrytí, zatímco mmWave AAS využívá stovky prvků k překonání vysokých útlumů na dráze prostřednictvím extrémně směrových paprsků. Digitální architektura systému také umožňuje pokročilé funkce, jako je plně-dimenzionální MIMO (FD-MIMO) pro elevaci beamformingu, procedury správy paprsků pro mobilní uživatele a podporu ultra-spolehlivých komunikací s nízkou latencí prostřednictvím rychlého přepínání paprsků.

## K čemu slouží

AAS byl vyvinut, aby řešil kritická omezení tradičních architektur základnových stanic, která se stávala stále problematičtějšími, jak se mobilní sítě vyvíjely směrem k 4G a 5G. Konvenční systémy používaly pasivní anténní pole s pevnými vyzařovacími diagramy a omezenými možnostmi beamformingu, typicky podporující pouze 2-8 anténních portů s hrubými úpravami sklonu paprsku. Tyto systémy trpěly významnými ztrátami ve výživních vedeních mezi rádiovými jednotkami a anténami, omezenou flexibilitou prostorového zpracování a neschopností dynamicky se přizpůsobovat měnící se distribuci uživatelů a charakteru provozu. Jak se s LTE-Advanced zvyšovaly požadavky na spektrální účinnost a síťová densifikace se stala nezbytnou pro splnění kapacitních nároků, tato omezení se stala hlavními překážkami výkonu sítě.

Primární motivací pro vytvoření AAS bylo umožnit pokročilé víceanténní techniky, které by mohly dramaticky zlepšit spektrální účinnost prostřednictvím prostorového multiplexování. Integrací aktivních komponent přímo s anténními prvky AAS eliminuje ztráty ve výživních vedeních, které typicky představují degradaci signálu o 2-3 dB, což přímo zlepšuje pokrytí a energetickou účinnost. Důležitější je, že umožňuje přesné elektronické řízení vyzařovacího diagramu každého anténního prvku, což základnovým stanicím dovoluje vytvářet více simultánních paprsků, které mohou sledovat jednotlivé uživatele nebo skupiny uživatelů. Tato schopnost je zásadní pro implementaci systémů masivního [MIMO](/mobilnisite/slovnik/mimo/), u kterých teoretické studie ukázaly, že mohou násobit kapacitu sítě o řád prostřednictvím multiplexování v prostorové doméně.

Historicky byl vývoj AAS hnán potřebou podporovat funkce LTE-Advanced, jako je 8vrstvé prostorové multiplexování a koordinovaný multipointový přenos, které vyžadovaly sofistikovanější anténní systémy než tradiční pasivní pole. Technologie získala další význam s 5G NR, které je závislé na operacích založených na paprscích, zejména v milimetrových vlnových pásmech, kde vysoký útlum na dráze vyžaduje vysoce směrové paprsky pro adekvátní pokrytí. AAS řeší praktické výzvy nasazení masivního MIMO integrací všech potřebných komponent do kompaktních, energeticky účinných jednotek, které lze nasadit na stávajících lokalitách bez nutnosti rozsáhlého dodatečného prostoru nebo konstrukčních úprav. Také řeší provozní složitost prostřednictvím schopností samokalibrace a samoptimalizace, které udržují přesnost beamformingu při teplotních variacích a stárnutí komponent.

## Klíčové vlastnosti

- Integrované anténní prvky s aktivními transceiverovými řetězci na prvek
- Digitální řízení fáze a amplitudy pro každý anténní prvek
- Podpora jak analogových, tak hybridních beamformingových architektur
- Dynamický 3D beamforming s řízením elevace a azimutu
- Podpora masivního MIMO s desítkami až stovkami anténních prvků
- Samokalibrační a vestavěné testovací schopnosti pro údržbu

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 32.865** (Rel-15) — OAM Aspects of SON for AAS-Based Deployments
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.114** (Rel-19) — EMC for Active Antenna System Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.808** (Rel-12) — PIM Handling for Base Stations Study
- **TS 37.810** (Rel-12) — Study on Base Station Specification Structure
- **TS 37.816** (Rel-16) — RAN-centric Data Collection & Utilization Study
- **TS 37.822** (Rel-12) — SON Enhancements for UE Types and Active Antennas
- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- … a dalších 12 specifikací

---

📖 **Anglický originál a plná specifikace:** [AAS na 3GPP Explorer](https://3gpp-explorer.com/glossary/aas/)
