---
ID: 1123
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/herecast-lokalizace-polohy-pomoci-wifi

  '
post_date: 2004-06-03 09:21:00
post_excerpt: ''
published: true
summary_points:
- Herecast je open source projekt lokalizace polohy pomocí WiFi hotspotů.
- Lokalizace Herecast funguje porovnáváním nalezených hotspotů s databází.
- Přesnost lokalizace Herecast je minimální, v řádu desítek až stovek metrů.
- Herecast nabízí aplikace HereSay (chat) a Area Maps (mapy oblasti).
title: Herecast &#8211; Lokalizace polohy pomocí WiFi
---

<p>
Nedávno jsem zde odkazoval na článek věnovaný sledování dětí v Legolandu pomocí WiFi. Porozhlédl jsem se trochu kolem a ukázalo se, že služeb založených na lokalizaci polohy pomocí WiFi pár existuje. Jedním z takových zajímavějších (protože mimo jiní open source) je projekt <a href="http://www.herecast.com/">Herecast</a>.</p>

<div class="leftbox"><img src="/wp-content/uploads/20040603-herecast.gif" alt="Herecast - WiFi scanner, mapa a přehled hotspotů" width="250" height="214" /></div><p>
Asi chápeme, že WiFi hotspoty při lokalizaci využívají svých slabin a nikoliv nějaké mytické technologie. Herecast neudává polohu ve stupních délky a šířky, jak jsme zvyklí z GPS, ale říká vám, kde se uživatel nachází (poblíž Bílé labutě třeba) - a to zjišťuje tak, že porovnává nalezené hotspoty s databází a z toho aproximuje, kde se tak zhruba uživatel nachází. Jde tedy o podobný princip, jako při lokalizaci v GSM síti, s tím drobným rozdílem, že v GSM síti se používá proměnná Timing Advance (TA) nabývající určitých hodnot v závislosti na vzdálenosti od BTS. A výhodou TA je fakt, že nezáleží na kvalitě signálu, zatímco u WiFi podobná proměnná není a tak si musí Herecast vystačit s porovnáním kvality signálu od jednotlivých hotspotů. Ergo přesnost je minimální (stovky či desítky metrů), rozhodně to nelze brát za bernou minci a konkurenci jiným systémům. Spíše jde o nadstavbový software, legrácku pro lidi, kteří mají zařízení s WiFi. Tomu odpovídá aplikační software HereSay - je to chat pro lidi, kteří jsou ve vašem blízkém okolí, prostě jim můžete napsat vzkaz (všem, či vybraným) a psát si s nimi. </p>

<p>
Druhou aplikací jsou Area Maps - dosti podrobná mapa oblasti. Samozřejmě se zobrazením, kde jste, pokud je jak to vyzkoumat (=chytáte nějaký hotspot).</p>

<p>
Herecast nezapírá, že je spíše pro zábavu. Profi využití si ani nedovedu představit, vyjma toho Legolandu. Herecast nadšeně popisuje, jaké location based hry se budou dát hrát - jenže je zatím nikdo nenaprogramoval. A navíc české hotspoty v databázi nejsou, což má ale snadnou pomoc, pokud byste někdo chtěl rozšiřovat Herecast do ČR, napište mi a já vám databázi hotspotů vyexportuji.
</p>