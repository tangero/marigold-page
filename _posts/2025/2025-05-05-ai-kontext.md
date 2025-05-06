---
author: Patrick Zandl
categories:
- AI
- kontext
layout: post
post_excerpt: A především, proč je tak drahé a zdlouhavé zvyšovat velikost kontextu?
thumbnail: https://www.marigold.cz/assets/llm-kontext.jpg
title: Proč je velikost kontextu u LLM tak důležitá?
---

A především, proč je tak drahé a zdlouhavé zvyšovat velikost kontextu? Tento článek se podrobně zabývá tím, co kontext znamená, proč je jeho délka kritická, jaké technické překážky brání jeho neomezenému rozšiřování a jaká řešení se v současnosti vyvíjejí.

__Co konkrétně se v tomto článku dozvíte?__ 
* Obsah
{:toc} 

Velké jazykové modely (LLM) jako GPT-4, Claude 3 nebo Gemini 2.5 se staly výkonnými nástroji pro zpracování přirozeného jazyka. Jejich schopnost generovat text, překládat, odpovídat na otázky a psát kód je využívána v mnoha oblastech. Navzdory jejich pokročilým schopnostem však narážejí na významné omezení: efektivní zpracování velmi dlouhých sekvencí dat, známé jako "problém dlouhého kontextu". 

## Co je kontext a proč je jeho délka klíčová?

V případě LLM představuje kontext (context window) veškerá data, která má model k dispozici v daném okamžiku pro zpracování a generování odpovědi. Funguje jako operační paměť modelu. Pokud si LLM chce něco pamatovat v rámci rozhovoru, předává si to jako kontext, ačkoliv to třeba nevidíte. Pokud má LLM pracovat s vašimi předchozími zprávami v rámci chatu, prostě je přibalí do posílaných dat. Obsah kontextu typicky zahrnuje:

1.  Vstupní text (prompt): Zadání nebo otázka od uživatele.
    
2.  Historie konverzace: Předchozí výměny v rámci aktuální interakce. U některých systémů může zahrnovat i relevantní informace z minulých interakcí (např. pomocí explicitních paměťových mechanismů).
    
3.  Poskytnuté dokumenty: Externí texty, které má model analyzovat, shrnout nebo z nich čerpat informace (např. nahrané PDF, webové stránky).
    
4.  Interní instrukce: Systémové prompty definující chování modelu, jeho personu nebo specifické úkoly.
    
5.  Vygenerovaný text: Část textu, kterou model sám postupně generuje jako odpověď.
    

Délka kontextu, obvykle měřená v tokenech, definuje maximální množství informací, které model může současně zpracovat. Token je základní jednotka textu pro LLM, která může odpovídat slovu, části slova nebo interpunkčnímu znaménku (pro hlubší vysvětlení viz článek [Tokeny versus Slova](/ai/tokeny-versus-slova)).

### Význam délky kontextu pro kvalitu výstupu:

-   Porozumění souvislostem: Delší kontext umožňuje modelu lépe zachytit složité vztahy, závislosti a nuance v rozsáhlých textech.
    
-   Konzistence: Schopnost udržet jednotný styl, téma a faktickou správnost napříč dlouhými konverzacemi nebo dokumenty.
    
-   Přesnost a relevance: Přístup k většímu množství relevantních informací vede k přesnějším a lépe zacíleným odpovědím.
    
-   Zpracování komplexních úloh: Úlohy jako detailní analýza rozsáhlých reportů, knih nebo kódových bází vyžadují schopnost pojmout velké množství dat najednou.
    
-   Omezení "halucinací": Poskytnutí dostatečného kontextu může snížit tendenci modelu vymýšlet si informace, které nejsou ve vstupních datech.
    

### Aktuální velikosti kontextových oken a ceny (květen 2025)

Velikost kontextového okna a cena jsou klíčové parametry při výběru modelu. Níže je uveden přehled některých populárních modelů s daty převážně z OpenRouter (duben 2025):

| **Model** | **Kontextové okno (Max vstup)** | **Max. výstup** | **Cena vstupu ($/1M tokenů)** | **Cena výstupu ($/1M tokenů)** |
|-----------|----------------------------------|-----------------|-------------------------------|--------------------------------|
| o3 (OpenAI) | 200 000 | 100 000 | $10.00 | $40.00 |
| o4-Mini (OpenAI) | 200 000 | 100 000 | $1.10 | $4.40 |
| o4-Mini High (OpenAI) | 200 000 | 100 000 | $1.10 | $4.40 |
| GPT-4.1 (OpenAI) | 1 050 000 | 33 000 | $2.00 | $8.00 |
| Claude 3.7 Sonnet | 200 000 | 64 000 | $3.00 | $15.00 |
| Claude 3.7 Sonnet Think | 200 000 | 64 000 | $3.00 | $15.00 |
| Gemini 2.5 Pro (Google) | 1 050 000 | 66 000 | $1.25 - $2.50 | $10.00 - $15.00 |
| Grok 3 beta (xAI) | 131 000 | 131 000 | $3.00 | $15.00 |
| Llama 4 | 10 milionů | - | (Open Source) | (Open Source) |
| Jamba-1.5 (AI21, OS) | 256 000 | - | (Open Source) | (Open Source) |

Poznámka: Ceny se mohou lišit v závislosti na poskytovateli API (zde OpenRouter) a aktuálním vytížení. U Gemini 2.5 Pro jsou ceny uvedeny v rozsahu. Open-source modely nemají přímé ceny za token, ale náklady na jejich provoz. Hodnota u LLAMA 4 je velmi optimistická, model na to nebyl řádně testován a výsledky nejsou příliš kvalitní.

  

Je důležité poznamenat, že nominální délka kontextového okna nemusí vždy odpovídat efektivní schopnosti modelu využívat informace z celého kontextu. Testy jako "Needle In A Haystack" (NIAH) ukazují, že některé modely mají problémy s vyhledáváním informací umístěných uprostřed velmi dlouhého kontextu (tzv. "lost in the middle" problém), i když se tento problém postupně daří zmírňovat.

Už teď je tedy zřejmé, že na rozsahu kontextu záleží, přičemž “kontext” není jen to, co zadáte do Prompt okna v ChatGPT, ale také spousta dodatečných dat, kterými ChatGPT váš dotaz “obalí”, aby využil toho, co ví o vás, o tom, co vyžadujete atd. Nabízí se tedy otázka, proč se jednoduše velikost kontextového okna nerozšíří na maximum! Odpověď? Protože to není vůbec jednoduché a především to stojí hromadu peněz při používání! Jak to?

## Jádro problému: Kvadratická složitost mechanismu pozornosti

Základem většiny moderních LLM je architektura transformátoru, představená v roce 2017 v článku "Attention Is All You Need". Klíčovou inovací této architektury je mechanismus sebe-pozornosti (self-attention). Ten umožňuje modelu vážit důležitost všech ostatních tokenů v kontextu při zpracování každého jednotlivého tokenu.

Jak to funguje (velmi zjednodušeně): model se při čtení každého slova “dívá” na všechna ostatní slova v textu, aby pochopil jeho význam v dané větě. Tedy počítá jej vůči všem předchozím slovům. Tímto způsobem zjišťuje, která slova jsou pro aktuální slovo nejdůležitější a jak spolu souvisí. Proto prodlužování textu zvyšuje náročnost výpočtů exponenciálně.

Jak funguje (méně zjednodušeně): Pro každý token model vypočítá tři vektory: Query (Q), Key (K) a Value (V). Poté pro každý token (reprezentovaný jeho Q vektorem) vypočítá skóre pozornosti vůči všem ostatním tokenům (porovnáním Q s K vektory všech tokenů). Tato skóre se normalizují (typicky pomocí funkce softmax) a použijí se k vytvoření váženého součtu V vektorů všech tokenů. Výsledkem je nová reprezentace tokenu, která zohledňuje jeho vztah ke všem ostatním tokenům v kontextu.

Problém škálování: Tento mechanismus je extrémně efektivní pro zachycení závislostí v textu, ale má zásadní nevýhodu: jeho výpočetní a paměťová složitost roste kvadraticky s délkou sekvence (N, počet tokenů).

-   Výpočetní složitost: Počet operací potřebných pro výpočet matice pozornosti je úměrný O(N2). Pro každý z N tokenů musíme vypočítat jeho vztah k N tokenům (včetně sebe sama).
    
-   Paměťová složitost: Model si musí během výpočtu uchovávat matici pozornosti o velikosti N×N, což vede k paměťové náročnosti O(N2).
    

Ilustrace dopadu:

Přesné časy zpracování závisí na mnoha faktorech (konkrétní model, hardware - např. typ GPU, optimalizace - např. FlashAttention, datový typ výpočtů), ale pro ilustraci řádového nárůstu náročnosti na výkonném GPU (např. NVIDIA H100/B100):

-   Kontext 1 000 tokenů: Vyžaduje řádově 10002=1000000 operací/paměťových jednotek. Zpracování (inference) může trvat zlomky sekundy až jednotky sekund.
    
-   Kontext 10 000 tokenů: Vyžaduje řádově 100002=100000000 operací/paměťových jednotek (100x více). Doba zpracování se může pohybovat v jednotkách až desítkách sekund.
    
-   Kontext 100 000 tokenů: Vyžaduje řádově 1000002=10000000000 operací/paměťových jednotek (10 000x více než pro 1k tokenů). Doba zpracování může dosahovat desítek sekund až několika minut.
    
-   Kontext 1 000 000 tokenů (jako u Gemini Pro, GPT-4.1): Vyžaduje řádově 10000002=1000000000000 (bilion) operací/paměťových jednotek. Doba zpracování se může pohybovat v řádu několika minut až desítek minut, silně závisí na optimalizacích a počtu použitých akcelerátorů.
    

Tento kvadratický nárůst představuje obrovskou bariéru pro neomezené prodlužování kontextového okna u standardních transformátorů, jak z hlediska výpočetní náročnosti (čas), tak paměťových požadavků.

## Praktické důsledky kvadratické složitosti

Kvadratická složitost mechanismu pozornosti má několik zásadních praktických dopadů. Především vede k enormní výpočetní náročnosti a latenci při zpracování dlouhých kontextů. Vyžaduje to obrovské množství výpočetních zdrojů, jako jsou GPU nebo TPU, což se projevuje delší dobou odezvy při generování odpovědí, vysokou spotřebou energie a následně i vysokými náklady na trénink a inferenci modelů kvůli potřebě výkonného a drahého hardwaru. Proto jsou modely, které mají velké množství parametrů a umožňují zpracovat velký kontext, také zpravidla výrazně dražší.

Dalším významným důsledkem jsou vysoké paměťové nároky, zejména na VRAM akcelerátorů. Model musí uchovávat matice pozornosti a mezivýpočty (aktivace) pro všechny tokeny v kontextu. Například optimalizace zvaná KV cache, která ukládá vypočtené vektory pro zrychlení inference, vyžaduje pro model Llama 3 70B s kontextem 128 000 tokenů stovky gigabajtů VRAM. Pro kontexty v řádu milionů tokenů tyto nároky dále dramaticky rostou, což omezuje nasazení takových modelů pouze na hardware s masivní paměťovou kapacitou.

Tyto zvýšené výpočetní a paměťové nároky se promítají do ekonomických dopadů. Poskytovatelé LLM služeb musí tyto náklady zohlednit, a proto zpravidla účtují vyšší ceny za použití modelů s delšími kontextovými okny nebo za zpracování tokenů přesahujících určitou hranici, jak je vidět v přehledové tabulce cen.

Nakonec, i když model technicky zvládne zpracovat velmi dlouhý kontext, objevuje se problém známý jako "Lost in the Middle". Empirické testy ukazují, že schopnost modelu efektivně využívat informace může klesat, pokud jsou tyto informace umístěny uprostřed velmi dlouhého vstupního textu. Modely často vykazují tendenci lépe pracovat s informacemi uvedenými na začátku nebo na konci kontextového okna.

## Současné přístupy a řešení

Výzkum a vývoj se intenzivně zaměřují na zmírnění nebo překonání O(N2) bariéry, protože překročení limitů přinášených kontextem by umožňovalo výrazně rozšířit úlohy, v nichž AI / LLM excelují. A také dosáhnout lepší ekonomiky. Hlavní směry výzkumu jsou zhruba následující:

### 1. Optimalizace standardní pozornosti

-   FlashAttention (a jeho následovníci FlashAttention-2, FlashAttention-3): Algoritmus, který restrukturalizuje výpočet pozornosti tak, aby lépe využíval hierarchii paměti GPU. Minimalizuje pomalé přesuny dat mezi HBM (High Bandwidth Memory) a SRAM (on-chip paměť) pomocí technik jako tiling a recomputation. Výrazně zrychluje výpočet a snižuje paměťové nároky bez změny matematiky pozornosti, takže výsledky jsou (téměř) identické se standardní pozorností. Stal se de facto standardem pro trénink a inferenci moderních LLM.
    
-   KV Cache (Key-Value Cache): Optimalizace pro inferenci (generování textu). Místo přepočítávání K a V vektorů pro všechny předchozí tokeny při generování každého nového tokenu se tyto vektory ukládají do paměti (cache). To snižuje výpočetní náročnost generování z O(N2) na O(N) pro každý nový token, ale paměťová náročnost pro uložení cache zůstává O(N).
    

### 2. Aproximace pozornosti (Řídká pozornost - Sparse Attention)

Cílem tohoto přístupu je snížit počet párů tokenů, mezi kterými se počítá pozornost, a tím prolomit kvadratickou složitost výpočtu plné matice pozornosti. Místo aby každý token interagoval se všemi ostatními, interakce se omezí na "řídký" vzor, který se snaží zachovat nejdůležitější informace. Longformer například kombinuje lokální pozornost, kde každý token interaguje pouze se svými nejbližšími sousedy v rámci "klouzavého okna", s globální pozorností pro několik předem určených tokenů (např. speciální tokeny jako [CLS]). Tyto globální tokeny mohou interagovat se všemi ostatními tokeny a všechny ostatní tokeny mohou interagovat s nimi, což umožňuje přenos informací napříč celou sekvencí při zachování převážně lokálních výpočtů. Podobně BigBird používá kombinaci tří typů řídké pozornosti: náhodnou pozornost (každý token interaguje s malým náhodným vzorkem ostatních tokenů), okénkovou pozornost (podobně jako Longformer) a globální pozornost. Tato kombinace má teoretické základy a snaží se efektivně aproximovat vlastnosti plné matice pozornosti. Jiné metody, jako Routing Transformer nebo Sinkhorn Transformer, jdou ještě dál a snaží se dynamicky "naučit" nebo optimalizovat, které páry tokenů jsou nejdůležitější pro výpočet pozornosti, například pomocí technik směrování informací nebo metod inspirovaných optimálním transportem (Sinkhorn), čímž se výpočty soustředí pouze na nejrelevantnější části matice pozornosti.

Ačkoliv tyto metody mohou dosáhnout lineární (O(N)) nebo téměř lineární (O(NlogN)) výpočetní složitosti, kompromisem může být mírné snížení kvality modelu oproti plné pozornosti. Důvodem je, že předdefinované nebo aproximované vzory řídké pozornosti nemusí vždy dokonale zachytit všechny relevantní dlouhodobé závislosti v textu, které by plná pozornost identifikovala.

### 3. Alternativní architektury (mimo transformátory)

Hledání architektur, které nejsou založeny na standardní O(N2) pozornosti:

-   Rekurentní [neuronové sítě](/ai/neuronove-site/) (RNN) / LSTM / GRU: Tyto sítě představují starší přístup ke zpracování sekvencí, jehož kořeny sahají až do 80. a 90. let 20. století. Základní myšlenka RNN spočívá ve zpracování sekvence krok za krokem (token po tokenu), přičemž si síť udržuje vnitřní "stav" nebo "paměť", která shrnuje informace z předchozích kroků. Tento stav se aktualizuje při zpracování každého nového tokenu. Díky tomu má zpracování inherentně lineární výpočetní složitost (O(N)), protože výpočet pro každý token závisí pouze na aktuálním vstupu a předchozím stavu, nikoli na všech předchozích tokenech současně. Varianty jako LSTM (Long Short-Term Memory, Hochreiter & Schmidhuber, 1997) a GRU (Gated Recurrent Unit) byly vyvinuty později, aby řešily klíčový problém základních RNN: tzv. mizení nebo explozi gradientů (vanishing/exploding gradients), které bránily učení závislostí na dlouhé vzdálenosti v sekvenci. Přestože LSTM a GRU tento problém zmírnily pomocí speciálních "bran" (gates), které řídí tok informací a gradientů, stále měly své limity. Hlavní nevýhodou oproti transformátorům se ukázala být jejich sekvenční povaha, která znesnadňuje paralelizaci výpočtů během tréninku na moderním hardwaru (GPU/TPU). Transformátory, které mohou zpracovávat všechny tokeny v sekvenci víceméně paralelně díky mechanismu pozornosti, se tak staly efektivnější pro trénink na velkých datech a dosáhly lepších výsledků v mnoha úlohách. Moderní výzkum se však k RNN a jejich vylepšením částečně vrací, snaží se kombinovat jejich výhody (lineární složitost) s novými technikami pro zlepšení výkonu a paralelizace.
    
-   State Space Models (SSM): Třída modelů inspirovaná teorií řízení.
    

-   Mamba: Populární SSM architektura, která dosahuje lineární složitosti škálování s délkou sekvence a zároveň si zachovává schopnost modelovat dlouhé závislosti díky selektivnímu mechanismu stavu. Ukazuje slibné výsledky, zejména v úlohách vyžadujících dlouhý kontext. Existují i novější varianty a vylepšení (Mamba-2, etc.).
    

-   Hybridní modely: Kombinují různé přístupy.
    

-   Jamba (AI21 Labs): Architektura, která střídá vrstvy standardní pozornosti (Transformer bloky) s Mamba bloky. Cílem je zkombinovat sílu pozornosti pro lokální a komplexní vztahy s efektivitou Mamby pro dlouhé sekvence. Výsledkem je model, který zvládá dlouhý kontext (256k tokenů) s výrazně nižšími paměťovými nároky než čistý transformátor podobné velikosti. Očekávají se nástupci.
    

### 4. Retrieval-Augmented Generation (RAG)

Alternativní přístup, který se nesnaží vtěsnat veškeré informace do kontextového okna modelu. Místo toho postupuje zhruba následovně:

1.  Rozsáhlá databáze znalostí (např. dokumenty, webové stránky) je indexována a uložena ve vektorové databázi.
    
2.  Když přijde dotaz uživatele, systém nejprve vyhledá nejrelevantnější části informací z databáze (retrieval).
    
3.  Tyto relevantní části (snippets) jsou pak spolu s původním dotazem vloženy do kontextového okna LLM.
    
4.  LLM použije tyto poskytnuté informace k vygenerování odpovědi.
    

Výhody RAG: Může pracovat s prakticky neomezeným množstvím externích dat bez nutnosti extrémně dlouhého kontextového okna. Je snadnější aktualizovat znalosti (stačí aktualizovat databázi).

Nevýhody RAG: Kvalita závisí na úspěšnosti vyhledávacího kroku. Model nemá "holistický" pohled na celý dokument, jen na vybrané části. Nemusí být vhodný pro úlohy vyžadující syntézu informací napříč celým rozsáhlým textem.

### 5. Další techniky

-   Context Compression: Metody, které se snaží zkrátit prompt nebo odstranit méně relevantní části kontextu před jeho předáním modelu.
    
-   Ring Attention: Technika pro distribuovaný trénink/inferenci, která umožňuje rozdělit zpracování dlouhého kontextu mezi více akcelerátorů (GPU) tak, že každý zpracovává část sekvence, ale mohou si efektivně vyměňovat informace potřebné pro výpočet pozornosti napříč celou sekvencí.
    

## Výzvy a budoucí směřování

Navzdory pokrokům zůstává efektivní a kvalitní zpracování dlouhého kontextu klíčovou výzvou. Budoucí vývoj se pravděpodobně zaměří na několik oblastí. Bude pokračovat zlepšování efektivity prostřednictvím dalších optimalizací algoritmů jako FlashAttention, vývoje nových aproximací pozornosti a zdokonalování alternativních architektur typu SSM a hybridních modelů. Současně bude kladen důraz na zlepšování kvality, zejména na řešení problému "lost in the middle" a zajištění spolehlivého využití informací z celého kontextu, což podpoří i vývoj lepších evaluačních metrik. Očekává se také hardwarová ko-evoluce s vývojem specializovaných akcelerátorů s větší pamětí a propustností, optimalizovaných pro LLM. Dále se bude prohlubovat kombinace přístupů, například hledání synergií mezi modely s dlouhým kontextem a technikami RAG pro lepší syntézu informací. V neposlední řadě bude pokračovat hledání fundamentálních průlomů a zcela nových paradigmat pro zpracování sekvenčních dat, která by mohla překonat současná omezení.

## Závěr

Schopnost pracovat s dlouhým kontextem je zásadní pro posun LLM směrem k hlubšímu porozumění a řešení komplexnějších úloh. Kvadratická složitost standardního mechanismu pozornosti v architektuře transformátoru představuje dosti podstatnou překážku, která vede k vysokým výpočetním, paměťovým a finančním nákladům. Současný výzkum přináší řadu inovativních řešení, od optimalizací stávajících metod (FlashAttention) přes aproximace (Sparse Attention) až po zcela nové architektury (Mamba, Jamba) a doplňkové techniky (RAG). V každém případě je tu ještě mnoho příležitostí, jak můžete prosadit svůj nápad a nabídnout nové, neotřelé řešení.

Nicméně soudím, že neexistuje jedno univerzální řešení. Budoucnost pravděpodobně spočívá v kombinaci různých přístupů, přizpůsobených konkrétním úlohám a hardwarovým možnostem. Vývoj v této oblasti je extrémně dynamický a lze očekávat další rychlé pokroky.