---
ID: 1047
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/jeste-jednou-k-te-wifi-chybe

  '
post_date: 2004-05-20 09:20:00
post_excerpt: ''
published: true
summary_points:
- WiFi zranitelnost spočívá v chybě logiky, umožňující rušení pásma nekooperujícími
  klienty.
- Problém nastane, až bude existovat jednoduchý software pro zneužití chyby běžnými
  uživateli.
- WiFi standard původně nepředpokládal použití mimo domácnosti/firmy, proto chybí
  obrana.
title: Ještě jednou k té WiFi chybě
---

<p>
V průběhu těch pár dní, které uplynuly od objevení té díry ve WiFi, o níž <A href="/zprava.html?cislo=28487">jsem psal nedávno</A>, jsem četl mnoho komentářů na toto téma - od zděšených po uklidňující. Například i <A href="http://vucako.bloguje.cz/42790_item.php" target=_blank>Kamojedov ukolébává</A> obecenstvo tvrzením, že o nulovou odolnost je těžké se snažit. O nulovou nepochybně - v tomto případě ale šlo o základní chybu v logice, neb chyba je sice triviální a překvapivá, ale ne nepředpokládatelná. Síť přeci musí mít mechanismus na to, jak vykopnout nekooperujícího&#160;či rovnou&#160;sabotujícího klienta, protože něco jiného je vysílat příznak "obsazeno" a něco jiného je postavit širokopásmový vysílač a jím rušit celé pásmo. Protože v tom druhém případě si vás za chvíli pár dobrovolníků například z CzFree (nebo jiných, kterým to nejde) zaměří, na to jim stačí dvě směrovky a dva notebooky a chvíle práce v terénu. A pak vám našlapou tu vaši rušičku do obličeje - a podle mne vcelku po právu. V tom první případě je odchycení nepoměrně složitější. </p>

<p>
Celý problém <STRONG>není problémem do chvíle, než někdo udělá jednoduchý software</STRONG>, který si bude moci každý lama nainstalovat do svých Windows a na běžně dostupné kartě ho spustit. Protože ono zas není tak jednoduché tu chybu z teorie převést do praxe - na to už musíte rozumět nejenom WiFi, ale i programování. Takže se jen modleme, aby to nějakého mudrce nenapadlo. </p>

<p>
Domnívám se, že chyba (či vlastnost) v návrhu zůstala proto, že <STRONG>WiFi je standard pro místní bezdrátovou síť</STRONG> a nepočítalo se s tím, že ho budou používat lidé mimo domácnost či mimo firmu. Nepočítalo se s tím, že na tom někdo bude provozovat last mile broadband přístup. A tak se tam ani žádný obranný mechanismus proti nekooperujícím klientům neimplementoval. Proč taky - v běžné WLAN síti by adminovi stačilo sabotujícího uživatele napomenout a email s napomenutím poslat v cc: i na personální...</p>