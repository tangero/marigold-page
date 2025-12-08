---
author: Marisa Aigen
category: kyberbezpečnost
date: '2025-12-07 15:22:50'
description: Rozšíření prohlížeče tiše infikovalo miliony uživatelů Chrome a Edge
  a proměnilo důvěryhodné nástroje pro produktivitu ve spyware, který v pozadí sledoval
  prohlížecí aktivitu. Celkem bylo postiženo přes 4,3 milionu uživatelů.
importance: 5
layout: tech_news_article
original_title: Millions of users were unknowingly tracked in a 7‑year Chrome and
  Edge malware scheme — extensions turned into spyware
publishedAt: '2025-12-07T15:22:50+00:00'
slug: millions-of-users-were-unknowingly-tracked-in-a-7y
source:
  emoji: 📰
  id: null
  name: Windows Central
title: Miliony uživatelů byly nechtěně sledovány v sedmiletém malware schématu v Chrome
  a Edge – rozšíření se změnila ve spyware
url: https://www.windowscentral.com/microsoft/windows/millions-of-users-were-unknowingly-tracked-in-a-7-year-chrome-and-edge-malware-scheme-extensions-turned-into-spyware
urlToImage: https://cdn.mos.cms.futurecdn.net/TBxEqXPN62mupuczxCyJ7R-1920-80.png
urlToImageBackup: https://cdn.mos.cms.futurecdn.net/TBxEqXPN62mupuczxCyJ7R-1920-80.png
---

## Souhrn
Firma Koi Security, specializující se na analýzu chování rozšíření prohlížečů, odhalila sedmileté schéma, při kterém uživatel známý jako ShadyPanda nahrával do obchodů Chrome Web Store a Edge Add-ons Store na první pohled neškodná rozšíření pro zvýšení produktivity. Po dosažení instalací v řádech milionů je aktualizoval na verze fungující jako spyware, které sbíralo citlivá data o prohlížení. Google a Microsoft rozšíření odstranily z obchodů, ale uživatelé je musí ručně odinstalovat.

## Klíčové body
- Rozšíření jako Clean Master (přes 200 000 instalací) a WeTab (spolu s dalšími od stejného vydavatele přes 3 miliony instalací) získala status ověřených a doporučených.
- Sbírala data včetně všech navštívených URL, celé historie prohlížení, vyhledávacích dotazů, kliků myší, browser fingerprints a HTTP referrer dat.
- Schéma probíhalo od roku 2018 a ovlivnilo přes 4,3 milionu uživatelů Chrome a Edge.
- Hrozba je odstraněna z obchodů, ale ne z nainstalovaných prohlížečů – uživatelé by měli zkontrolovat seznam rozšíření.
- Odhalení proběhlo analýzou chování rozšíření firmou Koi Security.

## Podrobnosti
Uživatel ShadyPanda začal v roce 2018 nahrávat rozšíření prezentovaná jako nástroje pro zvýšení produktivity, například pro čištění dat nebo správu záložek. Tyto počáteční verze se chovaly standardně, což umožnilo budovat důvěru a dosáhnout masivního počtu instalací. Jakmile se instalace vyšplhaly do milionů, přišly aktualizace měnící chování: rozšíření začala v pozadí zachytávat širokou škálu dat. Konkrétně logovala každou navštívenou URL adresu, plnou historii prohlížení, veškeré vyhledávací dotazy zadané v prohlížeči, pozice a kliky myší, detailní browser fingerprint – což je unikátní identifikace prohlížeče na základě jeho konfigurace – a HTTP referrer data, která odhalují, jak uživatel přecházel mezi weby.

Rozšíření Clean Master sloužila k čištění nepotřebných dat v prohlížeči, zatímco WeTab a podobné umožňovaly správu záložek a panelů. Díky neškodnému chování získala některá status „featured“ nebo „verified“, což znamená, že prošla základní kontrolou obchodů. Firma Koi Security, která se zaměřuje na bezpečnostní analýzu rozšíření, toto odhalila při monitorování chování a potvrdila rozsah v zprávě. Google potvrdil, že žádná z těchto škodlivých verzí není již v Chrome Web Store, Microsoft stejně pro Edge Add-ons Store. Odstranění z obchodu však neovlivní již nainstalované instance – uživatelé musí v Chrome přejít na chrome://extensions/ nebo v Edge na edge://extensions/, zkontrolovat seznam a odinstalovat podezřelé položky. Tento incident ukazuje slabiny v systémech schvalování: i ověřená rozšíření mohou být aktualizována na škodlivé verze bez okamžité detekce.

## Proč je to důležité
Tento případ zdůrazňuje rizika spojená s automatickými aktualizacemi rozšíření, které uživatelé často povolí bez kontroly. Pro jednotlivce znamená ztrátu soukromí: sbíraná data umožňují profilování chování, cílené reklamy nebo dokonce přípravu sofistikovanějších útoků. V širším kontextu kyberbezpečnosti odhaluje nedostatky u gigantů jako Google a Microsoft, jejichž obchody s rozšířeními slouží stovkám milionů uživatelů. Přestože Chrome a Edge dominují trhu s podílem přes 70 procent, takové incidenty oslabují důvěru v jejich bezpečnostní mechanismy. Doporučuje se pravidelně kontrolovat instalovaná rozšíření, povolit jen nutné a používat nástroje jako uBlock Origin pro blokování stopovačů. V průmyslu to vede k tlaku na lepší dynamickou analýzu aktualizací, podobně jako u mobilních aplikací v Google Play. Celkově to připomíná, že žádný systém není neomylný a uživatelská ostražitost zůstává klíčová.

---

[Číst původní článek](https://www.windowscentral.com/microsoft/windows/millions-of-users-were-unknowingly-tracked-in-a-7-year-chrome-and-edge-malware-scheme-extensions-turned-into-spyware)

**Zdroj:** 📰 Windows Central
