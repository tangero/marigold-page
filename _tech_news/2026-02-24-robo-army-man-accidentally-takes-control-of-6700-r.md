---
author: Marisa Aigen
category: kyberbezpečnost
date: '2026-02-24 16:56:57'
description: Strateg na umělou inteligenci náhodně získal přístup k více než 6700
  internetově propojeným robotickým vysavačům DJI Romo při pokusu o propojení svého
  zařízení s ovladačem PlayStation. Tento incident odhalil závažnou bezpečnostní zranitelnost,
  která umožnila přístup k půdorysům domů, živým kamerovým záběrům a mikrofonům.
importance: 5
layout: tech_news_article
original_title: 'Robo Army: Man Accidentally Takes Control of 6,700+ Robot Vacuums
  Worldwide While Hacking His Own'
publishedAt: '2026-02-24T16:56:57+00:00'
slug: robo-army-man-accidentally-takes-control-of-6700-r
source:
  emoji: 📰
  id: breitbart-news
  name: Breitbart News
title: 'Robo armáda: Muž náhodně ovládl přes 6700 robotických vysavačů po celém světě
  při úpravě svého vlastního'
url: https://www.breitbart.com/tech/2026/02/24/robo-army-man-accidentally-takes-control-of-6700-robot-vacuums-worldwide-while-hacking-his-own/
urlToImage: https://media.breitbart.com/media/2026/02/DJI-Romo-robot-vacuum-640x335.jpg
urlToImageBackup: https://media.breitbart.com/media/2026/02/DJI-Romo-robot-vacuum-640x335.jpg
---

## Souhrn
Strateg na umělou inteligenci Sammy Adoufal náhodně získal neoprávněný přístup k přibližně 6700 robotickým vysavačům DJI Romo rozloženým po celém světě, když se snažil upravit komunikaci svého vlastního zařízení pro ovládání PlayStation ovladačem. Tento objev odhalil kritickou bezpečnostní chybu umožňující přístup k citlivým datům jako jsou detailní půdorysy, živé video z kamer a audio z mikrofonů. Adoufal incident zodpovědně nahlásil výrobci DJI, který vydal opravné aktualizace.

## Klíčové body
- Adoufal použil nástroj Claude Code k reverznímu inženýrství komunikačního protokolu mezi vysavačem DJI Romo a servery, což vedlo k získání soukromého tokenu umožňujícího přístup k 6700 zařízením v USA, Evropě a Číně.
- Zranitelnost umožnila vzdálené ovládání vysavačů, přístup k mapám prostoru, živým kamerám a mikrofonům, což představuje riziko pro soukromí uživatelů.
- Spekulace o možném backdooru vloženém čínskou firmou DJI pro špionážní účely; Adoufal popírá tradiční hackování a zdůrazňuje, že jen extrahoval token ze svého zařízení.
- DJI reagovalo rychle aktualizacemi řešícími primární problém bez nutnosti akce od uživatelů.
- Incident se týká modelů DJI Romo, levných robotických vysavačů vyrobených čínskou firmou známou především drony.

## Podrobnosti
Sammy Adoufal, specialist na strategii umělé inteligence, se rozhodl upravit svůj robotický vysavač DJI Romo tak, aby ho lze ovládat herním ovladačem PlayStation. DJI Romo je levný model robotického vysavače s kamerou, mikrofonem a schopností mapování prostoru, který se propojuje s cloudovými servery pro aktualizace a ovládání přes mobilní aplikaci. Adoufal využil AI nástroj Claude Code od Anthropic k analýze komunikačního protokolu mezi zařízením a servery. Během tohoto procesu extrahoval soukromý autentizační token ze svého vysavače, který neočekávaně fungoval i na tisících jiných zařízeních.

Tento token umožnil přístup k živým datům z 6700 vysavačů napojených na servery v USA, Evropě a Číně. Mezi získané informace patřily detailní 3D mapy domácností vytvářené LiDAR senzory vysavačů, živé video z vestavěných kamer sloužících k navigaci a detekci překážek, stejně jako audio nahrávky z mikrofonů určených pro hlasové příkazy. Adoufal zdůraznil, že nedošlo k porušení bezpečnostních mechanismů jako brute force útok nebo crackování – stačilo použít legitimní token. Bezpečnostní výzkumníci spekulují, že chyba souvisí s backdoorem, který čínská firma DJI mohla implementovat pro vzdálenou diagnostiku nebo horší, špionáž. DJI, globální leader v dronech a teď i spotřební robotice, incident potvrdilo a vydalo několik aktualizací firmware, které zablokovaly sdílení tokenů a zlepšily autentizaci. Uživatelé nemuseli nic dělat, protože aktualizace proběhly automaticky přes cloud. Tento případ ilustruje typické slabiny IoT zařízení: slabou segmentaci přístupu na serverech a nedostatečnou ochranu autentizačních dat, což je běžné u čínských výrobců kvůli nižším bezpečnostním standardům.

## Proč je to důležité
Tento incident odhaluje systémové rizika v IoT ekosystému robotických zařízení, kde levné spotřební produkty sbírají citlivá data o domácnostech bez adekvátní ochrany. Pro uživatele to znamená potenciální únik půdorysů, které lze použít pro plánování krádeží nebo špionáže, a živé přístup k interiérům. V širším kontextu posiluje obavy z čínských technologií, kde backdoory mohou sloužit státnímu dohledu, podobně jako u Huawei zařízení. Pro průmysl to podtrhuje nutnost bug bounty programů a zero-trust architektury v cloudu. Jako expert na robotiku vidím zde varování pro autonomní systémy: bez robustní bezpečnosti hrozí masové kompromitace, což brzdí adopci v domácnostech i průmyslu. Celkový rozsah – 6700 zařízení – ukazuje, jak rychle se zranitelnosti šíří globálně.

---

[Číst původní článek](https://www.breitbart.com/tech/2026/02/24/robo-army-man-accidentally-takes-control-of-6700-robot-vacuums-worldwide-while-hacking-his-own/)

**Zdroj:** 📰 Breitbart News
