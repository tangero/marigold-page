---
author: Patrick Zandl
categories:
- AI
- LRM
layout: post
post_excerpt: Nedávná studie Apple odhaluje dosti zásadní omezení v architektuře uvažujících
  jazykových modelů (Large Reasoning Models) a zpochybňuje jejich skutečné uvažovací
  schopnosti. Je to jen vlnka na jezeře nadějí, že modely jako o3 nebo deepseek-r1
  jsou schopny kvalitativních posunů, či vážný problém?
summary_points:
- Apple studie zpochybňuje skutečné uvažovací schopnosti Large Reasoning Models (LRM).
- Standardní benchmarky LRM trpí kontaminací dat a neumožňují kontrolované experimenty.
- LRM vykazují tří-režimovou výkonnost s kolapsem při vysoké složitosti problémů.
- Studie odhalila architektonické limity LRM a potřebu nových přístupů k inferencím.
thumbnail: null
title: Limity současných uvažujících jazykových modelů -  Analýza skutečných schopností
  LRM'
---

Nedávná studie Apple odhaluje dosti zásadní omezení v architektuře uvažujících jazykových modelů (Large Reasoning Models) a zpochybňuje jejich skutečné uvažovací schopnosti. Je to jen vlnka na jezeře nadějí, že modely jako o3 nebo deepseek-r1 jsou schopny kvalitativních posunů, či vážný problém? 


Poslední generace jazykových modelů, označovaná jako Large Reasoning Models (LRM) - Velké modely uvažování, představuje modely jako OpenAI o1/o3, [DeepSeek](/item/deepseek/)-R1 nebo Claude 3.7 Sonnet Thinking. Tyto systémy se vyznačují generováním rozsáhlých "myšlenkových" procesů před poskytnutím odpovědi, tzv. obsáhlé řetězce úvah (chain-of-thought, CoT).  Což má simulovat lidské uvažování. Navzdory slibným výsledkům na standardních benchmarcích však zůstává otázka, zda skutečně dochází k zobecnitelnému uvažování, nebo jde o sofistikovanější formu pattern matchingu. A tuto otázku se pokusil zodpovědět Apple v studii, která se zaměřila na analýzu uvažovacích schopností těchto modelů. Studie se příznačně jmenuje [Iluze myšlení: Porozumění silným stránkám a omezením modelů uvažování z pohledu složitosti problémů](https://machinelearning.apple.com/research/illusion-of-thinking).

Na začátek si výzkumníci stanovily dvě hypotézy:

**Hypotéza 1:**
Zda LRM skutečně umějí generalizovat proces „myšlení“ na nové úlohy, nebo spíše sofistikovaně napodobují vzory z tréninkových dat, případně provádějí komplexní pattern matching.

**Hypotéza 2:**
Zda navyšování výpočetního rozpočtu a délky generovaného „myšlení“ skutečně zlepšuje řešení složitějších problémů, nebo modely narážejí na určitou hranici, za kterou selhávají bez ohledu na další zdroje.

## Metodologický problém současného hodnocení

Standardní evaluace LRM trpí několika zásadními nedostatky. Především se spoléhají na etablované matematické a programátorské benchmarky, které často obsahují data z trénovacích sad. Tato kontaminace se pak odráží ve zdánlivém výkonu.  Testy navíc neumožňují kontrolované experimentální podmínky napříč různými úrovněmi složitosti a neposkytují vhled do struktury a kvality samotných uvažovacích procesů.

Autoři studie proto navrhli alternativní přístup založený na kontrolovaných puzzle prostředích, které umožňují:

- **Přesné řízení složitosti** prostřednictvím úpravy parametrů při zachování logické struktury
- **Eliminaci kontaminace dat** použitím nových, specificky navržených problémů  
- **Důraz na algoritmické uvažování** s jasně definovanými pravidly
- **Rigorózní hodnocení** pomocí deterministických simulátorů

## Experimentální design

Výzkumníci využili čtyři typy puzzlí s různými charakteristikami složitosti, např. Hanojské věže, přesouvání figurek, přechod přes řeku, skládání bloků). Umožňují tak přesné řízení složitosti a eliminaci efektu „naučených“ řešení. A měří nejen finální správnost, ale i strukturu a kvalitu mezikroků v řetězci uvažování.

Každé puzzle bylo testováno s postupně rostoucí složitostí, přičemž byly analyzovány právě nejenom finální odpovědi, tak mezilehlé kroky v "myšlenkových" procesech modelů.

## Klíčová zjištění

### Tří-režimová architektura výkonnosti

Analýza odhalila konzistentní vzorec napříč všemi testovanými modely:

1.	Nízká složitost:
- Standardní LLM bez explicitního myšlení často dosahují lepších výsledků i vyšší efektivity.
- LRM v této oblasti často „přemýšlí zbytečně dlouho“ (overthinking).
2.	Střední složitost:
LRM začínají mít výhodu díky schopnosti déle rozebírat problém, občas naleznou řešení po delším zkoušení různých cest.
- Rozdíl ve výkonu mezi „thinking“ a „non-thinking“ modely roste ve prospěch LRMs.
3.	Vysoká složitost:
- Dochází k „kolapsu“ obou typů modelů: pravděpodobnost úspěchu padá na nulu.
- Zajímavé je, že právě v této fázi modely začnou paradoxně spotřebovávat méně výpočetního výkonu na myšlení (zkracují řetězec úvah), přestože složitost problému roste a mají dostatečný [token](/ai/tokeny-versus-slova/) budget.

### Paradoxní škálovací limity

Nejpřekvapivějším objevem je kontraintuitivní vztah mezi složitostí problému a investovaným "uvažovacím" úsilím. Modely nejprve zvyšují počet thinking [tokenů](/ai/tokeny-versus-slova/) úměrně se složitostí, ale při dosažení kritického prahu začínají úsilí snižovat - navzdory dostupnému token budgetu a rostoucí obtížnosti problémů.

Tento jev naznačuje fundamentální architektonické omezení v současných LRM, kde systémy nejsou schopny efektivně alokovat výpočetní zdroje při inference pro nejtěžší problémy.

### Selhání při exaktním výpočtu

Zvláště alarmující je zjištění, že poskytnutí kompletního algoritmu řešení nevedlo ke zlepšení výkonnosti. Modely selhávaly i při pouhém vykonávání předepsaných kroků, což odhaluje limity nejen v objevování strategií, ale i v konzistentním logickém ověřování a v provádění úkolů krok po kroku.

Například v Hanojských věžích dosáhly modely správných sekvencí přes 100 kroků, zatímco v River Crossing selhaly již po 4 krocích u problémů s kratším celkovým řešením. Tato nekonzistence naznačuje, že výkonnost není primárně funkcí délky sekvence, ale spíše dostupnosti podobných vzorců v trénovacích datech.

## Analýza myšlenkových procesů

Detailní rozbor postupu uvažování odhalil určité zákonitosti či vzorce:

- **U jednoduchých problémů**: Distribuce nesprávných řešení je posunuta směrem ke konci uvažování ve srovnání se správnými řešeními
- **U středně složitých problémů**: Opačný trend - správná řešení se objevují později v sekvenci
- **U vysoké složitosti**: Absence jakýchkoli správných řešení v celém průběhu uvažování

Tyto vzorce dokumentují omezenou schopnost samoopravy současných LRM a potvrzují hypotézu o existenci škálovacích bariér dnešního přístupu k AI prostřednictvím uvažujících jazykových modelů.

## Implikace pro vývoj AI

Výsledky zpochybňují současné paradigma, že zvýšení _inference-time resoning_ časů  automaticky vede k lepším reasoning schopnostem. Místo toho naznačují existenci architektonických bottlenecků, které brání efektivnímu škálování na složité problémy.

> 💡 **Inference-time reasoning** je schopnost AI modelu provádět složité uvažovací procesy během samotného používání (inference), nikoli pouze spoléhat na znalosti naučené během tréninku. Jde o proces, kdy model "přemýšlí" nad problémem v reálném čase a generuje mezikroky před poskytnutím finální odpovědi.


Pro nasazení v reálném světě znamenají tato zjištění, že současné LRM:

- Mohou být užitečné pro problémy střední složitosti s dobře definovanými vzorci
- Nejsou spolehlivé pro skutečně složité plánovací úlohy
- Vyžadují opatrnost při aplikacích vyžadujících konzistentní logické ověřování

### Směry dalšího výzkumu

Studie identifikuje několik kritických oblastí pro pokračující výzkum:

**Architektonické inovace**: Potřeba nových přístupů k inferencím, které překonají současné škálovací limity.

**Trénovací metodologie**: Zkoumání technik, které by vedly k robustnějšímu algoritmickému uvažování místo spoléhání na pattern matching.

**Evaluační frameworky**: Rozšíření kontrolovaných experimentálních prostředí na širší spektrum uvažovacích úloh.


## Závěr

V řadě případů se modely chovají „zdánlivě inteligentně“, ale selhávají v generalizaci, v exekuci jasných pravidel nebo v plánování pro opravdu složité úlohy. Studie také nenaznačuje, že samotná velikost modelu nebo více dat problém vyřeší. Bariéra je spíše v architektuře a schopnosti symbolické manipulace.

Tato studie poskytuje empiricky podložený pohled na skutečné schopnosti současných Large Reasoning Models. Zatímco tyto systémy představují pokrok v určitých doménách, jejich fundamentální omezení v zobecnitelném uvažování jsou zásadnější, než původně předpokládáno.

Výsledky nenaznačují, že reasoning modely jsou bezcenné, ale spíše definují jasné hranice jejich použití. Pro vědeckou komunitu to znamená potřebu přehodnotit současné přístupy k design inference-time reasoning a hledání nových architektonických řešení, která by překonala identifikované škálovací bariéry.

Vnímám zde několik otevřených otázek:

1. Jakým způsobem lze modely naučit skutečnou generalizaci uvažovacích postupů, nikoliv pouze **pattern matching** (tedy _založené na rozpoznávání vzorců_) a napodobování povrchových struktur?
2. Je možné kombinovat současné LLM s explicitními symbolickými moduly nebo plánovači pro zvýšení robustnosti reasoning?
3. Do jaké míry jsou limity způsobeny architekturou modelu, RL tréninkem, nebo samotným charakterem dat?


Rozhodující bude, zda se podaří vyvinout systémy skutečně schopné algoritmického uvažování, nebo zda zůstaneme omezeni na sofistikované metody, které v podstatě pouze rozpoznávají vzorce z trénovacích dat.