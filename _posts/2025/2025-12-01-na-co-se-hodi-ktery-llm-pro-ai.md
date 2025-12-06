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
title: "⏰ Jak vybrat správné LLM pro vaše AI použití (6.prosinec 2025)"
thumbnail: 
---

Před technologicky dávnou dobou jsem napsal článek o tom, k čemu lze použít jednotlivé konkrétní LLM. Modelů AI je totiž celá řada a každý je vhodný na něco jiného. I docela "přehledný" Anthropic má hned tři modely, které se liší buďto cenou, nebo rychlostí, jakou vám vyčerpají přidělenou kapacitu - to podle toho, zda platíte za dotaz nebo paušální poplatek. A i s ohledem k na kvalitu odpovědí je rozumné zamyslet se nad tím, který model použít.

**Aktualizace:** čtvrt hodiny po vydání článku vydal DeepSeek novou verzi 3.2 a její výsledky jsem do článku zapracoval... Zároveň Grok vydal novou verzi 4.1 a její výsledky je také vhodné zapracovat. Pak vydal novinky i Mistral a Apple, také přidáno.  

Dobrým vodítkem jsou nám testy, já budu nyní vycházet z [V2 WeirdML](https://htihle.github.io/weirdml.html) a čerstvě uniklých benchmarků matematických olympiád. Tyto testy totiž netestují jen "znalost Pythonu", ale simuluje reálnou práci ML inženýra či matematika. A právě v momentě, kdy jsem dopisoval tento text, se objevila nová data, která situaci dramaticky mění.

> **Proč se zajímat o cenu modelu, když platíte paušál?** Protože on to tak docela paušál není. U LLM buďto platíte za počty zpracovaných tokenů (při přístupu přes API, tedy zejména programátoři) nebo dosstanete v rámci paušálu jen určitý počet odpovědí za den, týden atd. Dražší modely pochopitelně dávají méně odpovědí. Pro jednu konverzaci za den to bývá jedno, ale při rutinním užívání narazíte snadno na limity svých tarifů a o ceně modelu se vyplatí přemýšlet. 

**A o čem bude řeč?**

{:toc}


## Stav trhu LLM (Prosinec 2025) 

**Univerzální volba:** Gemini 3 Pro si rychle získal pozici v oblasti obecné inteligence. S přesností téměř 70 % v komplexním reasoningu a cenou nižší než konkurence odsouvá GPT-5.1 na druhou kolej. Pro běžné užití je tarif Google AI Plus za 220 Kč měsíčně (a nyní ve slevě na 110 Kč měsíčně) výborná volba.

**Specialista na vědu:** DeepSeek-V3.2 "Speciale". Čínský model, který v matematice a kódu dosahuje výsledků srovnatelných s Googlem či OpenAI. Je náročný na spotřebu tokenů, což se může projevit na rychlosti, ale pro specifické výpočty je velmi výkonný.

**Potenciální skokan:** Grok 4.1 (Fast & Reasoning). Novinka týdne. xAI uvedla model, který má 2 miliony tokenů kontext (stejně jako Gemini) a schopnost Reasoning (přemýšlení), přičemž cena je stanovena na $0.20 za milion tokenů. To zní velmi lákavě pro sumarizaci a agenty, ale model zatím nemáme dlouhodobě ověřený. Ještě levnější je Grok-4-fast. Nabízí výkon “střední třídy” za cenu $0.013. To je tak levné, že se nevyplatí používat Llama modely. 

**Krize identity u OpenAI:** GPT-5.1 je drahý a v klíčových benchmarcích (CodeForces, HMMT) nyní prohrává jak s Googlem, tak s DeepSeekem. OpenAI drží pozici jen v oblasti strukturovaných dat (o4-mini). V podstatě nyní máte ChatGPT jen z nostalgie.

**Specializace Anthropicu:** Claude už nesoutěží hrubou silou, ale “lidskostí” a spolehlivostí agentů. Claude Code je nejlepší software pro autonomní vývoj.

## Nový král: Dominance Gemini 3 Pro

Vydání modelu Gemini 3 Pro byl blesk z čistého nebe. Jistě, bylo známo, že Google investuje a už jeho obrazový model Nano Banana vydaný o týdny dříve, byl skvělý, jenže pořád jsem si tak nějak myslel, že kompletní Gemini model se Googlu nepodaří vyladit tak dobře. A model Gemini 3 Pro je VELMI dobrý model, který o parník utekl jak OpenAI, tak Anthropicu. Já jsem to zjistili na našem Scribetonu Zítraslavných. Mám totiž takový prompt, kterým si nechávám vyhodnocovat mnou napsaný beletristický text a který mi hlídá, zda například nevypadávám z jazyka a povahy jednotlivých postav, či zda nejsou některé pasáže zbytečné, posouvají děj či jsou uvěřitelné. Vždycky jsem používal Sonnet, po letošním testování z něj lezly nejlepší výsledky, model o3 mi nepřišel pro češtinu moc dobrý, GPT-5 byl dost strojený, Gemini 2.5 Pro bylo velmi formální a ani laděním promptu se mi to nedařilo snadno změnit. Teď jsem to před týdnem vyzkoušel na GPT-5.1 (opět nic moc), Opus 4.5 (fajn výsledek) a když jsem čekal, než mi to Opus zpracuje, tak jsem překopíroval podklady do Gemini 3 Pro přes GEM Jazykový redaktor a zadal jednoduchý prompt - ani ne ten můj vyladěný. A doslova jsem nevěřil svým očím, jak komplexní a promyšlená byla odpověď. Od té doby používám na ladění textu Gemini 3 Pro, přičemž hlavní výhodou je milionový kontext, takže můžu v klidu nahrávat celý text knihy i obslužné story line a story canvas.

Nejvýraznějším zjištěním z datasetu je absolutní odskok modelu **gemini-3-pro-preview**.

**Výkonnostní skok:** S průměrnou přesností (avg_acc) 0.699 tento model nejenže vede, ale o parník poráží konkurenci. Pro kontext: rozdíl mezi Gemini 3 Pro a GPT-5.1 (0.608) je téměř 10 procentních bodů.

**Silné stránky:** Podívejte se na xor_easy_acc (0.916) a shapes_hard_acc (0.744). Google zjevně vyřešil multimodální a logické operace, které ostatním dělají potíže.

**Efektivita:** Přestože je to SOTA (State of the Art), jeho cena za běh ($0.53) je nižší než u GPT-5.1 ($0.69) i Claude Opus 4.5 ($0.74). Google zde využívá svou infrastrukturu TPU k cenové válce na špičce.

**Závěrem:** pokud používáte předplatné Google, máte v rámci něho dostupné Gemini 3 Pro a výrazně doporučuji se jím začít zabývat. Zatím tu není tolik integrací a také podpora projektů a GEMů je slabší, než v případě OpenAI, ale dá se to překlenout a očekávám, že tu Google zapracuje. A kromě “síly” modelu a jeho uvažování je velkou výhodou multimodalita.

Google Gemini se tak definitivně stalo skokanem roku v obecné inteligenci.

## Souboj titánů: Claude Opus 4.5 vs. GPT-5.1

Dlouho očekávaný souboj mezi nejnovějšími modely Anthropic a OpenAI má v těchto datech jasného vítěze. A není to OpenAI.

1.  **Claude Opus 4.5 (High, 16k):** S `avg_acc` **0.637** se Anthropicu podařilo překonat řadu GPT-5. Opus potvrzuje svou pověst modelu pro komplexní uvažování. Je sice nejdražší v datasetu ($0.74/run), ale pro případy, kde selhání není možnost, je to nyní silná volba pro agentní systémy. Model Sonnet 4.5 je klasika pro běžné použití a Haiku prověřený všude tam, kde je potřeba rychlost a jeho schopnost práce s textem téměř dosahuje Sonnetu za výrazně lepší cenu. 
    
2.  **GPT-5.1 & GPT-5:** OpenAI se ocitá v defenzivě. Vlajková loď `gpt-5.1` dosahuje pouze **0.608**. To je sice špičkový výsledek, ale v matematice prohrává s DeepSeekem o 10 % a v obecném reasoningu s Googlem taktéž. Model označený jako `gpt-5-pro` (0.604) nepřináší lepší přesnost než verze 5.1.

## Grok 4.1: Slibná novinka za 20 centů

Elonova xAI [vydala ceník pro řadu Grok 4.1](https://docs.x.ai/docs/models/grok-4-1-fast-non-reasoning), který představuje výzvu pro konkurenci v oblasti zpracování velkých dat.

Podívejme se na parametry modelu grok-4-1-fast-reasoning:

- Kontext: 2 000 000 tokenů. To umožňuje nahrát rozsáhlou dokumentaci nebo databáze. Tím se papírově vyrovnává Gemini 1.5/2.5 Pro.
- Schopnosti: Má v názvu "Reasoning". Měl by tedy disponovat schopností řetězení myšlenek (Chain of Thought).
- Cena: $0.20 za 1M vstupních tokenů / $0.50 za 1M výstupních.

Co to znamená? Oproti staršímu modelu grok-4-0709, který stál $3.00 za vstup, je nová verze výrazně dostupnější a nabízí větší kontext. Jde o zajímavou alternativu k modelům jako Gemini Flash nebo Claude Haiku. Pokud potřebujete analyzovat rozsáhlé PDF, Grok se jeví jako ekonomicky velmi efektivní řešení, které stojí za vyzkoušení. Praktickou zkušenost s ním ale zatím nemám. 

## Čínský drak: DeepSeek zase zvyšuje tlak

Zatímco Google ovládl "všeobecnou chytrost", z Číny právě dorazila data o novém modelu **DeepSeek-V3.2**, který zcela měří pohled na "High-End" modely. Už to není jen o tom, že čínské modely jsou "dost dobré a levné". V oblasti matematiky a programování je DeepSeek novým predátorem.

Podle čerstvých benchmarků se DeepSeek rozdělil na dvě verze a ta s názvem **"Speciale"** je absolutní monstrum:

1.  **Matematická dominance:** V testu **HMMT Feb 2025** (Harvard-MIT Mathematics Tournament) dosáhl DeepSeek Speciale skóre **99.2 %**. Pro srovnání: Gemini 3.0 Pro má 97.5 % a GPT-5 High jen 88.3 %. Pokud potřebujete počítat, DeepSeek je momentálně nejchytřejší entita na trhu.
2.  **Programování:** Na platformě **CodeForces** dosahuje ratingu **2701**, což je statistická remíza s Gemini 3.0 Pro (2708) a výrazně více než GPT-5 High (2537).

**Má to ale háček: "Tokenová daň".** Zatímco Gemini dosáhne svého výsledku na CodeForces s použitím 22 tisíc tokenů, DeepSeek Speciale jich "sežere" 77 tisíc. Tento model jde na věc hrubou silou – masivně přemýšlí, zkouší strategie a spotřebovává obrovské množství výpočetního času. Je to dříč, ne sprinter. Bude pomalejší a latence může být problém, ale pokud potřebujete vyřešit algoritmický problém, na kterém si ostatní vylámou zuby, je to vaše nová volba.

Běžná verze **DeepSeek-V3.2 Thinking** pak zůstává skvělou volbou pro poměr cena/výkon, kde stále drží krok s GPT-5, ale za zlomek ceny.    

## LLAMA (Meta) Pád králů?

Mark Zuckerberg v AI stále zaostává. **Llama v oblasti reasoningu ztratila kontakt se špičkou.** Model `llama-4-maverick` má přesnost pouze **0.245**. Oproti Gemini 3 Pro (0.699) je to pravěk. Mistral na tom byl podobně, ale pak v prosinci vydal zajímavou trojici modelů. 

## 🔒 Soukromí a Lokální AI (Edge)

Zatímco cloudové modely válčí o výkon, francouzský Mistral ovládá kategorii modelů, které běží u vás.

VÍTĚZ: Ministral 3 14B. Podle nových benchmarků tento model na běžném hardwaru (24GB RAM) poráží v matematice a logice i srovnatelné čínské modely Qwen.

Use-case: Pokud pracujete s citlivými daty (zdravotnictví, právo, know-how), která nesmí opustit firmu, je Ministral 3 aktuálně nejvýkonnější "mozek", který můžete provozovat offline, aniž byste potřebovali serverovnu. Ale ještě se podívejte na Apple [framework CLaRa](https://github.com/apple/ml-clara) - je to žhavá novinka a umožňuje práci s dokumenty a AI na vašem zařízení. 

## Amazon Nova: Podniková efektivita v AWS a video

Amazon čerstvě (prosinec 2025) představil čtyři modely, přičemž tři jsou dostupné nyní a vlajková loď (Premier) dorazí v Q1 2026. Hlavním prodejním argumentem není "magická inteligence", ale rychlost (latence), cena a integrace videa.

**Nova Micro**

Role: Textový model optimalizovaný pro rychlost a nízkou cenu. \
Konkurence: Grok-4-fast, Llama, Haiku.\
Analýza: Amazon tvrdí, že jde o nejrychlejší model ve své třídě. Pro vývojáře na AWS to znamená možnost nahradit externí "levné" modely (jako Llama na vlastním GPU) nativní službou s milisekundovou odezvou.

**Nova Lite & Pro**

Role: Multimodální modely schopné zpracovávat text, obrázky a video. \
Výkon: Amazon uvádí, že Nova Pro překonává GPT-4o v přesnosti, rychlosti a zpracování videa. \
Analýza: "Překonat GPT-4o" je v prosinci 2025 povinná jízda, nikoliv revoluce (Gemini 3 Pro je dále). Klíčová je zde schopnost chápat video. Pokud máte v S3 uložené terabajty videozáznamů, Nova Pro je dokáže analyzovat bez nutnosti posílat data mimo AWS.

**Nova Premier (Q1 2026)**

Toto má být model pro komplexní reasoning, který vyzve Gemini 3 Pro a DeepSeek Speciale. Zatím ale není dostupný, takže v prosincovém srovnání ho nemůžeme hodnotit.

Amazon Nova nemění hru pro běžného uživatele (jako Grok cenou nebo DeepSeek matematikou), ale mění hru pro firmy na AWS. Díky skvělé integraci, jednotné fakturaci a dobrému výkonu se vyplatí tyto modely minimálně zvážit. 

Pokud vaše infrastruktura běží na AWS, Amazon právě odstranil důvod, proč používat OpenAI.

**VÍTĚZ (Integrace):** Amazon Nova Pro. Podle interních testů Amazonu tento model překonává GPT-4o a exceluje v analýze videa. Pro firmy je zásadní, že data neopouští ekosystém AWS Bedrock.

**Specialita:** Model Distillation. Amazon umožňuje vzít velký model (Nova Pro) a "naučit" menší modely (Micro) specifické úlohy vaší firmy. To je cesta k extrémní efektivitě, kterou OpenAI ani Google v této formě nenabízejí.

## Jaký model použít na jaký typ úloh?

Níže uvádím aktualizovaná doporučení pro klíčové oblasti, zohledňující nástup DeepSeeku:

### Sumarizace a Analýza rozsáhlých dokumentů (RAG)

- **Zajímavá alternativa: Grok 4.1 Fast Reasoning.** S kontextem 2M tokenů a cenou $0.20 jde o ekonomicky atraktivní volbu. Doporučuji jej vyzkoušet na interních dokumentech, zda jeho výstupy odpovídají vašim požadavkům.

- **Ověřená kvalita: Gemini 2.5 Flash / Pro.** Pokud potřebujete mít jistotu, že modelu neunikne detail v dlouhém textu, Gemini zatím vykazuje stabilnější výsledky.

Apple v tichosti [vydal framework CLaRa](https://github.com/apple/ml-clara), který propojuje RAG koncept s modelem instalovaným přímo v zařízení, takže funguje lokálně. Místo aby AI četla text, čte "myšlenky". CLaRa dokáže zkomprimovat vaše dokumenty (smlouvy, skripta, maily) až 128x, aniž by ztratila kontext. Umožňuje tak provozovat pokročilý RAG (chatování s dokumenty) přímo na vašem Macu s minimálními nároky na paměť.

Pokud stavíte aplikaci, která má "rozumět" uživatelským datům a běžet offline, [CLaRa-7B](https://huggingface.co/apple/CLaRa-7B-Instruct) je technologicky nejpokročilejší řešení na trhu. Není to náhrada za GPT-4, je to náhrada za vaši databázi.

### 1. Překlad z angličtiny do češtiny

-   **Smart Choice (Cena/Výkon): Claude 4.5 Haiku.**
    Haiku 4.5 (cca $0.12/run) dosahuje v testech téměř stejných kvalitativních výsledků jako drahý Sonnet, ale za zlomek ceny.
    
-   **Budget Choice (Nejlevnější dostačující): Grok-4-fast.**
    S cenou $0.013 je bezkonkurenčně nejlevnější západní model.

### 2. Překlad z čínštiny do češtiny

-   **Smart Choice (Cena/Výkon): DeepSeek-V3.2-exp.**
    Čínský model, který nativně chápe nuance mandarínštiny. Cena ($0.018) je zanedbatelná. Nabízí nejvyšší kvalitu překladu předtím, než byste museli sáhnout po drahém Gemini 3 Pro.

### 3. Analýza finančních dat a Matematika

Zde nastala velká změna.

-   **Smart Choice (Komplexní analýza): Gemini 3 Pro.**
    Pro práci s multimodálními daty (PDF grafy + Excel) je Gemini stále nejbezpečnější volba díky pochopení kontextu.
    
-   **Hardcore Math & Logic: DeepSeek-V3.2 Speciale.**
    Pokud potřebujete čistou matematiku, statistiku nebo složité výpočty a nevadí vám, že si model chvíli "zapřemýšlí" (a sežere hodně tokenů), DeepSeek je nyní přesnější než Gemini.

-   **K vyzkoušení: Grok 4.1 Fast Reasoning.** 
Díky deklarovaným "Reasoning" schopnostem by měl zvládat strukturu (JSON) lépe než starší modely. Je vhodné jej nasadit paralelně a ověřit přesnost na datech.    

### 4. Sestavení horoskopu a kreativa

-   **Smart Choice (Cena/Výkon): Claude 4.5 Haiku.**
    Opět vítězí "malý" Anthropic. Dokáže simulovat mystický nebo empatický tón mnohem lépe než strohý Grok.
    
-   **Budget Choice:** DeepSeek-V3.2 (přes prompt engineering).

### 5. Programování (Vývoj softwaru)

-   **Smart Choice (Cena/Výkon): DeepSeek-V3.2 Speciale / Qwen3-Coder.**
    Pro náročné algoritmické úlohy je DeepSeek Speciale (CodeForces 2701) novou špičkou, která konkuruje Gemini 3 Pro za potenciálně nižší cenu. Pro rutinní kódování v IDE je Qwen3 stále nepřekonatelný poměrem cena/výkon.
    
-   **Agentní vývoj:** Claude Code (běžící na Sonnet/Opus). Zde je Anthropic stále nejpraktičtější díky spolehlivosti v terminálu.

## Závěr: Jakou architekturu zvolit pro vývoj? Router!

Pokud chcete maximalizovat efektivitu, doporučuji **hybridní přístup**. Registrujte se na [OpenRouter.ai](https://www.openrouter.ai) a vybírejte si model podle úkolu:

1.  **Výchozí model:** **Claude 4.5 Haiku** (texty, chat) nebo po otestování **Grok 4.1 Fast Reasoning**. Zkuste jej nasadit na objemové úlohy. Pokud se osvědčí, ušetříte významné prostředky ($0.20/1M).
2.  **Komunikace a Styl: Claude 4.5 Haiku**. Pro texty, kde záleží na formě.
3.  **Matematika / Hardcore Kód:** **DeepSeek-V3.2 Speciale** (když potřebujete hrubou sílu a genialitu).
4.  **Kritický byznys kontext:** **Gemini 3 Pro** (všeobecná inteligence).

OpenAI v těchto datech ztrácí dech. GPT-5.1 není lídrem trhu a v matematice dostává na frak od čínského modelu. Pokud nepřijdou s rychlou iterací, Google a Čína jim rozeberou trh.