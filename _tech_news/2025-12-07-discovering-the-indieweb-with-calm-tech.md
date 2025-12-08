---
author: Marisa Aigen
category: indieweb
date: '2025-12-07 03:26:01'
description: Článek popisuje problémy sociálních sítí jako rušivé notifikace a nekonečné
  scrollování, a představuje browserová rozšíření StreetPass pro objevování Mastodon
  profilů a Blog Quest pro RSS feedy, obě postavená na principu klidné technologie,
  která neodvádí pozornost uživatele.
importance: 3
layout: tech_news_article
original_title: Discovering the Indieweb with Calm Tech
publishedAt: '2025-12-07T03:26:01+00:00'
slug: discovering-the-indieweb-with-calm-tech
source:
  emoji: 📰
  id: null
  name: Alexsci.com
title: Objevování Indiewebu s klidnou technologií
url: https://alexsci.com/blog/calm-tech-discover/
---

## Souhrn
Článek analyzuje, jak sociální sítě z původního nástroje pro spojení lidí přerostly v rušivé platformy závislé na reklamách a dopaminových impulsech. Autor představuje rozšíření prohlížeče StreetPass, které tiše sbírá Mastodon profily z webů, a svůj vlastní projekt Blog Quest pro automatické objevování RSS a Atom feedů. Oba nástroje uplatňují princip klidné technologie, který umožňuje uživateli zůstat soustředěným na aktuální činnost.

## Klíčové body
- StreetPass automaticky detekuje Mastodon verifikační odkazy na blozích a osobních webech a sbírá je do seznamu bez notifikací.
- Funguje na Firefoxu, Chromu a Safari jako open source rozšíření od tvůrce tvler.
- Blog Quest rozšiřuje tento koncept na RSS a Atom feedy prostřednictvím rel="alternate" odkazů v HTML.
- Oba projekty minimalizují rušení a podporují Indieweb, decentralizovanou alternativu k centrálním sociálním sítím.
- Uživatel si obsah prohlédne v pohodlném čase, což zvyšuje uživatelskou autonomii.

## Podrobnosti
Sociální sítě jako Facebook původně sloužily k propojení lidí, například vysokoškoláků, ale dnes generují nekonečné notifikace, které odvádějí pozornost a podporují závislost na scrollování. Autor je přirovnává k sirénám, které lákají na dopaminové odměny uprostřed reklam. Řešením je návrat k Indiewebu, kde uživatelé kontrolují svůj obsah na vlastních webech.

Před několika týdny autor objevil StreetPass for Mastodon, rozšíření prohlížeče vytvořené tvlerem. Toto rozšíření prochází stránky, které uživatel navštěvuje, a hledá verifikační odkazy na Mastodon profily – Mastodon je decentralizovaná sociální síť podobná Twitteru, ale bez centrálního vlastníka. Když najde takový odkaz, StreetPass ho tiše přidá do interního seznamu, aniž by zobrazil popup nebo notifikaci. Uživatel tak může pokračovat v čtení blogu nebo webu bez přerušení. Seznam se projeví až při aktivním otevření rozšíření, což umožňuje následovat nové účty na vlastní půdě. StreetPass je open source, což znamená, že zdrojový kód je veřejně dostupný na GitHubu, a lze ho snadno upravit nebo rozšířit.

Inspirován tímto přístupem vytvořil autor Blog Quest, další browserové rozšíření. Blog Quest kontroluje každou načtenou stránku na přítomnost auto-objevitelného RSS nebo Atom feedu pomocí standardního HTML atributu rel="alternate" v odkazech. Tyto formáty slouží k syndikaci obsahu – RSS (Really Simple Syndication) umožňuje odběr aktualizací z blogů přes čtečky jako Feedly nebo Inoreader, Atom je podobný standard s lepší podporou Unicode. Rozšíření feedy sbírá na pozadí a uživatel si je může prohlédnout nebo přihlásit k odběru, kdy chce. Tento princip klidné technologie, poprvé definovaný v 90. letech Markem Weiserem z Xerox PARC, zdůrazňuje, že technologie by měla být periferií, ne centrem pozornosti – měnit se podle kontextu bez nutnosti aktivní interakce.

Oba nástroje jsou dostupné pro hlavní prohlížeče: Firefox, Chrome (včetně Chromium-based jako Edge) a Safari. Instalace probíhá přes oficiální obchody rozšíření, kde lze ověřit recenze a oprávnění.

## Proč je to důležité
V éře, kdy sociální sítě ovládají 70 % digitální komunikace, podporují tyto nástroje Indieweb – hnutí pro vlastnictví vlastního obsahu prostřednictvím standardů jako Webmention, Micropub nebo ActivityPub (základ Mastodonu). To snižuje závislost na algoritmech velkých platforem, které upřednostňují virální obsah před kvalitou. Pro uživatele znamená větší soukromí a méně stresu z notifikací; pro vývojáře inspiraci k nenásilným rozhraním. V širším kontextu IT posiluje decentralizaci, podobně jako blockchain v financích, a může ovlivnit budoucí design aplikací, kde se klidná technologie stane standardem proti vyhoření z digitálního přetížení. Celkově přispívá k udržitelnějšímu webu, kde technologie slouží člověku, ne naopak.

---

[Číst původní článek](https://alexsci.com/blog/calm-tech-discover/)

**Zdroj:** 📰 Alexsci.com
