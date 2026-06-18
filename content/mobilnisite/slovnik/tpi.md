---
slug: "tpi"
url: "/mobilnisite/slovnik/tpi/"
type: "slovnik"
title: "TPI – Transmitted Precoding Indicator"
date: 2025-01-01
abbr: "TPI"
fullName: "Transmitted Precoding Indicator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tpi/"
summary: "Řídicí ukazatel používaný v UMTS (3G) k signalizaci prekódovacího vektoru aplikovaného na vysílači pro uzavřenou smyčku přenosové diverzity. Umožňuje síti optimalizovat kvalitu signálu na downlinku tí"
---

TPI je řídicí ukazatel používaný v UMTS k signalizaci použitého prekódovacího vektoru pro uzavřenou smyčku přenosové diverzity, který informuje UE o zapnutí koherentní demodulace a zlepšení výkonu na downlinku.

## Popis

Transmitted Precoding Indicator (TPI) je základní součástí režimů uzavřené smyčky přenosové diverzity definovaných pro UMTS High-Speed Downlink Packet Access ([HSDPA](/mobilnisite/slovnik/hsdpa/)) a pozdější vylepšení. Funguje v rámci řídicí signalizace fyzické vrstvy. V režimu uzavřené smyčky 1 a 2 UE vypočítá a doporučí preferovaný prekódovací váhový vektor z předdefinovaného kodebooku na základě svého odhadu downlinkového kanálu. NodeB pak toto doporučené prekódování aplikuje na vysílaný signál. TPI je explicitní signál vysílaný NodeB na downlinku, který UE označuje, který konkrétní prekódovací vektor z dohodnutého kodebooku je právě aplikován na přenos dat. Tato signalizace je klíčová, protože skutečně aplikované prekódování se může lišit od doporučení UE kvůli rozhodnutím síťového plánování nebo zpožděním zpětné vazby.

TPI je vysílán na vyhrazeném fyzickém řídicím kanálu, konkrétně v polích Fractional Dedicated Physical Channel ([F-DPCH](/mobilnisite/slovnik/f-dpch/)) nebo přidružených řídicích kanálech pro HSDPA. Jeho hodnota přímo mapuje na index v prekódovacím kodebooku. Například v režimu uzavřené smyčky 1 vybírá 1bitový TPI mezi dvěma anténními váhovými vektory, zatímco pokročilejší režimy mohou používat více bitů. Po přijetí TPI použije UE indikovaný prekódovací vektor ke konfiguraci svého přijímacího zpracování, zejména algoritmů pro odhad kanálu a kombinování pro Primary Common Pilot Channel ([P-CPICH](/mobilnisite/slovnik/p-cpich/)) a datové kanály. To umožňuje UE koherentně demodulovat vysílaný signál, protože může přesně rekonstruovat efektivní kanál vytvořený kombinací fyzického kanálu a aplikovaného prekódování.

Z architektonického hlediska je TPI klíčovým prvkem spojujícím zpětnou vazbu o stavu kanálu od UE (přenášenou přes pole Feedback Information ([FBI](/mobilnisite/slovnik/fbi/)) na uplinkovém [DPCCH](/mobilnisite/slovnik/dpcch/)) a vysílací zpracování NodeB. Uzavírá tak smyčku v schématu přenosové diverzity. Bez TPI by muselo UE prekódování detekovat naslepo, což je neefektivní a náchylné k chybám. Úlohou TPI je snížit nejednoznačnost a zajistit, že předpoklady přijímače odpovídají akcím vysílače, což je nezbytné pro zachování zisku beamformingu a výhod diverzity operací uzavřené smyčky [MIMO](/mobilnisite/slovnik/mimo/) v UMTS. Jeho návrh odráží potřebu řídicí signalizace s nízkou režií a robustností pro podporu dynamické adaptace spoje.

## K čemu slouží

TPI byl zaveden, aby řešil výzvu efektivní implementace uzavřené smyčky přenosové diverzity v sítích UMTS. Před jeho zavedením schémata otevřené smyčky přenosové diverzity, jako je Space-Time Transmit Diversity ([STTD](/mobilnisite/slovnik/sttd/)), nevyžadovala explicitní signalizaci prekódování, ale nabízela menší zisk výkonu, protože se nepřizpůsobovala okamžitým podmínkám kanálu. Motivací pro režimy uzavřené smyčky bylo využít znalost kanálu na vysílači ke zlepšení poměru signál-šum ([SNR](/mobilnisite/slovnik/snr/)) na přijímači, čímž se zvýšily přenosové rychlosti a pokrytí buňky. TPI řeší kritický problém signalizační synchronizace mezi vysílačem a přijímačem ohledně aplikovaných prekódovacích vah.

Bez explicitního ukazatele, jako je TPI, by čelilo UE značné složitosti při demodulaci signálů, když by síť mohla aplikovat jiné prekódování, než které bylo naposledy doporučeno. K tomu mohlo dojít kvůli zpožděním zpracování, rozhodnutím plánování nebo chybám v uplinkové zpětné vazbě. TPI poskytuje spolehlivý downlinkový kanál s nízkou latencí pro předání této informace, což zajišťuje, že přijímač UE je správně sladěn s prostorovými charakteristikami vysílaného signálu. To umožňuje koherentní kombinaci signálů z více vysílacích antén, čímž se maximalizuje diverzita a zisk pole. Jeho vytvoření bylo hnací silou snah 3GPP v Release 11 o vylepšení výkonu UMTS a spektrální účinnosti, aby zůstal konkurenceschopný s vyvíjejícími se standardy LTE díky zlepšení MIMO schopností v rámci 3G frameworku.

## Klíčové vlastnosti

- Signalizuje aplikovaný index prekódovacího vektoru z předdefinovaného kodebooku
- Umožňuje koherentní demodulaci pro režimy uzavřené smyčky přenosové diverzity
- Vysílán na downlinkových fyzických řídicích kanálech (např. F-DPCH)
- Funguje ve spojení s uplinkovou FBI zpětnou vazbou od UE
- Podporuje více režimů uzavřené smyčky s různými velikostmi kodebooku
- Nezbytný pro udržení výkonu spoje v MIMO HSDPA operacích

## Související pojmy

- [FBI – Final Block Indicator](/mobilnisite/slovnik/fbi/)
- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [TPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tpi/)
