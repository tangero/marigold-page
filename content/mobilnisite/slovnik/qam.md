---
slug: "qam"
url: "/mobilnisite/slovnik/qam/"
type: "slovnik"
title: "QAM – Quadrature Amplitude Modulation"
date: 2025-01-01
abbr: "QAM"
fullName: "Quadrature Amplitude Modulation"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qam/"
summary: "Modulační schéma přenášející data změnou amplitudy i fáze nosné vlny. Je klíčové pro moderní bezdrátovou komunikaci, neboť umožňuje vysokou spektrální účinnost přenosem více bitů na jeden symbol. Vyšš"
---

QAM je modulační schéma klíčové pro moderní bezdrátové sítě, které přenáší data změnou amplitudy i fáze nosné vlny, čímž umožňuje vysokou spektrální účinnost.

## Popis

Kvadraturní amplitudová modulace (QAM) je sofistikovaná modulační technika hojně využívaná v radiových přístupových technologiích 3GPP, včetně LTE a NR. Funguje tak, že moduluje dvě nosné vlny, typně fázově posunuté o 90 stupňů (v kvadratuře), označované jako složka v fázi (I) a kvadraturní složka (Q). Nezávislou změnou amplitudy každé z těchto nosných vln vzniká na I-Q rovině konstelace diskrétních bodů. Každý bod v této konstelaci představuje jedinečný symbol, který kóduje specifickou sekvenci bitů. Počet bodů v konstelaci definuje řád QAM; například [16QAM](/mobilnisite/slovnik/16qam/) má 16 bodů, což představuje 4 bity na symbol, zatímco [64QAM](/mobilnisite/slovnik/64qam/) reprezentuje 6 bitů na symbol a 1024QAM reprezentuje 10 bitů na symbol.

Implementace QAM ve fyzické vrstvě 3GPP zahrnuje několik klíčových komponent a procesů. Řetězec základní pásma mapuje příchozí bitové toky na komplexní modulační symboly podle zvolené QAM konstelace. Tyto symboly jsou následně podrobeny dalšímu zpracování, jako je mapování vrstev pro [MIMO](/mobilnisite/slovnik/mimo/), předkódování a mapování na zdrojové prvky v časově-frekvenční mřížce vlnového tvaru Orthogonal Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) ([OFDM](/mobilnisite/slovnik/ofdm/)) nebo DFT-s-OFDM. Konkrétní řád QAM použitý pro přenos je dynamicky vybírán algoritmy adaptace spojení sítě na základě ukazatelů kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) v reálném čase hlášených uživatelským zařízením (UE). Tato adaptivní modulace zajišťuje optimální propustnost použitím vyšších řádů QAM (např. 256QAM) za vynikajících podmínek signálu a přechodem na robustnější schémata nižšího řádu (např. [QPSK](/mobilnisite/slovnik/qpsk/)) za špatných podmínek.

Úloha QAM je ústřední pro přenosové schopnosti vzdušného rozhraní. Její spektrální účinnost – schopnost vměstnat více bitů do dané šířky pásma – přímo úměrně roste s logaritmem řádu konstelace. To činí postup k vyšším řádům QAM hlavní metodou pro zvyšování špičkových datových rychlostí napříč následnými releasy 3GPP. Podpora QAM je podrobně definována v řadě technických specifikací upravujících charakteristiky radiového vysílání a příjmu základnových stanic a UE (např. 36.104, 38.104), požadavky na výkon (např. 36.141, 38.141) a postupy testování shody (např. 36.521, 38.521). Specifikace definují vše od přesných souřadnic bodů konstelace a normalizačních faktorů až po požadavky na velikost chybového vektoru ([EVM](/mobilnisite/slovnik/evm/)) nezbytné pro vysílače k udržení integrity signálu.

## K čemu slouží

QAM existuje za účelem maximalizace datové propustnosti v omezeném a ceněném rádiovém spektru. Základní problém, který řeší, je potřeba vysoké spektrální účinnosti – přenos maximálního počtu bitů za sekundu na jeden hertz šířky pásma. Před rozšířeným přijetím vyšších řádů QAM se používala jednodušší modulační schémata, jako je fázová manipulace (PSK) nebo QAM nižších řádů, která nabízela robustnost, ale omezené špičkové datové rychlosti. Jak explodovala uživatelská poptávka po mobilním širokopásmovém připojení, tato starší schémata se stala úzkým hrdlem.

Motivace pro začleňování stále vyšších řádů QAM do norem 3GPP byla hnací silou neustálého úsilí o vyšší špičkové datové rychlosti a kapacitu sítě. Každé nové vydání, od zavedení 64QAM v LTE přes podporu 256QAM v LTE-Advanced až po 1024QAM v 5G NR, byla přímou reakcí na tržní požadavky na rychlejší stahování, vysílání videa ve vyšší kvalitě a podporu datově náročných aplikací. Tento vývoj umožnil pokrok v technologii radiofrekvenčních komponent, vylepšené kódy pro opravu chyb (jako LDPC) a sofistikovanější algoritmy přijímačů, které dokázaly spolehlivě demodulovat husté konstelace, dříve považované za příliš náchylné k šumu a interferencím.

## Klíčové vlastnosti

- Moduluje amplitudu i fázi nosné vlny za účelem vytvoření dvourozměrné symbolové konstelace
- Dynamicky přizpůsobitelný řád (např. QPSK, 16QAM, 64QAM, 256QAM, 1024QAM) na základě podmínek kanálu
- Přímo určuje spektrální účinnost a špičkové datové rychlosti radiového spoje
- Integruje se s vlnovými tvary OFDM/DFT-s-OFDM pro vícekanálový přenos
- Podléhá přísným požadavkům na velikost chybového vektoru (EVM) a chyby konstelace v 3GPP specifikacích
- Základ pro pokročilé techniky, jako je neuniformní konstelace (NUC), v pozdějších releasech

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- … a dalších 24 specifikací

---

📖 **Anglický originál a plná specifikace:** [QAM na 3GPP Explorer](https://3gpp-explorer.com/glossary/qam/)
