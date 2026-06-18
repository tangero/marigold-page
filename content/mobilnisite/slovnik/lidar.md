---
slug: "lidar"
url: "/mobilnisite/slovnik/lidar/"
type: "slovnik"
title: "LIDAR – Light Detection and Ranging"
date: 2025-01-01
abbr: "LIDAR"
fullName: "Light Detection and Ranging"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lidar/"
summary: "Technologie dálkového průzkumu využívající pulzní laserové světlo k měření vzdáleností a vytváření přesných, vysokorozlišujících 3D map okolí. V kontextu 3GPP je studována jako klíčový senzor pro prop"
---

LIDAR je technologie dálkového průzkumu, která využívá pulzní laserové světlo k měření vzdáleností a vytváření přesných 3D map. V rámci 3GPP je studována jako klíčový senzor pro propojená automatizovaná vozidla (Connected Automated Vehicles) a pokročilé asistenční systémy řízení (Advanced Driving Assistance Systems).

## Popis

Light Detection and Ranging (LIDAR) je aktivní optická senzorová technologie, která měří vzdálenost osvětlením cíle laserovým světlem a analýzou odraženého signálu. Typický LIDAR systém se skládá z laserového emitoru, citlivého fotodetektoru (přijímače) a přesného skenovacího mechanismu (často rotačního nebo polovodičového). Funguje tak, že vysílá krátké, zaostřené pulzy infračerveného světla. Časové zpoždění mezi vyslaným pulzem a detekcí jeho odrazu (čas letu) se měří s extrémní přesností. Protože je rychlost světla konstantní, toto měření času letu přímo vypočítá vzdálenost k objektu, který odraz způsobil.

V automobilových aplikacích a aplikacích pro CAV jsou LIDAR senzory umístěny na vozidlech a provádějí rychlé 360stupňové skenování okolního prostředí. Každý vracející se laserový pulz generuje jediný datový bod se souřadnicemi X, Y, Z („bod“). Tyto body se shromažďují v řádu milionů za sekundu a vytvářejí detailní 3D reprezentaci známou jako „mračno bodů“. Tato data z mračna bodů jsou následně zpracována palubními počítači pomocí sofistikovaných percepčních algoritmů k identifikaci a klasifikaci objektů (např. jiná vozidla, chodci, cyklisté, obrubníky, dopravní značky), odhadu jejich rychlosti a trajektorie a modelování sjízdné dráhy.

Úloha 3GPP, jak je popsána v technických zprávách jako TR 26.928, spočívá v standardizaci způsobu, jak lze tato masivní, vysokopásmová a na zpoždění citlivá LIDAR data (a data z jiných senzorů, jako jsou kamery a radar) sdílet mezi vozidly ([V2V](/mobilnisite/slovnik/v2v/)), s infrastrukturou (V2I) a se sítí (V2N). To zahrnuje definování požadavků na datové formáty, kompresní techniky a parametry kvality služeb (QoS) pro komunikační spoje vozidel. Cílem je umožnit „kolektivní vnímání“ nebo „sdílení senzorů“, kde vozidlo může přijímat zpracovaná nebo nezpracovaná LIDAR data z blízkých entit, čímž se efektivně rozšiřuje jeho percepční horizont za hranice přímé viditelnosti jeho vlastních senzorů, což je klíčové pro bezpečnost a vysokou úroveň automatizace.

## K čemu slouží

Technologie LIDAR byla integrována do studií 3GPP, aby řešila požadavky na senzory a sdílení dat pro vysokou úroveň automatizace vozidel (úrovně [SAE](/mobilnisite/slovnik/sae/) 4-5). Zatímco kamery a radar jsou také nezbytné, LIDAR poskytuje jedinečné schopnosti: generuje přesné, vysokorozlišující 3D mapy bez ohledu na světelné podmínky (funguje ve tmě) a poskytuje přímá, přesná měření vzdálenosti a rychlosti. Motivace pro standardizaci její integrace s mobilními sítěmi (C-V2X) vychází z omezení čistě palubního snímání. Senzory jednotlivého vozidla mají omezené zorné pole a dosah, což vytváří překážky a slepá místa, zejména ve složitých městských scénářích.

Práce 3GPP na LIDAR datech si klade za cíl vyřešit problém „sdílení vnímání prostředí“. Využitím nízkolatenčních, vysoce spolehlivých rozhraní 5G NR sidelink (PC5) a Uu mohou vozidla a jednotky na okraji vozovky vyměňovat nezpracovaná nebo zpracovaná mračna bodů z LIDARu. To umožňuje vozidlu „vidět“ za roh nebo přes jiná vozidla, což dramaticky zlepšuje povědomí o situaci a bezpečnost. Standardizace této výměny je klíčová pro interoperabilitu mezi vozidly různých výrobců a pro vytváření škálovatelných senzorových služeb založených na infrastruktuře. Přeměňuje vozidlo z izolovaného senzorového ostrova na uzel v kooperativním inteligentním dopravním systému (C-ITS), což je základním krokem k plně autonomní jízdě.

## Klíčové vlastnosti

- Generuje vysokohustotní 3D mračna bodů pro přesné modelování prostředí
- Poskytuje přesná měření vzdálenosti a rychlosti pomocí výpočtu času letu
- Efektivně funguje v různých světelných podmínkách, včetně úplné tmy
- Vysoké úhlové rozlišení pro detailní detekci a klasifikaci objektů
- Klíčový vstup pro algoritmy simultánní lokalizace a mapování (SLAM)
- Data podléhají standardizaci 3GPP pro sdílení a kompresi v rámci V2X

## Související pojmy

- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.985** (Rel-19) — Media Handling for Advanced V2X Services
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [LIDAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/lidar/)
