---
category: kybernetická bezpečn
companies:
- Google
- Memento Labs
- Hacking Team
date: '2025-10-27 16:37:28'
description: Zranitelnost zero-day v prohlížeči Chrome, využitá při kampani ForumTroll,
  šířila malware od italské firmy Memento Labs, která vznikla z nechvalně známého
  Hacking Teamu.
importance: 4
layout: tech_news_article
original_title: Italian spyware vendor linked to Chrome zero-day attacks - BleepingComputer
publishedAt: '2025-10-27T16:37:28+00:00'
slug: italian-spyware-vendor-linked-to-chrome-zero-day-a
source:
  emoji: 📰
  id: null
  name: BleepingComputer
title: Italský výrobce špionážního softwaru stojí za útoky využívajícími zranitelnost
  v Chrome
url: https://www.bleepingcomputer.com/news/security/italian-spyware-vendor-linked-to-chrome-zero-day-attacks/
urlToImage: https://www.bleepstatic.com/content/hl-images/2023/11/28/Google_Chrome.jpg
urlToImageBackup: https://www.bleepstatic.com/content/hl-images/2023/11/28/Google_Chrome.jpg
---

## Souhrn

Bezpečnostní výzkumníci z Kaspersky odhalili spojení mezi útoky využívajícími zranitelnost zero-day v prohlížeči Chrome a italským výrobcem špionážního softwaru Memento Labs. Firma vznikla po akvizici kontroverzního Hacking Teamu společností InTheCyber Group a její malware s kódovým označením "Dante" byl aktivní minimálně od roku 2022.

## Klíčové body

- Kampaň ForumTroll zneužila zranitelnost CVE-2025-2783 v Chrome k útokům na ruské organizace včetně médií, univerzit a vládních institucí
- Malware Dante vyvinula firma Memento Labs, nástupce Hacking Teamu, který byl v roce 2015 kompromitován a odhalen jako dodavatel špionážního softwaru autoritářským režimům
- Útoky probíhaly prostřednictvím podvodných e-mailových pozvánek na konferenci Primakov Readings s maliciózními odkazy
- Pouhé načtení odkazu v jakémkoli prohlížeči založeném na Chromium stačilo k infikování systému
- Analýza odhalila další útoky na organizace v Rusku a Bělorusku sahající až do roku 2022

## Podrobnosti

Operace ForumTroll, kterou Kaspersky poprvé odhalil v březnu 2025, představovala sofistikovanou kybernetickou kampaň zaměřenou na ruské instituce. Útočníci využili pečlivě připravené e-maily vydávající se za pozvánky na prestižní mezinárodní fórum Primakov Readings. Tyto zprávy obsahovaly škodlivé odkazy, které po otevření v prohlížeči automaticky spustily infekční řetězec.

Klíčovým prvkem útoků byla zranitelnost CVE-2025-2783, umožňující útěk z bezpečnostního sandboxu prohlížeče Chrome. Tato zero-day zranitelnost, tedy bezpečnostní chyba neznámá v době zneužití, poskytla útočníkům možnost obejít ochranné mechanismy prohlížeče a nainstalovat malware přímo do systému oběti.

Při hlubší analýze starších útoků výzkumníci identifikovali dosud neznámý komerční špionážní software nazvaný Dante. Stopa vedla k italské firmě Memento Labs, která vznikla v roce 2019 po akvizici nechvalně známého Hacking Teamu společností InTheCyber Group. Hacking Team byl milánský výrobce špionážního softwaru Remote Control System (RCS), který prodával své nástroje vládním agenturám jako sledovací technologii.

Osud Hacking Teamu byl zpečetěn v roce 2015, kdy firma sama padla za oběť kybernetického útoku. Únik dat odhalil prodeje autoritářským režimům, přístup k zero-day zranitelnostem a spolupráci s vládními zpravodajskými službami. InTheCyber Group následně využil výzkum a know-how Hacking Teamu k vytvoření Memento Labs, která pokračuje v tradici vývoje komerčního špionážního softwaru.

## Proč je to důležité

Odhalení spojení mezi zero-day zranitelnostmi v široce používaném prohlížeči Chrome a komerčním špionážním softwarem ukazuje na rostoucí sofistikovanost kybernetických útoků sponzorovaných státy nebo prováděných s využitím komerčních nástrojů. Existence firem jako Memento Labs, které staví na základech kontroverzních předchůdců, poukazuje na problematický trh se špionážními technologiemi.

Případ také demonstruje, jak mohou být zero-day zranitelnosti v běžném softwaru zneužity k rozsáhlým špionážním kampaním. Skutečnost, že pouhé kliknutí na odkaz v e-mailu stačilo k infikování systému, zdůrazňuje důležitost pravidelných aktualizací prohlížečů a opatrnosti při otevírání odkazů i od zdánlivě důvěryhodných odesílatelů. Pro organizace v citlivých sektorech to znamená nutnost implementace vícevrstvé bezpečnosti a školení zaměstnanců v rozpoznávání phishingových útoků.

---

[Číst původní článek](https://www.bleepingcomputer.com/news/security/italian-spyware-vendor-linked-to-chrome-zero-day-attacks/)

**Zdroj:** 📰 BleepingComputer
