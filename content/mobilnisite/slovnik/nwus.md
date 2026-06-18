---
slug: "nwus"
url: "/mobilnisite/slovnik/nwus/"
type: "slovnik"
title: "NWUS – Narrow Band Wake Up Signal"
date: 2025-01-01
abbr: "NWUS"
fullName: "Narrow Band Wake Up Signal"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nwus/"
summary: "Nízkopříkonový signál v NB-IoT, který probouzí UE z klidového nebo neaktivního stavu, aby přijalo paging nebo systémovou informaci. Významně prodlužuje výdrž baterie IoT zařízení minimalizací doby, po"
---

NWUS je nízkopříkonový signál NB-IoT, který probouzí uživatelské zařízení z klidového stavu, aby mohlo přijímat paging, čímž prodlužuje výdrž baterie minimalizací aktivity hlavního přijímače.

## Popis

Narrow Band Wake Up Signal (NWUS) je signál fyzické vrstvy zavedený ve specifikaci 3GPP Release 15 pro Narrowband Internet of Things (NB-IoT) za účelem optimalizace spotřeby energie. Funguje tak, že vysílá jednoduchý, energeticky úsporný signál, který může být detekován nízkopříkonovým přijímačem pro probuzení ([LP-WUR](/mobilnisite/slovnik/lp-wur/)) IoT zařízení; tento přijímač spotřebovává mnohem méně energie než hlavní buněčný transceiver zařízení. Když síť potřebuje komunikovat s neaktivní UE, vyšle NWUS v předdefinovaném podrámci předcházejícím pagingové příležitosti. LP-WUR UE monitoruje tento specifický signálový vzor. Po úspěšné detekci LP-WUR spustí aktivaci hlavního přijímače UE a jednotky základního pásma právě včas, aby bylo možné dekódovat následnou pagingovou zprávu nebo blok systémové informace vysílaný na [NPDSCH](/mobilnisite/slovnik/npdsch/) (Narrowband Physical Downlink Shared Channel).

Z architektonického hlediska je NWUS integrován do struktury rámce downlinku NB-IoT. Jedná se o signál založený na sekvenci, typicky Zadoff-Chu nebo podobné, vybrané pro své dobré autokorelační vlastnosti, které umožňují spolehlivou detekci i při velmi nízkých poměrech signálu k šumu. Přenosové parametry, jako jsou časové a frekvenční zdroje pro NWUS, konfiguruje síť prostřednictvím signalizace vyšší vrstvy (např. SIB2-NB pro idle režim nebo [RRC](/mobilnisite/slovnik/rrc/) signalizace pro connected režim). Signál zabírá úzké šířky pásma, což odpovídá šířce nosného pásma 180 kHz u NB-IoT, a jeho vysílací výkon může být zvýšen oproti jiným signálům za účelem zlepšení pokrytí a spolehlivosti detekce.

Jeho role je klíčová pro funkce extended discontinuous reception (eDRX) a Power Saving Mode ([PSM](/mobilnisite/slovnik/psm/)) u NB-IoT. Bez NWUS musí UE periodicky aktivovat svůj plný přijímač, aby slepě kontrolovala pagingové indikátory během své pagingové příležitosti, což představuje většinu její energetické spotřeby. NWUS odděluje naslouchací aktivitu, což umožňuje UE zůstat v hlubokém spánkovém stavu s aktivním pouze minimálním LP-WUR. Aktivace hlavního přijímače je podmíněna přítomností probouzejícího signálu, což vede k dramatickému snížení spotřeby energie. Díky tomu je NWUS základní technologií pro dosažení více než desetileté výdrže baterie stacionárních IoT senzorů a měřidel, které jsou klíčovými případy užití pro massive IoT.

## K čemu slouží

NWUS byl vytvořen, aby řešil prvořadou výzvu ultranízké spotřeby energie v nasazeních massive IoT. Před jeho zavedením se NB-IoT UE spoléhala na standardní pagingové procedury, kdy zařízení muselo periodicky zapínat svůj hlavní rádiový přijímač, aby monitorovalo [PDCCH](/mobilnisite/slovnik/pdcch/) kvůli pagingovým indikacím. Toto periodické naslouchání, i při optimalizovaných cyklech eDRX, stále představovalo významný odběr energie v čase, což v mnoha scénářích omezovalo praktickou výdrž baterie na několik let. Požadavek průmyslu na výdrž baterie přes 10 let pro utility a environmentální senzory si vyžádal radikálnější přístup k úspoře energie.

Základní problém, který NWUS řeší, je neefektivita hlavního přijímače. Buněčné modemy, i úzkopásmové, vyžadují relativně vysoký výkon pro [RF](/mobilnisite/slovnik/rf/) zpracování, analogově-digitální převod a dekódování základního pásma. NWUS umožňuje použití samostatného, extrémně jednoduchého přijímacího obvodu ([LP-WUR](/mobilnisite/slovnik/lp-wur/)), který potřebuje pouze detekovat přítomnost známého signálového vzoru. Tento obvod může být implementován s řádově nižší spotřebou energie. Motivací bylo přiblížit spotřebu energie během dlouhých spánkových period blíže k teoretickému minimu, čímž se efektivně staly náklady energie za 'být dosažitelný' sítí zanedbatelnými ve srovnání s energií využitou pro skutečný přenos dat nebo měřicí úlohy.

Historicky tento koncept čerpá z technologií probouzejícího rádia v jiných nízkopříkonových bezdrátových standardech, jako je [IEEE](/mobilnisite/slovnik/ieee/) 802.11ba pro Wi-Fi. 3GPP jej přizpůsobilo pro kontext buněčného IoT v rámci frameworku NB-IoT. Jeho vytvoření bylo hnací silou potřeby učinit buněčné IoT konkurenceschopné vůči nebuněčným LPWAN technologiím (jako je LoRaWAN) v kritické metrice výdrže baterie, při zachování výhod licencovaného spektra, zabezpečení, kvality služeb a bezproblémové integrace do stávajících mobilních sítí.

## Klíčové vlastnosti

- Ultranízkopříkonová detekce prostřednictvím vyhrazeného přijímače pro probuzení (LP-WUR)
- Návrh signálu založený na sekvenci (např. Zadoff-Chu) pro spolehlivou detekci i v oblastech se špatným pokrytím
- Konfigurovatelné vysílací období a posun vůči pagingovým příležitostem
- Podporu vylepšení pokrytí prostřednictvím zvýšení výkonu a opakování
- Integrace s eDRX a Power Saving Mode (PSM) pro víceúrovňový správu napájení
- Definován pro provoz jak v idle režimu, tak v connected režimu s DRX

## Související pojmy

- [NPDSCH – Narrow Band Physical Downlink Shared Channel](/mobilnisite/slovnik/npdsch/)

## Definující specifikace

- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services

---

📖 **Anglický originál a plná specifikace:** [NWUS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nwus/)
