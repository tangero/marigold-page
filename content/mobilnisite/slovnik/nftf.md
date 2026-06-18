---
slug: "nftf"
url: "/mobilnisite/slovnik/nftf/"
type: "slovnik"
title: "NFTF – Near Field To Far-field"
date: 2025-01-01
abbr: "NFTF"
fullName: "Near Field To Far-field"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/nftf/"
summary: "Měřicí a transformační technika používaná při testování antén a OTA (Over-the-Air) validaci výkonu. Převádí data o vyzařovacím diagramu v blízkém poli, naměřená v těsné blízkosti antény, na vyzařovací"
---

NFTF je měřicí a transformační technika používaná při testování antén, která převádí data o vyzařovacím diagramu v blízkém poli na diagram v dalekém poli, aby přesně charakterizovala reálný výkon antény, například u 5G systémů massive MIMO.

## Popis

NFTF, neboli transformace z blízkého pole do dalekého pole, je základní elektromagnetická technika standardizovaná v rámci 3GPP pro testování a validaci rádiového zařízení, zejména antén. Základní princip spočívá v tom, že elektromagnetické pole vyzařované anténou má dvě odlišné oblasti: blízké pole (reaktivní a vyzařující blízké pole) a daleké pole (Fraunhoferova oblast). Přímé měření kompletního vyzařovacího diagramu v dalekém poli, zejména u velkých anténních polí, jako jsou ta používaná v 5G massive [MIMO](/mobilnisite/slovnik/mimo/), je často nepraktické kvůli obrovské vzdálenosti vyžadované mezi testovanou anténou (AUT) a měřicí sondou pro splnění podmínek dalekého pole. Proces NFTF tento problém řeší tím, že umožňuje měření v mnohem snáze zvládnutelné oblasti blízkého pole, typicky uvnitř anechoické komory.

Technika funguje tak, že sonda antény skenuje přes dobře definovanou plochu (rovinu, válec nebo kouli), která obklopuje AUT v blízkém poli. Sonda měří jak amplitudu, tak fázi vyzařovaného pole v mnoha bodech na této ploše. Tato vzorkovaná data z blízkého pole jsou následně zpracována pomocí rigorózních elektromagnetických transformačních algoritmů, jako je metoda spektra rovinných vln (Plane Wave Spectrum, [PWS](/mobilnisite/slovnik/pws/)) pro planární skeny nebo sférická vlnová expanze pro sférické skeny. Tyto algoritmy matematicky propagují data z blízkého pole do nekonečné vzdálenosti, čímž efektivně vypočítají vyzařovací diagram antény v dalekém poli, včetně zisku, směrovosti, šířky svazku a úrovní postranních laloků.

Klíčové komponenty systému NFTF zahrnují přesný robotický polohovač pro pohyb sondy, vektorový analyzátor sítí ([VNA](/mobilnisite/slovnik/vna/)) pro měření komplexních S-parametrů, anechoickou komoru pro eliminaci odrazů a sofistikovaný software pro provedení transformace a následného zpracování. V 3GPP specifikace jako TS 38.810 a TR 38.903 definují testovací metodologie a požadavky pro použití NFTF v konformním testování rádiových jednotek uživatelského zařízení (UE) a základnové stanice (gNB). Její role je nepostradatelná pro ověření výkonu pokročilých anténních systémů ([AAS](/mobilnisite/slovnik/aas/)), zajištění, že beamformingový zisk, přesnost natočení svazku a celkový vyzářený výkon ([TRP](/mobilnisite/slovnik/trp/)) splňují přísné standardy 5G, což přímo ovlivňuje pokrytí a kapacitu sítě.

## K čemu slouží

Primárním účelem transformace NFTF je umožnit přesné a proveditelné [OTA](/mobilnisite/slovnik/ota/) (Over-the-Air) testování moderních bezdrátových zařízení, zejména těch s integrovanými, neodnímatelnými anténami a složitými anténními poli. Před rozšířeným přijetím NFTF se charakterizace antén často spoléhala na přímá měření v dalekém poli na velkých otevřených testovacích plochách ([OATS](/mobilnisite/slovnik/oats/)) nebo na vedená testování pomocí koaxiálních kabelů. Tyto metody se s nástupem 5G staly nedostatečnými. Základnové stanice massive [MIMO](/mobilnisite/slovnik/mimo/) a uživatelská zařízení integrují desítky nebo stovky anténních prvků, což činí kabelová testování nepraktickými a narušuje chování antény. Navíc dosažení skutečné vzdálenosti dalekého pole pro tyto elektricky velké antény vyžaduje nepřiměřeně velké testovací vzdálenosti, někdy stovky metrů.

NFTF byla motivována potřebou testovat tato zařízení v kontrolovaném laboratorním prostředí bez obětování přesnosti měření. Řeší omezení prostoru tím, že umožňuje kompaktní testovací uspořádání uvnitř anechoické komory. Historicky byly matematické základy NFTF známy po desetiletí, ale její standardizace a přesná aplikace v rámci 3GPP byly hnací silou specifických požadavků na výkon 5G New Radio (NR). Technika řeší kritický problém validace výkonu beamformingu, který je základním kamenem 5G pro zlepšení spektrální účinnosti a uživatelského zážitku. Bez NFTF by bylo extrémně obtížné garantovat, že svazky 5G zařízení jsou vytvářeny správně a směřují do zamýšlených směrů, což by vedlo k potenciální degradaci výkonu sítě.

## Klíčové vlastnosti

- Umožňuje charakterizaci diagramu v dalekém poli z kompaktních měření v blízkém poli
- Podporuje více skenovacích geometrií: planární, válcová a sférická
- Vyžaduje přesné měření amplitudy i fáze vyzařovaného pole
- Využívá elektromagnetické transformační algoritmy, jako je expanze spektra rovinných vln (Plane Wave Spectrum, PWS)
- Klíčová pro testování integrovaných aktivních anténních systémů (AAS) a polí massive MIMO
- Standardizovaná metodologie pro testování celkového vyzářeného výkonu (TRP) a celkové izotropní citlivosti (TIS)

## Definující specifikace

- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TR 38.884** (Rel-18) — Technical Report
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [NFTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nftf/)
