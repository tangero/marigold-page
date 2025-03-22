---
ID: 1374
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/s-prehledy-wifi-siti-se-roztrhl-pytel

  '
post_date: 2004-10-27 14:36:26
post_excerpt: ''
published: true
summary_points:
- Marigoldova databáze WiFi hotspotů se smísila s body pro trvalé připojení.
- Internet pro všechny vytvořil seznam přípojných bodů pro trvalé připojení.
- Lupa a Mobil.cz také spustily databáze WiFi bodů a připojení.
- Marigold ztratil motivaci k vývoji databáze kvůli odchodu a mapovým podkladům.
title: "S přehledy WiFi sítí se roztrhl pytel"
---

<p>
Když jsem začínal s přehledem WiFi sítí na Marigoldovi, nic podobného u nás neexistovalo a pokud jste chtěli najít nějaké hotspoty, museli jste složitě prohledávat weby všech poskytovatelů. Za ty dva roky se ale situace změnila. Tak především se ukázalo, že nedonutím lidi zadávat do té marigoldí databáze pouze skutečné hotspoty, tedy přípojné body s přístupem možným snadno z ulice a placeným na bázi ad-hoc (když už ne zdarma), bez nutnosti paušální měsíční platby. Do databáze to zaneslo trochu zmatek, protože se hotspoty smíchaly s přípojnými body pro trvalé připojení. </p>

<p>
Naopak na serveru <a href="http://www.internetprovsechny.cz/">Internet pro všechny</a> vznikl seznam přípojných bodů pro trvalé připojení. </p>

<p>
Pak přišla s <a href="http://wifi.lupa.cz">databází WiFi bodů</a> také Lupa, zde už není ani pokud o oddělení trvalého a nárazového způsobu poskytování WiFi, dost možná i proto, že řada komerčních poskytovatelů hotspotů nabízí oba dva přístupové programy a problémy jsou jen s komunitními hotspoty, které většinou neumějí nárazový přístup zaúčtovat. </p>

<p>
Do čtvrtice tento týden přišel s <a href="http://mobil.idnes.cz/mobilni_komunikace/wifi/mapawifi/">databází WiFi připojení</a> také Mobil.cz - ačkoliv zde jde o přejímanou databázi z Internet pro všechny. Na druhou stranu je tato databáze překreslená a podle mne o něco přehlednější. Nevýhodou této databáze je hlavně fakt, že neregistruje přípojné body určené spíše pro nárazové připojení, jako jsou body T-Mobile, Eurotelu a Telecomu. </p>

<p>
Jak vidno, databází je tu celá řada. Nevýhodou té marigoldí byl fakt, že s odchodem z Genesis jsem ztratil možnost a motivaci ji řádně programově vyvíjet, prgat ji v PHP mne jednak ani nezačalo bavit, jednak už na to ani nebyl čas. </p>

<p>
Řešení se sice našlo v podobě přestavby databáze Tomášem, kdy jsme databázi doplnili i o hezkou mapu a možnost si přípojné body vyhledávat dle ulice a jejího okolí, jenže tady jsme narazili na zádrhel. Na mapový podklad. Myslel jsem si totiž bláhově, že ho od někoho koupíme za rozumné peníze nebo vyměním za nějaký sponzorský odkaz. <i>Na obrázku je vývojová verze bez designu.</i></p>

<p>
<img src="/wp-content/uploads/1/20041027-wifimapy.jpg" alt="naše verze WiFi map" width="500" height="336" /></p>

<p>
Ach ta naivita, že na nekomerční věci se něco takového sežene <i>(a tím se omlouvám lidem z CzFree, kteří vytvářeli Monitor a kterým jsem vynadal, že se nesnažili mapový podklad legalizovat. Už to zcela chápu)</i>. Čtveřice oslovených dodavatelů mapových podkladů nám nabídla kulantní podmínky obnášející několikatisícový měsíční poplatek za licenci k užití mapy s předpokládanou návštěvností stovek lidí. Jestli jsem si říkal, že licencoři hudby a filmů jsou pěkní nenažranci, tak o firmách vytvářejících mapové podklady si nově myslím něco o tři řády sprostšího :(</p>

<p>
Výsledek je jednoduchý - downgradovat databázi na verzi bez mapy se nám už nechce, ukrást mapy taky ne a zavazovat se k placení tisíců za mapový podklad tuplem ne. Navíc konkurence úspěšně kvete a ačkoliv mám k všem třem databázím své výhrady (zejména že nemají offline či wap verzi), mám nulovou chuť s databází hotspotů pokračovat. Takže uvidíme, jak dopadnou poslední jednání o mapových podkladech.
</p>