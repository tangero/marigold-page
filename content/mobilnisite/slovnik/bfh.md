---
slug: "bfh"
url: "/mobilnisite/slovnik/bfh/"
type: "slovnik"
title: "BFH – Bad Frame Handling"
date: 2025-01-01
abbr: "BFH"
fullName: "Bad Frame Handling"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/bfh/"
summary: "Bad Frame Handling (BFH) je mechanismus 3GPP pro správu poškozených nebo ztracených řečových rámců v hlasových službách. Zajišťuje kontinuitu hovoru a srozumitelnost skrytím nebo rekonstrukcí poškozen"
---

BFH je mechanismus 3GPP pro správu poškozených nebo ztracených řečových rámců v hlasových službách, který zajišťuje kontinuitu hovoru a srozumitelnost skrytím nebo rekonstrukcí poškozených rámců.

## Popis

Bad Frame Handling (BFH) je standardizovaná technika maskování chyb definovaná ve specifikacích 3GPP pro hlasové kodeky, především pro kodeky Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Funguje na aplikační vrstvě, konkrétně v dekodéru řečového kodeku, aby zmírnila slyšitelný dopad poškozených nebo zcela ztracených řečových rámců, k nimž dochází v důsledku přenosových chyb přes rádiové rozhraní. Proces je spuštěn, když dekodér obdrží rámec označený jako 'bad' (špatný) mechanismy detekce chyb fyzické vrstvy (jako jsou kontroly [CRC](/mobilnisite/slovnik/crc/)) nebo když rámec zcela chybí (vymazání rámce).

Při detekci špatného rámce algoritmus BFH nevypisuje prosté ticho, což by způsobilo slyšitelné kliknutí nebo výpadek. Místo toho využívá sofistikované zpracování signálu ke generování náhradního rámce. To zahrnuje použití parametrů z dříve správně přijatých rámců k extrapolaci nebo rekonstruci věrohodného řečového signálu. Mezi techniky patří opakování tvaru vlny, interpolace parametrů a potlačování přechodů. Dekodér používá excitační signál a paramelineární prediktivního kódování ([LPC](/mobilnisite/slovnik/lpc/)) z posledního dobrého rámce k syntéze náhrady, přičemž postupně utlumuje výstupní úroveň, pokud dojde k po sobě jdoucím špatným rámcům, aby signalizoval přirozené vyvanutí namísto náhlého zastavení.

Architektura BFH je nedílnou součástí rámce odolnosti kodeku a často funguje ve spojení s dalšími funkcemi, jako jsou parametry kvality služby (QoS) přístupového rádiového beareru ([RAB](/mobilnisite/slovnik/rab/)) pro nerovnoměrnou ochranu proti chybám. Jejím úkolem je zachovat srozumitelnost a přirozenost řeči a slouží jako poslední obranná linie poté, co schémata opravy chyb na nižších vrstvách (předzpětná korekce – [FEC](/mobilnisite/slovnik/fec/)) a mechanismy opakování přenosu (jako [HARQ](/mobilnisite/slovnik/harq/) v RAN) nedokázaly doručit bezchybný rámec. Skrytím chyb BFH přímo přispívá k vnímanému výsledku středního hodnocení ([MOS](/mobilnisite/slovnik/mos/)) hlasového hovoru, což z něj činí kritickou součást pro uživatelský zážitek, zejména na okraji buňky nebo ve scénářích s vysokým rušením.

## K čemu slouží

BFH byl vytvořen, aby řešil základní výzvu poskytování přijatelné hlasové kvality přes náchylné rádiové kanály. Před jeho standardizací systémy buď žádné maskování neměly (což vedlo k velmi špatnému uživatelskému zážitku při útlumech), nebo používaly proprietární, neinteroperabilní metody. Omezení spočívající pouze v opravě chyb na fyzické vrstvě jsou vysoká spotřeba přenosové kapacity a zavedení zpoždění; pokud chyby nelze opravit, hlasová služba by se výrazně zhoršila. BFH poskytuje řešení na vyšší, aplikačně specifické vrstvě, které efektivně maskuje zbytkové chyby.

Jeho zavedení v 3GPP Rel-8 spolu s kodekem AMR bylo motivováno potřebou robustního, standardizovaného přístupu k zajištění konzistentní hlasové kvality napříč různými síťovými zařízeními a výrobci terminálů. Řeší problém vnímání přerušení hovoru a ztráty srozumitelnosti při dočasném zhoršení signálu. Maskováním ztrát rámců zabraňuje tomu, aby hovor zněl 'přerušovaně', a snižuje frustraci uživatelů, což je zásadní pro přijetí služby a metriky spolehlivosti sítě. Historicky se vyvinul z jednodušších technik utlumování k parametrickému maskování používanému dnes, což umožňuje plynulé služby i při vývoji sítí přes HSPA, LTE až po 5G NR pro hlasové služby.

## Klíčové vlastnosti

- Maskuje poškozené řečové rámce označené nižšími vrstvami jako 'bad' (špatné)
- Zvládá po sobě jdoucí vymazání rámců s progresivním útlumem signálu
- Pro rekonstrukci využívá interpolaci parametrů z předchozích dobrých rámců
- Funguje integrovaně v dekodérech kodeků AMR, AMR-WB a EVS
- Zlepšuje percepční kvalitu řeči a výsledek středního hodnocení (MOS)
- Funguje nezávisle na rádiové technologii (aplikovatelné na GSM, UMTS, LTE, NR)

## Definující specifikace

- **TS 26.091** (Rel-19) — AMR Error Concealment Procedure
- **TS 26.102** (Rel-19) — Mapping of AMR and other codecs to interfaces
- **TS 26.191** (Rel-19) — AMR-WB Error Concealment Procedure
- **TS 26.202** (Rel-19) — AMR-WB Speech Codec Mapping Specification
- **TS 46.085** (Rel-19) — GSM Speech Codec Interoperability Test Report

---

📖 **Anglický originál a plná specifikace:** [BFH na 3GPP Explorer](https://3gpp-explorer.com/glossary/bfh/)
