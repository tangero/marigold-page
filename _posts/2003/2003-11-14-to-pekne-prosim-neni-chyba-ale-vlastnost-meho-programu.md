---
ID: 670
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/to-pekne-prosim-neni-chyba-ale-vlastnost-meho-programu

  '
post_date: 2003-11-14 09:02:00
post_excerpt: ''
published: true
summary_points:
- Marigold zobrazuje odkazy na nové články od poslední návštěvy uživatele.
- Některé odkazy na nové články nemusí fungovat kvůli předgenerování titulní stránky.
- Problém nastává, protože personalizovaná část zobrazuje odkazy dříve, než se článek
  vygeneruje.
- Řešením je zvyknout si na to, nebo manuálně upravit URL adresu článku.
title: To pěkně prosím není chyba, ale vlastnost mého programu…
---

<p>
Dostal jsem tento týden několik upozornění na "vlastnost" na Marigoldovi, která je už docela stará. A protože se mi nechce to vysvětlovat jednotlivě, dám to v plen. Jak jste si možná všimli, když přijdete po delší době na marigolda, vypíše se vám na začátek stránky odkazy na nové články, které přibyly od doby poslední návštěvy (pokud máte cookies) - maximálně tuším deset odkazů. Když na něj kliknete, sjedete na stránce na ten článek. Až potud je to fajn, jenže někdy se vám stane, že ten první odkaz <EM>(nebo několik prvních odkazů)</EM> vás na článek nehodí a ten článek tam není. </p>

<p>
To je tak: titulní stránku Marigolda v Genesis nechávám celou předgenerovat abych šetřil server <EM>(čili se sestaví data z databáze a uloží se do HTML fajlu na disk, jednoduše řečeno - a vám už se posílá jen ten fajl).</EM> Nemůže se předgenerovat jen ta "personalizovaná" část - protože ta musí zjistit, kdy právě vy jste naposledy byli na Marigoldovi a podle toho vám vypsat zprávy, které tu přibyly od té doby. Až potud je to v pohodě, trivialitka v Genesis na dvě minutky práce. Jediný problém ale je v tom, že tato nepředgenerovaná část vypíše i odkazy na zprávy, které jsem do systému právě přidal, jenže vy je nevidíte, protože v té části, kde se mají vypisovat jejich texty a kam odkaz míří, ještě nejsou vygenerované. Marigold se generuje jednou za tuším dvacet minut, takže se to nestává často, ale stane se to zejména ráno, kdy většinou zprávy zadávám. </p>

<p>
Jendoduché řešení problému mne nenapadlo z hlediska počítačů, ale z hlediska uživatele <EM>(=čtenáře, vás)</EM> - musíte si na to zvyknout. Jinak bych musel generovat online celou titulku Marigolda, což se mi nezdá moc dobré, nebo bych musel odečítat zprávy do času posledního generování, což se mi také nechce. </p>

<p>
Takže chybu prohlásím za vlasnost, nazvu ji SneakPreview, vydám k ní tiskovou zprávu a vše je OK, ano?</p>

<p>
<EM>PS: Pokud na ten článek spěcháte, stačí se podívat na to číslo za # v URL, kliknout si na oranžový odkaz zalinkovat který je pod každou zprávou a změnit to číslo v URL na číslo, které si pamatujete z předešle. Jak triviální, skoro jak dostat se na Oskar lince k živému operátorovi ;)</EM></p>