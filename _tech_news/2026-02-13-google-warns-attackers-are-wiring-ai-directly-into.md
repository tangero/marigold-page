---
author: Marisa Aigen
category: tech
companies:
- Google
date: '2026-02-13 00:00:48'
description: Nová zpráva Google Threat Intelligence Group upozorňuje, že kyberzločinci
  překračují fázi experimentálního zneužívání umělé inteligence a začínají ji integrovat
  přímo do svých operačních postupů při útocích. Zpráva se zaměřuje na zneužití modelů
  Gemini, včetně dynamického generování kódu malware a pokusů o extrakci modelů.
importance: 5
layout: tech_news_article
original_title: Google warns attackers are wiring AI directly into live cyberattacks
publishedAt: '2026-02-13T00:00:48+00:00'
slug: google-warns-attackers-are-wiring-ai-directly-into
source:
  emoji: 📰
  id: null
  name: SiliconANGLE News
title: 'Google varuje: Útočníci připojují AI přímo k probíhajícím kyberútokům'
url: https://siliconangle.com/2026/02/12/google-warns-attackers-wiring-ai-directly-live-cyberattacks/
urlToImage: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2026/02/aihacking.png
urlToImageBackup: https://d15shllkswkct0.cloudfront.net/wp-content/blogs.dir/1/files/2026/02/aihacking.png
---

## Souhrn
Google Threat Intelligence Group v nové zprávě varuje, že kyberzločinci přestávají s povrchním testováním umělé inteligence a začleňují ji přímo do aktivních útoků. Pozorováno bylo zneužití modelů Gemini, kde malware během provádění volatí API pro generování kódu, což komplikuje tradiční detekční mechanismy. Google zároveň odhalil pokusy o extrakci vnitřní logiky těchto modelů.

## Klíčové body
- Malware rodiny, jako HONESTCUE, dynamicky žádají o generování C# kódu z modelu Gemini prostřednictvím API volání během útoku.
- Útočníci provádějí model extraction (distillation attacks) velkým objemem strukturovaných dotazů, aby napodobily proprietární modely bez vlastního vývoje.
- Google identifikoval a zablokoval kampaně s vysokou aktivitou promptů zaměřenou na extrakci znalostí z Gemini.
- Tato taktika posouvá logiku útoku mimo statický binární kód, což ztěžuje detekci na základě signatur nebo chování.
- Zpráva zdůrazňuje testování a zneužívání generativních AI systémů v reálných útocích.

## Podrobnosti
Zpráva Google Threat Intelligence Group, aktualizovaná 12. února 2026, popisuje přechod kyberzločinců od sporadického experimentování s AI k jejímu plnohodnotnému nasazení v útočných řetězcích. Konkrétně se zaměřuje na zneužití Google svých vlastních modelů Gemini, které slouží k generování textu, kódu a dalších výstupů na základě přirozeného jazyka. Výzkumníci Google pozorovali malware, který během svého provádění přímo volatí API Gemini pro získání zdrojového kódu potřebného k dokončení úkolu. Například rodina malware HONESTCUE používá pečlivě navržené prompty k vygenerování C# kódu, který se následně spustí jako součást útoku. Tento přístup umožňuje útočníkům udržovat malware binární soubor minimální a flexibilní – logika útoku není pevně zakódována, ale generována na požádání, což výrazně ztěžuje detekci na základě statických signatur nebo předem definovaných chování.

Dalším významným prvkem jsou distillation attacks, známé také jako model extraction. Útočníci vysílají modelům jako Gemini tisíce strukturovaných dotazů, aby na základě odpovědí odvodili vnitřní chování, vzorce reakcí a logiku. Cílem je vytvořit levnější napodobeniny proprietárních modelů bez nutnosti investovat do tréninku od nuly, což by vyžadovalo obrovské výpočetní zdroje a data. Google tyto pokusy detekoval díky vysokému objemu API požadavků a následně kampaně disruptoval blokováním přístupu. Tato taktika není nová teoreticky, ale její aplikace na živé modely jako Gemini ukazuje na zralost útočníků v manipulaci s generativní AI. Zpráva také naznačuje pozorování státních aktérů, i když detaily nejsou plně specifikovány.

## Proč je to důležité
Tento vývoj označuje zásadní posun v kyberbezpečnosti: tradiční antivirové systémy založené na signaturách selžou proti dynamicky generovanému kódu, což nutí průmysl k adopci pokročilejších metod, jako je behaviorální analýza v runtime nebo monitorování API volání. Pro uživatele to znamená vyšší riziko sofistikovanějších útoků, kde AI urychluje exploitaci zranitelností nebo generování phishingu. V širším kontextu AI ekosystému to podtrhuje nutnost robustních ochran u cloudových modelů – rate limiting, watermarking výstupů a detekce anomálních promptů. Google svým reportem nejen upozorňuje, ale i demonstruje své schopnosti v detekci, což posiluje důvěru v jejich modely, avšak zároveň odhaluje, jak rychle se hrozby adaptují na nové technologie. Pokud se toto rozšíří, může to vést k eskalaci závodů ve výzbroji mezi obránci a útočníky, kde AI bude klíčovým faktorem na obou stranách.

---

[Číst původní článek](https://siliconangle.com/2026/02/12/google-warns-attackers-wiring-ai-directly-live-cyberattacks/)

**Zdroj:** 📰 SiliconANGLE News
