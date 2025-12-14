---
author: Marisa Aigen
category: ai
companies:
- Thinking Machines Lab Inc
- OpenAI Group PBC
date: '2025-12-12 23:51:26'
description: Společnost Thinking Machines Lab Inc. dnes uvedla svou službu Tinker
  pro doladění umělé inteligence do obecné dostupnosti. Firmu se sídlem v San Franciscu
  založila v únoru Mira Murati, bývalá šéftechnoložka OpenAI, která dohlížela na vývoj
  ChatGPT a Sora.
importance: 4
layout: tech_news_article
original_title: Thinking Machines makes its Tinker AI fine-tuning service generally
  available
people:
- Mira Murati
publishedAt: '2025-12-12T23:51:26+00:00'
slug: thinking-machines-makes-its-tinker-ai-fine-tuning-
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: Thinking Machines zpřístupňuje službu Tinker pro doladění umělé inteligence
  pro širokou veřejnost
url: https://siliconangle.com/2025/12/12/thinking-machines-makes-tinker-ai-fine-tuning-service-generally-available/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/Mira-Murati.png
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2025/12/Mira-Murati.png
---

## Souhrn
Společnost Thinking Machines Lab Inc. zpřístupnila svou cloudovou službu Tinker pro doladění velkých jazykových modelů (LLM) pro širokou veřejnost. Služba využívá metodu Low-Rank Adaptation (LoRA), která výrazně snižuje nároky na výpočetní zdroje oproti tradičnímu doladění. Firma, založená Mirou Murati z OpenAI, získala v červnu seed kolo ve výši 2 miliard dolarů při valuaci 10 miliard dolarů.

## Klíčové body
- Thinking Machines založila v únoru 2025 Mira Murati, ex-šéftechnoložka OpenAI zodpovědná za ChatGPT a Sora; tým zahrnuje Soumitha Chintalu, spolustvořitele PyTorch z Meta.
- Služba Tinker debutovala před čtyřmi měsíci a nyní je ve fázi general availability.
- Používá LoRA pro efektivní doladění LLM, což umožňuje přizpůsobení modelů specifickým úkolům s minimálními zdroji.
- Financování: 2 miliardy dolarů od investorů včetně Nvidia, AMD a ServiceNow.
- LoRA přidává malý počet parametrů k původnímu modelu a trénuje jen ty, což urychluje proces a snižuje náklady na infrastrukturu.

## Podrobnosti
Thinking Machines Lab Inc. je startup zaměřený na vývoj nástrojů pro umělou inteligenci, který vstoupil na trh s cloudovou službou Tinker určenou k doladění velkých jazykových modelů. Doladění znamená úpravu předtrénovaného LLM tak, aby lépe plnil konkrétní úkoly, například pochopení preferencí zákazníků v systému doporučení produktů nebo analýzu specializovaných textů v medicíně. Tradiční metody doladění aktualizují všechny parametry modelu – tedy nastavení určující zpracování dat – což vyžaduje obrovské množství GPU a dlouhou dobu tréninku.

Tinker naopak aplikuje LoRA, metodu vyvinutou v roce 2021 výzkumníky z Microsoftu. LoRA rozšiřuje LLM o malý počet dodatečných parametrů, typicky v řádu milionů oproti bilionům v původním modelu, a trénink probíhá pouze na těchto nových parametrech. To snižuje spotřebu výpočetního výkonu na zlomek oproti plnému doladění, zjednodušuje nasazení modelu a umožňuje rychlejší iterace. Například firma vyvíjející chatbota pro zákaznickou podporu může pomocí Tinkeru přizpůsobit model Llama nebo podobný za hodiny místo dnů, bez potřeby vlastního klastru GPU.

Zakladatelkou je Mira Murati, která v OpenAI řídila vývoj klíčových produktů jako ChatGPT a generativní video Sora. Tým posílil Soumith Chintala, jeden ze spolustvořitelů knihovny PyTorch, kterou Meta opustil minulý měsíc. Finanční zázemí je impozantní: v červnu 2025 získali 2 miliardy dolarů v seed kole při valuaci 10 miliard, s podporou od Nvidia (dodavatel GPU), AMD (konkurent v čipech) a ServiceNow (platforma pro automatizaci). Tinker byl představen čtyři měsíce po financování a nyní přechází z beta do plné dostupnosti, což znamená, že ji mohou využívat všichni uživatelé bez omezení.

LoRA není bez kompromisů: modely doladěné touto metodou mohou dosahovat mírně nižší přesnosti na složitých úkolech oproti plnému tréninku, protože nemění jádro modelu. Přesto je metoda široce přijímaná v průmyslu díky své efektivitě, jak ukazují implementace v Hugging Face nebo open-source projektech.

## Proč je to důležité
Toto spuštění posiluje konkurenci v oblasti fine-tuningu LLM, kde dominují služby jako OpenAI fine-tuning API nebo Google Vertex AI. Tinker s LoRA democratizuje přístup k custom modelům pro menší firmy a vývojáře, kteří nemohou investovat do vlastní infrastruktury. S pozadím Murati a Chintaly se Thinking Machines stává potenciálním hráčem schopným ovlivnit ekosystém AI, podobně jako Anthropic nebo xAI. Velké financování signalizuje důvěru investorů v efektivní metody jako LoRA, které řeší klíčový problém škálovatelnosti AI v éře rostoucích modelů. Pro průmysl to znamená nižší vstupní bariéry pro aplikace jako personalizované AI asistenty nebo specializované analyzátory, což urychlí adopci LLM mimo velké technologické giganty.

---

[Číst původní článek](https://siliconangle.com/2025/12/12/thinking-machines-makes-tinker-ai-fine-tuning-service-generally-available/)

**Zdroj:** 📰 SiliconANGLE News
