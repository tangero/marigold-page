---
ID: 2167
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/co-u-leopardu-zasmradlo

  '
post_date: 2007-11-07 09:14:25
post_excerpt: ''
published: true
summary_points:
- Skype přestává fungovat v Leopardu s aktivovaným firewallem kvůli modifikaci aplikace.
- System.log v Leopardu může narůst přes 250MB a způsobit zahlcení procesorem.
- Apple testuje aktualizaci 10.5.1 pro Leopard, která by měla opravit chyby.
- iPhone firmware 1.1.1 upgrade je snadný, ale další verze může telefony zablokovat.
title: Co u Leopardu zasmrádlo
---

Pár věcí, které se v Leopardovi nevydařily, se najde. 

<h3>Skype problém</h3>

Když opomineme vypnutý firewall, je s firewallem ještě jeden signifikantní problém. Skype. Když si firewall zapnete (System Preferences - Security) a nemáte nastaveno Allow all incoming connections a používáte Skype, dojde za nějakou dobu k nepříjemné události: Skype odmítne fungovat. Na chvíli pomůže reinstalace, po nějaké další blíže nejisté době nepomůže ani ta. <a href="http://securosis.com/2007/11/01/leopard-firewall-code-signing-breaks-skype-and-other-applications/">Securosis.com</a>

Zádrhel je ve spolupráci digitálního podpisu, firewallu a Skype. Skype totiž po spuštění zmodifikuje sám sebe. Což se nelíbí certifikátu a to se následně nelíbí firewallu. Přesný propletenec ještě nikdo přesvědčivě neobjasnil a ani není jasné, proč Skype modifikuje sám sebe. Možná je to nějaký pokus zabránit reverse engeneeringu, možná jen tak z legrace, já nevím a přesvědčivou odpověď jsem nenašel. Pomůže jen povolit veškerý provoz a Skype přeinstalovat. 

<h3>Systémový log</h3>

Další zádrhel je u systémového logu system.log a root procesu "syslogd". V momentě, kdy log přeroste 250MB, sežere root proces veškerý volný strojový čas. Zaříznutí procesu přes Activity Monitor nepomůže nadlouho, protože za chvíli se celý proces opakuje. 

Proč se tak děje, není jasné. Systémový log by se měl po určité délce přepisovat, ne se táhnout do nekonečna. Je to typický problém, ke kterému by nemělo dojít, ale zjevně někdy a na nějakých konfiguracích dochází. Diskuse o něm přímo <a href="http://discussions.apple.com/thread.jspa?threadID=1205706&tstart=240">na stránkách Apple zde</a>. 

Jen podotýkám, že tento problém je zatím naštěstí dosti zřídkavý a mně se vyhnul. Možná i proto, že nepoužívám Time Machine (nemám na ni volný disk). 

A dobrá zpráva: Apple už prý testuje update Leoparda na 10.5.1, kde se snad tyhle chybky vychytají. 

A dobrá zpráva pro mne: včera jsem se dokopal k upgrade iPhone na firmware 1.1.1, už je to vážně trivialně jednoduchý postup i pro hacknutý telefon. (zlá zpráva je, že se prý <a href="http://blog.wired.com/business/2007/11/iphone-firmware.html">chystá další firmware</a>, který zase bude telefony zavírat :) ) A hned jsem si povolil lokalizované verze. Je tu polština, ruština... jen čeština od Apple tradičně chybí. Oficiální prodej u nás je v nedohlednu. Takže <a href="http://czechiphone.googlepages.com/">zbývá jen šedý dovoz</a>. Ještě, že ten funguje :)