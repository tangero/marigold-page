---
slug: 'openai-o3-o4-mini'

author: Patrick Zandl
categories:
- AI
- OpenAI
date: 2025-04-18
summary_points:
- OpenAI vydalo nové modely o3 a o4-mini.
- Modely o3 a o4-mini jsou "reasoning models".
- Nové modely integrují nástroje jako vyhledávání a kódování.
- o3 je výkonnější, o4-mini optimalizovaný pro efektivitu.
thumbnail: https://www.marigold.cz/assets/souboj-llm.jpg
title: OpenAI vydala svůj nejsilnější model pro ChatGPT o3 a rychlý o4-mini
---

Novým a nejsilnějším modelem LLM společnosti OpenAI se stává o3. Firma jej právě uvolnila a přidala do webového rozhraní i API, tak si k němu řekneme pár věcí. 

Tou první věcí je moje dlouhodobé konstatování, že struktura pojmenování v OpenAI je fakt bordel. Sám si musím dělat tabulku, které modely co znamenají a studium ceníků pro použití přes API je opravdu únavné. Potřebovali bychom AI na to, jakou AI použít😞 A teď už k věci. 

OpenAI 16. dubna 2025 oznámilo vydání dvou nových modelů - o3 a o4-mini. 

Oba modely jsou označovány jako "reasoning models" (modely s rozumovým uvažováním) a podle dostupných informací poprvé nabízejí plnou agentní integraci všech nástrojů v rámci ChatGPT. To znamená schopnost kombinovat a využívat webové vyhledávání, Python, analýzu obrázků, interpretaci souborů a generování obrázků v rámci jednoho pracovního toku. 
Zjednodušeně řečeno, když zadáte o3 nějaký úkol, ona se nad tím zamyslí, zjistí, že by se hodilo prohledat web a pak si udělat script, kterým se vyhodnotí vyhledaná data, než vám odprezentuje výsledek - a nakonec vám z něj může udělat i požadovanou infografiku. Tohle je fakt silný moment práce s AI. Dlužno říct, že podobně se začíná chovat Claude Sonnet díky napojení na Google Workspace, kdy se může velmi autonomně prohrabovat ve vašich datech, k tomu používat vyhledávání a tvořit scripty, které si sám spustí a výstupy z nich použije. 
Model o3 je prezentován jako výkonnější varianta zaměřená na kódování, matematiku, vědu a vizuální uvažování. Model o4-mini je optimalizován pro efektivitu z pohledu rychlosti a nákladů, což umožňuje vyšší limity využití než u modelu o3.

### Technologické inovace

Zajímavou funkcí obou modelů je integrace nahraných obrázků přímo do procesu uvažování. To představuje posun od pouhého "vidění" obrázku k jeho zakomponování do myšlenkového procesu modelu, což potenciálně zlepšuje schopnost modelů pracovat s vizuálními informacemi.

### Jaké mají modely výsledky

S AI to začíná být jako s lidmi. Na internetu pořád kolují vtípky, jak se modely vypořádávají se spočítáním počtu r ve slově strawberries - s tím se modely vypořádávají různě. Jenže to není pointa. Pointa začíná být v tom, jaké výsledky dávají se složitějšími problémy a jak autonomně se k těm výsledků zvládají dostat, tedy zda zvládají nějaký režim uvažování, v němž si úlohu rozloží na menší, snáze realizovatelné úkoly, místo toho, aby halucinovaly se statistikou. 
o3 má být state of art model, to nejlepší z nejlepšího, nejrůznější výsledky to naznačují, já jsem si s ním proběhl svoji standardní sadu testů na českojazyčné úkoly, které používám já, většinou manipulace s rozsáhlými korpusy textů (náročné na kontext) či na uvažování, ale také jednoduché třídění a vyhledávání typu "vypiš z dokumentu všechna jména lidí a produktů". o3 vychází suverénně jako nejlepší ze všech modelů, na druhou stranu ne vždy je cenově nejvýhodnější, na některé typy úloh (právě třeba vyhledání jmen osob) je to kanón na vrabce a za to si připlatíte. Pokud tedy používáte modely přes API, trochu uvažujte nad cenou, pokud používáte modely přes webové rozhraní (kde neplatíte za dotaz), tak není o čem přemýšlet, prostě to sázejte do o3, leda by vás limitovala rychlost. 

Pozor musíte dávat jen **na délku kontextu**, model GPT-4.1 představený před pár dny má kontext 1 milion [tokenů](/ai/tokeny-versus-slova/), o3 je na 200 tisících tokenech. Je však třeba připustit, že jakmile se nástroje dostávají přes hranici 200 000 tokenů, začíná jít jejich kvalita výrazně dolů, takže užití většího kontextu je spíše hraniční případ, kterému navrhuji se zatím zkoušet vyhýbat. Příklad LLAMA 4 s desetimilionovým kontextem to ukazuje jasně.  

Testů se vyrojila celá řada, já vám dám můj oblíbený norský IQ test, ze kterého plyne, že v takovém tom obecném uvažování je o3 fakt špička. Za mě více důležité bude, jak se podaří OpenAI propojovat svůj systém na další systémy, protože kritická začíná být ani ne tak inteligence (IQ 130 nemá jen tak někdo), ale schopnost dostat se snadno k datům, aby je člověk pořád nepřehazoval jako copy-paste, což je při práci s AI to nejvíce frustrující. To si uvědomujete, že vy tam jste za toho podržtašku. 

![Výsledky IQ testu pro OpenAI o3](/assets/vysledky-o3.jpg)


### Dostupnost

Modely jsou od 16. dubna 2025 dostupné pro uživatele ChatGPT Plus, Pro a Team, přičemž nahrazují předchozí modely o1, o3-mini a o3-mini-high. Uživatelé ChatGPT Enterprise a Edu získají přístup s týdenním zpožděním. OpenAI uvádí, že rychlostní limity zůstávají stejné jako u předchozích modelů.
Pro vývojáře jsou modely k dispozici prostřednictvím Chat Completions API a Responses API. OpenAI také oznámilo, že model o3-pro s plnou podporou nástrojů bude vydán v následujících týdnech.

### API funkce

Responses API přináší několik technických vylepšení včetně "reasoning summaries" (shrnutí procesu uvažování), zachování tokenů uvažování kolem volání funkcí pro lepší výkon a v blízké budoucnosti přibude podpora vestavěných nástrojů jako webové vyhledávání, vyhledávání v souborech a interpretace kódu přímo v rámci uvažování modelu.


### Porovnání cen a výkonu LLM modelů (duben 2025) podle OpenRouter

Z ceníku je lépe patrné, proč říkám, že o3 může být kanón na vrabce. Prostě si nějaký ten dolar zaúčtuje, u většiny věcí je lepší zůstat u o3-mini nebo GPT-4.1 a proto také rád používám OpenRouter, který mi umožní přehodit provoz na modely podle aktuální ceny. Mám na to speciální patentní script, který mi umožňuje průběžně měnit LLM podle aktuálních parametrů potřebných pro daný úkol. 

| Model | Kontext | Max. výstup | Cena vstupu ($/1M tokenů) | Cena výstupu ($/1M tokenů) | Latence (s) | Throughput (t/s) |
|-------|---------|-------------|---------------------------|----------------------------|------------|-----------------|
| o3 | 200K | 100K | $10.00 | $40.00 | 9.52 | 68.78 |
| o4-Mini | 200K | 100K | $1.10 | $4.40 | 4.55 | 81.79 |
| o4-Mini High | 200K | 100K | $1.10 | $4.40 | 8.59 | 90.62 |
| GPT-4.1 | 1,05M | 33K | $2.00 | $8.00 | 0.55 | 58.07 |
| Claude 3.7 Sonnet | 200K | 64K | $3.00 | $15.00 | 1.69 | 56.27 |
| Claude 3.7 Sonnet Thinking | 200K | 64K | $3.00 | $15.00 | 1.69 | 56.28 |
| Gemini 2.5 Pro | 1,05M | 66K | $1.25-$2.50 | $10.00-$15.00 | 8.59 | 414.80 |
| Grok 3 beta | 131K | 131K | $3.00 | $15.00 | 0.74 | 34.21 |

Tady je ceník, přiznám se, že jsem ho nebral z oficiálních API, ale z OpenRouteru, který má výborné API a je to výborné místo pro testování a srovnání, včetně toho, že udává rychlost výstupu a latenci. 

Na závěr vám dám ještě [Aider Leaderboard](https://aider.chat/docs/leaderboards/), což je statistika, jakou vede kódovací nástroj Aider pro výkonnost a cenu jednotlivých LLM. Z toho je vidět, že o3 je suverénně nejlepší, ale taky velmi drahý. Lepší by bylo používat Gemini Pro 2.5 - ten má ale nyní podle mne výrazně dotovanou cenu (sám ho používám zdarma v promo balíku) a je otázka, kdy půjde nahoru. Nutno říct, že jak jsem Gemini modelům dlouho nepřišel na chuť, tak Pro 2.5 je velmi dobrý, i když na kódování mi zatím nesedl. 

![Aider Leaderboard](/assets/aider-leaderboard.png)