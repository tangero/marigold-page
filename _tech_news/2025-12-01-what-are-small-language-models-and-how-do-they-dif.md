---
author: Marisa Aigen
category: jazykové modely
date: '2025-12-01 19:04:10'
description: Malé jazykové modely fungují jako specializované nástroje v nářadí, na
  rozdíl od velkých modelů typu ChatGPT, které přinášejí celou dílnu možností.
importance: 3
layout: tech_news_article
original_title: What are small language models and how do they differ from large ones?
publishedAt: '2025-12-01T19:04:10+00:00'
slug: what-are-small-language-models-and-how-do-they-dif
source:
  emoji: 📰
  id: null
  name: The Conversation Africa
title: Co jsou malé jazykové modely a jak se liší od velkých?
url: https://theconversation.com/what-are-small-language-models-and-how-do-they-differ-from-large-ones-269103
urlToImage: https://images.theconversation.com/files/705449/original/file-20251130-56-srf3mb.jpg?ixlib=rb-4.1.0&rect=1560%2C1335%2C2144%2C1072&q=45&auto=format&w=1356&h=668&fit=crop
urlToImageBackup: https://images.theconversation.com/files/705449/original/file-20251130-56-srf3mb.jpg?ixlib=rb-4.1.0&rect=1560%2C1335%2C2144%2C1072&q=45&auto=format&w=1356&h=668&fit=crop
---

## Souhrn
Microsoft nedávno vydal nový malý jazykový model, který běží přímo na uživatelském počítači bez potřeby cloudových služeb. Tento článek vysvětluje, co jsou malé jazykové modely (SLM), jak se liší od velkých jazykových modelů (LLM) jako ChatGPT nebo Gemini, a proč nabývají na významu v praxi. Autoři z University of Technology Sydney zdůrazňují rozdíly v rozsahu, schopnostech a nárocích na zdroje.

## Klíčové body
- Malé jazykové modely mají méně parametrů (typicky desítky až stovky milionů) než velké modely (miliardy až biliony parametrů), což umožňuje jejich provoz na běžném hardware.
- SLM jsou optimalizovány pro specifické úkoly, jako je překlad, sumarizace nebo lokální zpracování textu, zatímco LLM zvládají širokou škálu úkolů včetně kreativního psaní.
- Hlavní výhody SLM: nižší spotřeba energie, rychlejší odezva a možnost offline provozu, například na mobilních zařízeních nebo edge zařízeních.
- Příklady: Microsoft Phi-3 (nový model běžící na PC), Google Gemma nebo Mistral 7B.
- Autoři Lin Tian a Marian-Andrei Rizoiu z University of Technology Sydney poukazují na rostoucí roli SLM v profesionálním prostředí.

## Podrobnosti
Jazykové modely jsou systémy strojového učení trénované na obrovských objemech textových dat, které rozpoznávají vzory a generují odpovědi na otázky, překládají jazyky nebo vytvářejí obsah. Rozdíl mezi SLM a LLM spočívá především v velikosti a architektuře. Velké modely jako GPT-4 od OpenAI nebo Claude od Anthropic mají stovky miliard parametrů, což vyžaduje výkonné GPU clustery a cloudovou infrastrukturu. Tyto modely excelují v komplexních úkolech, jako je analýza dlouhých textů, logické uvažování nebo generování kódu, ale jsou náročné na zdroje – trénink jednoho LLM může spotřebovat energii odpovídající spotřebě stovek domácností.

Naopak malé jazykové modely, jako nedávno vydaný Microsoft Phi-3 s 3,8 miliardami parametrů, jsou navrženy pro efektivitu. Běží na standardním procesoru v notebooku nebo smartphonu, bez nutnosti připojení k internetu. Phi-3 slouží k rychlému zpracování textu, jako je sumarizace dokumentů, automatické odpovědi v aplikacích nebo on-device překlady. Další příklady zahrnují model Gemma od Google (2 miliardy parametrů), který je určen pro vývojáře k integraci do mobilních aplikací, nebo Llama 3 8B od Meta, optimalizovaný pro lokální nasazení.

Autoři článku, Lin Tian (výzkumník v Data Science Institute) a Marian-Andrei Rizoiu (profesor behavioral data science a ředitel Defence Innovation Network), mají zkušenosti s financováním z australských obranných programů, jako je Advanced Strategic Capabilities Accelerator. Jejich analýza ukazuje, že SLM dosahují srovnatelné přesnosti v úzkých doménách díky lepšímu tréninku na kvalitních datech, nikoli kvantitě. Například Phi-3 překonává starší LLM v benchmarkách na matematické úlohy díky destilaci znalostí z větších modelů. Pro uživatele to znamená soukromí – data nezanechávají cloud – a rychlost, ideální pro profesionály v medicíně (diagnostické pomůcky) nebo průmyslu (prediktivní údržba).

## Proč je to důležité
Růst SLM reaguje na limity LLM: vysoké náklady (např. inference GPT-4 stojí centy za požadavek) a závislost na cloudu, což brání široké adopci v edge computingu. V širším ekosystému AI umožňují SLM decentralizaci – od IoT zařízení po autonomní drony – a snižují uhlíkovou stopu AI. Pro průmysl to otevírá dveře k hybridním systémům: LLM pro složité úkoly, SLM pro rutinu. Kriticky řečeno, SLM zatím nedosahují univerzálnosti LLM a mohou selhat v kreativních nebo kontextově bohatých scénářích, ale jejich pokrok (jako Phi-3 dosahující 80 % výkonu GPT-4 při 1 % nákladů) signalizuje posun k praktickému AI. V kontextu evropských regulací (AI Act) podporují SLM bezpečnější, transparentnější nasazení bez rizik velkých modelů.

---

[Číst původní článek](https://theconversation.com/what-are-small-language-models-and-how-do-they-differ-from-large-ones-269103)

**Zdroj:** 📰 The Conversation Africa
