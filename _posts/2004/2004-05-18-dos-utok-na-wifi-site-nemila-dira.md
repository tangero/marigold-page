---
ID: 1042
author: Patrick Zandl
layout: post
oldlink: 'https://www.marigold.cz/item/dos-utok-na-wifi-site-nemila-dira

  '
post_date: 2004-05-18 17:58:00
post_excerpt: ''
published: true
summary_points:
- WiFi díra umožňuje vyřadit 802.11b zařízení z činnosti zneužitím protokolu.
- DSSS technologie je zranitelná, útok spočívá ve vysílání falešných CCA signálů.
- Oprava vyžaduje změnu standardu 802.11b, což často znamená výměnu hardware.
- Útok zastaví síť, ale neprolamuje hesla ani neumožňuje průnik do sítě.
title: DoS útok na WiFi sítě – nemilá díra
---

<p>
Ve <STRONG>WiFi se objevila nepříjemná díra</STRONG>, která umožňuje zaútočit vůči libovolnému 802.11b zařízení a prakticky jej vyřadit z činnosti. Tato díra není žádnou specifickou implementační chybou, prostě jde o jistou nedomyšlenost v protokolu a nelze tedy aplikovat žádný patch. To je velmi nepříjemné, protože chyba je zde a ví se o ní. </p>

<p>
Problém se objevuje <STRONG>u technologie přímé sekvence (DSSS), </STRONG>nezasahuje tedy ani FH (to jsou u WiFi rychlosti do 2 Mb/s) ani OFDM (802.11g - tedy vše nad 11 Mb/s). Problém je přímo v implementaci fyzické vrstvy,konkrétně pak v práci s CSMA/CA, kolizním systémem, jenž zajišťuje, aby dvě WiFi zařízení nevysílala najednou.&#160;Informaci o zaneprázdnění kanálu&#160;předává procedura Clear Channel Assessment (CCA). Pokud nějaké WiFi zařízení svévolně vysílá informaci o obsazení kanálu pomocí CCA, myslí si všechna zařízení, že síť je plně obsazena a nepřenášejí. To se samozřejmě dotýká všech zařízení v dosahu. Podrobnější popis chyby najdete zde <A href="http://www.auscert.org.au/render.html?it=4091" target=_blank>na AusCERT</A>.</p>

<p>
<STRONG>Několik závěrů:</STRONG> </p>

<OL>
<LI>nedá se s tím prakticky nic dělat, odstranění chyby znamená změnu v 802.11b standardu, což se mnohdy neobejde bez výměny hardware. </LI>
<LI>nepříjemné je, že se to týká všech zařízení a že k útoku lze použít prakticky libovolné zařízení a jednoduchý software. Napadená síť se přitom prakticky zastaví. </LI>
<LI>není potřeba fyzický přístup k napadenému zařízení, stačí vysílat dostatečně silný radiový signál s falešným CCA. </LI>
<LI>problém se netýká 802.11g a 802.11a sítí - u géčka pozor, musí běžet nad 11 Mb/s, kde se uplatní OFDM. </LI>
<LI>útok nemá jiné následky, než přímo související s přerušením spojení. Nedochází k prolomení hesel, průniku do sítě ani na servery atd. </LI>
<LI>útok nemůže být proveden po internetu, zařízení musí být v radiovém dosahu. </LI></OL>
<p>
Další článek najdete například <A href="http://www.eweek.com/article2/0,1759,1591992,00.asp" target=_blank>na eWeek.com</A>. Aha a tady je to <A href="http://www.zive.cz/h/Viryabezpecnost/AR.asp?PG=1&amp;ARI=116454&amp;CAI=2156" target=_blank>na Živě</A>.</p>