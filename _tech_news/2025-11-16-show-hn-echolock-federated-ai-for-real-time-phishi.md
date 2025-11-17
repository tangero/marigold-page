---
author: Marisa Aigen
category: kybernetická bezpečn
date: '2025-11-16 13:26:24'
description: Echolock je open-source systém pro kolektivní detekci phishingových útoků
  založený na federované architektuře a hybridním přístupu kombinujícím statické seznamy,
  bloklisty a AI analýzu.
importance: 3
layout: tech_news_article
original_title: 'Show HN: Echolock – Federated AI for real-time phishing detection'
publishedAt: '2025-11-16T13:26:24+00:00'
slug: show-hn-echolock-federated-ai-for-real-time-phishi
source:
  emoji: 📰
  id: null
  name: Github.com
title: Echolock – Federovaná AI pro detekci phishingu v reálném čase
url: https://github.com/ojayballer/ECHOLOCK
urlToImage: https://opengraph.githubassets.com/8a445ec4b870deed9b8f9aa48719e60b3c670e13dc777022367fcbe8d11fe241/ojayballer/ECHOLOCK
urlToImageBackup: https://opengraph.githubassets.com/8a445ec4b870deed9b8f9aa48719e60b3c670e13dc777022367fcbe8d11fe241/ojayballer/ECHOLOCK
---

## Souhrn
Echolock je open-source nástroj pro kybernetickou obranu, který využívá federovanou AI k detekci phishingových útoků v reálném čase. Na rozdíl od tradičních izolovaných systémů sdílí jednotlivé uzly hrozby okamžitě po celé síti, čímž zkracuje reakční dobu na nové útoky z hodin či dní na sekundy.

## Klíčové body
- Federovaná architektura umožňuje okamžité sdílení indikátorů kompromitace (IOC) mezi všemi uzly sítě.
- Hybridní systém kombinuje statické allow/block seznamy, federované bloklisty a plnou AI analýzu.
- Detekční přesnost dosahuje 91 % při nízké paměťové náročnosti (45 MB).
- Vývoj proběhl v rámci Cyber AI Hackathonu 2025.
- Sdílení hrozeb probíhá přes Redis server s latencí pod 5 sekund.

## Podrobnosti
Echolock řeší zásadní nedostatek současných systémů pro detekci phishingu: jejich izolovanost. Když jedna organizace identifikuje novou hrozbu, tradiční nástroje tuto informaci nešíří, což umožňuje útočníkům opakovat stejný útok na jiné cíle. Echolock tento problém řeší federovanou sítí, kde každý uzel, který detekuje novou hrozbu s vysokou důvěryhodností, okamžitě publikuje její „otisk“ (IOC) na centrální server postavený na Redisu. Ostatní uzly tuto informaci přijímají během milisekund a mohou tak blokovat stejný útok, i když se s ním ještě nesetkaly.

Systém pracuje ve více vrstvách: nejrychlejší je validace pomocí statických seznamů (pod 50 ms), následuje federovaná bloklist vrstva (do 200 ms) a až nakonec plná AI analýza trvající 2–4 sekundy. Tento přístup umožňuje vyvážit rychlost a přesnost. Aplikace je navržena jako lehká (45 MB RAM) a přístupná přes jednoduché webové rozhraní pro zadávání URL a zobrazení výsledků včetně skóre důvěryhodnosti.

## Proč je to důležité
Echolock představuje praktickou implementaci federovaného modelu v kybernetické bezpečnosti, což je oblast s rostoucím významem v éře sofistikovaných a rychle se šířících útoků. I když se jedná o hackathonový projekt, jeho architektura ukazuje cestu, jak mohou organizace efektivně sdílet hrozby bez nutnosti centralizovaného řízení nebo odhalení citlivých dat. Takový přístup může výrazně zvýšit kolektivní odolnost proti phishingu, zejména pro menší subjekty, které nemají vlastní týmy threat intelligence. Projekt je open-source a dostupný na GitHubu, což umožňuje komunitě přispívat k jeho vývoji a integraci do existujících bezpečnostních řešení.

---

[Číst původní článek](https://github.com/ojayballer/ECHOLOCK)

**Zdroj:** 📰 Github.com
