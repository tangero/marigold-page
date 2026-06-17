---
slug: "acu"
url: "/mobilnisite/slovnik/acu/"
type: "slovnik"
title: "ACU – Antenna Combining Unit"
date: 2025-01-01
abbr: "ACU"
fullName: "Antenna Combining Unit"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/acu/"
summary: "Antenna Combining Unit (ACU) je hardwarová komponenta v základnových stanicích, která kombinuje více anténních signálů do jednoho výstupu pro přenos nebo zpracování. Umožňuje efektivní víceanténní kon"
---

ACU je hardwarová komponenta v základnových stanicích, která kombinuje více anténních signálů do jednoho výstupu, aby umožnila efektivní víceanténní konfigurace.

## Popis

Antenna Combining Unit (ACU) je klíčová hardwarová komponenta v infrastruktuře rádiového přístupového sítě (RAN), konkrétně v architekturách základnových stanic. Funguje jako analogová jednotka pro zpracování signálu, která kombinuje signály z více anténních prvků do jednoho konsolidovaného výstupního proudu pro vysílání, nebo naopak rozděluje přijímané signály pro distribuci k více anténním prvkům. ACU pracuje na rádiové frekvenci (RF) nebo mezifrekvenci ([IF](/mobilnisite/slovnik/if/)) a je typicky umístěna mezi anténní pole a transceiverové jednotky (TRx) nebo vzdálené rádiové hlavice (RRH). Jejím hlavním architektonickým úkolem je vytvořit rozhraní mezi fyzickými anténními prvky a jednotkami digitálního zpracování, což umožňuje efektivní agregaci a distribuci signálu bez nutnosti vyhrazeného transceiverového řetězce pro každý jednotlivý anténní prvek.

Technicky ACU implementuje pasivní nebo aktivní kombinační sítě pomocí komponent jako jsou děliče/kombinátory výkonu, fázové posouvače a atenuátory. V režimu vysílání přijímá jeden RF signál z transceiveru a distribuuje jej na více anténních portů s řízeným fázovým a amplitudovým vztahem za účelem vytvoření specifických vyzařovacích charakteristik. V režimu příjmu kombinuje signály z více anténních prvků do menšího počtu výstupních portů, čímž efektivně provádí analogový beamforming nebo kombinaci diverzity před analogově-digitální konverzí. Toto analogové předzpracování snižuje složitost a náklady digitálního základopásmového zpracování tím, že snižuje počet potřebných analogově-digitálních převodníků ([ADC](/mobilnisite/slovnik/adc/)) a digitálně-analogových převodníků ([DAC](/mobilnisite/slovnik/dac/)).

Fungování ACU je zásadní pro implementaci víceanténních technologií jako Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)) a beamforming. Tím, že umožňuje jednomu transceiveru obsluhovat více anténních prvků prostřednictvím analogového kombinování, umožňuje základnovým stanicím dosáhnout prostorové diverzity, směrování svazku a zvýšené kapacity bez úměrného zvýšení hardwarových nákladů. Jednotka typicky zahrnuje kalibrační obvody pro udržení konzistence fáze a amplitudy na různých cestách, což zajišťuje předvídatelný výkon anténního diagramu. V pokročilých implementacích může ACU zahrnovat spínací matice pro podporu rekonfigurovatelných anténních polí nebo podporu více kmitočtových pásem prostřednictvím filtračních komponent.

V širší síťové architektuře jsou ACU nasazovány v různých konfiguracích základnových stanic včetně makro buněk, small cells a systémů massive MIMO. Komunikují s anténními poli prostřednictvím koaxiálních kabelů nebo integrovaných spojů a se základopásmovými jednotkami prostřednictvím standardizovaných rozhraní jako Common Public Radio Interface (CPRI) nebo enhanced CPRI (eCPRI), když jsou integrovány se vzdálenými rádiovými hlavicemi. Výkon ACU přímo ovlivňuje klíčové rádiové metriky včetně anténního zisku, šířky svazku, úrovní postranních laloků a schopnosti potlačení rušení. Správný návrh a kalibrace ACU jsou nezbytné pro dosažení teoretických výhod víceanténních systémů v praktických nasazeních.

## K čemu slouží

Antenna Combining Unit (ACU) byla vytvořena, aby řešila rostoucí potřebu víceanténních systémů v mobilních sítích při současném zvládání hardwarové složitosti a nákladů. Rané mobilní systémy používaly jednoduché jednoprvkové anténní konfigurace s všesměrovými nebo sektorovými charakteristikami, ale s rostoucími nároky na kapacitu sítě potřebovali operátoři sofistikovanější anténní systémy pro zlepšení spektrální účinnosti, pokrytí a propustnosti pro uživatele. ACU se objevila jako řešení, které umožňuje pokročilé anténní techniky bez nutnosti úplné duplikace rádiově-frekvenčních řetězců pro každý anténní prvek.

Historicky, před rozšířeným přijetím ACU, vyžadovala implementace víceanténních systémů samostatné transceivery pro každý anténní prvek, což výrazně zvyšovalo náklady, velikost a spotřebu energie základnové stanice. To činilo pokročilé anténní technologie ekonomicky nepraktické pro mnohá nasazení. ACU tento problém řeší tím, že umožňuje více anténním prvkům sdílet společné transceiverové zdroje prostřednictvím analogového kombinování signálu, což dramaticky snižuje hardwarovou režii víceanténních implementací. To bylo obzvláště důležité, jak se standardy 3GPP vyvíjely a začaly zahrnovat podporu pro diverzitu vysílání, diverzitu příjmu a nakonec technologie [MIMO](/mobilnisite/slovnik/mimo/) počínaje [HSDPA](/mobilnisite/slovnik/hsdpa/) v Release 5.

ACU řeší několik konkrétních omezení předchozích přístupů: snižuje počet potřebných RF komponent (zesilovačů, filtrů, převodníků) tím, že umožňuje sdílení antén, snižuje systémovou složitost a počet možných míst selhání prostřednictvím konsolidace hardwaru a snižuje celkové náklady na nasazení při zachování výkonnostních benefitů. Také umožňuje flexibilnější anténní konfigurace tím, že umožňuje dynamickou rekonfiguraci anténních charakteristik prostřednictvím řízených úprav fáze a amplitudy v kombinační síti. Tato schopnost se stávala stále důležitější, jak se sítě vyvíjely směrem k chytrým anténním systémům a nakonec k massive MIMO, kde stovky anténních prvků musí být efektivně řízeny s praktickými hardwarovými omezeními.

## Klíčové vlastnosti

- Analogové kombinování signálu pro více anténních prvků
- Řízení fáze a amplitudy pro aplikace beamforming
- Snížení počtu potřebných transceiverových řetězců prostřednictvím agregace signálu
- Podpora jak vysílacích, tak přijímacích signálových cest
- Kalibrační obvody pro udržení integrity signálu napříč cestami
- Kompatibilita rozhraní s různými konfiguracemi anténních polí

## Související pojmy

- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [ACU na 3GPP Explorer](https://3gpp-explorer.com/glossary/acu/)
