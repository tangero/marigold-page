---
ID: 567
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/ngmp-next-generation-mail-protocol

  '
post_date: 2003-10-08 07:19:00
post_excerpt: ''
published: true
summary_points:
- NGMP kombinuje prvky SMTP a Jabberu, implementuje design Internet Mail 2000.
- Internet Mail 2000 obsahuje odvážné myšlenky, například ukládání pošty u ISP odesílatele.
- NGMP využívá stávající služby (Apache, MTA, Jabberd) pomocí skriptů.
- Instalace NGMP je složitá, což snižuje šanci na široké přijetí.
title: NGMP &#8211; Next Generation Mail Protocol
---

<p>
Od Petra Krištofa jsem dostal následující komentář k NGMP a protože si myslím, že by to mohlo zajímat více lidí, tak to, co mi poslal,&#160;končí na Marigoldovi:</p>

<p>
NGMP na první pohled vypadá jako kříženec klasické pošty (SMTP) a instant messagingu (jaber). Podle autorů je NGMP implementaci designu "Internet Mail 2000" navrženého legendárním a kontroverzním D. J. Bernsteinem. </p>

<p>
Jako každý DJB-ware, i IM2000 obsahuje brilantní myšlenky, které jsou ale příliš odvážné, než aby je praxe dokázala skousnout = ukládání odchozi pošty u ISP odesílatele, notifikace příjemce pomoci IM, kterou ISP adresáta drží v paměti, úspora diskové a přenosové kapacity, spolehlivost,.. <A href="http://cr.yp.to/im2000.html">http://cr.yp.to/im2000.html</A> </p>

<p>
NGMP využívá daemonu stávajících služeb - apache, MTA, jabberd, které spojuje nějakými skripty. Instalační howto jsem četl jenom zběžně, takže detaily nevím. A v tom je podle mě kámen úrazu. Po světě jsou tisíce open-relay SMTP serverů, které lidé nedokáží pořádně zabezpečit. A teď po nich někdo chce, aby si nainstalovali a nakonfigurovali 3 (slovy tři) služby a ještě nějaký doplňky. To není reálné, to nikdo dělat nebude. </p>

<p>
Co se týká budoucnosti pošty, dávám spíše více šanci AMTP - Authenticated mail transfer protokolu. Klasický smtp+větší bezpečnost. Jeden daemon, jeden konfigurak, žádný složitosti nebo revoluční myšlenky.</p>