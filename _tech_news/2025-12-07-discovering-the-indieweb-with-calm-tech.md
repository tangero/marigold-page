---
author: Marisa Aigen
category: indieweb
date: '2025-12-07 03:26:01'
description: Článek popisuje problémy současných sociálních sítí a představuje browserová
  rozšíření StreetPass pro Mastodon a Blog Quest pro RSS kanály, která objevují nezávislé
  profily a zdroje bez rušivých upozornění. Tyto nástroje podporují principy klidné
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
Článek kritizuje současné sociální sítě za jejich rušivost a dopaminovou závislost a navrhuje alternativu v podobě Indiewebu. Představuje browserové rozšíření StreetPass for Mastodon, které automaticky objevuje Mastodon profily na osobních webech, a autorovo vlastní rozšíření Blog Quest pro hledání RSS a Atom kanálů. Oba nástroje fungují na principu klidné technologie, která neodvádí pozornost uživatele notifikacemi.

## Klíčové body
- StreetPass for Mastodon objevuje ověřovací odkazy na Mastodon z webů a sbírá profily do seznamu bez upozornění.
- Blog Quest hledá RSS a Atom kanály pomocí rel="alternate" odkazů a umožňuje pozdější prohlížení sbírky.
- Oba nástroje jsou open source a dostupné pro Firefox, Chrome a Safari.
- Princip klidné technologie upřednostňuje pozadovou práci před okamžitými výzvami k akci.
- Podporují Indieweb, decentralizovanou alternativu k centrálním sociálním sítím.

## Podrobnosti
Sociální sítě jako Facebook původně slibovaly propojení, ale dnes jsou charakterizovány neustálými notifikacemi, nekonečným posunem obsahu a reklamami, které vyvolávají dopaminovou reakci. Autor čláčku na blogu alexsci.com popisuje tento posun jako invazi „monstrů“, která ohrožuje mentální zdraví. Řešením je návrat k Indiewebu – konceptu, kde jednotlivci spravují vlastní weby a propojují se decentralizovaně, například přes Mastodon nebo RSS kanály.

Před několika týdny autor narazil na rozšíření StreetPass for Mastodon, vytvořené vývojářem tvler. Toto rozšíření prohlíží stránky a automaticky detekuje ověřovací odkazy na Mastodon profily (typicky ve formě rel="me"), které blogeři a majitelé osobních stránek na nich uvádějí. Namísto vyskočení notifikace se profily tiše přidávají do interního seznamu. Uživatel si je může prohlédnout, když chce, a následovat je na Mastodonu – federovaném protokolu sociální sítě, který je open source a decentralizovaný, na rozdíl od proprietárních platforem jako X nebo Facebook. StreetPass tak obohacuje prohlížení webu bez rušení, což je příkladem klidné technologie podle principů Marka Weisers z Xerox PARC: technologie by měla být na pozadí, ne v popředí.

Inspirován tím vytvořil autor Blog Quest, rozšíření pro objevování blogů. Při prohlížení webu hledá standardní auto-discovery odkazy RSS nebo Atom (pomocí HTML atributu rel="alternate" s typem application/rss+xml nebo application/atom+xml). Tyto kanály sbírá do sbírky, kterou uživatel otevře v pohodě. Blog Quest umožňuje snadné přihlašování do čteček jako Feedly nebo Inoreader, čímž podporuje syndikaci obsahu bez nutnosti sledovat centrální platformy. Oba nástroje jsou open source, zdarma ke stažení z prohlížečových obchodů a fungují na principu webových standardů, které jsou podporovány od 90. let. Například RSS byl vyvinut Netscape v roce 1999 a Atom v roce 2003 jako jeho nástupce.

## Proč je to důležité
Tyto nástroje posilují Indieweb ekosystém, který bojuje proti centralizaci dat u velkých firem. V době, kdy sociální sítě experimentují s AI algoritmy pro maximalizaci času stráveného (engagement), klidná technologie nabízí udržitelnější přístup: uživatel si udržuje kontrolu nad daty a pozorností. Pro vývojáře a blogery to znamená lepší viditelnost bez placené propagace. V širším kontextu IT podporují open standardy jako ActivityPub (pro Mastodon) a RSS, což snižuje závislost na proprietárních API. Článek má zatím nízkou popularitu na Hacker News (5 bodů, 0 komentářů), ale ilustruje trend decentralizace webu, podobně jako Microsub protokoly nebo WebSub pro real-time RSS. Pro uživatele to znamená méně stresu z notifikací a více autentického propojení.

---

[Číst původní článek](https://alexsci.com/blog/calm-tech-discover/)

**Zdroj:** 📰 Alexsci.com
