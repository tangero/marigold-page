---
ID: 1460
author: Michal Krsek
layout: post
oldlink: 'https://www.marigold.cz/item/je-libo-etc-heslo

  '
post_date: 2004-12-30 09:35:00
post_excerpt: ''
published: true
summary_points:
- Článek na Mobil serveru popisuje zabezpečení WiFi sítí.
- Překlad článku obsahuje nepřesnosti ohledně Unix systémů.
- Soubor /etc/heslo neexistuje v Unixu, správný název je /etc/password.
- Hesla v Unixu se obvykle nacházejí v /etc/shadow nebo AAA databázi.
title: Je libo /etc/heslo ?
---

<p>
Ve dnešním vydání Mobil serveru vyšel článek (převzatý z ComputerWorldu) s názvem <a href="http://mobil.idnes.cz/mob_tech.asp?r=mob_tech&amp;c=A041228_164257_mob_tech_brz">Jak jsou (ne)bezpečné bezdrátové sítě?</a> Článek sám celkem rozumně popisuje možnosti zabezpečení infrastruktury postavené na WiFi. Překlad ovšem nedělal nikdo, kdo rozumí Unixu (aspoň na uživatelské úrovni). Perla &#8220;<span style="font-style: italic;">pokud svá hesla vedete na unixovém serveru ve formátu /etc/heslo</span>&#8221; je hned dvouúrovňová. Jednak soubor /etc/heslo na svém Unixu nehledejte (/etc/password tam asi bude) a i když ten soubor prohlédnete, hesla budou pravděpodobně v /etc/shadow (či v nějaké AAA databázi).
</p>