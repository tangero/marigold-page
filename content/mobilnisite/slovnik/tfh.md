---
slug: "tfh"
url: "/mobilnisite/slovnik/tfh/"
type: "slovnik"
title: "TFH – Total Frequency Hopping"
date: 2025-01-01
abbr: "TFH"
fullName: "Total Frequency Hopping"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tfh/"
summary: "Schéma skákání kmitočtů používané v GSM/EDGE, při kterém jak mobilní stanice, tak základnová stanice mění nosný kmitočet při každém výbuchu podle předdefinované sekvence. Zvyšuje robustnost spojení vů"
---

TFH je schéma skákání kmitočtů v GSM/EDGE, při kterém jak mobilní stanice, tak základnová stanice mění nosný kmitočet při každém výbuchu za účelem zvýšení odolnosti vůči rušení a útlumu.

## Popis

Total Frequency Hopping (TFH) je pokročilá technika skákání kmitočtů implementovaná v sítích GSM a [EDGE](/mobilnisite/slovnik/edge/). V systému GSM je rádiový kanál rozdělen na nosné kmitočty o šířce 200 kHz a rámce časového dělení ([TDMA](/mobilnisite/slovnik/tdma/)) obsahující 8 časových slotů. Skákání kmitočtů zahrnuje změnu nosného kmitočtu používaného pro vysílání a příjem výbuchů podle pseudonáhodného vzoru. TFH se vyznačuje tím, že tuto změnu kmitočtu aplikuje na *každý* výbuch pro daný kanál pro přenos hovoru/dat. To znamená, že pro jednotlivé volání nebo datovou relaci jsou po sobě jdoucí časové sloty (výbuchy) přenášeny na různých nosných kmitočtech podle sekvence skákání definované číslem hopping sequence ([HSN](/mobilnisite/slovnik/hsn/)) a parametrem Mobile Allocation Index Offset ([MAIO](/mobilnisite/slovnik/maio/)).

Sekvence skákání je odvozena z parametrů vysílaných na Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)) a přiřazena mobilní stanici během sestavování hovoru. MAIO zajišťuje, že různá spojení ve stejné buňce používají různá posunutí v rámci stejné sekvence skákání, čímž minimalizuje pravděpodobnost kolize. Sada kmitočtů dostupných pro skákání se nazývá Mobile Allocation ([MA](/mobilnisite/slovnik/ma/)) list. V režimu TFH musí být Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)) schopna vysílat a přijímat na všech kmitočtech v MA listu současně, což obvykle vyžaduje širokopásmový kombajner nebo schopnost skákání syntezátorem na každém vysílači/přijímači. To je v protikladu k Baseband Frequency Hopping ([BFH](/mobilnisite/slovnik/bfh/)), kde kmitočet vysílače BTS zůstává pevný a skákání je simulováno přepínáním časových slotů mezi různými vysílači/přijímači.

Z pohledu mobilní stanice musí rychle přelaďovat svůj syntezátor mezi výbuchy, aby sledovala sekvenci skákání. Tento proces zlepšuje výkon prostřednictvím kmitočtové diverzity. Protože mnohocestný útlum a rušení jsou kmitočtově selektivní, skákání rozprostírá expozici signálu na více kmitočtech. Tento průměrovací efekt snižuje pravděpodobnost, že hluboký útlum nebo přetrvávající rušení na jednom kmitočtu způsobí přerušení hovoru. Poskytuje také průměrování rušení, což rovnoměrněji rozděluje stejno-kanálové rušení mezi uživatele v kmitočtovém reusovacím vzoru, což může zvýšit celkovou kapacitu a kvalitu sítě.

## K čemu slouží

TFH byl vyvinut za účelem zvýšení výkonu a kapacity sítí GSM nad možnosti schémat bez skákání nebo s pomalým skákáním kmitočtů. Rané sítě GSM často používaly pevné přiřazení kmitočtu nebo pomalé skákání, což ponechávalo spojení zranitelná vůči trvalému rušení nebo hlubokému útlumu na konkrétním kmitočtu. V hustých městských prostředích s kmitočtovým reusem je stejno-kanálové rušení hlavním limitujícím faktorem.

TFH tyto problémy řeší přímo využitím kmitočtové diverzity. Tím, že nutí signál skákat po širokém pásmu při každém výbuchu, zajišťuje, že pokud je jeden kmitočet v hlubokém útlumu nebo silně rušen, následující výbuch bude pravděpodobně na lepším kmitočtu. Korekční kódování (a prokládání přes více výbuchů) v GSM pak může informaci obnovit. Díky tomu je spojení robustnější, což umožňuje nižší vysílací výkon (snížení rušení pro ostatní) a/nebo poskytuje lepší kvalitu hlasu a datový propust na okraji buňky. Kromě toho díky randomizaci použití kmitočtu mezi všemi uživateli v buňce TFH přeměňuje koncentrované stejno-kanálové rušení na šum na pozadí, který je průměrován napříč všemi spojeními, což vede k předvídatelnějšímu a lépe zvladatelnému prostředí rušení. To umožňuje plánovačům sítí používat těsnější kmitočtové reusové vzory, čímž se zvyšuje spektrální účinnost a celková kapacita sítě.

## Klíčové vlastnosti

- Změna kmitočtu nastává při každém TDMA výbuchu (každých 577 µs)
- Vyžaduje, aby BTS podporovala skákání syntezátorem nebo širokopásmový kombajner
- Využívá pseudonáhodnou sekvenci definovanou parametry HSN a MAIO
- Poskytuje maximální zisky z kmitočtové diverzity a průměrování rušení
- Zvyšuje odolnost vůči mnohocestnému útlumu a stejno-kanálovému rušení
- Umožňuje těsnější kmitočtový reus, čímž zvyšuje kapacitu sítě

## Definující specifikace

- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface
- **TS 45.056** (Rel-19) — GSM CTS-FP Radio Requirements

---

📖 **Anglický originál a plná specifikace:** [TFH na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfh/)
