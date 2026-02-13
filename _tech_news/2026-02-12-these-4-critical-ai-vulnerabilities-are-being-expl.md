---
author: Marisa Aigen
category: ai bezpečnost
date: '2026-02-12 16:26:56'
description: Od útoků typu prompt injection po podvody s deepfakes bezpečnostní výzkumníci
  uvádějí, že několik chyb nemá známou opravu. Zde je přehled těchto problémů.
importance: 5
layout: tech_news_article
original_title: These 4 critical AI vulnerabilities are being exploited faster than
  defenders can respond
publishedAt: '2026-02-12T16:26:56+00:00'
slug: these-4-critical-ai-vulnerabilities-are-being-expl
source:
  emoji: 📰
  id: null
  name: ZDNet
title: Tyto 4 kritické zranitelnosti AI jsou zneužívány rychleji, než obránci stihnou
  reagovat
url: https://www.zdnet.com/article/ai-security-threats-2026-overview/
urlToImage: https://www.zdnet.com/a/img/resize/32db0bda826046b0d2703b9713fd04f9739cf838/2026/02/10/bfe5dd37-f08f-4991-8009-84b7c6022267/gettyimages-1346242220.jpg?auto=webp&fit=crop&height=675&width=1200
urlToImageBackup: https://www.zdnet.com/a/img/resize/32db0bda826046b0d2703b9713fd04f9739cf838/2026/02/10/bfe5dd37-f08f-4991-8009-84b7c6022267/gettyimages-1346242220.jpg?auto=webp&fit=crop&height=675&width=1200
---

## Souhrn
Čtyři hlavní zranitelnosti v systémech umělé inteligence jsou aktivně zneužívány útočníky, zatímco bezpečnostní týmy nemají k dispozici účinné opravy. Mezi nimi patří útoky na autonomní AI agenty, otrava tréninkových dat, prompt injection a deepfake podvody. Bezpečnostní výzkumníci varují, že rychlost vývoje AI překonává možnosti obrany.

## Klíčové body
- Autonomní AI agenti jsou hijackováni státem sponzorovanými hackery, například čínskými aktéry na nástroji Claude Code od Anthropic.
- Otrava tréninkových dat vyžaduje jen 250 dokumentů a 60 dolarů.
- Útoky prompt injection úspěšně prolomí 56 procent velkých jazykových modelů (LLM).
- Repozitáře modelů obsahují stovky tisíc škodlivých souborů.
- Deepfake videohovory vedly k odcizení desítek milionů dolarů.

## Podrobnosti
Článek zdůrazňuje, že systémy umělé inteligence čelí současným útokům na více frontách, přičemž většina zranitelností postrádá známé řešení. První z nich se týká autonomních systémů: v září Anthropic odhalil, že čínští hackeři sponzorovaní státem zneužili nástroj Claude Code – což je AI nástroj pro generování a úpravu kódu – k provádění kybernetických útoků. Tito autonomní AI agenti, navržení pro samostatné plnění úkolů jako programování nebo analýza dat, se stávají ideálními zbraněmi, protože útočníci je mohou přesměrovat na škodlivé aktivity bez dalšího zásahu.

Druhá zranitelnost spočívá v otravě tréninkových dat (data poisoning), kde stačí infikovat jen 250 dokumentů za cenu 60 dolarů, aby byl model natrvalo narušen. Tento útok mění chování modelu ještě před nasazením, což ovlivňuje výstupy v produkčním prostředí, například v systémech pro detekci podvodů nebo medicínskou diagnostiku.

Třetí problém je prompt injection, technika, při které útočník vloží škodlivý příkaz do vstupního textu, aby přepsal instrukce modelu. Podle výzkumu uspěje u 56 procent testovaných LLM, jako jsou GPT nebo Claude varianty. To umožňuje únik citlivých dat nebo provedení neoprávněných akcí, což ohrožuje chatbota v podnikových aplikacích.

Čtvrtá hrozba pochází z repozitářů modelů, jako je Hugging Face, kde se skrývají stovky tisíc škodlivých souborů. Tyto modely, určené pro sdílení a fine-tuning, mohou obsahovat backdoory, které se aktivují po stažení. K tomu se přidávají deepfake videohovory, které už vedly k ukradení desítek milionů dolarů prostřednictvím falešných jednání s manažery.

Tyto exploity využívají přesně ty vlastnosti, které AI činí užitečnou – autonomii, rychlost učení a generování obsahu. Bezpečnostní týmy tak stojí před dilematem: buď se vyhnout AI a ztratit konkurenční výhodu, nebo nasadit systémy s inherentními slabostmi.

## Proč je to důležité
Tyto zranitelnosti ukazují systémové selhání v AI ekosystému, kde rychlost inovací předbíhá bezpečnostní vývoj. Pro firmy znamená riziko finančních ztrát, úniků dat a reputačních škod, zejména v oblastech jako finance nebo zdravotnictví. V širším kontextu posilují argumenty pro regulaci AI, jako je nadcházející EU AI Act, a nutnost investic do robustních obranných mechanismů, jako adversarial training nebo sandboxing. Bez rychlých opatření se AI stane větší hrozbou než přínosem, což ovlivní celý technologický průmysl.

---

[Číst původní článek](https://www.zdnet.com/article/ai-security-threats-2026-overview/)

**Zdroj:** 📰 ZDNet
