---
slug: "ctspch"
url: "/mobilnisite/slovnik/ctspch/"
type: "slovnik"
title: "CTSPCH – CTS Paging Channel"
date: 2025-01-01
abbr: "CTSPCH"
fullName: "CTS Paging Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ctspch/"
summary: "Vyhrazený kanál pro volání v sítích GSM/EDGE používaný speciálně pro okruhově spínané (CS) volání. Umožňuje efektivní sestavení příchozího hovoru tím, že síť může informovat mobilní stanice v klidovém"
---

CTSPCH je vyhrazený kanál pro volání v okruhově spínaných sítích GSM/EDGE, který informuje mobilní stanice v klidovém stavu o příchozích hlasových hovorech za účelem optimalizace kapacity volání a snížení prodlev při sestavování.

## Popis

Kanál pro volání [CTS](/mobilnisite/slovnik/cts/) (CTSPCH) je logický kanál v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), speciálně navržený pro operace volání související se službami s okruhovým přepínáním ([CS](/mobilnisite/slovnik/cs/)). Funguje jako součást rodiny Common Control Channel ([CCCH](/mobilnisite/slovnik/ccch/)), která spravuje signalizaci mezi sítí a mobilními stanicemi v klidovém režimu. Kanál je implementován prostřednictvím specifických časových slotů a přidělení frekvencí ve struktuře rámce GSM podle organizace multiframe definované v 3GPP TS 43.052.

Architektonicky existuje CTSPCH v rámci Base Station Subsystem ([BSS](/mobilnisite/slovnik/bss/)), kde Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)) vysílá zprávy volání na tomto kanálu podle pokynů z Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)). BSC přijímá žádosti o volání od Mobile Switching Center (MSC) přes rozhraní A a plánuje jejich vysílání na příslušné zdroje CTSPCH. Kanál používá specifické kódování a modulaci (obvykle Gaussian Minimum Shift Keying - GMSK), aby zajistil spolehlivý příjem mobilními stanicemi i na okraji buňky.

Z procesního hlediska, když je mobilní stanice v klidovém režimu (napojená na buňku, ale ne v aktivní komunikaci), periodicky monitoruje CTSPCH podle své přidělené skupiny volání. Skupina volání je vypočítána na základě International Mobile Subscriber Identity (IMSI) pomocí hashovacího algoritmu, který distribuuje mobilní stanice do různých příležitostí pro volání, aby se zabránilo přetížení. Když síť potřebuje sestavit příchozí CS hovor, odešle zprávu Paging Request obsahující Temporary Mobile Subscriber Identity (TMSI) nebo IMSI cílové mobilní stanice na CTSPCH během příslušné příležitosti pro volání.

Mobilní stanice detekuje svou identitu ve zprávě volání a reaguje zahájením žádosti o kanál na Random Access Channel (RACH), čímž začíná procedura sestavení hovoru. CTSPCH funguje vedle dalších kanálů pro volání, jako je kanál pro volání paketově spínaných (PS) služeb, ale je speciálně optimalizován pro CS služby s odlišnými časovými požadavky a formáty zpráv. Kanál podporuje jak plný, tak zkrácený formát zprávy volání, přičemž zkrácený formát se používá, když síť zná přesnou lokalizační oblast mobilní stanice, čímž se snižuje signalizační režie.

Klíčové komponenty zapojené do provozu CTSPCH zahrnují mapování logického kanálu Paging Channel (PCH) na fyzické zdroje, kanál Paging Indicator Channel (PICH) v některých implementacích pro efektivní indikaci volání a mechanismus Discontinuous Reception (DRX), který umožňuje mobilním stanicím šetřit baterii tím, že se probouzejí pouze během přidělených příležitostí pro volání. Kapacita kanálu je určena faktory, jako je počet přidělených časových slotů, distribuce skupin volání a strategie opakování zpráv volání používaná sítí.

## K čemu slouží

CTSPCH byl vytvořen, aby řešil základní potřebu efektivního sestavování příchozích hovorů v sítích GSM. Před jeho standardizací používaly rané implementace GSM obecné kanály pro volání, které nebyly optimalizovány pro různé typy služeb, což vedlo k neefektivnímu využití rádiových zdrojů a zvýšeným prodlevám při sestavování hovorů. Oddělení kanálů pro CS a PS volání umožnilo sítím upřednostňovat služby hlasu v reálném čase a zároveň jinak spravovat služby paketových dat.

Primární problém, který CTSPCH řeší, je spolehlivé doručování zpráv volání pro okruhově spínané hlasové hovory při minimalizaci spotřeby baterie v mobilních zařízeních. Implementací vyhrazeného kanálu pro CS volání s optimalizovaným časováním a kódováním mohly sítě dosáhnout rychlejší doby sestavení hovoru a lepší úspěšnosti volání. To bylo obzvláště důležité s rozšiřováním sítí GSM a potřebou zvládnout rostoucí hustotu účastníků bez zhoršení kvality hlasových služeb.

Historicky motivací pro CTSPCH byla evoluce sítí GSM směrem k efektivní podpoře jak hlasových, tak datových služeb. Se zavedením EDGE (Enhanced Data rates for GSM Evolution) se ukázala potřeba diferencovat mechanismy volání pro různé typy služeb. CTSPCH poskytl standardizovaný způsob zpracování CS volání, který byl zpětně kompatibilní s existující infrastrukturou GSM a zároveň nabízel lepší výkon oproti předchozím implementacím, které používaly sdílené zdroje pro volání pro všechny typy služeb.

## Klíčové vlastnosti

- Vyhrazený kanál pro operace okruhově spínaného (CS) volání
- Optimalizován pro sestavení příchozího hlasového hovoru
- Používá distribuční algoritmus skupin volání založený na IMSI
- Podporuje plný i zkrácený formát zprávy volání
- Implementuje Discontinuous Reception (DRX) pro úsporu energie
- Zpětně kompatibilní s legacy mechanismy volání GSM

## Definující specifikace

- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface

---

📖 **Anglický originál a plná specifikace:** [CTSPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ctspch/)
