---
ID: 1130
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/linksys-ma-problemy-s-bezpecnosti-wrt54g-a-prinasi-update

  '
post_date: 2004-06-07 08:39:17
post_excerpt: ''
published: true
summary_points:
- Linksys routery WRT54G umožňovaly dálkovou administraci i po vypnutí této funkce.
- Nová beta verze firmware 2.02.8 od Linksysu tento problém s administrací řeší.
- WiFisti spekulují, zda šlo o chybu nebo zadní vrátka, podobně jako u Netgear WG602.
- Linksys firmware je open-source, ale zdrojový kód je dostupný za poplatek.
title: Linksys má problémy s&nbsp;bezpečností WRT54G a&nbsp;přináší update
---

<p>
Linksys měl minulý týden proklatou smůlu - ukázalo se, že jeho oblíbené routery WRT54G lze dálkově administrovat i v případě, když člověk tuto vlastnost vypne. To je krajně nepříjemné, protože většina lidí, kteří si takto vzdálenou administraci po internetu vypnou, se neobtěžují ani změnit defaultní heslo &quot;admin&quot; - proč taky, když jsou doma jediní, kteří umí router administrovat. Proscanoval jsem kus Chella a za chvíli jsem našel čtyři adresy s Linksys routery s tímto problémem. Jeden můj vlastní, jasně že mám default heslo - jenže já mám zapnutý firewall na routeru a v takovém případě se problém neprojevuje. Na chybu přišel <a href="http://rateliff.net/">Alan W. Rateliff</a>. Zde je článek o ní na <a href="http://news.com.com/Linksys+Wi-Fi+router+vulnerability+discovered/2100-7349_3-5226918.html?tag=nefd.top">CNetu</a>.</p>
<p>
Linksys nicméně o víkendu vydal betaverzi nového firmware 2.02.8 - ta problémy s dostupností remote administrace odstraňuje. Nicméně jde o americkou betu, o evropské nemám zpráv. Dostupná je zde na <a href="http://www.linksys.com/download/firmware.asp?fwid=201">webu Linksysu</a>.</p>
<p>
WiFisti se ovšem začali nyní dohadovat, zda opravdu šlo o bug nebo o backdoor. Není to totiž první podobný problém, například <a href="http://besphere.blogspot.com/2004_06_01_besphere_archive.html#108637905031922711">zde zmiňují </a><strong>zadní vrátka do Netgear WG602</strong>, kde sice můžete nakrásně změnit heslo pro vzdálenou administraci routeru, jenže je tu jedno univerzální heslo v podobě telefonního čísla výrobce zadaného do políčka hesla. Fuj - to se těžko okecá. V případě Linksysu se kloním spíše k tomu, že jde o banální chybu. </p>
<p>
Tady je nutno připomenout, že Linksys firmware je (k velké nelibosti Linksysu a zejména Cisca) open-source, takže do zdrojáků může každý nahlédnout, i když v tomto případě je Linksys posílá jen na CD za 20 USD. </p>