---
author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- AI
- Sociální sítě
- Internet
- Automotive
date: '2024-07-28'
layout: post
original_newsletter: '#80: Kyberkatastrofa Crowdstrike'
summary_points:
- OpenAI GPT-4o mini je o 60 % levnější než GPT-3,5 Turbo.
- Meta vydala Llama 3.1, open-source model s kontextem 128k a 405 miliardami parametrů.
- Mistral Large 2, model s 123B parametry, konkuruje Llama 3.1 v generování kódu a
  matematice.
- Mistral dosahuje s menšími modely srovnatelných výsledků jako Llama, což snižuje
  provozní náklady.
title: "\U0001F916 Nové představené LLM modely - hustý týden"
---

**OpenAI představilo lehčí verzi 4o ([oznam zde](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/))**. GPT-4o mini je o 60 % levnější než GPT-3,5 Turbo. Slušný!

Cena modelu je 0,15 USD za milion vstupních tokenů a 0,60 USD za milion výstupních tokenů (~2500 stran knihy). Pro srovnání, GPT-3.5-turbo-0301 stál před zhruba více než rokem 2,00 USD za 1 milion tokenů.

Zatím to vypadá, že model je dobrý ve strukturování informací i porozumění dlouhému kontextu.

**Meta záhy poté právě vydala Llama 3.1** , svůj dosud největší open-source model umělé inteligence, a tvrdí, že v testech překonává GPT-4o i Claude 3.5 Sonnet.

Délka kontextu 128k, umí chatovat v osmi jazycích, psát lepší počítačový kód a řešit složitější matematické úlohy. Má 405 miliard parametrů trénována na 16 000 GPU H100 od Nvidia.

Jen open source, lze vyzkoušet [na Hugging Face](https://huggingface.co/chat/models/meta-llama/Meta-Llama-3.1-405B-Instruct-FP8) přes web. Omylem jsem si ho pustil na svém iMacu, kde mám jen 8 GB RAM a bylo vidět hned, co moderní AI na lokále potřebuje: mraky paměti ...

A do třetice - hned po oznámení Mety se přihlásil i francouzský Mistral se svým open source LLM modelem, když **vydal Mistral Large 2** , novou verzi největšího modelu firmy. Mistral Large 2 je model s parametry 123B s kontextovým oknem 128k. V mnoha benchmarcích (zejména v generování kódu a matematice) je podle tvrzení Mistralu lepší nebo na stejné úrovni jako Llama 3.1 405B. Stejně jako Mistral NeMo byl trénován na velkém množství zdrojového kódu a vícejazyčných dat. Firemní oznámení [je zde](https://mistral.ai/news/mistral-large-2407/).

Co je na tom podstatné? Zdá se, že Mistral s menšími modely dosahuje velmi podobných výsledků, jako Llama, což otevírá dveře lepší ekonomice provozu. Na grafu je vidět, jak si jednotlivé modely stojí proti testu MMLU a jak open source modely stahují ztrátu za modely uzavřeného kódu:

[![](https://substack-post-media.s3.amazonaws.com/public/images/88b9029b-539e-46f5-a1b4-d92c96f5055f_1600x1102.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88b9029b-539e-46f5-a1b4-d92c96f5055f_1600x1102.heic)

![](https://substack-post-media.s3.amazonaws.com/public/images/88b9029b-539e-46f5-a1b4-d92c96f5055f_1600x1102.heic)

* * *