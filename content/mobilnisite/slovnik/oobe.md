---
slug: "oobe"
url: "/mobilnisite/slovnik/oobe/"
type: "slovnik"
title: "OOBE – Out-Of-Band Emission"
date: 2025-01-01
abbr: "OOBE"
fullName: "Out-Of-Band Emission"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/oobe/"
summary: "Out-Of-Band Emissions (OOBE) označuje nežádoucí vyzařování vysílače vznikající bezprostředně mimo přidělenou šířku kanálu, způsobené nelinearitami a přechodovými jevy při přepínání. Řízení OOBE je klí"
---

OOBE (Out-Of-Band Emission) je nežádoucí vyzařování vysílače vznikající bezprostředně mimo přidělenou šířku kanálu, způsobené nelinearitami a přechodovými jevy při přepínání, které musí být regulováno, aby se zabránilo interferencím.

## Popis

Out-Of-Band Emission (OOBE) je základní parametr vysokofrekvenční (RF) výkonnosti každého vysílače, včetně těch v uživatelských zařízeních (UE) a základnových stanicích (gNB, [eNB](/mobilnisite/slovnik/enb/)) v systémech 3GPP. Kvantifikuje nežádoucí RF energii, kterou vysílač vyzařuje mimo přidělenou šířku svého kanálu. OOBE se liší od nežádoucích vyzařování (spurious emissions), která se vyskytují na kmitočtech dále od nosné. OOBE vzniká primárně ze dvou zdrojů: nelineárního zesílení modulovaného signálu ve výkonovém zesilovači (PA) a náhlého přepínání vysílače během náběhu a doběhu výkonu, zejména v systémech s časovým duplexem (TDD). Nelinearita PA způsobuje spektrální rozšíření (spectral regrowth), při kterém se šířka pásma vysílaného signálu rozprostře za své zamýšlené meze a vytváří tak rušení v sousedních kanálech.

Ve specifikacích 3GPP je OOBE rigorózně definováno a měřeno. Klíčové specifikace jako TS 38.101 (rádiové vysílání UE) a TS 38.104 (rádiové vysílání základnové stanice) definují limity pro OOBE prostřednictvím masek spektrálního vyzařování (SEM) a požadavků na poměr úniku do sousedního kanálu ([ACLR](/mobilnisite/slovnik/aclr/)). Maska spektrálního vyzařování definuje šablonu spektrální hustoty výkonu, kterou vysílaný signál při měření mimo přidělenou šířku kanálu nesmí překročit. ACLR je poměr porovnávající výkon změřený v sousedním kanálu s výkonem změřeným v přiděleném kanálu. Jde o klíčovou metriku pro posouzení potenciálu vysílače způsobit rušení přijímači v sousedním kanálu.

Omezování OOBE je komplexní technický problém zahrnující jak digitální základní pásmo, tak RF předkoncový stupeň. V digitální oblasti se používají techniky jako redukce faktoru špičkovosti ([CFR](/mobilnisite/slovnik/cfr/)) a digitální predistorze ([DPD](/mobilnisite/slovnik/dpd/)). CFR snižuje poměr špičkového a středního výkonu (PAPR) signálu, což umožňuje PA pracovat v lineárnější oblasti s menším spektrálním rozšířením. DPD linearizuje PA aplikací inverzní charakteristiky zkreslení na signál v základním pásmu, čímž kompenzuje nelinearitu PA před zesílením. V RF návrhu jsou zásadní pečlivá filtrace a použití lineárních PA. U TDD systémů je pro minimalizaci přechodového vyzařování klíčová přesná kontrola profilu náběhu a doběhu výkonu (tvaru zapínání/vypínání signálu). Dodržování limitů OOBE je povinné pro typové schválení a zásadní pro zajištění koexistence více operátorů a technologií rádiového přístupu ve stejném nebo sousedním kmitočtovém pásmu.

## K čemu slouží

Specifikace a přísná regulace Out-Of-Band Emissions jsou základním předpokladem efektivního a spravedlivého využití rádiového spektra, které je omezeným a sdíleným zdrojem. Bez limitů OOBE by výkonný vysílač pracující na jednom kanálu mohl přenášet významnou energii do sousedních kanálů a způsobovat tak závažné rušení. To by degradovalo výkon ostatních uživatelů a efektivně snižovalo celkovou kapacitu sítě a kvalitu služeb. Tento problém se stává palčivějším s hustým opakovaným využíváním kmitočtů a širokými kanálovými šířkami používanými v moderních systémech 4G LTE a 5G NR.

Historicky, jak se bezdrátové systémy vyvíjely od úzkopásmových analogových k širokopásmovým digitálním modulacím (jako je [OFDM](/mobilnisite/slovnik/ofdm/) používané v LTE a NR), potenciál pro spektrální rozšíření a rušení sousedních kanálů výrazně vzrostl. OFDM signály mají vysoký PAPR, což je činí obzvláště náchylnými k nelineárnímu zkreslení ve výkonových zesilovačích. Normy 3GPP pro OOBE se vyvíjely v průběhu jednotlivých releasů, aby tyto výzvy řešily a zajistily, že nové technologie mohou být nasazeny bez narušení stávajících služeb. Například při nasazení LTE v pásmech sousedících se systémy 2G/3G byly nutné přísné limity OOBE k ochraně těchto legacy sítí. Podobně v 5G NR, zejména pro scénáře mmWave kmitočtů a širokopásmové agregace nosných, je řízení OOBE klíčové pro vlastní vnitřní rušení mezi rádiovými moduly zařízení a pro koexistenci s jinými službami, jako jsou satelitní nebo radarové systémy pracující v blízkých pásmech. Pokračující vývoj požadavků na OOBE odráží neustálý tlak na vyšší energetickou účinnost (která má tendenci zvyšovat nelinearitu) a širší šířky pásem, vyvažující výkonnost s imperativem čistoty spektra.

## Klíčové vlastnosti

- Definován limitami Masky spektrálního vyzařování (SEM), které specifikují maximální povolený výkon mimo kanál
- Kvantifikován Poměrem úniku do sousedního kanálu (ACLR), což je klíčová metrika výkonnosti
- Primárně způsoben nelinearitou výkonového zesilovače a přechodovými jevy při přepínání vysílače
- Omezován technikami v základním pásmu, jako je Digitální predistorze (DPD) a Redukce faktorů špičkovosti (CFR)
- Klíčový pro zajištění koexistence mezi různými operátory a technologiemi rádiového přístupu
- Předmětem zkoušek shody pro typové schválení UE a základnových stanic

## Související pojmy

- [ACL – Asynchronous Connection-Oriented Link](/mobilnisite/slovnik/acl/)

## Definující specifikace

- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TR 37.880** (Rel-17) — High-power UE for fixed-wireless/vehicle use
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.108** (Rel-19) — NTN NR Satellite Access Node RF Requirements
- **TS 38.181** (Rel-19) — NR Satellite Access Node RF Testing
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.755** (Rel-19) — NR FR1 DL Fragmented Carriers Study
- **TS 38.793** (Rel-19) — Simultaneous Rx/Tx Band Combinations TR
- **TR 38.805** (Rel-14) — Study on New Radio Access Technology; 60 GHz unlicensed spectrum
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.839** (Rel-17) — Simultaneous Rx/Tx band combinations
- **TR 38.881** (Rel-18) — Technical Report on Lower MSD for Inter-band CA/EN-DC/DC
- **TR 38.894** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [OOBE na 3GPP Explorer](https://3gpp-explorer.com/glossary/oobe/)
