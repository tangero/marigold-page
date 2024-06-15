---
ID: 1347
title: 'Podpora HSDPA v&nbsp;UMTS Release 5'
author: Patrick Zandl
post_excerpt: ""
layout: post
oldlink: >
  https://www.marigold.cz/item/podpora-hsdpa-v-umts-release-5
published: true
post_date: 2004-10-05 12:55:38
categories: [UMTS, 3G, Turboúvod do mobilních sítí]
---
<p>
HSDPA jako další štace ve zrychlování UMTS dat je podle některých producentů za rohem a je dokonce pravděpodobné, že české UMTS sítě s HSDPA odstartují. Tedy, pokud se všechno stihne, že …</p>

<p>
Upgrade UMTS Release 99 na HSDPA je teoreticky poměrně jednoduchá věc, protože HSDPA může koexistovat na stejném RF přenašeči, jako Rel99 UMTS. Tomu pomáhá dynamické sdílení kódu u HSDPA, takže zdroje se sdílejí mezi Rel99 i HSDPA. Instalace HSDPA se dotýká hlavně NodeB, které se musí uzpůsobit na novou subvrstvu MAC (MAC-hs), zatímco zbytek RNC si vystačí prakticky jen s  Rel99. Doslovně to samozřejmě není pravda, protože fukcionalita řízení přístupu k médiu MAC je v Rel5 rozdělena mezi NodeB a RNC, zatímco u Rel99 zůstává jen na RNC. NodeB v Rel5 přebírá zodpovědnost za ty části MAC, které jsou kritické na zpoždění a výkon, ty jsou tedy vyčleněny v MAC-hs a jsou blíže mobilnímu terminálu. Jde například o rychlé plánování Fast Scheduling nebo CQF – Channel Quality Feedback, Zpětná informace o kvalitě kanálu. </p>

<p>
To  je docela důležitý poznatek, protože přizpůsobení NodeB pro HSDPA obnáší update pro podporu basebandu (sakra, jak se to překládá?) a zpracování MAC-hs. K tomu není nutný hardware upgrade, takže se může update distribuovat vzdálenou instalací, v horším případě jsou potřeba nové baseband karty. RNC bude potřebovat jen úpravu software, jádro sítě zůstává nedočteno a další úpravy čekají až terminály, které musí podporovat HAR-Q, multikódy a zpracování HSDPA podle jedné z dvanácti HSDPA tříd, do kterých chtějí patřit.</p>

<div class="rightbox"><img src="/assets/20041005-hsdpa-terminaly.jpg" alt="HSDPA z pohledu terminálu" width="400" height="260" /></div>
<i>Tenhle obrázek nemá prakticky žádný smysl a můžete do něj hledět po libosti, nic z něj nevykoukáte kromě toho, že dva mobily se překvapivě připojují na NodeB, překvapivě tam tečou nějaká  signalizační data a je tam nějaký TTI (Transmission Time Interval), který jsem vám mazaně zatajil a v němž se upřednostní signálově lepší mobilka. Jenže článek s obrázkem vypadá líp&#8230;</i></p>

<p>
Jen abychom věděli a znali – klíčové elementy HSDPA jsou:</p>

<ul>
<li>High-Speed Downlink Shared CHannel (HS-DSCH) – nový typ transportního kanálu. Ten umožní několika uživatelům sdílet kanál na vzdušném rozhraní o špičkové rychlosti až 14 Mb/s. </li>
<li>Fast scheduling – plánování je přesunuto z RNC na NodeB, takže 	síť se dozví rychleji o změnách v podmínkách příjmu na straně terminálu. </li>
<li>Fast Retransmissions a H-ARQ – Znovuzaslání dat při nemožnosti dekódovat paket dříve řešilo RNC, nyní ho také řeší NodeB. Tím se zase zkracuje doba potřebná pro znovuzaslání vadných dat. H-ARQ je Hybrid Automatic Repeat Request. </li>
<li>
Channel Quality Feedback</li>
<li>
Adaptivní modulace a kódování</li>
</ul>
<p>
Výsledek toho všeho povídání – HSDPA nabídnou v UMTS Release 5 síti teoretickou sdílenou rychlost až 14,4 Mb/s. V praxi samozřejmě podle toho, co utáhne mobilka, spisovně terminál. A taky podle toho, kolik lidí bude sdílet atd atd, jak je u rádia obvyklé. </p>

<p>
V praxi se počítá, že maximální propustnost UMTS Rel99 je na makrocele zhruba 900 Kb/s (teoreticky 2 Mb/s), HSDPA s plánováním Round Robin je na cca 1,5 Mb/s, proporcionálně spravedlivé plánování vytáhne až 2,2 Mb/s a pokud se použije telefon s dvěma anténami, dostane se 3,5 Mb/s agregované průměrné propustnosti na 5 MHz širokém přenašeči. </p>

<p>
Termín HSDPA se naučte, protože pro UMTS a jeho další naděje do budoucna je to jedna z nejčastěji vzývaných manter v boji o rychlodatovou mobilní přízeň… </p>

Pokračujte dále na [Seriál Mobilní sítě](/mobilnisite/)