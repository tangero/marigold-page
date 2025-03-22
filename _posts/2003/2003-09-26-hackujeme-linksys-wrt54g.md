---
ID: 533
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/hackujeme-linksys-wrt54g

  '
post_date: 2003-09-26 06:09:00
post_excerpt: ''
published: true
summary_points:
- Linksys WRT54G router běží na Linuxu s kernelem 2.4.5.
- Úpravy WRT54G vyžadují zálohu flash paměti pro případ selhání.
- WRT54G lze vylepšit o logování přístupů a úvodní stránku.
- Linksys zveřejnil zdrojové kódy Linuxu pro WRT54G po kritice.
title: "Hackujeme Linksys WRT54G"
---

<p>
Konečně se mi zase podařilo uvést můj přístupový bod <STRONG>Linksys WRT54G</STRONG> do původního stavu a tak mohu podat zprávu o tom, s čím jsem si hrál. Tento přístupový bod, resp širokopásmový směrovač <STRONG>je totiž vybaven Linuxem a kernelem 2.4.5</STRONG>. Což dalo příležitost, jak se do něj probojovat a provádět v něm podstatně větší změny, než výrobce zamýšlel přímým dohráním a rekonfigurací ovladačů. Například regulace vysílacího výkonu je dostupná, stačí si na routeru pustit shell...</p>

<p>
Než si s tím začnete taky hrát, upozorňuji, že resetem zařízení do původního režimu nedostanete, mějte někde zazálohovaný flash paměti, protože až to spadne, už se asi nedostanete na internet, abyste to stáhli. Bezpečné pokusy můžete provádět tak, že na Ping stránce dáte do políčka ping příkazu v apostrofech uzavřený příkaz pro linux. Jak pohodlné...</p>

<p>
Velmi kompletní a detailní návod, jak se štourat v útrobách linuxu Linksys WRT54G najdete na <A href="http://seattlewireless.net/index.cgi/LinksysWrt54g" target=_blank>těchto stránkách</A>. Možná se ptáte, proč byste to měli dělat? Inu proto, že <STRONG>tím můžete rozšířit sadu funkcí</STRONG>, které toto zařízení nabízí. Například o lepší logování přístupů a napadení, jak radí na těchto <A href="http://www.batbox.org/wrt54g-linux.html" target=_blank>stránkách Jim Buzbee</A>. Pokud jste si ještě málo vyhráli, můžete si instalovat podporu pro úvodní stránku pro lidi připojené do vaší sítě, to zase radí stránky <A href="http://nocat.net/~rob/wrt54g/" target=_blank>NoCatSplash on the Linksys WRT54G</A>. </p>

<p>
Mimochodem GLP komunita <A href="http://www.oreillynet.com/pub/wlg/3580" target=_blank>se hodně zlobila na Linksys</A>, protože zatímco používal&#160;Linux, neposkytoval k němu zdrojové kódy distribuce a to by měl. Nakonec je Linksys poskytnul a obliba jeho wifi routeru se tím mezi linuxáky výrazně zvýšila - mohou si teď pohrát :)</p>

<p>
WRT54G není jediný AP, který lze takto hackovat, podobně jsou na tom i starší verze <A href="http://www.ibiblio.org/pub/Linux/docs/HOWTO/Linksys-Blue-Box-Router-HOWTO" target=_blank>WAP11</A> atd nebo Buffalo technika, u níž jsou postupy také známé. Zde jsou ještě <A href="http://seattlewireless.net/index.cgi/WAP54G" target=_blank>postupy pro Linksys&#160;WAP54G</A>, ten nemám a nezkoušel jsem to.</p>