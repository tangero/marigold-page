---
author: Patrick Zandl
categories:
- Patrickův newsletter
- Apple
- Google
- AI
- Internet
- EU
- Automotive
date: '2024-02-20'
layout: post
original_newsletter: "Patrickův newsletter #73: \U0001F973 Před branami všeobecné
  umělé inteligence...?"
summary_points:
- OpenAI představila Sora, AI nástroj generující minutová, hyperrealistická videa
  z textu.
- Sora využívá difuzní transformátor, inspirovaný LLM, pro zpracování a komprimaci
  videodat.
- Tréninková data Sory a technické detaily zůstávají nejasné, což vyvolává otázky.
- Sora má potenciál ovlivnit filmový průmysl a vytvořit nové trhy.
title: OpenAI Sora je nový model, který převádí text na video
---

Minulý týden se pokusil Google ohromit celý svět novým posunem stran umělé inteligence nazvaným Gemini 1.5. Jenže společnost OpenAI byla nachystána a aby přerazila jakýkoliv dojem, že existuje ještě někdo jiný, kdo by svět umělé inteligence posouval, okamžitě uvolnila informace o novém AI nástroji nazvaném Sora, který umí převádět textové zadání do videa. Překotnost uvolnění informace je viditelná na první pohled. Je patrné, že OpenAI měla všechny tiskové informace připravené předem, presskity odladěné, ale samotný model Sora pro veřejnost neuvolnila, vydala z něj jen výstupy. Pravděpodobně jde o nějaký druh PR zápolení s Googlem, protože naprosto stejně (řekneme si později) postupoval i Google: informace vydal, model neuvolnil. 

Co je Sora? Velký jazykový model, který umí z textového zadání vytvořit hyperrealistická, až minutová videa. Videa jsou opravdu perfektní, alespoň ta uvolněná. Ale podrobností o tom, jak se k nim nástroj společnosti OpenAI dohrabal, je pramálo ([techspec je maximálně vágní)](https://openai.com/research/video-generation-models-as-world-simulators). Což dost handikapuje oznámení. Tak především se vlastně neví, odkud se vzala tréninková data - tedy jaká videa OpenAI více či méně vykradla. 

Srdcem systému Sora je difuzní transformátor, vizionářský model inspirovaný velkými jazykovými modely (LLM), který je určen ke zpracování vizuálních dat. Jedná se o komprimaci videodat do časoprostorových políček, podobných tokenům, kterým rozumí LLM, které jsou poté vycvičeny a znovu sestaveny do nových videosekvencí s vysokým rozlišením. Tento inovativní přístup nejen zjednodušuje složitý svět video dat, ale také se přizpůsobuje možnostem zpracování transformátorů, což znamená významný skok od manuální přesnosti Unreal Engine k intuitivním, daty řízeným poznatkům systému Sora. 

[![](https://substack-post-media.s3.amazonaws.com/public/images/ef4bf00b-caff-46e4-82c8-a46b77d5d8a5.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef4bf00b-caff-46e4-82c8-a46b77d5d8a5.heic)Krajinka s příbojem vygenerovaná Sorou. V 4K rozlišení fakt slušný… 

![](https://substack-post-media.s3.amazonaws.com/public/images/ef4bf00b-caff-46e4-82c8-a46b77d5d8a5.heic)

A o čem se v souvislosti s modelem Sora debatuje v USA? Jak dopadne tento nástroj na filmový průmysl. Podle mě zatím nijak zásadně a naopak vytvoří nový trh, potenciál má ale ničivý.

Vyzkoušet to zatím nemůžete, ale [nějaká vzorová videa jsou tady](https://openai.com/sora)...

Mimochodem, když jsme u těch videí, k čemu se to dá použít? Služba Neiro umožní vytvořit váš vlastní avatar a pak jej nechat odvyprávět text dodaný přes webové rozhraní či API. Já jsem použil předpřipraveného avatara, nechal jej načíst začátek dalšího odstavce a obrazově jsem to umístil do galerie Villa Pellé, kde [probíhá výstava obrazů Adolfa Lachmana Lachland](https://villapelle.cz/lachland-svet-posapokalyptickeho-romantika-adolfa-lachmana/), kterou mimochodem doporučuji navštívit. [Video zde.](https://share.neiro.ai/x9spk3eU)

* * *