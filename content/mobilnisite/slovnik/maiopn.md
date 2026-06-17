---
slug: "maiopn"
url: "/mobilnisite/slovnik/maiopn/"
type: "slovnik"
title: "MAIOPN – MAIO Permutation Number"
date: 2025-01-01
abbr: "MAIOPN"
fullName: "MAIO Permutation Number"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/maiopn/"
summary: "MAIO Permutation Number (číslo permutace MAIO) je parametr používaný ve frekvenčním skákání GSM/GPRS/EDGE k definování specifické permutace nebo uspořádání hodnot MAIO přiřazených různým časovým slotů"
---

MAIOPN je parametr používaný ve frekvenčním skákání GSM/GPRS/EDGE k definování specifického uspořádání hodnot MAIO napříč časovými sloty, optimalizující vzorce interference a využití zdrojů.

## Popis

[MAIO](/mobilnisite/slovnik/maio/) Permutation Number (MAIOPN) je parametr definovaný v 3GPP TS 45.914 související s pokročilými strategiemi alokace Mobile Allocation Index Offset (MAIO) ve systémech s frekvenčním skákáním. Zatímco MAIO přiřazuje offset jednotlivé mobilní stanici na konkrétním kanálu, MAIOPN řídí vzor nebo permutaci, ve které je sada hodnot MAIO distribuována napříč více časovými sloty nebo kanály v rámci buňky nebo sektoru. V podstatě se jedná o index, který vybírá předdefinovanou nebo algoritmicky generovanou sekvenci pro přiřazování MAIO k následujícím zdrojům, čímž zajišťuje strukturované a optimalizované rozdělení namísto náhodného nebo sekvenčního.

Z architektonického hlediska používá MAIOPN Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) jako součást svých algoritmů řízení rádiových zdrojů. Při konfiguraci buňky pro frekvenční skákání může operátor sítě definovat několik permutačních vzorů (každý asociovaný s MAIOPN), které určují, jak jsou dostupné hodnoty MAIO (0 až N-1, kde N je počet frekvencí v seznamu Mobile Allocation) mapovány na fyzické kanály (např. časové sloty TRX). Například jedna permutace může přiřazovat MAIO vzestupně napříč časovými sloty, zatímco jiná může používat přerušovaný nebo prokládaný vzor. BSC odkazuje na vybraný MAIOPN při alokaci kanálů pro nová volání nebo paketové relace.

Mechanismus funguje tak, že BSC udržuje vyhledávací tabulku nebo aplikuje generační funkci založenou na MAIOPN. Když je vyžadována aktivace nového kanálu na konkrétním časovém slotu, BSC určí další hodnotu MAIO k přiřazení na základě aktuálního stavu permutace pro danou buňku a sekvenci skákání. Tím je zajištěno, že celkové rozdělení MAIO napříč všemi aktivními časovými sloty sleduje plánovaný vzor navržený k maximalizaci separace mezi skákacími sekvencemi společně umístěných kanálů. To je obzvláště důležité ve scénářích s více transceivery (TRX), kde několik časových slotů skáče současně. Dobře navržená permutace minimalizuje pravděpodobnost, že dva časové sloty použijí ve stejný okamžik stejné nebo sousední frekvence, čímž snižuje vnitřní interferenci v rámci stejné buňky.

Role MAIOPN v síti spočívá v přidání další vrstvy optimalizace pro nasazení frekvenčního skákání. Zatímco [HSN](/mobilnisite/slovnik/hsn/) a MAIO řídí interferenci na úrovni jednotlivého kanálu, MAIOPN řídí interferenci na úrovni více kanálů, na úrovni buňky. Umožňuje síťovým plánovačům kontrolovat korelaci mezi skákacími vzory různých časových slotů, což může být klíčové pro výkon v buňkách s vysokou provozní zátěží. Výběrem vhodného MAIOPN mohou operátoři dosáhnout rovnoměrnějšího využití frekvenčního fondu, předejít 'shlukování' MAIO a dále vyhladit interferenci. To přispívá k vyšší celkové kapacitě buňky a konzistentnější kvalitě služeb, zejména pro datové služby jako [GPRS](/mobilnisite/slovnik/gprs/) a [EDGE](/mobilnisite/slovnik/edge/), kde propustnost je citlivá na úroveň interference.

## K čemu slouží

[MAIO](/mobilnisite/slovnik/maio/) Permutation Number byl zaveden k řešení omezení jednoduchého sekvenčního nebo libovolného přiřazování MAIO napříč více kanály v rámci jedné GSM buňky. Jak se sítě vyvíjely k podpoře více transceiverů a vyšších hustot provozu, riziko vnitřní interference – kdy si signály z různých časových slotů ve stejné buňce vzájemně interferují – se stalo významnějším. Sekvenční přiřazování MAIO (např. časový slot 0 dostane MAIO 0, časový slot 1 dostane MAIO 1 atd.) mohlo vést k situacím, kdy několik časových slotů skočí na těsně sousedící frekvence současně, zejména s určitými vzory [HSN](/mobilnisite/slovnik/hsn/), což degradovalo výkon. MAIOPN poskytuje řízenou metodu k de-korelaci těchto vzorů.

Tato technologie řeší problém suboptimálního řízení vnitrobuněčné interference. Definováním specifických permutací pro distribuci MAIO zajišťuje, že skákací sekvence souběžných kanálů jsou co nejvíce ortogonální vzhledem k dostupné sadě frekvencí. Tím maximalizuje přínosy frekvenčního skákání v rámci vlastních zdrojů buňky. Je obzvláště užitečná pro optimalizaci výkonu v sektorech s více TRX, kde je počet aktivních skákacích kanálů velký. Bez takové kontroly permutace by zákon průměrů mohl stále poskytovat diverzitu, ale záměrná permutace zaručuje lepší výkon v nejhorším případě a předvídatelnější chování sítě.

Historicky byl MAIOPN standardizován jako součást rozšířené sady funkcí pro GSM/[EDGE](/mobilnisite/slovnik/edge/) v 3GPP Release 8, zdokumentován v TS 45.914. Jeho vytvoření bylo motivováno potřebou nástrojů řízení rádiových zdrojů s jemnějším rozlišením, když sítě přecházely z primárně hlasových na smíšené hlasové a datové. Datové služby, se svými delšími dobami držení a vyššími požadavky na propustnost, jsou citlivější na přetrvávající podmínky interference. MAIOPN dal operátorům možnost ladit prostředí interference na úrovni buňky, čímž doplnil existující parametry HSN a MAIO. Představoval vývoj od základního frekvenčního skákání směrem k inteligentnímu, vícerozměrnému plánování skákacích vzorů, což umožnilo GSM sítím vytěžit maximální kapacitu a kvalitu ze svých spektrálních aktiv v konkurenčních podmínkách trhu.

## Klíčové vlastnosti

- Definuje permutační vzor pro distribuci hodnot MAIO napříč více časovými sloty nebo kanály
- Používá se BSC k optimalizaci vnitrobuněčné alokace MAIO
- Pomáhá minimalizovat korelaci mezi skákacími sekvencemi společně umístěných kanálů
- Zlepšuje rovnoměrnost využití frekvencí napříč zdroji buňky
- Snižuje vnitřní interferenci v rámci buňky, čímž zvyšuje celkovou kapacitu
- Poskytuje konfigurovatelný parametr pro pokročilé plánování rádiové sítě

## Související pojmy

- [MAIO – Mobile Allocation Index Offset](/mobilnisite/slovnik/maio/)
- [MAIOA – MAIO Allocation](/mobilnisite/slovnik/maioa/)

## Definující specifikace

- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [MAIOPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/maiopn/)
