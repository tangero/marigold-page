---
slug: "prefsens"
url: "/mobilnisite/slovnik/prefsens/"
type: "slovnik"
title: "PREFSENS – Conducted reference Sensitivity power level"
date: 2025-01-01
abbr: "PREFSENS"
fullName: "Conducted reference Sensitivity power level"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/prefsens/"
summary: "Klíčový parametr výkonu přijímače definující minimální úroveň vstupního výkonu na anténním konektoru, při které může uživatelské zařízení (UE) nebo základnová stanice správně demodulovat signál se sta"
---

PREFSENS je minimální úroveň vstupního výkonu na anténním konektoru, při které může uživatelské zařízení (UE) nebo základnová stanice správně demodulovat signál se stanovenou mírou bitových chyb.

## Popis

Úroveň výkonu referenční citlivosti v kabelovém rozhraní (Conducted Reference Sensitivity power level, PREFSENS) je klíčový výkonnostní parametr definovaný ve specifikacích 3GPP pro přijímače uživatelských zařízení (UE) i základnových stanic (gNB, [eNB](/mobilnisite/slovnik/enb/), NodeB). Kvantifikuje schopnost přijímače detekovat a demodulovat slabé signály. Technicky je PREFSENS minimální průměrný výkon přijatý na anténním konektoru (kabelové rozhraní) testovaného zařízení za stanovených referenčních podmínek, při kterém je dosaženo definované minimální propustnosti nebo maximální míry chyb bloků ([BLER](/mobilnisite/slovnik/bler/)). Měří se v dBm. Například u UE test zahrnuje příjem specifického referenčního měřicího kanálu (např. signál modulovaný [QPSK](/mobilnisite/slovnik/qpsk/) s nízkou kódovou rychlostí) na úrovni výkonu PREFSENS a UE musí dosáhnout propustnosti rovné nebo větší než 95 % maximální možné propustnosti pro daný kanál.

Měřicí uspořádání pro PREFSENS je přísně kontrolované. Signál je přiváděn přímo na anténní konektor pomocí kabelu (kabelové testování), čímž se eliminují variace způsobené šířením vzduchem. Test používá definovaný referenční kanál se specifickou šířkou pásma, modulací a schématem kódování (typicky nejodolnějším, jako je QPSK s nízkou kódovou rychlostí). Ke signálu je přidán aditivní bílý Gaussovský šum ([AWGN](/mobilnisite/slovnik/awgn/)), aby vznikla specifická podmínka poměru signál-šum ([SNR](/mobilnisite/slovnik/snr/)) odpovídající cílové BLER. Následně je vyhodnocen výkon přijímače. Hodnotu PREFSENS ovlivňuje šumové číslo přijímače, implementační ztráty jeho základnového zpracování a úroveň tepelného šumu, která sama závisí na šířce pásma kanálu (kTB).

PREFSENS není jediná hodnota, ale je specifikován pro každý provozní pásmo, šířku kanálu a pro různé typy přijímačů (např. diverzitní vs. nediverzitní). Ve specifikacích základnových stanic je klíčovým parametrem pro určení pokrytí buňky, zejména limitu pokrytí pro uplink. Pro plánování sítě výpočet rádiového rozpočtu využívá PREFSENS základnové stanice (jako citlivost přijímače) a maximální vysílací výkon UE k určení maximálního přípustného útlumu na trase. Pro testování shody UE splnění požadavku na PREFSENS zajišťuje, že zařízení má dostatečně citlivý přijímač pro provoz na okraji buňky za normálních podmínek sítě. Jde o základní test, který ověřuje základní [RF](/mobilnisite/slovnik/rf/) výkon zařízení před složitějšími testy, jako je selektivita na sousedním kanálu nebo blokování.

## K čemu slouží

PREFSENS byl standardizován, aby poskytl objektivní, opakovatelnou a všeobecně srovnatelnou metriku pro nejzákladnější schopnost rádiového přijímače: příjem slabých signálů. Jeho existence řeší problém definice společného referenčního bodu pro citlivost přijímače napříč všemi výrobci a modely zařízení, čímž zajišťuje základní úroveň výkonu sítě a uživatelského zážitku. Bez takového standardizovaného parametru by zařízení s nízkou citlivostí mohla degradovat celkový výkon sítě tím, že by vyžadovala vyšší vysílací výkon z druhé strany spoje, nebo by nedokázala udržet spojení na okraji buňky.

Historicky, jak se mobilní technologie vyvíjely od GSM přes UMTS, LTE až po NR, byla definice a testovací metodologie pro referenční citlivost upravována, aby zohlednila širší šířky pásma, nové modulační schémata a [MIMO](/mobilnisite/slovnik/mimo/). Jeho zavedení a kontinuální vývoj řeší potřebu přesného plánování sítě. Inženýři se spoléhají na garantované hodnoty PREFSENS publikované ve specifikacích při výpočtu realistických oblastí pokrytí buňky a zajišťují, aby nasazení sítě splňovalo cíle kontinuity služeb. Slouží také jako kritický kontrolní bod při typovém schvalování a testování shody, čímž brání vstupu podstandardních zařízení na trh, což chrání integritu sítě a zajišťuje spravedlivou konkurenci mezi výrobci zařízení na základě ověřitelných výkonnostních kritérií.

## Klíčové vlastnosti

- Definuje minimální vstupní výkon přijímače pro stanovenou propustnost/BLER
- Měřen za kontrolovaných kabelových podmínek na anténním portu
- Specifikován pro každé provozní pásmo, šířku pásma a konfiguraci přijímače
- Základní parametr pro RF testování shody UE a základnových stanic
- Kritický vstup pro výpočet rádiového rozpočtu a plánování pokrytí sítě
- Používá definované referenční měřicí kanály s AWGN

## Definující specifikace

- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.111** (Rel-19) — LMU Requirements for UTDOA Positioning
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.755** (Rel-15) — US 600 MHz LTE Band 71 Technical Report
- **TS 36.758** (Rel-15) — LTE TDD Band 52 for Africa 3300-3400MHz
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [PREFSENS na 3GPP Explorer](https://3gpp-explorer.com/glossary/prefsens/)
