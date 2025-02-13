---
ID: 911
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/prehled-technickeho-zpravodajstvi-muj-hyperportal

  '
post_date: 2004-03-10 16:41:00
post_excerpt: ''
published: true
summary_points:
- Autor vytvořil v Genesis agregátor českých technických zpráv.
- Agregátor řadí články podle důležitosti analyzováním titulků.
- Analýza titulků zohledňuje entity, akce a reaktanty v titulku.
- Veřejná alfaverze agregátoru je dostupná na internet.marigold.cz.
title: Přehled technického zpravodajství &#8211; můj hyperportál ;)
---

<p>
Nedávno jsem si tu stěžoval, že je škoda, že všechny agregátory obsahu řeší načítání RSS jako prosté rozchlívečkování (samozřejmě s čestnou blogportálovou výjimkou, kterou málokdo odhalí). A tak jsem si to vzal trochu jako výzvu, abych něco zkusil spíchnout v Genesis já. Otázka, proč v Genesis - v ničem jiném neumím a Genesis je docela mohutný framework. Bohužel někde už mi v mojí licenci nedává tolik prostoru, kolik by bylo třeba, takže je pravda, že v PHP by to bylo mnohem lepší. Až za to, že v PHP neumím :)</p>

<p>
Abych se k tomu vrátil. Základní zadání je jasné - postahovat všechna RSS technických českých zpravodajství, články rozstrkat do kategorií podle tématu a pak je seřadit podle důležitosti a vypsat na webu. </p>

<p>
Vypadá to jednoduše, ale taková prča to zase není. Protože RSS nepředává kategorie, je potřeba pro rozřazení do kategorií vymyslet jiný mechanismus a stejně tak vymyslet mechanismus pro váhová kritéria. Nakonec jsem zapátral, jak to dělá news.google.com a jak se sestavují titulky a použil jsem podobné (zjednodušené) schéma. Analýza se provádí podle titulku - novináři už mají vpodstatě algoritmizovaný postup, jak sestavit titulek a já ho jen reverzně aplikuji. Každý titulek tedy obsahuje "<EM>entitu"</EM>, o niž jde (zpravidla firmu či osobu - Microsoft, Mlynář atd), pak nějakou "<EM>akci"</EM> konkrétní entity (zlevňuje, představuje, nadává atd) a případně ještě "<EM>reaktanta</EM>" - tedy někoho, kdo na to reaguje nebo koho se událost také týká. Je jasné, že je důležitější titulek <STRONG>Microsoft žaluje firmu Nokia</STRONG>, než titulek <STRONG>Vonásek žaluje Tlučhubu</STRONG>. A málokdo&#160;z toho udělá titulek&#160;<EM>Velká software firma šupajdí k soudu s další velkou kumpanií, co&#160;flikuje&#160;utržený sluchadla</EM>. Obodujete, sečtete body a je vyřešeno. Samozřejmě drobná vada, potřebujete vytipovat ta slova do těch tří skupin, použil jsem Concordanci, program pro analýzu starověkých textů a bylo to ve chvilce :) A další drobná vada - ty váhová kritéria potřebujete vymyslet dost přesně, jinak ten automaticky generovaný výsledek nedává smysl. A do třetice - váhová kritéria jsou nastavená podle toho, co si myslím, že lidi zajímá :)</p>

<p>
Jak všechno zatím vypadá, <STRONG>můžete vidět na adrese </STRONG><A href="http://internet.marigold.cz/"><STRONG>internet.marigold.cz</STRONG></A> - je to taková veřejná alfaverze. Posupem doby na tom budu pracovat&#160;a přidávat zdroje, nicméně když se najde někdo, kdo by to chtěl přepsat do PHP, kde by to samozřejmě mělo hodně dalších možností, klidně se mi ozvěte :) Jako další část algoritmu bych totiž rád přidal kolaborativní filtrování a to už je na Genesis přeci jen silná káva. </p>

<p>
<STRONG>Všechny připomínky uvítám zde v komentářích...</STRONG></p>