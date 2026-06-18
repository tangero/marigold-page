---
slug: "dff"
url: "/mobilnisite/slovnik/dff/"
type: "slovnik"
title: "DFF – Direct Far Field"
date: 2025-01-01
abbr: "DFF"
fullName: "Direct Far Field"
category: "Physical Layer"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/dff/"
summary: "Direct Far Field (DFF) je kanálový model a metodika měření v 3GPP pro charakterizaci šíření rádiových vln ve vzdálené zóně (far-field) antén, zvláště relevantní pro vysokofrekvenční pásma jako mmWave."
---

DFF je kanálový model a metodika měření 3GPP pro charakterizaci šíření rádiových vln v anténní vzdálené zóně (far-field), který definuje vzdálenost, na níž se vlny stávají rovinnými, což je klíčové pro přesné beamforming a návrh systémů s masivním MIMO.

## Popis

Direct Far Field (DFF) představuje kritickou oblast v elektromagnetickém šíření, kde je vzdálenost od vysílací antény dostatečně velká, aby čelo vlny mohlo být aproximováno jako rovinné a úhlové spektrum výkonu se ustálí. Ve specifikacích 3GPP je DFF formálně definováno Rayleighovým vzdálenostním kritériem: R > 2D²/λ, kde D je největší rozměr apertury antény a λ je vlnová délka. Tato vzdálenostní hranice odděluje radiační blízkou zónu (Fresnelovu oblast) od vzdálené zóny (far-field), kde platí konvenční vyzařovací charakteristiky antén. Koncept DFF je obzvláště důležitý pro systémy s masivním [MIMO](/mobilnisite/slovnik/mimo/) s velkými anténními řadami, neboť určuje minimální vzdálenost potřebnou pro platné over-the-air testování, měření kanálu a verifikaci charakteristik svazků.

V praktických implementacích 3GPP zahrnují měření DFF specializovaná testovací uspořádání, kde je testované zařízení ([DUT](/mobilnisite/slovnik/dut/)) umístěno ve vzdálenostech přesahujících vypočtený práh DFF. To zajišťuje, že měření kanálu zachycují skutečné charakteristiky vzdálené zóny, včetně stabilních úhlových rozptylů, správných vlastností prostorové korelace a přesných exponentů útlumu na dráze. Metodologie specifikuje požadavky na anechoické komory, polohovací systémy a sondéry kanálu pro minimalizaci nejistot měření. Mezi klíčové parametry měřené v podmínkách DFF patří charakteristiky svazků, zisk, směrovost, úrovně bočních laloků a charakteristiky polarizace, které jsou nezbytné pro validaci shody s 3GPP.

Pro účely modelování kanálu používá 3GPP předpoklady DFF při vývoji statistických kanálových modelů pro různé scénáře nasazení. Ve vzdálené zóně může být kanál reprezentován jako superpozice rovinných vln s konkrétními úhly příchodu a odchodu, což umožňuje efektivní přístupy modelování založené na sledování paprsků a geometrii. Toto zjednodušení je zásadní pro 3GPP modely s klastrovaným zpožděním ([CDL](/mobilnisite/slovnik/cdl/)) a požadavky na prostorovou konzistenci. Podmínka DFF také ovlivňuje procedury správy svazků, protože kodebooky pro beamforming a konfigurace [CSI-RS](/mobilnisite/slovnik/csi-rs/) předpokládají charakteristiky šíření ve vzdálené zóně pro optimální výkon.

Z architektonického hlediska ovlivňují úvahy o DFF návrh základnových stanic a UE, zejména pro mmWave frekvence, kde jsou anténní řady fyzicky velké vzhledem k vlnové délce. Síťová zařízení musí udržovat podmínky DFF během kalibračních procedur, což vyžaduje pečlivý návrh interních měřicích systémů a [OTA](/mobilnisite/slovnik/ota/) testovacích schopností. Koncept také ovlivňuje nasazení sítě, protože nástroje pro plánování buněk musí zohledňovat vzdálenosti DFF při modelování interference mezi velkými anténními řadami. V Rel-16 a novějších byly principy DFF rozšířeny pro podporu uzlů integrovaného přístupu a přenosu ([IAB](/mobilnisite/slovnik/iab/)) a repeaterů, což zajišťuje konzistentní modelování kanálu napříč heterogenními síťovými prvky.

## K čemu slouží

Koncept Direct Far Field byl zaveden v 3GPP Rel-15, aby řešil jedinečné výzvy systémů s masivním [MIMO](/mobilnisite/slovnik/mimo/) a mmWave v 5G NR. Předchozí celulární systémy pracovaly primárně na sub-6 GHz frekvencích s relativně malými anténními řadami, kde byly podmínky vzdálené zóny snadno splněny v typických scénářích nasazení. Avšak se zavedením milimetrových vlnových pásem (24-52 GHz) a masivních MIMO řad se stovkami prvků se může vzdálenost DFF rozšířit na desítky či dokonce stovky metrů, což vytváří nové výzvy v měření a modelování, které se v 4G LTE nevyskytovaly.

DFF řeší kritické problémy v charakterizaci antén, modelování kanálu a validaci systému. Bez řádného zohlednění DFF by měření provedená v radiační blízké zóně vykazovala zakřivená čela vln a vzdálenostně závislé charakteristiky svazků, což by vedlo k nepřesným hodnocením výkonu a neshodným zařízením. To je obzvláště problematické pro beamformingové systémy, kde je přesná znalost směrů a zisků svazků zásadní pro optimalizaci sítě. Metodologie DFF zajišťuje konzistentní a reprodukovatelná měření napříč různými laboratořemi a dodavateli zařízení, což usnadňuje procesy interoperability a certifikace.

Vytvoření specifikací DFF bylo motivováno potřebou standardizovaných metodik over-the-air testování pro zařízení 5G NR. Tradiční přístupy testování přes vedení se staly nepraktickými pro integrované anténní systémy, zejména na mmWave frekvencích, kde jsou antény neoddělitelné od komponent vysokofrekvenčního front-endu. DFF poskytuje teoretický základ pro [OTA](/mobilnisite/slovnik/ota/) testování, umožňující komplexní vyhodnocení výkonu beamformingu, schopností prostorového multiplexování a charakteristik MIMO kanálu. Tato standardizace byla klíčová pro urychlení komercializace 5G stanovením jasných výkonnostních benchmarků a validačních procedur pro síťová zařízení a uživatelská zařízení.

## Klíčové vlastnosti

- Definuje Rayleighovo vzdálenostní kritérium pro určení hranice vzdálené zóny
- Umožňuje přesné over-the-air testování systémů s masivním MIMO
- Podporuje standardizované modelování kanálu pro mmWave frekvence
- Poskytuje základ pro verifikaci a kalibraci charakteristik svazků
- Zajišťuje konzistentní měření prostorové korelace
- Usnadňuje testování interoperability mezi různými dodavateli

## Definující specifikace

- **TS 38.771** (Rel-19) — FR2-1 OTA Testing for STxMP UEs
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TR 38.871** (Rel-18) — Technical Report
- **TR 38.884** (Rel-18) — Technical Report
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [DFF na 3GPP Explorer](https://3gpp-explorer.com/glossary/dff/)
