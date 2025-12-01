---
author: Patrick Zandl
categories:
- AI
- LLM
layout: post
summary_points:
- Shrnutí aktuální situace na trhu LLM pro rok 2025 a doporučení, jaké modely zvolit pro různé typy použití
- Porovnání hlavních AI modelů (Gemini 3 Pro, Grok-4-fast, GPT-5.1, Claude Opus 4.5) z hlediska výkonu a ceny
- Vysvětlení, proč Gemini 3 Pro aktuálně dominuje v reasoningu a běžných aplikacích
- Popis cenových strategií a výhod jednotlivých ekosystémů (Google vs. OpenAI vs. Anthropic)
- Praktické rady, pro koho má smysl zůstat u OpenAI, kdy zvolit Groka a v jakých případech využít Claude
- Upozornění na limity a výhody jednotlivých tarifů (paušál vs. platba za tokeny)
- Důsledky aktuálních změn pro vývojáře, firmy i koncové uživatele AI
post_excerpt: Neorientujete se tak dobře na trhu LLM a nevíte, jaký model pro jaké použití je vhodný? Tak tento článek vám to řekne buďto stručně, nebo v souvislostech... 
title: "Jak vybrat správné LLM pro vaše AI použití (prosinec 2025)"
thumbnail: 
---

Před technologicky dávnou dobou jsem napsal článek o tom, k čemu lze použít jednotlivé konkrétní LLM. Modelů AI je totiž celá řada a každý je vhodný na něco jiného. I docela "přehledný" Anthropic má hned tři modely, které se liší buďto cenou, nebo rychlostí, jakou vám vyčerpají přidělenou kapacitu - to podle toho, zda platíte za dotaz nebo paušální poplatek. A i s ohledem k na kvalitu odpovědí je rozumné zamyslet se nad tím, který model použít.

Dobrým vodítkem jsou nám testy, já budu nyní vycházet z [V2 WeirdML](https://htihle.github.io/weirdml.html).  Tento benchmark totiž netestuje jen "znalost Pythonu", ale simuluje reálnou práci ML inženýra – od pochopení problému přes návrh architektury až po iterativní ladění modelu. To vysvětluje, proč modely jako Gemini 3 Pro (se silným reasoningem) tak drtivě vítězí nad modely, které jen "statisticky doplňují kód". Díky tomu nejde jen o test programátorský, ale o test celkového myšlení, práce s textem atd. A za další mi dovolte vlastní názory, nepodchycené statisticky.

> **Proč se zajímat o cenu modelu, když platíte paušál?** Protože on to tak docela paušál není. U LLM buďto platíte za počty zpracovaných tokenů (při přístupu přes API, tedy zejména programátoři) nebo dosstanete v rámci paušálu jen určitý počet odpovědí za den, týden atd. Dražší modely pochopitelně dávají méně odpovědí. Pro jednu konverzaci za den to bývá jedno, ale při rutinním užívání narazíte snadno na limity svých tarifů a o ceně modelu se vyplatí přemýšlet. 

* A o čem bude řeč?
{:toc}

## Stav trhu LLM (Prosinec 2025)

Nejdříve stručně, pokud nemáte čas a stačí vám moje autoritativní tvrzení, jaká je situace s hlavními modely a co si vybrat. 

1.  **Výměna stráží na vrcholu:**  **Gemini 3 Pro** je novým králem. S přesností téměř 70 % v komplexním reasoningu (WeirdML) a cenou nižší než konkurence odsouvá GPT-5.1 na druhou kolej. Pro kritické aplikace je to jediná racionální volba. Pro běžné užití je tarif Google AI Plus za 220 Kč měsíčně (a nyní ve slevě na 110 Kč měsíčně) výborná volba, která zpřístupní i další služby Google ekosystému včetně lepších podmínek na NotebookLM.
    
2.  **Komoditizace inteligence:**  **Grok-4-fast** je jasná volba na jednodušší úlohy. Nabízí výkon "střední třídy" (úroveň Claude Haiku nebo starší verze Sonnet 3.5) za cenu **$0.013**. To je tak levné, že se nevyplatí používat Llama modely a čínské modely (DeepSeek) ztrácejí svou hlavní (cenovou) výhodu. Nic jiného od Groka smysl nemá, leda byste dostali extra slevu. 
    
3.  **Krize identity u OpenAI:** GPT-5.1 je drahý a ne nejlepší. Model **GPT-5-Codex** je sice mocný, ale jeho provoz je velmi neefektivní (obří spotřeba tokenů). OpenAI drží pozici jen v oblasti strukturovaných dat (o4-mini). V podstatě nyní máte ChatGPT jen z nostalgie a z víry, že se to za pár týdnů/měsíců otočí a pokud ho používáte přes API, tak zatím přejděte jinam. 
    
4.  **Specializace Anthropicu:** Claude už nesoutěží hrubou silou, ale "lidskostí" a spolehlivostí agentů. **Claude Code** je nejlepší software pro autonomní vývoj, i když model pod ním (Opus 4.5) je drahý. Pokud si předplácíte ekosystém Claude (zejména kvůli Claude Code), nemusíte se bát, že byste volili špatně.

Nyní si pojďme vyhodnotit situaci na poli modelů trochu podrobněji.     

## Nový král: Dominance Gemini 3 Pro

Vydání modelu Gemini 3 Pro byl blesk z čistého nebe. Jistě, bylo známo, že Google investuje a už jeho obrazový model Nano Banana vydaný o týdny dříve, byl skvělý, jenže pořád jsem si tak nějak myslel, že kompletní Gemini model se Googlu nepodaří vyladit tak dobře. A model Gemini 3 Pro je VELMI dobrý model, který o parník utekl jak OpenAI, tak Anthropicu. Já jsem to zjistili na [našem Scribetonu Zítraslavných](https://www.zitraslavni.cz). Mám totiž takový prompt, kterým si nechávám vyhodnocovat mnou napsaný beletristický text a který mi hlídá, zda například nevypadávám z jazyka a povahy jednotlivých postav, či zda nejsou některé pasáže zbytečné, posouvají děj či jsou uvěřitelné. Vždycky jsem používal Sonnet, po letošním testování z něj lezly nejlepší výsledky, model o3 mi nepřišel pro češtinu moc dobrý, GPT-5 byl dost strojený, Gemini 2.5 Pro bylo velmi formální a ani laděním promptu se mi to nedařilo snadno změnit. Teď jsem to před týdnem vyzkoušel na GPT-5.1 (opět nic moc), Opus 4.5 (fajn výsledek) a když jsem čekal, než mi to Opus zpracuje, tak jsem překopíroval podklady do Gemini 3 Pro přes GEM Jazykový redaktor a zadal jednoduchý prompt - ani ne ten můj vyladěný. A doslova jsem nevěřil svým očím, jak komplexní a promyšlená byla odpověď. Od té doby používám na ladění textu Gemini 3 Pro, přičemž hlavní výhodou je milionový kontext, takže můžu v klidu nahrávat celý text knihy i obslužné story line a story canvas.

Nejvýraznějším zjištěním z datasetu je **absolutní odskok modelu** `**gemini-3-pro-preview**`.

-   **Výkonnostní skok:** S průměrnou přesností (`avg_acc`) **0.699** tento model nejenže vede, ale o parník poráží konkurenci. Pro kontext: rozdíl mezi Gemini 3 Pro a GPT-5.1 (0.608) je téměř 10 procentních bodů. V "high-end" AI developmentu je takový rozdíl propastný – je to rozdíl mezi modelem, který "většinou funguje", a modelem, na kterém můžete stavět kritickou infrastrukturu.
    
-   **Silné stránky:** Podívejte se na `xor_easy_acc` (0.916) a `shapes_hard_acc` (0.744). Google zjevně vyřešil multimodální a logické operace, které ostatním dělají potíže.
    
-   **Efektivita:** Přestože je to SOTA (State of the Art), jeho cena za běh ($0.53) je nižší než u GPT-5.1 ($0.69) i Claude Opus 4.5 ($0.74). Google zde využívá svou infrastrukturu TPU k cenové válce na špičce (a o TPU si povíme něco někdy příště).
    
**Závěrem:** pokud používáte předplatné Google, máte v rámci něho dostupné Gemini 3 Pro a výrazně doporučuji se jím začít zabývat. Zatím tu není tolik integrací a také podpora projektů a GEMů je slabší, než v případě OpenAI, ale dá se to překlenout a očekávám, že tu Google zapracuje. A kromě "síly" modelu a jeho uvažování je velkou výhodou multimodalita. Můžete tak v jednom běhu kombinovat požadavky, například nahrát Excel, linkovat youtube video, obrázek ofocený v prezentaci a zadat prompt typu "najdi na tomto videu, kde se hovoří o tomto ofoceném slajdu, zpracuj kontext diskuse kolem slide a aktualizuj mi podklady pro příští diskusi na základně aktuálních dat v XLSX".

Druhá silná stránka je prohlubující se napojení na Google ekosystém, právě například na Youtube či do Google Docs a to i pro běžné, nefiremní účty v rámci tarifu Google AI Plus. 

Google Gemini se tak definitivně stalo skokanem roku.

## Souboj titánů: Claude Opus 4.5 vs. GPT-5.1

Dlouho očekávaný souboj mezi nejnovějšími modely Anthropic a OpenAI má v těchto datech jasného vítěze. A není to OpenAI.

1.  **Claude Opus 4.5 (High, 16k):** S `avg_acc` **0.637** se Anthropicu podařilo překonat řadu GPT-5. Opus potvrzuje svou pověst modelu pro komplexní uvažování a rozdíly. Je sice nejdražší v datasetu ($0.74/run), ale pro případy, kde selhání není možnost, je to nyní druhá nejlepší volba po Gemini.
    
2.  **GPT-5.1 & GPT-5:** OpenAI se ocitá v defenzivě. Vlajková loď `gpt-5.1` dosahuje pouze **0.608**. To je sice špičkový výsledek, ale nestačí na prvenství. Zajímavé je, že model označený jako `gpt-5-pro` (0.604) nepřináší lepší přesnost než verze 5.1, což může naznačovat, že narážíme na limity architektury transformerů u OpenAI, nebo že se "Pro" verze zaměřuje na jiné metriky (např. kontextové okno) než na čistou logickou přesnost.
    

### "Thinking" modely a specializace

Jak je to s dalšími modely zaměřenými na přemýšlení a se specializovanými modely, které jsou levnější, než SOTA modely (ten termín se naučte, běžně se používá a taky mám tendenci ho zaměňovat za "špičkové modely")?

V datech vidíme jasný trend specializovaných modelů s dlouhým řetězcem myšlení (Chain of Thought - CoT).

-   **GPT-5 Codex:** Tento model je anomálie. Má průměrnou přesnost jen 0.545, ale podívejte se na `mean_total_output_tokens`: **21 301 tokenů**. To je násobně více než u ostatních - a délka výstupního tokenu se projevuje na ceně. OpenAI zjevně vytvořilo specializovanou "továrnu na kód", která brutální silou generuje tisíce řádků self-correction a reasoning kroků, aby dosáhla výsledku.
    
-   **Claude Sonnet 4.5 vs. Haiku 4.5:** Zde je překvapení. Rozdíl mezi "Sonnet" (střední třída, 0.477) a "Haiku" (lehká třída, 0.454) se téměř smazal. Haiku 4.5 je extrémně kompetentní a kanibalizuje trh střední třídy, což je špatná zpráva pro modely jako GPT-4.1. Je totiž výrazně levnější. Při běžném programování jej lze používat místo Sonnetu, což v Claude Code dává lepší využití limitů či ceny (u toho se pak zastavíme).
    

### Čínské modely: Komoditizace "Včerejší SOTA"

Zatímco západní giganti bojují o hranici 0.60 - 0.70, čínské modely (DeepSeek, Qwen, Kimi) pevně obsadily pásmo **0.40 - 0.45,** kde konkurují cenou. Ačkoliv se Kimi K2 holedbá tím, jak je skvělý na programování, tak skvělý je především cenou a na jasně specifikované úlohy typu "najdi a oprav", než na výstavbu kompletních nových projektů.

-   **Pozice:** Modely jako `grok-3-mini`, `kimi-k2-thinking`, `deepseek-r1` a `qwen3` se pohybují okolo skóre **0.41 - 0.43**. Grok sem dávám pro představu, není to Čína, ale Muskův projekt, rozebereme si jej dále.
    
-   **Interpretace:** Čínští vývojáři efektivně replikují výkon modelů z počátku/středu roku 2025 (jako o1-preview nebo Claude 3.5 Sonnet) s odstupem cca 6 měsíců. To je to "nanosekundové" zpoždění za USA, o kterém mluvil nedávno Jensen Huang.
    
-   **DeepSeek & Qwen:** Nejsou na absolutní špičce, ale jejich strategie je jasná – poskytnout "good enough" inteligenci (na úrovni GPT-4o nebo raných o1) za zlomek ceny nebo jako open weights (viz `gpt-oss-120b`). Pokud budujete aplikaci, která nepotřebuje genialitu Gemini 3 Pro, ale potřebuje spolehlivost, čínské modely a open-source deriváty jsou nyní ekonomicky nejracionálnější volbou.
    

----------

## A co Zuckerberg a Musk? A co EU?

Výsledky vypráví **dva naprosto odlišné příběhy**. Zatímco Grok (xAI) se dere do střední třídy s agresivní cenovou politikou (kde ovšem naráží na Čínu), Meta (LLAMA) v tomto specifickém benchmarku "WeirdML" (zaměřeném na komplexní reasoning a ML úlohy) zaostává způsobem, který by měl být pro Marka Zuckerberga alarmující. A Mistral na tom není o nic líp. 

### Grok (xAI): Dravý nástup a "šampion levné efektivity"

Elonova xAI udělala obrovský skok. V datech vidíme jasnou evoluci od slabšího Grok-2 k velmi kompetentní řadě Grok-4. Nutno poznamenat, že běžné textové výstupy Groku, jak je známe z webu, vzbuzují pochybnosti o datech, se kterými pracuje, v modelu 4 už se přitáhly šroubky, protože se ukazovalo, že načíst do učebních dat kdejakou hámotinu, se projevuje na výsledcích velmi negativně, nejenom že směšně. V používanosti Groku pomohla integrace s [X.com](https://x.com/), kde Grok je vlastně jediný, kdo má přístup ke zdejším datům a dokonce se ho můžete zeptat tweetem, je to oblíbená trolicí strategie, pod něčí manipulativní post zmínit @grok a chtít po něm, aby data ověřil...

-   **Vlajková loď: Grok 4** `**grok-4-07-09**`
    
-   **Výkon:** S přesností **0.457** se tento model zařadil do solidního středu. Je srovnatelný s **Claude Haiku 4.5**(0.454) nebo starším **Claude 3.5 Sonnet** (0.399). Nevěřte prosím tvrzením, že se vyrovná SOTA modelům - nevyrovná. 
    
-   **Problém:** Cena **$0.45** za běh. To je příliš drahé. Za podobnou cenu máte o4-mini (High), který je přesnější (0.525), nebo za pětinu ceny Haiku. Vlajkový Grok tedy nedává ekonomický smysl.
    
-   **💎 Skrytý poklad: Grok 4 Fast**`**grok-4-fast**`
    
-   Tento model mě z nabídky Groku zaujal nejvíce. Rychlý, "dost přesný", levný a západní (akorát že Muskův).
    
-   **Výkon:** Přesnost **0.429** (téměř stejná jako "velký" Grok-4).
    
-   **Cena:**  **$0.013** za běh!
    
-   **Interpretace:** xAI se podařilo destilovat výkon velkého modelu do extrémně levné varianty. **Grok-4-fast je jedním z nejlepších modelů v poměru cena/výkon v celém datasetu.** Grok ($0.013) je **7× levnější** než Haiku ($0.09) a nabízí ekvivalentní přesnost. Takže no-brainer. To samé ve srovnání s Čínou: je dokonce levnější a přesnější, než DeepSeek.
    
-   **Use-case:** Pokud potřebujete zpracovávat terabajty dat Grok-4-fast je nejlepší "low-cost" volba. Poráží americké modely rozdílem třídy a je levnější, než známé čínské modely.
    

### LLAMA (Meta): Pád krále open-weights?

Mark Zuckerberg v AI stále zaostává a v poslední době o jeho AI není slyšet, co do novinek, jen co do skandálů s odchody a příchody nových lidí.  Při pohledu na výsledky modelů Llama v benchmarku WeirdML (a i jiných!) to musím říct naplacato: **Llama v oblasti reasoningu ztratila kontakt se špičkou.**

-   **Nejnovější model:** `**llama-4-maverick**` **(Duben 2025) - rozumíte, DUBEN!!! To je pravěk!!!**
   

-   **Výkon:** Přesnost pouze **0.245**.
    
-   **Srovnání:** To je propastný rozdíl.
    

-   Oproti **Gemini 3 Pro** (0.699) je to pravěk.
    
-   Ale co hůř – poráží ji i levné čínské modely jako **DeepSeek-V3.2** (0.395) nebo dokonce starší **Grok-3**(0.372).
    

-   **Interpretace:** Zdá se, že architektura Llamy 4 (nebo alespoň verze Maverick) nedokázala integrovat "System 2 thinking" (řetězec myšlenek) tak efektivně jako konkurence. Model selhává v komplexních úlohách, kde je potřeba iterativně ladit kód (což WeirdML vyžaduje).
    

-   **Starší modely:** `**llama-3.1-405b**`
    

-   Přesnost **0.214**. To potvrzuje, že ani hrubá síla 405 miliard parametrů nestačí na chytré, menší modely s lepším tréninkem reasoningu z roku 2025.
    

### 🇫🇷 Mistral: momentálně irelevantní 

Mistral v datech z listopadu 2025 bohužel ztratil svou tržní relevanci a propadl se do "země nikoho". Model mistral-medium-3.1 dosahuje přesnosti pouze 0.331, což je o třídu horší výsledek než u levnější konkurence (např. Grok-4-fast má skóre 0.429 a stojí třetinu toho co Mistral), a zároveň se kvalitou nemůže rovnat ani základnímu Claude Haiku 4.5. S cenou $0.04 za běh není ani "ultra-levný", ani "dostatečně chytrý", a v aktuálním dravém trhu tak pro něj z čistě pragmatického hlediska ROI neexistuje obhajitelný use-case, protože ho v poměru cena/výkon drtí xAI a DeepSeek z jedné strany a Anthropic z druhé.  
    

## Jaký model použít na jaký typ úloh?

V tom se chybuje často. Jasně, můžete zvolit nejvyšší (SOTA) model, ale pak bude provoz zbytečně drahý a navíc pomalý, protože nejlepším modelům trvá o něco déle, než odpovědí.   

Níže uvádím doporučení pro klíčové oblasti. U každé definuji  **Smart Choice**  (podle mne ideální vyvážení kvality a ceny s ohledem na kvalitní češtinu) a  **Budget Choice**  (nejnižší cena, při které je výsledek ještě akceptovatelný).

Jako vývojář bych v Q4 2025 strategii postavil následovně:

### 1. Překlad z angličtiny do češtiny

Pro firemní komunikaci a marketing je klíčová stylistika, pro interní dokumenty stačí faktická správnost. Pokud chcete nejlepší překlad, pak investujte do Deepl API, ale je fakt drahé (20 € za milion znaků, ne tokenů!). Alternativy k němu? 

-   Smart Choice (Cena/Výkon): Claude 4.5 Haiku.
    
    Modely Anthropicu mají dlouhodobě nejlepší "cit" pro češtinu. Znějí přirozeně a méně strojově než konkurence. Haiku 4.5 (cca $0.12/run) dosahuje v testech téměř stejných kvalitativních výsledků jako drahý Sonnet, ale za zlomek ceny. Je to zlatá střední cesta pro publikovatelné texty.
    
-   Budget Choice (Nejlevnější dostačující): Grok-4-fast.
    
    S cenou $0.013 je bezkonkurenčně nejlevnější západní model. Jeho čeština je strohá a občas doslovná, ale fakticky přesná. Pro překlady manuálů, dokumentace nebo interních e-mailů je naprosto dostačující. Udělejte si slepý text a pak se rozhodněte. 

### 2. Překlad z čínštiny do češtiny

Specifická disciplína vyžadující znalost kulturního kontextu zdrojového jazyka, jenže s rostoucím významem Číny a množstvím materiálů, které jsou jen čínsky, je to důležité. A opět, pokud nemáte na Deepl, kam se obrátit? 

-   Smart Choice (Cena/Výkon): DeepSeek-V3.2-exp.
    
    Čínský model, který nativně chápe nuance mandarínštiny lépe než většina západních modelů. V benchmarku si vede velmi dobře a jeho cena ($0.018) je zanedbatelná. Nabízí nejvyšší kvalitu překladu předtím, než byste museli sáhnout po drahém Gemini 3 Pro.
    
-   Budget Choice (Nejlevnější dostačující): Qwen3-Coder (nebo base Qwen3).
    
    Pokud potřebujete přeložit obrovské objemy dat a DeepSeek je z nějakého důvodu (např. dostupnost API) nevhodný, modely rodiny Qwen (Alibaba) jsou extrémně levné a v čínštině stále kompetentní, byť výstupní čeština může vyžadovat více úprav než u DeepSeeku.
    

### 3. Sumarizace cizojazyčných textů do češtiny 

Schopnost zpracovat dlouhý kontext (knihy, reporty) bez zapomínání informací.

-   Smart Choice (Cena/Výkon): Gemini 2.5 Flash.
    
    Tento model byl postaven přesně pro tento účel. Má masivní kontextové okno a je optimalizován na rychlost. Jeho schopnost najít informaci v kupce sena je na úrovni nejdražších modelů, ale cena je ve střední třídě. Pro sumarizaci 50stránkového PDF je to nejracionálnější volba.
    
-   Budget Choice (Nejlevnější dostačující): Grok-4-fast.
    
    Pro kratší texty (články, e-mailová vlákna), které se vejdou do standardního kontextu, je Grok-4-fast plně dostačující. Jeho sumarizace jsou stručné a jde rovnou k věci, což u "budget" řešení často vítáte.
    

### 4. Analýza finančních dat a reporting (Excel/CSV)

Kritická úloha, kde "halucinace" (vymyšlené číslo) znamená problém. Zde se nevyplatí šetřit za každou cenu.

-   Smart Choice (Cena/Výkon): Gemini 3 Pro.
    
    Zde musím udělat výjimku a jako "Smart Choice" označit nejdražší model. Důvodem je ROI. Gemini 3 Pro má v logických benchmarcích (shapes_hard, xor_hard) náskok téměř 10-15 % nad konkurencí. Chyba ve financích stojí víc než $0.50 za API volání. Toto je jediný model, kterému lze svěřit autonomní výpočet marží nebo rizik.
    
-   Budget Choice (Nejlevnější dostačující): o4-mini (High).
    
    Pokud nemáte rozpočet na Gemini, o4-mini je "nejbezpečnější z levných". OpenAI má velmi dobře zvládnuté dodržování struktury a práci s čísly v rámci svých možností. Nebude mít tak hluboký vhled jako Gemini, ale pravděpodobnost, že si vymyslí číslo, je menší než u Groka nebo Haiku.
    

### 5. Sestavení horoskopu a jiné kreativní texty

Tohle je můj oblíbený test: nechám si vygenerovat horoskop (týdenní či zrození) a dívám se na to, jak dobře se text čte. Test vyžaduje empatii, "lidský dotek" a schopnost psát poutavě, nikoliv jen fakticky - ale určitá matematická logika je tam nutná. 

-   Smart Choice (Cena/Výkon): Claude 4.5 Haiku.
    
    Opět vítězí "malý" Anthropic. Dokáže simulovat mystický nebo empatický tón mnohem lépe než strohý Grok nebo "robotický" GPT. Pro generování denních horoskopů v aplikaci je to ideální model, který uživatele neurazí strojovostí.
    
-   Budget Choice (Nejlevnější dostačující): DeepSeek-V3.2 (přes prompt engineering).
    
    Překvapivě, čínské modely jsou velmi tvárné v "roleplay". Pokud DeepSeeku dáte dobrý systémový prompt ("Jsi stará vědma..."), dokáže vygenerovat velmi kreativní text za cenu blížící se nule ($0.018). Vyžaduje to ale více práce s laděním promptu než u Claude.
    

### 6. Strukturování dat (Text -> JSON)

Převod nestrukturovaného textu (inzeráty, životopisy) do databáze.

-   Smart Choice (Cena/Výkon): o4-mini (High).
    
    OpenAI si drží prvenství v režimu "Structured Outputs". Model o4-mini má v benchmarcích na dodržování instrukcí (tzv. shapes_easy) extrémně vysoké skóre. Je to spolehlivý "úředník", který přesně dodrží vaše JSON schéma.
    
-   Budget Choice (Nejlevnější dostačující): Grok-4-fast.
    
    Pro jednoduché extrakce (např. vytáhni jméno a email) Grok stačí. Díky své rychlosti a ceně $0.013 můžete každou extrakci pustit klidně dvakrát pro kontrolu a stále budete na desetině ceny o4-mini. Na složité vnořené JSONy ale může selhat.
    

### 7. Programování (Vývoj softwaru)

Pokud používáte Claude Code, nešaškujte s jinými modely. Vyzkoušeno za vás, pokusy rozběhat na Xku hajpovaný Kimi K2 vedly ke zklamání. Pokud platíte moc peněz, přejděte na flat-fee tarif a naučte se jej optimálně využívat, nicméně Claude Code je vyladěný na Claude modely.  Jinak je to tam, kde si přinesete své vlastní API klíče či můžete používat jiné modely přímo, například Pomocník v IDE (Cursor) nebo otevřených CLI nástrojích.

-   Smart Choice (Cena/Výkon): Qwen3-Coder.
    
    Tento model je specializovaný výhradně na kód. Ačkoliv je velmi levný (cca $0.07), v programovacích úlohách často překonává i mnohem dražší generalizátory jako GPT-5.1. Pro každodenní našeptávání kódu a psaní funkcí je to nejlepší hodnota za peníze.
    
-   Budget Choice (Nejlevnější dostačující): Grok-4-fast / DeepSeek-V3.2.
    
    Zde je to remíza. Na triviální úkoly (HTML/CSS, Bash) stačí Grok. Na složitější logiku v Pythonu, kde máte minimální rozpočet, sáhněte po DeepSeeku. Oba modely stojí pod 2 centy a pro studenty nebo hobby projekty jsou plně dostačující.
    

## Závěr: Jakou architekturu zvolit pro vývoj? Router!

Pokud chcete maximalizovat efektivitu, doporučuji  **hybridní přístup**, tedy routování na nejlepší model podle typu úkolu. Registrujte se na [OpenRouter.ai](https://www.openrouter.ai), jeďte přes jejich API a vybírejte si jen model, který je nejlepší. 

A druhá věc: na OpenRouter se relativně často modely testují. Je dobré si to hlídat a můžete se snadno přepnout na model, který zrovna někdo potřebuje otestovat a je zdarma. 

Asi nějak takto:

1.  Jako  **výchozí model**  (default) ve vašem systému nastavte  **Claude 4.5 Haiku**. Pokryje 60 % úloh (překlady, texty, chat) s vysokou kvalitou a rozumnou cenou.
    
2.  Pro  **data mining a "tupou práci"**  mějte připravený fallback na  **Grok-4-fast**. Ušetří vám rozpočet na objemných datech. Grok ho bude v nejbližší době aktualizovat na verzi _grok-4.1-fast_ - právě se testuje a na OpenRouteru je zdarma.  
    
3.  Pro  **kritické momenty**  (finance, architektura kódu) si ponechte přístup k  **Gemini 3 Pro**. Používejte ho šetrně, ale v rozhodujících chvílích.

1.  **Pro nejnáročnější úlohy (Reasoning, Complex Logic):** Jednoznačně migrovat na **Gemini 3 Pro**. Je to v současnosti jediný "Tier 1+" model. Nabízí nejlepší poměr cena/výkon na absolutní špičce.
    
2.  **Pro produkční prostředí vyžadující stabilitu:**  **Claude Opus 4.5** je silná alternativa, pokud jste v ekosystému Anthropic, ale je dražší.
    
3.  **Pro běžné úlohy a zpracování dat:** Vyhnout se drahým modelům OpenAI (GPT-5). Místo toho využít **Claude Haiku 4.5** nebo Grok 4 Fast.
    
OpenAI v těchto datech ztrácí dech. GPT-5.1 není lídrem trhu a jejich specializované modely (Codex) jsou extrémně náročné na tokeny (a tedy pomalé a drahé). Pokud nepřijdou s rychlou iterací (např. gpt-5.5), Google jim přebere high-end segment a v low-end segmentu se vydělává špatně, konkurence je velká. 