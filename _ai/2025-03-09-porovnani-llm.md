---
date: 2025-03-09
layout: post
order: 2
thumbnail: https://cxscoop.com/wp-content/uploads/2023/07/Google-Microsoft-OpenAI-and-Anthropic-to-Form-Industry-Group-1440x914.png
title: Přehled LLM OpenAI, Anthropic a Google - na co jsou které modely vhodné (květen 2025) + přehled benchmarků
---

Situace s modely umělé inteligence začala být pro člověka, který to systematicky nesleduje, poněkud nepřehledná. Všechny hlavní firmy nabízejí několik modelů, které se na webovém rozhraní viditelně neliší a je od dodavatelů jen malá nápověda, k čemu jsou vhodnější a k čemu méně. Připravil jsem vám tedy přehledovou tabulku jednotlivých rodin modelů. Tím se můžete zorientovat. Nezapomínejte na to, že modely se na webovém rozhraní liší tím, kolik dotazů máte povoleno (zejména u Claude) a při použití přes API pak především cenou. 

__Co konkrétně se v tomto článku dozvíte?__ 
* Obsah
{:toc} 

A protože se na to často ptáte, tady je můj osobní setup, když se musím trochu víc koukat na cenu (tj. převážně v případě, když jedu přes API za peníze):

- Nejlepší model pro všeobecné použití: o3 (fakt!), dále Sonet 3.7 pokud chci používat češtinu, Gemini Pro 2.5 Experimental pokud je to na jazyk nenáročné (jinak OpenAI GPT-4.5, ale za to se nedoplatíte)
- Nejlepší okamžité odpovědi na cokoliv:  Perplexity Pro bez [Deepseek](/item/deepseek/) volby
- Zpracování velkého množství obsahu najednou (např. vytahání podstatných info z přepisů zastupitelstev): Gemini 2.5 Pro Experimental.
- Nejlepší psaní textu (a odůvodnění): o3 nebo 3.7 Sonet
- Nejlepší pro analýzu PDF, porozumění datům: o3 nebo 3.7 Sonet
- Nejlepší pro OCR: [Mistral OCR](https://mistral.ai/news/mistral-ocr)
- Nejlepší pro kód: 3.7 Sonnet (v Cursoru to počátkem března haprovalo, ladí se, tam nechte 3.5)
- Nejlepší agent pro výzkum: OpenAI Deep Research nebo Gemini Deep Research s myšlením Flash 2 je dobrý pro rychlejší a rozsáhlejší výzkum - Sonet 3.7 je málo důkladný. 
- Nejlepší uvažování pro pokročilou analýzu: o1 Pro - pokud nemáte, tak spíš GPT-4.5 s výhodou možnost zapnout si dohledávání na webu nebo o3. 
- Nejlepší pro okamžité odpovědi s úžasným vyhledáváním: Grok 3 (v češtině občas hapruje)
- Nejlepší multimodální: Gemini 2.0 Flash experimental / Gemini 2.0 Pro experimental

Můj univerzální model na všechno přes chatgpt: o3 - vyzkoušejte [prompt, jak vyhledat polohu pořízené fotografie](https://www.marigold.cz/item/urceni-polohy-fotky-chatgpt-o3/). 

Velmi často také nechávám používat na zpracování textu starý GPT-3.5, když mi jde o cenu na úlohy jazykového typu (najdi mi v přepisu všechna jména atd) - ale přes OpenRouter často narazíte na modely, které jsou mnohem silnější a zdarma, takže není důvod po starých modelech sahat. A po pravdě, ve web rozhraní OpenAI často používám také 4o, prostě proto, že už mám vychytané, co mu dělá a nedělá problémy... 

Osobně výrazně preferuju modely, u kterých se dá zapnout dohledávání infomací na webu a pro vývojáře je téměř nutností seznámit se s [MCP](/ai/mcp). 

__Co konkrétně se v tomto článku dozvíte?__ 
* Obsah
{:toc} 

## OpenAI 

| **Model** | **Počet parametrů** | **Vhodné pro úlohy** | **Klíčové vlastnosti** |
|-------------------|---------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **o1** | Neznámý | Úlohy vyžadující uvažování a řešení problémů ve vědě, kódování a matematice | V ChatGPT kontextové okno 32k tokenů, excelentní v matematice a kódování |
| **o3** | Neznámý | Programování a kódování, matematika, věda a úlohy vyžadující pokročilé uvažování | Rozšířené kontextové okno až 200K tokenů, výstup až 100K tokenů |
| **o4-mini** | Neznámý | Matematika, vizuální uvažování, a nákladově efektivní vývojové práce | Rychlý, cenově dostupný a pozoruhodně silný v matematických a vizuálních úlohách |
| **o4-mini-high** | Neznámý | Stejné úlohy jako o4-mini, ale s důrazem na hlubší uvažování | Stejný model jako o4-mini s nastavením reasoning_effort na high |
| **o3-mini** | Neznámý | Uvažování s nástroji, práce s daty, rozpoznávání obrazu | Dokáže používat nástroje, propojovat různé nástroje dohromady a přizpůsobovat se |
| **GPT-4.1** | Neznámý | Kódování, instrukce following, multimodální úlohy s dlouhým kontextem | Kontextové okno až 1 milion tokenů, zlepšené porozumění dlouhému kontextu |
| **GPT-4o** | ~200 miliard (odhad) | Multimodální úlohy (text, obraz), interakce v různých jazycích, vision úlohy | Integrace textu a obrazů v jednom modelu, zvýšená přesnost v interakcích |

### Shrnutí vhodnosti použití:
1. **o1:** Vhodný pro řešení složitých problémů v oblastech jako výzkum, strategie, kódování, matematika a věda. V ChatGPT má kontextové okno 32k tokenů.

2. **o3:** Nejsilnější reasoning model OpenAI s vysokým výkonem napříč doménami. Stanovuje nový standard pro matematiku, vědu, kódování a vizuální reasoning úlohy. Dosáhl 69,1% přesnosti na SWE-bench Verified a 88,9% na AIME 2025 v matematice.

3. **o4-mini:** Ideální pro analýzu velkého množství dat, vynikající v matematických a vizuálních úlohách při nižších nákladech. Dosáhl 68,1% přesnosti na SWE-bench Verified a 92,7% na AIME 2025.

4. **o4-mini-high:** Stejný model jako o4-mini s nastaveným vysokým stupněm uvažování (reasoning_effort), což umožňuje hlubší analýzu problémů na úkor rychlosti.

5. **o3-mini:** Škálovaná verze o3 optimalizovaná pro výkon a nákladovou efektivitu. K dispozici ve třech variantách (low/medium/high) podle úrovně uvažování.

6. **GPT-4.1:** Vyniká v kódování (SWE-bench Verified), instrukcích a multimodálním porozumění s dlouhým kontextem. Podporuje kontextové okno až 1 milion tokenů.

7. **GPT-4o:** Multimodální model přijímající text nebo obrazové vstupy a generující text. Překonává předchozí modely v neangličtině a vision úlohách.

## Anthropic Claude

| Model | Počet parametrů | Vhodné pro úlohy | Klíčové vlastnosti |
|-------|-----------------|-------------------|---------------------|
| Claude 3.7 Sonnet | Neznámý | Komplexní analýzy, kreativní úkoly, programování, zpracování kódu | Výrazná zlepšení v kódování a front-end vývoji, "rozšířené myšlení" umožňující detailní uvažování, hybridní reasoning model |
| Claude 3.5 Sonnet | Neznámý | Všeobecné použití, analýza dat, generování obsahu | Vylepšená verze 3 Sonnet, rychlejší než Opus |
| Claude 3.5 Haiku | Neznámý | Rychlé zpracování, nákladově efektivní úlohy | Nejrychlejší a nejlevnější model z rodiny Claude 3.5 |
| Claude 3 Opus | Neznámý | Komplexní analýzy, vědecký výzkum, pokročilé uvažování | Nejvýkonnější model, nejlepší v řešení složitých úloh |

### Shrnutí vhodnosti použití:

1. **Claude 3.7 Sonnet:** První hybridní reasoning model na trhu, schopný produkovat okamžité odpovědi nebo rozšířené, krok za krokem uvažování, které je viditelné pro uživatele. Vyniká v kódování, front-end vývoji a agenčním kódování. Zachovává 200K token kontextové okno, ale rozšířené myšlení umožňuje efektivnější uvažování nad dlouhými dokumenty.

2. **Claude 3.5 Sonnet:** Univerzální model pro širokou škálu úloh. Dobře se hodí pro analýzu dat a generování obsahu.

3. **Claude 3.5 Haiku:** Nejlepší volba pro aplikace vyžadující rychlé odpovědi a nízké náklady.

4. **Claude 3 Opus:** Nejvhodnější pro nejnáročnější úlohy vyžadující hluboké porozumění a analýzu, jako je vědecký výzkum nebo komplexní rozhodování.

Všechny modely mají pokročilé multimodální schopnosti, včetně zpracování textu a obrazu, a nabízejí zlepšené multilingvální porozumění.

Kontextové okno pro modely Anthropic je 200 000 tokenů, čili cca 680 000 unicode znaků.

## Google Gemini

| **Model** | **Max. počet tokenů** | **Vhodné pro úlohy** | **Klíčové vlastnosti** |
|------------------------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Gemini 2.5 Pro** | 1 048 576 (vstup), plánováno 2 miliony | Kódování, matematika, logika, věda a úlohy vyžadující uvažování | Nativní multimodalita, silné uvažovací schopnosti, rozšířené myšlení |
| **Gemini 2.5 Flash** | 1 048 576 (vstup) | Multimodální úlohy s vyváženým poměrem rychlosti a výkonu | Kontrola množství uvažování pro optimalizaci latence a nákladů |
| **Gemini 2.0 Flash** | 1 048 576 (vstup), 8 192 (výstup) | Multimodální úlohy (text, obraz, audio, video), generování kódu, analýza dat | Multimodální vstupy, podpora nástrojů, optimalizace na všeobecné použití |
| **Gemini 2.0 Flash-Lite** | 1 048 576 (vstup), 8 192 (výstup) | Rychlé a nákladově efektivní úlohy vyžadující multimodální vstupy | Optimalizace na rychlost a nízké náklady |
| **Gemini 2.0 Pro Experimental** | 2 097 152 (vstup), 8 192 (výstup) | Komplexní úlohy: programování, matematika, dlouhé kontexty | Nejdelší kontextové okno, vylepšené schopnosti faktické přesnosti |
| **Gemini 2.0 Flash Thinking Experimental** | 1 048 576 (vstup), 65 536 (výstup) | Úlohy vyžadující transparentní myšlenkový proces a hluboké uvažování | Zobrazuje myšlenkový proces modelu, lepší schopnosti uvažování |

### Shrnutí vhodnosti použití:
1. **Gemini 2.5 Pro:** Nejpokročilejší model pro komplexní úlohy. Vyniká v uvažování a kódovacích schopnostech, vedoucí v běžných kódovacích, matematických a vědeckých benchmarcích.

2. **Gemini 2.5 Flash:** Model s funkcí rozšířeného myšlení, nabízející vyvážené schopnosti při rozumné ceně. Aplikuje vhodné myšlenkové strategie napříč různými scénáři.

3. **Gemini 2.0 Flash:** Univerzální model pro multimodální úlohy s vysokou rychlostí a širokou podporou funkcí.

4. **Gemini 2.0 Flash-Lite:** Ideální pro aplikace s omezeným rozpočtem nebo tam, kde je prioritou rychlost.

5. **Gemini 2.0 Pro Experimental:** Nejlepší volba pro složité úlohy vyžadující dlouhé kontexty a přesnost.

6. **Gemini 2.0 Flash Thinking Experimental:** Vhodný pro analytické úkoly, kde je důležitá transparentnost myšlenkového procesu.

Každý model má unikátní zaměření, což umožňuje jejich využití v různých scénářích od rychlých aplikací po komplexní analýzy nebo vzdělávací projekty.

## Benchmarky

Potřebujete nějak modely porovnat mimo toto krátké shrnutí? Tak se podívejte na nejrůznější bechmarky, testy LLM - ale dejte si pozor, abyste si vybrali žebříček, který odpovídá typu vašeho problému, tedy typu úloh, pro něž chcete LLM porovnat. Tady jsou mnou vybrané žebříčky:

- [SimpleBench](https://simple-bench.com/index.html): open‑source sada jednoduchých testů pro rychlé porovnání základních schopností různých LLM v několika klíčových úlohách.  
- [SOLO‑Bench](https://github.com/jd-3d/SOLOBench): benchmark zaměřený na vyhodnocení schopnosti modelů řešit jednotlivé úlohy nezávisle (single‑objective) v rámci plánování a optimalizace.  
- [AidanBench](https://aidanbench.com): online platforma hodnotící výkonnost LLM na generování textu a porozumění přirozenému jazyku s důrazem na praktické scénáře.  
- [SEAL by Scale (MultiChallenge leaderboard)](https://scale.com/leaderboard): komplexní leaderboard s víceúlohami, který porovnává modely napříč různorodými výzvami, například překlad, shrnutí a Q&A.  
- [LMArena (Style Control)](https://beta.lmarena.ai/leaderboard): interaktivní žebříček, který kromě výkonu sleduje i míru kontroly stylu generovaného textu u různých LLM.  
- [LiveBench](https://livebench.ai): živě aktualizovaný benchmark měřící kvalitu odpovědí modelů na reálné uživatelské dotazy v reálném čase.  
- [ARC‑AGI](https://arcprize.org/leaderboard): soutěžní žebříček pro hodnocení obecné umělé inteligence na základě výkonu v standardizovaných úlohách ze školních testů (ARC dataset).  
- [Thematic Generalization by LechMazur](https://github.com/lechmazur/generalization): projekt testující schopnost modelů zobecňovat znalosti na nová témata na základě krátkých instrukcí.  
- [Elimination Game by LechMazur](https://github.com/lechmazur/elimination_game): hra‑benchmark, kde modely postupně eliminují nesprávné možnosti a hodnotí se jejich logické deduktivní schopnosti.  
- [Confabulations by LechMazur](https://github.com/lechmazur/confabulations): test odhalující, jak často a v jakém rozsahu LLM generují smyšlené („hallucinated“) informace mimo pravdivý kontext.  
- [EQBench (Longform writing leaderboard)](https://eqbench.com): žebříček hodnotící kvalitu delších narativních a esejistických výstupů LLM podle human‑aligned kritérií.  
- [Fiction‑Live Bench](https://fiction.live/stories/Fiction-liveBench-Mar-25-2025/oQdzQvKHw8JyXbN87): benchmark založený na skutečných interaktivních příbězích z platformy Fiction.Live, měřící schopnost modelů pokračovat v narrativu.  
- [MC‑Bench (ordered by winrate)](https://mcbench.ai/leaderboard): leaderboard, kde jsou modely seřazeny podle podílu vítězství v head‑to‑head srovnáních (winrate), nikoli podle Elo.  
- [TrackingAI – IQ Bench](https://trackingai.org/home): online testovací sada simulující IQ‑testové úlohy (logika, vizuální hádanky) pro měření „inteligence“ LLM.  
- [Dubesor LLM](https://dubesor.de/benchtable.html): lehký benchmark zobrazující aktuální výkon různých LLM na jednoduchém přehledovém Dashboardu.  
- [Balrog‑AI](https://balrogai.com): platforma pro hodnocení obecných schopností LLM, zejména generování koherentního textu a odpovědí na komplexní dotazy.  
- [Misguided Attention](https://github.com/cpldcpu/MisguidedAttention): benchmark odhalující slabiny v pozornosti modelů, kde nesprávně zaměřují váhu na irelevantní části vstupu.  
- [Snake‑Bench](https://snakebench.com): jednoduchý online benchmark testující schopnosti LLM generovat a vysvětlovat herní strategie pro hru Snake.  
- [SmolAgents LLM](https://huggingface.co/spaces/smolagents/smolagents-leaderboard): leaderboard na HuggingFace Spaces porovnávající malé agentní modely (SmolAgents) v úlohách GAIA a SimpleQA.  
- [Context‑Arena (MRCR and Graphwalks)](https://contextarena.ai): benchmark testující udržení dlouhodobého kontextu (MRCR) a procházení znalostních grafů (Graphwalks).  
- [OpenCompass](https://rank.opencompass.org.cn/home): čínský otevřený ranking LLM zaměřený na širokou škálu úloh včetně strojového čtení, překladů a logiky.  
- [HHEM (Hallucination Benchmark)](https://huggingface.co/spaces/vectara/leaderboard): benchmark měřící míru a charakter halucinací (nepravdivých tvrzení) v odpovědích modelů.  

**Benchmarky pro kódování, matematiku a agentní úlohy**

- [Aider-Polyglot-Coding](https://aider.chat/docs/leaderboards/): benchmark hodnotící schopnosti modelů v kódování napříč mnoha jazyky a úlohami.  
- [BigCodeBench](https://bigcode-bench.github.io): sada testů pro měření výkonu LLM v úlohách generování a analýzy kódu.  
- [WebDev-Arena](https://web.lmarena.ai/leaderboard): leaderboard zaměřený na webové vývojové úlohy, jako je psaní HTML/CSS a JavaScript.  
- [WeirdML](https://htihle.github.io/weirdml.html): benchmark zkoumající neobvyklé a extrémní scénáře pro modely strojového učení.  
- [Symflower Coding](https://symflower.com/en/company/blog/2025/dev-quality-eval-v1.0-anthropic-s-claude-3.7-sonnet-is-the-king-with-help-and-deepseek-r1-disappoints/): vyhodnocení kvality kódu modelů podle standardu Symflower.  
- [PHYBench](https://phybench-official.github.io/phybench-demo/): demonstrační stránka testující fyzikální a matematické schopnosti LLM.  
- [MathArena](https://matharena.ai): platforma pro benchmark matematických úloh všech úrovní obtížnosti.  
- [Galileo Agent](https://huggingface.co/spaces/galileo-ai/agent-leaderboard): leaderboard agentních modelů hodnocených na základě interaktivních úloh v prostředí Galileo.  
- [XLANG Agent](https://arena.xlang.ai/leaderboard): žebříček agentních modelů zaměřených na vícejazyčné úlohy.  

**Důležité pro sledování nástupu nových LLM**

- [METR long task benchmarks (incl. RE Bench)](https://metr.org): benchmark pro dlouhodobé úlohy klíčové pro sledování posunu AI k vyšší autonomii.  
- [PaperBench](https://openai.com/index/paperbench/): test výkonu LLM při generování a analýze vědeckých abstraktů.  
- [SWE-Lancer](https://openai.com/index/swe-lancer/): benchmark simulující úlohy softwarového inženýrství (SWE) pro hodnocení schopností modelů.  
- [MLE-Bench](https://github.com/openai/mle-bench): sada úloh pro měření maximální pravděpodobnosti učení a generalizace.  
- [SWE-Bench](https://swebench.com): online platforma pro hodnocení modelů v běžných úlohách softwarového inženýrství.  

**Ostatní klasiky, které je vždy dobré vidět při vydání nového modelu**

- [GPQA-Diamond](https://github.com/idavidrein/gpqa): rozšířený benchmark pro testování obecného porozumění otázkám s výběrem odpovědí.  
- [SimpleQA](https://openai.com/index/introducing-simpleqa/): benchmark zaměřený na jednoduché otázky a odpovědi, často používaný pro srovnání základní schopnosti LLM.  
- [Tau-bench](https://github.com/sierra-research/tau-bench): sada testů pro hodnocení přesnosti a rychlosti modelů v široké škále úloh.  
- [SciCode](https://github.com/scicode-bench/SciCode): benchmark pro generování a analýzu vědeckého kódu.  
- [MMMU](https://mmmu-benchmark.github.io/#leaderboard): žebříček víceúrovňových modelů měřících schopnost zvládat rozsáhlé multisektorové úlohy.  
- [Humanities Last Exam (HLE)](https://github.com/centerforaisafety/hle): test simulující závěrečné zkoušky v humanitních oborech.  

**Přehled klasických benchmarků (GPQA, SimpleQA, AIME, MMLU, ...)**

- [Simple-Evals](https://github.com/openai/simple-evals): knihovna a sada nástrojů pro rychlé evaluace LLM na základních úlohách.  
- [Vellum AI](https://vellum.ai/llm-leaderboard): online žebříček výkonu LLM v širokém spektru úloh.  
- [Artificial Analysis](https://artificialanalysis.ai): platforma nabízející analytické nástroje pro hodnocení generativních modelů.  

## Ponaučení

Ve skutečnosti, pokud budete něco vyvíjet, doporučuji nejdříve ve webovém rozhraní odladit prompt na konkrétní model. Nejprve si napište prompt, pak jej vyzkoušejte na jednotlivé modely ve webovém rozhraní a zjistěte, který vám vyhovuje nejlépe. Pak přizpůsobujte prompt tak, abyste dosáhli přesně toho výstupu, jaký potřebujete.