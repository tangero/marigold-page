---
ID: 1266
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/cdma-prakticky-zdvojnasobilo-datovy-provoz-eurotelu

  '
post_date: 2004-08-23 08:33:00
post_excerpt: ''
published: true
summary_points:
- NIX statistiky ukazují provoz ISP partnerů, zejména do českých zdrojů.
- Eurotel spustil CDMA v srpnu, což zvýšilo příchozí provoz přes NIX.
- Vyšší rychlost připojení vede k většímu objemu přenesených dat.
- Eurotel roste v provozu přes NIX, UPC je větší, T-Mobile menší.
title: CDMA prakticky zdvojnásobilo datový provoz Eurotelu
---

<p>
Via <a href="http://vucako.bloguje.cz/61033_item.php">VÚČAKO</a> jsem (znovu)objevil zajímavé <a href="http://www.nix.cz/index.php?lg=cz&amp;wid=63">statistiky o provozu linek</a> jednotlivých ISP propojených přes NIX. Tedy, statistiky jsou jen za provoz skrze NIX peering, tedy korespondují s objemem provozu do serverů na další NIX partnery, zpravidla tedy do českých zdrojů. I tak je v nich možno najít ledasco zajímavého - ISP se snaží odbavovat český provoz přes NIX. </p>
<p>
Na <a href="http://www.nix.cz/graf4/nix-agr-eurotel.html">této stránce</a> je agregovaný provoz Eurotelu přes NIX a z posledního grafu (toho, co tu vidíme) je vidět provoz na NIX linkách Eurotelu za poslední rok. Zeleně je příchozí provoz, modře provoz odchozí, zpracovalo MRTG. </p>
<div class="rightbox"><img src="/wp-content/uploads/20040823-nix-agr-eurotel-year.png" alt="Eurotel - roční provoz v NIXu" width="500" height="135" /></div><p>
Pokud se podíváme do grafu, vidíme, že počátkem srpna, kdy Eurotel spouštěl CDMA, měl příchozí provoz (přijímaná data, stahování) na úrovni pod 30 Mb/s ve špičce, na konci srpna se pohybuje přes 50 Mb/s (52-55). Pokud se podíváte na odchozí provoz, ten stoupnul tak o třetinu, možná o čtvrtinu. Plyne z toho jednoduchý a nikoliv překvapivý závěr - <strong>vyšší rychlost a kvalita připojení lidi ponouká více toto připojení používat a tedy více a více přenášet.</strong> </p>
<p>
Eurotel je v současné době tak zhruba na třetině provozu UPC a troj-čtyřnásobku provozu T-Mobile  a zatímco tito ISP jsou zhruba ve stabilizované poloze (což, jak víme z branné výchovy je taková, kdy nehrozí poškození vnitřních orgánů), Eurotel roste. </p>
<p>
Otázku, kolik získal Eurotel klientů pro CDMA, to jednoznačně zodpovědět nepomůže. Na druhou stranu grafy a aproximace k rychlosti a množství GPRS klientů napovídají, že drb, že Eurotel měl desetitisícího CDMA klienta už v prvních dnech druhého týdne prodeje CDMA, může mít pravdivý základ. </p>