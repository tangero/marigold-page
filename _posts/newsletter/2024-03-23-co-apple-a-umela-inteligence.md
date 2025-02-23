---
author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- Google
- AI
- Internet
- Automotive
date: '2024-03-23'
layout: post
original_newsletter: '#74: Apple vyměnilo auta za AI'
summary_points:
- Apple ukončil vývoj automobilu a přesunul tým do vývoje AI.
- MM1, nový multimodální AI model od Apple, vyniká schopností zpracovávat různé formáty
  dat.
- Apple jedná s Google o využití modelu Gemini v zařízeních Apple, například v iOS
  18.
- iOS 18 integruje AI do Siri, Apple Music, Pages, Xcode, Spotlight, Health a Zpráv.
title: "\U0001F34E Co Apple a umělá inteligence?"
---

Společnost Apple provedla v poslední době několik zajímavých a pro budoucnost důležitých obratů, u kterých stojí za to se zastavit. Tak především zřejmě poslala k vodě projekt automobilu. Spálila na něm miliardu dolarů, zlanařila spoustu lidí a stejně to nevedlo k ničemu, co by firmu uspokojilo. Lidi z projektu autonomního vozu přesunula do AI. 

V průběhu března [představilo Apple](https://arxiv.org/pdf/2403.09611.pdf?utm_source=aisecret.us&utm_medium=Patrick_Zandl) svůj **nový AI model jednoduše nazvaný MM1**. To je model, který drží prst na tepu doby a v něčem ji i posouvá dále. Je multimodální, tj. umožňuje různé vstupy a výstupy, jak textové, tak obrazové. Používá Mixture of Experts MoE, tedy zkoumání kontextu. Líbí se mi to na následujícím příkladě, kde uživatel vyfotil stůl v restauraci, jídelní lístek a zeptal se, kolik bude účet. MM1 správně odpověděla. 

[![](https://substack-post-media.s3.amazonaws.com/public/images/2a09b784-a897-423a-a3a8-dd24079fadd1.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a09b784-a897-423a-a3a8-dd24079fadd1.heic)

![](https://substack-post-media.s3.amazonaws.com/public/images/2a09b784-a897-423a-a3a8-dd24079fadd1.heic)

To také znamená, že počty natrénovaných parametrů nejsou všechno. Ostatně, v parametrech MM1 nevyniká. GPT-4 má bilion parametrů, Claude 3 Opus 2 biliony. Oproti tomu MM1 od společnosti Apple s 30 miliardami parametrů bledne. I starší GPT-3 mělo 175 miliard parametrů!

V současné době přední modely umělé inteligence vydané OpenAI a Anthropic neobsahují možnosti generování videa. Naproti tomu MM1 vyniká schopností trénovat různé formáty, včetně obrázků, videa, zvuku a textových dat. Vize společnosti Apple je tedy dosti odvážná a zjevně stojí právě na té multimodalitě. 

**Tahle zpráva je důležitá ze dvou pohledů.** Za prvé Apple přichází sice se zpožděním, ale také s novými přístupy a otevřeností vůči ostatním, protože své postupy hned publikuje. A za druhé, jeho vlastní LLM zřejmě není připraveno pro světla ramp. A s tím také koreluje pár dní stará zpráva, podle které Apple vyjednává se společností Google o tom, že by prozatím ve svých zařízeních používala jeho model Gemini podobně, jako například používala jeho mapy nebo vyhledávání. Apple by tak mohlo přijít na trh s dobrou AI již v další verzi iOS 18, což se po pravdě řečeno hodně čeká a bylo by zklamáním, kdyby to nebylo. Pro Apple by bylo podstatné představit LLM model fungující v zařízení, tedy bez toho, aby probíhala komunikace se serverem přes internet. Což Gemini Nano zvládá. [Přehled Gemini modelů najdete zde](https://medium.com/@raghuveer.awankar/google-gemini-a-new-horizon-in-multimodal-language-models-19b6aa666b17). 

Jak to změní rozložení sil v LLM se ještě uvidí. Bude záležet na tom, kolik úsilí do LLM Apple vrhne, například vytvoření jeho vlastních map trvalo Apple pět let. Jenže v LLM společnost usnout chtít nebude. Alespoň to tak vypadá. 

### Jak to bude s AI v iOS18?

Zde jsou [některé zvěsti o](https://9to5mac.com/2023/10/22/apple-ai-features-ios-18-iphone-siri/) nových funkcích umělé inteligence v systému iOS 18:

  * [Nová verze](https://9to5mac.com/2024/01/24/next-generation-siri-ios-18/) Siri, která je inteligentnější a založená na technologii LLM, podobně jako platformy ChatGPT a Gemini společnosti Google - ale s plynulým napojením na hlasový vstup a výstup. 

  * Nové funkce umělé inteligence pro Apple Music, které uživatelům umožňují automaticky vytvářet seznamy skladeb.

  * Integrace umělé inteligence do aplikací Pages, Keynote a Numbers pro shrnutí, tvorbu obsahu a další funkce.

  * [Funkce AI pro Xcode,](https://9to5mac.com/2024/02/15/apple-ai-xcode-features/) které umí doplňovat bloky kódu, pomáhají testovat aplikace a další.

  * [Vylepšená verze vyhledávání Spotlight](https://9to5mac.com/2024/02/15/apple-llm-ai-spotlight-upgrade-ios/), která je poháněna generativní AI a dokáže provádět složitější úlohy.

  * [Funkce wellness koučinku poháněná AI](https://9to5mac.com/2023/04/25/ipad-health-app-wellness-coaching-more/), která je integrovaná do Apple Health a Apple Watch.

  * Nové funkce AI pro aplikaci Zprávy, které umí automaticky doplňovat zprávy, odpovídat na otázky a shrnovat příchozí textové zprávy, navíc propojená se Siri, takže když Siri přikážete, aby se zeptala mámy, zda nepotřebuje s něčím pomoci, Siri odešle kvalitně natextovanou zprávu v tónu, jakým s mámou mluvíte. 




[Nová verze](https://9to5mac.com/2024/01/24/next-generation-siri-ios-18/) Siri, která je inteligentnější a založená na technologii LLM, podobně jako platformy ChatGPT a Gemini společnosti Google - ale s plynulým napojením na hlasový vstup a výstup. 

Nové funkce umělé inteligence pro Apple Music, které uživatelům umožňují automaticky vytvářet seznamy skladeb.

Integrace umělé inteligence do aplikací Pages, Keynote a Numbers pro shrnutí, tvorbu obsahu a další funkce.

[Funkce AI pro Xcode,](https://9to5mac.com/2024/02/15/apple-ai-xcode-features/) které umí doplňovat bloky kódu, pomáhají testovat aplikace a další.

[Vylepšená verze vyhledávání Spotlight](https://9to5mac.com/2024/02/15/apple-llm-ai-spotlight-upgrade-ios/), která je poháněna generativní AI a dokáže provádět složitější úlohy.

[Funkce wellness koučinku poháněná AI](https://9to5mac.com/2023/04/25/ipad-health-app-wellness-coaching-more/), která je integrovaná do Apple Health a Apple Watch.

Nové funkce AI pro aplikaci Zprávy, které umí automaticky doplňovat zprávy, odpovídat na otázky a shrnovat příchozí textové zprávy, navíc propojená se Siri, takže když Siri přikážete, aby se zeptala mámy, zda nepotřebuje s něčím pomoci, Siri odešle kvalitně natextovanou zprávu v tónu, jakým s mámou mluvíte. 

* * *