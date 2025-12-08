---
author: Marisa Aigen
category: indieweb
date: '2025-12-07 03:26:01'
description: Článek rozebírá problémy současných sociálních sítí a představuje browserová
  rozšíření StreetPass pro Mastodon a Blog Quest pro RSS kanály, která objevují obsah
  tiše na pozadí bez rušivých upozornění. Tyto nástroje podporují principy klidné
  technologie a Indiewebu.
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
Článek popisuje, jak sociální sítě zpočátku slibovaly propojení, ale dnes představují rušivý faktor s neustálými notifikacemi a algoritmy zaměřenými na maximalizaci času uživatelů. Autor ukotvuje řešení v klidné technologii prostřednictvím browserového rozšíření StreetPass, které automaticky sbírá odkazy na profily Mastodonu z webů, a svého vlastního projektu Blog Quest pro objevování RSS a Atom kanálů. Tyto nástroje fungují na pozadí, aniž by odváděly pozornost.

## Klíčové body
- StreetPass od tvler objevuje Mastodon profily pomocí ověřovacích odkazů (rel="me") na blozích a osobních webech.
- Blog Quest, vytvořené autorem, detekuje RSS a Atom kanály přes rel="alternate" odkazy a sbírá je tiše.
- Oba nástroje jsou open source a dostupné pro Firefox, Chrome a Safari.
- Princip klidné technologie znamená žádné okamžité notifikace, uživatel interaguje v svém tempu.
- Cílem je podpora Indiewebu jako alternativy k centralizovaným sociálním sítím.

## Podrobnosti
Sociální sítě jako Facebook zpočátku umožnily bezprecedentní propojení, zejména mezi studenty, ale postupně se proměnily v systémy závislé na algoritmech, které generují dopaminové smyčky prostřednictvím nekonečného scrollování a notifikací. Tyto platformy maximalizují interakci na úkor duševního zdraví uživatelů, což vede k únavě a závislosti. Indieweb představuje hnutí zaměřené na decentralizovaný web, kde jednotlivci vlastní svůj obsah na osobních webech a propojují se přes standardy jako RSS, Atom nebo fediverse protokoly.

StreetPass, vytvořené vývojářem tvler, řeší problém objevování lidí na Mastodonu, což je decentralizovaná sociální síť založená na fediverse protokolu ActivityPub. Rozšíření prochází stránky, které navštěvujete, a hledá ověřovací odkazy rel="me", které webmastrech přidávají do HTML hlavičky pro propojení s jejich Mastodon profilem. Namísto vyskočení notifikace se profily tiše ukládají do seznamu, který si můžete prohlédnout později. To respektuje principy klidné technologie, poprvé definované Markem Weiserem v 90. letech u Xerox PARC – technologie by měla být periferní, ne centrální v pozornosti uživatele.

Inspirován tímto přístupem vytvořil autor Blog Quest, rozšíření prohlížeče, které na každé stránce hledá auto-objevitelné RSS nebo Atom kanály prostřednictvím rel="alternate" odkazů v HTML. Tyto standardy umožňují webům deklarovat své syndikační kanály bez složitých manuálních hledání. Opět bez rušení sbírá seznam feedů, které lze pak otevřít v čtečce jako je například FreshRSS nebo Inoreader. Blog Quest tak usnadňuje přechod od centralizovaných platforem k soběstačným blogům, kde autoři kontrolují svůj obsah a čtenáři ho následují přes syndikaci. Oba projekty jsou open source, což znamená, že kód je veřejně dostupný na GitHubu, umožňuje příspěvky komunity a snadnou instalaci z oficiálních obchodů rozšíření prohlížečů.

## Proč je to důležité
V éře rostoucího znechucení z centralizovaných sociálních sítí, které ovládají obsah algoritmy a reklamy, nabízejí nástroje jako StreetPass a Blog Quest praktickou cestu k Indiewebu. Podporují decentralizaci dat, kde uživatelé nejsou uzamknuti v jedné platformě, a snižují závislost na notifikačních systémech, což přispívá k lepšímu duševnímu zdraví. Pro vývojáře a uživatele IT to znamená snadnější adopci standardů webu, jako je Webmention nebo Micropub, které umožňují interakci mezi weby bez prostředníků. V širším kontextu posilují odolnost webu vůči monopolům a podporují dlouhodobou udržitelnost obsahu, protože RSS feeds přežívají i po změnách platforem. I když nejde o masový produkt, představují krok k uživatelsky přívětivějšímu webu.

---

[Číst původní článek](https://alexsci.com/blog/calm-tech-discover/)

**Zdroj:** 📰 Alexsci.com
