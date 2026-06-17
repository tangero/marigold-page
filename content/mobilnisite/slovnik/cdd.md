---
slug: "cdd"
url: "/mobilnisite/slovnik/cdd/"
type: "slovnik"
title: "CDD – Cyclic Delay Diversity"
date: 2025-01-01
abbr: "CDD"
fullName: "Cyclic Delay Diversity"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cdd/"
summary: "Cyclic Delay Diversity (CDD) je technika vysílací diverzity používaná v systémech založených na OFDM, jako jsou LTE a 5G NR. Uměle vytváří frekvenčně selektivní útlum aplikací různých cyklických zpožd"
---

CDD je technika vysílací diverzity pro systémy OFDM, která aplikuje různé cyklické zpoždění na stejný signál přes více antén, aby uměle vytvořila frekvenčně selektivní útlum, čímž zlepšuje spolehlivost spoje bez nutnosti znalosti kanálu na straně vysílače.

## Popis

Cyclic Delay Diversity (CDD) je technika víceanténního vysílání navržená pro systémy s ortogonálním frekvenčním multiplexem ([OFDM](/mobilnisite/slovnik/ofdm/)). Na rozdíl od tradičních schémat prostorové diverzity, která vyžadují informaci o stavu kanálu na straně vysílače, CDD funguje jako metoda diverzity s otevřenou smyčkou, která vytváří umělou frekvenční selektivitu, aby využila inherentní frekvenční diverzitu dostupnou ve širokopásmových kanálech. Technika funguje tak, že z různých anténních portů jsou vysílány verzované verze stejného OFDM symbolu, přičemž zpoždění je implementováno jako cyklický posuv v časové oblasti před vysíláním.

Z architektonického hlediska je CDD implementována ve zpracovatelském řetězci fyzické vrstvy základnové stanice. Poté, co OFDM modulace vygeneruje časové vzorky pro symbol, systém vytvoří více verzí specifických pro antény aplikací různých cyklických posuvů na původní sekvenci vzorků. Tyto cyklické posuvy jsou pečlivě voleny tak, aby byly menší než délka cyklického prefixu OFDM, aby byla zachována ortogonalita mezi subnosnými a předešlo se mezisymbolovému rušení. Zpožděné verze jsou poté vysílány současně z různých fyzických antén, čímž vytvářejí na straně přijímače složený kanál, který se jeví jako frekvenčně selektivnější než skutečný fyzický kanál.

Z pohledu zpracování signálu CDD transformuje efektivní kanál, který přijímač zažívá. Když je stejný signál s různými cyklickými zpožděními vysílán z více antén, přijímač vidí to, co se jeví jako jediný přenos kanálem se zvýšenou frekvenční selektivitou. Tato umělá frekvenční selektivita přeměňuje kanál, který by mohl být s plochým útlumem, na frekvenčně selektivní, což umožňuje kanálovému kódování a prokládání na straně přijímače využít frekvenční diverzitu. Technika je zvláště účinná v kombinaci se schématy kanálového kódování, jako jsou turbo kódy nebo [LDPC](/mobilnisite/slovnik/ldpc/) kódy, protože zvýšené frekvenční variace poskytují dekodéru více diverzity.

Ve specifikacích 3GPP je CDD definována jako součást schémat vysílací diverzity pro víceanténní konfigurace. Pro systémy se 2 vysílacími anténami je standardizována konkrétní hodnota cyklického zpoždění, zatímco pro konfigurace se 4 vysílacími anténami je specifikována kombinace CDD s předkódováním. Implementační detaily, včetně přesných hodnot cyklického zpoždění a jejich aplikace pro různé přenosové režimy, jsou dokumentovány v 3GPP TS 36.211 pro fyzické kanály a modulaci, zatímco TS 36.213 pokrývá procedury fyzické vrstvy včetně toho, kdy a jak je CDD aplikována na základě konfigurace přenosového režimu a podmínek kanálu.

## K čemu slouží

CDD byla vyvinuta k řešení několika klíčových výzev v raných nasazeních LTE. Když mobilní sítě přecházely na rádiová rozhraní založená na [OFDM](/mobilnisite/slovnik/ofdm/) s LTE, návrháři systémů potřebovali efektivní víceanténní techniky, které by mohly poskytovat robustní výkon bez požadavku na rozsáhlou zpětnou vazbu o kanálu. Tradiční techniky [MIMO](/mobilnisite/slovnik/mimo/) s uzavřenou smyčkou, ačkoli potenciálně nabízely vyšší špičkové přenosové rychlosti, vyžadovaly přesnou informaci o stavu kanálu na straně vysílače, což bylo obtížné získat ve scénářích s vysokou mobilitou nebo s omezenými zdroji pro zpětnou vazbu. CDD poskytla elegantní řešení, které mohlo přinést spolehlivé zisky z diverzity s minimální režií.

Primární motivací pro CDD byla potřeba zlepšit výkon na okraji buňky a celkovou spolehlivost spoje v systémech OFDM. Ve širokopásmových OFDM přenosech zažívají různé subnosné různé podmínky kanálu. Umělým zvýšením této frekvenční selektivity prostřednictvím zpožděných přenosů CDD zajišťuje, že i když některé subnosné zažívají hluboké útlumy, jiné budou mít lepší podmínky kanálu. Tento diverzitní efekt je zvláště cenný pro řídicí kanály a kritické datové přenosy, kde je spolehlivost prvořadá. Technika také pomáhá zmírnit dopad korelace mezi anténními elementy v kompaktních instalacích základnových stanic.

Ve srovnání s dřívějšími diverzitními technikami, jako je Alamoutiho kódování v prostoru a čase, nabízela CDD implementační výhody pro systémy OFDM. Zatímco prostoro-časové kódy poskytovaly vynikající výkon, vyžadovaly specifické zpracování na straně přijímače a mohly být složité na implementaci pro více než dvě antény. CDD naopak mohla být snadno škálována na více antén a integrována s jinými přenosovými schématy. Dále kompatibilita CDD s ekvalizéry ve frekvenční oblasti běžně používanými v OFDM přijímačích z ní činila atraktivní volbu pro návrh fyzické vrstvy LTE, vyvažující zisky ve výkonu s implementační složitostí.

## Klíčové vlastnosti

- Provoz s otevřenou smyčkou nevyžadující zpětnou vazbu o stavu kanálu
- Vytváří umělou frekvenční selektivitu pro využití diverzity
- Zachovává ortogonalitu OFDM prostřednictvím zachování cyklického prefixu
- Kompatibilní se standardními OFDM přijímači a ekvalizéry
- Škalovatelná pro více konfigurací vysílacích antén
- Zlepšuje výkon kanálového kódování prostřednictvím zvýšené diverzity

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [CDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdd/)
