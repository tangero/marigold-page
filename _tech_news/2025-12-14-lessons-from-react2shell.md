---
author: Marisa Aigen
category: programování
date: '2025-12-14 06:26:30'
description: Kritická zranitelnost CVE-2025-55182 v Reactu umožnila neověřeným útočníkům
  spouštět libovolný kód na milionech serverů běžících React 19 a Next.js. Prohlášená
  3. prosince 2025 s maximálním skóre CVSS 10.0, byla rychle zneužita v praxi.
importance: 5
layout: tech_news_article
original_title: Lessons from React2Shell
publishedAt: '2025-12-14T06:26:30+00:00'
slug: lessons-from-react2shell
source:
  emoji: 📰
  id: null
  name: Dev.to
title: Lekce z React2Shell
url: https://dev.to/cheetah100/lessons-from-react2shell-1m8b
urlToImage: https://media2.dev.to/dynamic/image/width=1000,height=500,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyesjwmk56jzyxm2bamh3.png
urlToImageBackup: https://media2.dev.to/dynamic/image/width=1000,height=500,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fyesjwmk56jzyxm2bamh3.png
---

## Souhrn
3. prosince 2025 zveřejnila společnost React CVE-2025-55182, kritickou zranitelnost umožňující vzdálené spouštění kódu bez ověření s maximálním skóre CVSS 10.0. Během hodin ji útočníci zneužívali v reálném prostředí na téměř milion serverů s React 19 a Next.js. Tato chyba v protokolu Flight, součásti React Server Components, představuje největší bezpečnostní selhání frameworku po 13 letech bez významných incidentů.

## Klíčové body
- Zranitelnost v protokolu Flight umožnila deserializaci škodlivých dat z klienta, což vedlo k provedení libovolného kódu na serveru.
- Postihla servery s React Server Components bez nutnosti ověření, stačilo odeslat upravený HTTP požadavek.
- Kořen problému spočíval v nedostatečné ochraně proti neověřeným datům z klienta, včetně přístupu k vlastnostem jako .then nebo .constructor.
- React měl dříve čistý bezpečnostní záznam, pouze jedna menší XSS chyba v roce 2018 s CVSS 6.1.
- Rychlé zneužití zdůraznilo rizika nových serializačních formátů v serverových architekturách.

## Podrobnosti
React Server Components (RSC) představují zásadní změnu v architektuře Reactu. Dříve sloužil React primárně jako knihovna pro klientskou stranu, kde se v prohlížeči vykreslovaly uživatelské rozhraní a komunikovalo se s backendem přes standardní REST nebo GraphQL API. Backend mohl být napsán v jakémkoli jazyce, například Pythonu, Go nebo Javě, podle potřeb projektu. RSC toto mění tím, že umožňují spouštět React komponenty přímo na serveru. Tyto komponenty tak mají přímý přístup k databázím, souborovým systémům nebo jiným serverovým zdrojům bez nutnosti zprostředkovatele. Data a kontext se přenáší mezi klientem a serverem pomocí vlastního serializačního formátu nazvaného Flight.

Zranitelnost CVE-2025-55182 pramení právě z tohoto protokolu. Server přijímal serializovaná data od klienta, deserializoval je a na jejich základě spouštěl kód. Útočníci dokázali vytvořit škodlivá data, která po deserializaci umožnila přístup k JavaScriptovým primitivům pro spouštění kódu, jako jsou metody .then() nebo .constructor. Tento problém nastal proto, že React se spoléhal na bezpečnost samotného formátu Flight, místo aby všechna data z klienta považoval za neověřená a aplikoval striktní validaci. Stačilo mít síťový přístup k endpointu Server Components a odeslat upravený HTTP požadavek – žádné ověření uživatele nebylo potřeba.

Next.js, populární framework pro React založený na Node.js, tento model dále rozšiřuje. Umožňuje vývojářům budovat serverless aplikace nebo plnohodnotné serverové renderování, kde se komponenty vykreslují na serveru a posílají se klientovi jako HTML nebo JSON. Miliony serverů tak bylo vystaveno riziku, protože mnoho projektů přešlo na RSC pro lepší výkon a menší velikost balíčků na klientovi. React tým rychle vydal záplaty, ale škody byly již způsobeny – útočníci získali shell přístup (odtud název React2Shell) a mohli instalovat malware nebo krást data.

## Proč je to důležité
Tato krize ukazuje rizika spojená s přechodem na serverové komponenty v populárních frameworkech. React, používaný v milionech aplikací včetně těch od Facebooku (nyní Meta), Google nebo Netflixu, teď čelí důvěře v nové architektury. Vývojáři musí přehodnotit předpoklady o bezpečnosti serializace a vždy validovat vstupy z klienta. V širším kontextu to zdůrazňuje, jak rychlý vývoj nových funkcí jako RSC může vést k zero-day exploitům s maximálním dopadem. Průmysl by měl posílit audity deserializace, podobně jako u historických problémů v Java RMI nebo PHP unserialize(). Pro uživatele to znamená okamžité aktualizace a monitorování logů, protože exploit umožňoval trvalý přístup k serverům. Tento incident může zpomalit adopci RSC a donutit k přepracování bezpečnostních modelů v ekosystému JavaScriptu.

---

[Číst původní článek](https://dev.to/cheetah100/lessons-from-react2shell-1m8b)

**Zdroj:** 📰 Dev.to
