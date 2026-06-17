---
slug: "nbin"
url: "/mobilnisite/slovnik/nbin/"
type: "slovnik"
title: "NBIN – Narrowband Interference Number"
date: 2025-01-01
abbr: "NBIN"
fullName: "Narrowband Interference Number"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nbin/"
summary: "Parametr používaný v sekvencích frekvenčního přeskakování v GSM a příbuzných systémech k určení vzorů přeskakování a zmírnění rušení. Ovlivňuje přidělování rádiových kanálů, zvyšuje kapacitu sítě a sn"
---

NBIN je parametr používaný v sekvencích frekvenčního přeskakování (frequency hopping) v GSM k určení vzorů přeskakování, zmírnění rušení a optimalizaci alokace kanálů za účelem zlepšení kapacity sítě a kvality hovoru.

## Popis

Narrowband Interference Number (NBIN) je parametr definovaný ve specifikacích 3GPP pro algoritmy frekvenčního přeskakování, zejména v GSM a jeho evolučních verzích. Je součástí procesu generování sekvence přeskakování, který určuje, jak mobilní stanice a základnové stanice v čase přepínají mezi rádiovými frekvenčními kanály. NBIN funguje tak, že je spolu s dalšími parametry, jako je Mobile Allocation Index Offset ([MAIO](/mobilnisite/slovnik/maio/)) a Hopping Sequence Number ([HSN](/mobilnisite/slovnik/hsn/)), vložen do matematického algoritmu za účelem vytvoření pseudonáhodného vzoru přeskakování. Tento vzor diktuje pořadí, v jakém se frekvence používají během přenosu, čímž rozprostírá rušení napříč více kanály a snižuje dopad úzkopásmových rušičů nebo útlumu na konkrétních frekvencích.

V provozu sítě je NBIN konfigurován operátorem sítě a sdělen mobilní stanici prostřednictvím zpráv systémových informací. Ovlivňuje periodicitu a distribuci sekvence přeskakování, čímž zajišťuje, že sousední buňky používají různé vzory pro minimalizaci ko-kanálového rušení. Mezi klíčové komponenty patří samotný algoritmus frekvenčního přeskakování, který používá modulární aritmetiku k mapování časových slotů na frekvenční kanály, a tabulka přidělení frekvencí sítě. Variací NBIN napříč buňkami systém dosahuje frekvenční diverzity, čímž zlepšuje odolnost signálu a celkovou kapacitu. To je zvláště důležité v GSM, kde je frekvenční opakované využití těsné a řízení rušení je pro kvalitu hovoru klíčové.

Role NBIN sahá až ke zlepšení výkonu spojení v náročných rádiových podmínkách. Přeskakováním napříč frekvencemi systém průměruje účinky rušení a vícecestného útlumu, což vede ke konzistentnější chybovosti přenosu. V GSM je to implementováno v podsystému základnové stanice ([BSS](/mobilnisite/slovnik/bss/)), kde základnová přenosová stanice ([BTS](/mobilnisite/slovnik/bts/)) a mobilní stanice synchronizují své sekvence přeskakování na základě NBIN a dalších parametrů. Zatímco pokročilejší systémy jako UMTS a LTE používají jiné techniky zmírnění rušení (např. scrambling codes a [OFDMA](/mobilnisite/slovnik/ofdma/)), NBIN zůstává relevantní v nasazeních GSM a jako základní koncept pro principy frekvenčního přeskakování s rozprostřeným spektrem (FHSS) v bezdrátových komunikacích.

## K čemu slouží

NBIN byl vytvořen za účelem optimalizace frekvenčního přeskakování v sítích GSM, řeší problém ko-kanálového rušení a frekvenčně selektivního útlumu v celulárním prostředí. Před zavedením frekvenčního přeskakování trpěly sítě GSM zhoršenou kvalitou hovorů, když mobilní stanice zažívaly přetrvávající rušení na pevných kanálech. Zavedením sekvencí přeskakování parametrizovaných pomocí NBIN umožnila 3GPP dynamické přidělování frekvencí, které rozprostírá rušení, a tím zlepšuje celkový výkon a kapacitu sítě.

Motivace pro NBIN vychází z potřeby zvýšit spektrální účinnost v těsně uspořádaných vzorech frekvenčního opakovaného využití. V raných nasazeních GSM bez přeskakování mohlo rušení způsobovat přerušené hovory a špatnou kvalitu hovoru, zejména v hustě obydlených městských oblastech. NBIN jako součást algoritmu přeskakování umožňuje každé buňce používat jedinečný vzor, čímž snižuje pravděpodobnost, že dvě blízké buňky budou současně rušit na stejné frekvenci. Tím řeší omezení statického přidělování kanálů zavedením náhodnosti a diverzity, čímž se síť stává odolnější vůči úzkopásmovým rušičům z externích zdrojů nebo jiných buněk.

Historicky byl NBIN standardizován v 3GPP Release 5 jako součást vylepšených funkcí GSM, navazujících na dřívější koncepty přeskakování z vojenských komunikací. Poskytl strukturovaný způsob správy sekvencí přeskakování napříč zařízeními od různých dodavatelů, čímž zajišťoval interoperabilitu. Zatímco jeho přímé použití s novějšími technologiemi pokleslo, NBIN představuje důležitý krok v řízení rušení, který ovlivnil pozdější vývoj v oblasti frekvenční agility a strategií přidělování zdrojů pro mobilní sítě.

## Klíčové vlastnosti

- Parametr pro generování pseudonáhodných sekvencí frekvenčního přeskakování
- Snižuje ko-kanálové rušení a zmírňuje frekvenčně selektivní útlum
- Zvyšuje frekvenční diverzitu a kapacitu sítě v systémech GSM
- Konfigurovatelný na buňku pro optimalizaci vzorů přeskakování v celé síti
- Spolupracuje s HSN a MAIO k definování jedinečných sekvencí přeskakování
- Podporuje synchronizaci mezi BTS a mobilními stanicemi pro přeskakování

## Související pojmy

- [HSN – Hopping Sequence Number](/mobilnisite/slovnik/hsn/)
- [MAIO – Mobile Allocation Index Offset](/mobilnisite/slovnik/maio/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [NBIN na 3GPP Explorer](https://3gpp-explorer.com/glossary/nbin/)
