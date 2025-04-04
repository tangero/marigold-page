---
date: 2025-03-09
layout: post
order: 2
thumbnail: https://cxscoop.com/wp-content/uploads/2023/07/Google-Microsoft-OpenAI-and-Anthropic-to-Form-Industry-Group-1440x914.png
title: Přehled LLM OpenAI, Anthropic a Google - na co jsou které modely vhodné?
---

Situace s modely umělé inteligence začala být pro člověka, který to systematicky nesleduje, poněkud nepřehledná. Všechny hlavní firmy nabízejí několik modelů, které se na webovém rozhraní viditelně neliší a je od dodavatelů jen malá nápověda, k čemu jsou vhodnější a k čemu méně. Připravil jsem vám tedy přehledovou tabulku jednotlivých rodin modelů. Tím se můžete zorientovat. Nezapomínejte na to, že modely se na webovém rozhraní liší tím, kolik dotazů máte povoleno (zejména u Claude) a při použití přes API pak především cenou. 

A protože se na to často ptáte, tady je můj osobní setup, když se musím trochu víc koukat na cenu (tj. převážně v případě, když jedu přes API za peníze):

- Nejlepší model pro všeobecné použití: Sonet 3.7 pokud chci používat češtinu, Gemini Pro 2.0 Experimental pokud je to na jazyk nenáročné (jinak OpenAI GPT-4.5, ale za to se nedoplatíte)
- Nejlepší okamžité odpovědi na cokoliv:  Perplexity Pro bez [Deepseek](/item/deepseek/) volby
- Zpracování velkého množství obsahu najednou (např. vytahání podstatných info z přepisů zastupitelstev): Gemini 2.0 Pro Experimental.
- Nejlepší psaní textu (a odůvodnění): 3.7 Sonet
- Nejlepší pro analýzu PDF, porozumění datům: 3.7 Sonet
- Nejlepší pro OCR: [Mistral OCR](https://mistral.ai/news/mistral-ocr)
- Nejlepší pro kód: 3.7 Sonnet (v Cursoru to počátkem března haprovalo, ladí se, tam nechte 3.5)
- Nejlepší agent pro výzkum: OpenAI Deep Research nebo Gemini Deep Research s myšlením Flash 2 je dobrý pro rychlejší a rozsáhlejší výzkum - Sonet 3.7 je málo důkladný. 
- Nejlepší uvažování pro pokročilou analýzu: o1 Pro - pokud nemáte, tak spíš GPT-4.5 s výhodou možnost zapnout si dohledávání na webu. 
- Nejlepší pro okamžité odpovědi s úžasným vyhledáváním: Grok 3 (v češtině občas hapruje)
- Nejlepší multimodální: Gemini 2.0 Flash experimental / Gemini 2.0 Pro experimental

Velmi často také nechávám používat na zpracování textu starý GPT-3.5, když mi jde o cenu na úlohy jazykového typu (najdi mi v přepisu všechna jména atd) - ale přes OpenRouter často narazíte na modely, které jsou mnohem silnější a zdarma, takže není důvod po starých modelech sahat. A po pravdě, ve web rozhraní OpenAI často používám také 4o, prostě proto, že už mám vychytané, co mu dělá a nedělá problémy... 

Osobně výrazně preferuju modely, u kterých se dá zapnout dohledávání infomací na webu a pro vývojáře je téměř nutností seznámit se s [MCP](/ai/mcp). 

__Co konkrétně se v tomto článku dozvíte?__ 
* Obsah
{:toc} 

## OpenAI 

Zde je tabulka porovnávající modely OpenAI o1, o3-mini (včetně variant low/medium/high), GPT-4o a GPT-4.5 z hlediska parametrů a vhodnosti použití:

| **Model**        | **Počet parametrů**       | **Vhodné pro úlohy**                                                                                       | **Klíčové vlastnosti**                                                                                     |
|-------------------|---------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **o1**           | ~200 miliard (odhad)      | STEM (věda, technologie, inženýrství, matematika), generování kódu, vědecký výzkum, pokročilé uvažování   | Vylepšené uvažování (Chain of Thought), excelentní v matematice a kódování, analýza obrázků               |
| **o3-mini-low**   | ~8 miliard (odhad)        | Nákladově efektivní úlohy s nižšími požadavky na přesnost                                                 | Optimalizováno pro nízké náklady, základní úroveň uvažování                                               |
| **o3-mini-medium**| ~8 miliard (odhad)        | Vyvážené úlohy mezi výkonem a náklady                                                                     | Střední úroveň uvažování                                                                                  |
| **o3-mini-high**  | ~8 miliard (odhad)        | Úlohy vyžadující vyšší přesnost a lepší analytické schopnosti                                             | Nejvyšší úroveň uvažování, delší doba zpracování                                                          |
| **GPT-4o**        | ~200 miliard (odhad)      | Multimodální úlohy (text, obraz, audio), reálné interakce, analýza dat, překlady                          | Multimodalita (text, obraz, audio), velké kontextové okno (128 000 [tokenů](/ai/tokeny-versus-slova/)), generování řeči               |
| **GPT-4.5**       | Neznámý (větší než GPT-4) | Široké spektrum úloh: kreativní psaní, programování, komplexní analýzy                                    | Největší model OpenAI s vylepšeným kontextovým oknem (128 000 [tokenů](/ai/tokeny-versus-slova/)), excelentní v programování a analýze |

### Shrnutí vhodnosti použití:
1. **o1:** Ideální pro vědecký výzkum, matematiku a složité technické problémy. Nabízí pokročilé uvažování a schopnost analyzovat obrazy.
2. **o3-mini:** Nákladově efektivní volba pro STEM úlohy. Varianta "high" je vhodná pro přesnější analýzy.
3. **GPT-4o:** Skvělý pro multimodální aplikace zahrnující text, obraz a zvuk. Vhodný pro překlady, reálné interakce a datovou analýzu.
4. **GPT-4.5:** Nejuniverzálnější model s vysokou přesností a velkým kontextovým oknem. Vhodný pro kreativní psaní, programování a komplexní analýzy.

Každý model má své specifické silné stránky a je vhodný pro různé typy aplikací v závislosti na požadavcích na výkon, přesnost nebo náklady.

Zdroje:
- [OpenAI o1 explained: Everything you need to know](https://www.techtarget.com/whatis/feature/OpenAI-o1-explained-Everything-you-need-to-know)
- [OpenAI o3 explained: Everything you need to know](https://www.techtarget.com/WhatIs/feature/OpenAI-o3-explained-Everything-you-need-to-know)
- [GPT-4o explained: Everything you need to know - TechTarget](https://www.techtarget.com/whatis/feature/GPT-4o-explained-Everything-you-need-to-know)
- [What Is GPT-4o? - IBM](https://www.ibm.com/think/topics/gpt-4o)


## Anthropic Claude

Zde je tabulka porovnávající modely Claude 3.7 Sonnet, 3.5 Sonnet, 3.5 Haiku a 3 Opus z hlediska parametrů a vhodnosti použití:

| Model | Počet parametrů | Vhodné pro úlohy | Klíčové vlastnosti |
|-------|-----------------|-------------------|---------------------|
| Claude 3.7 Sonnet | Neznámý | Vyvážené úlohy mezi výkonem a rychlostí, kreativní úkoly, programování | Vylepšené schopnosti oproti 3.5, "rozšířené myšlení" |
| Claude 3.5 Sonnet | Neznámý | Všeobecné použití, analýza dat, generování obsahu | Vylepšená verze 3 Sonnet, rychlejší než Opus |
| Claude 3.5 Haiku | Neznámý | Rychlé zpracování, nákladově efektivní úlohy | Nejrychlejší a nejlevnější model z rodiny Claude 3.5 |
| Claude 3 Opus | Neznámý | Komplexní analýzy, vědecký výzkum, pokročilé uvažování | Nejvýkonnější model, nejlepší v řešení složitých úloh |

### Shrnutí vhodnosti použití:

1. **Claude 3.7 Sonnet:** Ideální pro úlohy vyžadující rovnováhu mezi výkonem a rychlostí. Vhodný pro kreativní práci a programování.
2. **Claude 3.5 Sonnet:** Univerzální model pro širokou škálu úloh. Dobře se hodí pro analýzu dat a generování obsahu.
3. **Claude 3.5 Haiku:** Nejlepší volba pro aplikace vyžadující rychlé odpovědi a nízké náklady.
4. **Claude 3 Opus:** Nejvhodnější pro nejnáročnější úlohy vyžadující hluboké porozumění a analýzu, jako je vědecký výzkum nebo komplexní rozhodování.

Všechny modely mají pokročilé multimodální schopnosti, včetně zpracování textu a obrazu, a nabízejí zlepšené multilingvální porozumění.

Kontextové okno pro modely Anthropic je 200 000 [tokenů](/ai/tokeny-versus-slova/), čili cca 680 000 unicode znaků. 

Zdroje
- [Introducing the next generation of Claude - Anthropic](https://www.anthropic.com/news/claude-3-family)
- [The Claude 3 Model Family: Opus, Sonnet, Haiku - Anthropic](https://anthropic.com/claude-3-model-card)
- [Claude 3 SOTA Model Suite: Opus, Sonnet, and Haiku - Encord](https://encord.com/blog/claude-3-explained/)
- [AI Anthropic Claude 3 Detailed Overview - Latenode](https://latenode.com/blog/ai-anthropic-claude-3-overview)
- [claude-3-opus model - Clarifai - The World's AI](https://clarifai.com/anthropic/completion/models/claude-3-opus)

## Google Gemini

Zde je tabulka porovnávající modely Google Gemini 2.0 z hlediska parametrů a vhodnosti použití. Starší modely 1.5 už jsem vypustil, nevyplatí se jimi zabývat snad už ani kvůli ceně. 

| **Model**                                | **Max. počet [tokenů](/ai/tokeny-versus-slova/)**       | **Vhodné pro úlohy**                                                                                       | **Klíčové vlastnosti**                                                                                     |
|------------------------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Gemini 2.0 Flash**                     | 1 048 576 (vstup), 8 192 (výstup) | Multimodální úlohy (text, obraz, audio, video), generování kódu, analýza dat                              | Multimodální vstupy/výstupy, podpora reálného času (Multimodal Live API), generování obrázků a řeči        |
| **Gemini 2.0 Flash-Lite**                | 1 048 576 (vstup), 8 192 (výstup) | Rychlé a nákladově efektivní úlohy vyžadující multimodální vstupy                                         | Optimalizace na rychlost a nízké náklady, nepodporuje multimodální výstupy ani pokročilé nástroje          |
| **Gemini 2.0 Pro Experimental**          | 2 097 152 (vstup), 8 192 (výstup) | Komplexní úlohy: programování, matematika, dlouhé kontexty                                               | Nejdelší kontextové okno, vylepšené schopnosti faktické přesnosti a řešení složitých problémů              |
| **Gemini 2.0 Flash Thinking Experimental** | 1 048 576 (vstup), 65 536 (výstup) | Úlohy vyžadující transparentní myšlenkový proces a hluboké uvažování                                      | Zobrazuje myšlenkový proces modelu, lepší schopnosti uvažování než základní Flash                          |
| **Gemini 2.0 Flash Experimental**        | 1 048 576 (vstup), 8 192 (výstup) | Testování nových funkcí: text-to-speech, multimodální generace                                            | Experimentální funkce jako generování řeči a obrázků                                                      |
| **LearnLM 1.5 Pro Experimental**         | Neznámý                      | Vzdělávací aplikace a personalizované učení                                                               | Optimalizováno pro vzdělávací účely, zaměřeno na adaptivní učení a personalizaci obsahu                    |

### Shrnutí vhodnosti použití:
1. **Gemini 2.0 Flash:** Univerzální model pro multimodální úlohy s vysokou rychlostí a širokou podporou funkcí.
2. **Gemini 2.0 Flash-Lite:** Ideální pro aplikace s omezeným rozpočtem nebo tam, kde je prioritou rychlost.
3. **Gemini 2.0 Pro Experimental:** Nejlepší volba pro složité úlohy vyžadující dlouhé kontexty a přesnost.
4. **Gemini 2.0 Flash Thinking Experimental:** Vhodný pro analytické úkoly, kde je důležitá transparentnost myšlenkového procesu.
5. **Gemini 2.0 Flash Experimental:** Experimentální model pro testování nových funkcí.
6. **LearnLM 1.5 Pro Experimental:** Specializovaný model pro vzdělávací aplikace.

Každý model má unikátní zaměření, což umožňuje jejich využití v různých scénářích od rychlých aplikací po komplexní analýzy nebo vzdělávací projekty.

Zdroje
- [Gemini models - Gemini API - Google AI for Developers](https://ai.google.dev/gemini-api/docs/models/gemini)
- [Gemini 2.0 Flash Thinking Mode - Gemini API - Google AI for Developers](https://ai.google.dev/gemini-api/docs/thinking-mode)
- [Google Gemini 2.0 explained: Everything you need to know](https://www.techtarget.com/whatis/feature/Google-Gemini-20-explained-Everything-you-need-to-know)
- [Google Gemini: Everything you need to know about the generative AI models - TechCrunch](https://techcrunch.com/2024/09/10/what-is-google-gemini-ai/)

## Ponaučení

Ve skutečnosti, pokud budete něco vyvíjet, doporučuji nejdříve ve webovém rozhraní odladit prompt na konkrétní model. Nejprve si napište prompt, pak jej vyzkoušejte na jednotlivé modely ve webovém rozhraní a zjistěte, který vám vyhovuje nejlépe. Pak přizpůsobujte prompt tak, abyste dosáhli přesně toho výstupu, jaký potřebujete.