---
ID: 1444
title: Chci bezdrátovou síť (6.1)
author: Noname
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/chci-bezdratovou-sit-6-1
published: true
post_date: 2004-12-14 22:12:00
---
	<div class="rightbox"><img src="/wp-content/uploads/cache/20041214-retranslace.gif" alt="Retranslace" width="250" height="156" /></div><p>
Tento článek je volným pokračováním mého srpnového seriálu <a href="http://www.marigold.cz/?query=chci%2Bbezdr%C3%A1tovou%2Bs%C3%AD%C5%A5&amp;amount=0&amp;blogid=1">Chci bezdrátovou síť</a>, jež objasňuje vše podstatné, co byste měli chtít vědět, když chcete bezdrátovou síť. Pro ty, kteří zde o prázdninách nebyli doporučuji <a href="/item/chci-bezdratovou-sit-1/category/wifi">první kapitolu</a> a pak si dole můžete kliknout na &#8220;lokální hledání&#8221; a můžete se tak dostat na další pokračování.</p>
<p>
Jak víte, seriál popisuje vše od historie, přes standardy, instalace vnitřních sítí až po instalace venkovních sítí a antény. V jednom z posledních dílů jsem slíbil, že rozvedu co jsou to retranslace a jak se dělají, bohužel jsem to tehdy nestihl.</p>
<p>
Berte to tedy jako splátku tohoto dluhu a zároveň jako omluvu všem, komu vadí ty články, které jsem sem za posledních pár dnů dal a které pravda nebyly vždy zcela v &#8220;duchu&#8221; tohoto serveru, ale měly jen zaplnit prostor a donutit vás na Marigold nezapomenout v době, kdy je Patrik na svatební cestě. Vedle kontroverzního článku &#8220;<a href="/item/cdma-je-slepa-ulicka">CDMA je slepá ulička</a>&#8221; je to asi druhý opravdový článek, který jsem vydal, vím o tom a ještě jednou se omlouvám všem, kteří ty zbylé nepřekousli.</p>
<p>
Takže tolik úvod a pojďte se vrhnout na problematiku retranslací. V první ze tří části se budu věnovat problematice obecně, v dalších dvou dílech každému ze dvou typů řešení samostatně (nebojte se, oba vyjdou ve středu).</p>

<!--more-->	<h3>Co to znamená retranslace</h3>
<p>
Představte si situaci, kdy potřebujete spojit dvě místa (řekněme A &amp; B) bezdrátovým spojem, která na sebe nevidí (což bývá téměř vždy nutná podmínka), případně jsou od sebe příliš vzdálena a vy nemůžete porušit generální licenci o maximální hustotě vyzářeného výkonu (případně je to příliš daleko i s porušením). Existuje ale místo R, které &#8220;vidí&#8221; na místo A i na místo B, případně je od obou míst méně vzdáleno. Potom místo R se nazývá retranslační bod a komunikace z A do B neprobíhá přímo, ale přes bod R. Bezdrátový spoj A → R → B se potom nazývá <strong>spoj s jednou retranslací</strong>.</p>
<p>
Retranslace mohou být někdy i několikanásobné, potřebujete-li např. vytvořit velmi dlouhý spoj, můžete zřetězit např. 3 retranslace (R, S, T) za sebou (víc už se v podstatě nedělá) a tak může komunikace jít postupně A → R → S → T → B.</p>
<p>
Aby to nebylo tak jednoduché, lze za určitých podmínek (které dále rozebereme) mít i různě větvenou retranslaci. Potřebujeme-li tedy spojit bod A s body B a C, ovšem tyto na sebe navzájem nevidí, ovšem vidí opět všechny na bod R, potom může komunikace probíhat i A → R → B,C.</p>
<p>
<strong>Způsoby retranslace </strong>se dají rozdělit nejsnadněji na:</p>

<ul>
<li>pasivní, </li>
	<li>aktivní. </li>
</ul>
<p>
<strong>Pasivní retranslace </strong>využívá jen přesměrování či odrazu signálu (rozebereme dále) bez nějakého přidaného aktivního prvku, není třeba tedy žádného napájení atp., ovšem má mnohá omezení (nelze z tohoto místa &#8220;odebírat internet&#8221;, těžko se monitoruje, vyžaduje speciální podmínky atd.).</p>
<p>
<strong>Aktivní retranslace</strong> využívá aktivní prvek, který je de-facto další přístupový bod, ovšem bez klientů (respektive klienty jsou jen okolní přístupové body). Při určitých řešeních je možné připojovat na tento prvek zároveň i klienty, ale nebývá to optimální (vše rozvedu později)</p>
