---
ID: 2220
author: Patrick Zandl
categories:
- Video
- Flash
layout: post
oldlink: 'https://www.marigold.cz/item/experimentovani-s-h264-ve-flashi

  '
post_date: 2008-04-09 16:14:38
post_excerpt: ''
published: true
summary_points:
- H.264 video ve Flashi testováno, vyžaduje Flash 9.0.115 a vyšší.
- Procesorová zátěž je vysoká, nutný přepis do AS3 pro optimalizaci.
- Kvalita H.264 videa dramaticky lepší než VP6 při srovnatelném bitrate.
- Flash 9 má jen 70% uživatelů, což je zádrhel pro rozšíření.
title: "Experimentování s H.264 ve Flashi"
---

Už jsem kdysi psal, že s tímhle bude jednou sranda - H.264 ve Flashi. Připravili jsme (tedy Franta, abych byl přesný v rámci elaborování s vyšší kvalitou) takový malý pokus, abyste si to uměli lépe představit ... 

<script src="http://www.stream.cz/include/61285"></script>

Pokud vám výše vložené video nehraje po stisku buttonku, nemáte patřičnou verzi Flashe (9 final a vyšší, tedy od 9.0.115) a dál se bez ní nepohnete, pokud tam nemáte nic, nemáte ani flash a bez toho se video ve flashi demonstruje fakt blbě. Ani to sem nepište, že ho nemáte rádi :)

Když se vám bude video přehrávat, povšimněte si pár věcí: 

1) Zátěž procesoru jde dramaticky nahoru
2) Video má skoro stejnou kvalitu, jako původní Flash VP6 video. 
3) Obraz se bude asi trhat, což souvisí s bodem 1 a s tím, že je to z testovací platformy

Ad 1 - to je pravda, o tom žádná. To se ladí a nepomůže ničehož menšího, než přepis do AS3. 

Ad 2 - z tohoto omylu vás vyvede stisknutí toho rámečkového tlačítka vpravo dole, které video roztáhne na celou obrazovku (v malém to nepoznáte). Záhy zjistíte, že s nepatrným navýšením bitrate (z 520 na 600 Kb/s) je rozdíl kvality dramatický a řekl bych, že je to velmi podobné kvalitnímu příjmu analogové TV. Ostatně, posuďte sami. Čím to? Kodek H.264 je dramaticky účinnější a takové kvality standardní VP6 nedosáhne ani při bitrate dvojnásobném.

Zádrhel? Flash 9 má jen 70% uživatelů ...