---
author: Marisa Aigen
category: ai
companies:
- OpenAI
date: '2025-11-02 22:49:40'
description: Agentic režim prohlížeče Atlas od OpenAI se aktivně vyhýbá webům médií,
  která žalují OpenAI, přestože technicky může tyto stránky navštívit.
importance: 3
layout: tech_news_article
original_title: ChatGPT's Browser Bot Seems to Avoid New York Times Links Like a Rat
  Who Got Electrocuted - Gizmodo
publishedAt: '2025-11-02T22:49:40+00:00'
slug: chatgpts-browser-bot-seems-to-avoid-new-york-times
source:
  emoji: 📰
  id: null
  name: Gizmodo.com
title: Prohlížecí bot ChatGPT se vyhýbá odkazům na New York Times jako potkán po elektrošoku
url: https://gizmodo.com/chatgpts-browser-bot-seems-to-avoid-new-york-times-links-like-a-rat-who-got-electrocuted-2000680444
urlToImage: https://gizmodo.com/app/uploads/2025/11/rat-maze-1200x675.jpg
urlToImageBackup: https://gizmodo.com/app/uploads/2025/11/rat-maze-1200x675.jpg
---

## Souhrn

Novinářské vyšetřování odhalilo, že prohlížeč Atlas od OpenAI se v agentic režimu systematicky vyhýbá webům médií, která vedou proti společnosti soudní spory. Zatímco běžné web crawlery respektují technická omezení, agentic režim může tato omezení obejít tím, že se tváří jako běžný uživatel, ale přesto se některým zdrojům aktivně vyhýbá.

## Klíčové points

- Atlas v agentic režimu se vyhýbá webům médií žalujících OpenAI, včetně New York Times
- Agentic prohlížeče se v logách serverů jeví jako běžné Chrome relace, mohou tedy obcházet blokování crawlerů
- Běžné web crawlery respektují robots.txt a další omezení, agentic režimy fungují pod záminkou běžného uživatele
- Vyšetřování provedli novináři z Columbia Journalism Review
- Chování bota naznačuje, že OpenAI programově vyhýbá svůj nástroj potenciálně problematickým zdrojům

## Podrobnosti

Prohlížeče s umělou inteligencí jako ChatGPT Atlas nejsou jen běžné prohlížeče s chatovacím oknem. Disponují takzvanými agentic schopnostmi, což znamená, že mohou teoreticky provádět úkoly jako nákup letenek nebo rezervace hotelů. Podle vyšetřování novinářů Aisvarya Chandrasekar a Klaudie Jaźwińské z Columbia Journalism Review však tyto boty vykazují zajímavé chování, když narazí na potenciálně nebezpečné zdroje - nebezpečné ovšem ne pro uživatele, ale pro mateřskou společnost OpenAI.

Tradiční web crawlery fungují podle jasných pravidel. Když narazí na instrukce, že nemají určitou stránku procházet (typicky v souboru robots.txt), jednoduše to respektují. Pokud v běžné aplikaci ChatGPT požádáte o vytažení informací z článků, které blokují crawlery, aplikace vám ohlásí, že to nemůže udělat.

Agentic režimy prohlížečů však fungují jinak. Využívají internet pod záminkou, že jsou běžným uživatelem, a v logech serverů se objevují jako normální Chrome relace. To je dáno tím, že Atlas je postaven na open-source prohlížeči Chromium od Googlu. Díky tomu mohou teoreticky procházet stránky, které jinak blokují automatizované chování.

Toto obcházení pravidel má svou logiku - kdyby Atlas respektoval všechna omezení pro boty, mohlo by to zabránit i manuálnímu přístupu uživatele na dané stránky přímo v prohlížeči Atlas, což by bylo přehnané. Problematické však je, že Atlas se zdá být naprogramován tak, aby se aktivně vyhýbal určitým zdrojům informací, konkrétně těm patřícím společnostem, které vedou proti OpenAI soudní spory.

## Proč je to důležité

Tato kauza odhaluje eticky problematickou oblast vývoje AI nástrojů. Zatímco OpenAI veřejně tvrdí, že respektuje autorská práva a pravidla webu, její agentic nástroje jsou navrženy tak, aby tato pravidla mohly obcházet. Zároveň se ale vyhýbají zdrojům, které by mohly být pro OpenAI právně problematické, což naznačuje selektivní přístup k dodržování pravidel.

Jde o důležitý precedens pro celý průmysl AI. Agentic prohlížeče a asistenti představují novou kategorii nástrojů, která se pohybuje v šedé zóně mezi běžným uživatelským chováním a automatizovaným sběrem dat. Absence jasné regulace a transparentnosti v tom, jak tyto nástroje fungují a jaká pravidla dodržují, může vést k dalším konfliktům mezi technologickými firmami a vydavateli obsahu.

---

[Číst původní článek](https://gizmodo.com/chatgpts-browser-bot-seems-to-avoid-new-york-times-links-like-a-rat-who-got-electrocuted-2000680444)

**Zdroj:** 📰 Gizmodo.com
