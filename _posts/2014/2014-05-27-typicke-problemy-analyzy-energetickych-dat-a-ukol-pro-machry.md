---
ID: 2899
title: 'Typické problémy analýzy energetických dat &#8211; a&nbsp;úkol pro machry'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/typicke-problemy-analyzy-energetickych-dat-a-ukol-pro-machry
published: true
post_date: 2014-05-27 14:01:15
---
<p>Dneska jsem četl příjemný <a href="http://www.lupa.cz/clanky/jiri-hlavenka-velka-data-nebo-jenom-velky-prachy">článek Jiřího Hlavenky o Velkých Datech na Lupě</a>. Asi mu rozumím trochu jinak, než většina diskutujících pod ním. Velká Data se používají občas jako kladivo na špendlíky, to ale neznamená, že to není dobře.</p>


<p>Ukážu vám, co analýza velkých dat není a co je - na příkladu dat o spotřebě elektřiny, tedy na úkolu, který dobře znám. </p>


<p>Mějme rezidenčního zákazníka, u něhož známe jeho minutové agregáty spotřeby elektřiny. Úkolem je navrhnout mechanismus analýzy této datové řady, která bude schopná v reálném čase určit, zda spotřeba je v normálu, nebo zda je něco se spotřebou v nepořádku. V nepořádku je spotřeba příliš malá (vypadl proud nebo část rozvodu) či příliš velká (neoprávněný odběr, ale poškozené či chybně zapnuté zařízení). To je normální analýza, i když i na ni musíte jít chytře. Tady vám nepomůže, že jste chodili jeden víkend na kurz programování, tady potřebujete slušné vzdělání v analýze dat a statistice. Vzdělání, které se teď hodí a které vás odlišuje od běžného nájemného kodera. Asi namítnete, že tohle s přehledem vyřeší směrodatná odchylka. Fakt? Jste machr? Stáhněte si <a href="http://goo.gl/sclFPK" target="_self" title="">tento export dat za měsíc</a> a zkuste to ověřit či vyluštit - vymyslet takový algoritmus, který na těch datech bude fungovat a nebude hlásit plané poplachy, když si zapnete rychlovarnou konvici. Řešení posílejte na <em>zandl zavináč energomonitor.cz</em> či ho pište do komentářů a za nejlepší (či nejzajímavější) řešení vám pošlu sadu energomonitoru, abyste si příště mohli hrát s vlastními daty. To je větší legrace, věřte mi :)</p>
<p><strong>Tohle ale analýza velkých dat není.</strong> Ani, když těch klientů budou tři miliony českých odběrných míst. Tohle je jen otázka hrubého výpočetního výkonu. Chytrý člověk se zapotí až při ladění parametrů takového algoritmu.</p>
<p><strong>Co jsou velká data?</strong> Mějme toho samého rezidenčního zákazníka, ale vteřinová data. Úkolem je automaticky rozpoznat spotřebiče, které tento zákazník používá a nabídnout mu je, aby si je mohl popsat a říct, že tohle je lednička, tohle je pračka, tohle bojler (předpokládáme jen větší/žravější spotřebiče). Tady už se machr zapotí hodně, protože potřebujete kontinuálně vyhledávat vzory v signálu a odvrhnout šum (tedy menší spotřebiče). Tohle je hodně chytrá analýza. Přidejme tři miliony odběrných míst. Ještě pořád je to jen chytrá analýza, i když už je fest rozdíl v tom, jak navrhnete vyhledávací algoritmy na to, abyste vyhledali vzory, protože jinak se za nájem výpočetního výkonu nedoplatíte.</p>
<p>Váš úkol je jiný. Vzít takto zanalyzovaná a zákazníky otagovaná data a zjistit, <strong>který zákazník spotřebič používá tak, že jeho užitím proti průměru šetří a který ho naopak užívá nehospodárně.</strong> Výsledkem úkolu je, říct nehospodárným klientům, jak mají své zařízení používat lépe. <strong>Příklad:</strong></p>
<ul><li>Lidé, kteří utratí za vaření vody v rychlovarné konvici méně, vaří menší množství vody. Nestačilo by vám menší množství vody? </li><li>Za mytí nádobí v myčce ušetří ostatní lidé tak, že zvolí kratší mycí cyklus a nádobí myjí v nízkém tarifu. </li></ul><p>Tři miliony záznamů musíte nejdříve dezintegrovat, pak analyzovat, rozpoznat, clusterovat do skupin podle typů domácností, aby další analýza dala smysl a pak znovu křížem analyzovat. Je v podstatě jedno, jakou komerční výpočetní sílu a technologie z roku 2000 byste chtěli použít, neuspěli byste s požadavkem, takový report zákazníkovi každotýdenně automaticky poskytovat. <strong>Tohle jsou velká data. Úkol obrovského datového rozsahu, obrovské algoritmizační složitosti s nutností průběžného zpracování v téměř reálném čase a na proměnných datech.</strong></p>
<p>Troufáte si ještě hledat řešení takového problému? Pokud ano, je to dobře. Vyřešíte ho? Ještě lépe. Pak jste teprve <strong>big data machr</strong> a ne jen anonymní žvanil z diskuse na Lupě ...</p>
<p>&nbsp;</p>
