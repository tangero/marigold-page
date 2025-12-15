---
author: Marisa Aigen
category: programování
date: '2025-12-14 06:26:30'
description: Analýza kritické bezpečnostní zranitelnosti CVE-2025-55182 v Reactu,
  která umožnila neautentizované spuštění libovolného kódu na milionech serverů během
  hodin po zveřejnění. Článek rozebírá příčiny v protokolu Flight a dopady na ekosystém
  React Server Components.
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
3. prosince 2025 oznámil React CVE-2025-55182, kritickou zranitelnost umožňující vzdálené spuštění kódu s maximálním skóre CVSS 10.0. Během několika hodin po zveřejnění ji útočníci exploitovali v reálném prostředí na téměř milion serverů s React 19 a Next.js. Tato chyba v protokolu Flight React Server Components představuje největší bezpečnostní selhání frameworku po 13 letech bez závažných incidentů.

## Klíčové body
- Zranitelnost v protokolu Flight umožňuje deserializaci neověřených dat z klienta, což vede k spuštění libovolného kódu na serveru bez autentizace.
- Postihuje React 19 a aplikace na Next.js; útok stačí odeslat HTTP požadavek na endpoint serverových komponent.
- Kořen problému spočívá v nebezpečné deserializaci objektů, které umožňují přístup k JavaScriptovým primitivům jako .then nebo .constructor.
- React předpokládal bezpečnost formátu serializace, místo aby považoval veškerá data z klienta za nedůvěryhodná.
- Exploit byl okamžitě ve volné přírodě, což ohrozilo širokou škálu webových aplikací.

## Podrobnosti
React Server Components (RSC) představují zásadní změnu architektury Reactu. Dříve sloužil React primárně jako knihovna pro vykreslování uživatelského rozhraní v prohlížeči, kde komunikoval s backendem přes standardní REST nebo GraphQL API. Backend mohl být napsán v libovolném jazyce, jako Python, Go nebo Java. RSC umožňují spouštět React komponenty přímo na serveru, kde mají přímý přístup k databázím a dalším zdrojům, což snižuje množství přenášených dat a zlepšuje výkon.

Protokol Flight je vlastní formát serializace pro přenos dat a kontextu provedení mezi klientem a serverem v rámci RSC. Server přijímá serializovaná data od klienta, deserializuje je a na jejich základě spouští kód. Zranitelnost spočívá v nebezpečné deserializaci: server neověřoval data z klienta a umožňoval přístup k vlastnostem objektů, jako .then (sloužící k řízení asynchronních operací) nebo .constructor (umožňující vytváření instancí tříd). Útočník tak mohl vytvořit škodlivý payload, který po deserializaci na serveru spustí libovolný JavaScript kód.

Útok nevyžaduje autentizaci ani speciální oprávnění – stačí síťový přístup k endpointu serverových komponent. React dosud měl vynikající bezpečnostní historii: za 13 let pouze jedna menší XSS zranitelnost s CVSS 6.1 v roce 2018. Tato chyba však ukazuje slabiny nové architektury RSC, kde se klient a server prolínají více než dříve. Next.js, populární framework pro React aplikace, integruje RSC a byl silně postižen, což ovlivnilo tisíce produkčních nasazení.

Vývojáři museli okamžitě aktualizovat na patchy, ale mnoho systémů zůstalo vystavených kvůli automatickému nasazení a závislostem. Tento incident odhaluje rizika přechodu k serverově vykreslovaným komponentám, kde se tradiční principy jako "nikdy nedůvěřuj datům z klienta" oslabily.

## Proč je to důležité
Tato zranitelnost má široké dopady na webový vývoj: React pohání miliony aplikací a Next.js je standardem pro server-side rendering. Exploit na milionech serverů mohl vést k masivním únikům dat, ransomware nebo úplnému ovládnutí infrastruktury. V širším kontextu zdůrazňuje nutnost robustní validace v hybridních architekturách, kde se klient-server hranice stírá. Lekce pro průmysl zahrnují: vždy validovat vstupy, oddělovat serializaci od provedení kódu a testovat proti deserializačním útokům. Pro uživatele znamená riziko kompromitace webů od velkých firem po startupy, což urychlí adopci bezpečnostních nástrojů jako Snyk nebo Dependabot. Incident může zpomalit přechod na RSC a donutit React tým přepracovat bezpečnostní model Flightu.

---

[Číst původní článek](https://dev.to/cheetah100/lessons-from-react2shell-1m8b)

**Zdroj:** 📰 Dev.to
